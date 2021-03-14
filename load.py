from ruamel.yaml import YAML


def loadcfg(cfg:str)->dict:
    yaml = YAML()
    with open(cfg, "r") as f:
        cfg = yaml.load(f)
        return cfg