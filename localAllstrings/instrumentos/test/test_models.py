from django.test import TestCase
from instrumento.models import Instrumento

class InstrumentoTestCase(TestCase):
    @classmethod

    def setUpTestData(cls):
        test_instrumento = Instrumento.objects.create(id='66019d35-b2db-4e65-be38-85deda5e7cd2', nombre='Micrófono de conferencia Itc T-4012', descripcion='Se conectan mediante un puerto RJ45 a través de un cable CAT5, se pueden conectar en cascada un máximo de 6 micrófonos juntos para un amplificador. El micrófono está integrado en un selector de timbre de dos y cuatro tonos, está alimentado por un amplificador a 24 V CC')

    def test_nombre_label(self):
        instrumento=Instrumento.objects.get(id='66019d35-b2db-4e65-be38-85deda5e7cd2')
        field_label = Instrumento._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

    def test_descripcion_label(self):
        instrumento=Instrumento.object.get(id='66019d35-b2db-4e65-be38-85deda5e7cd2')
        field_label = Instrumento._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label,'descripcion')
    
    def test_nombre_max_length(self):
        instrumento=Instrumento.objects.get(id='66019d35-b2db-4e65-be38-85deda5e7cd2')
        max_length = Instrumento._meta.get_field('nombre').max_length
        self.assertEquals(max_length,100)

    def test_descripcion_max_length(self):
        instrumento=Instrumento.objects.get(id='66019d35-b2db-4e65-be38-85deda5e7cd2')
        max_length = Instrumento._meta.get_field('descripcion').max_length
        self.assertEquals(max_length,5000)

    def test_get_absolute_url(self):
        instrumento=Instrumento.objects.get(id='66019d35-b2db-4e65-be38-85deda5e7cd2')
        self.assertEquals(instrumento.get_absolute_url(), '/instrumentos/instrumento/66019d35-b2db-4e65-be38-85deda5e7cd2')