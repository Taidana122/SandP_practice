def coincidence(lst=None, rng=None):
    if lst is None or rng is None:
        return []
    
    return [x for x in lst if isinstance(x, (int, float)) and 
            rng.start <= x < rng.stop and 
            (x == int(x) or rng.step == 1)]
    
