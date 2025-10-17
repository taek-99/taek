
## CNN

### MLP의 한계와 CNN의 한계
- MLP 는 각 픽셀을 숫자로 변환해 일렬로 나열해서 한계가 명확


### 주요 개념
- 입력 이미지
- 필터/ 커널
- 특징 맵

### 합성곱 신경망의 구성
- 합성곱층 -> 활성화 함수 적용 -> 풀링 층이 반복된 후에 완전히 상호 연결된 결합


```python

for epoch in range(2):  # 전체 데이터셋을 수차례(2회) 반복합니다.

    running_loss = 0.0  # 손실값을 누적하여 평균을 계산함, 2000 배치마다 평균계산한 후 초기화
    for i, data in enumerate(trainloader, 0):  # batchsize(4)단위로 데이터 가져오기
        # data로부터 inputs, labels 값 입력을 받은 후,
        inputs, labels = data

        # 변화도 매개변수(Gradient)를 0으로 만든 후
        optimizer.zero_grad()  # 새로운 배치 학습 전에 기울기 0으로 초기화(pytorch 의 기울기 누적 방지)

        # 학습 + 역전파 + 최적화
        outputs = net(inputs)  # 자동으로 __init__()과 forward()가 호출됨(__call__()메소드 때문)
        loss = criterion(outputs, labels) # 예측값과 레이블값의 차를 계산
        loss.backward() # 오차 역전파, 가중치의 기울기 계산
        optimizer.step() # 가중치 갱신

        # 통계 출력
        running_loss += loss.item()  # 개별 미니배치 손실 누적합
        if i % 2000 == 1999:    # 2000 배치마다 평균 손실 출력
            print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
            running_loss = 0.0

print('Finished Training')

```

