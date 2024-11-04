
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
    fetch('../HTML/Evento.html')
        .then(resposta => resposta.text())
        .then(html => {Evento.innerHTML = html; Evento.classList.add("Evento")})
        .catch(error => { console.error('Erro erro', error); });
    
    const feed = document.getElementById('DiaEvtQuinta')
    feed.appendChild(Evento)
    }




