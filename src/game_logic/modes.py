from .rules import GameMode
import gettext

_ = gettext.gettext

# --- rpsls mode ---
rpsls_mode = GameMode(
    id="rpsls",
    name=_("RPSLS"),
    icon="spock-symbolic",
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

# central modes registry
AVAILABLE_MODES = {
    "rpsls": rpsls_mode,
    "classic": classic_mode
}

# lists all possible moves
ALL_POSSIBLE_MOVES = ["rock", "paper", "scissors", "lizard", "spock"]
