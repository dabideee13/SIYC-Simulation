#!/opt/anaconda3/envs/siyc/bin/python
# -*- coding: utf-8 -*-
"""Ruth Simulation"""

import os
from collections import namedtuple
import numpy as np
from scipy.integrate import odeint

import plotly

import dash
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go

def ode_model(z: list, t, m, b1, b2, b3, a, a2, K, c, c1, c2, k1,
          k2, k3, r, beta):
    S, I, Y, C = z
    N = S + I + Y + C

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

def ode_solver(t: int, initial_conditions: list, params=None):
    initS, initI, initY, initC = initial_conditions
    #m, b1, b2, b3, a, a2, K, c, c1, c2, k1, k2, k3, r, beta = params
    result = odeint(ode_model, [initS, initI, initY, initC], t,
                    args=(m, b1, b2, b3, a, a2, K, c, c1, c2, k1, k2, 
                          k3, r, beta))
    return result

def main(initS, initI, initY, initC, m, b1, b2, b3, a, a2, K, c, 
         c1, c2, k1, k2, k3, r, beta, days):
        initial_conditions = [initS, initI, initY, initC]
        params = [m, b1, b2, b3, a, a2, K, c, c1, c2, k1, k2, k3, 
                  r, beta]
        tspan = np.arange(0, days, 1)
        sol = ode_solver(tspan, initial_conditions, params)
        S, I, Y, C = sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3]

        
        if days <= 30:
            step = 1
        elif days <= 90:
            step = 7
        else:
            step = 30


        #external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

        app = dash.Dash()
        server = app.server
        app.layout = html.Div(children=[
            html.H1(children='SIYC Model Simulation'),
            html.Div(children='''Simulation'''),
            dcc.Graph(
                id='example-graph',
                figure={
                    'data': 
                        [go.Scatter(x=tspan, 
                                    y=S, 
                                    mode='lines',
                                    name='S'),
                         go.Scatter(x=tspan,
                                    y=I,
                                    mode='lines',
                                    name='I'),
                         go.Scatter(x=tspan,
                                    y=Y, 
                                    mode='lines',
                                    name='Y'),
                         go.Scatter(x=tspan, 
                                    y=C,
                                    mode='lines',
                                    name='C')],
                    'layout':
                        go.Layout(title='Simulation of SIYC Model',
                                  xaxis_title='Day',
                                  yaxis_title='Counts',
                                  title_x=0.5, 
                                  width=800,
                                  height=700)
                },
                responsive=True)
        ])

        app.run_server(debug=True,
                       port=8000,
                       host='127.0.0.1')
        

if __name__ == '__main__':

    # Constants
    m = 0.25
    b1 = 0.5
    b2 = 0.5
    b3 = 0.01
    a = 2
    a2 = 0.75
    K = 100
    c = 0.5
    c1 = 0.01
    c2 = 0.25
    k1 = 1
    k2 = 0.5
    k3 = 98
    r = 1
    beta = 0.1

    S, I, Y, C = 1, 1, 2, 95

    main(S, I, Y, C, m, b1, b2, b3, a, a2, K, c, c1, c2, k1, k2,
         k3, r, beta, 30)
