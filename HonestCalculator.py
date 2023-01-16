import sys
def start_function():
    print(msg[0])
    equation = input().split(" ")
    if (not equation[0].islower() and not equation[2].islower()) or equation[0] == "M" or equation[-1] == "M":
        if equation[0] == "M": equation[0] = str(memory)
        if equation[2] == "M": equation[2] = str(memory)
        else:
            pass
        x = float(equation[0])
        y = float(equation[-1])
        laziness_function(x,y,equation[1])
        if equation[1] == "+":
            memory_function(summ_function(x, y))
        elif equation[1] == "-":
            memory_function(substr_function(x, y))
        elif equation[1] == "*":
            memory_function(multpl_function(x, y))
        elif equation[1] == "/":
            memory_function(divsn_function(x, y))
        else:
            print(msg[2])
    else:
        print(msg[1])
def summ_function(a,b):
    result = a+b
    print(result)
    return result
def substr_function(a,b):
    result = a - b
    print(result)
    return result
def multpl_function(a,b):
    result = a * b
    print(result)
    return result
def divsn_function(a,b):
    try:
        result = a / b
        print(result)
        return result
    except ZeroDivisionError:
        print(msg[3])
        start_function()
def memory_function(result):
    global memory
    print(msg[4])
    if input() == "y":
        if -10 < result < 10 and result.is_integer():
            msg_index = 10
            print(msg[msg_index])
            while input() == "y" and msg_index<11:
                msg_index += 1
                print(msg[msg_index])
                if input() == "y" and msg_index == 11:
                    print(msg[msg_index + 1])
                    memory = result
                else:
                    break
            else: pass
        else: memory = result
    else: memory = 0.0
    continue_code_func()
def continue_code_func():
    print(msg[5])
    if input() == "n": sys.exit()
    else: start_function()
def laziness_function(x,y,oper):
    msg_word = ""
    if -10<x<10 and x.is_integer() and -10<y<10 and y.is_integer():msg_word += msg[6]
    if (x == 1 or y == 1) and oper == "*":msg_word+=msg[7]
    if (x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):msg_word+=msg[8]
    if msg_word == "": pass
    else:print(msg[9]+msg_word)




msg = ["Enter an equation",
"Do you even know what numbers are? Stay focused!",
"Yes ... an interesting math operation. You've slept through all classes, haven't you?",
"Yeah... division by zero. Smart move...",
"Do you want to store the result? (y / n):",
"Do you want to continue calculations? (y / n):",
" ... lazy",
" ... very lazy",
" ... very, very lazy",
"You are",
"Are you sure? It is only one digit! (y / n)",
"Don't be silly! It's just one number! Add to the memory? (y / n)",
"Last chance! Do you really want to embarrass yourself? (y / n)"]

memory = 0.0
start_function()