while True:
    try:
        string_rep = input('Enter int: ')
        answer = int(string_rep)	   # int(...) may raise ValueError
        break
    except ValueError:
        print('Entry error (',string_rep,') is not a legal int')