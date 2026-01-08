# game_logic/modes.py
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

from .rules import GameMode
from . import _

# --- rpsls mode ---
rpsls_mode = GameMode(
    id="rpsls",
    name=_("RPSLS"),
    icon="spock-symbolic",
    diagram="diagram-rpsls",
    choices=["rock", "paper", "scissors", "lizard", "spock"],
    wins_map={
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"],
    },
    explanations={
        ("rock", "scissors"): _("Rock breaks Scissors!"),
        ("rock", "lizard"): _("Rock crushes Lizard!"),
        ("paper", "rock"): _("Paper covers Rock!"),
        ("paper", "spock"): _("Paper disproves Spock!"),
        ("scissors", "paper"): _("Scissors cuts Paper!"),
        ("scissors", "lizard"): _("Scissors decapitates Lizard!"),
        ("lizard", "spock"): _("Lizard poisons Spock!"),
        ("lizard", "paper"): _("Lizard eats Paper!"),
        ("spock", "scissors"): _("Spock breaks Scissors!"),
        ("spock", "rock"): _("Spock vaporizes Rock!"),
    }
)

# --- classic mode ---
classic_mode = GameMode(
    id="classic",
    name=_("Classic"),
    icon="scissors-symbolic",
    diagram="diagram-classic",
    choices=["rock", "paper", "scissors"],
    wins_map={
        "rock": ["scissors"],
        "paper": ["rock"],
        "scissors": ["paper"],
    },
    explanations={
        ("rock", "scissors"): _("Rock breaks Scissors!"),
        ("paper", "rock"): _("Paper covers Rock!"),
        ("scissors", "paper"): _("Scissors cuts Paper!"),
    }
)

# --- rps7 mode ---
rps7_mode = GameMode(
    id="rps7",
    name=_("RPS-7"),
    icon="air-symbolic",
    diagram="diagram-rps7",
    choices=["rock","paper","scissors","sponge","fire","water","air"],
    wins_map={
        "rock": ["fire", "scissors", "sponge"],
        "paper": ["air", "rock", "water"],
        "scissors": ["air", "paper", "sponge"],
        "sponge": ["paper", "air", "water"],
        "fire": ["scissors", "paper", "sponge"],
        "water": ["rock", "fire", "scissors"],
        "air": ["fire", "rock", "water"],
    },
    explanations={
        ("rock", "fire"): _("Rock pounds out Fire!"),
        ("rock", "scissors"): _("Rock breaks Scissors!"),
        ("rock", "sponge"): _("Rock crushes Sponge!"),
        ("paper", "air"): _("Paper fans Air!"),
        ("paper", "rock"): _("Paper covers Rock!"),
        ("paper", "water"): _("Paper floats on Water!"),
        ("scissors", "air"): _("Scissors swishes through Air!"),
        ("scissors", "paper"): _("Scissors cuts Paper!"),
        ("scissors", "sponge"): _("Scissors cuts Sponge!"),
        ("sponge", "paper"): _("Sponge soaks Paper!"),
        ("sponge", "air"): _("Sponge uses Air pockets!"),
        ("sponge", "water"): _("Sponge absorbs Water!"),
        ("fire", "scissors"): _("Fire melts Scissors!"),
        ("fire", "paper"): _("Fire burns Paper!"),
        ("fire", "sponge"): _("Fire burns Sponge!"),
        ("water", "rock"): _("Water erodes Rock!"),
        ("water", "fire"): _("Water puts out Fire!"),
        ("water", "scissors"): _("Water rusts Scissors!"),
        ("air", "fire"): _("Air blows out Fire!"),
        ("air", "rock"): _("Air erodes Rock!"),
        ("air", "water"): _("Air evaporates Water!"),
    }
)

# central modes registry
AVAILABLE_MODES = {
    "rpsls": rpsls_mode,
    "classic": classic_mode,
    "rps7": rps7_mode,
}

# lists all possible moves
ALL_POSSIBLE_MOVES = [
    "rock", "paper", "scissors",
    "lizard", "spock",
    "sponge", "fire", "water", "air",
]
