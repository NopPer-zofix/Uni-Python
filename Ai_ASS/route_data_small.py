# route_data_small.py
#
# Small map data for route-finding problem implementation.
#
# Representation:
# - ROADS[city] = list of (neighbor_city, road_distance)
# - LOCATIONS[city] = (x, y) position, for calculating the straight-line distance heuristic

ROADS = {
    "Arbor": [
        ("Brook", 3),
        ("Cedar", 3),
    ],
    "Brook": [
        ("Arbor", 3),
        ("Dover", 3),
    ],
    "Cedar": [
        ("Arbor", 3),
        ("Dover", 4),
        ("Elm", 3),
        ("Haven", 15),
    ],
    "Dover": [
        ("Brook", 3),
        ("Cedar", 4),
        ("Elm", 4),
        ("Fairview", 3),
    ],
    "Elm": [
        ("Cedar", 3),
        ("Dover", 4),
        ("Fairview", 4),
        ("Glen", 3),
    ],
    "Fairview": [
        ("Dover", 3),
        ("Elm", 4),
        ("Glen", 4),
        ("Haven", 3),
    ],
    "Glen": [
        ("Elm", 3),
        ("Fairview", 4),
        ("Haven", 4),
    ],
    "Haven": [
        ("Cedar", 15),
        ("Fairview", 3),
        ("Glen", 4),
    ],
}

LOCATIONS = {
    "Arbor": (0, 4),
    "Brook": (2, 6),
    "Cedar": (2, 3),
    "Dover": (4, 5),
    "Elm": (4, 2),
    "Fairview": (6, 4),
    "Glen": (6, 1),
    "Haven": (8, 3),
}

DEFAULT_START = "Arbor"
DEFAULT_GOAL = "Haven"