class RulesOfGame:

    """
        Metoda zwraca true, tylko gdy przejscie z polozenia source na destination w jednym ruchu jest zgodne
        z zasadami gry w szachy.
    """
    def is_correct_move(self, source, destination):
        raise NotImplementedError("Subclasses must implement this method")

class Bishop(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        return abs(source_col - dest_col) == abs(source_row - dest_row) and source != destination

class Knight(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False

        source_col, source_row = source
        dest_col, dest_row = destination

        dx = abs(source_col - dest_col)
        dy = abs(source_row - dest_row)

        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

class King(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False

        source_col, source_row = source
        dest_col, dest_row = destination

        dx = abs(source_col - dest_col)
        dy = abs(source_row - dest_row)

        return (dx <= 1 and dy <= 1) and source != destination

class Queen(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False

        source_col, source_row = source
        dest_col, dest_row = destination

        diagonal_move = abs(source_col - dest_col) == abs(source_row - dest_row)
        straight_move = (source_col == dest_col or source_row == dest_row)

        return (diagonal_move or straight_move) and source

class Rook(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False

        source_col, source_row = source
        dest_col, dest_row = destination

        dx = abs(source_col - dest_col)
        dy = abs(source_row - dest_row)

        m1 = (dx != 0 and dy == 0)
        m2 = (dy != 0 and dx == 0)

        return m1 or m2

class Pawn(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False

        source_col, source_row = source
        dest_col, dest_row = destination



        if source_col == dest_col and dest_row == source_row + 1:
            return True

        if source_row == 2 and source_col == dest_col and dest_row == 4:
            return True

        return False
