import streamlit as st

# halaman utama
st.title ('aplikasi perhitungan luas bangun datar')
st.header ('ini buatan anak SI')

menu = st.sidebar.selectbox('pilih bangun datar', ['luas persegi','luas segitiga','luas segitiga','luas lingkaran'])

if menu == 'luas persegi':
    st.write ('ini halaman untuk menghitung luas persegi')
    st.image ('https://imgs.search.brave.com/WGLZqfmXU7sa5rL8fQ6gYrcJS6R2GkVx3_I2ZvOhOMY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9ibG9n/Z2VyLmdvb2dsZXVz/ZXJjb250ZW50LmNv/bS9pbWcvYi9SMjl2/WjJ4bC9BVnZYc0Vq/UEJ1ZzhUT2Fqb2Yz/MjFTYllhS1l3WGhZ/SmJaa2EwdEI0SjlW/R1JZeGVIa3M3MUNa/SmFCY3lScmpMS1hZ/RFhlWExrRHV2aFQw/S0RscWl0d0xSRGo5/NFlvVjVlVmxMR0Iz/am95ZFd4T1RjZnJD/Z1RZa0ZmOFZyRDRL/MmlheTBfNGc2b3Ey/RWMyUlFQTEZrRUFL/amY1UWxod0JVbFFM/Q1FYZjFxNmNoNVhB/ano3M01JbFhEMzFh/NUdCLTdrNHl1L3cy/MjctaDIyNy9QZXJz/ZWdpLnBuZw', caption ='gambar persegi')
    sisi = st.number_input('silakan masuan sisi', min_value=0)
    if st.button('hitung'):
        luas = sisi * sisi
        st.success(f'luas persegi adalah {luas}')

elif menu == 'luas segitiga':
    st.write ('ini halaman untuk menghitung luas segitiga')