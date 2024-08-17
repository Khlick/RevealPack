import toml

def get_version():
    with open("pyproject.toml", "r") as f:
        pyproject = toml.load(f)
    return pyproject["tool"]["poetry"]["version"]

def generate_mkdocs_yml():
    version = get_version()
    with open("mkdocs_template.yml", "r") as template_file:
        template = template_file.read()
    mkdocs_yml_content = template.replace("{{ version }}", version)
    with open("mkdocs.yml", "w") as mkdocs_file:
        mkdocs_file.write(mkdocs_yml_content)

if __name__ == "__main__":
    generate_mkdocs_yml()
