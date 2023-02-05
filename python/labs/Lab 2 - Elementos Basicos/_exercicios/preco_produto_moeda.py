"""
SÉRIE DE EXERCÍCIOS 2 

Faca um programa para calcular o preco de venda final de um produto. 
Para tal solicita, através da linha de comandos (shell), o preço do 
produto, o valor da taxa de IVA a aplicar e (opcionalmente) o valor 
de um desconto a aplicar ao valor final do produto. O programa deverá
dar instruções ao utilizador de como deve ser invocado. O valor do IVA 
e do desconto deve ser dado em percentagem.
"""

import sys
import locale
from decimal import Decimal as dec


if not 3 <= len(sys.argv) <= 4:
    print("Utilização: python3", __file__, "preco_sem_iva taxa_iva [desconto]")

else:
    preco_s_iva = dec(sys.argv[1])
    taxa_iva    = dec(sys.argv[2])
    desconto    = dec(sys.argv[3]) if len(sys.argv) == 4 else 0

    preco = preco_s_iva * ((100 + taxa_iva) / 100)
    preco_final = preco * (100 - desconto) / 100

    # Consultar: 
    #   https://docs.python.org/3/library/locale.html?#module-locale
    locale.setlocale(locale.LC_ALL, '') 
    print("Preço final: {}".format(locale.currency(preco_final)))

