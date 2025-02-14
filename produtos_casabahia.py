import pandas as pd
from bs4 import BeautifulSoup
from configuration import Configuration

configuration = Configuration()

nome_produto_buscar = "smart tv 4k".replace(" ", "-")
dados_produtos = []

try:
    for page in range(1, 3):
        url_pagina = f"https://www.casasbahia.com.br/{nome_produto_buscar}/b?&page={page}"
        driver = configuration.configure_webdriver(url_pagina, headless=False)
        # driver.maximize_window()

        html = driver.page_source

        soup = BeautifulSoup(html, "html.parser")

        lista_produtos = soup.find_all("div", class_="dsvia-link-box dsvia-product-card productCard-busca css-1x75gno")

        for lista in lista_produtos:
            # Nome do produto
            nome_produto_element = lista.select_one("h3.product-card__title > a")
            if nome_produto_element:
                nome_produto = nome_produto_element.get("title")
                parcelamento = lista.find("div", class_="product-card__installment-text")
                texto_parcelamento = parcelamento.find("span", class_="css-1vmkvrm").get_text(strip=True)
                valor_pix = lista.find("div", class_="product-card__highlight-price")
                pix = valor_pix.get_text(strip=True)
            else:
                nome_produto = ""
                texto_parcelamento = ""
                pix = ""
            print(f"Produto: {nome_produto}", f"Parcelamento: {texto_parcelamento}", f"Valor no Pix: {pix}")

            dados_produtos.append([nome_produto, texto_parcelamento, pix])

        driver.quit()

finally:
    print("Fechando o navegador")

    df = pd.DataFrame(dados_produtos, columns=["Nome do Produto", "Parcela", "Valor no Pix"])
    df.to_excel("produtos_casasbahia.xlsx", index=False)
    print("Planilha Excel criada com sucesso!")