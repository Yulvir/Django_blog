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

        //Disable button after one click, if not show new text input for every click
        $(this).prop('disabled', true);

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
        input.style.height="50%";
        input.style.width="50%";
        parent.appendChild(input)

        var div = document.createElement('span')
        div.setAttribute('class', 'input-group-append')
        var btn = document.createElement('button')
        btn.setAttribute('class', 'btn btn-outline-secondary')
        btn.setAttribute('content', 'Publish');
        div.appendChild(btn)

        parent.appendChild(div)

    });
});

