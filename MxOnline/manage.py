#!/usr/bin/env python
import os
import sys

#C:\Users\Administrator\Envs\mxonline\Scripts
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxOnline.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
