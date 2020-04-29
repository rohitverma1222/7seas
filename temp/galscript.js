$(document).ready(function(){
	$('.toggler-nav').click(function(){
		$('.toggler-nav').toggleClass('bar-acrose');
		$('.main-nav').toggleClass('show-menu');
		$('.user-btn').toggleClass('show-btn');
	});
});
