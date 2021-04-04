
$(".top_bar__nav__item__title").on('click', function (el) {      
    // Відкриває елементи навігації таким чином, щоб випадаюче меню не виходило за межі екрену
    
    var el = this.parentElement;

    var checked = !$('.top_bar__nav__item__is_open', el).prop("checked");
    $('.top_bar__nav__item__is_open', el).prop("checked", checked);

    if ($('.top_bar__nav__item__menu', el).length) {        
        var elm = $('.top_bar__nav__item__menu', el);
        var off = elm.offset();
        var l = off.left;
        var w = elm.width();
        var docW = $(window).width();

        var isEntirelyVisible = (l + w <= docW);

        if (!isEntirelyVisible) {
            $(elm).addClass('__reverse');
        } else {
            $(elm).removeClass('__reverse');
        }
    }
});



document.addEventListener('click', function(event) {
    // Закриває меню навігації, якщо відбувся клік поза межеми цього меню

    var radio = document.querySelector('input[name="nav"]:checked');
    if(radio) {
        var nav_item = radio.parentElement;       
        if(!nav_item.contains(event.target)) {
            radio.checked = false;
        } 
    }         
});

