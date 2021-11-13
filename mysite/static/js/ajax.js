$(document).ready(function() {

    // Like Post Ajax
    $(".btn-like").click(function(e) {
        e.preventDefault();
        var id = $(this).attr('id');
        var ur = $(this).attr('data-url');
        let csr = $('input[name=csrfmiddlewaretoken]').val();
        // alert(id);
        // alert(ur);
        // console.log("liked button clicked.");
        let mydata = { csrfmiddlewaretoken: csr };
        debugger
        $.ajax({
            url: ur,
            method: "POST",
            data: mydata,
            dataType: 'json',
            success: function(data) {
                if (data.liked) {
                    // console.log(data)
                    $('#' + id).html('<i class="fas fa-2x fa-thumbs-up" style="color:royalblue;"></i> ' + data.count)
                } else {
                    // console.log(data)
                    $('#' + id).html('<i class="fas fa-2x fa-thumbs-up"></i> ' + data.count)
                }
            },
        });
    });

    // Comment Post Ajax
    $(".button_comment").click(function(e) {
        e.preventDefault();
        // console.log('Button Clicked!')
        let post_id = $(this).attr('data-postId')
        let path = $(this).attr('data-url');
        let csr = $('input[name=csrfmiddlewaretoken]').val();
        let comment = $("#exampleModal_" + post_id).find('textarea').val();
        $.ajax({
            method: 'POST',
            url: path,
            data: { comment_text: comment, csrfmiddlewaretoken: csr },
            dataType: 'json',
            success: function(data) {
                $('#added_comment_' + data.post).html('<h5>' + data.user + '</h5><p>' + data.comment_text + '</p>')
                $('#comment_' + data.post + '_count').html(data.comment_count + ' comments')
            },
            error: function(data) {
                alert('Ajax failed!')
            }
        });
    });
});