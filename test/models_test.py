# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Tests for app.models
"""
from app import config
from app import models

from test import base

class BlobKeyMappingTests(base.BlobMigratorTestCase):
  """
  Tests for BlobKeyMapping
  """
  def test_get_kind_uses_configuration(self):
    config.config.MAPPING_DATASTORE_KIND_NAME = 'foo'
    kind = models.BlobKeyMapping._get_kind()
    self.assertEquals('foo', kind)

  def test_build_key_uses_correct_kind(self):
    key = models.BlobKeyMapping.build_key('abc123')
    self.assertEquals(config.config.MAPPING_DATASTORE_KIND_NAME, key.kind())

  def test_build_key_uses_provided_id(self):
    key = models.BlobKeyMapping.build_key('abc123')
    self.assertEquals('abc123', key.id())

  def test_build_key_id_is_required(self):
    with self.assertRaises(ValueError):
      models.BlobKeyMapping.build_key('')
    with self.assertRaises(ValueError):
      models.BlobKeyMapping.build_key(None)
