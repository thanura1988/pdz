####################################
# Default Tugboat Fabric File
#
# Custom hooks are better defined in the hooks directory allowing for
# tugboat init to not overwrite them in an upgrade scenario
#####################################
import sys, os
from tugboat.deployment import *
from tugboat.deployment.app.tasks import activate, record_deployment
import fabric
import json
import urllib2
from datetime import datetime
from fabric.api import *
from fabric.colors import magenta
from fabric.network import *
from fabric.tasks import *
from tugboat.deployment import decorators
from tugboat.utils import tugboat_context as __tugboat_context
from tugboat.deployment.app.operations import app_servers as __app_servers

__all__ = ["app", "infrastructure", "full_deploy", "show_config", "full_undeploy","configure"]

#####################################
# Import External Hooks from Hooks Directory
#####################################
import_hooks(os.path.dirname(__file__))
@fabric.api.task
def configure(*args, **kwargs):
    sys.modules.get('hooks.app_custom').configure(*args, **kwargs)

