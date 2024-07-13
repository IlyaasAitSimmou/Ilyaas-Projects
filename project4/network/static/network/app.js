function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function PostHandler() {
    postSets = document.querySelectorAll('.postSet')
    console.log(postSets)
    console.log(postSets[0])
    console.log(postSets[1])

    let currentSet = 0
    postSets[currentSet].style.display = 'block'
    document.querySelector('#next_page').addEventListener('click', () => {
        if (currentSet + 2 <= postSets.length) {
            postSets[currentSet].style.display = 'none';
            currentSet += 1;
            postSets[currentSet].style.display = 'block';
        }
    })
    document.querySelector('#previous_page').addEventListener('click', () => {
        if (currentSet - 1 >= 0) {
            postSets[currentSet].style.display = 'none';
            currentSet -= 1;
            postSets[currentSet].style.display = 'block';
        }
    })

    

}

document.addEventListener('DOMContentLoaded', () => {
    button = document.querySelectorAll('.like_button')
    button.forEach(like_button => {
        like_button.addEventListener('click', () => {
            console.log(like_button)
            console.log(like_button.parentElement)
            fetch(`/addlike/${like_button.parentElement.id}`, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            })
            .then(response => {
                newRes = response.json()
                return (newRes)
            })
            .then(result => {
                console.log(result)
                console.log(String(result.message))
                console.log(parseInt(String(like_button.innerHTML).replace("❤️", "")))
                if (String(result.message) === "Like removed!") {

                    like_button.innerHTML = `❤️ ${parseInt(String(like_button.innerHTML).replace("❤️", "")) - 1}`
                }
                else {
                    like_button.innerHTML = `❤️ ${parseInt(String(like_button.innerHTML).replace("❤️", "")) + 1}`
                }
            })
        })
        
    })
    PostHandler()
})