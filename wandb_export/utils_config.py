import os
import sys

# Constants for the config path and default config name
PATH_CONFIGS : str = "configs_wandb_export"
NAME_CONFIG_DEFAULT : str = "config_default.yaml"

def assert_config_dir_exists():
    """Check if the configs_wandb_export directory exists."""
    if os.path.exists(PATH_CONFIGS) and os.path.isdir(PATH_CONFIGS):
        return
    else:
        print(f"Error: Config directory '{PATH_CONFIGS}' does not exist.")
        print("To initialize the config, please run: 'wandb-export-init-config' before.")
        print("Then you can run 'wandb-export' with eventual Hydra overrides (config name, config overrides).")
        print("See 'wandb-export --help' for more information.")
        sys.exit(1)