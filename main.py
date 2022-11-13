import xml.etree.ElementTree as ET
from files import ler_arquivo as ler
from files import criar_planilha
from files import salvar_xlsx as salvar

tree = ET.parse('mini_RM2699.xml')
root = tree.getroot()

linha = 2
processos = ler("processos.txt")

criar_planilha()  

salvar(("Data da RPI " + root.get('data')), 'A', 1)
salvar("Número do Processo", 'A', 2)
salvar("Titular", 'B', 2)
salvar("Código do Despacho", 'C', 2)
salvar("Nome do Despacho.", 'D', 2)

for processo in processos:
    linha += 1    
    salvar(processo, 'A', linha)    

    for node in root.findall(".//processo[@numero='" + processo + "']/titulares/titular"):        
        salvar(node.attrib['nome-razao-social'], 'B', linha)
        break
    
    for node in root.findall(".//processo[@numero='" + processo + "']/despachos/despacho"):        
        salvar(node.attrib['codigo'], 'C', linha)        
        salvar(node.attrib['nome'], 'D', linha)
        break

print("Pronto, veja o resultado no arquivo: processos.xlsx")
