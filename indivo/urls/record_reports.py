from django.conf.urls.defaults import *

from indivo.views import *
from indivo.lib.utils import MethodDispatcher

urlpatterns = patterns('',
  (r'^experimental/ccr$', 
   MethodDispatcher({'GET':report_ccr})),
  (r'^(?P<data_model>[^/]+)/$', 
   MethodDispatcher({'GET':generic_list})),
)
