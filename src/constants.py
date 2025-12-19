import gettext

_ = gettext.gettext

GAME_RULES = {
    "classic": {
        "name": _("Classic"),
        "icon": "scissors-symbolic",
        "choices": ["rock", "paper", "scissors"],
        "wins": {
            "rock": ["scissors"],
            "paper": ["rock"],
            "scissors": ["paper"],
        }
    },
    "rpsls": {
        "name": _("RPSLS"),
        "icon": "spock-symbolic",
        "choices": ["rock", "paper", "scissors", "lizard", "spock"],
        "wins": {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
            "scissors": ["paper", "lizard"],
            "lizard": ["spock", "paper"],
            "spock": ["scissors", "rock"],
        }
    }
}

ALL_POSSIBLE_MOVES = ["rock", "paper", "scissors", "lizard", "spock"]
