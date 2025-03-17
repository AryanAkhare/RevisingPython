def hello(name,lang):
    greetings={
        "English":"Hello ",
        "Hindi":"Namaste ",
        "Spanish":"Ola ",
        "German":"Hallo "
    }
    msg=f"{greetings[lang]}{name}"
    print(msg)

if __name__=='__main__':

    import argparse #command line library and arguments
    parser=argparse.ArgumentParser(
        description="Provides personal greeting."
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True,help="The name of person to greet."
    )

    parser.add_argument(
        "-l","--lang",metavar="language",
        required=True,choices=["English","Hindi","Spanish","German"],
        help="The language of greeting."

    )
    args=parser.parse_args()
    hello(args.name,args.lang)

    #run using python script.py -n Aryan
