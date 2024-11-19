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
    });
}
