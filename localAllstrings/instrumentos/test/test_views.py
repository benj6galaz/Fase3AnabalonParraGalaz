from django.test import TestCase
from django.urls import reverse
from instrumentos.models import Instrumento, Producto


#INSTRUMENTO
class InstrumentoListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_instrumento = 13

        for instrumento_id in range(number_of_instrumento):
            Instrumento.objects.create(
                nombre=f'Guitarra LesPaul {instrumento_id}',
                descripcion=f'Bonita {instrumento_id}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/instrumentos/instrumentos/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('instrumentos'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('instrumentos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'instrumentos/instrumento_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('instrumentos'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['instrumento_list']) == 10)

    def test_lists_all_intrumentos(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('instrumentos')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['instrumento_list']) == 3)

#PRODUCTO
class ProductoListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_producto = 13

        for producto_id in range(number_of_producto):
            Producto.objects.create(
                nombre=f'Guitarra LesPaul2 {producto_id}',
                descripcion=f'Bonita 2 {producto_id}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/instrumentos/producto/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'instrumentos/producto_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['producto_list']) == 10)

    def test_lists_all_productos(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('productos')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['producto_list']) == 3)


