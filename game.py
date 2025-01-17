try:
    from pygame import mixer   # Import PyGame to play music in the background
    import playsound           # Import playsound to play the Game Over music not in the background
    import random
    import os
    import os.path
    import sys
    from langdetect import detect

    reset = "\u001b[0m"
    green_bg = "\u001b[42;1m"
    green = "\u001b[32;1m"
    red_bg = "\u001b[41;1m"
    red = "\u001b[31;1m"
    black = "\u001b[30;1m"
    underline = "\u001b[4m"
    orange = "\u001b[202m"

    lang_select = ""

    def clear():
        os.system("clear")

    def start():
        clear()
        print(green + underline + "TYPING GAME\n" + reset)
        print(red + "Preparing..." + reset)

        path = os.getcwd() + "/"
        lang_list = []
        language = ""

        if os.path.isfile(path + "words.txt"):
            file = open("words.txt", "r")
            file.readlines()

            file.seek(0)
            lines = 0

            for line in file:
                lines += 1

            for i in range(2000, 2050):
                word = random.randint(1, lines)

                for position, line in enumerate(file):
                    if position == word:
                        lang_list.append(line.strip("\n"))

                file.seek(0)

            file.close()

            detectlanguage = lang_list[0] + " " + lang_list[5] + " " + lang_list[10] + " " + lang_list[15] + " " + lang_list[20]
            language = detect(detectlanguage)


        clear()


        print(green + underline + "TYPING GAME\n" + reset)


        # List all available languages
        print("Current language: " + green + language)

        sys.stdout.write(reset + "Other languages: " + green)
        for fname in os.listdir("Languages/."):
            remove_chars = ["words", "(", ")"]

            filename, extension = fname.split(".")

            for char in remove_chars:
                filename = filename.replace(char, "")

            sys.stdout.write(filename + " ")



        lang_select = input(green + "\n\nChoose language > " + reset)

        if lang_select == language:
            main()

        else:
            if os.path.isfile(path + "words.txt"):
                os.system("mv words.txt words\(" + language + "\).txt")
                os.system("mv words\(" + language + "\).txt " + path + "Languages/")

            os.system("mv " + path + "Languages/words\(" + lang_select + "\).txt " + path)
            os.system("mv " + path + "words\(" + lang_select + "\).txt words.txt")

            main()



    def main():
        # Read words.txt file and choose words
        word_list = []
        failed_wordlist = []

        file = open("words.txt", "r")
        file.readlines()

        file.seek(0)
        lines = 0

        for line in file:
            lines += 1



        # Choose 500 words from the text file
        for i in range(500):
            loadingstat = str(len(word_list) / 5) + "%"
            clear()

            print(green + underline + "TYPING GAME\n" + reset)
            print(red + "Loading... " + reset + loadingstat)

            file.seek(0)
            word = random.randint(1, lines)

            for position, line in enumerate(file):
                if position == word:
                    word_list.append(line.strip("\n"))

        file.close()



        # Make a sentance of the words to detect the language easier
        detectlanguage = word_list[0] + " " + word_list[10] + " " + word_list[100]

        # Detect language
        language = detect(detectlanguage)

        # Game setup
        health = ["    ", "    ", "    ", "    ", "    "]
        health_lost = []

        current_word = 0
        completed_words = 0
        failed_words = 0




        # Game loop
        mixer.init()
        mixer.music.load("Music/song.mp3")
        mixer.music.play(loops=-1)
                
        while True:
            if failed_words != 5:
                clear()

                print(green + "TYPING GAME" + red + "\nLanguage: " + reset + language.upper())
                print(red + "\n-----------------------------------------\n" + reset)
                print("Correct words: " + str(completed_words) + "\nFailed words: " + str(failed_words))
                print()

                sys.stdout.write("Health: ")

                for healthlost in health_lost:
                    sys.stdout.write(red_bg + red + healthlost + reset)

                for healthremaining in health:
                    sys.stdout.write(green_bg + green + healthremaining + reset)

                print(red + "\n\n-----------------------------------------\n" + reset)


                for word in range(0, 5):
                    if word == current_word:
                        sys.stdout.write(underline + green + word_list[current_word] + reset + " ")

                    elif word in failed_wordlist:
                        sys.stdout.write(red + word_list[word]+ reset + " ")

                    else:
                        sys.stdout.write(word_list[word] + " ")
                        sys.stdout.flush()

                user_input = input("\n\n> ")

                if user_input == word_list[current_word]:
                    completed_words += 1
                    word_list.remove(word_list[current_word])

                else:
                    failed_words += 1
                    failed_wordlist.append(current_word)
                    health.pop(0)
                    health_lost.append("    ")
                    current_word += 1

            else:
                mixer.quit()

                while True:
                    playsound.playsound("Music/gameover.mp3")

                    clear()
                    print(underline + red + "Game Over!" + reset)
                    print("\nCorrect Words: " + str(completed_words))
                    print("Failed Words: " + str(failed_words))
                    print("\nC/F = " + str(completed_words / failed_words))
                    print()

                    print(red + "-----------------------------------------" + reset)
                    retry = input("Continue? [Y/N] > ")

                    if retry == "y" or retry == "Y":
                        clear()
                        main()
                        break

                    elif retry == "n" or retry == "N":
                        clear()
                        exit()
                        break


    start()



except(FileNotFoundError):
    clear()

    errormsg = green + underline + 'Language not found!\n' + reset

    print(green + underline + "TYPING GAME\n" + reset)
    print(red + "ERROR!\n" + reset)

    raise FileNotFoundError(errormsg) from None
