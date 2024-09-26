다음과 같은 디렉토리 구성을 가지고 있습니다.
```
search_instance_types
├── static/
│   ├── index.html                       // 화면코드
│   └── searchInstanceTypePrice.js       // 스크립트 코드
├── serchInstace/     // python 으로 작성된 코어로직
│   ├── config/       // 필요한 환경 변수 상수 선언
│   ├── service/      // 비즈니스 로직이 수행되는 곳
│   ├── persistent/   // DB 관련 쿼리를 수행하는 영속성 layer
│   └── lambda_function.py     // 람다 코드 핸들러
├── mydatabase.db              // embedded DB
└── README.md
```

static/ 디렉토리의 코드들은 화면단 코드로 S3로 배포되어 S3를 통해 호스팅됩니다. 해당 서비스의 트래픽이 많을 경우 s3앞 단에 cloudfront를 구성하는 것을 추천드립니다.

serchInstance/ 디렉토리의 python 코드들은 lambda를 통해서 서비스됩니다. static/ 디렉토리와 같이 S3로 zip파일 형태로 배포되며 배포이후 lambda는 해당 zip파일로 코드를 최신화합니다.

mydatabase.db 는 현재 empty 파일이며 위의 코드들이 배포되는 같은 s3로 배포되는 것을 추천합니다.
