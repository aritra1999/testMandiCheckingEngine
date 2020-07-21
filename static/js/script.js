function change_lang(language) {
    // console.log(language);
    var id = language.id;
    var optionid = "#"+id+" option:selected"
    editor.session.setMode("ace/mode/" + $(optionid).attr("data-subvalue"));
}

function change_default(language) {
    console.log(language.value);
    $.ajax({
        url: "/metadata/language_default/",
        data: {
            'sector': language.value
        },
        success: function(output){
            // var e = $('#sub_' + id);
            // e.html(output);
            editor.setValue(output)
            console.log(output);
        }
    });
    // editor.session.setMode("ace/mode/" + language.value);
}

function change_theme(theme) {
    editor.setTheme("ace/theme/" + theme.value);
}

function code_submit() {
    language = document.getElementById('language').value;
    code = editor.getSession().getValue();
    document.getElementById('solution').innerHTML = code;
    document.getElementById('code_form').submit();
    $.ajax({
        url: "/metadata/language_default/",
        data: {
            'sector': language.value
        },
        success: function(output){
            // var e = $('#sub_' + id);
            // e.html(output);
            editor.setValue(output)
            console.log(output);
        }
    });
}

$(function () {
    $('[data-toggle="popover"]').popover()
    $('.popover-dismiss').popover({
      trigger: 'focus'
    })
})

