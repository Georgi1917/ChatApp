let url = `ws://${window.location.host}/ws/socket-server/`

const chatSocket = new WebSocket(url)

chatSocket.onmessage = function(e){
    let data = JSON.parse(e.data)

    if (data.type === "chat") {
        let messages = document.getElementById("messages")
        let pMessageElement = document.createElement("p")
        pMessageElement.textContent = `${data.username} : ${data.message}`
        if (data.message_foreign_id === data.user_id) {
            pMessageElement.style.color = "red"
        }

        messages.appendChild(pMessageElement)
    }
}

let form = document.getElementById("form")

form.addEventListener("submit", (e) => {
    e.preventDefault()
    let message = e.target.message.value
    chatSocket.send(JSON.stringify({
        'message': message
    }))
    form.reset()
})

