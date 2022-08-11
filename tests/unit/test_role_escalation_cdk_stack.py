import aws_cdk as core
import aws_cdk.assertions as assertions

from role_escalation_cdk.role_escalation_cdk_stack import RoleEscalationCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in role_escalation_cdk/role_escalation_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = RoleEscalationCdkStack(app, "role-escalation-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
