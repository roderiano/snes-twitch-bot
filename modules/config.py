import yaml
import os

def get_config(module):
    with open('config.yaml', 'r') as stream:
        data = yaml.safe_load(stream)
        module = os.path.basename(module).split('.')[0]
        
        return data[module]
