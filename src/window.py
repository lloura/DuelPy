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

from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import Gio
import random

import gettext

_ = gettext.gettext

@Gtk.Template(resource_path='/io/github/lloura/DuelPy/window.ui')
class DuelpyWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'DuelpyWindow'

    navigation_view = Gtk.Template.Child()
    img_player_choice = Gtk.Template.Child()
    img_computer_choice = Gtk.Template.Child()
    lbl_result = Gtk.Template.Child()
    lbl_explanation = Gtk.Template.Child()

    shortcuts_dialog = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.create_action('rock', self.on_play, 'Rock', ['1'])
        self.create_action('paper', self.on_play, 'Paper', ['2'])
        self.create_action('scissors', self.on_play, 'Scissors', ['3'])
        self.create_action('lizard', self.on_play, 'Lizard', ['4'])
        self.create_action('spock', self.on_play, 'Spock', ['5'])
        self.create_action('retry', self.on_retry, shortcuts=['<Ctrl>R'])

        self.create_action('show-help-overlay', self.on_show_shortcuts, shortcuts=['<Ctrl>question'])

    def create_action(self, name, callback, parameter=None, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect(
            "activate",
            lambda action, _: callback(parameter) if parameter else callback()
        )
        self.add_action(action)

        if shortcuts:
            app = self.get_application()
            app.set_accels_for_action(f"win.{name}", shortcuts)

    def on_play(self, player_choice):
        choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        computer_choice = random.choice(choices)

        result = self.determine_winner(player_choice, computer_choice)

        self.img_player_choice.set_from_icon_name(player_choice.lower())
        self.img_computer_choice.set_from_icon_name(computer_choice.lower())

        self.lbl_result.set_text(result)
        self.lbl_explanation.set_text(self.get_explanation(player_choice, computer_choice))

        if self.navigation_view.get_visible_page_tag() != "results":
            self.navigation_view.push_by_tag("results")

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return _("Draw!")

        wins = {
            'Rock': ['Scissors', 'Lizard'],
            'Paper': ['Rock', 'Spock'],
            'Scissors': ['Paper', 'Lizard'],
            'Lizard': ['Spock', 'Paper'],
            'Spock': ['Scissors', 'Rock']
        }

        if computer_choice in wins[player_choice]:
            return _("You Won!")
        else:
            return _("You Lost!")

    def get_explanation(self, player_choice, computer_choice):
        if (player_choice == computer_choice):
            return player_choice + " " + _("evens out with") + " " + computer_choice + "!"

        match(player_choice):
            case "Rock":
                if (computer_choice == "Scissors" or computer_choice == "Lizard"):
                    return player_choice + " " + _("smashes") + " " + computer_choice + "!"
                if (computer_choice == "Paper"):
                    return player_choice + " " + _("gets covered by") + " " + computer_choice + "!"
                if (computer_choice == "Spock"):
                    return player_choice + " " + _("gets vaporized by") + " " + computer_choice + "!"
            case "Paper":
                if (computer_choice == "Rock"):
                    return player_choice + " " + _("covers") + " " + computer_choice + "!"
                if (computer_choice == "Spock"):
                    return player_choice + " " + _("disproves") + " " + computer_choice + "!"
                if (computer_choice == "Scissors"):
                    return player_choice + " " + _("gets cut by") + " " + computer_choice + "!"
                if (computer_choice == "Lizard"):
                    return player_choice + " " + _("gets eaten by") + " " + computer_choice + "!"
            case "Scissors":
                if (computer_choice == "Paper"):
                    return player_choice + " " + _("cuts") + " " + computer_choice + "!"
                if (computer_choice == "Lizard"):
                    return player_choice + " " + _("decapitates") + " " + computer_choice + "!"
                if (computer_choice == "Rock" or computer_choice == "Spock"):
                    return player_choice + " " + _("gets smashed by") + " " + computer_choice + "!"
            case "Lizard":
                if (computer_choice == "Paper"):
                    return player_choice + " " + _("eats") + " " + computer_choice + "!"
                if (computer_choice == "Spock"):
                    return player_choice + " " + _("poisons") + " " + computer_choice + "!"
                if (computer_choice == "Scissors"):
                    return player_choice + " " + _("gets decapitated by") + " " + computer_choice + "!"
                if (computer_choice == "Rock"):
                    return player_choice + " " + _("gets smashed by") + " " + computer_choice + "!"
            case "Spock":
                if (computer_choice == "Rock"):
                    return player_choice + " " + _("vaporizes") + " " + computer_choice + "!"
                if (computer_choice == "Scissors"):
                    return player_choice + " " + _("smashes") + " " + computer_choice + "!"
                if (computer_choice == "Paper"):
                    return player_choice + " " + _("gets disproven by") + " " + computer_choice + "!"
                if (computer_choice == "Lizard"):
                    return player_choice + " " + _("gets poisoned by") + " " + computer_choice + "!"

    def on_retry(self):
        if self.navigation_view.get_visible_page_tag() == "results":
            self.navigation_view.pop()

    def on_show_shortcuts(self):
        self.shortcuts_dialog.present(self)

