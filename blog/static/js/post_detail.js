/* like button */
$(document).ready(function() {
    $('.post-likes').click(function() {
        var id;
        id = $(this).attr('data-post-id');
        $.get('/like-blog/', {
            post_id: id
        }, function(data) {
        console.log(data)
            $('.like_count_blog').html(data);
        });
    });
});

// Get cookie value to extract the csrf token using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function sendMessage(){

        var id;
        id = $(".add-new-comment").attr('data-post-id');
        var text = $(".comment-text-area").val()
        console.log(text)

        if(text !== ""){
        var csrftoken = getCookie('csrftoken');
        var request;
        request = $.ajax({
            url: "/add-comment-to-post/",
            method: "POST",
            data:
            {
                post_id: id,
                text: text,
                csrfmiddlewaretoken: csrftoken
            },
            datatype: "json"
        });

        request.done(function(msg) {
            //Refresh browser
            window.location.reload()
        });

        request.fail(function(jqXHR, textStatus) {
        });


        $(".submit-comment-button").detach()
        $(".comment-text-area").detach()
        $('.add-new-comment').text("Add New Comment")

        }

}


$(document).ready(function() {


$('#myForm input').on('change', function() {
            var var_name = $("input[name='answer']:checked", "#myForm").val();
            console.log(var_name);

            id = $(".add-new-comment").attr('data-post-id');
            console.log(id);

            var csrftoken = getCookie('csrftoken');
            var request;
            request = $.ajax({
                url: "/answer/",
                method: "POST",
                data:
                {
                    post_id: id,
                    text: var_name,
                    csrfmiddlewaretoken: csrftoken
                },
                datatype: "json"
            });

            request.done(function(msg) {
                //Refresh browser
                window.location.reload()

            });

            request.fail(function(jqXHR, textStatus) {
            });




        });
        });




// Add new comment
$(document).ready(function() {




    $('.add-new-comment').click(function() {
        var state = $('.add-new-comment').text()
        console.log(state)
        if(state == "Add New Comment"){
            $('.add-new-comment').text("Cancel Comment")

            var text_area = document.createElement("textarea");
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

