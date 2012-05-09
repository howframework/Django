#!/usr/bin/env python

#!/usr/bin/env python
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'app'))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "openshift.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
