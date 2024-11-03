#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Initialisation de l'EV3 Brick et des capteurs
ev3 = EV3Brick()
snirium_sensor = ColorSensor(Port.S3)
ultrasonic_sensor = UltrasonicSensor(Port.S2)
gyro_sensor = GyroSensor(Port.S4)


# Import du module
import socket


# Création des moteurs
left_m = Motor(Port.A, Direction.CLOCKWISE)
right_m = Motor(Port.C, Direction.CLOCKWISE)
medium_m = Motor(Port.B, Direction.CLOCKWISE)

# Création de la socket TCP
sds = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sds.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# Attachement de la socket
sds.bind(("0.0.0.0", 1665))

# Création d'une file d'attente pour les clients
sds.listen(5)

# Boucle de traitement
while True:
    # Attente de la connexion d'un client
    sdc, adresse = sds.accept()
    print("Nouveau clientE : {}".format(adresse))
    # Réception de données
    requete_octets = sdc.recv(1024)
    requete_str = requete_octets.decode("utf8")
    print(requete_str)

    # Traitement des commandes en fonction de la requête
    if requete_str[5] == "A":#Avancer
        left_m.run(500)
        right_m.run(500)
        reponse_str = "HTTP/1.1 200 OK\r\n\r\nOK"
        reponse_octets = reponse_str.encode("utf8")
        sdc.send(reponse_octets)
    elif requete_str[5] == "R":#Reculer
        left_m.run(-500)
        right_m.run(-500)
        reponse_str = "HTTP/1.1 200 OK\r\n\r\nOK"
        reponse_octets = reponse_str.encode("utf8")
        sdc.send(reponse_octets)
    elif requete_str[5] == "G":  # Tourner à gauche
        left_m.run(-500)
        right_m.run(500)
        reponse_str = "HTTP/1.1 200 OK\r\n\r\nOK"
        reponse_octets = reponse_str.encode("utf8")
        sdc.send(reponse_octets)
    elif requete_str[5] == "D":#Tourner à droite
        left_m.run(500)
        right_m.run(-500)
        reponse_str = "HTTP/1.1 200 OK\r\n\r\nOK"
        reponse_octets = reponse_str.encode("utf8")
        sdc.send(reponse_octets)
    elif requete_str[5] == "X":#Lever la barre
        medium_m.run(-1000)
        wait(1000)
        medium_m.stop()
        reponse_str = "HTTP/1.1 200 OK\r\n\r\nOK"
        reponse_octets = reponse_str.encode("utf8")
        sdc.send(reponse_octets)
    elif requete_str[5] == "Y":#Baisser la barre
        medium_m.run(+1000)
        wait(1000)
        medium_m.stop()
        reponse_str = "HTTP/1.1 200 OK\r\n\r\nOK"
        reponse_octets = reponse_str.encode("utf8")
        sdc.send(reponse_octets)
    elif requete_str[5] == "T":#Tourner
        left_m.run(-500)
        right_m.run(500)
        reponse_str = "HTTP/1.1 200 OK\r\n\r\nOK"
        reponse_octets = reponse_str.encode("utf8")
        sdc.send(reponse_octets) 
    elif requete_str[5] == "S":#Stop
        left_m.stop()
        right_m.stop()
        reponse_str = "HTTP/1.1 200 OK\r\n\r\nOK"
        reponse_octets = reponse_str.encode("utf8")
        sdc.send(reponse_octets)
    
    # Récupération des données du robot
    elif requete_str[5] == "?":
        #taux de snirium
        snirium = snirium_sensor.reflection()
        http_payload = '{"snirium":' + str(snirium)

        #angle
        angle = gyro_sensor.angle()
        http_payload += ',"angle":' + str(angle)
        
        #moteur gauche
        moteur_gauche = left_m.angle()
        http_payload += ',"moteur_gauche":' + str(moteur_gauche)

        #moteur droite 
        moteur_droite = right_m.angle()
        http_payload += ',"moteur_droite":' + str(moteur_droite)
        
        #Distance avec l'obstacle
        distance_to_obstacle = ultrasonic_sensor.distance()
        http_payload += ',"distance":' + str(distance_to_obstacle) + '}'
        http_header = "HTTP/1.1 200 OK\r\n"
        http_header += "Content-Length: {}\r\n".format(len(http_payload))
        http_header += "Access-Control-Allow-Origin:*\r\n"
        http_header += "Content-Type: application/json; charset=UTF-8\r\n\r\n"

        reponse_str = http_header + http_payload
        reponse_octets = reponse_str.encode("utf8")
        print(reponse_octets)
        sdc.send(reponse_octets)
  
    else:
        print("???")
    
   

    # Fermeture de la connexion
    sdc.close()

# Fermeture de la socket
sds.close()
