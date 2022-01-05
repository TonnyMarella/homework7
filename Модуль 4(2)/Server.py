import socket
import webbrowser
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 5050))

server.listen()

while True:
    user, adres = server.accept()

    while True:
        date = user.recv(1024).decode("utf-8").lower()
        print(date)

        if date == "youtube":
            webbrowser.open("https://www.youtube.com/")
        elif date == "google":
            webbrowser.open("https://www.google.com")
        elif date == "viber":
            os.startfile("C:/Users/Admin/AppData/Local/Viber/Viber.exe")
        elif date == "pogoda":
            webbrowser.open("https://www.gismeteo.ua/weather-kyiv-4944/")