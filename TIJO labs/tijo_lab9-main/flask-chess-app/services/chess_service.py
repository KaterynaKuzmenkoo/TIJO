import logging
from .rules_of_game import Bishop, Knight, King, Queen, Rook, Pawn

logger = logging.getLogger(__name__)


def _convert_to_point(algebraic_notation):
    sign_fields = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    number_fields = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8}

    if not algebraic_notation or len(algebraic_notation) != 3 or algebraic_notation[1] != '_':
        return None

    x_char = algebraic_notation[0].lower()
    y_char = algebraic_notation[2]

    if x_char in sign_fields and y_char in number_fields:
        x = sign_fields[x_char]
        y = number_fields[y_char]
        return x, y
    return None


class ChessService:
    def __init__(self):
        self.rules = {
            'BISHOP': Bishop(),
            'KNIGHT': Knight(),
            'ROOK':  Rook(),
            'QUEEN': Queen(),
            'KING': King(),
            'PAWN': Pawn()
        }


    def is_correct_move(self, move_data):
        source = _convert_to_point(move_data.get('source'))
        destination = _convert_to_point(move_data.get('destination'))
        figure_type = move_data.get('figureType')

        rule = self.rules.get(figure_type)
        if not rule:
            return False
        return rule.is_correct_move(source, destination)


