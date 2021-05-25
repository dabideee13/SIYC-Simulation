# -*- coding: utf-8 -*-
"""
Utility functions for SIYC Simulation
"""

from typing import Dict, Union

import pandas as pd
import plotly.graph_objects as go


def get_values(**constants) -> Dict[str, Union[float, int]]:

    defaults = {
        't': 30,
        'S': 1,
        'I': 1,
        'Y': 2,
        'C': 95,
        'm': 0.25,
        'b1': 0.5,
        'b2': 0.5,
        'b3': 0.01,
        'a': 2,
        'a2': 0.75,
        'K': 100,
        'c': 0.5,
        'c1': 0.01,
        'c2': 0.25,
        'k1': 1,
        'k2': 0.5,
        'k3': 98,
        'r': 1,
        'beta': 0.1
    }

    common_keys = set(defaults.keys()).intersection(set(constants.keys()))

    for key in common_keys:
        defaults[key] = eval(constants[key])

    return defaults


def map_to_none(inputs: dict) -> dict:
    return {key: None for key, val in inputs.items() if val == ''}


def plot_results(data: pd.DataFrame):

    fig = go.Figure()
    for col in data:
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data.loc[:, col],
                mode='lines',
                name=col
            )
        )
    return fig.show()
