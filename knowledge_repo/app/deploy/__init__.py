import logging

from .common import KnowledgeDeployer, get_app_builder

# The following subclasses of KnowledgeDeployer must be
# imported in order to be registered as a deployer and hence
# made accessible using `KnowledgeDeployer.using(..)`.
from .flask import FlaskDeployer
from .uwsgi import uWSGIDeployer

# Wrap the gunicorn deployer in a try/except block, as it
# has a hard dependency on gunicorn which does not work on
# non-POSIX systems, or if it is not installed.
try:
    from .gunicorn import GunicornDeployer
except ImportError:
    pass
