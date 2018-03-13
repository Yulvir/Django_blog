/* like button */
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


/* Add new comment on post button */
$(document).ready(function() {
    $('.add-new-comment').click(function() {
        var id;
        id = $(this).attr('data-post-id');
        $.get('/add-comment-to-post/', {
            post_id: id
        }, function(data) {
            $('.add_comment_to_post').html(data);

            var input = document.createElement("input");
            input.setAttribute('type', 'text');
            var parent = document.getElementById("add-comment");
            parent.appendChild(input);

        });
    });
});