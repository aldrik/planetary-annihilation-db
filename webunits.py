"""
Local "web app" for the PA unit database. See http://localhost:8080/list
"""

# Step 0: Make sure we have Bottle. If not, download it.
try:
    import bottle
except ImportError:
    def get_bottle():
        import urllib.request
        import os.path
        savename = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'bottle.py')
        urllib.request.urlretrieve('https://raw.github.com/defnull/bottle/0.11.6/bottle.py',
                                   savename)
        print("Saved Bottle as '{}'".format(savename))
    get_bottle()

from bottle import route, run, template

import units
units.load_units()

@route('/list')
def unit_list():
    return template('unitlist', units=units.units.values())

if __name__ == '__main__':
    run(host='localhost', port=8080,
        reloader=True, # Reload on changes to .py files
        debug=True, # Reload changes to .tpl files
        )