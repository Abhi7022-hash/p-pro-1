function sendFeedback() {
    const name = document.getElementById("name").value;
    const message = document.getElementById("message").value;

    fetch("/api/feedback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, message })
    })
    .then(res => res.json())
    .then(() => {
        loadFeedback();
    });
}

function loadFeedback() {
    fetch("/api/feedback")
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("list");
            list.innerHTML = "";
            data.forEach(f => {
                const li = document.createElement("li");
                li.innerText = `${f.name}: ${f.message}`;
                list.appendChild(li);
            });
        });
}

loadFeedback();

