import unittest
from scr.elementos_finitos_ex1 import funcao, grad_num_f
from libnumpy.matrizes import soma
from elementos_finitos.o_tal_do_teste import x,y


class TestGrad(unittest.TestCase):
    def test_retorno_da_derivada(self):
        self.assertEqual(funcao(10),10)

    def test_retorno_derivada_num(self):
        self.assertEqual(grad_num_f(17),1.000000082740371)

    def test_soma_de_matriz(self):
        self.assertEqual(soma(x,y),)



