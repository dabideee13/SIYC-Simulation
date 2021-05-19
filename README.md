# SIYC-Simulation

## Table of Contents
- [Installation](#Installation)
  * [MacOS](#MacOS)
  * [Ubuntu](#Ubuntu)
  * [Windows](#Windows)
- [Usage](#Usage)
- [Example](#Example)
- [License](#License)

## Installation ([MacOS](#MacOS), [Ubuntu](#Ubuntu) and [Windows](#Windows))
### MacOS 

Make sure you have Python 3.7.7 and [virtualenv](https://pypi.org/project/virtualenv/) installed.

Create a new directory for this project.
```
$ mkdir new_project
$ cd new_project
```

Create an isolated environment for this project to avoid package conflicts during installation.
```
$ virtualenv venv
$ source venv/bin/activate
```

Clone this repository locally.
```
$ git clone https://github.com/dabideee13/SIYC-Simulation.git 
```

Install the necessary packages for this project.
```
$ cd SIYC-Simulation
$ pip install -r requirements.txt
```

### Ubuntu
### Windows

## Usage

In terminal:

If using default parameter values, run simulation.py.
```
$ python simulation.py
```

If not using default parameter values, input or change parameter values in the first row of input.csv then run simulation.py.
```
$ python simulation.py
```

To view current parameter settings (values), run [params.py](params.py) or open [param_values.txt](param_values.txt).
```
$ python params.py
```

## Example
```
$ python simulation.py
```
![Simulation results for 30 days](plot.png)


## License
### Code
MIT License: https://dabideee13.mit-license.org/ or see the [LICENSE](LICENSE) file.
