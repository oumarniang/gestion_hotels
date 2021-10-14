Gestion environnement
-----------------------------

conda create -n mypython3 python=3
conda activate mypython3
conda deactivate

-------------------------------

cd development/projects/18_projet-oumar/web/mon_app
conda activate tf

export FLASK_APP=project/__init__
export FLASK_DEBUG=1
flask run

pip install -r requirements.txt 

Installer requirements
-----------------------------------
pip install -r requirements.txt

Générer requirements
---------------------------
pip list –format=freeze > requirements.txt



-----------------------------------
pip install Flask-SQLAlchemy

conda install flask
conda install flask_sqlalchemy
conda install Flask-SQLAlchemy
pip install flask_login
conda install wtforms



conda list -e > requirements.txt
