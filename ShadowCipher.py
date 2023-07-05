#!/usr/bin/env python3
import argparse
import random
import string
import time


def generate_wordlist(first_name, last_name, count):
    print("\033[92;1mGenerating the wordlist...\033[0m")
    start_time = time.time()

    wordlist = []
    variations = [
        f"{first_name.capitalize()[0]}{first_name.lower()[1:]}{last_name.capitalize()}!1",
        f"{first_name.capitalize()[0]}{first_name.lower()[1:]}{last_name.capitalize()}!123",
        f"{first_name.capitalize()[0]}{first_name.lower()[1:]}{last_name.capitalize()}#1",
        f"{first_name.capitalize()[0]}{first_name.lower()[1:]}{last_name.capitalize()}%1",
        f"{first_name.capitalize()[0]}{first_name.lower()[1:]}{last_name.capitalize()}123@",
        f"{first_name.capitalize()[0]}{first_name.lower()[1:]}{last_name.capitalize()}@1",
        f"{first_name.capitalize()[0]}{first_name.lower()[1:]}{last_name.capitalize()}@123",
        f"{first_name.capitalize()[0]}{last_name.capitalize()[0]}{random.choice(string.digits)}",
        f"{first_name.capitalize()[0]}{last_name.capitalize()[0]}{random.choice(string.punctuation)}",
        f"{first_name.capitalize()[0]}{last_name.capitalize()}",
        f"{first_name.capitalize()[0]}{last_name.lower()}{first_name.lower()[1:]}!1",
        f"{first_name.capitalize()[0]}{last_name.lower()}{first_name.lower()[1:]}!123",
        f"{first_name.capitalize()[0]}{last_name.lower()}{first_name.lower()[1:]}#1",
        f"{first_name.capitalize()[0]}{last_name.lower()}{first_name.lower()[1:]}%1",
        f"{first_name.capitalize()[0]}{last_name.lower()}{first_name.lower()[1:]}123@",
        f"{first_name.capitalize()[0]}{last_name.lower()}{first_name.lower()[1:]}@1",
        f"{first_name.capitalize()[0]}{last_name.lower()}{first_name.lower()[1:]}@123",
        f"{first_name.capitalize()[0]}{random.choice(string.ascii_uppercase)}{last_name.capitalize()[0]}{random.choice(string.ascii_lowercase)}",
        f"{first_name.capitalize()[0]}{random.choice(string.ascii_uppercase)}{last_name.capitalize()[0]}{random.choice(string.ascii_uppercase)}",
        f"{first_name.capitalize()[0]}{random.choice(string.ascii_uppercase)}{last_name.capitalize()[0]}{random.choice(string.digits)}",
        f"{first_name.capitalize()}!1",
        f"{first_name.capitalize()}!12",
        f"{first_name.capitalize()}!123",
        f"{first_name.capitalize()}!{last_name.capitalize()}123",
        f"{first_name.capitalize()}#1",
        f"{first_name.capitalize()}#12",
        f"{first_name.capitalize()}#123",
        f"{first_name.capitalize()}#{last_name.capitalize()}1",
        f"{first_name.capitalize()}%1",
        f"{first_name.capitalize()}%12",
        f"{first_name.capitalize()}%123",
        f"{first_name.capitalize()}%{last_name.capitalize()}1",
        f"{first_name.capitalize()}123#",
        f"{first_name.capitalize()}123%",
        f"{first_name.capitalize()}123@",
        f"{first_name.capitalize()}@1",
        f"{first_name.capitalize()}@123",
        f"{first_name.capitalize()}@{last_name.capitalize()}123",
        f"{first_name.capitalize()}{last_name.capitalize()}!1",
        f"{first_name.capitalize()}{last_name.capitalize()}!12",
        f"{first_name.capitalize()}{last_name.capitalize()}!123",
        f"{first_name.capitalize()}{last_name.capitalize()}",
        f"{first_name.capitalize()}{last_name.capitalize()}#1",
        f"{first_name.capitalize()}{last_name.capitalize()}#12",
        f"{first_name.capitalize()}{last_name.capitalize()}#123",
        f"{first_name.capitalize()}{last_name.capitalize()}%1",
        f"{first_name.capitalize()}{last_name.capitalize()}%12",
        f"{first_name.capitalize()}{last_name.capitalize()}%123",
        f"{first_name.capitalize()}{last_name.capitalize()}123#",
        f"{first_name.capitalize()}{last_name.capitalize()}123%",
        f"{first_name.capitalize()}{last_name.capitalize()}123@",
        f"{first_name.capitalize()}{last_name.capitalize()}@1",
        f"{first_name.capitalize()}{last_name.capitalize()}{random.choice(string.digits)}",
        f"{first_name.capitalize()}{last_name.capitalize()}{random.choice(string.punctuation)}",
        f"{first_name.capitalize()}{last_name.lower()}!1",
        f"{first_name.capitalize()}{last_name.lower()}!123",
        f"{first_name.capitalize()}{last_name.lower()}",
        f"{first_name.capitalize()}{last_name.lower()}#1",
        f"{first_name.capitalize()}{last_name.lower()}%1",
        f"{first_name.capitalize()}{last_name.lower()}123@",
        f"{first_name.capitalize()}{last_name.lower()}@1",
        f"{first_name.capitalize()}{last_name.lower()}@123",
        f"{first_name.capitalize()}{last_name.lower()}{first_name.lower()}123@",
        f"{first_name.capitalize()}{last_name.lower()}{first_name.lower()}@1",
        f"{first_name.capitalize()}{last_name.lower()}{first_name.lower()}@123",
        f"{first_name.capitalize()}{random.choice(string.ascii_letters)}{random.choice(string.digits)}",
        f"{first_name.capitalize()}{random.choice(string.ascii_letters)}{random.choice(string.punctuation)}",
        f"{first_name.capitalize()}{random.choice(string.ascii_lowercase)}{random.choice(string.ascii_lowercase)}",
        f"{first_name.capitalize()}{random.choice(string.ascii_lowercase)}{random.choice(string.punctuation)}",
        f"{first_name.capitalize()}{random.choice(string.ascii_uppercase)}{random.choice(string.punctuation)}",
        f"{first_name.capitalize()}{random.choice(string.digits)}!",
        f"{first_name.capitalize()}{random.choice(string.digits)}@",
        f"{first_name.capitalize()}{random.choice(string.digits)}{random.choice(string.ascii_letters)}",
        f"{first_name.capitalize()}{random.choice(string.digits)}{random.choice(string.digits)}",
        f"{first_name.capitalize()}{random.choice(string.digits)}{random.choice(string.digits)}{random.choice(string.digits)}",
        f"{first_name.capitalize()}{random.choice(string.digits)}{random.choice(string.digits)}{random.choice(string.punctuation)}",
        f"{first_name.capitalize()}{random.choice(string.digits)}{random.choice(string.punctuation)}",
        f"{first_name.capitalize()}{random.choice(string.punctuation)}",
        f"{first_name.capitalize()}{random.choice(string.punctuation)}{random.choice(string.digits)}",
        f"{first_name.capitalize()}{random.choice(string.punctuation)}{random.choice(string.punctuation)}",
        f"{first_name.lower()[0]}{last_name.lower()[0]}{random.choice(string.digits)}",
        f"{first_name.lower()[0]}{last_name.lower()[0]}{random.choice(string.punctuation)}",
        f"{first_name.lower()[0]}{last_name.lower()}",
        f"{first_name.lower()}!123",
        f"{first_name.lower()}#123",
        f"{first_name.lower()}%123",
        f"{first_name.lower()}123!",
        f"{first_name.lower()}123#",
        f"{first_name.lower()}123%",
        f"{first_name.lower()}{last_name.capitalize()}",
        f"{first_name.lower()}{last_name.lower()}!123",
        f"{first_name.lower()}{last_name.lower()}",
        f"{first_name.lower()}{last_name.lower()}$123",
        f"{first_name.lower()}{last_name.lower()}%123",
        f"{first_name.lower()}{last_name.lower()}123!",
        f"{first_name.lower()}{last_name.lower()}123$",
        f"{first_name.lower()}{last_name.lower()}123%",
        f"{first_name.lower()}{last_name.lower()}{random.choice(string.digits)}",
        f"{first_name.lower()}{last_name.lower()}{random.choice(string.punctuation)}",
        f"{first_name.lower()}{random.choice(string.ascii_letters)}{random.choice(string.digits)}",
        f"{first_name.lower()}{random.choice(string.ascii_letters)}{random.choice(string.punctuation)}",
        f"{first_name.lower()}{random.choice(string.digits)}!",
        f"{first_name.lower()}{random.choice(string.digits)}@",
        f"{first_name.lower()}{random.choice(string.digits)}{random.choice(string.ascii_letters)}",
        f"{first_name.lower()}{random.choice(string.digits)}{random.choice(string.punctuation)}",
        f"{first_name.lower()}{random.choice(string.punctuation)}",
        f"{first_name.lower()}{random.choice(string.punctuation)}{random.choice(string.digits)}",
        f"{last_name.capitalize()[0]}{first_name.lower()}{last_name.lower()[1:]}!1",
        f"{last_name.capitalize()[0]}{first_name.lower()}{last_name.lower()[1:]}!123",
        f"{last_name.capitalize()[0]}{first_name.lower()}{last_name.lower()[1:]}#1",
        f"{last_name.capitalize()[0]}{first_name.lower()}{last_name.lower()[1:]}%1",
        f"{last_name.capitalize()[0]}{first_name.lower()}{last_name.lower()[1:]}123@",
        f"{last_name.capitalize()[0]}{first_name.lower()}{last_name.lower()[1:]}@1",
        f"{last_name.capitalize()[0]}{first_name.lower()}{last_name.lower()[1:]}@123",
        f"{last_name.capitalize()[0]}{last_name.lower()[1:]}{first_name.capitalize()}!1",
        f"{last_name.capitalize()[0]}{last_name.lower()[1:]}{first_name.capitalize()}!12",
        f"{last_name.capitalize()[0]}{last_name.lower()[1:]}{first_name.capitalize()}!123",
        f"{last_name.capitalize()[0]}{last_name.lower()[1:]}{first_name.capitalize()}#1",
        f"{last_name.capitalize()[0]}{last_name.lower()[1:]}{first_name.capitalize()}#12",
        f"{last_name.capitalize()[0]}{last_name.lower()[1:]}{first_name.capitalize()}#123",
        f"{last_name.capitalize()[0]}{last_name.lower()[1:]}{first_name.capitalize()}%1",
        f"{last_name.capitalize()[0]}{last_name.lower()[1:]}{first_name.capitalize()}%12",
        f"{last_name.capitalize()[0]}{last_name.lower()[1:]}{first_name.capitalize()}%123",
        f"{last_name.capitalize()[0]}{last_name.lower()[1:]}{first_name.capitalize()}@1",
        f"{last_name.capitalize()}!1",
        f"{last_name.capitalize()}!12",
        f"{last_name.capitalize()}!123",
        f"{last_name.capitalize()}#1",
        f"{last_name.capitalize()}#12",
        f"{last_name.capitalize()}#123",
        f"{last_name.capitalize()}#{first_name.capitalize()}1",
        f"{last_name.capitalize()}%1",
        f"{last_name.capitalize()}%12",
        f"{last_name.capitalize()}%123",
        f"{last_name.capitalize()}%{first_name.capitalize()}1",
        f"{last_name.capitalize()}@1",
        f"{last_name.capitalize()}{first_name.capitalize()}!1",
        f"{last_name.capitalize()}{first_name.capitalize()}!12",
        f"{last_name.capitalize()}{first_name.capitalize()}!123",
        f"{last_name.capitalize()}{first_name.capitalize()}#1",
        f"{last_name.capitalize()}{first_name.capitalize()}#12",
        f"{last_name.capitalize()}{first_name.capitalize()}#123",
        f"{last_name.capitalize()}{first_name.capitalize()}%1",
        f"{last_name.capitalize()}{first_name.capitalize()}%12",
        f"{last_name.capitalize()}{first_name.capitalize()}%123",
        f"{last_name.capitalize()}{first_name.capitalize()}1$",
        f"{last_name.capitalize()}{first_name.capitalize()}123%",
        f"{last_name.capitalize()}{first_name.capitalize()}123@",
        f"{last_name.capitalize()}{first_name.capitalize()}@1",
        f"{last_name.capitalize()}{first_name.capitalize()}@123",
        f"{last_name.capitalize()}{first_name.lower()}!1",
        f"{last_name.capitalize()}{first_name.lower()}!123",
        f"{last_name.capitalize()}{first_name.lower()}#1",
        f"{last_name.capitalize()}{first_name.lower()}%1",
        f"{last_name.capitalize()}{first_name.lower()}123@",
        f"{last_name.capitalize()}{first_name.lower()}@1",
        f"{last_name.capitalize()}{first_name.lower()}@123",
        f"{last_name.capitalize()}{random.choice(string.digits)}!",
        f"{last_name.capitalize()}{random.choice(string.digits)}@",
        f"{last_name.capitalize()}{random.choice(string.digits)}{random.choice(string.ascii_letters)}",
        f"{last_name.capitalize()}{random.choice(string.digits)}{random.choice(string.digits)}",
        f"{last_name.capitalize()}{random.choice(string.digits)}{random.choice(string.digits)}{random.choice(string.digits)}",
        f"{last_name.capitalize()}{random.choice(string.digits)}{random.choice(string.digits)}{random.choice(string.punctuation)}",
        f"{last_name.capitalize()}{random.choice(string.digits)}{random.choice(string.punctuation)}",
        f"{last_name.capitalize()}{random.choice(string.punctuation)}",
        f"{last_name.capitalize()}{random.choice(string.punctuation)}{random.choice(string.digits)}",
        f"{last_name.capitalize()}{random.choice(string.punctuation)}{random.choice(string.punctuation)}",
        f"{last_name.lower()}!123",
        f"{last_name.lower()}#123",
        f"{last_name.lower()}%123",
        f"{last_name.lower()}123!",
        f"{last_name.lower()}123#",
        f"{last_name.lower()}123%",
        f"{last_name.lower()}{first_name.capitalize()[0]}{first_name.lower()[1:]}!1",
        f"{last_name.lower()}{first_name.capitalize()[0]}{first_name.lower()[1:]}!123",
        f"{last_name.lower()}{first_name.capitalize()[0]}{first_name.lower()[1:]}#1",
        f"{last_name.lower()}{first_name.capitalize()[0]}{first_name.lower()[1:]}%1",
        f"{last_name.lower()}{first_name.capitalize()[0]}{first_name.lower()[1:]}@1",
        f"{last_name.lower()}{first_name.lower()}!123",
        f"{last_name.lower()}{first_name.lower()}$123",
        f"{last_name.lower()}{first_name.lower()}%123",
        f"{last_name.lower()}{first_name.lower()}123!",
        f"{last_name.lower()}{first_name.lower()}123$",
        f"{last_name.lower()}{first_name.lower()}123%",
        f"{last_name.lower()}{random.choice(string.digits)}!",
        f"{last_name.lower()}{random.choice(string.digits)}#",
        f"{last_name.lower()}{random.choice(string.digits)}@",
        f"{last_name.lower()}{random.choice(string.digits)}{random.choice(string.ascii_letters)}",
        f"{last_name.lower()}{random.choice(string.digits)}{random.choice(string.punctuation)}",
        f"{last_name.lower()}{random.choice(string.punctuation)}",
        f"{last_name.lower()}{random.choice(string.punctuation)}{random.choice(string.digits)}",
        f"{random.choice(string.ascii_lowercase)}{first_name.capitalize()[0]}{random.choice(string.ascii_lowercase)}{last_name.capitalize()[0]}",
        f"{random.choice(string.ascii_lowercase)}{first_name.capitalize()[0]}{random.choice(string.digits)}{last_name.capitalize()[0]}",
        f"{random.choice(string.ascii_uppercase)}{last_name.capitalize()}{random.choice(string.ascii_lowercase)}",
        f"{random.choice(string.ascii_uppercase)}{last_name.capitalize()}{random.choice(string.ascii_uppercase)}",
        f"{random.choice(string.ascii_uppercase)}{last_name.capitalize()}{random.choice(string.digits)}",
        f"{random.choice(string.ascii_uppercase)}{last_name.capitalize()}{random.choice(string.punctuation)}",
    ]

    # Generate variations using f-strings
    variations.append(f"{first_name.capitalize()}{last_name.capitalize()}")
    variations.append(f"{first_name.lower()}{last_name.lower()}")
    variations.append(f"{first_name.capitalize()[0]}{last_name.capitalize()}")
    variations.append(f"{first_name.lower()[0]}{last_name.lower()}")
    variations.append(f"{first_name.capitalize()}{last_name.lower()}")
    variations.append(f"{first_name.lower()}{last_name.capitalize()}")
    # Add more variations using f-strings

    for _ in range(count):
        wordlist.append(random.choice(variations))

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Generated wordlist in {format_time(elapsed_time)}")

    return wordlist


def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    second = int(seconds % 60)

    return f"{hours:02d}h:{minutes:02d}m:{second:02d}s"


def save_wordlist(wordlist, filename):
    with open(filename, "w") as file:
        for word in wordlist:
            file.write(word + "\n")


def main():
    parser = argparse.ArgumentParser(description="Wordlist Generator")
    parser.add_argument("first_name", help="First name")
    parser.add_argument("last_name", help="Last name")
    parser.add_argument(
        "-n",
        "--count",
        type=int,
        default=100,
        help="Number of wordlist entries to generate (default: 100)",
    )
    parser.add_argument(
        "-sv",
        "--save",
        metavar="filename",
        help="Save wordlist to the specified file",
    )

    args = parser.parse_args()

    if args.count > 50000000:
        print(
            '\033[91m\033[1mWARNING: Generating a large wordlist may slow down your device. If you want to stop, press "CTRL + C"\033[0m'
        )

    print("Running the script in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    wordlist = generate_wordlist(args.first_name, args.last_name, args.count)

    if args.save:
        save_wordlist(wordlist, args.save)
        print(
            "\033[92m\u2713\ufe0f Generated",
            len(wordlist),
            "words and saved it in",
            args.save,
            "\U0001F389\033[0m",
        )

    else:
        print(wordlist)


if __name__ == "__main__":
    print(
        "\033[94;1m-----------------------------------------------------------------------------------------------------------------------------------\033[0m"
    )

    print(
        "\033[34m"
        """
░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
╚█████╗░███████║███████║██║░░██║██║░░██║░╚██╗████╗██╔╝██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
░╚═══██╗██╔══██║██╔══██║██║░░██║██║░░██║░░████╔═████║░██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
██████╔╝██║░░██║██║░░██║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""
        "\033[0m"
    )

    print(
        "\033[94;1m-----------------------------------------------------------------------------------------------------------------------------------\033[0m"
    )

    print(
        "\033[38;5;208mPassword WordList Generator\033[0m                                             \033[38;5;46mDiscord/Twitter: @rezydev\033[0m"
    )

    print(
        "\033[94;1m-----------------------------------------------------------------------------------------------------------------------------------\033[0m"
    )

    main()
