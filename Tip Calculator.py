def tipQuestions():
    billTotal = input('What is the bill total?\n')
    numberOfPeople = input('How many people will the bill be split between?\n')

    return print('Total cost will be', "${:,.2f}".format(float(billTotal) / int(numberOfPeople)), 'per person.')

tipQuestions()
