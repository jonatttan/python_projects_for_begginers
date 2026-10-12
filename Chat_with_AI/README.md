<div align="center">

# 🤖 Python Projects for Beginners

### Sistema de chat de IA com Python

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow?style=for-the-badge)](#-status-do-projeto)

**Projetos práticos para introdução ao Python com alguns casos de uso correlacionados ao mundo real.**

[Sobre](#-sobre-o-projeto) •
[Objetivos](#-objetivos) •
[Tecnologias](#️-tecnologias) •
[Demonstração](#-demonstração) •
[Instalação](#-instalação) •
[Como usar](#️-como-usar) •

</div>

---

## 📌 Sobre o projeto

Nesse projeto abordamos uma forma de construir um sistema de chat integrando com a IA de sua escolha. Muito útil para se ter uma base e exercitar habilidades nesse tipo de construção, afim de implementar em sistemas empresariais para colaboradores ou mesmo como um chat de contexto fechado dentro de uma página institucional para uso de clientes. Não foi abordado nessa primeira versão, mas conseguimos passar um contexto por mensagem, ou mesmo adicionar documentos de formatos variados para que o chat receba insumos e responda baseado estritamente naquelas informações. Esses dados não ficam salvas fora da sessão, o que dá um certo nível de segurança.

> 💡 **Ideia central:** Construção de um sistema de chat com IA usando a linguagem Python.

---

### 🎯 Objetivos

- 🕒 Construir um sistema de chat usando uma ferramenta de solução pra web (Lib streamlit).
- ⚙️ Lidar com listas e dicionários dentro de cache da biblioteca.
- 🧩 Entender a integração com APIs de IA (Lib openai).
- 📚 Aprender a estrutura e filtragem de retorno dos dados na consulta com a IA.
- 🚀 Conhecer as possibilidades de evolução do projeto.

---

## 🛠️ Tecnologias

| Tecnologia | Utilização |
|---|---|
| 🐍 Python | Linguagem principal |
| 📦 pip | Gerenciamento de dependências |
| 📝 Git e GitHub | Versionamento e hospedagem do projeto |

---

## 📸 Demonstração

> Demonstração do projeto de automação.

![Demonstração do projeto de asistende de chat com IA](sample_images/PythonChatWithAI.gif)

---

## 🚀 Instalação

### Pré-requisitos

- [Python 3.10 ou superior](https://www.python.org/downloads/)
- Git instalado na máquina

### 1. Clone o repositório

```bash
git clone https://github.com/jonatttan/python_projects_for_begginers.git
cd Chat_with_AI
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 3. Crie e edite o .env

Para sua chave de API de IA, crie um arquivo para armazená-la e poder utilizar no código.
Dentro do diretório do arquivo ChatWithAI.py, execute o comando abaixo com sua chave.

##### macOS / Linux
```bash
echo 'AI_API_KEY = "sua_key"' >> .env
```

##### Windows (CMD)
```bash
echo AI_API_KEY = "sua_key">> .env
```

##### Windows (PowerShell)
```bash
Add-Content .env 'AI_API_KEY = "sua_key"'
```

## ▶️ Como usar

Depois de configurar o ambiente, ainda no diretório do arquivo 'ChatWithAI.py", execute o comando abaixo no terminal.
```bash
streamlit run ChatWithAI.py
```

---

<div align="center">

⭐ **Se este projeto foi útil para você, considere deixar uma estrela!**

Feito com 🐍 Python e ☕

</div>
