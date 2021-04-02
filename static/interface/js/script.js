$(".top_bar__nav__item").on('mouseenter mouseleave', function (el) {
    
    $('.top_bar__nav__item__menu', this).toggleClass('__show');
    if ($('.top_bar__nav__item__menu', this).length) {        
        var elm = $('.top_bar__nav__item__menu', this);
        var off = elm.offset();
        var l = off.left;
        var w = elm.width();
        var docW = $(window).width();
        console.log(off)

        var isEntirelyVisible = (l + w <= docW);

        if (!isEntirelyVisible) {
            $(elm).addClass('__reverse');
        } else {
            $(elm).removeClass('__reverse');
        }
    }
});