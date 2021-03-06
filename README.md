<div align="center">
<!-- Title: -->
  <a href="https://pandasbots.com"><img src="https://avatars.githubusercontent.com/u/81653170?s=96&v=4" height="100"></a>
  <h1><a href="https://pandasbots.com">Pandas Bots</a> - Python</h1>  
<!-- Short description: -->
<h3>Automation that saves time and money. <a href="https://pandasbots.com/get-in-touch">Contact us now!</a></h3>
</div>
<!-- Description: -->

Implementations are for learning purposes only. As they may be less efficient than the implementations in the Python standard library, use them at your discretion.

<div align="left">

# DISCLAIMER

This package requires selenium. For that reason it will may not work if you are using Google Colab or similar.

# Project Gimbel Mexicana

* GitHub: https://github.com/PandasBots/pandasbots-gimbel
* Ref.: https://gimbelmexicana.com/
* Author: Rafael Klanfer Nunes

## Description:

User will input the website URL and the program will return:

* Excel file containing product info.

* PDF file containg product instructions.

* JSON file with:

1. name:  The name of the product
2. code: The SKU of the product (codigo)
3. Image: The src url of the images of the product
4. Details: The details of the product (separating each in JSON format)
5. Info: The "more info" of the product (separating each in JSON format)
6. Brand: The brand name

### Installing

    pip install gimbel

### Usage

    >>> from gimbel import gimbel_scraper
    >>> URL = "https://gimbelmexicana.com/gimbel/store/articulo/16680"
    >>> data = gimbel_scraper.get_product_info(URL)
    >>> print(data)

### Return
<code>
    {'Brand': 'GIM SPORTS', 'Code': 'Código: 15GIMNAS419CH', 'Name': 'BALON PARA CROSSFIT 2KG', 'Details': 'ÿþBalón medicinal para CROSSFIT\n\nCaracterísticas:\n" Fabricada de caucho resistente con relleno de arena.\n* Superficie con textura que evita derrape\n" No rebota\n" Perfecta para complementar los ejercicios de fuerza y resistencia en los músculos.\n" Entre los principales músculos trabajados encontramos glúteos/ cuádriceps/ isquiotibiales/ hombros y de forma secundaria/ abdominales\ny demás músculos de zona media del cuerpo que se contraen para conservar una correcta postura durante el movimiento.\n" Marca \x1c GIM\x1d', 'Info': '{"C\\u00f3digo":{"0":null,"1":"15GIMNAS419CH"},"Peso":{"0":null,"1":"2 kg"},"Color":{"0":null,"1":"Azul"}}', 'Image': ['https://gimbelmexicana.com/gimbel/img/products_images/thumb/15GIMNAS419CH_1.jpg', 'https://gimbelmexicana.com/gimbel/img/products_images/thumb/15GIMNAS419CH.jpg']}
</code>

</div>