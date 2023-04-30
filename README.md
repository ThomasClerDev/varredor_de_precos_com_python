# varredor_de_precos_com_python

Nesta parte do bootcamp, criamos um código para varrer sites previamente selecionados para buscar o menor preço de um determinado produto, servindo para fazer varreduras diárias no dia para uma possível compra com o melhor preço.

Os sites fictícios foram fornecidos pelo menistro do bootcamp, sendo eles:
https://sitepreco1.netlify.app/
https://sitepreco2.netlify.app/
https://sitepreco3.netlify.app/

Feita a busca e encontrados os preços, o código irá fazer a inserção dos preços em uma planilha.

Importante lembrar que neste código em específico, procuramos o melhor preço do produto "ABACATE".

Bibliotecas Python utilizadas: 
 - Selenium - Te permite abrir navegadores através de webdriver (navegador que você pode enviar comandos python para ele)
 
Depois: <br>
 1 - Escolher qual navegador quer utilizar ( recomendado o chrome, por ser mais estável)
 2 - Instalar esse navegador no PC do cliente
 3 - Instalar o Selenium via terminal - $ pip install selenium
 4 - Instalar um webdriver, através do webdriver-manager (pelo terminal) - $ pip install webdriver-manager

Para extração de dados no navegador utilizamos o XPATH - O caminho para chegar até um elemento dentro do HTML

* Para montar um XPATH, você precisa de digitar // e o nome da tag no "Inspecionar página - F11" e depois F8 para fazer essa pesquisa.
Ficando: //nome_da_tag[@atributo='valor_do_atributo']
