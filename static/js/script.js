function change_lang(language){
    editor.session.setMode("ace/mode/" + language.value);
}

function change_theme(theme){
    editor.setTheme("ace/theme/" + theme.value);
}

function code_submit(){
    language = document.getElementById('language').value;
    code = editor.getSession().getValue();
    document.getElementById('solution').innerHTML = code;
    document.getElementById('code_form').submit();

}