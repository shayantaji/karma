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





// Product  adn Article Load More Comments


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


//add_product_to_order
function addProductToOrder(productId, productCount = 1) {

    $.get('/order/add-to-order/', {
        product_id: productId,
        count: productCount
    }).then(function (res) {

        Swal.fire({
            title: 'اعلان',
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirm_button_text
        }).then(function (result) {

            if (result.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/user/login/';
            }

        });

    }).fail(function (xhr) {

        console.log('STATUS:', xhr.status);
        console.log('RESPONSE:', xhr.responseText);

        Swal.fire({
            title: 'خطا',
            text: 'خطایی رخ داده است. لطفاً دوباره تلاش کنید.',
            icon: 'error',
            confirmButtonText: 'باشه'
        });

    });
}

function removeOrderDetail(detailId) {
    $.get('/panel/remove-order-detail?detail_id=' + detailId).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}


// detail id => order detail id
// state => increase , decrease
function changeOrderDetailCount(detailId, state) {
    $.get('/panel/change-order-detail?detail_id=' + detailId + '&state=' + state).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}



// Ajax favorites icon in single-product
$(document).on('click', '.favorite-btn', function (e) {

    e.preventDefault();

    const button = $(this);
    const productId = button.data('product-id');
    const url = button.data('url');

    $.get(url, {
        product_id: productId
    }).then(function (res) {

        if (res.status === 'success') {

            Swal.fire({
                title: 'اعلان',
                text: res.message,
                icon: 'success',
                confirmButtonText: 'باشه'
            });

            if (res.is_favorite) {

                button.addClass('favorite-active');

                button.attr(
                    'title',
                    'حذف از لیست علاقه‌مندی‌ها'
                );

            } else {

                button.removeClass('favorite-active');

                button.attr(
                    'title',
                    'اضافه کردن به لیست علاقه‌مندی‌ها'
                );

            }

        } else {

            Swal.fire({
                title: 'اعلان',
                text: res.message,
                icon: 'warning',
                confirmButtonText: 'باشه'
            });

        }

    }).fail(function (xhr) {

        console.log('STATUS:', xhr.status);
        console.log('RESPONSE:', xhr.responseText);

        Swal.fire({
            title: 'خطا',
            text: 'خطایی رخ داده است. لطفاً دوباره تلاش کنید.',
            icon: 'error',
            confirmButtonText: 'باشه'
        });

    });

});

//payment
document.addEventListener('DOMContentLoaded', function () {
    const messageBox = document.getElementById('message-box');

    if (messageBox) {
        setTimeout(function () {
            messageBox.scrollIntoView({
                behavior: 'smooth',
                block: 'center'
            });
        }, 100);
    }

    const form = document.getElementById('checkout-form');
    const accept = document.getElementById('accept');
    const paymentBtn = document.getElementById('payment-btn');

    if (!form || !accept || !paymentBtn) return;

    const requiredFields = form.querySelectorAll('.checkout-required');

    function checkForm() {
        let valid = true;

        requiredFields.forEach(function (field) {
            if (!field.value.trim()) {
                valid = false;
            }
        });

        if (valid && accept.checked) {
            paymentBtn.classList.remove('payment-disabled');
            paymentBtn.classList.add('payment-active');
        } else {
            paymentBtn.classList.remove('payment-active');
            paymentBtn.classList.add('payment-disabled');
        }
    }

    requiredFields.forEach(function (field) {
        field.addEventListener('input', checkForm);
        field.addEventListener('change', checkForm);
    });

    accept.addEventListener('change', checkForm);

    paymentBtn.addEventListener('click', function (event) {
        if (paymentBtn.classList.contains('payment-disabled')) {
            event.preventDefault();
        }
    });

    checkForm();
});