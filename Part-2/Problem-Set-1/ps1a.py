###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import string

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
    cows = {}
    file = open(filename,'r')
    for line in file:
        line_as_list = line.split(',')
        cows[line_as_list[0]] = line_as_list[1]
    
    return cows

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
    cows_copy = cows.copy()
    trips = [] #this stores the list of lists to be returned
    while cows_copy != {}:
        trip = []
        current_weight = 0
        for cow in sorted(cows_copy, key=cows_copy.__getitem__, reverse = True):
            if int(cows_copy[cow]) + current_weight <= limit:
                trip.append(cow)
                current_weight += int(cows_copy[cow])
                cows_copy.pop(cow)
            else:
                continue
        trips.append(trip)
    return trips

            

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
    def get_trip_weight(trip_cows):
        trip_weight = 0
        for cow in trip_cows:
            trip_weight += int(cows_copy[cow])
        
        return trip_weight
    
    cows_copy = cows.copy()
    best_set = list(cows_copy)
    
    for set_of_trips in get_partitions(cows_copy.keys()):
        is_good_set = True
        for trip in set_of_trips:
            if get_trip_weight(trip) > limit:
                is_good_set = False
                break
            else:
                continue
        if is_good_set and len(set_of_trips) < len(best_set):
            best_set = set_of_trips
    return best_set
            
        
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
    cows = load_cows('ps1_cow_data.txt')
    
    start_greedy = time.time() 
    trips_greedy = len(greedy_cow_transport(cows))
    end_greedy = time.time() 
    
    start_brute_force = time.time() 
    trips_brute_force = len(brute_force_cow_transport(cows))
    end_brute_force = time.time() 
    
    print('Greedy algorithm: ',trips_greedy,'trips', 'and took', end_greedy - start_greedy,'seconds')
    print('Brute force algorithm: ',trips_brute_force,'trips', 'and took', end_brute_force - start_brute_force,'seconds')