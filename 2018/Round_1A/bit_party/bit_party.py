class Cashier():

    def __init__(self, m, s, p):
        self.max_bits = m
        self.scan_time = s
        self.pay_time = p
    
    def maximum_items_in_time(self, time):
        if time < self.scan_time + self.pay_time:
            # Too fast to this cashier
            return 0
        maximum_time_per_customer = (self.scan_time * self.max_bits) + self.pay_time
        if time > maximum_time_per_customer:
            # Only one robot is allowed to interact with a single cashier.
            return self.max_bits
        # time = (scan_time * items) + (pay_time * num_robots)
        # items = (time - pay_time ) // scan_time
        self.items_processed = (time - self.pay_time) // self.scan_time
        return self.items_processed


def possible_to_solve_in_time(cashiers, robots, items, time):
    # Order cashiers by the maximun_items_in_time
    cashiers.sort(key=lambda c: c.maximum_items_in_time(time), reverse=True)
    # Calculate the maximum item processed given the time
    max_items = 0
    for r in range(robots):
        max_items += cashiers[r].maximum_items_in_time(time)
    # Return if its possible to solve
    return max_items >= items


def solve_it():
    r, b, c = [int(x) for x in input().split(' ')]
    cashiers = []
    for _ in range(c):
        m, s, p = [int(x) for x in input().split(' ')]
        cashiers.append(Cashier(m, s, p))

    # Find the minimum time. Using binary search to find the minimum time
    # maximum time: 1 cashier, 10^9 items * 10^9 each item + 10^9 pay
    # 10^9 * 10^9 + 10^9 = 10^18 + 10^9
    _10_9 = 1000000000
    max_time = (_10_9 * _10_9) + _10_9
    last_valid_time = max_time
    actual_time = max_time // 2
    while last_valid_time != actual_time:
        if possible_to_solve_in_time(cashiers, r, b, actual_time):
            t = actual_time
            if last_valid_time - actual_time > 3:
                actual_time //= 2
            else:
                actual_time -= 1
            last_valid_time = t
        else:
            if last_valid_time - actual_time > 3:
                actual_time = last_valid_time - ((last_valid_time - actual_time) // 2)
            else:
                actual_time += 1
    return last_valid_time



t = int(input())

for case in range(1, t+1):
    answer = solve_it()
    print('Case #{}: {}'.format(case, answer))
