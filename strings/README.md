# Desafio 1: Strings

Após ler o coding style do kernel Linux, você descobre a mágica que é 
ter linhas de código com, no máximo, 80 caracteres cada uma.

Assim, você decide que de hoje em diante seus e-mails enviados também 
seguirão este padrão e resolve desenvolver um plugin para te ajudar
com isso.

Implemente uma função que receba 
1. um texto qualquer e 
2. um limite de
comprimento e seja capaz de gerar os outputs dos desafios abaixo.

## Exemplo input

`In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.`

`And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.`


### Parte 1 (Básico) - limite 40 caracteres

`In the beginning God created the heavens
and the earth. Now the earth was
formless and empty, darkness was over
the surface of the deep, and the Spirit
of God was hovering over the waters.`

`And God said, "Let there be light," and
there was light. God saw that the light
was good, and he separated the light
from the darkness. God called the light
"day," and the darkness he called
"night." And there was evening, and
there was morning - the first day.`

### Parte 2 (Intermediário) - limite 40 caracteres

`In the beginning God created the heavens
and   the  earth.   Now  the  earth  was
formless  and empty,  darkness was  over
the  surface of the deep, and the Spirit
of  God was  hovering over  the  waters.`

`And  God said, "Let there be light," and
there  was light. God saw that the light
was  good, and  he separated  the  light
from  the darkness. God called the light
"day,"   and  the   darkness  he  called
"night."  And  there  was  evening,  and
there  was  morning  -  the  first  day.`


## Rodando

 - sudo pip install virtualenv
 - virtualenv projetos
 - cd /projetos/
 - git clone https://github.com/reginaldojunior/desafios.git
  - Rode "pip install -r requirements.txt"
  - Edite o arquivo input.txt se deseja e rode "python format.py"
