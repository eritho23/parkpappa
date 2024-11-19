{
    inputs = {
        # Unstable Nixpkgs
        nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";

        # Flake utils
        utils.url = "github:numtide/flake-utils";
    };

    outputs = {self, nixpkgs, ...}: {

    };
}