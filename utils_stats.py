def calculate_mean(list):
    """
    calculates the mean of a list of numbers.
    """
    if len(list) == 0:
        return None
    return sum(list) / len(list)


def calculate_median(list):
    """
    calculates the median of a list of numbers.
    """
    if len(list) == 0:
        return None
    list.sort()
    length = len(list)
    if length % 2 == 0:
        return (list[int(length/2) - 1] + list[int(length/2)]) / 2
    else:
        return list[int(length/2)]


def calculate_quart(list):
    """
    calculates the quartile (25% and 75%) of a list of numbers.
    """
    if len(list) == 0:
        return None
    list.sort()
    length = len(list)
    half = int(length / 2)

    if length % 2 == 0:
        Q1 = calculate_median(list[:half - 1])
        Q3 = calculate_median(list[half:])
    else:
        Q1 = calculate_median(list[:half + 1])
        Q3 = calculate_median(list[half:])

    return [float(Q1), float(Q3)]


def calculate_var(list):
    """
    calculates the Standard Deviation of a list of numbers.
    """
    # variance = moyenne des carrés des différences entre chaque élément
    # et la moyenne.
    # écart-type = la racine carrée de la variance.
    if len(list) == 0:
        return None
    mean = calculate_mean(list)
    var = sum((x - mean) ** 2 for x in list) / len(list)
    return var

def calculate_std(list):
    """
    calculates the Standard Deviation of a list of numbers.
    """
    # variance = moyenne des carrés des différences entre chaque élément
    # et la moyenne.
    # écart-type = la racine carrée de la variance.
    if len(list) == 0:
        return None
    mean = calculate_mean(list)
    var = sum((x - mean) ** 2 for x in list) / len(list)
    std = var ** 0.5
    return std