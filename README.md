Execute the following commands:
python3 -m pip install --upgrade virtualenv
python3 -m venv venv-test-pypi
source venv-test-pypi/bin/activate
pip install -i https://test.pypi.org/simple/ BMI==0.0.1

from BMI import BMI_calc
BMI_calc(‘file_name’)
