# Part 1: 
with open("input.txt") as f:
    left_list, right_list = map(
        list, zip(*[map(int, line.strip().split()) for line in f])
    )

left_list.sort()
right_list.sort()

result = [abs(left_list[i] - right_list[i]) for i in range(len(left_list))]
print(sum(result))

# Part 2:
right_list_freq_table = {x:right_list.count(x) for x in right_list}

result = sum(left_list[i] * right_list_freq_table.get(left_list[i], 0) for i in range(len(left_list)))
print(result)

