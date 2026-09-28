pkgname = "dasel"
pkgver = "3.11.2"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/dasel"]
hostmakedepends = ["go"]
pkgdesc = "CLI tool for querying, modifying, and transforming data structures"
license = "MIT"
url = "https://github.com/TomWright/dasel"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5471fe33b28c98efed2b1a13431ed24097785f56a24dc9fb15e37b1e266446e1"


def post_build(self):
    with open(self.cwd / "dasel.1", "w") as f:
        self.do(f"{self.make_dir}/dasel", "man", stdout=f)
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"dasel.{shell}", "w") as f:
            self.do(f"{self.make_dir}/dasel", "completion", shell, stdout=f)


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("dasel.1")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"dasel.{shell}", shell)
