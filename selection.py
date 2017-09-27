import random
import numpy as np

from salesman import Salesman

def tournament(parents, tournament_size=3):
  offsprings = []
  for _ in range(len(parents)):
    minfitness = 1e14
    samples = random.sample(parents, tournament_size)
    for salesman in samples:
      if salesman.fitness < minfitness:
        tmp = salesman
        minfitness = salesman.fitness
    offsprings.append(tmp)
  return offsprings 

# TODO : Implementation
def rank(parents):
  offsprings = parents
  return offsprings
