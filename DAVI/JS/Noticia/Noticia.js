


function abrirNoticia(page, event) {

    fetch(page)
        .then(Response => Response.text())
        .then(html => { 
            let modal = document.createElement('div')
            modal.classList.add("MODAL")
            modal.id = "ModalNoticia"
            modal.innerHTML = html
            document.getElementById("SIUNI").appendChild(modal)
            } )
        .catch(error => console.log("Não foi possivel carregar: ", error ) )

    }


window.addEventListener("click", (event) => {
    if (event.target = document.getElementById('ModalNoticia')) { fecharModal('ModalNoticia', event) }
    })
    












