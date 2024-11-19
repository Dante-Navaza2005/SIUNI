
var SIUNI = document.getElementById("SIUNI")

function abrirModal(event) {
    if (isOpenModal == 0) {
        let Modal = document.createElement('div')
        Modal.id = 'Modal'

        fetch('Modais/Modal.html')
            .then(resposta => resposta.text())
            .then(respostaTexto => { Modal.innerHTML = respostaTexto })
            .catch(error => console.log("Não foi possivel carregar: ", error ) )

        SIUNI.appendChild(Modal)
        isOpenModal = 1
        }
    }


function carregarConteudoModal(conteudo) {
    if (isOpenModal == 1) {
        foundAndExecute('ModalConteudo', ()=> {
            fetch(conteudo)
                .then(resposta => resposta.text())
                .then(respostaTexto => {   
                    var cntmdl = document.getElementById('ModalConteudo')
                    cntmdl.innerHTML = respostaTexto })
                .catch(error => console.log("Não foi possivel carregar: ", error ) )
            })

        }
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

 