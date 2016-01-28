import fabric, os, time, json, sys
from fabric.api import local, sudo, run , env
from urllib import urlopen
from tugboat.utils import tugboat_context as __tugboat_context
from tugboat.deployment import operations, events
from tugboat.deployment.app.operations import app_servers as __app_servers
from tugboat.decorators import deployment
from tugboat.core.operations import clone_git_repo
from tugboat.utils.logging_tools import puts_prefixed as log


@fabric.api.task
@deployment.task
def configure(*args,**kwargs):
     print("Getting web server IPs ")
     deployEnvironment = __tugboat_context.get_environment()
     appName =  __tugboat_context.get_app_name()
     config = __tugboat_context.get_infrastructure()
     hosts = __app_servers.find(*args, **kwargs)
     if len(hosts) < 1:
        log('Unable to locate any hosts to deploy product data to', 'Product Data')
        raise ValueError('No hosts found to deploy product data to')
     ip = list(set(hosts))
     f=open('hosts', 'w')
     print >> f,"[webservers]"
     for host in hosts:
        #print(host)
        print >> f,(host)
     f.close()
