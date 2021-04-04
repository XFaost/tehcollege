
$(".nav__item__title").on('click', function () {          
    
    var el = this.parentElement; 

    // Відкриває елементи навігації таким чином, щоб випадаюче меню не виходило за межі екрену
    var checked = !$('.nav__item__is_open', el).prop("checked");
    $('.nav__item__is_open', el).prop("checked", checked);

    if ($('.nav__item__menu', el).length) {        
        var elm = $('.nav__item__menu', el);
        $(elm).removeClass('__reverse');
        var off = elm.offset();
        var l = off.left;
        var w = elm.width();
        var docW = $(window).width();

        var isEntirelyVisible = (l + w <= docW);

        if (!isEntirelyVisible) {
            $(elm).addClass('__reverse');
        }
    }   
});

$(document).on('click', function (el) { 
    
    var radio = $('input[name="nav"]:checked').get(0);
    
    if(radio) {
        var nav_item = radio.parentElement;   
           
        if(!nav_item.contains(el.target)) {
            radio.checked = false;
        } 
    } 
});


