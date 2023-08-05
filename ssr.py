# Load datra
dados = [
    {"name": "João", "age": 30, "city": "São Paulo"},
    {"name": "Maria", "age": 20, "city": "Rio de Janeiro"},
    {"name": "José", "age": 40, "city": "Curitiba"}
]

# Process data
template = """\
<html>
    <body>
        <ul>
            <li> Name: {data[name]} </li>
            <li> Age: {data[age]} </li>
            <li> City: {data[city]} </li>
        </ul>
    </body>
</html>
"""

# Render

for data in dados:
    print(template.format(data=data))