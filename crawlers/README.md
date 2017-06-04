# Desafio 2: Crawlers

Parte do trabalho na IDwall inclui desenvolver *crawlers/scrapers* para coletar dados de websites.
Como nós nos divertimos trabalhando, às vezes trabalhamos para nos divertir!

O Reddit é um... bom, é difícil de explicar. O importante é que o Reddit é um website de entretenimento e muito frequentado por procrastinadores :)

Subreddits são como fóruns dentro do Reddit e as postagens são chamadas *threads*.

Para quem gosta de gatos, há o subreddit ["/r/cats"](https://www.reddit.com/r/cats) com threads contendo fotos de gatos fofinhos.
Para *threads* sobre o Brasil, vale a pena visitar ["/r/brazil"](https://www.reddit.com/r/brazil) ou ainda ["/r/worldnews"](https://www.reddit.com/r/worldnews/).
Um dos maiores subreddits é o "/r/AskReddit".

Cada *thread* possui uma pontuação que, simplificando, aumenta com "up votes" (tipo um like) e é reduzida com "down votes".

Sua missão é encontrar e listar as *threads* que estão bombando no Reddit naquele momento!
Consideramos como bombando *threads* com 5000 pontos ou mais.

## Entrada
- Lista com nomes de subreddits. Ex: "askreddit;worldnews;cats"

### Parte 1
Gerar e imprimir uma lista contendo número de upvotes, subreddit, título da thread, link para os comentários da thread, link da thread.

### Parte 2
Construir um robô que nos envie essa lista via Telegram sempre que receber o comando "/NadaPraFazer askreddit;worldnews;cats"


Qualquer método para coletar os dados é válido. Caso não saiba por onde começar, procure por SeleniumHQ (Java), PhantomJS (Javascript) e Scrapy (Python).


## Rodando Projeto

 - sudo pip install virtualenv
 - virtualenv projetos
 - cd /projetos/
 - git clone https://github.com/reginaldojunior/desafios.git
 - run bot
     + cd crawlers
     + run dependencies pip "pip install -r requirements.txt"
     + python bot.py
 - run crawler
     + cd crawlers
     + run dependencies pip "pip install -r requirements.txt"
     + scrapy runspider reddit.py -a subreddit=r/{subreddit} -a chat_id={chat_id}

## BOT

Procure pelo bot @ScrapyIdWall_bot no Telegram.

/start: Mostra os comando e mensagem de boas vindas.
/NadaPraFazer subreddit1;subreddit2: Comando para crawlear as páginas e trazer os reddits mais votados.
