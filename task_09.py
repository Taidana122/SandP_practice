def connect_dicts(dict1, dict2):
    sum1=sum(x for x in dict1.values() if isinstance(x, (int, float)))
    sum2=sum(x for x in dict2.values() if isinstance(x, (int, float)))

    if sum1 > sum2:
        h_prior=dict1
        l_prior=dict2
    else:
        h_prior=dict2
        l_prior=dict1
    
    new_slovar={}

    for key, value in l_prior.items(): #клюючи из низкого пр больше 10
        if isinstance(value, (int, float)) and value >= 10:
            new_slovar[key] = value
    
    for key, value in h_prior.items(): #клюючи из высокого пр больше 10
        if isinstance(value, (int, float)) and value >= 10:
            new_slovar[key] = value
    
    sorted_result = dict(sorted(new_slovar.items(), key=lambda x: x[1]))
    
    return sorted_result    
print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }))
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }))
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))