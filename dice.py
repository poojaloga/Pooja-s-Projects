import time 

def pseudo_random(seed):
    a = 1103515245
    c = 12345
    m = 2 ** 31
    seed = (a * seed + c) % m
    return seed

def roll_dice(seed):
    number = pseudo_random(seed)
    return number % 10 + 1, number

def consequence(roll):
    consequences = {
        1: "Eat a spoon of cinnamon.",
        2: "Drive to McDonald's and buy everyone ice cream.",
        3: "Sing your favorite song loudly.",
        4: "Do 10 jumping jacks.",
        5: "Share an embarrassing story.",
        6: "Make a funny face and take a selfie.",
        7: "Give someone a compliment.",
        8: "Dance for 30 seconds.",
        9: "Imitate your favorite movie character.",
        10: "Tell a joke."
    }
    return consequences.get(roll, "No consequence")

if __name__ == "__main__":
    # Use current time as seed
    seed = int(time.time())
    roll, new_seed = roll_dice(seed)
    print(f"You rolled a {roll}!")
    print(consequence(roll))
