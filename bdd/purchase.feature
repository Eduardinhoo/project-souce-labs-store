Feature: Purchase Product

Scenario: Successful purchase

Given  user is logged in
When   user adds product to cart
And    completes checkout
Then   purchase should be successful

----

Funcionalidade: Comprar do Produto

Cenário: Compra bem-sucedida

Dado:    que o usuário está logado
Quando:  o usuário adiciona um produto ao carrinho
E:       finaliza a compra
Então:   a compra deve ser bem-sucedida:
