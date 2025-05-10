import re

txt = "The rain in Spain"
#Check if "ain" is present,and return the whole word:
x = re.findall(r"\S*ain", txt)

import re
sentence = "hola como estas 123 hola"
matches = re.search("hola", sentence)
print(matches.start()) #donde la encontró

# '\b' asegura que coincidamos con palabras completas.
regex = r'\b' + re.escape(palabra) + r'\b' 
matches = list(re.finditer(regex, texto)) # Obtenemos los índices de los matches encontrados 
indices = [match.start() for match in matches]