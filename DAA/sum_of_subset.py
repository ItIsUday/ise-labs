def generate_sum_of_subsets(nums, max_sum):
    def create_state_space_tree(num_index, path, remaining_nums_sum):
        if sum(path) > max_sum or (remaining_nums_sum + sum(path)) < max_sum:
            return
        if sum(path) == max_sum:
            result.append(path)
            return
        for i in range(num_index, len(nums)):
            create_state_space_tree(i + 1, path + [nums[i]], remaining_nums_sum - nums[i])

    result = []
    create_state_space_tree(0, [], sum(nums))
    return result


def main():
    nums = list(map(int, input("Enter the elements: ").split()))
    max_sum = int(input("Enter max sum: "))
    print("The solutions are: ")
    print(*generate_sum_of_subsets(nums, max_sum))


if __name__ == "__main__":
    main()
