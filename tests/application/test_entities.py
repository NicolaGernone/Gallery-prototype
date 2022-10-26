from django.test import TestCase
from model_bakery import baker

from api.infrastructure.models import *

class PingViewTest(TestCase):

    def setUp(self) -> None:
        self.image = baker.make(Image)
        self.event = baker.make(Event)
        self.category = baker.make(Category)

    def test_simple_event(self) -> None:
        simple_event = baker.make('Event')
        assert simple_event

    def test_simple_event(self) -> None:
        simple_image = baker.make('Image')
        assert simple_image

    def test_simple_event(self) -> None:
        simple_category = baker.make('Category')
        assert simple_category

    def test_image_fields(self) -> None:
        image = self.image

        self.assertEqual(str(image), "Image: {}, {}, {}, {}".format(image.id, image.name, image.categories, image.created_at))
        self.assertNotEqual(str(image), "{} {}".format(image.id, image.created_at))

    def test_event_fields(self) -> None:
        event = self.event

        self.assertEqual(str(event), "Event: clicks {}, views {}, weight {}".format(event.view, event.click, event.weight))
        self.assertNotEqual(str(event), "ent: clicks {}, views {}".format(event.view, event.click))

    def test_category_fields(self) -> None:
        category = self.category

        self.assertEqual(str(category), "Category: {}".format(category.name))
        self.assertNotEqual(str(category), ": name {}".format(category.name))