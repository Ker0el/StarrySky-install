# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('config', 'config'), ('assets', 'assets')],
    hiddenimports=['backend.cai_backend', 'backend.gbe_backend', 'backend.pan_search_backend', 'backend.trainer_backend', 'rarfile', 'zhon.hanzi', 'fuzzywuzzy', 'PyQt6', 'qfluentwidgets', 'httpx', 'socksio', 'aiofiles', 'ujson', 'colorlog', 'vdf'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['IPython', 'ipykernel', 'ipywidgets', 'jupyter', 'jupyter_client', 'jupyter_core', 'nbformat', 'nbconvert', 'matplotlib', 'matplotlib_inline', 'mpl_toolkits', 'scipy', 'pandas', 'sklearn', 'sympy', 'networkx', 'torch', 'torchvision', 'torchaudio', 'functorch', 'transformers', 'diffusers', 'accelerate', 'timm', 'gradio', 'datasets', 'huggingface_hub', 'safetensors', 'tokenizers', 'pygame', 'altair', 'narwhals', 'polars', 'duckdb', 'dask', 'ibis'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='StarrySkyInstall',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets/icon.ico'],
)
