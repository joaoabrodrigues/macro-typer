# macro-typer

Script para copiar o texto e digitar automaticamente após um delay em segundos (default 2 segundos).

## Requisitos 

 - python3, pip3, pynput, pyperclip

## Pré instalação
`sudo apt install python3, pip3, xclip`

`pip3 install pynput pyperclip`

## Como usar

Uso:   

`python3 paste.py [-h] [-d N] [-t TEXT] [-u]`

Argumentos opicionais:  
```
  -h, --help            show this help message and exit  
  -d N, --delay N       Time delay to paste (in seconds)  
  -t TEXT, --text TEXT  Text to be typed  
  -u, --uppercase       Convert text to Uppercase
```
Exemplo:

`python3 paste.py --delay=1`

O script pegará o que estiver na área de transferência e colará após o delay configurado(no caso 1 segundo).


## Dica

Para uma melhor experiência, é interessante criar um atalho customizado no teclado, que executará o comando citado anteriormente.

Sendo assim, é possível usar Ctrl+C e depois o seu atalho customizado (por exemplo: Ctrl+Alt+V) para colar.
