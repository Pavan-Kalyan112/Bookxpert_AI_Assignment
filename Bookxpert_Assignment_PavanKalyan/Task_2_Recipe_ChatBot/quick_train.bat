@echo off
echo Setting up environment...
python -m venv venv
call venv\\Scripts\\activate

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r training/requirements-train.txt

echo.
echo Starting training...
cd training
python train_recipe_model.py

pause
