# [learneveryword](https://twitter.com/learneveryword)

Learn every word in the English language. Task will complete in 2022.

### Tech stack

- Python
- S3
- AWS Lambda

### Installation

1. Make a `config.py` in `bot/` that looks like this:

```
twitter = dict(
  key = '',
  secret = '',
  token = '',
  token_secret = '',
)

aws = dict(
  key = '',
  secret = '',
  bucket = 'learneveryword',
  data = 'data.json',
)
```

2. Upload `data.json` in your `aws.bucket`.

3. Zip `bot/` contents (not the directory). Upload to AWS Lambda.

4. Set whatever schedule you want it to run on (see Lambda docs).

5. ???

6. Profit.
