class calculate:

    @staticmethod
    def count(list):
        """
        counts the number of items in the list.
        """
        if len(list) == 0:
            return None
        return len(list)

    @staticmethod
    def mean(list):
        """
        calculates the mean of a list of numbers.
        """
        if len(list) == 0:
            return None
        return sum(list) / len(list)

    @staticmethod
    def median(list):
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

    @staticmethod
    def quart(list):
        """
        calculates the quartile (25% and 75%) of a list of numbers.
        """
        if len(list) == 0:
            return None
        list.sort()
        length = len(list)
        half = int(length / 2)

        if length % 2 == 0:
            Q1 = calculate.median(list[:half - 1])
            Q3 = calculate.median(list[half:])
        else:
            Q1 = calculate.median(list[:half + 1])
            Q3 = calculate.median(list[half:])

        return [float(Q1), float(Q3)]

    @staticmethod
    def var(list):
        """
        calculates the Standard Deviation of a list of numbers.
        """
        # variance = moyenne des carrés des différences entre chaque élément
        # et la moyenne.
        # écart-type = la racine carrée de la variance.
        if len(list) == 0:
            return None
        mean = calculate.mean(list)
        var = sum((x - mean) ** 2 for x in list) / len(list)
        return var

    @staticmethod
    def std(list):
        """
        calculates the Standard Deviation of a list of numbers.
        """
        # variance = moyenne des carrés des différences entre chaque élément
        # et la moyenne.
        # écart-type = la racine carrée de la variance.
        if len(list) == 0:
            return None
        mean = calculate.mean(list)
        var = sum((x - mean) ** 2 for x in list) / len(list)
        std = var ** 0.5
        return std
    
    @staticmethod
    def min(lst):
        if len(lst) == 0:
            return None
        min_value = lst[0]
        for num in lst:
            if num < min_value:
                min_value = num
        return min_value
    
    @staticmethod
    def max(lst):
        if len(lst) == 0:
            return None
        max_value = lst[0]
        for num in lst:
            if num > max_value:
                max_value = num
        return max_value