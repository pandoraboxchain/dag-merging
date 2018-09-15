class Block:

    def __init__(self, timeslot, identifier, is_empty, is_immutable):
        self.timeslot = timeslot
        self.identifier = identifier
        self.is_empty = is_empty
        self.is_immutable = is_immutable

class Chain(list):
    pass

def merge(chains):
    pass