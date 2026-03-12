import streamlit as st
from analyzer import generate_meal_plan, calculate_nutrition, summarize_diet_plan

st.set_page_config(page_title="AI Diet Planner", page_icon="🥗")

def main():

    st.title("🥗 AI Chronic Disease Diet Planner")

    st.write("根据健康状况生成 AI 饮食方案")

    disease_type = st.selectbox(
        "选择健康状况",
        ["diabetes", "hypertension", "healthy"]
    )

    if st.button("生成AI饮食计划"):

        with st.spinner("AI正在生成饮食方案..."):

            try:

                meal_plan = generate_meal_plan(disease_type)

                nutrition = calculate_nutrition(meal_plan)

                summary = summarize_diet_plan(disease_type, meal_plan)

                st.subheader("🍽 推荐餐单")

                for meal in meal_plan:
                    st.write(f"• {meal}")

                st.subheader("📊 营养统计")

                col1, col2 = st.columns(2)

                col1.metric("Calories", f"{nutrition['total_calories']} kcal")
                col1.metric("Protein", f"{nutrition['total_protein']} g")

                col2.metric("Carbs", f"{nutrition['total_carbs']} g")
                col2.metric("Fat", f"{nutrition['total_fat']} g")

                st.subheader("🧠 AI 饮食建议")

                st.write(summary)

            except Exception as e:

                st.error(f"系统错误: {e}")


if __name__ == "__main__":
    main()