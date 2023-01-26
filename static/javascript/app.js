const pop_menu = document.querySelector("#popup")
const Post_id = document.getElementById('post_id')
const wrapper = document.querySelector('#wrapper')
const delete_btn = document.querySelectorAll('.delete_btn')
const like = document.querySelector('.likes')

const menu = () => {
    if (pop_menu.id == "popup") {
        pop_menu.className = "flex z-20 shadow-black-500/50 bg-white gap-3 flex-col w-60 px-4 py-4 absolute top-12 shadow-2xl"
        pop_menu.id = "popoff"
    } else {
        pop_menu.className = "hidden z-20 shadow-black-500/50 bg-white gap-3 flex-col w-60 px-4 py-4 absolute top-12 shadow-2xl"
        pop_menu.id = "popup"
    }
}


delete_btn.forEach((btn) => {
    console.log(btn)
    btn.addEventListener("click", (e) => {
        e.preventDefault()
        const post = document.querySelector('.post_id')
        console.log(post)
        fetch('http://127.0.0.1:8000/delete/', {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                id: post.id,
            })

        }).then(response => {
            response.json().then(data => {
                wrapper.removeChild(document.querySelector('#remove_post'))

            }).catch(err => {
                alert(err);
            })
        }
        )

    })
})


like.addEventListener('click', (e) => {
    e.preventDefault()
    const get_id = document.querySelector('.post_like').id
    fetch('http://127.0.0.1:8000/likes/', {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            id: get_id,
        })
    }).then(response => {
        response.json().then(data => {
            const like_tag = document.querySelector('#like_count')
            like_tag.textContent = `${data.total_like} likes`
        }).catch(err => {
            window.location.href="http://127.0.0.1:8000/login/"
        })
    }
    )
})


