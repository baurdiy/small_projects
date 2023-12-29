class Motion:
    def __init__(self):
        self.solution = str(input(
        "This program can calculate: " 
        "\n  'v' = Average speed." 
        "\n  'd' = Distance traveled." 
        "\n  't' = Travel time." 
        "\n  'a' = Acceleration." 
        "\n  'f' = Final speed."
        "\n  'b' = Starting speed." 
        "\nPleace enter:  ")
        )
        if self.solution == 'v':
            self.average_speed()
        elif self.solution == 'd':
            self.distance_traveled()
        elif self.solution == 't':
            self.travel_time()
        elif self.solution == 'a':
            self.acceleration()
        elif self.solution == 'f':
            self.final_velosity()
        elif self.solution == 'b':
            self.start_velosity()
        else:
            print("Please enter valid input!")


    def average_speed(self) -> float:
        """ Average Speed equal to distance divided by time. """
        try:
            distance = float(input("Enter traveled distance(km): "))
            time = float(input("Enter travel time(h): "))
            if time != 0:
                avg_speed = distance / time
                print(f"Average travel speed = {avg_speed} km/h")
                print(self.dist)
                return avg_speed
            else:
                print("Error: Time cann't be zero!")
                return 0
        except ValueError as e:
            print("Invalid Input!")


    def distance_traveled(self) -> float:
        """ Travel distance equal to average velocity multiplied by time. """
        try:
            avg_speed = float(input("Enter average speed(km/h): "))
            time = float(input("Enter travel time(h): "))
            distance = avg_speed * time
            print(f"Travel distance = {distance} km")
            return distance
        except ValueError as e:
            print("Invalid Input!")


    def travel_time(self) -> float:
        """ Travel time equal to distance divided by average velocity.  """
        try:
            distance = float(input("Enter traveled distance(km): "))
            avg_speed = float(input("Enter average speed(km/h): "))
            if avg_speed != 0:
                time = distance / avg_speed
                print(f"Travel time = {time} h")
                return time
            else: 
                print("Error: Average speed can't be zero!")
                return 0
        except ValueError as e:
            print("Invalid Input!")


    def acceleration(self) -> float:
        """ The change in the speed divided by the time it takes to change is called acceleration.  """
        try:
            velosity_f = float(input("Enter velosity after t time passed(km/h): "))
            velosity_0 = float(input("Enter velosity in the begin(km/h): "))
            time = float(input("Enter travel time(h): "))
            if time != 0:
                accel = (velosity_f - velosity_0) / time
                print(f"Acceleration = {accel} km/h")
                return accel
            else:
                print("Error: Time cann't be zero!")
                return 0
        except ValueError as e:
            print("Invalid Input!")    


    def final_velosity(self) -> float:
        """ Final speed of the object after t time passed with acceleration. """
        try:
            velosity_0 = float(input("Enter velosity in the begin(km/h): "))
            accel = float(input("Enter acceleration(km/h/s): "))
            time = float(input("Enter travel time(h): "))
            velosity_f = velosity_0 + (accel * time)
            print(f"Final velosity = {velosity_f}km/h")
            return velosity_f
        except ValueError as e:
                print("Invalid Input!")    


    def start_velosity(self) -> float:
        """ Starting speed of the object after t time passed with acceleration. """
        try:
            velosity_f = float(input("Enter velosity in the end(km/h): "))
            accel = float(input("Enter acceleration(km/h/s): "))
            time = float(input("Enter travel time(h): "))
            velosity_0 = velosity_f - (accel * time)
            print(f"Starting velosity = {velosity_0}km/h")
            return velosity_0
        except ValueError as e:
                print("Invalid Input!") 
    

if __name__ == "__main__":
    # Example of using the Motion class with user inputs:
    run = Motion()

