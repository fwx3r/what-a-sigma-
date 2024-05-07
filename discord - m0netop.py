import os
import webbrowser

os.system("title discord - m0netop")

def check_app_name():
    file_path = os.path.basename(__file__)
    if file_path != "discord - m0netop.py":
        raise Exception("Ошибка: Название приложения было изменено!")

if __name__ == "__main__":
    check_app_name()

print("Какой сайт вы хотите открыть?")
print("1. VK")
print("2. YouTube")
print("3. Spotify")
print("4. Github")
print("5. what a sigma?")
print("6. ALL")

choice = input("Введите номер выбранного сайта: ")

if choice == "1":
    webbrowser.open("https://www.vk.com")
elif choice == "2":
    webbrowser.open("https://www.youtube.com")
elif choice == "3":
    webbrowser.open("https://www.spotify.com")
elif choice == "4":
    webbrowser.open("https://www.github.com")
elif choice == "5":
    webbrowser.open("https://www.google.com/search?q=what+a+sigma")
elif choice == "6":
    webbrowser.open("https://www.vk.com")
    webbrowser.open("https://www.youtube.com")
    webbrowser.open("https://www.spotify.com")
    webbrowser.open("https://www.github.com")




