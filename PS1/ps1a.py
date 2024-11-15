###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================


# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    with open(filename) as cow_data:
        lines = cow_data.readlines()
    dict = {}
    for line in lines:
        key, value = line.strip().split(',')
        dict[key.strip()] = int(value.strip())
    return dict
    pass

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    sorted_cows = sorted(cows.items(), key=lambda x: x[1], reverse=True)

    # Initialize variables
    travel_lists = []
    room_left = limit

    # While there are still cows to transport
    while sorted_cows:
        current_list = []
        room_left = limit

        # Iterate over the sorted cows list
        i = 0
        while i < len(sorted_cows):
            cow_name, weight = sorted_cows[i]
            # If the cow can fit in the remaining space of the current trip
            if weight <= room_left:
                # Add the cow to the current trip
                current_list.append(cow_name)
                # Update the remaining space
                room_left -= weight
                # Remove the cow from the sorted list
                sorted_cows.pop(i)
            else:
                # Move to the next cow
                i += 1
        # Add the current trip to the travel lists
        travel_lists.append(current_list)

    return travel_lists
    pass

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    best_partition = None
    # Iterate over all possible partitions
    for partition in get_partitions(cows):
        # Initialize a flag to check if the partition is valid
        is_valid_partition = True
        # Iterate over each trip in the partition
        for trip in partition:
            # Calculate the total weight of cows in the trip
            trip_weight = sum(cows[name] for name in trip)
            # If the total weight exceeds the limit, mark the partition as invalid
            if trip_weight > limit:
                is_valid_partition = False
                break
        # If the partition is valid and either the best partition is None or the current partition uses fewer trips
        if is_valid_partition and (best_partition is None or len(partition) < len(best_partition)):
            # Update the best partition
            best_partition = partition

    # Return the best partition found
    return best_partition
    pass

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    listB =[]
    listG =[]
    dict = load_cows('ps1_cow_data.txt')

    # timing bruteforce
    startB = time.time()
    listB = brute_force_cow_transport(dict, 10)
    endB = time.time()
    print(f"Brute force algorithm took {endB - startB} seconds and returned {len(listB)} trips.")

    # timing Greedy Algo
    startG = time.time()
    listG = greedy_cow_transport(dict, 10)
    endG = time.time()
    print(f"Greedy algorithm took {endG - startG} seconds and returned {len(listG)} trips.")

    pass

compare_cow_transport_algorithms()