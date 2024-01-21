import sys as fileReader  # Import the sys module and alias it as fileReader

def max_constraint_check(n, k):
    if k == 0 or k == n:
        return 1
    # If k is greater than n - k,  to calculate C(n, k) as C(n, n - k)
    #need to calculate C(n, k) and k is greater than n - k, calculate C(n, k) as C(n, n - k)
    #For example, when you want to distribute 3 robots into a set of 7 stacks, choosing how to distribute the robots (3 robots into 7 stacks)
    # is equivalent to choosing not to include 4 stacks (7 - 3) from the same set of 7.
    if k > n - k:
        k = n - k
    finalValue = 1
    # Use a loop to compute C(n, k) iteratively
    for i in range(k):
        # Calculate (n - i) * (n - i - 1) * ... * (n - k + 1) / (i + 1)
        finalValue = finalValue * (n - i)  # Multiply the current result by (n - i)
        finalValue = finalValue // (i + 1)  # Divide the current result by (i + 1)
    return finalValue

def climibing_wall_ways_rec(b, n, k, store_m):
    # Base cases
    if b == 0:
        return 1
    if n == 0:
        return 0

    # Check if k is 1 or b
    if k == 1:
        return max_constraint_check(n, b)
    elif k == b:
        return max_constraint_check(n + b - 1, b)
    else:
        # Checking whether data is already memoized or not
        if store_m[b][n][k] != -1:
            return store_m[b][n][k]

    # Calculate the number of ways recursively
    final_climb_ways_out = 0
    # Distribute robots into stacks with constraints
    # Determine the constraint to impose based on the smaller of k and b
    if k <= b:
        constraint_impose = k
    else:
        constraint_impose = b
    # Calculate the number of ways to distribute robots by recursively considering different constraint values
    for i in range(constraint_impose + 1):
        final_climb_ways_out += climibing_wall_ways_rec(b - i, n - 1, k, store_m)

    # Memoize the result
    store_m[b][n][k] = final_climb_ways_out
    return final_climb_ways_out


#helper fun for climibing_wall_ways_rec
def final_output_assist(b, n, k):
    # Initialize the memoization table
    store_m = []
    constraint_in = 0
    while constraint_in <= b:
        no_of_list = [[-1] * (k + 1) for _ in range(n + 1)]
        store_m.append(no_of_list)
        constraint_in += 1

    # Calculate the number of ways to distribute the robots
    final_entire_ways = climibing_wall_ways_rec(b, n, k, store_m)
    return final_entire_ways

def main():
    # Read the input file name from command line arguments
    if len(fileReader.argv) != 2:
        print("To run code it requires input.txt file please provide the file")
        exit(1)  #if fileReader.argv <2 then exit from program
    argument_file_in = fileReader.argv[1]

    # Read the input file in read mode
    with open(argument_file_in, 'r') as in_file:
        lineReads = in_file.readlines()

    for eachinstanceline in lineReads:
        # Parse the values of b, n, and k from the space-separated eachinstanceline string
        # where n= number of stacks
        # b  = number of robots
        # k = number of robots that can go in each stack
        b, n, k = map(int, eachinstanceline.strip().split())
        entire_ways = final_output_assist(b, n, k)
        print("(%d, %d, %d) = %d" % (b, n, k, entire_ways))


if __name__ == "__main__":
    main()
