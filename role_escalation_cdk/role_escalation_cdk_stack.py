from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_lambda
)
from constructs import Construct

class RoleEscalationCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        example_lambda = aws_lambda.Function(
            self,
            "EscalationLambda",
            handler="app.handler",
            architecture=aws_lambda.Architecture.ARM_64,
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            code=aws_lambda.Code.from_asset('functions/escalation')
        )

        example_lambda.role.add_managed_policy(
            policy=iam.ManagedPolicy.from_aws_managed_policy_name(
                managed_policy_name="AdministratorAccess"
            )
        )
