 echo "BUILD START"
 apt-get update && apt-get install -y python3-pip
 python3.9 -m pip install -r requirements.txt
 python3.9 manage.py collectstatic --noinput --clear
 echo "BUILD END"