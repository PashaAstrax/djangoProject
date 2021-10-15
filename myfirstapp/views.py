from django.shortcuts import render

users_list = []

def hello(request):
    return render(request, "hello.html")

# def users(request):
#     return render(request, "users.html")

def users(request, name):
    users_list.append(name)
    check = False if len(users_list) > 3 else True
    return render(request, "users.html", {"xxx": name, "users": users_list, "check": check})

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