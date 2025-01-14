from importlib.metadata import version, PackageNotFoundError

def get_version():
    try:
        return version("RevealPack")
    except PackageNotFoundError:
        # If package is not installed, return version from __init__
        from . import __version__
        return __version__

def get_description():
    from . import __description__
    return __description__ 