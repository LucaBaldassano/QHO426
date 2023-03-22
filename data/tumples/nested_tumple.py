def steps():
    likelihoods = [("step 1", 50), ("step 2", 28), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods

def run():
    steps_list = steps()
    good_steps = []
    bad_steps = []
    for step in steps_list:
        if step[1] >= 50:
            bad_steps.append(step)
        else:
            good_steps.append(step)
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

run()