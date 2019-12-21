AOS.init({
    once: true,
    duration: 1000,
    offset: 0,
    delay: 100
});

function vanquishNav() {
    var navlinks = document.getElementsByClassName("navlinks").item(0);
    if (navlinks.style.height) {
        toggleNav();
    }
}

function toggleNav() {
    let navlinks = document.getElementsByClassName("navlinks").item(0);
    if (navlinks.style.height) {
        navlinks.style.removeProperty("height");
        navlinks.removeAttribute("style");
    } else {
        let height = 0;
        let links = navlinks.getElementsByTagName("a");
        for (var i = 0; i < links.length; i++) {
            height += links.item(i).clientHeight;
        }
        navlinks.style = "height: " + height + "px";
    }
}

function positionFooter() {
    var nav = document.getElementsByTagName("nav").item(0);
    var footer = document.getElementsByTagName("footer").item(0);
    var main = document.getElementsByTagName("main").item(0);
    mainHeight = window.innerHeight - (nav.offsetHeight + footer.offsetHeight);
    main.style.minHeight = mainHeight + "px";
}

document.body.onresize = function() {
    vanquishNav();
    positionFooter();
    window.onscroll();
}

window.onscroll = function() {
    // Get the key elements
    var nav = document.getElementsByTagName("nav").item(0);
    var logo = document.getElementById("logo-img");
    var burger = document.getElementsByTagName("button").item(0);

    // What are the key values?
    var IMGHEIGHT = getComputedStyle(burger)["display"] === "none" ? 400 : 200;
    var NAVHEIGHT = 50;
    var position = window.pageYOffset;
    
    // What should the height of the navbar be?
    var desiredNavHeight = Math.max(IMGHEIGHT - position, NAVHEIGHT)
    nav.style.height = desiredNavHeight + "px";

    // What opacity should the nav background be?
    var desiredOpacity = Math.min(position / (IMGHEIGHT - NAVHEIGHT), 1);
    var background = getComputedStyle(nav)["background-color"];
    var re = /\d+, \d+, \d+/;
    nav.style.backgroundColor = "rgba(" + background.match(re)[0] + ", " + desiredOpacity + ")";

    // Should the coloring be dark or light?
    if (position < (IMGHEIGHT / 2)) {
        nav.classList.add("expanded");
    } else {
        nav.classList.remove("expanded");
    }

    // What should the height of the logo be?
    var desiredLogoHeight = Math.max(0.3 * nav.offsetHeight, 0.8 * NAVHEIGHT);
    logo.style.height = desiredLogoHeight + "px";
}

document.body.onresize();
window.onscroll();