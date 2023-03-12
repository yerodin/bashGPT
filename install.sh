#!/bin/bash

function main() {
    python3 -m pip install -r requirements.txt || die
    apt install rustc
    mkdir /var/command-not-found
    mkdir /usr/share/command-not-found-bashGPT
    cp -r CommandNotFound/share/* /usr/share/command-not-found-bashGPT || die
    cp CommandNotFound/etc/zsh_command_not_found /etc/ || die
    cp CommandNotFound/etc/50command-not-found /etc/apt/apt.conf.d || die
    cp -r CommandNotFound/runtime.d/command-not-found.rtupdate /usr/share/python3/runtime.d/ || die
    ln -s /usr/share/command-not-found-bashGPT/command-not-found /usr/bin/command-not-found
    ln -s /usr/share/command-not-found-bashGPT/command-not-found /usr/sbin/command-not-found
    ln -s /usr/share/command-not-found-bashGPT/cnf-update-db /usr/lib/cnf-update-db
    ln -s /usr/share/command-not-found-bashGPT/command-not-found /usr/lib/command-not-found
    sed -i 's/command-not-found -- "$1"/command-not-found -- "$@"/g' /etc/bash.bashrc || die
    source /etc/bash.bashrc || die
    set -e

    if command -v py3compile >/dev/null 2>&1; then
        py3compile -p command-not-found /usr/share/command-not-found-bashGPT
    fi
    if command -v pypy3compile >/dev/null 2>&1; then
        pypy3compile -p command-not-found /usr/share/command-not-found-bashGPT || true
    fi
}
function die() {
    echo "exiting due to error.."
    exit 1
}

main