def get_age():
#input the age of the user age
    user_age = int(input())
# if the user is younger than 18 or older than 75 then the user is invalid
    if user_age < 18 or user_age > 75:
#return an Error when the if statement is not meet
        raise ValueError("Invalid age.")
    return user_age

def fat_burning_heart_rate(user_age):
# fat burning equation
    top_heart_rate = 220
    fat_burn = 0.7 * (top_heart_rate - user_age)
    return fat_burn

if __name__ == '__main__':
    try:
        age = get_age()
        rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {rate:.1f} bpm")
    except ValueError as error:
        print(error)
        print("Could not calculate heart rate info.")
        print()