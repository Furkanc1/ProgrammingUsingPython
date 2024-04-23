from mobileClass import Mobile;

phone1 = Mobile(
    "Iphone",
    "6s",
    "IOS",
    "red",
)

phone2 = Mobile(
    "Samsung",
    "Galaxy-Flip",
    "AOS",
    "black",
)

phone3 = Mobile(
    "Samsung",
    "Galaxy-Bud",
    "AOS",
    "green",
)

print(f"Phone 1 description:\n\n{phone1.description()}")
phone2.call()
phone2.text()
phone2.facetime()
phone3.facetime()
phone1.instagram()
phone1.text()

