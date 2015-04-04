def M_extended(n, m, k, s, e, calls):
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
    return M_extended(n, m, k, s, e, 0)['value']

def M_91(n):
    return M(n, m=100, k=11, s=10, e=2)

def r(n, m, k, s, e):
    return M_extended(n, m, k, s, e, 0)['calls'] - 1

def S(n, m, k, s):
    return n - s + max(0, round_up(m-n+1, k-s))*(k-s)

def round_up(a, b):
    return (a+b-1) // b
