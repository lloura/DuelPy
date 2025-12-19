# window.py
# Copyright 2025 Lucas Loura
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw, Gtk, Gio, GLib
import random
import gettext
import os

# import our constants
from .constants import GAME_RULES, ALL_POSSIBLE_MOVES

@Gtk.Template(resource_path='/io/github/lloura/DuelPy/window.ui')
class DuelpyWindow(Adw.ApplicationWindow):
    __gtype_name__ = "DuelpyWindow"

    # localization setup
    localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
    gettext.bindtextdomain('io.github.lloura.DuelPy', localedir)
    gettext.textdomain('io.github.lloura.DuelPy')

    # we use staticmethod to prevent Python from passing 'self' to gettext
    _ = staticmethod(gettext.gettext)

    # template children
    navigation_view = Gtk.Template.Child()
    mode_stack = Gtk.Template.Child()
    img_player_choice = Gtk.Template.Child()
    img_computer_choice = Gtk.Template.Child()
    lbl_result = Gtk.Template.Child()
    lbl_explanation = Gtk.Template.Child()
    mode_label = Gtk.Template.Child()
    shortcuts_dialog = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.settings = Gio.Settings.new("io.github.lloura.DuelPy")
        self.create_game_actions()

        # monitor mode changes in the stack
        self.mode_stack.connect("notify::visible-child-name", self.on_mode_changed)

        # restore saved mode and apply initial action states
        saved_mode = self.settings.get_string("game-mode")
        if saved_mode in GAME_RULES:
            self.mode_stack.set_visible_child_name(saved_mode)
            self.sync_mode_ui(saved_mode)

    def create_game_actions(self):
        """Initialize all window actions and shortcuts"""
        # Gameplay actions
        self.create_action("rock", self.on_play, "rock", ["1", "KP_1"])
        self.create_action("paper", self.on_play, "paper", ["2", "KP_2"])
        self.create_action("scissors", self.on_play, "scissors", ["3", "KP_3"])
        self.create_action("lizard", self.on_play, "lizard", ["4", "KP_4"])
        self.create_action("spock", self.on_play, "spock", ["5", "KP_5"])

        # system actions
        self.create_action("retry", self.on_retry, shortcuts=["<Ctrl>R"])
        self.create_action("show-help-overlay", self.on_show_shortcuts, shortcuts=["<Ctrl>question"])

        # mode change action (Stateful)
        mode_val = self.settings.get_string("game-mode") or "rpsls"
        mode_action = Gio.SimpleAction.new_stateful(
            "change-mode",
            GLib.VariantType.new('s'),
            GLib.Variant('s', mode_val)
        )
        mode_action.connect("activate", self.on_change_mode_activated)
        self.add_action(mode_action)

        # global accels for mode switching
        app = self.get_application()
        app.set_accels_for_action("win.change-mode('rpsls')", ["<Ctrl><Shift>R"])
        app.set_accels_for_action("win.change-mode('classic')", ["<Ctrl><Shift>C"])

    def create_action(self, name, callback, parameter=None, shortcuts=None):
        """Helper to create SimpleActions quickly"""
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", lambda a, v: callback(parameter) if parameter else callback())
        self.add_action(action)
        if shortcuts:
            self.get_application().set_accels_for_action(f"win.{name}", shortcuts)

    # --- sync logic ---

    def on_mode_changed(self, stack, param):
        """Ensures the app behaves correctly when switching modes"""
        mode = stack.get_visible_child_name()
        self.settings.set_string("game-mode", mode)
        self.sync_mode_ui(mode)

        if self.navigation_view.get_visible_page_tag() == "results":
            self.navigation_view.pop()

    def sync_mode_ui(self, mode):
        """Updates icons, labels and enables/disables shortcuts"""
        rules = GAME_RULES.get(mode)
        if not rules: return

        self.mode_label.set_label(rules["name"])
        self.mode_label.set_icon_name(rules["icon"])

        # enable only the keys allowed in the current mode
        for move in ALL_POSSIBLE_MOVES:
            action = self.lookup_action(move)
            if action:
                action.set_enabled(move in rules["choices"])

    # --- game logic ---

    def on_play(self, player_choice):
        mode = self.mode_stack.get_visible_child_name()
        choices = GAME_RULES[mode]["choices"]
        computer_choice = random.choice(choices)

        result_text = self.determine_winner(mode, player_choice, computer_choice)

        self.img_player_choice.set_from_icon_name(player_choice)
        self.img_computer_choice.set_from_icon_name(computer_choice)
        self.lbl_result.set_text(result_text)
        self.lbl_explanation.set_text(self.get_explanation(player_choice, computer_choice))

        if self.navigation_view.get_visible_page_tag() != "results":
            self.navigation_view.push_by_tag("results")

    def determine_winner(self, mode, player, computer):
        if player == computer:
            return self._("Draw!")

        if computer in GAME_RULES[mode]["wins"].get(player, []):
            return self._("You Won!")
        return self._("You Lost!")

    def get_explanation(self, player, computer):
        """Returns the localized string explaining why someone won"""
        explanations = {
            ("rock", "scissors"): self._("Rock smashes Scissors!"),
            ("rock", "lizard"): self._("Rock smashes Lizard!"),
            ("paper", "rock"): self._("Paper covers Rock!"),
            ("paper", "spock"): self._("Paper disproves Spock!"),
            ("scissors", "paper"): self._("Scissors cuts Paper!"),
            ("scissors", "lizard"): self._("Scissors decapitates Lizard!"),
            ("lizard", "paper"): self._("Lizard eats Paper!"),
            ("lizard", "spock"): self._("Lizard poisons Spock!"),
            ("spock", "rock"): self._("Spock vaporizes Rock!"),
            ("spock", "scissors"): self._("Spock smashes Scissors!"),
        }

        # check both directions (player wins or computer wins)
        if player == computer:
            return self._("It's a tie!")

        return explanations.get((player, computer),
               explanations.get((computer, player), ""))

    # --- ui callbacks ---

    def on_change_mode_activated(self, action, parameter):
        mode = parameter.get_string()
        action.set_state(parameter)
        self.mode_stack.set_visible_child_name(mode)

    def on_retry(self):
        if self.navigation_view.get_visible_page_tag() == "results":
            self.navigation_view.pop()

    def on_show_shortcuts(self):
        self.shortcuts_dialog.present(self)
