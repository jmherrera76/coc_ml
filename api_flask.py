from apiflask import APIFlask
from blueprints.predict.attacks import construct_blueprint as attack_stars_blueprint
from blueprints.detection.defenses import construct_blueprint as detection_defenses_blueprint


app = APIFlask(__name__,
               title='API COC ML IA',
               version='0.0.1')

app.config['SERVERS'] = [
    {
        'name': 'Development Server',
        'url': 'http://127.0.0.1:5000/'
    },
    {
        'name': 'Production Server',
        'url': 'http://api.example.com'
    },
    {
        'name': 'Testing Server',
        'url': 'http://test.example.com'
    }
]


app.config['DESCRIPTION'] = """
The description for this API. It can be very long and **Markdown** is supported.
In this example, the tags is manually set. However, in a real world application, it will be
enough to use the automatic tags feature based on blueprint, see the example for blueprint
tags under the "examples/blueprint_tags" folder:
```

$ flask run
```
The source can be found at [examples/blueprint_tags/app.py][_blueprint_tags].
[_blueprint_tags]: https://github.com/apiflask/apiflask/tree/main/examples/blueprint_tags/app.py
"""

"""
app.config['TAGS'] = [
    {'name': 'Hello', 'description': 'The description of the **Hello** tag.'},
    {'name': 'Pet', 'description': 'The description of the **Pet** tag.'}
]
"""


# openapi.info.contact
app.config['CONTACT'] = {
    'name': 'API Support',
    'url': 'https://support.chickensclan.com/',
    'email': 'support@chickensclan.com'
}

# openapi.info.license
app.config['LICENSE'] = {
    'name': 'MIT',
    'url': 'https://opensource.org/licenses/MIT'
}

app.config['INFO'] = {
    'description': 'hello info',
    'termsOfService': 'http://example.com',
    'contact': {
        'name': 'API Support',
        'url': 'http://www.example.com/support',
        'email': 'support@example.com'
    },
    'license': {
         'name': 'Apache 2.0',
         'url': 'http://www.apache.org/licenses/LICENSE-2.0.html'
     }
}

app.config['TERMS_OF_SERVICE'] = 'http://example.com'

app.register_blueprint(attack_stars_blueprint())
app.register_blueprint(detection_defenses_blueprint())
app.run()
