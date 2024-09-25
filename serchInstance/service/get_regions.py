import boto3
import json

def get_regions():
    # boto3를 사용하여 리전 목록 가져오기
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions(AllRegions=False)
    regions = response['Regions']

    # 리전 코드를 리스트로 반환
    return [region['RegionName'] for region in regions]