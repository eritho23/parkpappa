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
      sweref-lib = pkgs.python312Packages.buildPythonPackage rec {
        pname = "sweref99";
        version = "0.2";
        format = "setuptools";

        pythonImportsCheck = ["sweref99"];

        src = pkgs.fetchPypi {
          inherit pname version;
          hash = "sha256-0Ae359fEjpv4cZY2dDCb1kvZr4Dkj2K0bMaNextMtRM=";
        };
      };
      python3WithPkgs = pkgs.python312.withPackages (po: with po; [flask requests pyproj schedule werkzeug python-dotenv gunicorn sweref-lib]);
    in rec {
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
          nodePackages.prettier
          python3WithPkgs
          ripgrep
        ];
      };

      packages = rec {
        frontend-src = pkgs.stdenvNoCC.mkDerivation {
          pname = "parkpappa-src-for-ci";
          inherit version;
          src = pkgs.lib.cleanSource ./frontend;

          installPhase = ''
            runHook preInstall
            mkdir -p $out
            cp -r ./* $out
            runHook postInstall
          '';
        };

        frontend = pkgs.buildNpmPackage {
          pname = "parkpappa-frontend";
          inherit version;
          src = pkgs.lib.cleanSource ./frontend/.;

          npmDepsHash = "sha256-ZEIr3Z0Jo2E+S1UQWNTWXWn9HBifWpb+lKRcpVC3m5s=";
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
      actions-frontend-formatting = pkgs.writeShellScriptBin "actions-frontend-formatting" ''
        set -eu
        echo Checking formatting on frontend
        ${pkgs.nodePackages.prettier}/bin/prettier --check ${pkgs.lib.cleanSource ./frontend}
      '';
      apps.actions-frontend-formatting = utils.lib.mkApp {drv = actions-frontend-formatting;};
      actions-frontend-check = pkgs.writeShellScriptBin "actions-frontend-check" ''
        set -eu
        echo Checking Svelte using npm run check
        cd frontend

        ${pkgs.nodePackages.npm}/bin/npm install
        ${pkgs.nodePackages.npm}/bin/npm run check

      '';
      apps.actions-frontend-check = utils.lib.mkApp {drv = actions-frontend-check;};
    });
}
