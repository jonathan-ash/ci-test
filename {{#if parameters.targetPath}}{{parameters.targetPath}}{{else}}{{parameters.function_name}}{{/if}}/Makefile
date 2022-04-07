AWS_DEFAULT_REGION=1
AWS_ACCOUNT=123456

authenticate:
	saml2aws login --skip-prompt --profile={{cookiecutter.function_name}} --role=arn:aws:iam::${AWS_ACCOUNT}:role/ADFS-EnterpriseAdmin --region eu-west-1 --force

validate: authenticate
	AWS_DEFAULT_REGION=eu-west-1 sam validate -t template.yaml --profile {{cookiecutter.function_name}}

## Used to build pip dependencies
build:
	sam build --use-container --profile {{cookiecutter.function_name}}

.PHONY: deploy
deploy: authenticate validate build
	sam deploy --profile {{cookiecutter.function_name}} --parameter-overrides --confirm-changeset  --no-fail-on-empty-changeset--region ${AWS_DEFAULT_REGION}

## To invoke lambda function:  aws lambda invoke --function-name "Account{{cookiecutter.function_name}}" --endpoint-url "http://127.0.0.1:3001" --no-verify-ssl out.txt
.PHONY: local
local: build
	sam local invoke --profile {{cookiecutter.function_name}} --region eu-west-1 -e event.json --debug
