class Yatzy:

    ### Public methods ###

    @staticmethod
    def chance(*dices):

        total = 0

        for dice in dices:
            total += dice

        return total

    @staticmethod
    def yatzy(*dices):

        total = 0

        for dice in dices:
            if dice == dices[0]:
                continue

            else:
                return total

        total = 50
        return total

    @staticmethod
    def ones(*dices):

        total = dices.count(1)

        return total

    @staticmethod
    def twos(*dices):

        total = dices.count(2) * 2

        return total

    @staticmethod
    def threes(*dices):

        total = dices.count(3) * 3

        return total

    @staticmethod
    def fours(*dices):

        total = dices.count(4) * 4

        return total

    @staticmethod
    def fives(*dices):

        total = dices.count(5) * 5

        return total

    @staticmethod
    def sixes(*dices):

        total = dices.count(6) * 6

        return total

    @staticmethod
    def pair(*dices):

        total = 0
        pairs = []

        for dice in dices:
            if dice in pairs:
                continue

            if dices.count(dice) >= 2:
                pairs.append(dice)

        if pairs:
            result = sorted(pairs)[-1]
            total = result * 2
            return total

        else:
            return total

    @staticmethod
    def strict_pair(*dices):

        for number in range(1, 7):

            if dices.count(number) == 2:
                return 2 * number

        return 0

    @staticmethod
    def two_pairs(*dices):

        total = 0
        pairs = []

        for dice in dices:
            if dice in pairs:
                continue

            if dices.count(dice) >= 2:
                pairs.append(dice)

        if len(pairs) >= 2:
            for number in pairs:
                total += number

            total = total * 2

            return total

        else:
            return total

    @staticmethod
    def four_of_a_kind(*dices):

        total = 0
        fours = []

        for dice in dices:
            if dice in fours:
                continue

            if dices.count(dice) >= 4:
                fours.append(dice)

        if fours:
            result = sorted(fours)[-1]
            total = result * 4
            return total

        else:
            return total

    @staticmethod
    def three_of_a_kind(*dices):

        total = 0
        threes = []

        for dice in dices:
            if dice in threes:
                continue

            if dices.count(dice) >= 3:
                threes.append(dice)

        if threes:
            result = sorted(threes)[-1]
            total = result * 3
            return total

        else:
            return total

    @staticmethod
    def small_straight(*dices):
        total = 0

        for number in range(1, 6):
            if dices.count(number) != 1:
                return total

        return Yatzy.chance(*dices)

    @staticmethod
    def large_straight(*dices):
        total = 0

        for number in range(2, 7):
            if dices.count(number) != 1:
                return total

        return Yatzy.chance(*dices)

    @staticmethod
    def full_house(*dices):
        total = 0

        if Yatzy.strict_pair(*dices) and Yatzy.three_of_a_kind(*dices) and not Yatzy.yatzy(*dices) and not Yatzy.four_of_a_kind(*dices):
            return Yatzy.chance(*dices)
        else:
            return total
