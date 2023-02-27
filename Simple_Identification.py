import sys

def identification(nome: str, apelido: str, idade: int, email: str, telemovel: int):
    print(f"\nChamas-te {nome} {apelido}")
    print(f"Tens {idade} anos")
    print(f"Os teus contactos são: telemovel {telemovel} e o Email {email}\n")
    

# Usage:     Simple_Identification.py [Alex] [Jan] [51] [alex@gmail.com] [211234567]
identification(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]))   

# identification(input("\nQual o teu promeiro nome? "), 
#                input("Qual o teu apelido? "),
#                input("Qual é a tua idade? "),
#                input("Qual o teu email? "),
#                input("E qual o teu número de telemóvel? "))
               
               



  