function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function FollowerHandler() {
    const follow_status = localStorage.getItem('follow_status')
    console.log(follow_status)
    const FollowerCount = document.querySelector('#FollowerCount')
    const follow_button = document.querySelector('#follow_button')
    if(follow_status==undefined){
        follow_status = "Unfollowed"
        localStorage.setItem('follow_status', follow_status)
    };
    if (follow_status === "Unfollowed") {
        follow_button.innerHTML = "Follow"
    } else {
        follow_button.innerHTML = "Unfollow"
    }
    follow_button.addEventListener('click', () => {
        console.log(follow_button)
        console.log(follow_button.parentElement)
        followername = follow_button.value
        followedname = document.querySelector('.username').id
        fetch(`/follow/${followername}/${followedname}`, {
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
            console.log(String(FollowerCount.innerHTML).replace('Followers: ', ""))
            if (String(result.message) === "Unfollowed") {
                follow_button.innerHTML = 'Follow'
                FollowerCount.innerHTML = `Followers: ${parseInt(String(FollowerCount.innerHTML).replace('Followers: ', "")) - 1}`
                localStorage.setItem("follow_status", "Following");
            }
            else {
                follow_button.innerHTML = 'Unfollow'
                FollowerCount.innerHTML = `Followers: ${parseInt(String(FollowerCount.innerHTML).replace('Followers: ', "")) + 1}`
                localStorage.setItem("follow_status", "Unfollowed");
            }
        })
    })
    
}
document.addEventListener('DOMContentLoaded', () => {
    FollowerHandler()
})