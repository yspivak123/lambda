import boto3

def lambda_client():
    aws_lambda = boto3.client('lambda', region='us-east-1')
    """ :type : pyboto3.lambda """
    return aws_lambda

def iam_clent():
    iam = boto3.client('iam')
    """ :type : pyboto3.iam """
    return iam

def create_access_policy_for_lambda():
