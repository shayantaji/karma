const menu = document.querySelector(".main_menu");

window.addEventListener("scroll", function () {

    if (window.scrollY > 120) {

        menu.classList.add("karma-sticky");
        document.body.classList.add("karma-header-padding");

    } else {

        menu.classList.remove("karma-sticky");
        document.body.classList.remove("karma-header-padding");

    }

});