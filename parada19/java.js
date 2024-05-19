
let primeiroDigito = 5;
let segundoDigito= 2;


 if( primeiroDigito >  segundoDigito ) {
 console.log('o numero maior e',primeiroDigito);
} else {
   console.log('o numero2 maior e', segundoDigito);
 }


 if( primeiroDigito % 2 != 0) {
  console.log('o numero impar');
} else {
  console.log('o numero par');
 }


 let digiteseuVoto = prompt('Digite seu voto 1,2,3,4 ou nulo/branco');
 let valor = digiteseuVoto;
 
 switch (valor) {
    case "1":
     console.log('Você votou no candidato 1');
     break;
    case "2":
     console.log('Você votou no candidato 2');
     break;
    case "3":
     console.log('Você votou no candidato 3');
     break;
    case "4":
      console.log('Você votou no candidato 4');
      break;

    default: ''
     console.log('Você digitou nulo');
     break;
 }