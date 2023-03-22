def observed():
    observations = []
    for i in range(7):
        observation = input(f"Enter observation {i+1}: ")
        observations.append(observation)
    return observations

def run():
    print("Counting observations...")
    observations_list = observed()
    observations_set = set((obs, observations_list.count(obs)) for obs in set(observations_list))
    print(observations_set)
run()