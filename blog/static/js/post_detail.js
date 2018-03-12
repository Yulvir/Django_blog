
/* like counting */
$(document).ready(function() {
    $('.post-likes').click(function() {
        var id;
        id = $(this).attr('data-post-id');
        $.get('/like-blog/', {
            post_id: id
        }, function(data) {
            $('.like_count_blog').html(data);
        });
    });
});


/* Comment rendering */
$(document).ready(function() {
    $('.add-comment').click(function() {
        var id;
        id = $(this).attr('data-post-id');
        $.get('/add-comment-to-post/', {
            post_id: id
        }, function(data) {
            $('.like_count_blog').html(data);

            var input = document.createElement("input");
            input.setAttribute('type', 'text');
            var parent = document.getElementById("add-comment");
            parent.appendChild(input);

        });
    });
});
