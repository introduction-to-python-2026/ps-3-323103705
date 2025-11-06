def approximate_pi(n_terms):
    distance_to_center = 0
    for i in range(n_terms):
      distance_to_center += ((-1 ** i) / (2 * i + 1))
    pai = distance_to_center * 4
    return pai
