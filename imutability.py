def get_imutability(chain, gossips, block, dzeta, dzeta_i):
    for p in chain[chain.find_by_block():]:
        if p.is_immutable:
            return True
    gossips = gossips.by_blocks(block)

    if block.is_empty:
        return len(gossips[negative])>=(dzeta-dzeta_i+1)
    else:
        return len(gossips[positive])=>dzeta_i