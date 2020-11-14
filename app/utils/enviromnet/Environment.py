from app.utils.resource import ResourceUtil


def is_development():
    return ResourceUtil.get_resource_file('environment.yml')['environment']['production']
