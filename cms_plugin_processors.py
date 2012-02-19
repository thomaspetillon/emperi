import re

def removeParroundIMG(source, adds):
    try:
        source = source.replace("\n","")
        out = re.sub('<p>.*<img(.*)/?>.*</p>','<img '+re.match('<p>.*<img(.*)/?>.*</p>',source).groups()[0]+' '+adds+' />',source)
    except:
    	out = source
    return out

def carousel(instance, placeholder, rendered_content, original_context):
    '''
    This plugin processor wraps text plugin's output in 'carousel' placeholder.
    So we get the correct structure for coda-slider.js 
    '''
    if placeholder.slot != 'carousel' or (instance._render_meta.text_enabled and instance.parent):
        # Plugins embedded in Text should remain unchanged in order not to break output
        return rendered_content
    else:
        # remove <p> tag arround <img (.*)/>
        # and add left class for auto positionning
        rendered_content = removeParroundIMG(rendered_content,"class='left'")
        from django.template import Context, Template
        # For simplicity's sake, construct the template from a string:
        t = Template('<div class="panel"> <div class="panel-wrapper"><div class="center">{{ content|safe }}</div></div></div>')

        # Prepare that template's context:
        c = Context({
            'content': rendered_content,
        })
        return t.render(c)


