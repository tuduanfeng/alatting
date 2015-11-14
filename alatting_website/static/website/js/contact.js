$(document).ready(function () {
    $('a.contact').click(function(){
        var target = 'div.' + $(this).attr('for');
        var target_container = $(this).parents().find('div.poster-top').find('div.poster-top-information');
        $(target_container).find('div.description').hide();
        $(target_container).find('div.contact-info').hide();
        $(target_container).find(target).show();
        $(target_container).find(target).css('display','table-cell');
    });
     $('a.logo').click(function(){
        var target_container = $(this).parents().find('div.poster-top').find('div.poster-top-information');
        $(target_container).find('div.description').show();
        $(target_container).find('div.contact-info').hide();
    });
});