var showing = document.getElementsByClassName("show");
var hiding = document.getElementsByClassName("hide");

function showGregDate(a) {
    var i = Array.prototype.indexOf.call(showing, a.target);
    hiding[i].style.display = "block";
    a.target.style.display = "none";
}

function showMarsDate(a) {
    var i = Array.prototype.indexOf.call(hiding, a.target);
    showing[i].style.display = "block";
    a.target.style.display = "none";
}

for (var i = 0; i < showing.length; i++) {
    showing[i].addEventListener("mouseover", showGregDate); 
    hiding[i].addEventListener("mouseout", showMarsDate);
}



/*
function changeBG(css) {
    document.body.style.backgroundImage = "url(imgs/"+ css + ")";
    console.log(css);
}
*/

function goToAnchor(anchor) {
    window.location.hash = '#' + anchor;
}
