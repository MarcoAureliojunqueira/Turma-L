import prompt from 'prompt-sync';
const myPrompt = prompt({ sigint: true });
 function play () {
 let jogador =  myPrompt('Qual o seu nome? ');
 
let idade =  myPrompt('Qual e a sua idade? ');
  return [`nome: ${jogador}, idade:${idade}`]
}

export {play};