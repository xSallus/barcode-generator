import os


template_folder = os.path.abspath(__file__)
template_folder = os.path.dirname(template_folder)
template_folder = os.path.dirname(template_folder)
template_folder = os.path.dirname(template_folder)
template_folder = os.path.join(template_folder,'templates')
static_folder = os.path.join(template_folder,'static')
