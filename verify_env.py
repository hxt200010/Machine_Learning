"""
Quick verification script to test installed AI/ML libraries.
Run with: python verify_env.py
"""

def test_imports():
    packages = [
        ("NumPy", "numpy", "__version__"),
        ("Pandas", "pandas", "__version__"),
        ("SciPy", "scipy", "__version__"),
        ("Matplotlib", "matplotlib", "__version__"),
        ("Seaborn", "seaborn", "__version__"),
        ("Scikit-Learn", "sklearn", "__version__"),
        ("TensorFlow", "tensorflow", "__version__"),
        ("PyTorch", "torch", "__version__"),
        ("Torchvision", "torchvision", "__version__"),
        ("Kaggle", "kaggle", "__file__"),
    ]

    print("=" * 60)
    print("Machine Learning Environment Verification")
    print("=" * 60)

    all_passed = True
    for name, module_name, attr in packages:
        try:
            mod = __import__(module_name)
            val = getattr(mod, attr, "Installed")
            print(f"[OK] {name:<15} : {val}")
        except Exception as e:
            all_passed = False
            print(f"[FAILED] {name:<15} : Error ({e})")

    print("-" * 60)
    try:
        import torch
        cuda_avail = torch.cuda.is_available()
        gpu_name = torch.cuda.get_device_name(0) if cuda_avail else "N/A"
        print(f"PyTorch CUDA Available: {cuda_avail} (Device: {gpu_name})")
    except Exception:
        pass

    try:
        import tensorflow as tf
        gpus = tf.config.list_physical_devices('GPU')
        print(f"TensorFlow GPUs Found : {len(gpus)}")
    except Exception:
        pass

    print("=" * 60)
    if all_passed:
        print("All machine learning packages are working properly!")
    else:
        print("Some packages encountered issues.")
    print("=" * 60)

if __name__ == "__main__":
    test_imports()
