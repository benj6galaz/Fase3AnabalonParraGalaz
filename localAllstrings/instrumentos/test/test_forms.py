from django.test import TestCase
from django.urls import reverse
from instrumentos.models import Instrumento, Producto


def test_get_template_reverse_isntrumento(self):

        instrumento = Instrumento.objects.create(nombre="Guitarra preciosa", descripcion="roja,bonita")
        response = self.client.get(reverse('instrumento-detail', kwargs={'pk':instrumento.pk}))
        self.assertEqual(response.status_code, 200)

def test_get_template_reverse_producto(self):
        producto = Producto.objects.create(nombre="bateria grande", descripcion="bateria azul, estable")
        response = self.client.get(reverse('producto-detail', kwargs={'pk':producto.pk}))
        self.assertEqual(response.status_code, 200)