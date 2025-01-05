from itertools import product

def solve(input: list[str]):
    total_calibrations = 0
    
    for line in input:
        result, number_string = line.split(': ')
        result = int(result)
        numbers= list(map(int, number_string.split()))
        
        # all combinations of operators for the length of numbers -1, two numbers can only be operated on once...
        ops_comb = product(['+','*','||'], repeat=len(numbers)-1)
        
        for ops in ops_comb:
            if eval(numbers, ops) == result:
                total_calibrations += result
                break
                
    return total_calibrations

    
def eval(numbers, operators):
    result = numbers[0]
    
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i+1]
        if op == '*':            
            result *= numbers[i+1]
        if op == '||':            
            result = int(str(result) + str(numbers[i + 1]))

    return result        
            
def read_file(name: str):
    with open(name, "r") as file:
        return [line.strip() for line in file.readlines()]


if __name__ == "__main__":
    print("Day 7")
    print("Part 1")
    print(f'{solve(read_file("example.txt"))} calibrations')
    print(f'{solve(read_file("input.txt"))} calibrations')