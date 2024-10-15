$(document).ready(function() {
	$('[data-detail-widget]').click(function() {
		var widgetId = $(this).attr('data-detail-widget');
		var widgetState = $(this).attr('data-detail-widget');
		if (widgetState == 'collapse') {
			$(this).attr('data-detail-widget', 'expand');
			$(this).attr('title', 'Expand');
			$(this).find('i').removeClass('fa-minus').addClass('fa-plus');
		}else{
			$(this).attr('data-detail-widget', 'collapse');
			$(this).attr('title', 'Collapse');
			$(this).find('i').removeClass('fa-plus').addClass('fa-minus');
		}
		console.log('Widget with ID ' + widgetId + ' clicked!');
		console.log(widgetState);
		// Perform additional actions or logic here
	});
});
