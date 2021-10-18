# Lists
crypto_prices = [
    ["bitcoin", 3000],
    ["eth", 2000],
    ["iota", 30],
    ["nem", 2]
]

print(crypto_prices)
print(crypto_prices[0])
print(crypto_prices[0][1])



# SEt
crypto_prices_set = {3000, 2000, 30, 10} # kolejnpsc elementow losowa, ale elementy unikatowe

print(crypto_prices_set)

# Dictionary - elementy w slowniku losowa kolejnosc
crypto_prices_dictionary = {
    "bitcoin": 3000,
    "eth": 2000,
    "iota": 30,
    "nem": 2,
    "test": -1
}
print(crypto_prices_dictionary)


# tuple - raz zadeklarowana nie moze byc zmieniona (nie mozna dodawac ani usuwac elementow, ani zmieniac)
crypto_prices_tuple = (3000, 200, 30, 10)


print("Podaj nazwe krypto: ")
crypto_name = input()
print("Podaj cene krypto: ")
crypto_price = int(input())


# handling errors and throwing errors
try:
    if crypto_name == "test":
        raise KeyError("Unable to handle this key")
    if crypto_price > crypto_prices_dictionary[crypto_name]:
        print("Waiting for better rate")
    else:
        print("good price")
except KeyError as e:
    print(e)
    print("Unable to find a key: ")
finally:
    print("I will be invoked!")
