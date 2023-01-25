import yaml
import argparse
from train import train
from test import test

def yaml_config_parser(config_file):
    with open(config_file, 'r') as stream:
        try:
            config = yaml.load(stream, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            print(exc)
    return config


if __name__=="__main__":
    #take in an argument for the config file path using argaparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='config.yaml', help='path to config file')
    parser.add_argument('--train', type=str, default=True, help='run training')
    parser.add_argument('--test', type=str, default=True, help='run testing')
    args = parser.parse_args()
    config = yaml_config_parser(f'/root/configs/{args.config}')
    print(config)
    if args.train:
        train(config)
    if args.test:
        test(config)    
