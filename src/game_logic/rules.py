# game_logic/rules.py
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

import gettext
_ = gettext.gettext

class GameMode:
    def __init__(self, id, name, icon, choices, wins_map, explanations):
        self.id = id
        self.name = name
        self.icon = icon
        self.choices = choices
        self.wins_map = wins_map
        self.explanations = explanations

    def check_winner(self, player_move, computer_move):
        """returns 'player', 'computer', or 'tie'"""
        if player_move == computer_move:
            return 'tie'
        if computer_move in self.wins_map.get(player_move, []):
            return 'player'
        return 'computer'

    def get_explanation(self, winner_move, loser_move):
        """returns the localized string explaining the victory"""
        return self.explanations.get((winner_move, loser_move), "")
