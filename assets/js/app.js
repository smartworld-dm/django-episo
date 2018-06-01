$(document).on("click", ".publish", function() {
    var article_id = $(this).attr('article_id');
	$(this).addClass('btn-default');
	$(this).removeClass('btn-success');
	$(this).addClass('dispublish');
	$(this).removeClass('publish');
	$(this).html('非公開にする');

	$.ajax({
		type: "POST",
        url: '/brand-admin/publish_article/',
        data: {
          'article_id': article_id,
          'is_published': false,
          'csrfmiddlewaretoken':$( "input[name='csrfmiddlewaretoken']" ).val()
        },
        dataType: 'json',
        success: function (data) {
        }
      });
});

$(document).on("click", ".dispublish", function() {
	var article_id = $(this).attr('article_id');
	$(this).removeClass('btn-default');
	$(this).addClass('btn-success');
	$(this).removeClass('dispublish');
	$(this).addClass('publish');
	$(this).html('公開する');

	$.ajax({
		type: "POST",
        url: '/brand-admin/publish_article/',
        data: {
          'article_id': article_id,
          'is_published': true,
          'csrfmiddlewaretoken':$( "input[name='csrfmiddlewaretoken']" ).val()
        },
        dataType: 'json',
        success: function (data) {
        }
      });
});