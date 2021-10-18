def print_all(ski_jumpers): # przekazywanie przez referencje
    for jumper in ski_jumpers:
        print(jumper)


def find_jumper(ski_jumpers, jumper_name="Kamil stoch"):  # domyslna wartosc
    for jumper in ski_jumpers:
        if list(jumper.keys())[0] == jumper_name:
            print(jumper)
            break


def find_by_nationality(ski_jumpers, nationality):  # domyslna wartosc
    for jumper in ski_jumpers:
        if list(jumper.values())[0] == nationality:
            print(jumper)
            break


def print_nice(*ski_jumpers):
    for jumper in ski_jumpers:
        print("\n***************Ski Jumper***************")
        print("\n***************", jumper, "*************")
        print("\n****************************************")
        print("\n")

ski_jumpers = [
    {
        "Ryoyo Kubayashi": "Jpn"
    },
    {
        "piotr zytla": "PL"
    },
    {
        "Robert johanson": "NOR"
    },
    {
        "someone": "NOR"
    },
    {
        "Kamil Stoch": "PL"
    },
    {
        "Jakis ziomek": "PL"
    }
]


print("###########")
find_by_nationality(ski_jumpers, "PL") # normal function with arguments
print("###########")
find_by_nationality(nationality="PL", ski_jumpers=ski_jumpers) # function with arguments like in javascript {}


print("##########################")
print(print_nice("Piotr zyla", "Timi Zac"))
