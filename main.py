import streamlit as st
import pandas as pd # Needed for the Serial Dilution Table

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="BenchAmigo",
    page_icon="⚗️",
    layout="centered"
)

# --- SESSION STATE MANAGEMENT ---
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def navigate_to(page_name):
    st.session_state.page = page_name
    st.rerun() # <--- THIS FIXES THE DOUBLE CLICK ISSUE

# --- PAGE 1: LANDING PAGE ---
def show_landing_page():
    st.title("B E N C H A M I G O")
    
    col_nav1, col_nav2 = st.columns(2)
    with col_nav1:
        st.caption("About Project")
    with col_nav2:
        st.caption("About Me")

    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**WHAT IS BENCHAMIGO?**\n\nYour All-in-one Lab Calculator!\n\nWe handle the math so you can focus on the science.")
    with col2:
        st.success("**CUSTOMIZE!**\n\nPick your lab avatar, choose a role, and generate your ID card.\n\n*(Feature coming soon)*")
    with col3:
        st.warning("**WHAT CAN IT DO?**\n\nFrom formulas to falcon tubes.\n\nDensity, RPM, PCR Mastermix, Dilutions, and more.")

    st.write("")
    _, col_btn, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button("Start Calculating 🚀", use_container_width=True):
            navigate_to('menu')

# --- PAGE 2: MAIN MENU ---
def show_menu_page():
    st.header("WELCOME! HOW MAY I HELP YOU?")
    st.write("")
    
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

# --- CALCULATOR 1: DILUTION LAW (C1V1 = C2V2) ---
def show_dilution_page():
    st.header("DILUTION LAW")
    st.caption("Equation: C1 * V1 = C2 * V2")
    st.info("💡 Enter 3 values. Leave the one you want to calculate as 0.")

    col1, col2 = st.columns(2)
    with col1:
        v1 = st.number_input("V1 (Initial Vol):", min_value=0.0, step=0.1, format="%.2f")
        c1 = st.number_input("C1 (Initial Conc):", min_value=0.0, step=0.1, format="%.2f")
    with col2:
        v2 = st.number_input("V2 (Final Vol):", min_value=0.0, step=0.1, format="%.2f")
        c2 = st.number_input("C2 (Final Conc):", min_value=0.0, step=0.1, format="%.2f")

    st.divider()
    if st.button("Calculate 🧪", use_container_width=True):
        inputs = [v1, c1, v2, c2]
        if inputs.count(0) != 1:
            st.error("Please enter exactly 3 values.")
        else:
            try:
                if v1 == 0: st.success(f"**V1 = {(c2 * v2) / c1:.4f}**")
                elif c1 == 0: st.success(f"**C1 = {(c2 * v2) / v1:.4f}**")
                elif v2 == 0: st.success(f"**V2 = {(c1 * v1) / c2:.4f}**")
                elif c2 == 0: st.success(f"**C2 = {(c1 * v1) / v2:.4f}**")
            except ZeroDivisionError:
                st.error("Cannot divide by zero.")

    if st.button("⬅️ Menu"): navigate_to('menu')

# --- CALCULATOR 2: MOLARITY ---
def show_molarity_page():
    st.header("MOLARITY CALCULATOR")
    st.caption("Calculate Mass required to reach a specific Molarity.")
    
    mw = st.number_input("Molecular Weight (MW) [g/mol]:", min_value=0.0, format="%.2f")
    vol = st.number_input("Desired Volume (L):", min_value=0.0, format="%.2f")
    conc = st.number_input("Desired Concentration (M):", min_value=0.0, format="%.2f")
    
    if st.button("Calculate Mass", use_container_width=True):
        mass = mw * vol * conc
        st.success(f"You need **{mass:.4f} grams** of solute.")

    if st.button("⬅️ Menu"): navigate_to('menu')

# --- CALCULATOR 3: DENSITY ---
def show_density_page():
    st.header("DENSITY CALCULATOR")
    st.caption("Equation: Density = Mass / Volume")
    st.info("💡 Enter 2 values. Leave the target as 0.")

    c1, c2 = st.columns(2)
    with c1:
        mass = st.number_input("Mass (g):", min_value=0.0, format="%.2f")
        vol = st.number_input("Volume (mL):", min_value=0.0, format="%.2f")
    with c2:
        density = st.number_input("Density (g/mL):", min_value=0.0, format="%.2f")

    if st.button("Calculate", use_container_width=True):
        if mass == 0 and vol > 0 and density > 0:
            st.success(f"**Mass = {vol * density:.4f} g**")
        elif vol == 0 and mass > 0 and density > 0:
            st.success(f"**Volume = {mass / density:.4f} mL**")
        elif density == 0 and mass > 0 and vol > 0:
            st.success(f"**Density = {mass / vol:.4f} g/mL**")
        else:
            st.error("Please enter exactly 2 non-zero values.")

    if st.button("⬅️ Menu"): navigate_to('menu')

# --- CALCULATOR 4: RPM / RCF ---
def show_rpm_page():
    st.header("RPM ↔ RCF CONVERTER")
    st.caption("Equation: RCF = 1.118 × 10⁻⁵ × r × RPM²")
    
    radius = st.number_input("Rotor Radius (cm):", min_value=0.1, value=10.0, format="%.1f")
    
    col1, col2 = st.columns(2)
    with col1:
        rpm = st.number_input("Speed (RPM):", min_value=0.0, step=100.0)
    with col2:
        rcf = st.number_input("G-Force (RCF):", min_value=0.0, step=100.0)

    if st.button("Convert", use_container_width=True):
        if rpm > 0 and rcf == 0:
            calc_rcf = 1.118e-5 * radius * (rpm ** 2)
            st.success(f"**{rpm} RPM = {calc_rcf:.0f} x g**")
        elif rcf > 0 and rpm == 0:
            calc_rpm = (rcf / (1.118e-5 * radius)) ** 0.5
            st.success(f"**{rcf} x g = {calc_rpm:.0f} RPM**")
        else:
            st.error("Enter either RPM or RCF (not both) to convert.")

    if st.button("⬅️ Menu"): navigate_to('menu')

# --- CALCULATOR 5: SERIAL DILUTION ---
def show_serial_page():
    st.header("SERIAL DILUTION PLANNER")
    st.caption("Generate a step-by-step dilution table.")
    
    start_conc = st.number_input("Starting Concentration (e.g., 100 mM):", min_value=0.0, value=100.0)
    dil_factor = st.number_input("Dilution Factor (e.g., 10 for 1:10):", min_value=1.1, value=10.0)
    steps = st.number_input("Number of Steps (Tubes):", min_value=1, max_value=20, value=5)
    
    if st.button("Generate Table", use_container_width=True):
        data = []
        current_conc = start_conc
        for i in range(1, int(steps) + 1):
            current_conc = current_conc / dil_factor
            data.append([f"Tube {i}", f"1 : {dil_factor**i:.0f}", f"{current_conc:.6f}"])
        
        df = pd.DataFrame(data, columns=["Tube", "Ratio", "Concentration"])
        st.table(df)

    if st.button("⬅️ Menu"): navigate_to('menu')

# --- CALCULATOR 6: ALIQUOT PLANNER ---
def show_aliquot_page():
    st.header("ALIQUOT PLANNER")
    st.info("💡 Enter 2 values. Leave the target as 0.")
    
    c1, c2 = st.columns(2)
    with c1:
        total_vol = st.number_input("Total Volume Available (mL):", min_value=0.0)
        aliquot_vol = st.number_input("Volume per Aliquot (mL):", min_value=0.0)
    with c2:
        num_tubes = st.number_input("Number of Tubes:", min_value=0.0, step=1.0)
        
    if st.button("Calculate", use_container_width=True):
        if num_tubes == 0 and total_vol > 0 and aliquot_vol > 0:
            count = int(total_vol // aliquot_vol)
            leftover = total_vol % aliquot_vol
            st.success(f"You can make **{count} tubes**. (Leftover: {leftover:.2f} mL)")
        elif total_vol == 0 and num_tubes > 0 and aliquot_vol > 0:
            req = num_tubes * aliquot_vol
            st.success(f"You need **{req:.2f} mL** total.")
        else:
            st.error("Please check inputs.")

    if st.button("⬅️ Menu"): navigate_to('menu')

# --- CALCULATOR 7: BUFFER PREP (STOCK MIXER) ---
def show_buffer_page():
    st.header("BUFFER PREP (STOCK MIXER)")
    st.caption("Calculate how much Stock solution to add to get a Target concentration.")
    
    final_vol = st.number_input("Final Buffer Volume (mL):", value=1000.0)
    st.divider()
    
    # Simple fixed inputs for up to 3 components
    st.subheader("Component 1")
    c1a, c1b = st.columns(2)
    s1 = c1a.number_input("Stock Conc (e.g., 1000 mM):", key="s1")
    t1 = c1b.number_input("Target Conc (e.g., 50 mM):", key="t1")
    
    st.subheader("Component 2")
    c2a, c2b = st.columns(2)
    s2 = c2a.number_input("Stock Conc:", key="s2")
    t2 = c2b.number_input("Target Conc:", key="t2")
    
    if st.button("Calculate Recipe", use_container_width=True):
        st.markdown("### 📝 Recipe:")
        total_solutes = 0
        
        # Component 1 Calc
        if s1 > 0 and t1 > 0:
            v1 = (t1 * final_vol) / s1
            st.write(f"- Add **{v1:.2f} mL** of Component 1")
            total_solutes += v1
            
        # Component 2 Calc
        if s2 > 0 and t2 > 0:
            v2 = (t2 * final_vol) / s2
            st.write(f"- Add **{v2:.2f} mL** of Component 2")
            total_solutes += v2
            
        water = final_vol - total_solutes
        st.write(f"- Add **{water:.2f} mL** of Water (or solvent)")
        st.success(f"**Total Volume: {final_vol} mL**")

    if st.button("⬅️ Menu"): navigate_to('menu')

# --- CALCULATOR 8: PERCENT SOLUTION ---
def show_percent_page():
    st.header("PERCENT SOLUTION (%)")
    st.caption("Calculate grams (w/v) or mL (v/v) needed.")
    
    percent = st.number_input("Desired Percentage (%):", min_value=0.0, value=1.0)
    final_vol = st.number_input("Final Volume (mL):", min_value=0.0, value=100.0)
    
    if st.button("Calculate", use_container_width=True):
        amt = (percent / 100) * final_vol
        st.success(f"Add **{amt:.4f} g (or mL)** of solute, then fill to {final_vol} mL.")

    if st.button("⬅️ Menu"): navigate_to('menu')

# --- CALCULATOR 9: UNIT CONVERTER ---
def show_converter_page():
    st.header("UNIT CONVERTER")
    category = st.selectbox("Category", ["Volume", "Mass"])
    
    val = st.number_input("Value:", min_value=0.0)
    
    if category == "Volume":
        units = {"µL": 1e-6, "mL": 1e-3, "L": 1}
    else:
        units = {"µg": 1e-6, "mg": 1e-3, "g": 1, "kg": 1000}
        
    c1, c2 = st.columns(2)
    u_from = c1.selectbox("From:", list(units.keys()))
    u_to = c2.selectbox("To:", list(units.keys()))

    if st.button("Convert", use_container_width=True):
        # Base conversion to standard unit (L or g)
        base_val = val * units[u_from]
        # Convert to target
        final_val = base_val / units[u_to]
        st.success(f"**{val} {u_from} = {final_val:.6f} {u_to}**")

    if st.button("⬅️ Menu"): navigate_to('menu')

# --- MAIN ROUTING ---
if st.session_state.page == 'landing': show_landing_page()
elif st.session_state.page == 'menu': show_menu_page()
elif st.session_state.page == 'density': show_density_page()
elif st.session_state.page == 'molarity': show_molarity_page()
elif st.session_state.page == 'rpm': show_rpm_page()
elif st.session_state.page == 'dilution': show_dilution_page()
elif st.session_state.page == 'serial': show_serial_page()
elif st.session_state.page == 'converter': show_converter_page()
elif st.session_state.page == 'aliquot': show_aliquot_page()
elif st.session_state.page == 'buffer': show_buffer_page()
elif st.session_state.page == 'percent': show_percent_page()

