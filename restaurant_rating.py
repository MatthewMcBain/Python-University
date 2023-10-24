# Finds the average rating

rating = 0
ratings = [0, 0, 0, 0, 0]
number_of_ratings = 0
average_rating = 0
total_rating = 0
exception = False

while rating != -1 and exception is False:
    rating = 0
    while not(0 < rating < 6) and rating != -1 and exception is False:
        try:
            rating = int(input("Rate the restaurant between 1 and 5: "))
            if not(0 < rating < 6) and rating != -1:
                raise Exception

        except ValueError:
            print("Value Error. You have not entered an integer")
            exception = True

        except Exception:
            print("Range Error. You have not entered an integer between 1 and 5")
            exception = True

    for i in range(0, 5):
        if rating == i + 1:
            ratings[i] += 1
            number_of_ratings += 1

if exception is False:
    print("Ratings:")
    for i in range(0, 5):
        print("{}*:".format(i + 1), end='   ')
        total_rating += ratings[i] * (i + 1)
    print()

    for i in range(0, 5):
        print(ratings[i], end='     ')
    print()

    try:
        print("Average rating:", total_rating / number_of_ratings)

    except ZeroDivisionError:
        print("Zero Division Error. Cannot divide by 0")
