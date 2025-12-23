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
