let invoiceList = []; let duplicates = [];

const invoiceTableGlobal = document.getElementById("ctl00_Contentplaceholder1_ctrlHistorico_gridAceptados");
const invoiceTable = invoiceTableGlobal.children[0]; //Lista de elementos
const tableLen = invoiceTable.children.length; //Longitud Tabla

function downloadFile(){
    const blob = new Blob([...invoiceList], {type:"octet-stream"});
    const href = URL.createObjectURL(blob);
    const boton = Object.assign(document.createElement("a"), {href, download:"invoiceList.txt"});

    const div = document.getElementsByClassName("limitePantalla")[4]; //Div de los botones
    const prntBtn = document.getElementById("ctl00_Contentplaceholder1_ctrlHistorico_gridAceptados_ctl01_imbImprimirSeleccionAceptados");

    //Estilos del boton
    boton.textContent = "Descargar Todo";
    boton.style.textDecoration = "none";
    boton.style.color = "white";
    boton.style.background = "url(https://nbem.banorte.com/NBXI/App_Themes/images/bg_btnenvia.jpg) repeat-x";
    boton.style.border = "solid 1px #CCC";
    boton.style.font = "bold 10px/13px Verdana,Arial,Helvetica,sans-serif";
    boton.style.height = "20px";
    boton.style.marginLeft = "6px";
    boton.style.padding = "2px 6px 4px";

    div.children[2].after(boton);

    boton.addEventListener("click", () =>{
        prntBtn.click();
    });
}

function verifyDuplicity(semiresult){
    let result = semiresult + "\n";

    if (invoiceList.includes(result) || duplicates.includes(result)){
        const index = invoiceList.indexOf(result);
        
        duplicates.push(result);

        if (invoiceList[index] == result){ invoiceList[index] = semiresult + " (" + 0 + ")\n"; }

        invoiceList.push(semiresult + " (" + duplicates.filter((e) => e == result).length + ")\n");

    } else { invoiceList.push(result); }
}

if (invoiceTableGlobal != undefined){

    if (document.URL.indexOf("CuentasPropias.aspx") >= 0){
        for (let i = 1; i < tableLen; i++){

            let invoice = invoiceTable.children[i];
            
            const name = invoice.children[14].textContent; //Nombre del archivo - CUENTAS PROPIAS
            const amount = invoice.children[10].textContent; //Importe a Transferir - CUENTAS PROPIAS
            const date = (invoice.children[12].textContent).replace(/\./g, ''); //Fecha de la factura - CUENTAS PROPIAS
            const semiresult = (name + " " + amount + " (" +  date + ")").replace(/\//g, '-'); //Nombre final del PDF
            
            verifyDuplicity(semiresult);
        } downloadFile();
    }
    
    if (document.URL.indexOf("SPEI.aspx") >= 0 || document.URL.indexOf("CuentasTercero.aspx") >= 0){
        for (let i = 1; i < tableLen; i++){

            let invoice = invoiceTable.children[i]; 
    
            const name = invoice.children[8].textContent; //Nombre del archivo - Terceros Banorte / Ixe
            const amount = invoice.children[12].textContent; //Importe a Transferir - Terceros Banorte / Ixe
            const date = (invoice.children[14].textContent).replace(/\./g, ''); //Fecha de la factura - Terceros Banorte / Ixe
            const semiresult = (name + " " + amount + " (" +  date + ")").replace(/\//g, '-'); //Nombre final del PDF
    
            verifyDuplicity(semiresult);
        } downloadFile();
    }
}