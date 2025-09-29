nums = list(map(int, input().split()))

while True:
    line = input().strip()
    if line == "end":
        print(f"[{', '.join(map(str, nums))}]")
        break

    parts = line.split()
    command = parts[0]

    if command == "exchange":
        index = int(parts[1])
        if index < 0 or index >= len(nums):
            print("Invalid index")
            continue
        nums = nums[index + 1:] + nums[:index + 1]

    elif command in ("max", "min"):
        even_odd_type = parts[1]
        is_even = (even_odd_type == "even")
        found = False
        if command == "max":
            max_value = -1
            max_index = -1
            for i in range(len(nums)):
                number = nums[i]
                if ((number % 2 == 0) == is_even)\
                        and (number > max_value or
                             (number == max_value and
                              i > max_index)):
                    max_value = number
                    max_index = i
                    found = True
            if found:
                print(max_index)
            else:
                print("No matches")
        else:
            min_value = float("inf")
            min_index = -1
            for i in range(len(nums)):
                number = nums[i]
                if ((number % 2 == 0) == is_even) \
                        and (number < min_value or
                             (number == min_value and
                              i > min_index)):
                    min_value = number
                    min_index = i
                    found = True
            if found:
                print(min_index)
            else:
                print("No matches")

    elif command in ("first", "last"):
        count = int(parts[1])
        even_odd_type = parts[2]
        if count > len(nums):
            print("Invalid count")
            continue
        is_even = (even_odd_type == "even")
        new_list = [num for num in nums if
                    ((num % 2 == 0) == is_even)]
        if command == "first":
            new_list = new_list[:count]
        else:
            new_list = new_list[-count:]
        print(f"[{', '.join(map(str, new_list))}]")
