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

@Gtk.Template(resource_path='/io/github/lloura/DuelPy/window.ui')
class DuelpyWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'DuelpyWindow'

    navigation_view = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.create_action('rock', self.on_play, 'rock')
        self.create_action('paper', self.on_play, 'paper')
        self.create_action('scissors', self.on_play, 'scissors')
        self.create_action('lizard', self.on_play, 'lizard')
        self.create_action('spock', self.on_play, 'spock')
        self.create_action('retry', self.on_retry)

    def create_action(self, name, callback, parameter=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', lambda action, _: callback(parameter) if parameter else callback())
        self.add_action(action)

    def on_play(self, player_choice):
        choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        computer_choice = random.choice(choices)

        result = self.determine_winner(player_choice, computer_choice)

        print(f"player_choice: {player_choice}")
        print(f"computer_choice: {computer_choice}")
        print(f"result: {result}")

        self.navigation_view.push_by_tag("results")

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return 'Draw!'

        wins = {
            'rock': ['scissors', 'lizard'],
            'paper': ['rock', 'spock'],
            'scissors': ['paper', 'lizard'],
            'lizard': ['spock', 'paper'],
            'spock': ['scissors', 'rock']
        }

        if computer_choice in wins[player_choice]:
            return "You Won!"
        else:
            return "You Lost!"

    def on_retry(self):
        self.navigation_view.pop()
