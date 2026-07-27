import streamlit as st

st.title("이상기체 상태 방정식을 이용한 기체 판별기")

# 사용자 입력창 (Streamlit 전용 UI)
p_val = st.number_input("압력 P (atm)", value=1.0)
v_val = st.number_input("부피 V (L)", value=22.4)
t_val = st.number_input("온도 T (K)", value=273.15)
mass_val = st.number_input("질량 Mass (g)", value=28.01)
error_val = st.slider("오차 범위 Error (%)", min_value=0.0, max_value=0.5, value=0.1)

if st.button("계산하기"):
    # 기존 계산 함수 호출 (calculate_molecular_weight, identify_gas)
    calc_M = calculate_molecular_weight(p_val, v_val, t_val, mass_val)
    res = identify_gas(calc_M, known_gases, error_val)

    st.write(f"**[결과] 계산된 분자량:** {calc_M:.2f} g/mol")
    st.success(res)
