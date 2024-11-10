// VIZUALIZAÇÃO DE OPCOES =========================================================================================================================== >>>

const botao = document.getElementById('BlocoConfiguracoes');
const elemento = document.getElementById('OpcoesConfiguracoes');
elemento.style.display = 'none';

// Função para mostrar/ocultar o elemento
botao.addEventListener('click', (event) => {
    elemento.style.display = elemento.style.display === 'none' ? 'block' : 'none';
    event.stopPropagation(); 
    });

// Impede o evento de clique do documento ao clicar no elemento
elemento.addEventListener('click', (event) => {
    event.stopPropagation();
    });

// Esconde o elemento ao clicar em qualquer lugar fora dele
document.addEventListener('click', (event) => {
    if (elemento.style.display === 'block' && !elemento.contains(event.target) && event.target !== botao) {
        elemento.style.display = 'none';
    }
    });


// OPÇÃO 1 ( Trocar tema ) =========================================================================================================================== >>>


const BotaoTrocaTema = document.getElementById('OP-TEMA-COR');
const IconTema = document.getElementById('IconOptionTheme');

BotaoTrocaTema.addEventListener('click', () => { 
    document.body.classList.toggle('lightTheme'); 
    });







