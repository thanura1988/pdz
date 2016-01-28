from tugboat.core import events
from tugboat.deployment.app.tasks import activate

def activate_app(version, result, *args, **kwargs):
    activate.run(version, **kwargs)

events.add_listener(events.EventNames.POST_APP_DEPLOY, activate_app)
