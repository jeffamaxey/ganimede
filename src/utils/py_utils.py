def pkg_info(pkg, version):
    return f"{pkg}=={version}" if version and len(version) > 0 else pkg
