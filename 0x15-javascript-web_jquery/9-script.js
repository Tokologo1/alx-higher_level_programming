$('document').ready(function () {
	$.get('https://fourfish.com/hellosalut/?lang=fr', function (data) {
		$('DIV#hello').text(data.hello);
	});
});
