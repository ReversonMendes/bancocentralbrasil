#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from bancocentral import Inflacao, Poupanca, Dolar, Euro, Selic

class TestCase(unittest.TestCase):

    def setUp(self):
        self.inflacao = Inflacao()
        self.poupanca = Poupanca()
        self.dolar = Dolar()
        self.euro = Euro()
        self.selic = Selic()

    """ Inflação """
    def test_inflacao_meta(self):
        self.assertIsNotNone(self.inflacao.get_meta_tax())

    def test_inflacao_meta_maior_zero(self):
        self.assertTrue(self.inflacao.get_meta_tax() > 0)

    def test_inflacao_acumulada(self):
        self.assertIsNotNone(self.inflacao.get_acumulada_tax())

    def test_inflacao_acumulada_maior_zero(self):
        self.assertTrue(self.inflacao.get_acumulada_tax() > 0)

    """ Poupança """
    def test_poupanca(self):
        self.assertIsNotNone(self.poupanca.get_poupanca_tax())

    def test_poupanca_maior_zero(self):
        self.assertTrue(self.poupanca.get_poupanca_tax() > 0)

    """ Dólar """
    def test_dolar_compra(self):
        self.assertIsNotNone(self.dolar.get_dolar_compra())

    def test_dolar_compra_maior_zero(self):
        self.assertTrue(self.dolar.get_dolar_compra() > 0)

    def test_dolar_venda(self):
        self.assertIsNotNone(self.dolar.get_dolar_venda())

    def test_dolar_venda_maior_zero(self):
        self.assertTrue(self.dolar.get_dolar_venda() > 0)

    """ Euro """
    def test_euro_compra(self):
        self.assertIsNotNone(self.euro.get_euro_compra())

    def test_euro_compra_maior_zero(self):
        self.assertTrue(self.euro.get_euro_compra() > 0)

    def test_euro_venda(self):
        self.assertIsNotNone(self.euro.get_euro_venda())

    def test_euro_venda_maior_zero(self):
        self.assertTrue(self.euro.get_euro_venda() > 0)

    """ Taxa Selic """
    def test_selic_meta(self):
        self.assertIsNotNone(self.selic.get_selic_meta())

    def test_selic_meta_maior_zero(self):
        self.assertTrue(self.selic.get_selic_meta() > 0)

    def test_selic_real(self):
        self.assertIsNotNone(self.selic.get_selic_real())

    def test_selic_real_maior_zero(self):
        self.assertTrue(self.selic.get_selic_real() > 0)

if __name__ == '__main__':
    unittest.main()
