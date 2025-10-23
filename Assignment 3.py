input = " 8 , -2 , 1.68 , False , -2.5"
user_input_list = input.split(",")
integer_list = []
float_list = []
boolean_list = []

for element in user_input_list:
    item = element.strip()
    if item.lower()=="false":
        boolean_list.append(False)
    elif item.lower()=="true":
        boolean_list.append(True)
    else:
        if '.' in item:
            float_list.append(float(item))
        else:
            integer_list.append(int(item))
print(integer_list)
print(float_list)
print(boolean_list)
