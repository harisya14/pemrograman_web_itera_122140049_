def includeme(config):
    # API routes tetap
    config.add_route('mk_list', '/api/matakuliah', request_method='GET')
    config.add_route('mk_detail', '/api/matakuliah/{id}', request_method='GET')
    config.add_route('mk_add', '/api/matakuliah', request_method='POST')
    config.add_route('mk_update', '/api/matakuliah/{id}', request_method='PUT')
    config.add_route('mk_delete', '/api/matakuliah/{id}', request_method='DELETE')

    # Frontend web routes
    config.add_route('mk_home', '/matakuliah')
    config.add_route('mk_add_form', '/matakuliah/add')
    config.add_route('mk_delete_form', '/matakuliah/delete/{id}')
