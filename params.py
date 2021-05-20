# -*- coding: utf-8 -*-
import csv
import json

from utils import get_values, map_to_none


def wrangle_inputs(vars: list, vals: list):

    # Set values not defined by user to be None
    inputs = map_to_none(
        dict(
            zip(vars, vals)
        )
    )

    # Filter values only inputed by the user
    inputs = dict(
        filter(
            lambda x: x[1] is not None,
            inputs.items()
        )
    )

    return inputs


def main():

    # Import csv data inputed by the user
    with open('input.csv', newline='') as f:
        f = csv.reader(f)
        for i, line in enumerate(f):
            if i == 0:
                vars = line
            elif i == 1:
                vals = line
            else:
                break

    # Clean input data and set the right format
    inputs = wrangle_inputs(vars, vals)

    # Parameter values for the model
    param_values = get_values(**inputs)

    # Export current parameter values to .txt file
    with open('param_values.txt', 'w') as file:
        file.write(json.dumps(param_values))

    return param_values


if __name__ == '__main__':

    # Show parameter values in console or terminal
    print(main())
