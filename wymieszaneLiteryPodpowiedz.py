# Popraw program Wymieszane litery tak, żeby każdemu słowu towarzyszyła
# podpowiedź. Gracz powinien mieć możliwość zobaczenia podpowiedzi, jeśli
# utknie w martwym punkcie. Dodaj system punktacji, który nagradza graczy
# rozwiązujących anagram bez uciekania się do podpowiedzi.


# Wymieszane litery
# Komputer wybiera losowo słowo, a potem miesza w nim litery
# Gracz powinien odgadnąć pierwotne słowo

import random

WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")

#wybieram losowo jedno słowo
word = random.choice(WORDS)
correct = word
point = 0

#utwórz pomieszaną wersje słowa
jumble = ""

def pokazSlowo(correct):
    podpowiedz = ""
    word = correct
    for litera in word:
        if(random.randint(0, 1)):
            podpowiedz += litera
        else:
            podpowiedz += "_"
    return podpowiedz

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

#rozpocznij grę
print("""
            Witaj w grze 'Wymieszane litery'!
    Uporządkuj litery aby odtworzyć prawidłowe słowo
""")

print("Zgadnij, jakie to słowo", jumble)

guess = input("\nTwoja odpowiedz: ")
while(correct != guess and guess != ""):
    print("niestety to nie to słowo.")
    podpowiedz = input('czy potrzebujesz podpowiedzi (t/n): ')
    if(podpowiedz == 'n'):
        continue
        point += 1
    elif(podpowiedz == 't'):
        print("Podpoweidź:", pokazSlowo(correct))
        point -= 0
    else:
        continue
    guess = input("Twoja odpowiedz: ")

    if(guess == correct):
        print("Gratulacje zgadłeś")
        point += 1

print("Dziękuję za udział w grze.")
print(f"Zdobyłeś {point} punktów.")
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

pokazSlowo(word)