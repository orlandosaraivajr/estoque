from django.test import TestCase
from .models import Produto, Categoria


class ProdutoModelTest(TestCase):
    def setUp(self):
        self.produto = Produto(
            ncm = '12345678',
            produto = 'Celular XingLing',
            preco = 1000.00,
            estoque = 10,
        )
        self.produto.save()

    def test_create(self):
        self.assertTrue(Produto.objects.exists())

    def test_type_data(self):
        self.assertEquals(self.produto.data, None)
        
    def test_importado(self):
        self.assertIsInstance(self.produto.importado, bool)
        self.assertFalse(self.produto.importado)

    def test_preco(self):
        self.assertEquals(self.produto.preco, 1000)

    def test_estoque(self):
        self.assertEquals(self.produto.estoque, 10)

    def test_estoque_minimo(self):
        self.assertEquals(self.produto.estoque_minimo, 0)
    
    def test_str(self):
        self.assertEqual(str(self.produto), 'Celular XingLing')

    def test_to_dict_json(self):
        json_esperado = {'pk': 1, 'produto': 'Celular XingLing', 'estoque': 10}
        self.assertIsInstance(self.produto.to_dict_json(), dict)
        self.assertEquals(self.produto.to_dict_json(), json_esperado)


class CategoriaModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria(
            categoria = 'celular',
        )
        self.categoria.save()
        self.produto = Produto(
            importado = True,
            ncm = '12345678',
            produto = 'Celular XingLing',
            preco = 1000.00,
            estoque = 10,
            categoria = self.categoria
        )
        self.produto.save()

    def test_create(self):
        self.assertTrue(Categoria.objects.exists())
        self.assertTrue(Produto.objects.exists())

    def test_type_data(self):
        self.assertEquals(self.produto.data, None)
        
    def test_importado(self):
        self.assertIsInstance(self.produto.importado, bool)
        self.assertTrue(self.produto.importado)

    def test_preco(self):
        self.assertEquals(self.produto.preco, 1000)

    def test_estoque(self):
        self.assertEquals(self.produto.estoque, 10)

    def test_estoque_minimo(self):
        self.assertEquals(self.produto.estoque_minimo, 0)
    
    def test_str(self):
        self.assertEqual(str(self.categoria), 'celular')


class View_produto_list_Test(TestCase):
    def setUp(self):
        self.resp = self.client.get('/produto')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'base.html')
        self.assertTemplateUsed(self.resp, 'includes/nav.html')
        self.assertTemplateUsed(self.resp, 'produto_list.html')
        
    def test_texto(self):
        self.assertContains(self.resp, 'Estoque')


class View_produto_add_Test(TestCase):
    def setUp(self):
        self.resp = self.client.get('/produtoadd')

    def test_301_response(self):
        self.assertEqual(301, self.resp.status_code)

class View_produto_add_Test2(TestCase):
    def setUp(self):
        self.resp = self.client.get('/produtoadd', follow=True)

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'base.html')
        self.assertTemplateUsed(self.resp, 'includes/nav.html')
        self.assertTemplateUsed(self.resp, 'produto_form2.html')
        
    def test_texto(self):
        self.assertContains(self.resp, 'Estoque')