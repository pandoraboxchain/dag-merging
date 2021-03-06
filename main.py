import random

class Block:

    def __init__(self, timeslot, identifier, is_empty, is_immutable):
        self.timeslot = timeslot
        self.identifier = identifier
        self.is_empty = is_empty
        self.is_immutable = is_immutable

class Chain(list):

    def __init__(self, l):
        for i in l:
            self.append(i)

    def get_chain_size(self):
        r = 0
        for item in self:
            if not item.is_empty:
                r+=1
        return r

    def get_diff(self, another):
        i = 0
        stop = False
        while i != min(len(self), len(another)) and (not stop):
            eq = self[i].timeslot==another[i].timeslot
            eq = eq and (self[i].identifier==another[i].identifier)
            eq = eq and (self[i].is_empty==another[i].is_empty)
            eq = eq and (self[i].is_immutable==another[i].is_immutable)
            stop = not eq
            if not stop:
                i+=1
        dpoint = i
        return {
            0: Chain(self[dpoint:]),
            1: Chain(another[dpoint:]),
        }

    def get_merging_point(self):
        i = 0
        stop = False
        while i != len(self) and (not stop):
            stop = not self[i].is_immutable
            if not stop:
                i+=1
        mpoint = i
        return mpoint

    def find_block_by_identifier(self, identifier):
        res = [item for item in self if item.identifier==identifier]
        if res:
            return res[0]
        else:
            return False
    
    def get_all_immutable(self):
        return [item for item in self if item.is_immutable]

    def get_all_mutable(self):
        return [item for item in self if not item.is_immutable]

def merge(chains):
    sizes = [chain.get_chain_size() for chain in chains]
    dict_sizes = dict(enumerate(sizes))
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

    active = chains[deterministic_ordering[0]]
    mp = active.get_merging_point()
    active_merged_point = Chain(active[:mp])
    merged_chain = Chain(active[:mp])

    for doi in deterministic_ordering[1:]:
        diffchain = active_merged_point.get_diff(chains[doi])[1]
        im_chain = diffchain.get_all_immutable()
        if im_chain:
            for im in im_chain:
                if not merged_chain.find_block_by_identifier(im.identifier):
                    merged_chain.append(im)
    
    for doi in deterministic_ordering:
        diffchain = active_merged_point.get_diff(chains[doi])[1]
        m_chain = diffchain.get_all_mutable()
        if m_chain:
            for m in m_chain:
                if not merged_chain.find_block_by_identifier(m.identifier):
                    merged_chain.append(m)

    return {
        "deterministic_ordering": deterministic_ordering,
        "merged_chain": merged_chain,
    }
