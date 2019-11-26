function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = $.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
}

$(document).on('change', '.btn-file :file', function () {
    let input = $(this),
        numFiles = input.get(0).files ? input.get(0).files.length : 1,
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.trigger('fileselect', [numFiles, label]);
});

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});
$(document).ajaxError(function (xhr, err) {
    $('#dimmer_of_page').removeClass('active');
    if (err['responseJSON']) {
        if (err['responseJSON'].error) err_notify(err['responseJSON'].error);
        else if (err['responseJSON'].detail) err_notify(err['responseJSON'].detail);
        else err_notify(UNKNWON_ERROR);
    }
    else err_notify(UNKNWON_ERROR);
});

window.err_notify = function (message) {
    $.notify(message, {autoHide: false, style: 'bootstrap', className: 'error'});
    return false;
};

window.success_notify = function (message) {
    $.notify(message, {style: 'bootstrap', className: 'success', autoHide: true, autoHideDelay: 10000});
    return true;
};

window.upload_diploma = function(url, data) {
    $('#dimmer_of_page').addClass('active');
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        dataType: 'json',
        contentType: false,
        processData: false,
        mimeType: 'multipart/form-data',
        xhr: function() {
            return $.ajaxSettings.xhr();
        },
        success: function () {
            $('#dimmer_of_page').removeClass('active');
            window.location.replace('');
        }
    });
};

$(document).ready(function () {
    $('.note-popup').each(function () {
        let position = $(this).data('position');
        position ? $(this).popup({position: position}) : $(this).popup();
    });
});
