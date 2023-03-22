def observed():
    observations = []
    for i in range(5):
        obeservation = input("Enter an observation: ")
        observations.append(obeservation)
    return observations

def remove_observations(observations):
    while True:
        remove = input("Do you wish to remove an observation? (y/n): ")
        if remove.lower() == "n":
            break
        elif remove.lower() == "y":
            observation = input("Enter ab observation to remove: ")
            if observation in observations:
                observations.remove(observation)
                print(f"{observation} removed.")
            else:
                print(f"{observation} not found in observations.")
        else:
            print("Invalid input. Please enter y or n.")

def run():
    observations = observed()
    remove_observations(observations)
    observation_count = {}
    for observation in observations:
        if observation in observation_count:
            observation_count[observation] += 1
        else:
            observation_count[observation] = 1
    sorted_observations = sorted(set(observations))
    print("Observations:")
    for observation in sorted_observations:
        count = observation_count[observation]
        print(f"{observation} observed {count} times")

run()