pkgname = "sd"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", "sd-cli"]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Find and replace CLI"
license = "MIT"
url = "https://github.com/chmln/sd"
source = f"https://github.com/chmln/sd/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "defdce484f8c92f265e1282490572575028967c2c55d356111d1e49a3ea9a88e"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/sd")
    self.install_man("gen/sd.1")
    self.install_completion("gen/completions/sd.bash", "bash")
    self.install_completion("gen/completions/sd.fish", "fish")
    self.install_completion("gen/completions/_sd", "zsh")
    self.install_license("LICENSE")
