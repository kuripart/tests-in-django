# Demo Tests in Djano

### 1. Using coverage

#### Installation
```bash
python3.7 -m pip install coverage
```

#### Execution
> Run Tests
```bash
coverage run manage.py test testapp01 -v 2

test_person_creation (testapp01.tests.test_models.Person) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
```
> Get report
```bash
% coverage report -m
Name                                   Stmts   Miss  Cover   Missing
--------------------------------------------------------------------
manage.py                                 12      2    83%   11-12
test01/__init__.py                         0      0   100%
test01/settings.py                        18      0   100%
test01/urls.py                             3      0   100%
testapp01/__init__.py                      0      0   100%
testapp01/admin.py                         1      0   100%
testapp01/apps.py                          3      0   100%
testapp01/migrations/0001_initial.py       5      0   100%
testapp01/migrations/__init__.py           0      0   100%
testapp01/models.py                        6      0   100%
testapp01/tests/__init__.py                0      0   100%
testapp01/tests/test_models.py             7      0   100%
--------------------------------------------------------------------
TOTAL                                     55      2    96%
```
> Generate an HTML [report](htmlcov)
```bash
coverage html
```
