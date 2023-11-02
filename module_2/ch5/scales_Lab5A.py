# lexi scales, complete
# this program takes in numeric ratings from critics for restaurants and gives the restaurant a star rating.

def main():
    # this function accepts five numeric ratings from the user, and calculates the average score. it then calls a function to process that average score. 
    NUMBER_OF_RATINGS = 5
    total_ratings = 0
    average_ratings = 0
    for score in range(NUMBER_OF_RATINGS):
        rating = int(input('Enter critic\'s score between 0 and 10: '))
        while rating < 0 or rating > 10:
            print('Error: critic\'s score must be between 0 and 10')
            rating = int(input('Enter valid critic score: '))
        total_ratings += rating
    average_ratings = total_ratings / NUMBER_OF_RATINGS    
    
    star_rating = determine_stars(average_ratings)
    star_display = ''
    if star_rating == 0:
        star_display = '˙◠˙no stars˙◠˙'
    for star in range(star_rating):
        star_display = '⭐' * star_rating
    
    print(f'\nYour average numeric score is {average_ratings:.2f}.')
    print(f'Your final star rating for this restaurant is... {star_display}')

    
def determine_stars(number):
    # this function calculates a number of stars based on the number it receives
    FIVE_STAR_MIN = 9.0
    FOUR_STAR_MIN = 8.0
    THREE_STAR_MIN = 7.0
    TWO_STAR_MIN = 6.0
    ONE_STAR_MIN = 5.0
    
    if number >= FIVE_STAR_MIN:
       stars = 5
    elif number >= FOUR_STAR_MIN:
      stars = 4
    elif number >= THREE_STAR_MIN:
      stars = 3
    elif number >= TWO_STAR_MIN:
      stars = 2
    elif number >= ONE_STAR_MIN:
      stars = 1
    else:
        stars = 0
    return stars

main()