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

function sortTable(n) {
    /**
     * Sorts the rows of a table according to the values in column n.
     */

    // Get references
    var table = document.getElementsByTagName("table").item(0);
    var tbody = table.tBodies[0];
    var ths = table.rows.item(0).getElementsByTagName("th");
    var th = ths.item(n);
    var store = [];

    // Should we sort ascending or descending?
    var dir = "desc";
    if (th.classList.contains("desc")) {
        dir = "asc";
    }
    console.log("Going to sort:", dir)
    
    // Update store with values
    var textColumn = false;
    for (var i=1, len=table.rows.length; i<len; i++){
        var row = table.rows[i];
        var sortnr = parseFloat(row.cells[n].dataset.sort);
        if (isNaN(sortnr)) {
            textColumn = true;
            store.push([row.cells[n].dataset.sort, row]);
        } else {
            store.push([sortnr, row]);
        } 
    }

    // Sort the values
    if (textColumn) {
        store.sort(dir == "asc" ? function(x,y){
            return y[0] < x[0] ? 1 : -1;
        } : function(x,y){
            return x[0] < y[0] ? 1 : -1;  
        });
    } else {
        store.sort(dir == "asc" ? function(x,y){
            return x[0] - y[0];
        } : function(x,y){
            return y[0] - x[0];
        });
    }
    
    for(var i=0, len=store.length; i<len; i++){
        tbody.appendChild(store[i][1]);
    }

    // Update HTML class names
    for (var t = 0; t < ths.length; t++) {
        ths[t].classList.remove("asc");
        ths[t].classList.remove("desc");
    }
    if (dir === "asc") {
        th.classList.add("asc");
    } else {
        th.classList.add("desc");
    }
}

document.body.onresize = function() {
    vanquishNav();
}