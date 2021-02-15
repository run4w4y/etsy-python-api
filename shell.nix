{ pkgs ? import <nixpkgs>, ... }:

pkgs.mkShell {
    name = "python-etsy-api";
    buildInputs = [];
}