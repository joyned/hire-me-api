import os
import sys

import yaml

root = os.path.abspath(os.path.dirname(sys.argv[0]))


def get_resource_file(file_name):
    return yaml.safe_load(open(os.path.join(root, 'resource', file_name)))
