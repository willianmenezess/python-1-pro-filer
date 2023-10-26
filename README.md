# Project ProFiler - Eletiva Back-end com Python

Repositório do projeto ProFiler.
  
<details>
<summary><strong>🧑‍💻 O que deverá ser desenvolvido</strong></summary>

Você irá trabalhar com uma aplicação com uma interface de linha de comando (CLI) que recebe como entrada um caminho (diretório ou arquivo) e gera um relatório com informações sobre o caminho informado.

Para executar a aplicação:

1. Siga os passos do tópico [**🏕️ Ambiente Virtual**]
2. Configure o auto-complete da aplicação com o comando `pro-filer --install-completion` e reinicie o terminal;
3. Execute o comando `pro-filer` seguido de um caminho (diretório ou arquivo) e uma ação. Por exemplo:

```bash
pro-filer . preview
```

![pro-filer preview](./images/pro-filer-preview.gif)

A aplicação já está funcional, mas possui dois problemas:

1. alguns bugs precisam ser corrigidos;
2. mais testes precisam ser implementados.

Você deverá corrigir os bugs e implementar os testes para garantir que a aplicação funcione corretamente. Será o momento de aplicar tudo o que você aprendeu sobre debugging e testes automatizados em Python!

</details>
  
<details>
  <summary><strong>:memo: Habilidades a serem trabalhadas </strong></summary>

Neste projeto, verificamos se você é capaz de:

- Encontrar bugs no código de uma aplicação escrita em Python;
- Corrigir bugs no código de uma aplicação escrita em Python;
- Criar testes para uma aplicação escrita em Python;
- Utilizar o `pytest` para criar testes automatizados em uma aplicação escrita em Python.

<!-- 🤔 [HS] Escrevam as habilidade utilizando a Taxonomia de Bloom. -->

</details>

<details>
<summary><strong>‼ Antes de começar a desenvolver</strong></summary>

<!-- 🤔 [HS] Aqui, deve-se adicionar os comandos mais utilizados e orientações de como preparar o repositório. Atualize o nome do repositório do projeto nas instruções a seguir -->

1. Clone o repositório

- Use o comando: `git clone git@github.com:tryber/python-029-python-projeto-pro-filer.git`
- Entre na pasta do repositório que você acabou de clonar:
  - `cd python-029-python-projeto-pro-filer`

2. Instale as dependências

    - Siga os passos do tópico [**🏕️ Ambiente Virtual**]

3. Crie uma branch a partir da branch `main`

- Verifique que você está na branch `main`
  - Exemplo: `git branch`
- Se você não estiver, mude para a branch `main`
  - Exemplo: `git checkout main`
- Agora, crie uma branch à qual você vai submeter os `commits` do seu projeto:
  - Você deve criar uma branch no seguinte formato: `nome-sobrenome-nome-do-projeto`;
  - Exemplo: `git checkout -b maria-soares-pro-filer`

4. Crie na raiz do projeto os arquivos que você precisará desenvolver:

- Verifique que você está na raiz do projeto:
  - Exemplo: `pwd` -> o retorno vai ser algo tipo _/Users/maria/code/**python-029-python-projeto-pro-filer**_
- Crie ou edite algum arquivo necessário ao projeto

5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

- Verifique que as mudanças ainda não estão no _stage_:
  - Exemplo: `git status` (devem aparecer listados os novos arquivos em vermelho)
- Adicione o novo arquivo ao _stage_ do Git:
  - Exemplo:
    - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
    - `git status` (devem aparecer listados os arquivos em verde)
- Faça o `commit` inicial:
  - Exemplo:
    - `git commit -m 'iniciando o projeto. VAMOS COM TUDO :rocket:'` (fazendo o primeiro commit)
    - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

6. Adicione a sua branch com o novo `commit` ao repositório remoto

- Usando o exemplo anterior: `git push -u origin maria-soares-pro-filer`

7. Crie um novo `Pull Request` _(PR)_

- Vá até a página de _Pull Requests_ do repositório no GitHub em `<url_do_repositório>/pulls`:
  - Clique no botão verde _"New pull request"_
  - Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
- Coloque um título para o seu _Pull Request_
  - Exemplo: _"Cria tela de busca"_
- Clique no botão verde _"Create pull request"_

- Adicione uma descrição para o _Pull Request_, um título nítido que o identifique, e clique no botão verde _"Create pull request"_

 <img width="1335" alt="Exemplo de pull request" src="https://user-images.githubusercontent.com/42356399/166255109-b95e6eb4-2503-45e5-8fb3-cf7caa0436e5.png">

- Volte até a página de _Pull Requests_ do repositório no GitHub em `<url_do_repositório>/pulls` e confira que o seu _Pull Request_ está criado

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary>
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` instalará todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. Se você desejar instalar uma nova dependência, basta adicioná-la no arquivo `dev-requirements.txt` e executar o comando `python3 -m pip install -r dev-requirements.txt` novamente.

  Se o VS Code não reconhecer as dependências instaladas no ambiente virtual criado, será necessário informar o caminho do interpretador Python. Para isso, abra o VS Code e pressione `Ctrl + Shift + P` (no Mac, `Cmd + Shift + P`) e digite `Python: Select Interpreter`. Selecione o interpretador que possui o caminho `./.venv/bin/python` no nome.
</details>

<details>
<summary><strong>🎛 Linter</strong></summary>

Para garantir a qualidade do código, vamos utilizar nesse projeto o linter `Flake8`. Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível e de fácil manutenção! Para poder executar o `Flake8`, certifique-se de ter seguido os passos do tópico [**🏕️ Ambiente Virtual**] dentro do repositório.

Para rodá-lo localmente no repositório, execute o comando a seguir:

```bash
python3 -m flake8
```

Se a análise do `Flake8` encontrar problemas no seu código, tais problemas serão mostrados no seu terminal. Se não houver problema no seu código, nada será impresso no seu terminal.

</details>

<details>
  <summary><strong>🛠 Testes</strong></summary>

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o `pytest`. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv --continue-on-collection-errors
  ```

  O `pytest` possui diversos parâmetros que podem ser utilizados para executar os testes de diferentes formas. Alguns exemplos são:

  ```bash
  python3 -m pytest tests/test_nome_do_arquivo.py  # Executa todos os testes do arquivo de testes especificado
  python3 -m pytest tests/test_nome_do_arquivo.py::test_nome_do_teste  # Executa apenas o teste especificado
  python3 -m pytest -k expressao  # Executa apenas os testes que contém a expressão informada como substring
  python3 -m pytest -x  # Executa os testes até encontrar o primeiro erro
  ```

  Você pode combinar os parâmetros para executar os testes da forma que desejar! Para mais informações, consulte a [documentação do pytest](https://docs.pytest.org/en/7.3.x/contents.html).
</details>

## Requisitos do projeto

### 1. Elimine o(s) bug(s) da função `show_deepest_file`

> Arquivo a ser alterado: `pro_filer/actions/beta_actions.py`

Você está colaborando com a comunidade open-source e recebeu uma tarefa de corrigir bugs em algumas funções!

Encontre e corrija o(s) bug(s) da função `show_deepest_file` para que ela informe corretamente o caminho arquivo mais profundo dentro do diretório informado.

Execute os testes do arquivo `tests/actions/test_deepest_file.py` para te ajudar a encontrar o(s) bug(s): **você saberá que o(s) bug(s) foi(ram) corrigido(s) quando todos os testes desse arquivo passarem.**

<details>

<summary> 🤖 Comportamento esperado da função <code>show_deepest_file</code> </summary>

A função `show_deepest_file` deve receber um dicionário `context` com a chave `all_files` e imprime na saída padrão (`stdout`) o caminho do arquivo mais profundo dentro do diretório informado. A chave `all_files` armazena uma lista de strings, que representam os caminhos de todos os arquivos dentro de um diretório.

**O caminho mais profundo** será o caminho que possui a maior quantidade de diretórios aninhados. Considere esse exemplo:

```python
context = {
    "all_files": [
        "/home/trybe/Downloads/trybe_logo.png",
        "/home/trybe/Documents/aula/python/tests.txt",
    ]
}

show_deepest_file(context)
# Saída:
# Deepest file: /home/trybe/Documents/aula/python/tests.txt

context = {
    "all_files": []
}

show_deepest_file(context)
# Saída:
# No files found
```

Na primeira chamada, o arquivo com caminho mais profundo é `/home/trybe/Documents/aula/python/tests.txt`, pois ele possui 5 diretórios aninhados: `home`, `trybe` e `Documents`, `aula` e `python`.

Na segunda chamada, não há arquivos dentro do diretório informado, então a função imprime `No files found`.

> **De olho na dica 👀:** Essa função pode ser acionada pelo comando `pro-filer <caminho> deepest-file`!

</details>

<details>

<summary> 📌 O que será testado </summary>

- A função `show_deepest_file` deve imprimir, na saída padrão (`stdout`), o caminho do arquivo mais profundo dentro do diretório informado;
- A função `show_deepest_file` deve imprimir, na saída padrão (`stdout`), `No files found` caso não haja arquivos listados no dicionário `context`;
- Todos os testes do arquivo `tests/actions/test_deepest_file.py` devem passar.

</details>

### 2. Elimine o(s) bug(s) da função `find_file_by_name`

> Arquivo a ser alterado: `pro_filer/actions/beta_actions.py`

Com a resolução do último bug, as pessoas responsáveis pela manutenção do projeto ficaram extremamente satisfeitas e agora estão solicitando uma nova tarefa para você!

Encontre e corrija o(s) bug(s) da função `find_file_by_name` para que ela faça corretamente a busca de arquivos baseada em um termo de busca.

Execute os testes do arquivo `tests/actions/test_find_file_by_name.py` para te ajudar a encontrar o(s) bug(s): **você saberá que o(s) bug(s) foi(ram) corrigido(s) quando todos os testes desse arquivo passarem.**
<details>

<summary> 🤖 Comportamento esperado da função <code>find_file_by_name</code> </summary>

A função `find_file_by_name` deve receber como parâmetro:

- um dicionário `context` com a chave `all_files`, que armazena uma lista de strings, representando os caminhos de todos os arquivos dentro de um diretório
- uma _string_ `search_term` com a string a ser buscada
- (opcional) um _booleano_ `case_sensitive` que indica se a busca deve ser sensível a maiúsculas e minúsculas ou não. O valor padrão é `True`.

O retorno será uma lista de strings com os caminhos dos arquivos que possuem o termo buscado em seu nome.

**A busca é realizada** considerando apenas o nome do arquivo (com sua extensão), ignorando o nome das pastas. Considere esse exemplo:

```python
context = {
    "all_files": [
        "/home/trybe/Downloads/Trybe_logo.png",
        "/home/trybe/Documents/aula/python/tests.py",
    ]
}


find_file_by_name(context, '.py')
# Retorno: ["/home/trybe/Documents/aula/python/tests.py"]

find_file_by_name(context, 'trybe', case_sensitive=False)
# Retorno: ["/home/trybe/Downloads/Trybe_logo.png"]

context = {
    "all_files": []
}

find_file_by_name(context, "trybe")
# Retorno: []
```

Na 1ª chamada, apenas o segundo arquivo é encontrado pois apenas ele possui o termo `.py` em seu nome.

Já na 2ª chamada, apenas o primeiro arquivo é encontrado, pois apenas ele possui o termo `Trybe` em seu nome. Como `case_sensitive` foi passado como `False`, a busca não diferencia maiúsculas de minúsculas.

E na 3ª chamada, não há arquivos dentro do dicionário `context`, então a função retorna uma lista vazia.

> **De olho na dica 👀:** Essa função pode ser acionada pelo comando `pro-filer <caminho> search-file <termo_de_busca>`!

</details>

<details>

<summary> 📌 O que será testado </summary>

- A função `find_file_by_name` deve retornar uma lista com todos os caminhos de arquivos que possuem o a string `search_term` em seu nome, ignorando o nome das pastas;
- A função `find_file_by_name` deve realizar a busca por arquivos considerando corretamente o parâmetro `case_sensitive`;
- A função `find_file_by_name` deve retornar uma lista vazia caso não haja arquivos listados no dicionário `context`;
- Todos os testes do arquivo `tests/actions/test_find_file_by_name.py` devem passar.

</details>

### 3. Crie testes para a função `show_preview`

> Arquivo a ser alterado: `tests/actions/test_show_preview.py`

Agora que você já corrigiu bugs do projeto e mostrou que consegue trabalhar com o `Pytest`, as pessoas encarregadas do projeto solicitaram que você desenvolva testes para as funções que ainda não foram testadas!

Implemente testes para a função `show_preview` do arquivo `pro_filer/actions/main_actions.py` para garantir que ela está funcionando corretamente. **Os testes devem ser implementados no arquivo `tests/actions/test_show_preview.py`. Você pode criar quantas funções de teste desejar, desde que respeite o padrão do `Pytest`.**

<details>

<summary> 🤖 Comportamento esperado da função <code>show_preview</code> </summary>

A função `show_preview` deve receber como parâmetro um dicionário `context` com as chaves `all_files` e `all_dirs`:

- `all_files` armazena uma lista de strings, representando os caminhos de todos os arquivos dentro de um diretório;
- `all_dirs` armazena uma lista de strings, representando os caminhos de todos os diretórios dentro de um diretório.

A função imprime na saída padrão (`stdout`):

- A quantidade de arquivos e diretórios listados;
- Se houver algum dado nas chaves do dicionário `context`, os 5 primeiros arquivos listados;
- Se houver algum dado nas chaves do dicionário `context`, os 5 primeiros diretórios listados.

Considere esse exemplo:

```python
context = {
    "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
    "all_dirs": ["src", "src/utils"]
}


show_preview(context)
# Saída:
# Found 3 files and 2 directories
# First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']
# First 5 directories: ['src', 'src/utils']


context = {
    "all_files": [],
    "all_dirs": []
}


show_preview(context)
# Saída:
# Found 0 files and 0 directories
```

Na 1 primeira chamada, a função imprime as informações como.

Na 2ª chamada, não há arquivos listados em `all_files`, então a função imprime apenas o espaço total ocupado: `0`.

> **De olho na dica 👀:** Essa função pode ser acionada pelo comando `pro-filer <caminho> preview`!

> **De olho na dica 👀:** Execute o teste da Trybe `tests/trybe/show_preview_test.py` para verificar se seus testes cobrem todos os casos de uso previstos!

</details>

<details>

<summary> 📌 O que será testado </summary>

- Os seus testes rejeitam implementações de `show_preview` que consideram apenas `all_files` e `all_dirs` vazios;
- Os seus testes rejeitam implementações de `show_preview` que exibem mais do que 5 arquivos e/ou diretórios;
- Os seus testes aprovam a implementação de `show_preview` presente em `pro_filer/actions/main_actions.py`.

</details>

<details>
  <summary> 📌 Como seu teste é avaliado </summary>

O **teste da Trybe** irá avaliar se os **seus testes** estão passando conforme seu objetivo, e se estão falhando em alguns casos que deveria falhar.

Executaremos as funções de teste que você escrever no arquivo indicado (`tests/actions/test_show_preview.py`) substituindo a função sendo testada (`show_preview`) por outras implementações "quebradas".

❌ Se seu teste **aprovar** alguma das implementações "quebradas", **o teste da Trybe FALHARÁ**, indicando que o requisito **não está** aprovado.

✅ Se seu teste **rejeitar** todas as implementações "quebradas", **o teste da Trybe PASSARÁ**, indicando que o requisito **está** aprovado.

</details>

### 4. Crie testes para a função `show_details`

> Arquivo a ser alterado: `tests/actions/test_show_details.py`

Parabéns por todas as contribuições feitas até aqui! O time responsável pelo projeto está gostando do seu trabalho e tem uma nova tarefa para você: criar testes para outra funcionalidade!

Implemente testes para a função `show_details` do arquivo `pro_filer/actions/main_actions.py` para garantir que ela está funcionando corretamente. **Os testes devem ser implementados no arquivo `tests/actions/test_show_details.py`. Você pode criar quantas funções de teste desejar, desde que respeite o padrão do `Pytest`.**

<details>

<summary> 🤖 Comportamento esperado da função <code>show_details</code> </summary>

A função `show_details` deve receber como parâmetro um dicionário `context` com as chave `base_path`, que armazena uma string representando o caminho do arquivo (ou diretório) que deve ser analisado. A função então imprime na saída padrão (`stdout`) as seguintes informações:

- O nome do arquivo informado;
- O tamanho ocupado pelo arquivo informado;
- O tipo do arquivo informado (`file` ou `directory`);
- A extensão do arquivo informado (ou `[no extension]` caso não possua extensão);
- A data da última modificação do arquivo informado, no formato `yyyy-mm-dd`.

```python
context = {
    "base_path": "/home/trybe/Downloads/Trybe_logo.png"
}


show_details(context)
# Saída:
# File name: Trybe_logo.png
# File size in bytes: 22438
# File type: file
# File extension: .png
# Last modified date: 2023-06-13


context = {
    "base_path": "/home/trybe/????"
}


show_details(context)
# Saída:
# File '????' does not exist
```

Na 1ª chamada, o arquivo é um arquivo comum, então a função imprime `file` como tipo do arquivo e `.png` como extensão.

Na 2ª chamada, o arquivo informado não existe, então a função imprime `File '????' does not exist`.

> **De olho na dica 👀:** Essa função pode ser acionada pelo comando `pro-filer <caminho> file-details`!

> **De olho na dica 👀:** Execute o teste da Trybe `tests/trybe/show_details_test.py` para verificar se seus testes cobrem todos os casos de uso previstos!

</details>

<details>

<summary> 📌 O que será testado </summary>

- Os seus testes rejeitam implementações de `show_details` que não utilizam as mensagens corretas para exibir cada informação;
- Os seus testes rejeitam implementações de `show_details` que utilizam o formato de data incorreto;
- Os seus testes rejeitam implementações de `show_details` que não tratam corretamente o caso de o arquivo informado não existir;
- Os seus testes rejeitam implementações de `show_details` que não tratam corretamente o caso de o arquivo não possuir extensão;
- Os seus testes aprovam a implementação de `show_details` presente em `pro_filer/actions/main_actions.py`.

</details>

<details>
  <summary> 📌 Como seu teste é avaliado </summary>

O **teste da Trybe** irá avaliar se os **seus testes** estão passando conforme seu objetivo, e se estão falhando em alguns casos que deveria falhar.

Executaremos as funções de teste que você escrever no arquivo indicado (`tests/actions/test_show_details.py`) substituindo a função sendo testada (`show_details`) por outras implementações "quebradas".

❌ Se seu teste **aprovar** alguma das implementações "quebradas", **o teste da Trybe FALHARÁ**, indicando que o requisito **não está** aprovado.

✅ Se seu teste **rejeitar** todas as implementações "quebradas", **o teste da Trybe PASSARÁ**, indicando que o requisito **está** aprovado.

</details>

### 5. Crie testes para a função `show_disk_usage`

> Arquivo a ser alterado: `tests/actions/test_show_disk_usage.py`

Continuando suas contribuições no projeto, precisamos que você crie testes para mais uma funcionalidade importante do projeto!

Implemente testes para a função `show_disk_usage` do arquivo `pro_filer/actions/main_actions.py` para garantir que ela está funcionando corretamente. **Os testes devem ser implementados no arquivo `tests/actions/test_show_disk_usage.py`. Você pode criar quantas funções de teste desejar, desde que respeite o padrão do `Pytest`.**

<details>

<summary> 🤖 Comportamento esperado da função <code>show_disk_usage</code> </summary>

A função `show_disk_usage` deve receber como parâmetro um dicionário `context` com a chave `all_files`, que armazena uma lista de strings representando os caminhos de todos os arquivos dentro de um diretório. A função então imprime na saída padrão (`stdout`) o espaço total ocupado por todos os arquivos dentro do diretório informado.

A função então imprime na saída padrão (`stdout`) as seguintes informações:

- Para cada arquivo listado em `all_files`:
  - O caminho do arquivo;
  - O espaço ocupado pelo arquivo, em bytes;
  - A porcentagem do tamanho ocupado pelo arquivo em relação ao espaço total ocupado (por todos os arquivos listados em `all_files`);
- O espaço total ocupado por todos os arquivos listados em `all_files`, em bytes.

**A listagem de arquivos** é realizada em ordem decrescente de espaço ocupado. Considere esse exemplo:

```python
context = {
    "all_files": [
        "src/app.py",
        "src/__init__.py",
    ]
}


show_disk_usage(context)
# Saída:
# 'src/app.py':                                                          2849 (100%)
# 'src/__init__.py':                                                     0 (0%)
# Total size: 2849

context = {
    "all_files": []
}


show_disk_usage(context)
# Saída:
# Total size: 0
```

Na 1 primeira chamada, a função imprime a listagem de arquivos e seu tamanho em _bytes_ com a porcentagem do total e, ao final, o espaço total ocupado pelos arquivos listados.

Na 2ª chamada, não há arquivos listados em `all_files`, então a função imprime apenas o espaço total ocupado: `0`.

**Atenção ⚠️:** Como pode ser observado na implementação de `show_disk_usage`, a formatação de cada linha da listagem de arquivos é feita com auxílio da função `_get_printable_file_path`. Não se preocupe em validar o comportamento dessa função, você pode criar um dublê de teste para ela.

> **De olho na dica 👀:** Essa função pode ser acionada pelo comando `pro-filer <caminho> disk-usage`!

> **De olho na dica 👀:** Execute o teste da Trybe `tests/trybe/show_disk_usage_test.py` para verificar se seus testes cobrem todos os casos de uso previstos!

</details>

<details>

<summary> 📌 O que será testado </summary>

- Os seus testes rejeitam implementações de `show_disk_usage` que não calculam corretamente o espaço total ocupado pelos arquivos listados em `all_files`;
- Os seus testes rejeitam implementações de `show_disk_usage` que consideram todos os arquivos como vazios;
- Os seus testes rejeitam implementações de `show_disk_usage` que não ordenam corretamente a listagem de arquivos;
- Os seus testes aprovam a implementação de `show_disk_usage` presente em `pro_filer/actions/main_actions.py`;
- Os seus testes utilizam a fixture `tmp_path` para criar arquivos temporários.

</details>

<details>
  <summary> 📌 Como seu teste é avaliado </summary>

O **teste da Trybe** irá avaliar se os **seus testes** estão passando conforme seu objetivo, e se estão falhando em alguns casos que deveria falhar.

Executaremos as funções de teste que você escrever no arquivo indicado (`tests/actions/test_show_disk_usage.py`) substituindo a função sendo testada (`show_disk_usage`) por outras implementações "quebradas".

❌ Se seu teste **aprovar** alguma das implementações "quebradas", **o teste da Trybe FALHARÁ**, indicando que o requisito **não está** aprovado.

✅ Se seu teste **rejeitar** todas as implementações "quebradas", **o teste da Trybe PASSARÁ**, indicando que o requisito **está** aprovado.

</details>

### 6. Crie testes para a função `find_duplicate_files`

> Arquivo a ser alterado: `tests/actions/test_find_duplicate_files.py`

Para concluir sua participação na temporada de melhorias, as pessoas responsáveis pelo projeto têm uma última tarefa para você: criar testes para uma funcionalidade final!

Implemente testes para a função `find_duplicate_files` do arquivo `pro_filer/actions/main_actions.py` para garantir que ela está funcionando corretamente. **Os testes devem ser implementados no arquivo `tests/actions/test_find_duplicate_files.py`. Você pode criar quantas funções de teste desejar, desde que respeite o padrão do `Pytest`.**

<details>

<summary> 🤖 Comportamento esperado da função <code>find_duplicate_files</code> </summary>

A função `find_duplicate_files` deve receber como parâmetro um dicionário `context` com a chave `all_files`, que armazena uma lista de strings representando os caminhos de todos os arquivos dentro de um diretório.

A função então retorna uma lista de tuplas com os pares de arquivos que possuem o mesmo conteúdo.

Considere esse exemplo:

```python
context = {
    "all_files": [
        ".gitignore",
        "src/app.py",
        "src/utils/__init__.py",
    ]
}


find_duplicate_files(context)
# Retorno:
# []

context = {
    "all_files": [
        "./tests/__init__.py",
        "./tests/actions/__init__.py",
        "./pro_filer/__init__.py",
    ]
}

find_duplicate_files(context)
# Retorno:
# [
#     ('./tests/__init__.py', './tests/actions/__init__.py'),
#     ('./tests/__init__.py', './pro_filer/__init__.py'),
#     ('./tests/actions/__init__.py', './pro_filer/__init__.py')
# ]
```

Na 1 primeira chamada, o resultado é uma lista vazia pois não há arquivos duplicados: todos os arquivos possuem conteúdos diferentes.

Na 2ª chamada, o resultado é uma lista de tuplas com todos os pares de arquivos duplicados. Como todos os arquivos possuem o mesmo conteúdo, todos os pares são retornados.

> **Atenção ⚠️:** Como pode ser observado na implementação de `find_duplicate_files`, a comparação de conteúdo de arquivos é feita com auxílio da função `filecmp.cmp(...)`. Essa função é nativa do Python, e compara o conteúdo dos arquivos (retornando `True` se forem iguais). Caso algum dos arquivos não exista, é levantada uma exceção `FileNotFoundError`.

Caso a exceção `FileNotFoundError` seja levantada na chamada de `filecmp.cmp(...)`, a função `find_duplicate_files` levantará uma exceção `ValueError`. Você deve testar se a exceção `ValueError` é levantada caso algum arquivo em `all_files` não exista.

> **De olho na dica 👀:** Essa função pode ser acionada pelo comando `pro-filer <caminho> find-duplicate`!

> **De olho na dica 👀:** Execute o teste da Trybe `tests/trybe/find_duplicate_test.py` para verificar se seus testes cobrem todos os casos de uso previstos!

</details>

<details>

<summary> 📌 O que será testado </summary>

- Os seus testes rejeitam implementações de `find_duplicate_files` que consideram todos os arquivos em `all_files` como diferentes;
- Os seus testes rejeitam implementações de `find_duplicate_files` que consideram todos os arquivos em `all_files` como iguais;
- Os seus testes rejeitam implementações de `find_duplicate_files` que não levanta `ValueError` caso algum arquivo em `all_files` não exista;
- Os seus testes aprovam a implementação de `find_duplicate_files` presente em `pro_filer/actions/main_actions.py`;
- Os seus testes utilizam a fixture `tmp_path` para criar arquivos temporários.

</details>

<details>
  <summary> 📌 Como seu teste é avaliado </summary>

O **teste da Trybe** irá avaliar se os **seus testes** estão passando conforme seu objetivo, e se estão falhando em alguns casos que deveria falhar.

Executaremos as funções de teste que você escrever no arquivo indicado (`tests/actions/test_show_disk_usage.py`) substituindo a função sendo testada (`show_disk_usage`) por outras implementações "quebradas".

❌ Se seu teste **aprovar** alguma das implementações "quebradas", **o teste da Trybe FALHARÁ**, indicando que o requisito **não está** aprovado.

✅ Se seu teste **rejeitar** todas as implementações "quebradas", **o teste da Trybe PASSARÁ**, indicando que o requisito **está** aprovado.

</details>

---

<!-- mdi versão 1.0 projeto python ⚠️ não exclua esse comentário -->
