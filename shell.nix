{ pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
    packages = with pkgs; [nodejs_22 nodePackages.npm ripgrep fzf];
}
