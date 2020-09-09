from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item, List

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')  
        self.assertTemplateUsed(response, 'home.html') 

class ListAndItemModelsTest(TestCase):

    def test_saving_and_retrieving_items(self):
        my_list = List()
        my_list.save()

        first_item = Item()
        first_item.text = 'O primeiro item'
        first_item.list = my_list
        first_item.save()

        second_item = Item()
        second_item.text = 'O segundo item'
        second_item.list = my_list
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, my_list)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'O primeiro item')
        self.assertEqual(first_saved_item.list, my_list)
        self.assertEqual(second_saved_item.text, 'O segundo item')
        self.assertEqual(second_saved_item.list, my_list)

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')


    def test_displays_all_items(self):
        my_list = List.objects.create()

        Item.objects.create(text='itemey 1', list=my_list)
        Item.objects.create(text='itemey 2', list=my_list)

        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
