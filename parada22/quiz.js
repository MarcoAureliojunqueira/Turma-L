const prompt = require('prompt-sync')({sigint:true});

const jogador = prompt('Qual o seu nome? ');

let op = 10;
let pontuacao = 0;
let resposta;

while (op != 0) {
    op = parseInt(prompt("Qual tema você deseja jogar?  1 - Zoologia  2 - Astronomia  0 - Sair "));

    switch (op) {
        case 1:
            resposta = prompt("O maior animal que já vimos no planeta foi um dinossauro! Verdadeiro ou falso? ");
            if (resposta.toLowerCase() === "falso") {
                console.log("Parabéns!");
                pontuacao++;
            } else {
                console.log("Resposta incorreta. A baleia azul foi o maior animal que já viveu.");
            }
            resposta = prompt("As tartarugas podem viver mais de 100 anos. Verdadeiro ou falso? ");
            if (resposta.toLowerCase() === "verdadeiro") {
                console.log("Parabéns!");
                pontuacao++;
            } else {
                console.log("Resposta incorreta.");
            }
            resposta = prompt("As aranhas são insetos. Verdadeiro ou falso? ");
            if (resposta.toLowerCase() === "falso") {
                console.log("Parabéns!");
                pontuacao++;
            } else {
                console.log("Resposta incorreta. Elas são aracnídeos.");
            }
            break;

        case 2:
            resposta = prompt("O Sol é uma estrela de tamanho médio. Verdadeiro ou falso? ");
            if (resposta.toLowerCase() === "verdadeiro") {
                console.log("Parabéns!");
                pontuacao++;
            } else {
                console.log("Resposta incorreta.");
            }
            resposta = prompt("Júpiter é o maior planeta do nosso sistema solar. Verdadeiro ou falso? ");
            if (resposta.toLowerCase() === "verdadeiro") {
                console.log("Parabéns!");
                pontuacao++;
            } else {
                console.log("Resposta incorreta.");
            }
            resposta = prompt("A Terra é o terceiro planeta a partir do Sol. Verdadeiro ou falso? ");
            if (resposta.toLowerCase() === "verdadeiro") {
                console.log("Parabéns!");
                pontuacao++;
            } else {
                console.log("Resposta incorreta.");
            }
            break;

        case 0:
            console.log("Você saiu!");
            break;

        default:
            console.log("Digite uma opção válida.");
            break;
    }
}

console.log(`Obrigado por jogar, ${jogador}! Sua pontuação foi: ${pontuacao}`);


let numeros = prompt('digite seu numero para ser multiplicado');
let numero = parseInt(numeros);

for (let index = 0; index <=10; index++) {
    const result = numero * index;
    console.log(result);
   
}