from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        # Aktifkan Jinja2 untuk render template HTML
        config.include('pyramid_jinja2')

        # Include modul model dan route
        config.include('.models')
        config.include('.routes')

        # Pindai semua view di folder views, termasuk frontend dan API
        config.scan('.views.mk_web')         # frontend
        config.scan('.views.matakuliah')     # API

    return config.make_wsgi_app()
