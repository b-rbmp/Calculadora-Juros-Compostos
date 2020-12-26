import unittest
import requests
from dev.calculos import calculo_juros_compostos

class TestFlask(unittest.TestCase):
     def test_web_app_running(self):
        try:
             r = requests.get("http://127.0.0.1:5000/")
        except:
            self.fail("Nao pode acessar o web app. Teste falhou")

class TestCalculos(unittest.TestCase):
     def test_calculos(self):
         dados = calculo_juros_compostos(100, 10, 1, 12)
         capital_final = dados[-1, 0]
         juros_mensais_ao_fim = dados[-1, 1]
         juros_acumulados = dados[-1, 2]
         self.assertEqual(capital_final, 239.48)
         self.assertEqual(juros_mensais_ao_fim, 2.27)
         self.assertEqual(juros_acumulados, 19.48)
         

if __name__ == "__main__":
    unittest.main(warnings='ignore', failfast = True)