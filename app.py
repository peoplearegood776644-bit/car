import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Car Rental App", page_icon="🚗")

# --- HEADER / IDENTIFICATION ---
st.title("🚗 Car Rental Management System")
st.subheader("Developer Information")
st.info(f"**Name:** Awais Ahmad  \n**Roll Number:** 25-ME-108")

# --- SAMPLE DATA ---
if 'cars' not in st.session_state:
    st.session_state.cars = [
        {"Model": "Toyota Corolla", "Type": "Sedan", "Price/Day": 50, "Status": "Available"},
        {"Model": "Honda Civic", "Type": "Sedan", "Price/Day": 55, "Status": "Available"},
        {"Model": "Hyundai Tucson", "Type": "SUV", "Price/Day": 80, "Status": "Rented"},
    ]

# --- RENTAL INTERFACE ---
tab1, tab2 = st.tabs(["Available Cars", "Rent a Car"])

with tab1:
    st.write("### Browse Our Fleet")
    df = pd.DataFrame(st.session_state.cars)
    st.table(df)

with tab2:
    st.write("### Book Your Ride")
    available_list = [car["Model"] for car in st.session_state.cars if car["Status"] == "Available"]
    
    if available_list:
        selected_car = st.selectbox("Select a car to rent:", available_list)
        days = st.number_input("Rental Duration (Days):", min_value=1, max_value=30)
        
        if st.button("Confirm Rental"):
            # Update status logic
            for car in st.session_state.cars:
                if car["Model"] == selected_car:
                    car["Status"] = "Rented"
            st.success(f"Successfully rented {selected_car} for {days} days!")
            st.balloons()
    else:
        st.warning("No cars are currently available for rent.")

# Footer
st.markdown("---")
st.caption("Developed for Academic Purposes - 25-ME-108")
