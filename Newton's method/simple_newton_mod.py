# модифицированная реализация Метода Ньютона

# добавлен новый параметр в функцию: s - кратность корня;
def simple_newton_mod(func, dfunc, x,  s = 1, tol = 1e-12):

    sol = 0
    iteration = 0
    dxs = []

    for i in range(30):
        iteration += 1

        # в starterpack-е не учтен случай, когда dfunc(x) = 0.
        # Чтобы решить данную проблему возьмем малое значение,
        # в качестве dfunc, например: dfunc = 1e-3;
        if dfunc(x) == 0:
            dx = -func(x) / 1e-3
        else:
            dx = -func(x)/dfunc(x)

        dxs.append(s*dx)
        x = x + s*dx
        if abs(s*dx) < tol:
            sol = x
            return [sol, iteration, dxs]

    sol = float('nan')
    print('More then 30 iterations!')
    return [sol, iteration]
