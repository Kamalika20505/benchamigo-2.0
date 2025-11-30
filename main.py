import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="BenchAmigo",
    page_icon="⚗️",
    layout="centered"
)

# --- SESSION STATE MANAGEMENT ---
# This manages which page is currently visible
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def navigate_to(page_name):
    st.session_state.page = page_name

# --- PAGE 1: LANDING PAGE ---
def show_landing_page():
    st.title("B E N C H A M I G O")
    
    # Navigation tabs (using columns for text layout)
    col_nav1, col_nav2 = st.columns(2)
    with col_nav1:
        st.caption("About Project")
    with col_nav2:
        st.caption("About Me")

    st.divider()

    # The 3 Information Sections
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**WHAT IS BENCHAMIGO?**\n\nYour All-in-one Lab Calculator!\n\nWe handle the math so you can focus on the science.")
    
    with col2:
        st.success("**CUSTOMIZE!**\n\nPick your lab avatar, choose a role, and generate your ID card.\n\n*(Feature coming soon)*")
        
    with col3:
        st.warning("**WHAT CAN IT DO?**\n\nFrom formulas to falcon tubes.\n\nDensity, RPM, PCR Mastermix, Dilutions, and more.")

    st.write("")
    st.write("")
    
    # Start Button
    # 'use_container_width=True' makes the button stretch to fit the column
    _, col_btn, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button("Start Calculating 🚀", use_container_width=True):
            navigate_to('menu')

# --- PAGE 2: MAIN MENU ---
def show_menu_page():
    st.header("WELCOME! HOW MAY I HELP YOU?")
    st.write("")
    
    # Grid Layout for Icons (3x3 grid)
    
    # Row 1
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("⚖️ Density\nCalculator", use_container_width=True):
            navigate_to('density')
    with c2:
        if st.button("🧪 Molarity\nCalculator", use_container_width=True):
            navigate_to('molarity')
    with c3:
        if st.button("🔄 RPM/RCF\nCalculator", use_container_width=True):
            navigate_to('rpm')

    # Row 2
    c4, c5, c6 = st.columns(3)
    with c4:
        if st.button("💧 Dilution Law\nCalculator", use_container_width=True):
            navigate_to('dilution')
    with c5:
        if st.button("🌡️ Serial\nDilution", use_container_width=True):
            navigate_to('serial')
    with c6:
        if st.button("📏 Unit\nConverter", use_container_width=True):
            navigate_to('converter')

    # Row 3
    c7, c8, c9 = st.columns(3)
    with c7:
        if st.button("📊 Aliquot\nPlanner", use_container_width=True):
            navigate_to('aliquot')
    with c8:
        if st.button("⚗️ Buffer\nPrep", use_container_width=True):
            navigate_to('buffer')
    with c9:
        if st.button("% Percent\nSolution", use_container_width=True):
            navigate_to('percent')

    st.divider()
    if st.button("⬅️ Back to Home"):
        navigate_to('landing')

# --- PAGE 3: DILUTION LAW CALCULATOR (C1V1 = C2V2) ---
def show_dilution_page():
    st.header("DILUTION LAW CALCULATOR")
    
    st.subheader("Enter parameters:")
    st.caption("Equation: C1 * V1 = C2 * V2")
    st.info("💡 Note: Add values for only 3 components. Leave the one you want to calculate as 0.")

    col1, col2 = st.columns(2)
    
    with col1:
        v1 = st.number_input("Value of V1 (Initial Vol):", min_value=0.0, step=0.1, format="%.2f")
        c1 = st.number_input("Value of C1 (Initial Conc):", min_value=0.0, step=0.1, format="%.2f")
    
    with col2:
        v2 = st.number_input("Value of V2 (Final Vol):", min_value=0.0, step=0.1, format="%.2f")
        c2 = st.number_input("Value of C2 (Final Conc):", min_value=0.0, step=0.1, format="%.2f")

    st.divider()
    st.subheader("Your answer:")

    if st.button("Calculate Result 🧪", use_container_width=True):
        inputs = [v1, c1, v2, c2]
        zeros = inputs.count(0)

        # Logic to ensure exactly 3 values are entered
        if zeros != 1:
            st.error("Please enter exactly 3 values and leave 1 as 0.")
        else:
            try:
                if v1 == 0:
                    ans = (c2 * v2) / c1
                    st.success(f"**V1 = {ans:.4f}**")
                elif c1 == 0:
                    ans = (c2 * v2) / v1
                    st.success(f"**C1 = {ans:.4f}**")
                elif v2 == 0:
                    ans = (c1 * v1) / c2
                    st.success(f"**V2 = {ans:.4f}**")
                elif c2 == 0:
                    ans = (c1 * v1) / v2
                    st.success(f"**C2 = {ans:.4f}**")
            except ZeroDivisionError:
                st.error("Cannot divide by zero. Check your inputs.")

    st.write("")
    if st.button("⬅️ Back to Menu"):
        navigate_to('menu')

# --- EXTRA PAGE: UNIT CONVERTER ---
def show_converter_page():
    st.header("UNIT CONVERTER")
    
    st.subheader("Select Conversion Type:")
    category = st.selectbox("Category", ["Volume", "Mass", "Concentration"])
    
    col1, col2 = st.columns(2)
    with col1:
        val = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
    
    # Simple logic for Volume demo
    if category == "Volume":
        with col2:
            units_from = st.selectbox("From:", ["Microliter (µL)", "Milliliter (mL)", "Liter (L)"])
            units_to = st.selectbox("To:", ["Microliter (µL)", "Milliliter (mL)", "Liter (L)"])
    else:
        with col2:
            st.warning("Logic for Mass/Conc needs to be added!")
            units_from, units_to = "N/A", "N/A"

    st.divider()
    
    if st.button("Convert 📏", use_container_width=True):
        if category == "Volume":
            # Convert everything to liters first, then to target
            factors = {"Microliter (µL)": 1e-6, "Milliliter (mL)": 1e-3, "Liter (L)": 1}
            
            try:
                val_in_liters = val * factors[units_from]
                final_val = val_in_liters / factors[units_to]
                st.success(f"**{val} {units_from} = {final_val:.6f} {units_to}**")
            except KeyError:
                 st.error("Conversion logic pending for this selection.")

    st.write("")
    if st.button("⬅️ Back to Menu"):
        navigate_to('menu')

# --- EXTRA PAGE: MOLARITY CALCULATOR ---
def show_molarity_page():
    st.header("MOLARITY CALCULATOR")
    st.caption("Mass (g) = Concentration (mol/L) * Volume (L) * Molecular Weight (g/mol)")
    
    mw = st.number_input("Molecular Weight (MW) [g/mol]:", min_value=0.0, format="%.2f")
    vol = st.number_input("Desired Volume (L):", min_value=0.0, format="%.2f")
    conc = st.number_input("Desired Concentration (M):", min_value=0.0, format="%.2f")
    
    if st.button("Calculate Mass Required", use_container_width=True):
        mass = mw * vol * conc
        st.success(f"You need **{mass:.4f} grams** of solute.")

    st.write("")
    if st.button("⬅️ Back to Menu"):
        navigate_to('menu')

# --- PLACEHOLDER FOR OTHER PAGES ---
def show_wip_page(name):
    st.header(name.upper())
    st.info(f"The {name} calculator is currently under construction 🚧.")
    if st.button("⬅️ Back to Menu"):
        navigate_to('menu')

# --- MAIN APP ROUTING ---
# This block decides which function to run based on the session state
if st.session_state.page == 'landing':
    show_landing_page()
elif st.session_state.page == 'menu':
    show_menu_page()
elif st.session_state.page == 'dilution':
    show_dilution_page()
elif st.session_state.page == 'converter':
    show_converter_page()
elif st.session_state.page == 'molarity':
    show_molarity_page()
else:
    # Fallback for pages (density, rpm, serial, aliquot, buffer, percent) not fully coded yet
    show_wip_page(st.session_state.page)

