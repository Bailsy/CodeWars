def tower_builder(n_floors):
    tower = []
    for n in range(1, n_floors+1):
        tower.append('*'*(n))
    return tower

print(tower_builder(3))