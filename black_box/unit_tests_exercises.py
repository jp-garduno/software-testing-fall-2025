def Exercise_One(number):
    if number == 0:
        return "Its Zero"
    elif number < 0:
        return "Its negative"
    else:
        return "Its positive"


def Exercise_Two(password):
    special_chars = ["!", "@", "#", "$", "%", "&"]
    hasUpper = False
    hasLower = False
    spchar = False
    digits = False

    if len(password) < 8:
        return False
    
    for char in password:
        if char in special_chars:
            spchar = True
        if char.isupper():
            hasUpper = True
        if char.islower():
            hasLower = True
        if char.isdigit():
            digits = True

    if spchar and hasUpper and hasLower and digits:
        return True
    else:
        return False

def Exercise_Three(total):
	if total < 100:
		return "0%"
	elif total <= 500:
		return "10%"
	else:
		return "20%"
     


def main():
    print(Exercise_One(5))  # debería imprimir "Its positive"
    print(Exercise_Two("Password123!"))  # ejemplo válido → True
    print(Exercise_Three(450))

main()
