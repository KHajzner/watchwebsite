function tabView(page) {
    var i, tabcontent;
    tabcontent = document.getElementsByClassName("tabcontent");

    for (i = 0; i <tabcontent.length; i++){
        tabcontent[i].style.display = "none";
    }
    document.getElementById(page).style.display = "block";

}
