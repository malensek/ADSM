/** Created by Josiah on 2/18/2015. */

function toggle(element, attribute){
    if($(element).prop(attribute) || $(element).attr(attribute)) {
        $(element).prop(attribute, false);
        $(element).removeAttr(attribute, false);
    } else {
        $(element).prop(attribute, true);
        $(element).attr(attribute, attribute);
    }

}

function toggle_added_state(text) {
    $('#ProductionTypes li').filter(function () {
        return $(this).find('.pt-name').text() == text;  // must be an exact match NOT :contains()
    }).toggleClass('pt-added');  // for styling rows that have already been added
}

function select_production_type(text) {
    var selectors = ['.productiontypelist option', '.grouplist option'];
    $.each(selectors, function(index, selector){
        $(selector).each(function() {
            if ($(this).text() == text) {
                toggle(this, 'selected')
                $(this).closest('.layout-panel').find('.btn-save').removeAttr('disabled') //unsaved changes
            }
        })
    });
    toggle_added_state(text);
}

$(document).on('mousedown', '#ProductionTypes li, #ProductionGroups li, .productiontypelist option', function(event){
    //It's really critical this is mousedown and not click.  the default mousedown event behavior deselects all the other options
    event.preventDefault()
    var text = $(this).text();
    if(this.tagName == 'LI'){  // I want the click target to be the whole row, but the name is defined in pt-name
        text = $(this).find('.pt-name, .pt-group-name').text();
    }
    select_production_type(text)
})

$('.productiontypelist, .grouplist').livequery(function(){
    $('#ProductionTypes li').removeClass('pt-added')  // clears old data
    $(this).find('option[selected]').each(function(index, element){
        toggle_added_state($(element).text())
    })
})