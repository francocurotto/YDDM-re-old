import yaml

def get_library():
    from settings import library_path
    return yaml.full_load(open(library_path))
