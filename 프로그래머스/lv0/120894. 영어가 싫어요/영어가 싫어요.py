def solution(numbers):
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(10):
        numbers = numbers.replace(num_list[i],str(i))
    return int(numbers)