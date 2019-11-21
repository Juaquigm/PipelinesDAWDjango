from django.test import TestCase
from .models import Curso
#Test para modelos
class TestCurso(TestCase):
    def setUp(self):
        Curso.objects.create(abrev='DAW',denom='Desarrollo de aplicaciones web')
        Curso.objects.create(abrev='Mate',denom='Matematicas Básicas')
    
    def TestCursoNombre(self):
        abrev1 = Curso.objects.get(abrev='DAW')
        abrev2 = Curso.objects.get(abrev='Mate')
        self.assertEqual(abrev1.abrev, 'DAW')
        self.assertEqual(abrev2.abrev, 'Mates')
        



