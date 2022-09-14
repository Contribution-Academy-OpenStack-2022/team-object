# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from openstack import resource


class MetadefObject(resource.Resource):
    resources_key = 'objects'
    base_path = '/metadefs/namespaces/%(namespaces_name)s/objects'

    # capabilities
    allow_create = True
    allow_fetch = True
    allow_commit = True
    allow_delete = True
    allow_list = True

    # Store all unknown attributes under 'properties' in the object.
    # Remotely they would be still in the resource root
    _store_unknown_attrs_as_properties = True

    _query_mapping = resource.QueryParameters(
        "namespace",
        "name",
        "description",
        "properties",
        "required",
        "created_at",
        "schema",
        "self",
        "updated_at",
    )

    namespace = resource.Body("namespace")
    name = resource.Body("name")
    description = resource.Body("description")
    properties = resource.Body("properties")
    required = resource.Body("required")
    created_at = resource.Body("created_at")
    schema = resource.Body("schema")
    self = resource.Body("self")
    updated_at = resource.Body("updated_at")