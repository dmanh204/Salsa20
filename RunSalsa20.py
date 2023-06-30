from Salsa20 import Salsa20
key = "9e33bd7c6068e87fbe8aa2e7c5628f0d3699a5c5f108fdc1e995982028cbfb7c"
nonce = "947cb4326dba6e79"
output = ""

k = Salsa20(key, nonce)
for i in range(1954):
    output += k.run()

with open("salsa20.manh.txt", "w") as f:
    f.write(output)