Letter1 = str(input('Letter 1: '))
Letter2 = str(input('Letter 2: '))

if ( Letter1 == 'A' and Letter2 == 'B' ) or (Letter1 == 'B' and Letter2 == 'A'):
    Result = 'AB'
elif (Letter1 == 'O' or Letter2 == 'O') and Letter1 != Letter2:
    Result = Letter2 if Letter2!='O' else Letter1
elif Letter1 == Letter2:
    Result = Letter1

print('The combination of the ABO alleles', Letter1, 'and', Letter2, 'results in blood type', Result+'.')
