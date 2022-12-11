class Part1:
    def __init__(self, rucksack_list:list[str] = None):
        self.rucksack_list = rucksack_list

    def split_rucksack(self) -> list[tuple[str, str]]:
        """
        Split the list of rucksacks into pockets.

        :return: List of rucksacks split into separate pockets.
        """
        rucksack_pockets = []

        for rucksack in self.rucksack_list:
            # calculate the length of each rucksack
            pocket_len = len(rucksack) // 2

            # use string splicing to split the rucksack
            pocket_1 = rucksack[:pocket_len]
            pocket_2 = rucksack[pocket_len:]

            # append to the list
            rucksack_pockets.append((pocket_1, pocket_2))

        return rucksack_pockets

    @staticmethod
    def check_pockets(pocket_1, pocket_2):
        """
        Check both pockets for the duplicate item in each.

        :return: Duplicate item in both pockets.
        """
        if len(pocket_1) != len(pocket_2):
            raise ValueError('Pockets must have the same length.')

        return ''