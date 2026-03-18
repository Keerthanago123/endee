
function uploadResume(){

let file=document.getElementById("resume").files[0]

let formData=new FormData()
formData.append("resume",file)

fetch("/upload",{method:"POST",body:formData})
.then(res=>res.json())
.then(data=>{

let html=""

data.forEach(job=>{

html+=`
<div class="job">

<h3>${job.role}</h3>

<b>${job.company}</b>

<p><b>Skills:</b> ${job.skills}</p>

<p><b>Match Score:</b> ${job.match}%</p>

<a href="${job.url}" target="_blank">
<button>Apply</button>
</a>

</div>
`

})

document.getElementById("jobs").innerHTML=html

})

}

function toggleChat(){

let box=document.getElementById("chatbox")

if(box.style.display==="none" || box.style.display===""){
box.style.display="block"
}else{
box.style.display="none"
}

}

function sendChat(){

let input=document.getElementById("chat-input").value

fetch("/chat",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({message:input})
})
.then(res=>res.json())
.then(data=>{

let area=document.getElementById("chat-messages")

area.innerHTML+="<p><b>You:</b> "+input+"</p>"
area.innerHTML+="<p><b>Bot:</b> "+data.reply+"</p>"

})

}

function toggleTheme(){

let body=document.getElementById("body")
body.classList.toggle("dark")

}
