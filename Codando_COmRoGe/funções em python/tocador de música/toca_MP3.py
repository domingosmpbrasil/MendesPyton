from playsound import playsound
import pygame

# Função para tocar música

def miuzick(opc):
    match opc:
        case 1:
            return playsound('1.mp3')

        case 2:
            return playsound('2.mp3')

        case 3:
            return playsound('3.mp3')

        case _:
            return print("fim do programa")

