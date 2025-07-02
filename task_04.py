def sort_list(lst):
    if not lst:
        return []
    
    min_zn = min(lst)
    max_zn = max(lst)
    
    result = [max_zn if x == min_zn else min_zn if x == max_zn else x for x in lst]
    result.append(min_zn)
    return result



