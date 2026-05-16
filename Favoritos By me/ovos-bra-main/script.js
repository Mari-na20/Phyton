function showOptions(){
document.getElementById("startScreen").classList.add("hidden")
document.getElementById("optionsScreen").classList.remove("hidden")
}

function startTimer(seconds){

document.getElementById("optionsScreen").classList.add("hidden")
document.getElementById("timerScreen").classList.remove("hidden")

let time = seconds

let timer = setInterval(function(){

let minutes = Math.floor(time/60)
let secs = time % 60

document.getElementById("time").innerText =
String(minutes).padStart(2,"0") + ":" +
String(secs).padStart(2,"0")

time--

if(time < 0){

clearInterval(timer)

document.getElementById("timerScreen").classList.add("hidden")
document.getElementById("doneScreen").classList.remove("hidden")

}

},1000)

}

function restart(){
location.reload()
}