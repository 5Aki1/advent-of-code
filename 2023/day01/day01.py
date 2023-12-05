import re


def main():
    num_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    result_list_one = []
    result_list_two = []

    with open("input.bib", "r") as file:
        for line in file:
            line = line.strip()

            # Solution 1
            first_digit = next((int(s) for s in line if s.isdigit()), None)
            last_digit = next((int(s) for s in reversed(line) if s.isdigit()), None)
            result_list_one.append((str(first_digit) + str(last_digit)))

            # Solution 2
            result = find_matches(line, num_dict)
            swap_keys_values(result, num_dict)
            result_list_two.append(swap_keys_values(result, num_dict))

    sum_result = sum(int(s) for s in result_list_one)
    print("Part 1:", sum_result)
    sum_result = concat_and_sum(result_list_two)
    print("Part 2:", sum_result)


def find_matches(input_string: str, num_dict: dict) -> list:
    matches = []

    # Dictionary matches
    for key in num_dict:
        pattern = re.compile(re.escape(key), re.IGNORECASE)
        for match in pattern.finditer(input_string):
            matches.append({"key": key, "index": match.start()})

    # Digit matches
    digit_pattern = re.compile(r"\d")
    for digit_match in digit_pattern.finditer(input_string):
        matches.append({"key": int(digit_match.group()), "index": digit_match.start()})

    matches = sorted(matches, key=lambda x: x["index"])
    return matches


def swap_keys_values(result_list: list, num_dict: dict) -> list:
    swapped_values = []
    for match in result_list:
        line = []
        key = match["key"]

        if key in num_dict:
            swapped_value = num_dict[key]
        else:
            swapped_value = key

        line.append(swapped_value)
        line = "".join(str(x) for x in line)
        swapped_values.append(line)
    return swapped_values


def concat_and_sum(l: list) -> int:
    result = []
    for item in l:
        if item:
            first_digit = item[0]
            last_digit = item[-1]
            result.append(int(str(first_digit) + str(last_digit)))
    return sum(result)


if __name__ == "__main__":
    main()
