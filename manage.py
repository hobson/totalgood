#!/usr/bin/env python
import os
import sys

PROJECT_NAME = os.path.basename(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), PROJECT_NAME))

sys.path.insert(0, PROJECT_ROOT)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
