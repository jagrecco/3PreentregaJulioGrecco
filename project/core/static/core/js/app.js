
function cambia_lista_card(){

    const txt_boton=document.getElementById("lista_card")

    const card_container=document.getElementById("contenedor_card_libros")
    const lista_container=document.getElementById("contenedor_lista_libros")

    if (txt_boton.value=='card'){

        txt_boton.value='lista'
        txt_boton.textContent='Cambiar a Cards'
        card_container.className="contenedor_invisible"
        lista_container.className="contenedor_lista_libros"
    } 
    else 
    {

        txt_boton.value='card'
        txt_boton.textContent='Cambiar a Lista'
        card_container.className="contenedor_card_libros"
        lista_container.className="contenedor_invisible"
    }


}