# 현재 시간을 반환하는 함수
def get_current_time():
    from datetime import datetime
    return datetime.now()

# 오늘 할 일을 반환하는 함수
def get_todays_tasks():
    # 이 함수는 실제 애플리케이션에서는 데이터베이스나 다른 소스에서 할 일을 가져올 것입니다.
    # 여기서는 예시 데이터를 반환합니다.
    return ["오전 9시 팀 미팅", "오후 2시 고객사 미팅 준비", "오후 4시 주간 보고서 작성"]

# mbti를 판단하는 함수
def get_mbti():
    # 이 함수는 실제 애플리케이션에서는 사용자 입력이나 다른 소스에서 mbti 정보를 가져올 것입니다.
    # 여기서는 예시 데이터를 반환합니다.
    return "ENFJ"

# 혈액형을 알려주는 함수
def get_blood_type():
    # 이 함수는 실제 애플리케이션에서는 사용자 입력이나 다른 소스에서 혈액형 정보를 가져올 것입니다.
    # 여기서는 예시 데이터를 반환합니다.
    return "A"

# 할 일을 저장하는 함수
def save_task(task):
    # 이 함수는 실제 애플리케이션에서는 데이터베이스나 다른 소스에 할 일을 저장할 것입니다.
    task_list = []
    task = input()
    task_list.append(task)
    print(task_list)
    return task_list