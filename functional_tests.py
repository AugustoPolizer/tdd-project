from selenium import webdriver

browser = webdriver.Firefox()

# Maria decidiu utilizar o novo app TODO. Ela entra em sua página principal:
browser.get('http://localhost:8000')

# Ela nota que o título da página menciona TODO
assert 'To-Do' in browser.title

# Ela é convidada a entrar com um item TODO imediatamente

# Ela digita "Estudar testes funcionais" em uma caixa de texto

# Quando ela aperta enter, a página atualiza, e mostra a lista
# "1: Estudar testes funcionais" como um item da lista TODO

# Ainda existe uma caixa de texto convidando para adicionar outro item
# Ela digita: "Estudar testes de unidade"

# A página atualiza novamente, e agora mostra ambos os itens na sua lista

# Maria se pergunta se o site vai lembrar da sua lista. Então, ela verifica que
# o site gerou uma URL única para ela -- existe uma explicação sobre essa feature

# Ela visita a URL: a sua lista TODO ainda está armazenada

# Satisfeita, ela vai dormir

browser.quit()
