# PHSX 815: Week 12
## Gaussian Kernel Density Estimation

This repository includes a script that demonstrates a method of estimating density from a set of generated data. 

---

### Homework 13:

### Running the Code
The construction plots are made by the `Kernel.py` python file. This file requires python3 to run, and includes the following packages listed at the top of the script:

```
  import sys
  import numpy as np
  import matplotlib.pyplot as plt
```

To run this script from the terminal in linux, run:

> $ python3 Kernel.py

This runs the file with the default parameters which is seed number 555 for the Random algorithm. This can be changed from the terminal, as with the number of experiments.

For example, it may looks something like this in linux:

> $ python3 Kernel.py -seed 486 -Nexp 1000

which would run the algorithm with an initial seed value of 486 instead of the default 555 and the number of experiments as 1000 instead of the default 100.

### The Output

The script first outputs the raw data and densities in a plot.

![hw13](https://user-images.githubusercontent.com/76142511/235572316-27ba4f21-3e59-4932-b330-0b378b4d8847.png)

