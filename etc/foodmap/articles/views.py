# app/views.py
import requests
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse

KAKAO_LOCAL_URL = "https://dapi.kakao.com/v2/local/search/category.json"


def index(request):
    # 단순 입력 폼
    return render(request, "articles/index.html")

def restaurants(request):
    # GET 파라미터로 위도/경도/반경 입력받기 (JS 없이)
    y = request.GET.get("lat")   # 위도
    x = request.GET.get("lng")   # 경도
    radius = request.GET.get("radius", "1000")  # 기본 1km
    size = request.GET.get("size", "10")        # 10개

    if not x or not y:
        return HttpResponseBadRequest("lat(위도), lng(경도) 파라미터가 필요합니다.")

    headers = {"Authorization": f"KakaoAK {settings.KAKAO_API_KEY}"}
    params = {
        "category_group_code": "FD6",  # 음식점
        "x": x, "y": y,
        "radius": radius,              # 0~20000
        "size": size,                  # 1~15
        "sort": "distance",
    }

    r = requests.get(KAKAO_LOCAL_URL, headers=headers, params=params, timeout=5)
    r.raise_for_status()
    raw = r.json()

    # 템플릿에 넘길 최소 필드 가공
    items = []
    for d in raw.get("documents", []):
        items.append({
            "name": d.get("place_name"),
            "addr": d.get("road_address_name") or d.get("address_name"),
            "phone": d.get("phone"),
            "distance_m": int(d.get("distance") or 0),
            "lat": d.get("y"),
            "lng": d.get("x"),
            "url": d.get("place_url"),
            "category": d.get("category_name"),
        })

    context = {
        "count": len(items),
        "items": items,
        "lat": y, "lng": x, "radius": radius,
    }
    return render(request, "articles/restaurant.html", context)


def best(request):
    dish = None
    # 필터가 하나라도 넘어오면 추천을 보여주자 (프로토타입)
    if request.GET:  
        dish = "삼겹살"
    return render(request, 'articles/best.html', {"dish":dish})