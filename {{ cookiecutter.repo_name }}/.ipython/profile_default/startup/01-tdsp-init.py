import logging.config

global np
global pd
global os

try:
    import pandas as pd
    import numpy as np
except ImportError:
    logging.error(
        "Numpy or Pandas appear not to have been installed in your current environment"
    )

if np is not None:
    logging.info("Defined global variable `np`, `pd` and `os`")
else:
    logging.info("Defined global variable `os`")
