import toca_MP3
import pygame
import playsound


print("Bem vindos!")

while True:
    toca_musica = int(input("digite 1, 2 ou 3  para ouvir a musica :"))

    toca_MP3.miuzick(toca_musica)
    print("para parar digite 4")
    if toca_musica == 4:
        print("fim do programa. ")
        break


