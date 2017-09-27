import random
import copy
import numpy as np

from salesman import Salesman

###########
# Private #
###########
def _uniform_order(route1, route2):
  size = len(route1)
  mask = np.random.randint(0, 2, size)
  tmproute1 = (route1*mask).copy()
  tmproute2 = (route2*mask).copy()
  for i in range(size):
    if route2[i] not in tmproute1:
      insert_index = np.where(tmproute1==0)[0][0]
      tmproute1[insert_index] = route2[i]
  for i in range(size):
    if route1[i] not in tmproute2:
      insert_index = np.where(tmproute2==0)[0][0]
      tmproute2[insert_index] = route1[i]
  return tmproute1, tmproute2

#def _order(route1, route2):
#  size = len(route1)
#  point1 = random.randint(0, size)
#  point2 = random.randint(0, size-1)
#  if point2 >= point1:
#    point2 += 1
#  else
#    point1, point2 = point2, point1
#  mask = np.zeros(size)
#  mask[pint1:point2] = 1
#  tmproute1 = (route1*mask).copy()
#  tmproute2 = (route2*mask).copy()
#  for i in range(point2-1, size):
#  for i in range(point1):
#  for i in range(point2-1, size):
#  for i in range(point1):


##########
# Public #
##########
# Uniform Order Crossocer(UOX)
def uniform_order(salesman_list, rate=0.5):
  new_salesman_list = []
  half = len(salesman_list)/2
  for (salesman1, salesman2) in         \
      zip (salesman_list[0:half], salesman_list[half:]):
    tmp1 = copy.deepcopy(salesman1)
    tmp2 = copy.deepcopy(salesman2)
    if random.random() < rate:
      (tmp1.route, tmp2.route) =        \
          _uniform_order(salesman1.route, salesman2.route)
    new_salesman_list.append(tmp1)
    new_salesman_list.append(tmp2)
  return new_salesman_list

# Order Crossover (OX)
#def order(salesman_list, rate=0.5):
#  new_salesman_list = []
#  half = len(salesman_list)/2
#  for (salesman1, salesman2) in         \
#      zip (salesman_list[0:half], salesman_list[half:])
#    tmp1 = copy.deepcopy(salesman1)
#    tmp2 = copy.deepcopy(salesman2)
#    if random.random() < rate:
#      (tmp1.route, tmp2.route) =        \
#          _order(salesman1.route, salesman2.route)
#
#  new_salesman_list.append(tmp1)
#  new_salesman_list.append(tmp2)
#  return new_salesman_list
