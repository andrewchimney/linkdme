function edit(i){
    document.getElementsByClassName(`link_normal ${i}`)[0].style.display="none"
    document.getElementsByClassName(`link_edit ${i}`)[0].style.display="initial"
}
function add(){
    document.getElementsByClassName('add_normal')[0].style.display="none"
    document.getElementsByClassName('add_link')[0].style.display="initial"
}
function del(i){
    link = document.getElementsByClassName(`span ${i}`)[0].innerHTML
    const requestOptions = {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ del_link: link})
    };
    fetch(`http://${ip}/profile`, requestOptions)
    document.getElementsByClassName(`link ${i}`)[0].remove()
}

function put(i){
    inputs = document.getElementsByClassName(`input ${i}`)
    const requestOptions = {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ o_link: inputs[0].value, n_link: inputs[1].value})
        
    };
    fetch(`http://${ip}/profile`, requestOptions)
    document.getElementsByClassName(`span ${i}`)[0].innerHTML=inputs[1].value
    document.getElementsByClassName(`link_normal ${i}`)[0].style.display="initial"
    document.getElementsByClassName(`link_edit ${i}`)[0].style.display="none"
    
}

async function post(){
    inputs = document.getElementsByName(`add_link`)
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ add_link: inputs[0].value})
    };
    console.log(requestOptions)
    response = await fetch(`http://${ip}/profile`, requestOptions)
    location.reload(true)
}