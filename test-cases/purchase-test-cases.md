TC01 – Login com usuário válido
Tipo: Positivo

Passos:
1 acessar página saucedemo
2 inserir usuário
3 inserir senha
4 clicar login

Resultado esperado:
Usuário acessa página de produtos

---

TC02 – Adicionar produto ao carrinho
Tipo: Positivo

Passos:
1 acessar pagina saucedemo
1 acessar produtos
2 selecionar produtos
3 clicar add to carrinho

Resultado esperado:
Produto aparece no carrinho

---

TC03 – Finalizar checkout com produtos no carrinho 
Tipo: Positivo

Passos:
1 acessar pagina da soucedemo
2 selecionar produto
3 acessar carrinho 
4 clicar em checkout
5 preecher os dados obrigatorios
6 clicar continuar
7 clicar em finish

Resultado esperado:
Compra concluída

---

TC04 – Finalizar checkout sem produto no carrinho vazio
Tipo: Negativo

Passos:
1 acessar pagina da soucedemo
2 acessar carrinho 
3 clicar em checkout
4 preecher os dados obrigatorios
5 deixar carrinho vazio
6 clicar continuar
7 clicar em finish

Resultado esperado:
Sistema deve exibir erro

Resultado real:
Sitema passa conclui pedido.

---

TC05 – Checkout sem dados obrigatórios
Tipo: Negativo

Passos:
1 acessar pagina da soucedemo
2 acessar carrinho 
3 acessar checkout
4 não preencher dados
5 clicar continuar
6 clicar em finish

Resultado esperado:
Sistema deve exibir erro

---

