# 99freelas-desafio1
Tratamento de XML e Excel com Python

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

Costumo vasculhar projetos no site 99freelas em busca de desafios interessantes. Busco principalmente projetos em Python com especificações claras e regras bem escritas. Quando encontro algo, sem contatar o solicitante, inicio o projeto estudando quais tecnologias, técnicas e abordagens serão eficientes para entregar as funcionalidades com qualidade. Não recebo dinheiro por esse trabalho, meus objetivos principais são a prática profissional, o desenvolvimento técnico de programação e a construção de portfólio.

## Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)<br>
:small_blue_diamond: [Funcionalidades](#funcionalidades)<br>
:small_blue_diamond: [Acesso ao projeto](#acesso-ao-projeto)<br>
:small_blue_diamond: [Pré-requisitos](#pré-requisitos)<br>
:small_blue_diamond: [Abrir e rodar o projeto](#abrir-e-rodar-o-projeto)<br>
:small_blue_diamond: [Tecnologias utilizadas](#tecnologias-utilizadas)<br>

## Descrição do Projeto

O objetivo desse projeto é buscar processos publicados no arquivo XML da Revista da Propriedade Industrial. O script deverá recuperar os atributos das tags especificadas apenas dos processos listados no arquivo de texto `processos.txt` e posteriormente, salvar os resultados na planilha `processos.xlsx` que poderá ser editada no Microsoft Excel ou no LibreOffice Calc.

## Funcionalidades

- `Funcionalidade 1`: Disponibiliza o arquivo `processos.txt` para o usuário informar a relação dos processos que pretende pesquisar. Em cada linha deverá constar um número diferente de processo.

- `Funcionalidade 2`: Recupera do arquivo XML os atributos com o número do processo, titular, nome do despacho e o seu texto complementar.

- `Funcionalidade 3`: Centraliza o texto, fixa as duas primeira linhas da planilha e informa a data da revista RPI e os nomes das colunas.

## Acesso ao projeto

Você pode acessar o [código fonte](https://github.com/eder-projetos-dev/99freelas-desafio1) ou [baixá-lo](https://github.com/eder-projetos-dev/99freelas-desafio1/archive/refs/heads/main.zip)

~~~bash
git clone git@github.com:eder-projetos-dev/99freelas-desafio1.git
~~~

## Pré-requisitos

Baixe e instale o Python 3.10 no link abaixo: <br>
[https://www.python.org/downloads/](https://www.python.org/downloads/)<br>

Caso precise, instale o gerenciador de pacotes pip versão 22.3 (ou superior):<br>
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

Atualizando o pip no Windows
```bash
python.exe -m pip install --upgrade pip
````

Instale a biblioteca openpyxl no Windows:<br>
```bash
pip install openpyxl
```

No Linux utilize esse comando:<br>
```bash
pip3 install openpyxl
```

Informações adicionais:<br>
[https://openpyxl.readthedocs.io](https://openpyxl.readthedocs.io)<br>
[https://docs.python.org/3/library/xml.etree.elementtree.html](https://docs.python.org/3/library/xml.etree.elementtree.html)

## Abrir e rodar o projeto

Abrindo o projeto no IDLE:
- Clique no menu `File`, `Open`;
- Procure o local onde você salvou o projeto e selecione o arquivo `main.pyw`.
- Com o arquivo aberto, pressione a tecla <kbd>F5</kbd> ou vá no menu `Run` e em seguida `Run Module`. :heavy_check_mark:


## Tecnologias utilizadas

- ``Python 3.10`` :snake:
- ``openpyxl``
- ``The ElementTree XML API``
- ``IDLE 3.10``

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/%C3%A9der-lu%C3%ADs-britto-garcia-803778207/
