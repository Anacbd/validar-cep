import xml.etree.ElementTree as ET
from jinja2 import Template

# Ler XML do pytest
tree = ET.parse('resultado_testes.xml')
root = tree.getroot()

testes = []

for testcase in root.iter('testcase'):
    nome_tecnico = testcase.get('name')

    nome_amigavel = nome_tecnico.replace('test_', '').replace('_', ' ').title()

    status = "APROVADO" if len(list(testcase)) == 0 else "REPROVADO"

    testes.append({
        "item": nome_amigavel,
        "status": status
    })

# Template HTML
html_template = """
<html>
<body>

<h1>Termo de Aceite Técnico - Projeto CEP</h1>
<p>O seguinte relatório formaliza a validação das funcionalidades:</p>

<ul>
{% for t in testes %}
<li>{{ t.item }}: <b>{{ t.status }}</b></li>
{% endfor %}
</ul>

<br><br>
__________________________________________<br>
Assinatura do Usuário (Stakeholder)

</body>
</html>
"""

template = Template(html_template)

with open("termo_de_aceite.html", "w") as f:
    f.write(template.render(testes=testes))