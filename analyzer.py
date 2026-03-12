import os
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)

def generate_meal_plan(disease_type):

    prompt = f"""
你是一名营养师。
请给 {disease_type} 人群设计一天饮食。
列出5个食物。
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是专业营养师"},
            {"role": "user", "content": prompt}
        ]
    )

    text = response.choices[0].message.content
    meals = [m.strip("- ") for m in text.split("\n") if m.strip()]

    return meals


def calculate_nutrition(meal_plan):

    # 简单模拟营养数据库

    nutrition_db = {
        "燕麦": (150, 5, 27, 3),
        "鸡胸肉": (165, 31, 0, 4),
        "西兰花": (55, 4, 11, 1),
        "糙米": (216, 5, 45, 2),
        "鸡蛋": (78, 6, 1, 5),
        "鱼": (180, 25, 0, 8),
        "菠菜": (23, 3, 4, 0),
        "牛油果": (160, 3, 12, 12)
    }

    calories = 0
    protein = 0
    carbs = 0
    fat = 0

    for meal in meal_plan:

        for food in nutrition_db:

            if food in meal:

                data = nutrition_db[food]

                calories += data[0]
                protein += data[1]
                carbs += data[2]
                fat += data[3]

    return {
        "total_calories": calories,
        "total_protein": protein,
        "total_carbs": carbs,
        "total_fat": fat
    }


def summarize_diet_plan(condition, meals):

    prompt = f"""
用户健康状况：{condition}

饮食计划：
{meals}

请给出100字饮食建议。
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是营养专家"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
