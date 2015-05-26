# Author -- Jerome Isaacs
# ICS Project 33 - Lottery Game!
from numpy import append
from sys import exit


class LotterySetError(Exception):
    def _init_(self, has_failed):
        self.has_failed = has_failed
        return self.has_failed
        sys.exit(0)


# Make a new lottery_set that is UNIQUE
def make_lottery_set_type(lottery_set, lottery_num_count, lottery_tuple):
    Dynamic = '%s' % lottery_set

    class Dynamic:
        lottery_static_set = lottery_set
        set_size = lottery_num_count
        min_set_number = lottery_tuple[0]
        max_set_number = lottery_tuple[1]

        def __init__(self, lottery_list):
            if len(lottery_list) != self.set_size:
                raise LotterySetError('Error -- constructor not specified length')
            else:
                pass
            for n in lottery_list:
                if n >= self.min_set_number or n <= self.max_set_number:
                    pass
                else:
                    raise LotterySetError('Error -- constructor was not within number bounds')
            for n in range(0, len(lottery_list)):
                for j in range(1, len(lottery_list)):
                    a = lottery_list[n]
                    k = lottery_list[j]

                    if n != j and a == k:
                        raise LotterySetError('Error -- constructor numbers equaled each other')
                    else:
                        pass

            self.lottery_list = lottery_list
        def full_match(self, replica_lottery_set):

            if self.lottery_list == replica_lottery_set.lottery_list:
                return True
            elif self.lottery_list != replica_lottery_set.lottery_list:
                return False
            else:
                raise LotterySetError('Error -- This set belongs to a different game')


        def match_count(self, replica_lottery_set):
            new_list = []
            global lottery_static_set

            if self.lottery_static_set != replica_lottery_set.lottery_static_set:
                raise LotterySetError('Error -- This set belongs to a different game')
            else:
                for n in self.lottery_list:
                    for k in replica_lottery_set.lottery_list:
                        if n == k:
                            new_list.append(n)
                        else:
                            pass
            print len(new_list)

        def _repr_(self):
            return '%s({})'.format(self.lottery_list) % lottery_set

        def __len__(self):
            return len(self.lottery_list)

        def __eq__(self, replica_lottery_set):
            self.lottery_set = lottery_set
            if (self.lottery_set == replica_lottery_set) and (self.lottery_set.lottery_list == replica_lottery_set.lottery_list):
                return True
            else:
                return False

        def __in__(self, lottery_number):
            self.lottery_set = lottery_set

            for x in self.lottery_set.lottery_list:
                if x == lottery_number:
                    return True
                else:
                    pass
            return False
        def __not__in(self, lottery_number):
            self.lottery_set = lottery_set

            for x in self.lottery_set.lottery_list:
                if x != lottery_number:
                    return True
                else:
                    pass
            return False

        def reverse_iter(self):
            for i in range(0, len(self.lottery_list)):
                for j in range(1, len(self.lottery_list)):
                    a = self.lottery_list[i]
                    k = self.lottery_list[j]

                    if i == 0:
                        if a >= k:
                            pass
                        else:
                            self.lottery_list.pop(j)
                            self.lottery_list.insert(0, k)
                    else:
                        break

            return self.lottery_list
        def forward_iter(self):
            for i in range(0, len(self.lottery_list)):
                for j in range(1, len(self.lottery_list)):
                    a = self.lottery_list[i]
                    k = self.lottery_list[j]

                    if j != i and j > i:
                        if a > k:
                            self.lottery_list.pop(i)
                            self.lottery_list.insert(j, a)
                        else:
                            pass
                    else:
                        pass

            return self.lottery_list

    return Dynamic



BooLotto = make_lottery_set_type('BooLotto', 6, (1, 30))
b1 = BooLotto([3, 6, 9, 12, 15, 18])
b2 = BooLotto([3, 4, 9, 12, 20, 25])
b1.full_match(b2)
















