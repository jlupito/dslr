class calculate:

    @staticmethod
    def my_count(lst):
        """
        counts the number of items in the list.
        """
        if len(lst) == 0:
            return None
        return len(lst)

    @staticmethod
    def my_mean(lst):
        """
        calculates the mean of a list of numbers.
        """
        if len(lst) == 0:
            return None
        return sum(lst) / len(lst)

    @staticmethod
    def my_median(lst):
        """
        calculates the median of a list of numbers.
        """
        if len(lst) == 0:
            return None
        lst.sort()
        length = len(lst)
        if length % 2 == 0:
            return (lst[int(length/2) - 1] + lst[int(length/2)]) / 2
        else:
            return lst[int(length/2)]

    @staticmethod
    def my_quart(lst):
        """
        calculates the quartile (25% and 75%) of a list of numbers.
        """
        if len(lst) == 0:
            return None
        lst.sort()
        length = len(lst)
        half = int(length / 2)

        if length % 2 == 0:
            Q1 = calculate.my_median(lst[:half - 1])
            Q3 = calculate.my_median(lst[half:])
        else:
            Q1 = calculate.my_median(lst[:half + 1])
            Q3 = calculate.my_median(lst[half:])

        return [float(Q1), float(Q3)]

    @staticmethod
    def my_var(lst):
        """
        calculates the Standard Deviation of a list of numbers.
        """
        # variance = moyenne des carrés des différences entre chaque élément
        # et la moyenne.
        # écart-type = la racine carrée de la variance.
        if len(lst) == 0:
            return None
        mean = calculate.my_mean(lst)
        var = sum((x - mean) ** 2 for x in lst) / len(lst)
        return var

    @staticmethod
    def my_std(lst):
        """
        calculates the Standard Deviation of a list of numbers.
        """
        # variance = moyenne des carrés des différences entre chaque élément
        # et la moyenne.
        # écart-type = la racine carrée de la variance.
        if len(lst) == 0:
            return None
        mean = calculate.my_mean(lst)
        var = sum((x - mean) ** 2 for x in lst) / len(lst)
        std = var ** 0.5
        return std
    
    @staticmethod
    def my_min(lst):
        if len(lst) == 0:
            return None
        min_value = lst[0]
        for num in lst:
            if num < min_value:
                min_value = num
        return min_value
    
    @staticmethod
    def my_max(lst):
        if len(lst) == 0:
            return None
        max_value = lst[0]
        for num in lst:
            if num > max_value:
                max_value = num
        return max_value