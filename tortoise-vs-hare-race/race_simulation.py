import random

def position_tortoise(position):
    num = random.randint(1, 10)
    if 1 <= num <= 5:
        return min(position + 3, 50)  # fast plod
    elif num in [6, 7]:
        return max(1, position - 5)  # slip
    else:
        return min(position + 1, 50)  # slow plod

def position_hare(position):
    num = random.randint(1, 10)
    if num in [1, 2]:
        return position  # sleep
    elif num in [3, 4]:
        return min(position + 7, 50)  # big hop
    elif num == 5:
        return max(1, position - 10)  # big slip
    elif 6 <= num <= 8:
        return min(position + 1, 50)  # small hop
    else:
        return max(1, position - 2)  # small slip

def display_track(hare, tortoise):
    track = [" "] * 50
    if hare == tortoise:
        track[hare - 1] = "OW!!"
    else:
        if 1 <= hare <= 50:
            track[hare - 1] = "H"
        if 1 <= tortoise <= 50:
            track[tortoise - 1] = "T"
    print("".join(f"{pos:<5}" for pos in track))

def main():
    print("ON YOUR MARK... GET SET...")
    print("GO!!!!!!")
    print("AND THEY'RE OFF!\n")

    hare = 1
    tortoise = 1
    time = 0

    while hare < 50 and tortoise < 50:
        hare = position_hare(hare)
        tortoise = position_tortoise(tortoise)
        time += 1
        display_track(hare, tortoise)

    print()
    if tortoise >= 50:
        print("Tortoise wins!! Yay!")
    elif hare >= 50:
        print("Hare wins. Yay.")
    print(f"Time of race: {time} seconds")

if __name__ == "__main__":
    main()