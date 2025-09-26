# -*- coding: utf-8 -*-
import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()

# Commented out IPython magic to ensure Python compatibility.
# %%writefile words.py
# word_list = [
#     "PYTHON", "PROGRAMMING", "COMPUTER", "SCIENCE", "INTELLIGENCE",
#     "MACHINE", "LEARNING", "ARTIFICIAL", "NEURAL", "NETWORK",
#     "ALGORITHM", "DATA", "STRUCTURE", "FUNCTION", "VARIABLE",
#     "LOOP", "CONDITIONAL", "STATEMENT", "SYNTAX", "DEBUGGING",
#     "COMPILER", "INTERPRETER", "DATABASE", "SOFTWARE", "HARDWARE",
#     "INTERNET", "WEBSITE", "BROWSER", "SERVER", "CLIENT",
#     "OPERATING", "SYSTEM", "MOBILE", "APPLICATION", "DEVELOPMENT",
#     "CLOUD", "COMPUTING", "CYBERSECURITY", "ENCRYPTION", "DECRYPTION",
#     "AUTHENTICATION", "AUTHORIZATION", "FIREWALL", "ANTIVIRUS", "MALWARE",
#     "VIRUS", "TROJAN", "PHISHING", "SPAM", "BACKUP",
#     "RECOVERY", "NETWORK", "PROTOCOL", "ETHERNET", "WIFI",
#     "BLUETOOTH", "ROUTER", "SWITCH", "HUB", "CABLE",
#     "MONITOR", "KEYBOARD", "MOUSE", "PRINTER", "SCANNER",
#     "SPEAKER", "MICROPHONE", "CAMERA", "WEBCAM", "HEADPHONES",
#     "SMARTPHONE", "TABLET", "LAPTOP", "DESKTOP", "NOTEBOOK",
#     "PROJECTOR", "SCREEN", "WHITEBOARD", "MARKER", "ERASER",
#     "CHAIR", "TABLE", "DESK", "LAMP", "CLOCK",
#     "BOOK", "PEN", "PENCIL", "PAPER", "NOTEBOOK",
#     "BAG", "BACKPACK", "WALLET", "KEYS", "PHONE",
#     "CAR", "BUS", "TRAIN", "PLANE", "SHIP",
#     "BICYCLE", "MOTORCYCLE", "SCOOTER", "TRUCK", "VAN",
#     "HOUSE", "BUILDING", "APARTMENT", "OFFICE", "SCHOOL",
#     "UNIVERSITY", "LIBRARY", "MUSEUM", "PARK", "GARDEN",
#     "STREET", "ROAD", "HIGHWAY", "BRIDGE", "TUNNEL",
#     "RIVER", "LAKE", "OCEAN", "SEA", "MOUNTAIN",
#     "HILL", "VALLEY", "FOREST", "DESERT", "ISLAND",
#     "BEACH", "COAST", "SHORE", "CLIFF", "WATERFALL",
#     "SUN", "MOON", "STAR", "PLANET", "GALAXY",
#     "UNIVERSE", "SPACE", "TIME", "ENERGY", "MATTER",
#     "PHYSICS", "CHEMISTRY", "BIOLOGY", "MATH", "HISTORY",
#     "GEOGRAPHY", "LANGUAGE", "ENGLISH", "SPANISH", "FRENCH",
#     "GERMAN", "CHINESE", "JAPANESE", "KOREAN", "RUSSIAN",
#     "ARABIC", "HINDI", "BENGALI", "PUNJABI", "URDU",
#     "TAMIL", "TELUGU", "MARATHI", "GUJARATI", "KANNADA",
#     "MALAYALAM", "ODIA", "ASSAMESE", "NEPALI", "SINHALA",
#     "BURMESE", "THAI", "VIETNAMESE", "INDONESIAN", "MALAY",
#     "FILIPINO", "TURKISH", "GREEK", "HEBREW", "LATIN",
#     "SANSKRIT", "PALI", "PRAKRIT", "APABHRAMSA", "OLD",
#     "MIDDLE", "MODERN", "ANCIENT", "MEDIEVAL", "RENAISSANCE",
#     "BAROQUE", "CLASSICAL", "ROMANTIC", "MODERN", "CONTEMPORARY",
#     "FUTURE", "PAST", "PRESENT", "MORNING", "AFTERNOON",
#     "EVENING", "NIGHT", "DAY", "WEEK", "MONTH",
#     "YEAR", "DECADE", "CENTURY", "MILLENNIUM", "SECOND",
#     "MINUTE", "HOUR", "JANUARY", "FEBRUARY", "MARCH",
#     "APRIL", "MAY", "JUNE", "JULY", "AUGUST",
#     "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER", "MONDAY",
#     "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY",
#     "SUNDAY", "SPRING", "SUMMER", "AUTUMN", "WINTER",
#     "NORTH", "SOUTH", "EAST", "WEST", "UP",
#     "DOWN", "LEFT", "RIGHT", "FRONT", "BACK",
#     "INSIDE", "OUTSIDE", "ABOVE", "BELOW", "NEAR",
#     "FAR", "HERE", "THERE", "EVERYWHERE", "NOWHERE",
#     "SOMETHING", "NOTHING", "EVERYTHING", "ANYTHING", "SOMEONE",
#     "NOONE", "EVERYONE", "ANYONE", "SOMEWHERE", "NOWHERE",
#     "EVERYWHERE", "ANYWHERE", "ALWAYS", "NEVER", "SOMETIMES",
#     "OFTEN", "RARELY", "USUALLY", "GENERALLY", "NORMALLY",
#     "SUDDENLY", "SLOWLY", "QUICKLY", "HAPPILY", "SADLY",
#     "ANGRILY", "CALMLY", "LOUDLY", "SOFTLY", "BRIGHTLY",
#     "DARKLY", "CLEARLY", "UNCLEARLY", "EASILY", "DIFFICULTLY",
#     "POSSIBLY", "IMPOSSIBLY", "PROBABLY", "IMPROBABLY", "CERTAINLY",
#     "UNCERTAINLY", "DEFINITELY", "INDEFINITELY", "ACTUALLY", "REALLY",
#     "VERY", "TOO", "ENOUGH", "JUST", "ALMOST",
#     "ABOUT", "AROUND", "APPROXIMATELY", "EXACTLY", "PRECISELY",
#     "ROUGHLY", "MORE", "LESS", "MOST", "LEAST",
#     "BETTER", "WORSE", "BEST", "WORST", "BIGGER",
#     "SMALLER", "BIGGEST", "SMALLEST", "TALLER", "SHORTER",
#     "TALLEST", "SHORTEST", "FASTER", "SLOWER", "FASTEST",
#     "SLOWEST", "STRONGER", "WEAKER", "STRONGEST", "WEAKEST",
#     "RICHER", "POORER", "RICHEST", "POOREST", "HAPPIER",
#     "SADDER", "HAPPIEST", "SADDEST", "HOTTER", "COLDER",
#     "HOTTEST", "COLDEST", "WETTER", "DRIER", "WETTEST",
#     "DRIEST", "LIGHTER", "HEAVIER", "LIGHTEST", "HEAVIEST",
#     "EARLIER", "LATER", "EARLIEST", "LATEST", "NEWER",
#     "OLDER", "NEWEST", "OLDEST", "CLOSER", "FARTHER",
#     "CLOSEST", "FARTHEST", "HIGHER", "LOWER", "HIGHEST",
#     "LOWEST", "DEEPER", "SHALLOWER", "DEEPEST", "SHALLOWEST",
#     "WIDER", "NARROWER", "WIDEST", "NARROWEST", "LONGER",
#     "SHORTER", "LONGEST", "SHORTEST", "THICKER", "THINNER",
#     "THICKEST", "THINNEST", "BRIGHTER", "DIMMER", "BRIGHTEST",
#     "DIMMEST", "CLEANER", "DIRTIER", "CLEANEST", "DIRTIEST",
#     "SAFER", "DANGEROUS", "SAFEST", "MOST DANGEROUS", "EASIER",
#     "MORE DIFFICULT", "EASIEST", "MOST DIFFICULT", "BETTER", "WORSE",
#     "BEST", "WORST", "MORE", "LESS", "MOST",
#     "LEAST", "MANY", "FEW", "MUCH", "LITTLE",
#     "A LOT", "PLENTY", "SEVERAL", "SOME", "ANY",
#     "NO", "ALL", "NONE", "EACH", "EVERY",
#     "OTHER", "ANOTHER", "SAME", "DIFFERENT", "SIMILAR",
#     "OPPOSITE", "NEXT", "PREVIOUS", "FOLLOWING", "LEADING",
#     "TRAILING", "FIRST", "LAST", "ONLY", "SINGLE",
#     "DOUBLE", "TRIPLE", "QUADRUPLE", "MULTIPLE", "FEW",
#     "SEVERAL", "MANY", "A FEW", "A LITTLE", "A LOT OF",
#     "PLENTY OF", "SOME", "ANY", "NO", "ALL",
#     "NONE", "EACH", "EVERY", "OTHER", "ANOTHER",
#     "SAME", "DIFFERENT", "SIMILAR", "OPPOSITE", "NEXT",
#     "PREVIOUS", "FOLLOWING", "LEADING", "TRAILING", "FIRST",
#     "LAST", "ONLY", "SINGLE", "DOUBLE", "TRIPLE",
#     "QUADRUPLE", "MULTIPLE", "ZERO", "ONE", "TWO",
#     "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
#     "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE",
#     "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
#     "EIGHTEEN", "NINETEEN", "TWENTY", "THIRTY", "FORTY",
#     "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY",
#     "HUNDRED", "THOUSAND", "MILLION", "BILLION", "TRILLION",
#     "PERCENT", "HALF", "QUARTER", "THIRD", "WHOLE",
#     "PART", "FRACTION", "DECIMAL", "PERCENTAGE", "RATIO",
#     "PROPORTION", "AMOUNT", "NUMBER", "QUANTITY", "MEASURE",
#     "UNIT", "SIZE", "WEIGHT", "HEIGHT", "WIDTH",
#     "LENGTH", "DEPTH", "AREA", "VOLUME", "CAPACITY",
#     "TEMPERATURE", "PRESSURE", "SPEED", "VELOCITY", "ACCELERATION",
#     "FORCE", "MASS", "DENSITY", "ENERGY", "POWER",
#     "WORK", "HEAT", "LIGHT", "SOUND", "ELECTRICITY",
#     "MAGNETISM", "GRAVITY", "FRICTION", "TENSION", "COMPRESSION",
#     "STRESS", "STRAIN", "MOMENTUM", "IMPULSE", "VELOCITY",
#     "ACCELERATION", "FORCE", "MASS", "WEIGHT", "PRESSURE",
#     "TEMPERATURE", "DENSITY", "VOLUME", "AREA", "LENGTH",
#     "WIDTH", "HEIGHT", "DEPTH", "TIME", "SPEED",
#     "DISTANCE", "DISPLACEMENT", "VELOCITY", "ACCELERATION", "MOMENTUM",
#     "IMPULSE", "ENERGY", "POWER", "WORK", "HEAT",
#     "LIGHT", "SOUND", "ELECTRICITY", "MAGNETISM", "GRAVITY",
#     "FRICTION", "TENSION", "COMPRESSION", "STRESS", "STRAIN",
#     "MOMENTUM", "IMPULSE", "VELOCITY", "ACCELERATION", "FORCE",
#     "MASS", "WEIGHT", "PRESSURE", "TEMPERATURE", "DENSITY",
#     "VOLUME", "AREA", "LENGTH", "WIDTH", "HEIGHT",
#     "DEPTH", "TIME", "SPEED", "DISTANCE", "DISPLACEMENT",
#     "VELOCITY", "ACCELERATION", "MOMENTUM", "IMPULSE", "ENERGY",
#     "POWER", "WORK", "HEAT", "LIGHT", "SOUND",
#     "ELECTRICITY", "MAGNETISM", "GRAVITY", "FRICTION", "TENSION",
#     "COMPRESSION", "STRESS", "STRAIN", "MOMENTUM", "IMPULSE"
# ]