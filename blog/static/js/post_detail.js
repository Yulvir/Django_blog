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

//insert after is not implemented in js so you can use this
function insertAfter(referenceNode, newNode) {
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}

$(document).ready(function() {
    $('.add-new-comment').click(function() {
        console.log("Estroy dentyro")
        //Disable button after one click, if not show new text input for every click
        $(this).prop('disabled', true);

        /*
        var parent = document.getElementById('text-box-input')
        var div = document.createElement('div')
        div.setAttribute('class', 'input-group mb-3')
        div.setAttribute('id', 'input-group mb-3')
        insertAfter(parent, div)


        var parent = document.getElementById('input-group mb-3')
        var input = document.createElement("input");
        input.setAttribute('type', 'text');
        input.setAttribute('class', 'form-control');
        input.setAttribute('placeholder', "Left your comment here");

        parent.appendChild(input)

        parent.appendChild(div)
        */

        var comment_text = document.createElement("textarea")
        comment_text.setAttribute("id", "text-box-input")
        var like_comment_div = document.getElementById('like_comment_div')
        insertAfter(parent, like_comment_div)
//This span is used to measure the size of the textarea
//it should have the same font and text with the textarea and should be hidden
        var span = $('<span>').css('display','inline-block')
                              .css('word-break','break-all')
                              .appendTo('#text-box-input')
        function initSpan(textarea){
          span.text(textarea.text())
              .width(textarea.width())
              .css('font',textarea.css('font'));
        }
        $('textarea').on({
            input: function(){
               var text = $(this).val();
               console.log
               span.text(text);
               $(this).height(text ? span.height() : '1.1em');
            },
            focus: function(){
               initSpan($(this));
            },
            keypress: function(e){
               //cancel the Enter keystroke, otherwise a new line will be created
               //This ensures the correct behavior when user types Enter
               //into an input field
               if(e.which == 13) e.preventDefault();
            }
        });



    });
});

