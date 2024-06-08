const toggleButton = document.getElementById("toggleButton");
const main_heading = document.querySelector(".main-top-heading");
const card_borders = document.querySelectorAll(".card");
const card_image = document.querySelectorAll(".card-img");
const card_heading = document.querySelectorAll(".card-heading-text");
const card_text = document.querySelectorAll(".card-body-text");
const all_btn = document.querySelectorAll(".navigation-btn-links");

toggleButton.addEventListener("change", function() {
    if (toggleButton.checked) {
        document.body.style.backgroundColor = 	"#808080";
        main_heading.style.color = "black";
        card_borders.forEach(function(card_loop) {
            card_loop.style.border = "1px solid white";
        });
        card_image.forEach(function(card_img_loop) {
            card_img_loop.style.backgroundColor = "#808080";
        });
        card_heading.forEach(function(card_heading_loop) {
            card_heading_loop.style.color = "black";
        });
        card_text.forEach(function(card_text_loop) {
            card_text_loop.style.color = "black";
        });
        all_btn.forEach(function(all_btn_loop) {
            all_btn_loop.style.color = "red";
        })

    } else {
        document.body.style.backgroundColor = "";
        main_heading.style.color = ""; 
        card_borders.forEach(function(card_loop) {
            card_loop.style.border = "";
        });
        card_image.forEach(function(card_img_loop) {
            card_img_loop.style.backgroundColor = "";
        });
        card_heading.forEach(function(card_heading_loop) {
            card_heading_loop.style.color = "";
        });
        card_text.forEach(function(card_text_loop) {
            card_text_loop.style.color = "";
        });
        all_btn.forEach(function(all_btn_loop) {
            all_btn_loop.style.color = "";
        })

    }
});
