from . import models
from . import report

from . import hooks

def pre_init_hook(cr):
    hooks.pre_init_hook(cr)

def post_init_hook(cr, registry):
    hooks.post_init_hook(cr, registry)
