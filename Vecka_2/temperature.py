temperature_scale = None
temperature_number = None

while True:
    temperatur = input("Skriv in temperatur i C eller Fahrenheit, tex 22C eller 32F: ")
    if temperatur[-1] in "CF" and temperatur[:-1].isdigit():
        temperature_scale = temperatur[-1]
        temperature_number = float(temperatur[:-1])
        break
    else:
        print("Inputfel, försök igen...")

if temperature_scale == "C":
    converted_scale = "F"
    converted_number = ((1.8 * temperature_number) + int(32))
#Review: Om användaren har matat in fel scale (ex. 22W) kommer programmet omvandla temperaturen till Celsius utan att meddela användaren om inputfel. Annars jättebra idé  
else:
    converted_scale = "C"
    converted_number = (temperature_number - 32) / 1.8

print(f"{temperature_number}{temperature_scale} blir {converted_number:.2f}{converted_scale}")
