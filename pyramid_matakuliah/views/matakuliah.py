from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest
from ..models import Matakuliah

@view_config(route_name='mk_list', renderer='json')
def mk_list(request):
    mks = request.dbsession.query(Matakuliah).all()
    return {'matakuliah': [mk.to_dict() for mk in mks]}

@view_config(route_name='mk_detail', renderer='json')
def mk_detail(request):
    mk = request.dbsession.query(Matakuliah).get(request.matchdict['id'])
    if not mk:
        return HTTPNotFound(json_body={'error': 'Matakuliah tidak ditemukan'})
    return {'matakuliah': mk.to_dict()}

@view_config(route_name='mk_add', request_method='POST', renderer='json')
def mk_add(request):
    try:
        data = request.json_body
        mk = Matakuliah(**data)
        request.dbsession.add(mk)
        request.dbsession.flush()
        return {'success': True, 'matakuliah': mk.to_dict()}
    except Exception as e:
        return HTTPBadRequest(json_body={'error': str(e)})

@view_config(route_name='mk_update', request_method='PUT', renderer='json')
def mk_update(request):
    mk = request.dbsession.query(Matakuliah).get(request.matchdict['id'])
    if not mk:
        return HTTPNotFound(json_body={'error': 'Matakuliah tidak ditemukan'})
    data = request.json_body
    for key in ['kode_mk', 'nama_mk', 'sks', 'semester']:
        if key in data:
            setattr(mk, key, data[key])
    return {'success': True, 'matakuliah': mk.to_dict()}

@view_config(route_name='mk_delete', request_method='DELETE', renderer='json')
def mk_delete(request):
    mk = request.dbsession.query(Matakuliah).get(request.matchdict['id'])
    if not mk:
        return HTTPNotFound(json_body={'error': 'Matakuliah tidak ditemukan'})
    request.dbsession.delete(mk)
    return {'success': True, 'message': 'Matakuliah berhasil dihapus'}
