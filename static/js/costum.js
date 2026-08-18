const menu = document.querySelector(".main_menu");

window.addEventListener("scroll", function () {

    if (window.scrollY > 120) {

        menu.classList.add("karma-sticky");
        document.body.classList.add("karma-header-padding");

    } else {

        menu.classList.remove("karma-sticky");
        document.body.classList.remove("karma-header-padding");

    }

});

const overlay = document.getElementById("mapOverlay");

if (overlay) {

    overlay.addEventListener("click", function () {

        this.style.display = "none";

    });

}
document.addEventListener("DOMContentLoaded", function () {

    const errorList = document.querySelector(".errorlist");

    if (errorList) {

        const form = errorList.closest("form");

        if (form) {

            form.scrollIntoView({
                behavior: "smooth",
                block: "center"
            });

        }

    }

});

document.addEventListener("DOMContentLoaded", function () {
    const section = document.getElementById("auth-section");

    if (section) {
        section.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }
});

document.addEventListener('DOMContentLoaded', function () {
    document.addEventListener('submit', function (e) {
        if (!e.target.matches('#newsletter-form')) {
            return;
        }

        e.preventDefault();

        const form = e.target;
        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            let messageBox = document.querySelector('.newsletter-message');

            if (!messageBox) {
                messageBox = document.createElement('div');
                messageBox.className = 'newsletter-message';
                form.parentNode.insertBefore(messageBox, form);
            }

            messageBox.className = 'newsletter-message ' + data.type;
            messageBox.textContent = data.message;

            messageBox.scrollIntoView({
                behavior: 'smooth',
                block: 'center'
            });
        })
        .catch(error => {
            console.error('Newsletter Error:', error);
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {

    document.addEventListener('submit', function (e) {

        if (!e.target.matches('#contactForm')) {
            return;
        }

        e.preventDefault();

        const form = e.target;
        const messageBox = document.getElementById('contact-message');
        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {

            messageBox.className = 'contact-message ' + data.type;
            messageBox.textContent = data.message;

            if (data.type === 'success') {
                form.reset();
            }

            messageBox.scrollIntoView({
                behavior: 'smooth',
                block: 'center'
            });

        })
        .catch(error => {

            console.error('Contact Error:', error);

            messageBox.className = 'contact-message error';
            messageBox.textContent = 'خطایی رخ داد. لطفاً دوباره تلاش کنید.';

        });

    });

});

$(document).on('click', '.reply-comment', function (e) {

    e.preventDefault();


    let commentId = $(this).data('comment-id');


    $('#parent-id').val(commentId);


    $('#product-comment-form-title')
        .text('پاسخ به نظر');


    $('#product-comment-submit')
        .text('ارسال پاسخ');


    $('#cancel-reply').show();


    $('#product-comment-form')[0].scrollIntoView({
        behavior: 'smooth',
        block: 'center'
    });


});


$(document).on('click', '#cancel-reply', function () {


    $('#parent-id').val('');


    $('#comment-form-title').text('ارسال نظر');


    $('#comment-submit').text('ارسال نظر');


    $('#cancel-reply').hide();


});




// Article Comment

$(document).on('submit', '#article-comment-form', function (e) {

    e.preventDefault();


    let form = $(this);

    let submit = $('#comment-submit');

    let messageBox = $('#comment-message');


    submit.prop('disabled', true);



    $.ajax({

        url: articleCommentUrl,

        type: 'POST',

        data: form.serialize(),


        success:function(response){


            messageBox.html(
                '<div class="alert alert-success">'+
                response.message+
                '</div>'
            );


            form[0].reset();


            $('#parent-id').val('');


            $('#comment-form-title').text('یک نظر بگذارید');


            submit.text('ارسال نظر');


            $('#cancel-reply').hide();



            setTimeout(function(){

                location.reload();

            },700);



        },


        error:function(xhr){


            let message='خطایی رخ داد.';


            if(xhr.responseJSON && xhr.responseJSON.message){

                message=xhr.responseJSON.message;

            }



            messageBox.html(
                '<div class="alert alert-danger">'+
                message+
                '</div>'
            );


        },


        complete:function(){

            submit.prop('disabled',false);

        }


    });


});





// Product Load More Comments


$(document).on('click','#load-more-comments',function(){


    let btn=$(this);


    let page=parseInt(btn.attr('data-page'))+1;


    let url=btn.data('url');



    btn.prop('disabled',true);


    btn.text('در حال بارگذاری...');



    $.ajax({


        url:url,

        type:'GET',


        data:{
            page:page
        },


        success:function(response){


            $('#comments-list').append(response.html);


            btn.attr('data-page',page);



            if(!response.has_next){


                btn.remove();


            }else{


                btn.prop('disabled',false);


                btn.text('نمایش نظرات بیشتر');


            }


        },


        error:function(){


            btn.prop('disabled',false);


            btn.text('نمایش نظرات بیشتر');


            alert('خطا در دریافت نظرات');


        }


    });


});





// Product Comment

$(document).on('submit','#product-comment-form',function(e){

    e.preventDefault();


    let form=$(this);

    let submit=$('#product-comment-submit');

    let messageBox=$('#product-comment-message');


    submit.prop('disabled',true);



    $.ajax({

        url:productCommentUrl,

        type:'POST',

        data:form.serialize(),


        success:function(response){


            messageBox.html(

                '<div class="alert alert-success">'+
                response.message+
                '</div>'

            );


            form[0].reset();


            $('#parent-id').val('');


            $('#product-comment-form-title')
                .text('ارسال نظر');


            $('#product-comment-submit')
                .text('ارسال نظر');


            $('#cancel-reply').hide();



            setTimeout(function(){

                location.reload();

            },700);



        },


        error:function(xhr){


            let message='خطایی رخ داد';



            if(xhr.responseJSON && xhr.responseJSON.message){

                message=xhr.responseJSON.message;

            }



            messageBox.html(

                '<div class="alert alert-danger">'+
                message+
                '</div>'

            );


        },


        complete:function(){


            submit.prop('disabled',false);


        }


    });


});

document.querySelectorAll('.reply-comment').forEach(button => {

    button.addEventListener('click',function(e){

        e.preventDefault();

        let commentId = this.dataset.commentId;

        document.getElementById('parent-id').value = commentId;

        document.getElementById('comment-form-title').innerText =
        "پاسخ به نظر";

        document.getElementById('product-comment-form')
        .scrollIntoView();

    });

});