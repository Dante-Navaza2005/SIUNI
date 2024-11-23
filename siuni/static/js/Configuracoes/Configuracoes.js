// VIZUALIZAÇÃO DE OPCOES =========================================================================================================================== >>>

const botao = document.getElementById('BlocoConfiguracoes');
const elemento = document.getElementById('OpcoesConfiguracoes');

const botaoMini = document.getElementById('IconConfiguracoesBarra')
const elementoMini = document.getElementById('OpcoesConfiguracoesB');


elemento.style.display = 'none';
elementoMini.style.display = 'none';


// Função para mostrar/ocultar o elemento
botao.addEventListener('click', (event) => {
    elemento.style.display = elemento.style.display === 'none' ? 'block' : 'none';
    event.stopPropagation(); 
    });


botaoMini.addEventListener('click', (event) => {
    elementoMini.style.display = elementoMini.style.display === 'none' ? 'block' : 'none';
    event.stopPropagation(); 
    });
    


// Impede o evento de clique do documento ao clicar no elemento
elemento.addEventListener('click', (event) => {
    event.stopPropagation();
    });


elementoMini.addEventListener('click', (event) => {
    event.stopPropagation();
    });


// Esconde o elemento ao clicar em qualquer lugar fora dele
document.addEventListener('click', (event) => {
    if (elemento.style.display === 'block' && !elemento.contains(event.target)) {
        elemento.style.display = 'none';
        }
    if (elementoMini.style.display === 'block' && !elementoMini.contains(event.target)) {
        elementoMini.style.display = 'none';
        }

    });


// OPÇÃO 1 ( Trocar tema ) =========================================================================================================================== >>>


// Função para aplicar o tema
function aplicaTema(tema) {
    const root = document.documentElement;
    if (tema === 'light') {
        root.classList.add('lightTheme');
        root.classList.remove('darkTheme');
    } else {
        root.classList.add('darkTheme');
        root.classList.remove('lightTheme');
    }
    // Salvar o tema no localStorage
    localStorage.setItem('temaAtual', tema);
}

// Função para alternar o tema
function alternaTema() {
    const temaAtual = localStorage.getItem('temaAtual') || 'dark';
    const novoTema = temaAtual === 'dark' ? 'light' : 'dark';
    aplicaTema(novoTema);
}

// Aplica o tema ao carregar a página
function temaSistemaOperacional() {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
        return 'light';
    } else {
        return 'dark';
    }
}

// Aplica o tema ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
    const temaSalvo = localStorage.getItem('temaAtual');
    const temaInicial = temaSalvo || temaSistemaOperacional(); // Usa o tema salvo ou o do sistema
    aplicaTema(temaInicial);
});