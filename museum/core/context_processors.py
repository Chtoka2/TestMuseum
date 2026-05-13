from .models import MuseumInfo

def museum_info(request):
    try:
        info = MuseumInfo.load()
        return {
            'museum_name': info.name,
            'museum_description': info.description,
        }
    except:
        return {
            'museum_name': 'Музей школы 22',
            'museum_description': '',
        }