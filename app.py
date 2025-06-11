import streamlit as st

# Judul
st.set_page_config(page_title="Kalkulator Bahan Organik Tanah")
st.title("🧪 Kalkulator Bahan Organik Tanah")
st.subheader("Metode Walkley & Black")

# Penjelasan singkat
with st.expander("📘 Penjelasan Singkat"):
    st.markdown("""
    **Rumus:**
    > **Bahan Organik (%) = ((Vb - Vs) × N × 0.003 × 1.33 × 100) / (Berat × (100 - Lengas))**

    - **Vb** = Volume blanko (mL)  
    - **Vs** = Volume sampel (mL)  
    - **N** = Normalitas larutan FeSO₄  
    - **0.003** = Gram C yang setara per mL FeSO₄ 1N  
    - **1.33** = Faktor koreksi (karena hanya 77% C teroksidasi)  
    """)

# Tombol Reset
if st.button("🔄 Reset Semua"):
    st.experimental_rerun()

# Input pengguna
vb = st.number_input("📌 Volume Blanko (mL)", min_value=0.0, step=0.1)
vs = st.number_input("📌 Volume Sampel (mL)", min_value=0.0, step=0.1)
n = st.number_input("📌 Normalitas FeSO₄", value=1.0, step=0.1)
berat = st.number_input("📌 Berat Tanah (gram)", value=1.0, step=0.1)
lengas = st.number_input("📌 Kadar Lengas (%)", value=10.0, step=0.1)

# Hitung hasil
if berat > 0 and (100 - lengas) > 0:
    selisih = vb - vs
    bahan_organik = ((selisih * n * 0.003 * 1.33 * 100) / (berat * (100 - lengas))) * 100
    karbon_organik = bahan_organik / 1.33

    st.success(f"✅ Kadar Bahan Organik: **{bahan_organik:.4f} %**")
    st.info(f"🌿 Karbon Organik: **{karbon_organik:.4f} %**")
else:
    st.warning("⚠️ Harap masukkan semua data dengan benar.")
