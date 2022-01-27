from django.test import TestCase

class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'base.html')
        self.assertTemplateUsed(self.resp, 'includes/nav.html')
        self.assertTemplateUsed(self.resp, 'index.html')
        
    def test_texto(self):
        self.assertContains(self.resp, 'Estoque')
        