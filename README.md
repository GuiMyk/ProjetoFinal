# Análise de Vendas — Livraria Página Viva

Este projeto analisa as vendas de uma livraria online. Os dados atuais são de novembro de 2026 e incluem livros, quantidades vendidas e preços.

## Arquivos do projeto

- `analise.py`: lê os arquivos de dados, faz os cálculos e exibe o relatório.
- `configuracao.json`: contém informações da empresa, período, meta de faturamento e orçamento de despesas.
- `vendas.csv`: contém uma venda por linha, com identificador, data, produto, quantidade e preço.

## O que o programa faz

O programa usa os módulos `csv` e `json`, que já fazem parte do Python. Não é necessário instalar bibliotecas adicionais.

Ao ser executado, ele:

1. Lê as configurações de `configuracao.json` e as vendas de `vendas.csv`.
2. Mostra o total de cada venda.
3. Calcula o faturamento, as unidades vendidas e o produto com mais unidades vendidas.
4. Compara o faturamento com a meta definida na configuração.
5. Mostra as despesas previstas e verifica se elas estão dentro do orçamento.
6. Calcula o total estimado no caixa pela fórmula:
   `saldo restante do orçamento + faturamento`
   O saldo restante do orçamento é calculado como `orçamento para despesas - despesas previstas`.

## Como executar no Windows

É necessário ter o Python 3 instalado. Se ainda não tiver, instale-o pelo [site oficial do Python](https://www.python.org/downloads/windows/) e marque a opção para adicionar o Python ao PATH durante a instalação.

Abra o PowerShell na pasta do projeto e execute:

```powershell
python analise.py
```

Se o comando `python` não for reconhecido, tente:

```powershell
py analise.py
```

O relatório será exibido no terminal.
