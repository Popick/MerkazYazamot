



$(document).ready(function() {
    $(signupbutton).click(function() {
        $(".container-signin").css("display", "none");
        $(".container-signup").css("display", "block");
    });

    $(signinbutton).click(function() {
        $(".container-signup").css("display", "none");
        $(".container-signin").css("display", "block");
    });

});