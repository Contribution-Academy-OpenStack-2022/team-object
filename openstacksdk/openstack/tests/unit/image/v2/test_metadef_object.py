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

from openstack.image.v2 import metadef_object
from openstack.tests.unit import base


EXAMPLE = {
    'created_at': '2014-09-19T18:20:56Z',
    'description': 'You can configure the CPU limits with control parameters.',
    'name': 'CPU Limits',
    'properties': {
        'quota:cpu_period': {
            'description': "Specifies the enforcement interval (unit: microseconds) for QEMU and LXC hypervisors. Within a period, each VCPU of the domain is not allowed to consume more than the quota worth of runtime. The value should be in range [1000, 1000000]. A period with value 0 means no value.",
            'maximum': 1000000,
            'minimum': 1000,
            'title': 'Quota: CPU Period',
            'type': 'integer'
        },
        'quota:cpu_quota': {
            'description': 'Specifies the maximum allowed bandwidth (unit: microseconds). A domain with a negative-value quota indicates that the domain has infinite bandwidth, which means that it is not bandwidth controlled. The value should be in range [1000, 18446744073709551] or less than 0. A quota with value 0 means no value. You can use this feature to ensure that all vCPUs run at the same speed.',
            'title': 'Quota: CPU Quota',
            'type': 'integer'
        },
        'quota:cpu_shares': {
            'description': 'Specifies the proportional weighted share for the domain. If this element is omitted, the service defaults to the OS provided defaults. There is no unit for the value; it is a relative measure based on the setting of other VMs. For example, a VM configured with value 2048 gets twice as much CPU time as a VM configured with value 1024.',
            'title': 'Quota: CPU Shares',
            'type': 'integer'
        }
    },
    'required': [],
    'updated_at': '2014-09-19T18:20:56Z'
}


class TestMetadefObject(base.TestCase):
    def test_basic(self):
        sot = metadef_object.MetadefObject()
        self.assertIsNone(sot.resource_key)
        self.assertEqual('objects', sot.resources_key)
        self.assertEqual('/metadefs/namespaces/%(namespace)s/objects', sot.base_path)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_fetch)
        self.assertTrue(sot.allow_commit)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = metadef_object.MetadefObject(**EXAMPLE)
        self.assertEqual(EXAMPLE['created_at'], sot.created_at)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['properties'], sot.properties)
        self.assertEqual(EXAMPLE['required'], sot.required)
        self.assertEqual(EXAMPLE['updated_at'], sot.updated_at)
        self.assertDictEqual(
            {
                'limit': 'limit',
                'marker': 'marker',
                'namespace_name': 'namespace_name',
                'name': 'name',
                'description': 'description',
                'properties': 'properties',
                'required': 'required',
                'created_at': 'created_at',
                'schema': 'schema',
                'updated_at': 'updated_at'
            }, sot._query_mapping._mapping)
