# Dash HTML Components
#   - Dash provides pure Python abstraction around HTML, CSS and JS
#   - Allows you to compose your layout using Python structures via
#     the dash-html-components library

# Example: Simple HTML structure
html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P(
            'This conversion happens begint the scenes by Dash\'s Javascript front-end')
    ])
])

# This becomes
'''
<div>
    <h1>Hello</h1>
    <div>
        <p>Dash converts Python classes into HTML</p>
        <p>This conversion happens behind the scenes by Dash's JavaScript front-end</p>
    </div>
</div>
'''

# Using HTML Components
#   - style -> dictionary
#   - style properties -> camelCase
#   - class key is renamed -> className
#   - Don't need to specify px

# Example: Styling HTML Components
html.Div([
    html.Div('Example Div', style={'color': 'blue', 'fontSize': 14}),
    html.P('Example P', className='my-class', id='my-p-element')
], style={'marginBottom': 50, 'marginTop': 25})

# This Becomes

'''
<div style="margin-bottom: 50px; margin-top: 25px;">

    <div style="color: blue; font-size: 14px">
        Example Div
    </div>

    <p class="my-class", id="my-p-element">
        Example P
    </p>

</div>
'''