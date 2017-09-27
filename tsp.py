import math
import numpy as np
import matplotlib.pyplot as plt

from salesman import Salesman
import selection
import crossover
import mutation

POPULATION = 50
LOOPMAX = 10
NODENUM = 10

def main():
  
  nodes = []
  parents = []
  offsprings = []

  ##############
  # Initialize #
  ##############
  for i in range(NODENUM):
    nodes.append(create_node(isfirst=(i==0)))

  for _ in range(POPULATION):
    salesman = create_salesman(NODENUM)
    salesman.fitness = evaluate(nodes, salesman.route)
    parents.append(create_salesman(NODENUM))


  #############
  # Main Loop #
  #############
  loopcount = 0
  while not does_end(loopcount):
    # Selection
    offsprings = selection.tournament(parents)
    
    # Crossover
    offsprings = crossover.uniform_order(offsprings)

    # Mutation
    offsprings = mutation.exchange(offsprings)

    # Change Generation
    parents = offsprings[:]

    # Evaluation
    for salesman in parents:
      salesman.fitness = evaluate(nodes, salesman.route)
    best_salesman = pick_best_salesman(parents)      

    loopcount += 1
    #<DEBUG>#
    print "Generation : " + str(loopcount)
    print best_salesman.route
    print best_salesman.fitness
    #</DEBUG>#

  #<DEBUG>#
  print "########## result ##########"
  print best_salesman.route
  print best_salesman.fitness
  #</DEBUG>#

  #######################
  # Route Visualization #
  #######################
  visualize(nodes, best_salesman.route)


def create_salesman(nodenum):
  salesman = Salesman(np.arange(1,nodenum))
  np.random.shuffle(salesman.route)
  return salesman

def create_node(dimension=2, isfirst=False, variance=5.0):
  if isfirst:
    return np.zeros(dimension)
  return np.random.normal(0.0, variance, dimension)

def get_distance(node1, node2):
  diff = node1 - node2
  return math.sqrt(diff.dot(diff))

def evaluate(nodes, route):
  total_distance = 0
  total_distance += get_distance(nodes[0], nodes[route[0]])
  for i in range(len(route)-1):
    total_distance += get_distance(nodes[route[i]],nodes[route[i+1]])
  total_distance += get_distance(nodes[route[-1]], nodes[0])
  return total_distance

def pick_best_salesman(salesman_list):
  best_salesman = salesman_list[0]
  for salesman in salesman_list:
    if salesman.fitness < best_salesman.fitness:
      best_salesman = salesman
  return best_salesman

def visualize(nodes, route):
  plt.clf()
  plt.plot([nodes[0][0], nodes[route[0]][0]], [nodes[0][1], nodes[route[0]][1]], c="black", lw=1)
  plt.plot([nodes[0][0], nodes[route[-1]][0]], [nodes[0][1], nodes[route[-1]][1]], c="black", lw=1)
  for i in range(1, len(route)):
    plt.plot([nodes[route[i-1]][0], nodes[route[i]][0]],      \
             [nodes[route[i-1]][1], nodes[route[i]][1]], c="black", lw=1)
  plt.scatter(nodes[0][0], nodes[0][1], c="blue", marker="o")
  for i in range(1, len(nodes)):
    plt.scatter(nodes[i][0], nodes[i][1], c="red", marker="o")

  plt.savefig("fig.png")

def does_end(loopcount):
  if loopcount > LOOPMAX:
    return True
  return False

if __name__ == "__main__":
  main()
