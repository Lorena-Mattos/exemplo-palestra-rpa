# Web Scraping de Produtos da Casas Bahia

Este projeto realiza a coleta automatizada de dados de produtos da Casas Bahia, como nome, condições de parcelamento e valor no Pix, e os exporta para uma planilha Excel.

## 🚀 Funcionalidades

- Busca produtos com base em um termo de pesquisa (ex: "smart tv 4k").
- Navega por múltiplas páginas de resultados.
- Extrai informações como:
  - Nome do produto
  - Condições de parcelamento
  - Preço com desconto no Pix
- Gera uma planilha Excel (`produtos_casasbahia.xlsx`) com os dados coletados.

## 📥 Instalação

1. **Pré-requisitos**:
   - Python 3.x instalado.
   - WebDriver compatível com seu navegador (ex: ChromeDriver para Google Chrome).

2. **Instalar dependências**:
   ```bash
   pip install pandas beautifulsoup4 selenium

   
 ## ⚙️ Configuração:
 - Certifique-se de que o arquivo configuration.py esteja configurado para usar o WebDriver corretamente.
 - Atualize o caminho do WebDriver no código se necessário.

## ▶️ Como Usar
Clone o repositório:
```bash
git clone https://github.com/seu-usuario/projeto-casasbahia.git
cd projeto-casasbahia
```
Execute o script:
```bash
python produtos_casabahia.py
```

## 🛠 Tecnologias Utilizadas
- Python: Linguagem principal.
- Pandas: Manipulação de dados e exportação para Excel.
- BeautifulSoup: Extração de dados HTML.
- Selenium: Automação da navegação web.

## 🔧 Melhorias Futuras
- Adicionar suporte para mais sites de e-commerce.
- Implementar tratamento robusto de erros e timeout.
- Adicionar interface gráfica (GUI) para facilitar a interação.
- Permitir escolha de termos de busca via input do usuário.

## ⚠️ Aviso
- Este projeto é apenas para fins educacionais.
- O web scraping pode violar os termos de serviço de alguns sites. Use com responsabilidade e respeite as políticas do alvo.

## 📝 Licença

Distribuído sob a licença MIT. Veja [LICENSE](https://github.com/Lorena-Mattos/exemplo-palestra-rpa/blob/main/LICENSE) para mais detalhes.

---

**Contribuições são bem-vindas!**

Se encontrar problemas, abra uma [issue](https://github.com/Lorena-Mattos/exemplo-palestra-rpa/issues) ou envie um pull request.
