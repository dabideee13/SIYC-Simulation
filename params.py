import csv

from utils import get_values, map_to_none


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

    # Returns the whole parameter data
    return get_values(**inputs)


if __name__ == '__main__':
    print(main())
