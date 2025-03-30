import os
import shutil
from pathlib import Path

# Import path constants for config management
from wandb_export.utils_config import PATH_CONFIGS, NAME_CONFIG_DEFAULT

def init_config():
    """Initializes the default config.yaml in the current repository."""
    config_dir = Path(PATH_CONFIGS)  # The location where the default config should be placed
    config_dir.mkdir(parents=True, exist_ok=True)

    # Define the path to the default config
    default_config_path = Path(__file__).parent / f"{PATH_CONFIGS}/{NAME_CONFIG_DEFAULT}"

    # Ensure default_config.yaml is in place
    default_config_dest = config_dir / NAME_CONFIG_DEFAULT
    if not default_config_dest.exists():
        shutil.copy(default_config_path, default_config_dest)
        print(f"Default config created at {default_config_dest}")
    else:
        print(f"Default config already exists at {default_config_dest}. Please remove/rename it and run this script again to recreate it.")

def main():
    init_config()

if __name__ == "__main__":
    main()
