import json
from serchInstance.persistant.sqlite_db_manager import save_search_history, fetch_search_history
from service.get_regions import get_regions
from service.search_price import get_ec2_instance_price
def lambda_handler(event, context):

    # 경로별 분기 처리

    path = event.get('path')
    if path == '/getRegions':
        # AWS 리전 정보 가져오기
        regions = get_regions()
        return {
            'statusCode': 200,
            'body': {"regions": regions},
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    if path == '/getPrice':
        # 가격정보 가져오기
        price = get_ec2_instance_price()
        return {
            'statusCode': 200,
            'body': {"price": price},
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
            
    if path == '/saveHistory':
        # 검색 기록을 저장
        body = json.loads(event['body'])
        instance_type = body.get('instanceType')
        region = body.get('region')
        price = body.get('price')

        # 필수 값 검증
        if not instance_type or not region or not price:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': '인스턴스타입, 리전, 가격 정보 다시 확인'})
            }

        # 검색 기록 저장
        save_search_history(instance_type, region, price)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': '검색이력 저장완료'})
        }

    elif path == '/searchHistory':
        # 검색 기록을 조회
        search_history = fetch_search_history()

        return {
            'statusCode': 200,
            'body': json.dumps(search_history)
        }

    else:
        # 정의되지 않은 경로 처리
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Not Found'})
        }