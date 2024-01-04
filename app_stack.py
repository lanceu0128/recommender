from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_lambda_python_alpha as _lambda_python,
)
from aws_cdk.aws_apigateway import (
    LambdaIntegration,
    RestApi,
)
from constructs import Construct


class AwsCdkFlaskStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        api = RestApi(self, "flask-api", rest_api_name="flask-api")

        flask_lambda = _lambda_python.PythonFunction(
            self,
            "recommender",
            function_name="flask-lambda",
            entry="lambdas",
            index="app.py",
            handler="handler",
            runtime=_lambda.Runtime.PYTHON_3_8,
            timeout=Duration.seconds(30),
        )

        root_resource = api.root

        any_method = root_resource.add_method(
            "ANY",
            LambdaIntegration(flask_lambda)
        )
