def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    indices_encontrados = 0
    for input, output in permanence_period:
        if not isinstance(input, int) or not isinstance(output, int):
            return None
        if input <= target_time <= output:
            indices_encontrados += 1
    return indices_encontrados
    # raise NotImplementedError


# print(study_schedule([(10, 11), (8, 12), (12, 22)], 12))
