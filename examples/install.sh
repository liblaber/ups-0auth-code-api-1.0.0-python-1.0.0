python -m venv .venv
. .venv/bin/activate
pip install build
python -m build --outdir dist ../
pip install dist/ups_0auth_auth_code-1.0.0-py3-none-any.whl --force-reinstall
