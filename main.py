from itertools import *
import numpy as np


def print_step_1(nr):
    print("The number of bases of the vector space (Z2)^n over Z2 is: " + str(nr), file=g)


def calculate_nr_of_bases(n):
    """
    # a = (q^n -1)(q^n -q)...(q^n - q^(k-1))
    # a = number of ways of specifying a linearly independent set of cardinality k
    # in our case q = 2
    :param n: vector space (Z2)^n (type: int)
    :return: the number of bases of the vector space (Z2)^n over Z2 (type: int)
    """
    a = 1
    for i in range(n):
        a *= 2 ** n - 2 ** i
    result = a
    return result


def list_of_vectors(n):
    """
    We generate all the vectors of (Z2)^n over Z2

    product -> It returns the cartesian product of the provided iterable with itself
    for the number of times specified by the optional keyword “repeat”

    :param n: vector space (Z2)^n (type: int)
    :return: the vectors (type: list)
    """
    vec = list(product([0, 1], repeat=n))
    vec.pop(0)
    return vec


def calculate_vectors(possibilities):
    """
    The vectors of each such basis
    :param possibilities:
    :return:
    """
    for matrix in possibilities:
        det = np.linalg.det(matrix) % 2
        if det:
            print(matrix, file=g)



if __name__ == '__main__':
    f = open('test1.in', 'r')
    # choose from:
    # test1.in
    # test2.in
    # test3.in
    # test4.in
    # test5.in

    g = open('test1.out', 'w+')
    # choose from:
    # test1.out
    # test2.out
    # test3.out
    # test4.out
    # test5.out

    n = int(f.read())
    nr_sub = calculate_nr_of_bases(n)

    print_step_1(nr_sub)

    if n <= 4:
        vectors = list_of_vectors(n)
        possibilities = list(permutations(vectors, n))
        calculate_vectors(possibilities)