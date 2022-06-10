from jinja2 import Template

name = input("Enter name: ")
age = int(input("Enter age: "))

t = Template("Hello {{name}} you are {{age}} years old")

m = t.render(name=name, age=age)

print(m)

print("\n\n")

lt = [1, {"shreyas": "gavhalkar", "vishwakarma": "college"}, 1.4, True]

with open("practice.html.jinja") as f:
    tmp = Template(f.read())
print(tmp.render(l=lt))
