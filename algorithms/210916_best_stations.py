states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut'}
stations = {
    'kone': {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'nv', 'ut'},
    'kfive': {'ca', 'az'}
}

final_stations = set()
while states_needed:
    best_stations = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_stations = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_stations)

print(final_stations)