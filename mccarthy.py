def M_extended(n, m, k, s, e, calls):
    # Generalized version of McCarthy's 91 function, where every constant is
    # abstracted away by a variable:
    #   * m generalizes 100,
    #   * k generalizes 11,
    #   * s generalizes 10, and
    #   * e generalizes 2 (i.e., the number of nested calls)
    # The number of calls performed is returned along with the function value
    # at n.

    calls += 1

    if n > m:
       value = n - s
    else:
        result = M_extended(n + k, m, k, s, e, calls)

        for _ in range(e-1):
            result = M_extended(result['value'], m, k, s, e, result['calls'])

        value = result['value']
        calls = result['calls']

    return {'value' : value,
            'calls' : calls}

def M(n, m, k, s, e):
    # Value of generalized McCarthy's 91 function.
    return M_extended(n, m, k, s, e, 0)['value']

def M_91(n):
    # Traditional McCarthy's 91 function, implemented in terms of its
    # generalized version.
    return M(n, m=100, k=11, s=10, e=2)

def r(n, m, k, s, e):
    # Number of recursive calls performed by M(n, m, k, s, e).
    # The -1 term is because we do not count the first call; just recursive
    # calls are counted.
    return M_extended(n, m, k, s, e, 0)['calls'] - 1
