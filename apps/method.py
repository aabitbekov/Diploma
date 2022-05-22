import streamlit as st
from PIL import Image

def buildMain():
    st.markdown("""
    # Межотраслевой баланс
    Межотраслевой баланс (МОБ, модель «затраты — выпуск», метод «затраты — выпуск») — экономико-математическая балансовая модель, характеризующая межотраслевые производственные взаимосвязи в экономике страны. Характеризует связи между выпуском продукции в одной отрасли и затратами, расходованием продукции всех участвующих отраслей, необходимым для обеспечения этого выпуска. Межотраслевой баланс составляется в денежной и натуральной формах.""")
    st.write('')
    st.write('')
    col1, col2, col3 = st.columns([2,6,1])

    with col1:
        st.write("")

    with col2:
        st.image(image=Image.open('static/175.png'),use_column_width=False, caption='Экономико-математическая модель межотраслевого баланса')

    with col3:
        st.write("")
    st.markdown("""Межотраслевой баланс представлен в виде системы линейных уравнений. Межотраслевой баланс (МОБ) представляет собой таблицу, в которой отражен процесс формирования и использования совокупного общественного продукта в отраслевом разрезе. Таблица показывает структуру затрат на производство каждого продукта и структуру его распределения в экономике.""")