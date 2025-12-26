# window.py
#
# Copyright 2025 Lucas Loura
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw, Gtk, Gio, GLib
import random
import gettext
import os

# import all available modes & all available moves
from .game_logic.modes import AVAILABLE_MODES, ALL_POSSIBLE_MOVES

# import ui widgets
from .ui.widgets import ClassicView, RpslsView
from .ui.how_to_play import HowToPlayDialog

@Gtk.Template(resource_path='/io/github/lloura/DuelPy/window.ui')
class DuelpyWindow(Adw.ApplicationWindow):
    __gtype_name__ = "DuelpyWindow"

    # localization setup
    localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
    gettext.bindtextdomain('io.github.lloura.DuelPy', localedir)
    gettext.textdomain('io.github.lloura.DuelPy')

    _ = gettext.gettext

    # template children
    navigation_view = Gtk.Template.Child()
    mode_stack = Gtk.Template.Child()
    img_player_choice = Gtk.Template.Child()
    img_computer_choice = Gtk.Template.Child()
    lbl_result = Gtk.Template.Child()
    lbl_explanation = Gtk.Template.Child()
    mode_label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.settings = Gio.Settings.new("io.github.lloura.DuelPy")

        # loads default or currently saved mode
        saved_mode_id = self.settings.get_string("game-mode") or "rpsls"
        self.current_game_mode = AVAILABLE_MODES.get(saved_mode_id, AVAILABLE_MODES["rpsls"])

        self.create_game_actions()

        # monitor mode changes in the stack
        self.mode_stack.connect("notify::visible-child-name", self.on_mode_changed)

        # apply initial ui state
        self.mode_stack.set_visible_child_name(self.current_game_mode.id)
        self.sync_mode_ui()

    def create_game_actions(self):
        """initialize all window actions and shortcuts"""
        # gameplay actions

        for move in ALL_POSSIBLE_MOVES:
            idx = ALL_POSSIBLE_MOVES.index(move) + 1
            self.create_action(move, self.on_play, move, [str(idx), f"KP_{idx}"])

        # system actions
        self.create_action("retry", self.on_retry, shortcuts=["<Ctrl>R"])
        self.create_action("show-help-overlay", self.on_show_shortcuts, shortcuts=["<Ctrl>question"])
        self.create_action("how-to-play", self.on_how_to_play, shortcuts=["<Ctrl>H"])

        # mode change action (stateful)
        mode_action = Gio.SimpleAction.new_stateful(
            "change-mode",
            GLib.VariantType.new('s'),
            GLib.Variant('s', self.current_game_mode.id)
        )
        mode_action.connect("activate", self.on_change_mode_activated)
        self.add_action(mode_action)

        # global accels for mode switching
        app = self.get_application()
        app.set_accels_for_action("win.change-mode('rpsls')", ["<Ctrl><Shift>R"])
        app.set_accels_for_action("win.change-mode('classic')", ["<Ctrl><Shift>C"])

    def create_action(self, name, callback, parameter=None, shortcuts=None):
        """helper to create SimpleActions quickly"""
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", lambda a, v: callback(parameter) if parameter else callback())
        self.add_action(action)
        if shortcuts:
            self.get_application().set_accels_for_action(f"win.{name}", shortcuts)

    # --- sync logic ---

    def on_mode_changed(self, stack, param):
        """ensures the app behaves correctly when switching modes"""
        mode_id = stack.get_visible_child_name()
        self.current_game_mode = AVAILABLE_MODES[mode_id]
        self.settings.set_string("game-mode", mode_id)
        self.sync_mode_ui()

        if self.navigation_view.get_visible_page_tag() == "results":
            self.navigation_view.pop()

    def sync_mode_ui(self):
        """updates icons, labels and enables/disables shortcuts"""
        self.mode_label.set_label(_(self.current_game_mode.name))
        self.mode_label.set_icon_name(self.current_game_mode.icon)

        # enable only the keys allowed in the current mode
        for move in ALL_POSSIBLE_MOVES:
            action = self.lookup_action(move)
            if action:
                action.set_enabled(move in self.current_game_mode.choices)

    # --- game logic ---

    def on_play(self, player_choice):
        # the computer can only choose options available in the current game mode
        computer_choice = random.choice(self.current_game_mode.choices)

        # verifies winner using now modularized method
        result = self.current_game_mode.check_winner(player_choice, computer_choice)

        # defines text and explanation
        match (result):
            case('tie'):
                result_text = _("Draw!")
                explanation = _("it's a tie!")
            case('player'):
                result_text = _("You Won!")
                explanation = _(self.current_game_mode.get_explanation(player_choice, computer_choice))
            case('computer'):
                result_text = _("You Lost!")
                explanation = _(self.current_game_mode.get_explanation(computer_choice, player_choice))

        self.img_player_choice.set_from_icon_name(player_choice)
        self.img_computer_choice.set_from_icon_name(computer_choice)
        self.lbl_result.set_text(result_text)
        self.lbl_explanation.set_text(explanation)

        if self.navigation_view.get_visible_page_tag() != "results":
            self.navigation_view.push_by_tag("results")

    # --- ui callbacks ---

    def on_change_mode_activated(self, action, parameter):
        mode = parameter.get_string()
        action.set_state(parameter)
        self.mode_stack.set_visible_child_name(mode)

    def on_retry(self):
        if self.navigation_view.get_visible_page_tag() == "results":
            self.navigation_view.pop()

    def on_show_shortcuts(self):
        current_view = self.mode_stack.get_visible_child()
        dialog = getattr(current_view, 'shortcuts_dialog', None)

        if dialog:
            dialog.present(self)
        else:
            print("error: dialog not found on current view")

    def on_how_to_play(self):
        dialog = HowToPlayDialog(mode=self.current_game_mode)
        dialog.present(self)
