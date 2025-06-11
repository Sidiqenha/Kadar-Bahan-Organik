import streamlit as st

st.set_page_config(page_title="Aplikasi Praktikum Ilmu Tanah", layout="wide")
st.title("🌱 Aplikasi Praktikum Dasar Ilmu Tanah")

menu = st.sidebar.selectbox("Pilih Acara Praktikum", [
    "Acara 1: Kadar Lengas Tanah",
    "Acara 2: Tekstur Tanah",
    "Acara 3: Struktur Tanah",
    "Acara 4: Kadar Bahan Organik",
    "Acara 5: pH Tanah"
])

# ACARA 1
if menu == "Acara 1: Kadar Lengas Tanah":
    st.header("🧪 Acara 1: Kadar Lengas Tanah")
    a = st.number_input("Berat penimbang kosong (a) gram", min_value=0.0)
    b = st.number_input("Berat penimbang + tanah basah (b) gram", min_value=0.0)
    c = st.number_input("Berat penimbang + tanah kering (c) gram", min_value=0.0)

    if c - a > 0:
        lengas = ((b - c) / (c - a)) * 100
        st.success(f"✅ Kadar lengas tanah: {lengas:.2f} %")
    else:
        st.warning("⚠️ Pastikan nilai (c - a) lebih dari 0.")

# ACARA 2
elif menu == "Acara 2: Tekstur Tanah":
    st.header("🌾 Acara 2: Tekstur Tanah")
    pasir = st.number_input("Pasir (%)", min_value=0.0, max_value=100.0)
    debu = st.number_input("Debu (%)", min_value=0.0, max_value=100.0)
    liat = st.number_input("Liat (%)", min_value=0.0, max_value=100.0)
    total = pasir + debu + liat

    if total != 100:
        st.error(f"⚠️ Total fraksi tidak 100%. Saat ini: {total}%")
    else:
        st.success(f"Total komposisi: {total}%.")
        # Klasifikasi USDA
        if liat >= 40:
            if pasir >= 45:
                klasifikasi = "Lempung berpasir (Sandy Clay)"
            elif debu >= 40:
                klasifikasi = "Lempung berdebu (Silty Clay)"
            else:
                klasifikasi = "Lempung (Clay)"
        elif liat >= 27:
            if pasir >= 20 and pasir <= 45:
                klasifikasi = "Lempung berliat (Clay Loam)"
            elif pasir > 45:
                klasifikasi = "Lempung berpasir (Sandy Clay Loam)"
            else:
                klasifikasi = "Lempung berdebu (Silty Clay Loam)"
        elif liat >= 7 and liat < 27:
            if pasir > 52:
                klasifikasi = "Lempung berpasir (Sandy Loam)"
            elif debu >= 50:
                klasifikasi = "Lempung berdebu (Silty Loam)"
            else:
                klasifikasi = "Lempung (Loam)"
        elif liat < 7:
            if pasir >= 85:
                klasifikasi = "Pasir (Sand)"
            elif pasir >= 70:
                klasifikasi = "Pasir berlempung (Loamy Sand)"
            else:
                klasifikasi = "Pasir berlempung halus (Sandy Loam)"
        else:
            klasifikasi = "Tidak terklasifikasi"

        st.subheader("📌 Klasifikasi Tekstur USDA:")
        st.success(f"Hasil klasifikasi: **{klasifikasi}**")

# ACARA 3
elif menu == "Acara 3: Struktur Tanah":
    st.header("🧱 Acara 3: Struktur Tanah")

    st.subheader("📍 Kerapatan Butir Tanah")
    berat_kering = st.number_input("Berat tanah kering mutlak (g)", min_value=0.0)
    volume_butir = st.number_input("Volume total butir tanah (cm³)", min_value=0.0)
    if volume_butir > 0:
        bd = berat_kering / volume_butir
        st.success(f"Kerapatan Butir Tanah: {bd:.2f} g/cm³")

    st.subheader("📍 Kerapatan Massa Tanah")
    berat_kering_bongkah = st.number_input("Berat tanah kering bongkah (g)", min_value=0.0)
    volume_air_naik = st.number_input("Volume air naik karena bongkah (ml)", min_value=0.0)
    if volume_air_naik > 0:
        volume_bongkah = volume_air_naik * 0.87
        bv = berat_kering_bongkah / volume_bongkah
        st.success(f"Kerapatan Massa Tanah: {bv:.2f} g/cm³")
# ACARA 4
elif menu == "Acara 4: Kadar Bahan Organik":
    st.header("🌱 Acara 4: Kadar Bahan Organik Tanah (Metode Walkley & Black)")

    vb = st.number_input("Volume titran blanko (Vb) (mL)", min_value=0.0)
    vs = st.number_input("Volume titran sampel (Vs) (mL)", min_value=0.0)
    n = st.number_input("Normalitas FeSO₄ (N)", value=1.0)
    berat_tanah = st.number_input("Berat tanah (gram)", value=1.0)
    kadar_lengas = st.number_input("Kadar lengas tanah (%)", value=10.0)

    if berat_tanah > 0 and (100 - kadar_lengas) > 0:
        selisih = vb - vs
        bahan_organik = ((selisih * n * 0.003 * 1.33 * 100) / (berat_tanah * (100 - kadar_lengas))) * 100
        st.success(f"✅ Kadar Bahan Organik: {bahan_organik:.4f} %")
    else:
        st.warning("⚠️ Pastikan berat tanah dan kadar lengas valid.")

# ACARA 5
elif menu == "Acara 5: pH Tanah":
    st.header("🌡️ Acara 5: pH Tanah")
    ph = st.number_input("Hasil pengukuran pH", min_value=0.0, max_value=14.0, step=0.01)
    suhu = st.number_input("Suhu tanah saat pengukuran (°C)", min_value=0.0)

    if ph > 0:
        if ph < 5.5:
            kategori = "Asam"
        elif 5.5 <= ph <= 7.0:
            kategori = "Netral"
        else:
            kategori = "Basa"
        st.success(f"pH Tanah: {ph:.2f} → {kategori}")
    else:
        st.info("Masukkan nilai pH yang valid untuk melihat kategori.")
