# Portions (c) 2014, Alexander Klimenko <alex@erix.ru>
# All rights reserved.
#
# Copyright (c) 2011, SmartFile <btimby@smartfile.com>
# All rights reserved.
#
# This file is part of DjangoDav.
#
# DjangoDav is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DjangoDav is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with DjangoDav.  If not, see <http://www.gnu.org/licenses/>.
from djangodav.acl import FullAcl
from djangodav.lock import DummyLock

from djangodav.views import DavView

from django.conf.urls import patterns

from samples.fs.resource import TempDirWebDavResource
from samples.db.resource import MyDBDavResource


urlpatterns = patterns('',
    # Mirroring tmp folder
    (r'^fs(?P<path>.*)$', DavView.as_view(resource_class=TempDirWebDavResource, lock_class=DummyLock, acl_class=FullAcl)),
    # Db file keeper
    (r'^db(?P<path>.*)$', DavView.as_view(resource_class=MyDBDavResource, lock_class=DummyLock, acl_class=FullAcl)),
)
