class Converter:
    def __init__(self) -> float:
        self.convert = str(input(
            "Distance unit converter. "
            "\n 'k' = km to miles."
            "\n 'm' = miles to km."
            "\nPlease enter: "  
        )).lower()
        if self.convert == "k":
            self.km_miles()
        elif self.convert == "m":
            self.miles_km()
        else:
            print("Invalid input!")
    

    def km_miles(self):
        km = float(input("Enter km: "))
        miles = km / 1.609
        print(f"{km} km = {miles} miles.")
    
    def miles_km(self):
        miles = float(input("Enter miles: "))
        km = miles * 1.609
        print(f"{miles} miles = {km} km.")


if __name__ == "__main__":
    run_program = Converter()