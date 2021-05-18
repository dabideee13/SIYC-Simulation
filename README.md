# SIYC-Simulation

## Table of Contents
- [Installation](#Installation)
  * [MacOS](#MacOS)
  * [Ubuntu](#Ubuntu)
  * [Windows](#Windows)
- [Usage](#Usage)
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

If using default parameter values, simply run simulation.py.
```
$ python simulation.py
```

If not using default parameter values, input or change parameter values in the first row of input.csv then run simulation.py.
```
$ python simulation.py
```

## License
### Code
MIT License: https://dabideee.mit-license.org/ or see the LICENSE file.
