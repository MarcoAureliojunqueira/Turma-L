programa
{
	funcao inicio()
	{
		inteiro a, b, soma, sub, mult, div
		caracter  opcao
		escreva("Digite o primeiro n�mero: ")
		leia(a)
    escreva("Digite a opera��o: ")
    leia(opcao)
		escreva("Digite o segundo n�mero: ")
		leia(b)

		soma = a + b // Soma os dois valores
		sub  = a - b // Subtrai os dois valores
		mult = a * b // Multiplica os dois valores
		div  = a / b // Divide os dois valores
    opcao == '+'
    opcao == '-'
escolha (opcao)	
		{
			caso '+': 
		 		escreva ("\nA soma dos n�meros � igual a: ", soma)

		 		pare   // Impede que as instru��es do caso 2 sejam executadas
		 	caso '-': 
		 		escreva ("\nA subtra��o dos n�meros � igual a: ", sub)
		 		pare   // Impede que as instru��es do caso 2 sejam executadas
		 	caso '*': 
		 		escreva ("\nA multiplica��o dos n�meros � igual a: ", mult)
		 		pare
        	caso '/': 
		 		escreva ("\nA divis�o dos n�meros � igual a: ", div, "\n")
		 		pare
		 	caso contrario: // Ser� executado para qualquer op��o diferente de 1, 2 ou 3
		 		escreva ("Op��o Inv�lida !")
		}
		//escreva("\nA soma dos n�meros � igual a: ", soma) 		// Exibe o resultado da soma
		//escreva("\nA subtra��o dos n�meros � igual a: ", sub) 		// Exibe o resultado da subtra��o
		//escreva("\nA multiplica��o dos n�meros � igual a: ", mult) 	// Exibe o resultado da multiplica��o
		//escreva("\nA divis�o dos n�meros � igual a: ", div, "\n") 	// Exibe o resultado da divis�o
	}
}