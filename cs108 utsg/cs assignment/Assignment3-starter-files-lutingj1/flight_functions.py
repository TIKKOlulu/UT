"""CSC108H1S: Functions for Assignment 3 - Airports and Routes.

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the CSC108 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 The CSC108 Team
"""
from flight_constants import AirportDict, RouteDict, OPENFLIGHTS_NULL_VALUE

import flight_example_data


################################################################################
# Part 2 - Querying the data
################################################################################
def is_direct_flight(route_infor: RouteDict, source_airport: str,
                     destination_airport: str) -> bool:
    """Return True if there is a direct flight from the source to destination
    airport in the route information.
    
    >>> route = {'RCM': {'JCK': ['SF3']}}
    >>> is_direct_flight(route, 'RCM', 'JCK')
    True
    >>> is_direct_flight(route, 'TOR', 'JCK')
    False
    """
    
    if source_airport in route_infor:
        if destination_airport in route_infor[source_airport]:
            return True
        else:
            return False
    return False


def is_valid_flight_sequence(route_infor: RouteDict,
                             airport_list: list[str]) -> bool:
    """Return True if there are direct flight between each adjacent pair 
    of IATA codes, and the flight sequence is a valid route, otherwise, 
    return False.
    
    >>> route = {'TRO': {'GFN': ['SF3']}, 'RCM': {'JCK': ['SF3']}}
    >>> is_valid_flight_sequence(route, ['RCM', 'JCK'])
    True
    >>> is_valid_flight_sequence(route, ['JCK', 'TRO', 'RCM'])
    False
    """
    
    if len(airport_list) < 2:
        return False
    for i in range(len(airport_list) - 1):
        if not is_direct_flight(route_infor, airport_list[i],
                                airport_list[i + 1]):
            return False
    return True


def summarize_by_timezone(airport_infor: AirportDict) -> dict[str, int]:
    """Return a dictionary mapping timezones to the number of airports 
    in that timezone.
    
    >>> airport = {}
    >>> airport['GFN'] = {}
    >>> airport['GFN']['Tz'] = 'Australia/Sydney'
    >>> airport['JCK'] = {}
    >>> airport['JCK']['Tz'] = 'Australia/Brisbane'
    >>> summarize_by_timezone(airport)
    {'Australia/Sydney': 1, 'Australia/Brisbane': 1}
    >>> airport['TRO'] = {}
    >>> airport['TRO']['Tz'] = 'Australia/Sydney'
    >>> summarize_by_timezone(airport)
    {'Australia/Sydney': 2, 'Australia/Brisbane': 1}
    """

    timezone_dict = {}
    for k in airport_infor:
        if airport_infor[k]['Tz'] != OPENFLIGHTS_NULL_VALUE:
            if airport_infor[k]['Tz'] not in timezone_dict:
                timezone_dict[airport_infor[k]['Tz']] = 1
            else:
                timezone_dict[airport_infor[k]['Tz']] += 1
    return timezone_dict


################################################################################
# Part 3 - Implementing useful algorithms
################################################################################
def find_reachable_destinations(routes: RouteDict, source: str, n: int) -> \
        list[str]:
    """Return the list of IATA airport codes that are reachable from source by
    taking at most n direct flights.

    The list should not contain an IATA airport code more than once. The airport
    codes in the list should appear in lexicographical order (use the
    list.sort method on a list of strings to achieve this).

    Preconditions:
        - n >= 1
        - (source in routes) is True

    >>> example_routes = flight_example_data.create_example_routes()
    >>> find_reachable_destinations(example_routes, 'GFN', 1)
    ['TRO']
    >>> find_reachable_destinations(example_routes, 'GFN', 2)
    ['GFN', 'SYD', 'TRO']
    """

    reachable = []
    i = 0
    source_list = [source]
    while i < n:
        next_destinations = []
        for s in source_list:
            for d in routes[s]:
                if d not in next_destinations:
                    next_destinations.append(d)
                if d not in reachable:
                    reachable.append(d)
        source_list = next_destinations[:]
        i += 1
    reachable.sort()
    return reachable


def decomission_plane(routes: RouteDict, plane: str) -> list[tuple[str, str]]:
    """Update routes by removing plane from all source-destination routes that
    use plane. Do not remove the source-destination pair, only the plane.

    In addition, return a sorted list of two-element tuples where the first
    index is source and the second index is destination (use the list.sort
    method on a list of tuples to achieve this). The list includes *all* routes
    that that have no planes that can be used.

    >>> example_routes = flight_example_data.create_example_routes()
    >>> decomission_plane(example_routes, 'DH4')
    []
    >>> example_routes['TRO']['SYD']
    ['SF3']
    >>> example_routes = flight_example_data.create_example_routes()
    >>> decomission_plane(example_routes, 'SF3')
    [('GFN', 'TRO'), ('JCK', 'RCM'), ('RCM', 'JCK'), ('TRO', 'GFN')]
    >>> example_routes['TRO']['SYD']
    ['DH4']
    """
    plane_left = []
    for k in routes:
        for s in routes[k]:
            if plane in routes[k][s]:
                routes[k][s].remove(plane)
    for k in routes:
        for s in routes[k]:
            if routes[k][s] == []:
                plane_left.append((k, s))
    for r in plane_left:
        del routes[r[0]][r[1]]
        if len(routes[r[0]]) == 0:
            del routes[r[0]]
    plane_left.sort()
    return plane_left


if __name__ == '__main__':
    # On A3 we do not have a separate checker but instead include code that
    # performs the required checks.  This code requires python_ta to be
    # installed.  See the 'Completing the CSC108 Setup' section in the
    # Software Installation page on Quercus for details.

    # Uncomment the 3 lines below to have function type contracts checked
    # # Enable type contract checking for the functions in this file
    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()

    # Check the correctness of the doctest examples
    import doctest
    doctest.testmod()

    # Uncomment the 2 lines below to check your code style with python_ta
    import python_ta
    python_ta.check_all(config='pyta/a3_pyta.txt')
