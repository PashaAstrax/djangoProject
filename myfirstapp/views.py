from django.shortcuts import render

def multi(request, num1, action, num2):
    global res
    if action == "*":
        res = int(num1 * num2)
    elif action == "div":
        res = int(num1 / num2)
    elif action == "+":
        res = int(num1 + num2)
    elif action == "-":
        res = int(num1 - num2)
    return render(request, "Multi_table.html", {"num1": num1, "action": action, "num2": num2, "res": res})