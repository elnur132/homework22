from django import template

register = template.Library()

@register.filter('uglify')
def uglify(field):
    i=0
    modified_text = ""
    for letter in field:
        i += 1
        if i % 2 == 0:
            modified_text += letter.upper()
        else:
            modified_text += letter.lower()
    
    return modified_text