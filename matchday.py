day = input("Enter the day of the week (Monday-Sunday): ").lower()

match day:
    case "monday":
        print("Urgg, Monday...")
    case "tuesday":
        print ("Just another workday...")
    case "wednesday":
        print ("Hump day!")
    case "thursday":
        print ("Almost there...")
    case "friday":
        print ("TGIF!")
    case "saturday" | "Sunday":
        print ("Weekend vibes!")
    case _ :
        print ("Invalid day entered!")