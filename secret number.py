print("km/milla")

km = int(input("how many km? "))
print(str(km), "km", km*0.621371, "millas")


while True:
    Conversion = input("wanna other conversion? (sure/nah)")

    if Conversion == "sure":
        km = int(input(" how many km? "))
        print(str(km) + " km = millas:")
        print(km * 0.621371)

    else:
        print("OK GO FCKING OUT")
        break

