let mesAtual = new Date().getMonth();
let anoAtual = new Date().getFullYear();
let semanaAtual = 1;

const nomesDosMeses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
const diasDaSemana = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"];

function alterarMes(direcao) {
    mesAtual += direcao;

    if (mesAtual < 0) {
        mesAtual = 11;
        anoAtual--;
    } else if (mesAtual > 11) {
        mesAtual = 0;
        anoAtual++;
    }

    semanaAtual = 1; // Reinicia para a primeira semana ao mudar de mês
    atualizarCalendario();
}

function alterarSemana(direcao) {
    semanaAtual += direcao;

    const semanasNoMes = Math.ceil((obterDiasDoMes(mesAtual, anoAtual) + obterPrimeiroDiaDaSemana(mesAtual, anoAtual)) / 7);

    if (semanaAtual < 1) {
        alterarMes(-1);
        const semanasMesAnterior = Math.ceil((obterDiasDoMes(mesAtual, anoAtual) + obterPrimeiroDiaDaSemana(mesAtual, anoAtual)) / 7);
        semanaAtual = semanasMesAnterior;
    } else if (semanaAtual > semanasNoMes) {
        alterarMes(1);
        semanaAtual = 1;
    }

    atualizarCalendario();
}

function obterDiasDoMes(mes, ano) {
    return new Date(ano, mes + 1, 0).getDate();
}

function obterPrimeiroDiaDaSemana(mes, ano) {
    const primeiroDiaDoMes = new Date(ano, mes, 1).getDay(); // Primeiro dia do mês
    return (primeiroDiaDoMes + 6) % 7; // Ajusta para segunda-feira como primeiro dia
}

function atualizarCalendario() {
    const elementoMes = document.getElementById("Mes");
    const elementoAno = document.getElementById("Ano");
    const elementoSemana = document.getElementById("SemanaNumero");
    const elementoCalendarioInferior = document.getElementById("CalendarioInferior");

    elementoMes.textContent = nomesDosMeses[mesAtual];
    elementoAno.textContent = anoAtual;
    elementoSemana.textContent = `Semana ${semanaAtual}`;

    elementoCalendarioInferior.innerHTML = "";

    const diasNoMes = obterDiasDoMes(mesAtual, anoAtual);
    const primeiroDiaDaSemana = obterPrimeiroDiaDaSemana(mesAtual, anoAtual);
    const inicioSemana = (semanaAtual - 1) * 7 - primeiroDiaDaSemana + 1;
    const fimSemana = inicioSemana + 6;

    diasDaSemana.forEach((dia, index) => {
        const diaNumero = inicioSemana + index;

        // Verifica se o dia está fora do mês atual
        if (diaNumero <= 0 || diaNumero > diasNoMes) {
            return; // Ignora a criação de colunas vazias
        }

        const diaDiv = document.createElement("div");
        diaDiv.classList.add("Dia");

        const diaTitulo = document.createElement("div");
        diaTitulo.classList.add("DiaTitulo");
        diaTitulo.textContent = `${dia} ${diaNumero}`;

        diaDiv.appendChild(diaTitulo);

        const eventosDiv = document.createElement("div");
        eventosDiv.classList.add("DiaEventos");
        diaDiv.appendChild(eventosDiv);

        // Adiciona destaque ao dia atual
        const hoje = new Date();
        if (
            anoAtual === hoje.getFullYear() &&
            mesAtual === hoje.getMonth() &&
            diaNumero === hoje.getDate()
        ) {
            diaDiv.classList.add("DiaAtual");
        }

        elementoCalendarioInferior.appendChild(diaDiv);
    });
}

// Inicializa o calendário e a hora ao carregar a página
document.addEventListener("DOMContentLoaded", () => {
    atualizarCalendario();
    HorarioAtualizado();
});

setInterval(HorarioAtualizado, 1000);

function HorarioAtualizado() {
    const elementoHora = document.getElementById("DataTexto");
    if (elementoHora) {
        const dataAtual = new Date();

        const diasDaSemanaTexto = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"];
        const mesesTexto = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

        const diaSemana = diasDaSemanaTexto[dataAtual.getDay()];
        const dia = String(dataAtual.getDate()).padStart(2, "0");
        const mes = mesesTexto[dataAtual.getMonth()];
        const ano = dataAtual.getFullYear();

        const horas = String(dataAtual.getHours()).padStart(2, "0");
        const minutos = String(dataAtual.getMinutes()).padStart(2, "0");
        const segundos = String(dataAtual.getSeconds()).padStart(2, "0");

        elementoHora.textContent = `Hoje é ${diaSemana}, ${dia} de ${mes} de ${ano}, ${horas}:${minutos}:${segundos}`;
    }
}
