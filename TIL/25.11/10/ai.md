이론 출제 범위: MLP, 데이터 생성 방법, 토큰화와 임베딩
이론 + 코드 출제 범위: EDA, 선형회귀, 리니어프로빙

위 범위 내에서 총 3문제가 출제됨
각 개념은 타인에게 설명할 수 있을 정도로 명확히 이해해야 함
기존에 보았던 문항에 대해 오답이 될 수 있었던 부분에 대해 다시 고민해보고 추가 학습이 필요
출제 범위 내 주요 개념을 타인에게 설명할 수 있도록 내용을 이해해야 함
이론 + 코드 출제 범위는 소스코드까지 공부해야함


# 실습
## EDA
- 데이터셋 불러오기
- drop
    - 해당 컬럼 제거
- filtered
    - 조건부 필터링

```python
df_sub = df.drop(columns=['sepal_length', 'sepal_width']) # drop = 시리즈 제거!
df_filtered = df_sub[df_sub["petal_width"] >= 0.3] # 필터링
df_sub.head(10)
```

``` python
df = sns.load_dataset("")
df.head()
```

- 변수 간 상간관계
```python
import seaborn as sns
sns.regplot(data=df, x="변수명", y="변수명", scatter_kws={'alpha': 0.6}) ## alpha는 투명도
print()
```

- 히트맵
``` python
import numpy as np
import seaborn as sns

# 상관계수 행렬 계산
corr = df.corr(numeric_only=True)

# 삼각형 마스크 만들기
mask = np.triu(np.ones_like(corr, dtype=bool))

# 히트맵 출력
sns.heatmap(corr, mask=mask, annot=True, cmap="coolwarm", linewidth=1)
print()
```

- pair plot(추세선)
```python
import matplotlib.pyplot as plt

sns.pairplot(df[['mpg', 'weight', 'acceleration']], corner=True, kind='reg', plot_kws={'line_kws': {'color' : 'red'}})
```

## 선형회귀
- 선형회귀 모델은 추세선 방정식을 의미한다
- 이 추세선을 찾아내면, 미래 데이터 예측 가능



```python

tips = sns.load_dataset('tips')
sns.regplot(x="total_bill", y='tips', data=tips, ci=None, line_kws={'color' : 'red'})

```


## Linear Probing
- 다른 파라미터값은 건드리지 않고 마지막 Layer 추가


# 이론

## 토큰화 임베딩
- 문장은 모델에 바로 대입 X
- 각 토큰 단위로 글자를 자르고, 이를 숫자로 변환
- 각 수를 벡터공간의 벡터값으로 치환
- 같은 의미를 가진 단어는 유사한 벡터값을 가지도록 맵핑해주는 임베딩 모델

## MLP
- 입력층 → 은닉층 → 출력층으로 여러층으로 구성된 구성된 다층 신경망 모델
- y = Wx + b 같은 단순 선형식 대신, 여러 층과 비선형 활성화 함수를 통해 복잡한 패턴을 학습할 수 있다.
- 신경망으로 선형회귀선을 그리는것

## ReLu 함수
- 활성화 함수 중 하나
- 음수는 0, 양수는 그대로 통과
- 기울기 소실 문제를 줄여 학습 안전화
- 직선 조합으로 표현 불가능한 복잡한 함수도 표현 가능