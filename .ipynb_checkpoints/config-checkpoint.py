import os

PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/blank/'
MODEL_DIR = os.path.join(PROJECT_ROOT_DIR, 'nn_models')
DATA_DIR = os.path.join(PROJECT_ROOT_DIR, 'wav')
OUTPUT_DIR = os.path.join(PROJECT_ROOT_DIR, 'output')
