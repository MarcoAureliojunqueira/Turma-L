programa
{
	funcao inicio()
	{
		inteiro a, b, soma, sub, mult, div
		caracter  opcao
		escreva("Digite o primeiro número: ")
		leia(a)
    escreva("Digite a operação: ")
    leia(opcao)
		escreva("Digite o segundo número: ")
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
		 		escreva ("\nA soma dos números é igual a: ", soma)

		 		pare   // Impede que as instruções do caso 2 sejam executadas
		 	caso '-': 
		 		escreva ("\nA subtração dos números é igual a: ", sub)
		 		pare   // Impede que as instruções do caso 2 sejam executadas
		 	caso '*': 
		 		escreva ("\nA multiplicação dos números é igual a: ", mult)
		 		pare
        	caso '/': 
		 		escreva ("\nA divisão dos números é igual a: ", div, "\n")
		 		pare
		 	caso contrario: // Será executado para qualquer opção diferente de 1, 2 ou 3
		 		escreva ("Opção Inválida !")
		}
		//escreva("\nA soma dos números é igual a: ", soma) 		// Exibe o resultado da soma
		//escreva("\nA subtração dos números é igual a: ", sub) 		// Exibe o resultado da subtração
		//escreva("\nA multiplicação dos números é igual a: ", mult) 	// Exibe o resultado da multiplicação
		//escreva("\nA divisão dos números é igual a: ", div, "\n") 	// Exibe o resultado da divisão
	}
}