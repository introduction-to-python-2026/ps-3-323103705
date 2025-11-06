import random
def approximate_pi(n_terms):
    radius = 0.5
    count_in_circle = 0
    count_in_squre = 0
    for i in range(n_terms):
      x = random.random()
      y = random.random()
      distance_to_center = ((x - radius) ** 2 + (y - radius) ** 2) ** 0.5
      if distance_to_center < radius:
        count_in_circle += 1
      count_in_squre += 1
    pai = (count_in_circle / count_in_squre) * 4
    return pai
