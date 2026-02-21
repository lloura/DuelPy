# game_logic/modes.py
#
# Copyright 2025-2026 Lucas Loura
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
        "rock": ["scissors", "sponge", "fire"],
        "paper": ["rock", "water", "air"],
        "scissors": ["paper", "sponge", "air"],
        "sponge": ["paper", "water", "air"],
        "fire": ["paper", "scissors", "sponge"],
        "water": ["rock", "scissors", "fire"],
        "air": ["rock", "fire", "water"],
    },
    explanations={
        ("rock", "scissors"): _("Rock breaks Scissors!"),
        ("rock", "sponge"): _("Rock crushes Sponge!"),
        ("rock", "fire"): _("Rock pounds out Fire!"),
        ("paper", "rock"): _("Paper covers Rock!"),
        ("paper", "water"): _("Paper floats on Water!"),
        ("paper", "air"): _("Paper fans Air!"),
        ("scissors", "paper"): _("Scissors cuts Paper!"),
        ("scissors", "sponge"): _("Scissors cuts Sponge!"),
        ("scissors", "air"): _("Scissors swishes through Air!"),
        ("sponge", "paper"): _("Sponge soaks Paper!"),
        ("sponge", "water"): _("Sponge absorbs Water!"),
        ("sponge", "air"): _("Sponge uses Air pockets!"),
        ("fire", "paper"): _("Fire burns Paper!"),
        ("fire", "scissors"): _("Fire melts Scissors!"),
        ("fire", "sponge"): _("Fire burns Sponge!"),
        ("water", "rock"): _("Water erodes Rock!"),
        ("water", "scissors"): _("Water rusts Scissors!"),
        ("water", "fire"): _("Water puts out Fire!"),
        ("air", "rock"): _("Air erodes Rock!"),
        ("air", "fire"): _("Air blows out Fire!"),
        ("air", "water"): _("Air evaporates Water!"),
    }
)

# --- rps9 mode ---
rps9_mode = GameMode(
    id="rps9",
    name=_("RPS-9"),
    icon="gun-symbolic",
    diagram="diagram-rps9",
    choices=["rock","paper","scissors","sponge","fire","water","air","human","gun"],
    wins_map={
        "rock": ["scissors", "sponge", "fire", "human"],
        "paper": ["rock", "water", "air", "gun"],
        "scissors": ["paper", "sponge", "air", "human"],
        "sponge": ["paper", "water", "air", "gun"],
        "fire": ["paper", "scissors", "sponge", "human"],
        "water": ["rock", "scissors", "fire", "gun"],
        "air": ["rock", "fire", "water", "gun"],
        "human": ["paper", "sponge", "water", "air"],
        "gun": ["rock", "scissors", "fire", "human"],
    },
    explanations={
        ("rock", "scissors"): _("Rock breaks Scissors!"),
        ("rock", "sponge"): _("Rock crushes Sponge!"),
        ("rock", "fire"): _("Rock pounds out Fire!"),
        ("rock", "human"): _("Rock crushes Human!"),
        ("paper", "rock"): _("Paper covers Rock!"),
        ("paper", "water"): _("Paper floats on Water!"),
        ("paper", "air"): _("Paper fans Air!"),
        ("paper", "gun"): _("Paper outlaws Gun!"),
        ("scissors", "paper"): _("Scissors cuts Paper!"),
        ("scissors", "sponge"): _("Scissors cuts Sponge!"),
        ("scissors", "air"): _("Scissors swishes through Air!"),
        ("scissors", "human"): _("Scissors cuts Human!"),
        ("sponge", "paper"): _("Sponge soaks Paper!"),
        ("sponge", "water"): _("Sponge absorbs Water!"),
        ("sponge", "air"): _("Sponge uses Air pockets!"),
        ("sponge", "gun"): _("Sponge cleans Gun!"),
        ("fire", "paper"): _("Fire burns Paper!"),
        ("fire", "scissors"): _("Fire melts Scissors!"),
        ("fire", "sponge"): _("Fire burns Sponge!"),
        ("fire", "human"): _("Fire burns Human!"),
        ("water", "rock"): _("Water erodes Rock!"),
        ("water", "scissors"): _("Water rusts Scissors!"),
        ("water", "fire"): _("Water puts out Fire!"),
        ("water", "gun"): _("Water rusts Gun!"),
        ("air", "rock"): _("Air erodes Rock!"),
        ("air", "fire"): _("Air blows out Fire!"),
        ("air", "water"): _("Air evaporates Water!"),
        ("air", "gun"): _("Air tarnishes Gun!"),
        ("human", "paper"): _("Human writes on Paper!"),
        ("human", "sponge"): _("Human cleans with Sponge!"),
        ("human", "water"): _("Human drinks Water!"),
        ("human", "air"): _("Human breathes Air!"),
        ("gun", "rock"): _("Gun targets Rock!"),
        ("gun", "scissors"): _("Gun outclasses Scissors!"),
        ("gun", "fire"): _("Gun Fires!"),
        ("gun", "human"): _("Gun shoots Human!"),
    }
)

# central modes registry
AVAILABLE_MODES = {
    "rpsls": rpsls_mode,
    "classic": classic_mode,
    "rps7": rps7_mode,
    "rps9": rps9_mode,
}

# lists all possible moves
ALL_POSSIBLE_MOVES = [
    "rock", "paper", "scissors",
    "lizard", "spock",
    "sponge", "fire", "water", "air",
    "human", "gun",
]
