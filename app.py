import streamlit as st

st.set_page_config(page_title="GIAIC Unit Converter", page_icon="🔄")

st.sidebar.title("🌟 GIAIC Unit Converter")
st.sidebar.markdown("Effortlessly convert units with a sleek interface. 🚀")

conversion_types = ["Length 📏", "Speed 🏎️"]

tab1, tab2 = st.tabs(["Length 📏", "Speed 🏎️"])

st.sidebar.subheader("🔀 Select Conversion Type")
selected = st.sidebar.selectbox(
    "Choose a category to convert:",
    conversion_types,
    help="Pick the type of unit you want to convert."
)

st.sidebar.markdown("---")
st.sidebar.subheader("💬 Quote of the Day")
st.sidebar.info("🌟 *Consistency is the key to success.*")


st.sidebar.markdown("---")
st.sidebar.subheader("📞 **Contact**")
st.sidebar.write("🛠️ Developed by **Syed Mesum Ali Shah**")
st.sidebar.write("📫 [syedmesumjaffary@gmail.com](mailto:syedmesumjaffary@gmail.com)")

st.sidebar.markdown("---")
st.sidebar.write("⚙️ *Version 1.0.0 | Powered by Streamlit*")


def length_conversion(value, from_unit, to_unit):
    to_meters = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1,
        "kilometer": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34,
    }

    value_in_meters = value * to_meters[from_unit]
    result = value_in_meters / to_meters[to_unit]
    return result

if selected == "Length 📏" or tab1:
    with tab1:
        st.subheader("📏 **Length Conversion**")
        st.write("Convert between **millimeters**, **centimeters**, **meters**, **kilometers**, **inches**, **feet**, **yards**, and **miles**. ")
        col1, col2 = st.columns(2)

        with col1:
            from_unit = st.selectbox(
                "From",
                ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"]
            )

        with col2:
            to_unit = st.selectbox(
                "To",
                ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"]
            )
        value = st.number_input("Enter Value", min_value=0.0,)

        if st.button("Covert 🔚"):
            if value >= 0:
                result = length_conversion(value, from_unit, to_unit)
                st.success(f"{value} {from_unit} = {result: .2f} {to_unit}")
            else:
                st.error("Please enter a non-negative value.")

def speed_conversion(speed, from_spped, to_speed):
    to_mps = {
        "m/s": 1,
        "km/h": 0.27778,
        "mph": 0.44704,
        "ft/s": 0.3048,
        "knots": 0.514444,
    }

    value_in_mps = speed * to_mps[from_speed]
    result = value_in_mps / to_mps[to_speed]
    return result

if selected == "Speed 🏎️" or tab2:
    with tab2:
        st.title("**Speed Conversion 🏎️**")
        st.write("Convert between **m/s**, **km/h**, **mph**, **ft/s**, and **knots**.")
        col1, col2 = st.columns(2)

        with col1:
            from_speed = st.selectbox(
                "From",
                ["m/s", "km/h", "mph", "ft/s", "knots"]
            ) 

        with col2:
            to_speed = st.selectbox(
                "To",
                ["m/s", "km/h", "mph", "ft/s", "knots"]
            )
        speed = st.number_input("Enter Speed Value", min_value=0.0,)

        if st.button("Convert 💨"):
            if speed >= 0:
                result = speed_conversion(speed, from_speed, to_speed)
                st.success(f"{speed} {from_speed} = {result: .2f} {to_unit}")
            else:
                st.error("Please enter a non-negative value.")