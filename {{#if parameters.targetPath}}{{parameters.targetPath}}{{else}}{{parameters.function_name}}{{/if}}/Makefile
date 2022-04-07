AWS_DEFAULT_REGION={{ parameters.aws_region }}
AWS_ACCOUNT={{ parameters.aws_account_id }}

authenticate:
	saml2aws login --skip-prompt --profile={{ parameters.function_name }} --role=arn:aws:iam::${AWS_ACCOUNT}:role/ADFS-EnterpriseAdmin --region eu-west-1 --force

validate: authenticate
	AWS_DEFAULT_REGION=eu-west-1 sam validate -t template.yaml --profile {{ parameters.function_name }}

## Used to build pip dependencies
build:
	sam build --use-container --profile {{ parameters.function_name }}

.PHONY: deploy
deploy: authenticate validate build
	sam deploy --profile {{ parameters.function_name }} --parameter-overrides --confirm-changeset  --no-fail-on-empty-changeset--region ${AWS_DEFAULT_REGION}

## To invoke lambda function:  aws lambda invoke --function-name "Account{{ parameters.function_name }}" --endpoint-url "http://127.0.0.1:3001" --no-verify-ssl out.txt
.PHONY: local
local: build
	sam local invoke --profile {{ parameters.function_name }} --region eu-west-1 -e event.json --debug