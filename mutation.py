import random
import copy
import numpy as np

from salesman import Salesman

###########
# Private #
###########
def _insertion(route, rate=0.02):
  size = len(route)
  tmp = route.copy()
  for i in range(size):
    if random.random() < rate:
      tmp = np.delete(route, i)
      insert_point = random.randint(0, len(tmp))
      tmp = np.insert(tmp, insert_point, route[i])
  return tmp

def _exchange(route, rate=0.02):
  size = len(route)
  for i in range(size):
    if random.random() < rate:
      swap_point = random.randint(0, size-1)
      route[i], route[swap_point] = route[swap_point], route[i]
  return route

##########
# Public #
##########
def insertion(salesman_list, rate=0.3, irate=0.02):
  size = len(salesman_list)
  new_salesman_list = []
  for salesman in salesman_list:
    tmp = copy.deepcopy(salesman)
    if random.random() < rate:
      tmp.route = _insertion(salesman.route, irate)
    new_salesman_list.append(tmp)
  return new_salesman_list

def exchange(salesman_list, rate=0.3, irate=0.02):
  size = len(salesman_list)
  new_salesman_list = []
  for salesman in salesman_list:
    tmp = copy.deepcopy(salesman)
    if random.random() < rate:
      tmp.route = _exchange(salesman.route, irate)
    new_salesman_list.append(tmp)
  return new_salesman_list
