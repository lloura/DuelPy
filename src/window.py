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

def translate_choice(choice):
    translations = {
        'Rock': _('Rock'),
        'Paper': _('Paper'),
        'Scissors': _('Scissors'),
        'Lizard': _('Lizard'),
        'Spock': _('Spock')
    }

    return translations.get(choice, choice)

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
        player = translate_choice(player_choice)
        computer = translate_choice(computer_choice)

        if (player_choice == computer_choice):
            return f"{player} {_('evens out with')} {computer}!"

        match(player_choice):
            case "Rock":
                if (computer_choice == "Scissors" or computer_choice == "Lizard"):
                    return f"{player} {_('smashes')} {computer}!"
                if (computer_choice == "Paper"):
                    return f"{player} {_('gets covered by')} {computer}!"
                if (computer_choice == "Spock"):
                    return f"{player} {_('gets vaporized by')} {computer}!"
            case "Paper":
                if (computer_choice == "Rock"):
                    return f"{player} {_('covers')} {computer}!"
                if (computer_choice == "Spock"):
                    return f"{player} {_('disproves')} {computer}!"
                if (computer_choice == "Scissors"):
                    return f"{player} {_('gets cut by')} {computer}!"
                if (computer_choice == "Lizard"):
                    return f"{player} {_('gets eaten by')} {computer}!"
            case "Scissors":
                if (computer_choice == "Paper"):
                    return f"{player} {_('cuts')} {computer}!"
                if (computer_choice == "Lizard"):
                    return f"{player} {_('decapitates')} {computer}!"
                if (computer_choice == "Rock" or computer_choice == "Spock"):
                    return f"{player} {_('gets smashed by')} {computer}!"
            case "Lizard":
                if (computer_choice == "Paper"):
                    return f"{player} {_('eats')} {computer}!"
                if (computer_choice == "Spock"):
                    return f"{player} {_('poisons')} {computer}!"
                if (computer_choice == "Scissors"):
                    return f"{player} {_('gets decapitated by')} {computer}!"
                if (computer_choice == "Rock"):
                    return f"{player} {_('gets smashed by')} {computer}!"
            case "Spock":
                if (computer_choice == "Rock"):
                    return f"{player} {_('vaporizes')} {computer}!"
                if (computer_choice == "Scissors"):
                    return f"{player} {_('smashes')} {computer}!"
                if (computer_choice == "Paper"):
                    return f"{player} {_('gets disproven by')} {computer}!"
                if (computer_choice == "Lizard"):
                    return f"{player} {_('gets poisoned by')} {computer}!"

    def on_retry(self):
        if self.navigation_view.get_visible_page_tag() == "results":
            self.navigation_view.pop()

    def on_show_shortcuts(self):
        self.shortcuts_dialog.present(self)
