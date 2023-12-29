class Profile:
    """ Display profile information about a person. """

    def __init__(self, first=None, last=None, age=None, occupation=None, height=None):
        self.first = first if first is not None else str(input("Enter your name (skip with Enter): ")) or None
        self.last = last if last is not None else str(input("Enter your last name (skip with Enter): ")) or None

        while True:
            try:
                age_input = input("Enter your age (skip with Enter): ")
                if age_input.strip() == '' or age_input.lower() == 'skip':
                    self.age = None
                    break  # Break out of the loop if the user skips
                else:
                    self.age = int(age_input)
                    break  # Break out of the loop if the input is a valid integer
            except ValueError:
                print("Invalid input. Please enter a valid integer for age.")

        occupation_input = input("Enter your occupation (skip with Enter): ")
        self.occupation = occupation_input.strip() if occupation_input.strip() != '' else None

        height_input = input("Enter your height (in meters, skip with Enter): ")
        self.height = float(height_input) if height_input.strip() != '' else None

    def display_info(self):
        return f"Name: {self.first} {self.last}\nAge: {self.age}"


if __name__ == "__main__":
    person = Profile()
    print(person.display_info())
