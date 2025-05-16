from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from ..models import Matakuliah

@view_config(route_name='mk_home', renderer='templates/matakuliah.jinja2')
def mk_home(request):
    mks = request.dbsession.query(Matakuliah).all()
    return {'matakuliah': mks}

@view_config(route_name='mk_add_form', request_method='POST')
def mk_add_form(request):
    data = request.POST
    mk = Matakuliah(
        kode_mk=data.get('kode_mk'),
        nama_mk=data.get('nama_mk'),
        sks=int(data.get('sks')),
        semester=int(data.get('semester'))
    )
    request.dbsession.add(mk)
    return HTTPFound(location=request.route_url('mk_home'))

@view_config(route_name='mk_delete_form', request_method='POST')
def mk_delete_form(request):
    mk_id = request.matchdict['id']
    mk = request.dbsession.query(Matakuliah).get(mk_id)
    if mk:
        request.dbsession.delete(mk)
    return HTTPFound(location=request.route_url('mk_home'))
