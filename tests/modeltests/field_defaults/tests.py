from __future__ import absolute_import

from datetime import datetime

from django.test import TestCase
from django.utils import six

from .models import Article


class DefaultTests(TestCase):
    def test_field_defaults(self):
        a = Article()
        now = datetime.now()
        a.save()

        self.assertTrue(isinstance(a.id, six.integer_types))
        self.assertEqual(a.headline, "Default headline")
        self.assertTrue((now - a.pub_date).seconds < 5)
