## Complete tasks 1-6 to activate live RNG s3 cloud data storage

##

1. Install requirements

   > pip install -r requirements.txt

2. Run RNG .txt file writer:

   > python RNGActivateMultiV3

3. Run server

   > python dev-server.py or python production-server.py

4. To continuosly update s3 cloudstorage with new trueRNG data and delete old data

   > python .s3/data_update.py

## Automate git workflow (deprecated)

1. Run git commit/push workflow automation in terminal of local repo

   > python ./github/commit.py

2. Run git pull workflow automation in terminal of deployed app

   > python ./github/pull-changes.py

3. Run tests:
   > pytest -v --cov

##

-> Errors

1.  error: pytest -v --cov  
    pytest : The term 'pytest' is not
    recognized as the name of a cmdlet,  
    function, script file, or operable  
    program. Check the spelling of the name,  
    or if a path was included, verify that  
    the path is correct and try again.
    At line:1 char:1

- pytest -v --cov
- ```
    + CategoryInfo          : ObjectNotFo
   und: (pytest:String) [], CommandNotFo
  undException
    + FullyQualifiedErrorId : CommandNotF
   oundException
  ```

Workaround python -m pytest -v --cov
