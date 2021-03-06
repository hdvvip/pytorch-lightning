import os

import numpy as np

TEST_ROOT = os.path.dirname(__file__)
PROJECT_ROOT = os.path.dirname(TEST_ROOT)
TEMP_PATH = os.path.join(PROJECT_ROOT, 'test_temp')

if PROJECT_ROOT not in os.getenv('PYTHONPATH', ""):
    os.environ['PYTHONPATH'] = f'{PROJECT_ROOT}:{os.environ.get("PYTHONPATH", "")}'

# generate a list of random seeds for each test
RANDOM_PORTS = list(np.random.randint(12000, 19000, 1000))

if not os.path.isdir(TEMP_PATH):
    os.mkdir(TEMP_PATH)
