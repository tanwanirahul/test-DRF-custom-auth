from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import Route, DefaultRouter
from myAuth.apiviews import ProfileViewSet, UserViewSet


admin.autodiscover()


router = DefaultRouter()
router.register("profiles", ProfileViewSet)
router.register("users", UserViewSet)

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'', include(router.urls))
                       )
