// THEME TOGGLE
const toggle = document.getElementById("themeToggle");
toggle.onclick = () => {
document.body.classList.toggle("light");
localStorage.theme = document.body.classList.contains("light") ? "light":"dark";
};
if(localStorage.theme==="light") document.body.classList.add("light");

// SEARCH
const search = document.getElementById("search");
search.oninput = () => {
const q = search.value.toLowerCase();
document.querySelectorAll(".card").forEach(c=>{
c.style.display = c.innerText.toLowerCase().includes(q) ? "block":"none";
});
};

// TOP BUTTON
const topBtn=document.getElementById("topBtn");
window.onscroll=()=> topBtn.style.display=window.scrollY>300?"block":"none";
topBtn.onclick=()=>window.scrollTo({top:0,behavior:"smooth"});
