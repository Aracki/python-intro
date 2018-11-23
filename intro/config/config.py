import yaml


def get_config():
    with open("aws-config.yml", 'r') as stream:
        try:
            conf = yaml.load(stream)
            return conf
        except yaml.YAMLError as exc:
            print(exc)
            return dict()
