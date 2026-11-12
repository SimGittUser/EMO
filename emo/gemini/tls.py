"""Making HTTPS work on Pythons that ship without root certificates."""

import importlib
import importlib.util
import ssl

CA_BUNDLES = (
    "/etc/ssl/cert.pem",  # macOS, Alpine, BSD
    "/etc/ssl/certs/ca-certificates.crt",  # Debian, Ubuntu, Raspberry Pi OS
    "/etc/pki/tls/certs/ca-bundle.crt",  # Fedora, RHEL
    "/etc/ssl/ca-bundle.pem",  # openSUSE
)


def _bundles() -> list[str]:
    """Places a set of trusted root certificates might be found."""
    if importlib.util.find_spec("certifi") is None:
        return list(CA_BUNDLES)
    return [importlib.import_module("certifi").where(), *CA_BUNDLES]


def tls_context() -> ssl.SSLContext:
    """An HTTPS context that can actually verify Google's certificate.

    Some Python builds (notably the python.org installer for macOS) ship
    without any trusted roots, so every HTTPS request fails with
    CERTIFICATE_VERIFY_FAILED. Verification always stays on; if Python's own
    store is empty we borrow the roots from certifi or from the system.
    """
    ctx = ssl.create_default_context()
    if ctx.cert_store_stats().get("x509_ca"):
        return ctx
    for path in _bundles():
        try:
            ctx.load_verify_locations(cafile=path)
        except (OSError, ssl.SSLError):
            continue
        if ctx.cert_store_stats().get("x509_ca"):
            break
    return ctx
