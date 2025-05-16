def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    config.add_route('mk_list', '/api/matakuliah', request_method='GET')
    config.add_route('mk_detail', '/api/matakuliah/{id}', request_method='GET')
    config.add_route('mk_add', '/api/matakuliah', request_method='POST')
    config.add_route('mk_update', '/api/matakuliah/{id}', request_method='PUT')
    config.add_route('mk_delete', '/api/matakuliah/{id}', request_method='DELETE')
