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
      python3WithPkgs = pkgs.python312.withPackages (po: with po; [flask requests pyproj]);
    in {
      devShells.default = pkgs.mkShell {
        packages = with pkgs; [
          act
          alejandra
          bat
          fzf
          mdcat
          nil
          nodejs_22
          nodePackages.npm
          python3WithPkgs
          ripgrep
        ];
      };

      packages = rec {
        frontend = pkgs.buildNpmPackage {
          pname = "parkpappa-frontend";
          inherit version;
          src = pkgs.lib.cleanSource ./frontend/.;

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

        frontend-docker = pkgs.dockerTools.streamLayeredImage rec {
          name = "parkpappa-frontend";
          tag = version;
          config.Cmd = ["${pkgs.nodejs_22}/bin/node" frontend];
          config.exposedPorts = {
            "3000/tcp" = {};
          };
        };

        backend = pkgs.stdenv.mkDerivation {
            name = "parkpappa-backend";
            inherit version;
            src = pkgs.lib.cleanSource ./backend/.;

            installPhase = ''
              mkdir -p $out 
              cp *.py $out
            '';
        };
      };
    });
}
