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


function sendMessage(){




        console.log("Send comment")
        $(".submit-comment-button").detach()
        $(".comment-text-area").detach()
        $('.add-new-comment').text("Add New Comment")


}


// Add new comment
$(document).ready(function() {
    $('.add-new-comment').click(function() {
        var state = $('.add-new-comment').text()
        console.log(state)
        if(state == "Add New Comment"){
            $('.add-new-comment').text("Cancel Comment")

            var text_area = document.createElement("TEXTAREA");
            $("<input type='submit' class='submit-comment-button' onclick='sendMessage()' />").appendTo(".like_comment_div");


            $(text_area).addClass("comment-text-area");
            $(text_area).attr("rows", "4").attr("cols", "60")
            $('.leave_comment_div').append(text_area)
        } else{

            $('.add-new-comment').text("Add New Comment")
            $('.comment-text-area').detach()
            $('.submit-comment-button').detach()
        }

    });
});

