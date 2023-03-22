def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    min_likelihood = min(likelihoods)
    max_likelihood = max(likelihoods)
    return (min_likelihood, max_likelihood)

min_max_likelihoods = likelihood()
print(f"Minimum likelihood of falling: {min_max_likelihoods[0]}%")
print(f"Maximum likelihood of falling: {min_max_likelihoods[1]}%")