import os
import sys
from pathlib import Path

def setup_project():
    # Create necessary directories
    base_dir = Path(__file__).parent
    dirs = [
        base_dir / 'resources' / 'images',
        base_dir / 'resources' / 'sounds',
    ]
    
    for dir_path in dirs:
        dir_path.mkdir(parents=True, exist_ok=True)
    
    # Create default resources
    sys.path.append(str(base_dir))
    from src.utils.create_default_resources import create_default_images
    create_default_images()
    
    print("Project setup completed successfully!")

if __name__ == "__main__":
    setup_project()