const pop_menu = document.querySelector("#popup")
const dialog_pop = document.querySelector("#dialog")

const myclick = () => {
    if (pop_menu.id == "popup") {
        pop_menu.className = "flex z-20 shadow-black-500/50 bg-white gap-3 flex-col w-60 px-4 py-4 absolute top-12 shadow-2xl"
        pop_menu.id = "popoff"
    } else {
        pop_menu.className = "hidden z-20 shadow-black-500/50 bg-white gap-3 flex-col w-60 px-4 py-4 absolute top-12 shadow-2xl"
        pop_menu.id = "popup"
    }
}
const getFetch = () => {
    const url = "http://127.0.0.1:8000/test/"
    fetch(url, {
        '  method': 'POST',
        '   credentials': 'same-origin',

        ' header': 'application/json',
        'x-Requested-With': 'XMLHttpRequest',
        // 'X-CSRFToken': getCookie('csrftoken')

        body: JSON.stringify({ "post_data": "data to post" })

    }).then(response => {
        return response.json()
    }).then(data => [
        console.log(data)
    ]).catch(error => {
        console.log(error)
    })

}

const pop = () => {
    dialog_pop.className = "absolute top-0 w-full h-screen flex flex-col  justify-center"
}

// "{% url 'deletePost' post.id %} "