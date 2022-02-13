$(document).ready(function (){
    $('#name').focusout(function () {
       $('.dropdown-menu').toggle();
    });
    $(document).mousedown(function(){
    	$('.dropdown-menu').hide();
    })
    
});