from django.test import TestCase
from django.contrib.auth.models import User
from core.models import TimeStampedModel
from produto.models import Produto, Categoria
from .models import Estoque, EstoqueItens


class EstoqueModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="foo", password="bar")
        self.estoque = Estoque(
            funcionario=self.user,
            nf=1, movimento='e',)
        self.estoque.save()
        self.estoque2 = Estoque(
            funcionario=self.user,
            movimento='s',)
        self.estoque2.save()

    def test_create(self):
        self.assertIsInstance(self.estoque, TimeStampedModel)
        self.assertTrue(User.objects.exists())
        self.assertTrue(Estoque.objects.exists())

    def test_movimento(self):
        self.assertEquals(self.estoque.movimento, 'e')
        self.assertEquals(self.estoque2.movimento, 's')

    def test_str(self):
        dt = self.estoque.created.strftime('%d-%m-%Y')
        self.assertEquals(str(self.estoque), '1 - 1 - '+ dt)
        self.assertEquals(str(self.estoque2), '2 --- '+ dt)


class EstoqueItensModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="foo", password="bar")
        self.estoque = Estoque(funcionario=self.user,nf=1, movimento='e',)
        self.estoque.save()
        self.produto = Produto(
            ncm = '12345678', produto = 'Celular XingLing',
            preco = 1000.00, estoque = 10,)
        self.produto.save()
        self.estoqueItem = EstoqueItens(
            estoque=self.estoque,
            produto=self.produto,
            quantidade=2,
            saldo=8)
        self.estoqueItem.save()

    def test_create(self):
        self.assertIsInstance(self.estoque, TimeStampedModel)
        self.assertTrue(User.objects.exists())
        self.assertTrue(Estoque.objects.exists())
        self.assertTrue(EstoqueItens.objects.exists())

    def test_movimento_default(self):
        self.assertEquals(self.estoque.movimento, 'e')

    def test_str(self):
        self.assertEquals(str(self.estoqueItem), '1 - 1 - Celular XingLing')