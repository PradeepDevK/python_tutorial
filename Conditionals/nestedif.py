age = int(input('Enter your age '))


if age >= 18:
    score = int(input('Enter your exam score '))
    if score >= 40:
        print('you meet both the age and score criteria, you are qualified')
    else:
        print('you meet the age criteria but do not meet the score criteria')
else:
    print('you do not meet age criteria, please try when you are above')