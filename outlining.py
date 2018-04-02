"""
You work for a consumer ratings website. Users submit reviews and scores for products they use, and you show the results so that consumers
can make informed choices.

Write a function that takes as input five scores and aggregates them to output a single rating.

Because the highest and lowest scores might be outliers and skew the results,
take the three middle scores out of the five, discarding the highest and lowest.

Then provide the rating:
Average Score 	Rating
0 <= score < 1 	Terrible
1 <= score < 2 	Bad
2 <= score < 3 	OK
3 <= score < 4 	Good
4 <= score <= 5 Excellent

"""

def convert_to_numeric(score):
    """
    Convert the score to a numerical type.
    Input:  string, int, or float
    Output: float
    """
    return float(score)

# Check
print("Check:")
print(convert_to_numeric(3))
print(type(convert_to_numeric(3)))

def av_score(score1,score2,score3,score4,score5):
    """
    Find the average of sum of the middle three numbers out of the five given.
    Input:  5 scores, float
    Output: average, float
    """
    sum=score1+score2+score3+score4+score5
    sum-=max(score1,score2,score3,score4,score5)
    sum-=min(score1,score2,score3,score4,score5)
    return sum/3

# Check
print("Check:")
print(av_score(3,3,1,5,2))

def score_to_rating_string(av_score):
    """
    Convert the average score, which should be between 0 and 5,
    into a string rating.
    """
    rating =None
    if av_score<1:
        rating="Terrible"
    elif av_score<2:
        rating="Bad"
    elif av_score<3:
        rating="OK"
    elif av_score<4:
        rating="Good"
    else:
        rating="Excellent"
    return rating

# Check
print("Check:")
print (score_to_rating_string(3))

def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = av_score(score1,score2,score3,score4,score5)

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating

# Check
print("Check:")
print(scores_to_rating(3,1,2.0,3,5))