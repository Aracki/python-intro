import yaml


def get_config():
    with open("prop.yaml", 'r') as stream:
        try:
            conf = yaml.load(stream)
            return conf
        except yaml.YAMLError as exc:
            print(exc)
            return dict()
