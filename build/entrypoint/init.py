#!/usr/bin/env python3
import config
import logging
import os
import parser
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format="%(message)s")

try:
    arguments = parser.parse()
    setup = config.Setup(arguments)
    setup.arguments()
    path = os.path.expanduser('~/.ipython/profile_default/startup')
    os.makedirs(path, exist_ok=True)
    file = os.path.join(path,"disable-warnings.py")

    f = open(file, 'w')
    f.writelines(["import warnings\n", "warnings.filterwarnings('ignore')"])
    f.close()

    os.system("/usr/local/bin/$JUPYTER_ARGS")
except:
    logging.exception('failed!')
