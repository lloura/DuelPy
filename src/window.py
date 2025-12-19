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
import os

@Gtk.Template(resource_path='/io/github/lloura/DuelPy/window.ui')
class DuelpyWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'DuelpyWindow'

    localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')

    gettext.bindtextdomain('io.github.lloura.DuelPy', localedir)
    gettext.textdomain('io.github.lloura.DuelPy')
    _ = gettext.gettext

    navigation_view = Gtk.Template.Child()
    img_player_choice = Gtk.Template.Child()
    img_computer_choice = Gtk.Template.Child()
    lbl_result = Gtk.Template.Child()
    lbl_explanation = Gtk.Template.Child()

    shortcuts_dialog = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.create_action('rock', self.on_play, 'rock', ['1','KP_1'])
        self.create_action('paper', self.on_play, 'paper', ['2','KP_2'])
        self.create_action('scissors', self.on_play, 'scissors', ['3','KP_3'])
        self.create_action('lizard', self.on_play, 'lizard', ['4','KP_4'])
        self.create_action('spock', self.on_play, 'spock', ['5','KP_5'])
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
        choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
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
            'rock': ['scissors', 'lizard'],
            'paper': ['rock', 'spock'],
            'scissors': ['paper', 'lizard'],
            'lizard': ['spock', 'paper'],
            'spock': ['scissors', 'rock']
        }

        if computer_choice in wins[player_choice]:
            return _("You Won!")
        else:
            return _("You Lost!")

    def get_explanation(self, player_choice, computer_choice):
        match(player_choice, computer_choice):
            case ("rock", "rock"):
                return _("Rock evens out with Rock!")
            case ("rock", "paper"):
                return _("Rock gets covered by Paper!")
            case ("rock", "scissors"):
                return _("Rock smashes Scissors!")
            case ("rock", "lizard"):
                return _("Rock smashes Lizard!")
            case ("rock", "spock"):
                return _("Rock gets vaporized by Spock!")

            case ("paper", "rock"):
                return _("Paper covers Rock!")
            case ("paper", "paper"):
                return _("Paper evens out with Paper!")
            case ("paper", "scissors"):
                return _("Paper gets cut by Scissors!")
            case ("paper", "lizard"):
                return _("Paper gets eaten by Lizard!")
            case ("paper", "spock"):
                return _("Paper disproves Spock!")

            case ("scissors","rock"):
                return _("Scissors gets smashed by Rock!")
            case ("scissors","paper"):
                return _("Scissors cuts Paper!")
            case ("scissors","scissors"):
                return _("Scissors evens out with Scissors!")
            case ("scissors","lizard"):
                return _("Scissors decapitates Lizard!")
            case ("scissors","spock"):
                return _("Scissors gets smashed by Spock!")

            case ("lizard","rock"):
                return _("Lizard gets smashed by Rock!")
            case ("lizard","paper"):
                return _("Lizard eats Paper!")
            case ("lizard","scissors"):
                return _("Lizard gets decapitated by Scissors!")
            case ("lizard","lizard"):
                return _("Lizard evens out with Lizard!")
            case ("lizard","spock"):
                return _("Lizard poisons Spock!")

            case ("spock", "rock"):
                return _("Spock vaporizes Rock!")
            case ("spock", "paper"):
                return _("Spock gets disproven by Paper!")
            case ("spock", "scissors"):
                return _("Spock smashes Scissors!")
            case ("spock", "lizard"):
                return _("Spock gets poisoned by Lizard!")
            case ("spock", "spock"):
                return _("Spock evens out with Spock!")

        return ""

    def on_retry(self):
        if self.navigation_view.get_visible_page_tag() == "results":
            self.navigation_view.pop()

    def on_show_shortcuts(self):
        self.shortcuts_dialog.present(self)
