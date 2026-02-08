# 🤖 Bot de Automação de Cadastro de Produtos

Este projeto é uma automação de processos (RPA) desenvolvida em **Python**. O bot automatiza o login em um sistema web, lê uma base de dados de produtos e realiza o cadastro de cada item automaticamente, economizando tempo e evitando erros humanos.

## 🚀 Funcionalidades
- **Auto-Login:** Abre o navegador e realiza login no sistema da empresa.
- **Processamento de Dados:** Lê um arquivo CSV utilizando a biblioteca `Pandas`.
- **Preenchimento Automático:** Utiliza a `PyAutoGUI` para controlar mouse e teclado, preenchendo os formulários campo a campo.
- **Lógica de Verificação:** Trata observações vazias na base de dados antes de preencher.

## 🛠️ Tecnologias Utilizadas
- **Python**
- **PyAutoGUI**: Para automação de interface (teclado e mouse).
- **Pandas**: Para manipulação da base de dados.
- **Time**: Para controle de intervalos entre comandos.

## ⚠️ Requisitos
Para rodar este bot, você precisará instalar as dependências:
```bash
pip install pyautogui pandas
```
> **Nota:** Este bot utiliza coordenadas de tela específicas (x e y). Para rodar em telas diferentes, as coordenadas podem precisar de ajuste usando o comando pyautogui.position().
---





