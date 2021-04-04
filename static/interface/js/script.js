
function toggle_nav_menu(el) {
    // Відкриває елементи навігації таким чином, щоб випадаюче меню не виходило за межі екрену
    var checked = !$('.top_bar__nav__item__is_open', el).prop("checked");
    $('.top_bar__nav__item__is_open', el).prop("checked", checked);

    if ($('.top_bar__nav__item__menu', el).length) {        
        var elm = $('.top_bar__nav__item__menu', el);
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
}

$(".top_bar__nav__item__title").on('click', function (el) {          
    
    var el = this.parentElement;    
    toggle_nav_menu(el);    
});

$(document).on('click', function (el) { 
    
    var radio = $('input[name="nav"]:checked').get(0);
    
    if(radio) {
        var nav_item = radio.parentElement;   
           
        if(!nav_item.contains(el.target)) {
            toggle_nav_menu(nav_item);
        } 
    } 
});


