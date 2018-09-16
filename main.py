import random

class Block:

    def __init__(self, timeslot, identifier, is_empty, is_immutable):
        self.timeslot = timeslot
        self.identifier = identifier
        self.is_empty = is_empty
        self.is_immutable = is_immutable

class Chain(list):

    def get_chain_size(self):
        r = 0
        for item in self:
            if not item.is_empty:
                r+=1
        return r

    def get_diff(self, another):
        i = 0
        while i != min(len(self), len(another)) and (not stop):
            eq = self.timeslot==another.timeslot
            eq = eq and (self.identifier==another.identifier)
            eq = eq and (self.is_empty==another.is_empty)
            eq = eq and (self.is_immutable==another.is_immutable)
            stop = not eq
            if not stop:
                i+=1
        dpoint = i
        mx = max(len(self), len(another))
        return {
            0: self[dpoint:m],
            1: self[dpoint:m],
        }

    def get_merging_point(self):
        while i != len(self) and (not stop):
            stop = not self[i].is_immutable
            if not stop:
                i+=1
        mpoint = i
        return mpoint


def merge(chains):
    sizes = [chain.get_chain_size() for chain in chains]
    dict_sizes = enumerate(sizes)
    deterministic_ordering = []
    while dict_sizes:
        m = max(dict_sizes.values())
        indexes = [key for key,value in dict_sizes.items() if value==m]
        if len(indexes)==1:
            dict_sizes.pop(indexes[0])
            deterministic_ordering.append(indexes[0])
        else:
            for item in indexes:
                dict_sizes.pop(item)
            random.shuffle(indexes)
            deterministic_ordering += indexes

    active = deterministic_ordering[0]
    mp = active.get_merging_point()

    return deterministic_ordering
