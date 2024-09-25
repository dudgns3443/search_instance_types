async function fetchRegions() {
    try {
        const response = await apiRequest('/getRegions');
        const regions = await response.json().regions;
        const selectBox = document.getElementById('region');
        
        // 셀렉트 박스 초기화
        selectBox.innerHTML = '';

        // 기본 옵션 추가
        const defaultOption = document.createElement('option');
        defaultOption.value = '';
        defaultOption.text = 'Select a region';
        selectBox.appendChild(defaultOption);

        // 리전 옵션 추가
        regions.forEach(region => {
            const option = document.createElement('option');
            option.value = region;
            option.text = region;
            selectBox.appendChild(option);
        });
    } catch (error) {
        console.error('Error fetching regions:', error);
    }
}

// 페이지가 로드될 때 리전 정보를 가져옴
window.onload = function() {
    fetchRegions();
};

document.getElementById('searchBtn').addEventListener('click', async function () {
    const region = document.getElementById('region').value;
    const instanceType = document.getElementById('instanceType').value;

    if (!instanceType) {
        alert("Please enter an EC2 instance type.");
        return;
    }
    body = {
        "region": region,
        "instanceType": instanceType
    }
    // Fetch the EC2 price (API or dummy data in this example)
    const price = await apiRequest('/getPrice',"GET",body);

    // Display result
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = ` ${instanceType} 타입의 ${region}지역 시간당 가격: $${price}`;

    // Save the search to the database (server-side handling)
    await saveSearchHistory(region, instanceType, price);
});

document.getElementById('historyBtn').addEventListener('click', async function () {
    // Fetch the search history from the server
    const history = await fetchSearchHistory();

    // Populate the history table
    const historyTable = document.getElementById('historyTable');
    const tbody = historyTable.querySelector('tbody');
    tbody.innerHTML = '';  // Clear any existing rows

    history.forEach(record => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${record.date}</td><td>${record.instanceType}</td><td>${record.region}</td><td>$${record.price}</td>`;
        tbody.appendChild(row);
    });

    historyTable.style.display = 'table';
});


// Dummy function to simulate saving search history to the database
async function saveSearchHistory(region, instanceType, price) {
    body = {
        "region": region,
        "instanceType": instanceType,
        "price": price
    }
    return new Promise((resolve) => {
        apiRequest('/savehistory','POST',body);
        console.log(`Saving to DB: ${region}, ${instanceType}, $${price}`);
        resolve();
    });
}

// Dummy function to simulate fetching search history from the database
async function fetchSearchHistory() {
    return new Promise((resolve) => {
        const history = apiRequest('/searchHistory')
        resolve(dummyHistory);
    });
}

async function apiRequest(url, method = 'GET', body = null) {
    try {
        const request_url = 'http://0.0.0.0' + url
        const options = {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            }
        };

        if (body) {
            options.body = JSON.stringify(body);
        }

        const response = await fetch(request_url, options);
        
        if (!response.ok) {
            throw new Error(`Error: ${response.status} - ${response.statusText}`);
        }

        return await response.json();  // JSON 형식으로 응답 처리
    } catch (error) {
        console.error('API 요청 중 에러가 발생했습니다:', error);
        throw error;
    }
}