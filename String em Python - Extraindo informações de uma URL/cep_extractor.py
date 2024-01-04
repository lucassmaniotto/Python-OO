address = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re

pattern = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
search = pattern.search(address)  # Match
if search:
    cep = search.group()
    print(cep)