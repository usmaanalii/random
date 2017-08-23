# External CSS and JS
from dash import Dash
#   - dash_core_components and dash_html_components
#     come with bundles
#   - dash checks which are needed, this can be customised and extended

# * Including custom CSS and JS in your Dash app
app = Dash()

# Append an externall hosted CSS stylesheet
my_css_url = "https://unpkg.com/normalize.css@5.0.0"
app.css.append_css({
    'external_url': my_css_url
})

# Append as an externally hosted JS bundle
my_js_url = 'https://unkpg.com/some-npm-package.js'
app.scripts.append_script({
    'external_url': my_js_url
})

# Rendering dash apps offline
#   - Serve these files from a folder
#   - Stored as part of components site-packages folder
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True