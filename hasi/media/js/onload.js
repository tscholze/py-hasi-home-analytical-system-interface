
$(document).ready(function() {
    $(".box .minimize").click(function () {
    	if($(this).hasClass('max')) {
        	$(this).parent().parent().find('.boxcontent').slideUp('fast');
        }
        else if($(this).hasClass('min')) {
        	$(this).parent().parent().find('.boxcontent').slideDown('fast');
   		}
		$(this).toggleClass('min').toggleClass('max');

   	});
   	
    $(".box .close").click(function () {
        	$(this).parent().parent().css('display', 'none');
   	});
})
