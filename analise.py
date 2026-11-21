import csv
import json
from pathlib import Path


def analisar_vendas():
    # Usa a pasta deste arquivo para localizar os dados.
    pasta = Path(__file__).resolve().parent

    # Lê as configurações gerais da empresa.
    with (pasta / "configuracao.json").open(encoding="utf-8") as arquivo:
        configuracao = json.load(arquivo)

    # Lê cada linha do CSV como uma venda, usando os nomes das colunas como chaves.
    with (pasta / "vendas.csv").open(encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        vendas = list(leitor)

    # Encerra a análise quando o arquivo não contém vendas.
    if not vendas:
        print("Nenhuma venda foi encontrada.")
        return

    # Prepara os valores que serão somados durante a leitura das vendas.
    faturamento = 0
    unidades = 0
    quantidades_por_produto = {}

    print(f"ANÁLISE DE VENDAS — {configuracao['empresa']}")
    print(f"Período: {configuracao['periodo']['descricao']}\n")

    # Calcula o valor de cada venda e acumula os totais do período.
    for venda in vendas:
        numero = venda["id_venda"]
        data = venda["data"]
        produto = venda["produto"].strip()
        quantidade = float(venda["quantidade"])
        preco = float(venda["preço"])
        total = quantidade * preco

        faturamento += total
        unidades += quantidade

        if produto in quantidades_por_produto:
            quantidades_por_produto[produto] += quantidade
        else:
            quantidades_por_produto[produto] = quantidade

        print(
            f"Venda {numero} ({data}) — {produto}: "
            f"{quantidade:g} unidade(s) × R$ {preco:.2f} = R$ {total:.2f}"
        )

    # Descobre qual produto teve a maior quantidade vendida.
    produto_destaque = ""
    quantidade_destaque = 0
    for produto, quantidade in quantidades_por_produto.items():
        if quantidade > quantidade_destaque:
            produto_destaque = produto
            quantidade_destaque = quantidade

    meta = float(configuracao["meta_faturamento"])
    orcamento_despesas = float(configuracao["orcamento_despesas"])
    despesas = configuracao["despesas_detalhadas"]

    # Soma as despesas previstas e calcula o saldo do orçamento e o caixa estimado.
    total_despesas = 0
    for valor in despesas.values():
        total_despesas += float(valor)

    saldo_orcamento = orcamento_despesas - total_despesas
    total_no_caixa = saldo_orcamento + faturamento

    # Exibe o resumo das vendas e informa se a meta foi alcançada.
    print("\nRESUMO DO PERÍODO")
    print(f"Faturamento total: R$ {faturamento:.2f}")
    print(f"Unidades vendidas: {unidades:g}")
    print(f"Número de vendas: {len(vendas)}")
    print(
        f"Produto com mais unidades vendidas: {produto_destaque} "
        f"({quantidade_destaque:g} unidade(s))"
    )
    print(f"Meta de faturamento: R$ {meta:.2f}")
    if faturamento >= meta:
        print(f"Meta atingida! Excedente: R$ {faturamento - meta:.2f}.")
    else:
        print(f"Meta não atingida. Faltaram R$ {meta - faturamento:.2f}.")

    # Mostra os itens de despesa e compara o total com o orçamento disponível.
    print("\nDESPESAS PREVISTAS")
    for nome, valor in despesas.items():
        nome_legivel = nome.replace("_", " ").capitalize()
        print(f"{nome_legivel}: R$ {float(valor):.2f}")

    print(f"Total de despesas previstas: R$ {total_despesas:.2f}")
    print(f"Orçamento para despesas: R$ {orcamento_despesas:.2f}")
    if saldo_orcamento >= 0:
        print(
            f"Saldo restante do orçamento: R$ {saldo_orcamento:.2f}"
        )
    else:
        print(
            f"Despesas acima do orçamento: "
            f"R$ {-saldo_orcamento:.2f}"
        )
    print(f"Total estimado no caixa: R$ {total_no_caixa:.2f}")


if __name__ == "__main__":
    try:
        analisar_vendas()
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as erro:
        print(f"Não foi possível concluir a análise: {erro}")
