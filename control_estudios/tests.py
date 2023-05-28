from django.test import TestCase
from control_estudios.models import Noticias


class NoticiasTests(TestCase):
    def test_creacion_noticia(self):
        noticia = Noticias(titular="Titulo", subtitulo='subtitulo', autor='admin',cuerpo='cuerpo', categoria='anime')
        noticia.save()

        self.assertEqual(Noticias.objects.count(), 1)
        self.assertIsNotNone(noticia.id)
        self.assertEqual(noticia.titular, "Titulo")
        self.assertEqual(noticia.subtitulo, 'subtitulo')

    def test_noticia_str(self):
        noticia = Noticias(titular="Noticia Python", subtitulo='subtitulo', autor='admin',cuerpo='cuerpo', categoria='anime')
        noticia.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(noticia.__str__(), "Noticia Python | admin")