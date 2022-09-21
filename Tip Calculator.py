def tipQuestions():
    billTotal = input('What is the bill total?\n')
    numberOfPeople = input('How many people will the bill be split between?\n')
    tipQuestion = input('Would you like to give a tip? (Y or N)\n')
    
    if tipQuestion.upper() == 'Y':
        tipPercentQuestion = input('How much of a tip would you like to give?\n')
        tipPercent = float(tipPercentQuestion) * .01
        tipAmount = float(billTotal) * tipPercent
        costPerPerson = (float(billTotal) + tipAmount) / int(numberOfPeople)
    else:
        costPerPerson = float(billTotal) / int(numberOfPeople)

    return print('Total cost will be', "${:,.2f}".format(costPerPerson), 'per person.')

tipQuestions()
