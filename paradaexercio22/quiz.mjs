import { play } from  './digiteJogador.mjs';
import prompt from 'prompt-sync';
const myPrompt = prompt({ sigint: true });

const jogador = play() ;

let op = 10;
let pontuacao = 0;
let resposta;

function jogaZoologia() {
    resposta = myPrompt ("O maior animal que já vimos no planeta foi um dinossauro! Verdadeiro ou falso? ");
            if (resposta.toLowerCase() === "falso") {
                console.log("Parabéns!");
                pontuacao++;
            } else {
                console.log("Resposta incorreta. A baleia azul foi o maior animal que já viveu.");
            }
            resposta = myPrompt ("As tartarugas podem viver mais de 100 anos. Verdadeiro ou falso? ");
            if (resposta.toLowerCase() === "verdadeiro") {
                console.log("Parabéns!");
                pontuacao++;
            } else {
                console.log("Resposta incorreta.");
            }
            resposta = myPrompt ("As aranhas são insetos. Verdadeiro ou falso? ");
            if (resposta.toLowerCase() === "falso") {
                console.log("Parabéns!");
                pontuacao++;
            } else {
                console.log("Resposta incorreta. Elas são aracnídeos.");
            }
           
}
function jogaAstronomia() {
    resposta = myPrompt ("O Sol é uma estrela de tamanho médio. Verdadeiro ou falso? ");
            if (resposta.toLowerCase() === "verdadeiro") {
                console.log("Parabéns!");
                pontuacao++;
            } else {
                console.log("Resposta incorreta.");
            }
            resposta = myPrompt ("Júpiter é o maior planeta do nosso sistema solar. Verdadeiro ou falso? ");
            if (resposta.toLowerCase() === "verdadeiro") {
                console.log("Parabéns!");
                pontuacao++;
            } else {
                console.log("Resposta incorreta.");
            }
            resposta = myPrompt ("A Terra é o terceiro planeta a partir do Sol. Verdadeiro ou falso? ");
            if (resposta.toLowerCase() === "verdadeiro") {
                console.log("Parabéns!");
                pontuacao++;
            } else {
                console.log("Resposta incorreta.");
            }
  }
  function jogaPlantas() {
        resposta = myPrompt ("As plantas produzem oxigênio durante a fotossíntese. Verdadeiro ou falso?   ");
                if (resposta.toLowerCase() === "verdadeiro") {
                    console.log("Parabéns!");
                    pontuacao++;
                } else {
                    console.log("Resposta incorreta.");
                }
                resposta = myPrompt ("Os cactos são encontrados apenas nos desertos. Verdadeiro ou falso?   ");
                if (resposta.toLowerCase() === "falso") {
                    console.log("Parabéns!");
                    pontuacao++;
                } else {
                    console.log("Resposta incorreta.");
                }
                resposta = myPrompt ("As plantas precisam de luz para crescer. Verdadeiro ou falso? ");
                if (resposta.toLowerCase() === "verdadeiro") {
                    console.log("Parabéns!");
                    pontuacao++;
                } else {
                    console.log("Resposta incorreta.");
                }
      
  }
function tabuadaMultiplicação() {
    let pergunta = myPrompt('Gostaria de saber um numero da tabuada? sim ou nao  ');

    if(pergunta.toLowerCase() == 'sim'){
    let numeros = myPrompt('digite seu numero para ser multiplicado  ');
    let numero = parseInt(numeros);

for (let index = 0; index <= 10; index++) {
    const result = numero * index;
   console.log(result);
} 
    } else pergunta.toLowerCase() == 'nao'; {
    return console.log('tenha um boa tarde');
     
    }
   
    
}


while (op != 0) {
   op = parseInt( myPrompt ("Qual tema você deseja jogar?  1 - Zoologia   2 - Astronomia   3 - Tabuada  4 - Plantas 0 - Sair "));
   console.log(op);

    switch (op) {
    
        case 1:
            jogaZoologia()
        break
        case 2:
            
           jogaAstronomia()
           break
        case 3:
            
        tabuadaMultiplicação()
        break

        case 4:
            
       jogaPlantas()
        break
        case 0:
            console.log("Você saiu!");
            break;

        default:
            console.log("Digite uma opção válida.");
            break;
    }
    console.log(`Obrigado por jogar, ${jogador}! Sua pontuação foi: ${pontuacao}`);
}



