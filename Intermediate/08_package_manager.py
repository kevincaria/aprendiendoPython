#Python package manager 

# PIP https://pypi.org

# pip install pip
# pip --version

# pip install requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package


print(arithmetics.sum_two_values(1, 4))