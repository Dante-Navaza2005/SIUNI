
var SIUNI = document.getElementById("SIUNI")

function abrirModal(event, modalName) {
    if (isOpenModal == 0) {
        let Modal = document.createElement('div');
        Modal.id = 'Modal';

        // Carrega o modal base (Modal.html)
        fetch(`/modal/Modal/`)
            .then(resposta => resposta.text())
            .then(respostaTexto => {
                Modal.innerHTML = respostaTexto; // Insere o conteúdo do modal base
                const modalConteudo = Modal.querySelector('#ModalConteudo'); // Seleciona o "ModalConteudo"

                if (modalConteudo) {
                    // Carrega o conteúdo dinâmico (conteudoSobreSiuni.html) para o "ModalConteudo"
                    fetch(`/modal/${modalName}/`)
                        .then(resposta => resposta.text())
                        .then(html => {
                            modalConteudo.innerHTML = html; // Insere o conteúdo carregado no ModalConteudo
                            SIUNI.appendChild(Modal); // Adiciona o modal ao DOM somente após tudo estar pronto
                            isOpenModal = 1; // Marca o modal como aberto
                        })
                        .catch(error => console.log("Erro ao carregar conteúdo do modal:", error));
                } else {
                    console.error("Elemento #ModalConteudo não encontrado no modal base.");
                }
            })
            .catch(error => console.log("Erro ao carregar o modal base:", error));
    }
}


    function carregarConteudoModal(modalName) {
        fetch(`/modal/${modalName}/`)
            .then(resposta => {
                if (!resposta.ok) {
                    throw new Error(`Erro ao carregar modal: ${resposta.status}`);
                }
                return resposta.text(); // Retorna o HTML completo
            })
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const modalConteudo = doc.querySelector('#ModalConteudo'); // Obtém apenas o conteúdo necessário
    
                const modalDiv = document.getElementById('ModalConteudo');
                if (modalConteudo && modalDiv) {
                    modalDiv.innerHTML = modalConteudo.innerHTML; // Insere o conteúdo no modal
                } 
            })
            .catch(error => console.error("Erro ao carregar conteúdo do modal:", error));
    }
    




window.addEventListener('click', (event) => {
    if (isOpenModal == 1) {
        var Modal = document.getElementById('Modal')
        if (event.target == Modal ) { fecharModal(event) }

        }
    })

function fecharModal(event)  {

    var Modal = document.getElementById('Modal')
    SIUNI.removeChild(Modal) 
    isOpenModal = 0
    
    }

 