{
  inputs = {
    # Unstable Nixpkgs
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";

    # Flake utils
    utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    utils,
    ...
  }:
    utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {inherit system;};
      version = "0.0.0-dev";
    in {
      devShells.default = pkgs.mkShell {
        packages = with pkgs; [
          nodejs_22
          nodePackages.npm
          ripgrep
          fzf
          mdcat
          bat
          alejandra
          nil
        ];
      };

      packages = {
        frontend = pkgs.buildNpmPackage {
          pname = "parkpappa-frontend";
          inherit version;
          src = ./frontend/.;

          npmDepsHash = "sha256-H/OhyZ+VlZQk3/SKnJ7Fz+PZ8YOoNxqbI5INO8NmVaY=";
          # npmDepsHash = pkgs.lib.fakeHash;

          buildPhase = ''
            runHook preBuild
            npm --loglevel=verbose run build --offline
            runHook postBuild
          '';

          installPhase = ''
            runHook preInstall
            mkdir -p $out
            cp -r build/* $out
            runHook postInstall
          '';
        };
      };
    });
}
