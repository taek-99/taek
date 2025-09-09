# views.py
from django.shortcuts import render
from django.http import HttpResponse
import threading, time
from datetime import datetime, timedelta

# ===== 전역 상태 =====
_worker_thread = None
_stop_event = threading.Event()
# ====================

def _click_bot(x: int, y: int, target_dt: datetime,
               pre_seconds: float = 1.0,  # T-1초부터
               post_seconds: float = 2.0  # T+2초까지
               ):
    """
    예약 시각(target_dt) 1초 전부터 가능한 한 빠르게 (x,y)를 클릭한다.
    """
    import pyautogui  # 로컬에서만 필요
    pyautogui.FAILSAFE = True   # 화면 좌상단(0,0)으로 마우스 보내면 긴급 중지
    pyautogui.PAUSE = 0         # 각 동작 사이 기본 지연 제거

    # 1) T - pre_seconds 까지 느슨히 대기
    start_phase_dt = target_dt - timedelta(seconds=pre_seconds)
    while not _stop_event.is_set():
        now = datetime.now()
        if now >= start_phase_dt:
            break
        # 멀리 남았으면 느슨히, 가까우면 촘촘히
        remaining = (start_phase_dt - now).total_seconds()
        time.sleep(0.2 if remaining > 1.0 else 0.005)

    if _stop_event.is_set():
        return

    # 2) 초고속 클릭 구간: [T - pre, T + post]
    end_dt = target_dt + timedelta(seconds=post_seconds)

    # 미리 커서 이동 (클릭 정확도 ↑)
    try:
        pyautogui.moveTo(x, y)
    except Exception:
        pass

    # 가능한 한 빠르게 클릭 루프
    # 파이썬/OS 한계상 완전 무한속도는 아니지만, PAUSE=0으로 최대한 빠르게 갑니다.
    while not _stop_event.is_set() and datetime.now() < end_dt:
        pyautogui.click(x, y)

    # 끝
    return


def click_view(request):
    """
    폼에서 X,Y, 예약시각(로컬) 입력 → 시작 누르면 T-1초부터 초고속 좌표 클릭
    """
    global _worker_thread, _stop_event

    status_text = "대기 중"

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "start":
            # 1) 파라미터 파싱
            try:
                x = int(request.POST.get("x", "").strip())
                y = int(request.POST.get("y", "").strip())
            except Exception:
                return HttpResponse("X, Y는 정수로 입력하세요.", status=400)

            target_local = request.POST.get("target_time", "").strip()
            if not target_local:
                return HttpResponse("예약 시각을 입력하세요.", status=400)

            # datetime-local: "YYYY-MM-DDTHH:MM" 또는 "YYYY-MM-DDTHH:MM:SS"
            if len(target_local) == 16:
                target_local += ":00"
            try:
                target_dt = datetime.strptime(target_local, "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                return HttpResponse("시간 형식이 올바르지 않습니다. 예) 2025-09-10T10:00", status=400)

            # 2) 기존 스레드 정리
            if _worker_thread and _worker_thread.is_alive():
                _stop_event.set()
                _worker_thread.join(timeout=2)

            # 3) 새 작업 시작
            _stop_event = threading.Event()
            _worker_thread = threading.Thread(
                target=_click_bot,
                args=(x, y, target_dt),
                daemon=True
            )
            _worker_thread.start()
            status_text = f"실행 중: 좌표({x},{y}) / {target_dt.strftime('%Y-%m-%d %H:%M:%S')}"

        elif action == "stop":
            if _worker_thread and _worker_thread.is_alive():
                _stop_event.set()
                _worker_thread.join(timeout=2)
            status_text = "중지됨"

    # 상태 표시
    if _worker_thread and _worker_thread.is_alive():
        status_text = "실행 중 (클릭 스케줄 대기/진행 중)"

    return render(request, "click_form.html", {"status": status_text})
