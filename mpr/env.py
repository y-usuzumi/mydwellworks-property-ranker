# MOD_SPATIALITE_PATH = '/usr/lib/mod_spatialite.so'
import os
import subprocess
import shutil


def get_os():
    if shutil.which('nix-store'):
        return 'nixos'
    return None


def get_mod_spatialite_name():
    os_name = get_os()
    if os_name == 'nixos':
        path = subprocess.check_output([
            'nix-build',
            '<nixpkgs>',
            '--no-build-output',
            '-A',
            'libspatialite'
        ]).strip().decode('utf-8')
        return os.path.join(path, 'lib', 'mod_spatialite.so')
    return 'mod_spatialite'


def get_db_connstr():
    return "sqlite:///mpr.db"
