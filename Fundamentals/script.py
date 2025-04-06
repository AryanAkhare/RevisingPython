import argparse  # For command-line argument parsing

def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Hindi": "Namaste",
        "Spanish": "Ola",
        "German": "Hallo"
    }
    msg = f"{greetings.get(lang, 'Hello')} {name}"
    print(msg)

def main():
    parser = argparse.ArgumentParser(
        description="Provides a personalized greeting."
    )
    
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True,
        help="The name of the person to greet."
    )
    
    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True,
        choices=["English", "Hindi", "Spanish", "German"],
        help="The language to use for the greeting."
    )
    
    args = parser.parse_args()
    hello(args.name, args.lang)

if __name__ == "__main__":
    main()
