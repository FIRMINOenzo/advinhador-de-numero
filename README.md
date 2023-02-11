# advinhador-de-numero
Adivinhe o número aleatório!!

Este código foi feito para treinar conceitos básicos da linguagem Python

Neste código, podemos escolher entre tentarmos advinhar o número nós mesmo e também deixar a máquina tentar advinhar o número.

# Jogador tentando advinhar
Quando o jogador tenta advinhar o número, é pedido a ele a definição do número máximo que pode ser gerado aleatoriamente, usando o método randint(0, numLimite).

Quando ele da seu palpite, podemos ter três caminhos:
 * A tentativa está correta e ele ganha;
 * A tentativa é muito baixa, então o programa o diz para tentar um número maior;
 * A tentativa é muito alta, então o programa o diz para tentar um número menor.

No final, quando esse jogador acerta, a quantidade de tentativas dele é exibida na tela.

# Máquina tentando advinhar
Quando o jogador decide ver a máquina advinhando o número aleatório, novamente é pedido a definição do número limite que pode ser gerado aleatóriamente.

A maneira que a máquina gera números aleatórios é bem similar ao processo de gerar o número que deve ser advinhado, utilizando o método randint(numMin, numMax).

Novamente, quando a máquina tenta um número, podemos ter três caminhos:
 * A tentativa está correta e ela ganha;
 * A tentativa é muito baixa, então o programa define o numMin como a tentativa +1;
 * A tentativa é muito alta, então o programa define o numMin como a tentativa -1;

Sendo assim, a máquina nunca tenta o mesmo número mais de uma vez

No final, quando a máquina acerta, o total de tentativas que ela levou é exibido na tela para o usuário.
