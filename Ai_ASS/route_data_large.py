# route_data_large.py
#
# Large map data for route-finding problem implementation.
#
# Representation:
# - ROADS[city] = list of (neighbor_city, road_distance)
# - LOCATIONS[city] = (x, y) position, for calculating the straight-line distance heuristic

ROADS = {
    "Ashton": [
        ("Briar", 4),
        ("Claremont", 3),
    ],
    "Briar": [
        ("Ashton", 4),
        ("Dunfield", 3),
    ],
    "Claremont": [
        ("Ashton", 3),
        ("Dunfield", 4),
        ("Easton", 3),
        ("Lakeside", 20),
    ],
    "Dunfield": [
        ("Briar", 3),
        ("Claremont", 4),
        ("Grafton", 3),
    ],
    "Easton": [
        ("Claremont", 3),
        ("Foxley", 4),
        ("Grafton", 4),
        ("Harton", 3),
    ],
    "Foxley": [
        ("Easton", 4),
        ("Harton", 4),
        ("Kingsley", 5),
    ],
    "Grafton": [
        ("Dunfield", 3),
        ("Easton", 4),
        ("Harton", 4),
        ("Ivydale", 3),
        ("Lakeside", 10),
    ],
    "Harton": [
        ("Easton", 3),
        ("Foxley", 4),
        ("Grafton", 4),
        ("Juniper", 3),
        ("Kingsley", 4),
    ],
    "Ivydale": [
        ("Grafton", 3),
        ("Juniper", 4),
        ("Lakeside", 8),
    ],
    "Juniper": [
        ("Harton", 3),
        ("Ivydale", 4),
        ("Kingsley", 4),
        ("Lakeside", 3),
    ],
    "Kingsley": [
        ("Foxley", 5),
        ("Harton", 4),
        ("Juniper", 4),
        ("Lakeside", 4),
    ],
    "Lakeside": [
        ("Claremont", 20),
        ("Grafton", 10),
        ("Ivydale", 8),
        ("Juniper", 3),
        ("Kingsley", 4),
    ],
}

LOCATIONS = {
    "Ashton": (0, 8),
    "Briar": (2, 10),
    "Claremont": (2, 7),
    "Dunfield": (4, 9),
    "Easton": (4, 6),
    "Foxley": (4, 3),
    "Grafton": (6, 8),
    "Harton": (6, 5),
    "Ivydale": (8, 9),
    "Juniper": (8, 6),
    "Kingsley": (8, 3),
    "Lakeside": (10, 5),
}

DEFAULT_START = "Ashton"
DEFAULT_GOAL = "Lakeside"