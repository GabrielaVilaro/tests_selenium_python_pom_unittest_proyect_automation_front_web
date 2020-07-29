**Pruebas automatizadas usando: Python, Selenium, UnitTest, Page Object Model (POM) hecho en Pycharm.**

**Proyecto en curso, los casos de pruebas y capturas pueden no estar actualizados**

Primero escribí los casos de prueba, usando esta página de práctica: http://automationpractice.com/

Después realicé la auomatización de los casos de prueba usando las herramientas mencionadas anteriormente.

**Casos de prueba:**

Los casos de prueba se pueden ver escritos acá. 

https://docs.google.com/spreadsheets/d/1xJxVy7hZBSpHSzhdFZTcU998BdypeW7BxLj3vNbyV9Q/edit?usp=sharing

**Requisitos**

    Python >= 3.5
    Instalar las dependencias del proyecto: pip3 install -r requirements.txt
    Pycharm
  
El proyecto incluye reporte en HTLM que se puede ver al finalizar la ejecución.

Correr todos los tests juntos:

     python -m unittest discover   

Ejemplo de reporte del archivo tests_index_page.py


<a href="https://ibb.co/BBhK0D4"><img src="https://i.ibb.co/ZxQ1qsH/Screen-Shot-2020-07-18-at-14-14-43.png" alt="Screen-Shot-2020-07-18-at-14-14-43" border="0"></a>

**La documentación completa del proyecto se puede ver abriendo el archivo /docs/tests/index.html en un navegador, haciendo click izquierdo y en "Open Browser" elejir su navegador de preferencia**

Para generar la documentación usé pdocs3 (está dentro de requirements.txt)  pdoc --html tests

<a href="https://ibb.co/jkZcFQc"><img src="https://i.ibb.co/1GJDxPD/Screen-Shot-2020-07-18-at-15-00-55.png" alt="Screen-Shot-2020-07-18-at-15-00-55" border="0"></a>