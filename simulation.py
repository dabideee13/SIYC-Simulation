"""
SIYC Simulation
"""

from typing import Callable

import pandas as pd
import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go

import params


def ode_model(z: list, t, m, b1, b2, b3, a, a2, K, c, c1, c2, k1,
              k2, k3, r, beta):

    S, I, Y, C = z

    fst = (b1 * S * C * m) / (a + C)
    snd = (b2 * S * C * (1 - m) / a + C)
    trd = 1 - ((S + I) / K)
    fourth = (c * S * Y) / (k1 + S)
    fth = beta * S * I

    dSdt = ((-fst + snd) * trd) - fourth - fth
    dIdt = (fst * trd) - (c1 * I) + fth
    dYdt = (a2 - ((c2 * Y) / (k2 + S))) * Y
    dCdt = (r * (1 - (C / k3)) * C) - ((b3 * S * C) / a + C)
    return [dSdt, dIdt, dYdt, dCdt]


def ode_solver(model: Callable, t: int, initial_conditions: list, params):

    (m, b1, b2, b3, a, a2, K, c, c1, c2, k1, k2, k3, r, beta) = params
    initS, initI, initY, initC = initial_conditions

    result = odeint(model, [initS, initI, initY, initC], t,
                    args=(m, b1, b2, b3, a, a2, K, c, c1, c2, k1, k2,
                          k3, r, beta))

    return result


def main(const: dict):

    initial_conditions = [
        const['S'],
        const['I'],
        const['Y'],
        const['C']
    ]
    params = list(const.values())[5:]
    days = const['t']
    tspan = np.arange(0, days, 1)

    sol = ode_solver(ode_model, tspan, initial_conditions, params)
    S, I, Y, C = sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3]

    # Convert to simulation results to dataframe
    simData = {'S': S, 'I': I, 'Y': Y, 'C': C}
    df = pd.DataFrame(simData)

    # Export simulation data to csv
    df.to_csv('simulation-data.csv')

    # Plot results
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df.S,
            mode='lines',
            name='S'
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df.I,
            mode='lines',
            name='I'
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df.Y,
            mode='lines',
            name='Y'
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df.C,
            mode='lines',
            name='C'
        )
    )
    fig.show()


if __name__ == '__main__':

    # Import parameter values inputed by the user
    param_values = params.main()

    # Run simulation
    main(param_values)

