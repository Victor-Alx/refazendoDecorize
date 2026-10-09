/* =====================================
   ELEMENTOS DOS MODAIS
===================================== */

const overlay = document.getElementById("overlay");

const modalLogin = document.getElementById("modalLogin");

const modalAnexo = document.getElementById("modalAnexo");


/* =====================================
   ABRIR MODAL DE LOGIN
===================================== */

function abrirModalLogin() {

    overlay.classList.add("ativo");

    modalLogin.classList.add("ativo");
}


/* =====================================
   ABRIR MODAL DE ANEXO
===================================== */

function abrirModalAnexo() {

    overlay.classList.add("ativo");

    modalAnexo.classList.add("ativo");
}


/* =====================================
   FECHAR TODOS OS MODAIS
===================================== */

function fecharModais() {

    overlay.classList.remove("ativo");

    modalLogin.classList.remove("ativo");

    modalAnexo.classList.remove("ativo");
}


/* =====================================
   CLICAR FORA DO MODAL
===================================== */

overlay.addEventListener("click", function (event) {
    event.stopPropagation();
});


/* =====================================
   LOGIN
===================================== */

function irParaLogin() {

    /*
        Depois você pode colocar aqui:

        window.location.href = "login.html";
    */

    console.log("Ir para página de login");

}


/* =====================================
   REGISTRO
===================================== */

function irParaRegistro() {

    /*
        Depois você pode colocar aqui:

        window.location.href = "registro.html";
    */

    console.log("Ir para página de registro");

}


/* =====================================
   CONFIRMAR PROJETO
===================================== */

function confirmarProjeto() {

    const imagens = document.getElementById("imagens");

    const largura = document.getElementById("largura").value;

    const comprimento = document.getElementById("comprimento").value;


    /*
        Verifica se o usuário colocou
        as medidas.
    */

    if (largura === "" || comprimento === "") {

        alert("Informe a largura e o comprimento do quarto.");

        return;
    }


    /*
        Aqui futuramente você pode mandar
        os dados para o PHP/Laravel.
    */

    console.log("Largura:", largura);

    console.log("Comprimento:", comprimento);

    console.log("Imagens:", imagens.files);


    alert("Projeto confirmado!");

}

/*
Hábilitar ou não o erro login


window.onload = function () {
    abrirModalLogin();
}; 
*/