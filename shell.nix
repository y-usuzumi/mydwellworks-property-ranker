{ pkgs ? import <nixpkgs> {} }:
with pkgs;
let
  pythonEnv = python38.withPackages (ps: [
    ps.sqlalchemy
    ps.geoalchemy2
    ps.requests
    ps.pyyaml
  ]);
in mkShell {
  buildInputs = [
    libspatialite
    sqlite
    pythonEnv
  ];
}
