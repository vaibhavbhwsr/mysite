$(document).ready(function () {

    $(".btn-like").click(function (e) {
        e.preventDefault();
        var id = $(this).attr('id');
        var ur = $(this).attr('data-url');
        let csr = $('input[name=csrfmiddlewaretoken]').val();
        // alert(id);
        // alert(ur);
        // console.log("liked button clicked.");
        let mydata = {sid: id, csrfmiddlewaretoken: csr};
        $.ajax({
            url: ur,
            method: "POST",
            data: mydata,
            dataType: 'json',
            success: function (data) {
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
    // alert("hello");
});
