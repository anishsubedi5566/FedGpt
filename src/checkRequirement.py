import pkg_resources

def check_requirements(requirements_file):
    with open(requirements_file, 'r') as file:
        lines = file.readlines()

    requirements = []
    for line in lines:
        if line.strip() and not line.startswith('#'):
            requirements.append(line.strip())

    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}

    for req in requirements:
        package, version = req.split('==')
        package = package.lower()
        if package in installed_packages:
            installed_version = installed_packages[package]
            if installed_version == version:
                print(f'{package}=={version} is installed')
            else:
                print(f'{package}=={version} is required but {package}=={installed_version} is installed')
        else:
            print(f'{package}=={version} is required but not installed')

# Specify the path to your requirements.txt file
check_requirements('requirements.txt')
