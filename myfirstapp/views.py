from django.shortcuts import render

def multi(request, num1, action, num2, num3):

    if action == "*":
        res = f"{num1} * {num2} = {num3}"
        return res

    # elif action == "div":
    #     res = int(num1 / num2)
    # elif action == "+":
    #     res = int(num1 + num2)
    # elif action == "-":
    #     res = int(num1 - num2)
    return render(request, "Multi_table.html", {"num1": num1, "action": action, "num2": num2, "num3": num3})