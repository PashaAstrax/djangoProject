from django.shortcuts import render

def multi(request, num1, action, num2):

    if action == "*":
        res = f"{num1} * {num2} = {num1*num2}"
    elif action == "div":
        res = f"{num1} / {num2} = {num1/num2}"
    elif action == "+":
        res = f"{num1} + {num2} = {num1+num2}"
    elif action == "-":
        res = f"{num1} - {num2} = {num1-num2}"
    else:
        res = "wrong"

    return render(request, "Multi_table.html", {"num1": num1, "action": action, "num2": num2, "res": res})