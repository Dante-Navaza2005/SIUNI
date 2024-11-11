
function AbrirSobreSiuni(page, event) {
    fetch(page)
        .then(Response => Response.text())
        .then(html => { 
            let modal = document.createElement('div')
            modal.classList.add("MODAL")
            modal.id = "ModalSobreSiuni"
            modal.innerHTML = html
            document.getElementById("SIUNI").appendChild(modal)
            } )
        .catch(error => console.log("Não foi possivel carregar: ", error ) )
    }

window.addEventListener("click", (event) => {
    if (event.target = document.getElementById('ModalSobreSiuni')) { fecharModal('ModalSobreSiuni', event) }
    })


function fecharModal(modal, event)  {
    var SIUNI = document.getElementById("SIUNI")
    var Modal = document.getElementById(`${modal}`)
    SIUNI.removeChild(Modal)
    }

 