"""
Calculate how many years you should work to save for retirement.

STEP 1. Ask the user for their dream job title.
        Input: string.
        It is not important to error check on the dream job title. Assume it is a reasonable string.

STEP 2. Ask the user for the hourly wage they want to earn.
        Input: integer or float; should account for dollars and cents.

STEP 3. Calculate the annual wage.
        52 paid weeks per year (48 work weeks + 4 vacation weeks).

STEP 4. Ask the user how much money they need at retirement time.
        Input: integer or float.

STEP 5. Determine the number of years to work to save up retirement dollar value assuming the only source of income is paycheck.
        We can assume it will be yearly income savings, so if there is no current savings it will be retirement money needed divided by yearly savings.

STEP 6. Check if the number of years is an even or odd number.
        Input: number of years, integer (use modulus operator).
        Print out the value: "If the value is --- then the number is odd, however, if the value is ----- then the number is even."
"""


# Preset global variable with essential configurations
CURRENT_RETIREMENT_SAVINGS = 0
YEARLY_SAVINGS_PERCENT = 0.1

# STEPS
dream_job_title = input("What is your dream job title?\n")
try:
    dream_job_title = str(dream_job_title)
except ValueError:
    print("The dream job title", dream_job_title, " is not a valid string")

else:

    hourly_wage = input("What is the hourly wage you want to earn?\n")
    try:
        hourly_wage = float(hourly_wage)
    except ValueError:
        print("The hourly wage", hourly_wage, " is not a valid integer or float")

    else:

        retirement_plan = input("How much money do you feel you will need at retirement time?\n")
        try:
            retirement_plan = float(retirement_plan)
        except ValueError:
            print("The amount of money needed at retirement time ", retirement_plan, " is not a valid integer or float")

        else:
            annual_wage = 52 * (40 * hourly_wage)
            yearly_savings = annual_wage * YEARLY_SAVINGS_PERCENT
            years_to_retirement = (retirement_plan - CURRENT_RETIREMENT_SAVINGS) / yearly_savings
            years_to_retirement = int(years_to_retirement)

            to_print = ''
            to_print += '\nYour dream job title is "' + dream_job_title + '".'
            to_print += "\nYour hourly wage is: " + str(hourly_wage) + " dollar(s)."
            to_print += "\nIf you work 40 hours per week and you have 4 weeks vacation, your annual income will be: " + str(annual_wage) + " dollars."
            to_print += "\nAt retirement time you feel you need " + str(retirement_plan) + " dollars."
            to_print += "\nIf you don't have current savings and you will save 10% of your income (neither interest nor inflation were taken into account), it will take " + str(years_to_retirement) + " years to work to save it up."

            print(to_print)

number_type= years_to_retirement % 2

if number_type == 0:
    print("Number of years you have to work to save up retirement plan is even.")
else:
    print("Number of years you have to work to save up retirement plan is odd.")

