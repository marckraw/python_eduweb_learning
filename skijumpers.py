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

# for loop
for jumper in ski_jumpers:
    print(jumper)


print("####################")

index = 0
while index < len(ski_jumpers):
    print(ski_jumpers[index], ski_jumpers[index + 1])
    index += 2


print("####################")

for jumper in ski_jumpers:
    if list(jumper.keys())[0] == "Kamil Stoch":
        print(jumper)
        break


print("####################")


index = 0
number_of_jumpers = 3
while index < number_of_jumpers:
    print(ski_jumpers[index])
    index += 1

print("####################")

for jumper in ski_jumpers:
    if list(jumper.values())[0] == "PL":
        print(jumper)
        break

print("####################")

norwegians = [jumper for jumper in ski_jumpers if list(jumper.values())[0] == "NOR"  ] # list comprehension
print(norwegians)