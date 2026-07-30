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

const overlay = document.getElementById("mapOverlay");

if (overlay) {

    overlay.addEventListener("click", function () {

        this.style.display = "none";

    });

}
document.addEventListener("DOMContentLoaded", function () {

    const errorList = document.querySelector(".errorlist");

    if (errorList) {

        const form = errorList.closest("form");

        if (form) {

            form.scrollIntoView({
                behavior: "smooth",
                block: "center"
            });

        }

    }

});

document.addEventListener("DOMContentLoaded", function () {
    const section = document.getElementById("auth-section");

    if (section) {
        section.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }
});