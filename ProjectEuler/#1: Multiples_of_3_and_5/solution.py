#!/bin/python3

def multiple_of_three(n):

    last_term = n - 1
    while last_term % 3 != 0:
        last_term -= 1

    n_term = (last_term) // 3
    sum_of_terms = ((3 + last_term) * n_term) // 2

    return sum_of_terms

def multiple_of_five(n):

    last_term = n - 1
    while last_term % 5 != 0:
        last_term -= 1

    n_term = (last_term) // 5
    sum_of_terms = ((5 + last_term) * n_term) // 2

    return sum_of_terms

def multiple_of_fifteen(n):

    last_term = n - 1
    while last_term % 15 != 0:
        last_term -= 1

    n_term = (last_term) // 15
    sum_of_terms = ((15 + last_term) * n_term) // 2
    
    return sum_of_terms

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    print((multiple_of_three(n) + multiple_of_five(n)) - multiple_of_fifteen(n))
