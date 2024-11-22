
    
// DATA ------------------------------------------------------------------------------------------- >>>

function HorarioAtualizado() {
    const ElementoHora = document.getElementById("Data")
    if (ElementoHora) {
        var DataAtual = new Date()
    
        var Dia = String(DataAtual.getDate()).padStart(2, '0');
        var Mes = String(DataAtual.getMonth() + 1).padStart(2, '0'); // Janeiro é 0!
        var Ano = DataAtual.getFullYear();
        
        var Horas = String(DataAtual.getHours()).padStart(2, '0')
        var Minutos = String(DataAtual.getMinutes()).padStart(2, '0')
        var Segundos = String(DataAtual.getSeconds()).padStart(2, '0')
        
        var HorarioFormatado = `${Dia}/${Mes}/${Ano} ${Horas}:${Minutos}:${Segundos}`
        
        ElementoHora.textContent = HorarioFormatado
        }
    }    

setInterval(HorarioAtualizado, 1000)    

function AdicionarEvento() {
    let Evento = document.createElement('div')
    fetch('../HTML/Elementos/Evento.html')
        .then(resposta => resposta.text())
        .then(html => {Evento.innerHTML = html; Evento.classList.add("Evento")})
        .catch(error => { console.error('Erro erro', error); });
    
    const feed = document.getElementById('DiaEvtQuinta')    
    feed.appendChild(Evento)
    }



// Detalhes do evento ----------------------------------------------------------------------------- >>>    
let OPEN = 0

function AbrirDetalhesDoEvento(event) {
    if (OPEN == 0) {
        console.log("AQUIII")
        let evento = event.currentTarget
        let modalEvento = document.createElement("div")
    
        fetch('Modais/Modal_Evento.html')
            .then(response => response.text())
            .then(data => { 
                modalEvento.classList.add("ModalEvento")
                modalEvento.innerHTML = data 
                evento.appendChild(modalEvento)
                } )
            .catch(error => console.log("Não foi possivel carregar: ", error ) )    
        OPEN = 1    
        }
    else {
        let evento = event.currentTarget
        let modalEvento = document.getElementsByClassName("ModalEvento")[0]

        evento.removeChild( modalEvento )

        OPEN = 0
        }


    }

