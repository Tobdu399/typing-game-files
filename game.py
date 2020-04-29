try:
    import random
    import os
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


    def clear():
        os.system("clear")


    def main():
        clear()
        print(green + "Loading words...")
        print("This may take a while depending on the size of the text file" + reset)

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
        for i in range(0, 500):
            word = random.randint(1, lines)

            for position, line in enumerate(file):
                if position == word:
                    word_list.append(line.strip("\n"))

            file.seek(0)
        file.close()

        # Make a sentance of the words to detect the language easier
        detectlanguage = word_list[0] + " " + word_list[10] + " " + word_list[100]

        # Detect language
        language = detect(detectlanguage)

        # Game setup
        health = ["[][]", "[][]", "[][]", "[][]", "[][]"]
        health_lost = []

        current_word = 0
        completed_words = 0
        failed_words = 0

        # Game loop
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
                    health_lost.append("[][]")
                    current_word += 1

            else:
                clear()
                print(underline + red + "Game Lost!" + reset)
                print("\nCorrect Words: " + str(completed_words))
                print("Failed Words: " + str(failed_words))
                print()

                print(red + "\n-----------------------------------------" + reset)
                retry = input("Continue? [Y/N] > ")

                if retry == "y" or retry == "Y":
                    main()
                    break

                else:
                    clear()
                    break

                main()

    main()

except(FileNotFoundError):
    clear()
    print(red + "Error!" + reset + " words.txt file does not exist")
    print("\nMake sure that your word file name is 'words.txt' and it is\nin the same directory as this Python file (game.py)")
    print("\nIf you have lost your words.txt file, you can get new one in here:")
    print(green + "https://github.com/tobdu399/typing-game-files/\n" + reset)