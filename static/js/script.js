// Seletores
const form = document.querySelector("#cadastroForm");
const mensagem = document.querySelector("#mensagem");

// Função para enviar dados ao Flask
async function enviarFormulario(event) {
    event.preventDefault();

    const usuario = document.querySelector("#usuario").value;
    const nota = document.querySelector("#nota").value;
    const titulo = document.querySelector("#titulo").value;
    const email = document.querySelector("#email").value;
    const senha = document.querySelector("#senha").value;

    const response = await fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ usuario, nota, senha, nota, titulo, email })
    });

    if (response.ok) {
        mensagem.textContent = "Cadastro enviado com sucesso!";
        mensagem.style.color = "green";
        form.reset();
    } else {
        mensagem.textContent = "Erro ao enviar. Tente novamente!";
        mensagem.style.color = "red";
    }
}

// Evento
form.addEventListener("submit", enviarFormulario);
