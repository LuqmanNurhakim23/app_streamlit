import streamlit as st

# halaman utama
st.title ('aplikasi perhitungan luas bangun datar')
st.header ('ini buatan anak SI')

menu = st.sidebar.selectbox('pilih bangun datar', ['luas persegi','luas segitiga','luas lingkaran'])

if menu == 'luas persegi':
    st.write ('ini halaman untuk menghitung luas persegi')
    st.image ('https://imgs.search.brave.com/WGLZqfmXU7sa5rL8fQ6gYrcJS6R2GkVx3_I2ZvOhOMY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9ibG9n/Z2VyLmdvb2dsZXVz/ZXJjb250ZW50LmNv/bS9pbWcvYi9SMjl2/WjJ4bC9BVnZYc0Vq/UEJ1ZzhUT2Fqb2Yz/MjFTYllhS1l3WGhZ/SmJaa2EwdEI0SjlW/R1JZeGVIa3M3MUNa/SmFCY3lScmpMS1hZ/RFhlWExrRHV2aFQw/S0RscWl0d0xSRGo5/NFlvVjVlVmxMR0Iz/am95ZFd4T1RjZnJD/Z1RZa0ZmOFZyRDRL/MmlheTBfNGc2b3Ey/RWMyUlFQTEZrRUFL/amY1UWxod0JVbFFM/Q1FYZjFxNmNoNVhB/ano3M01JbFhEMzFh/NUdCLTdrNHl1L3cy/MjctaDIyNy9QZXJz/ZWdpLnBuZw', caption ='gambar persegi')
    sisi = st.number_input('silakan masuan sisi', min_value=0)
    if st.button('hitung'):
        luas = sisi * sisi
        st.success(f'luas persegi adalah {luas}')

elif menu == 'luas segitiga':
    st.write ('ini halaman untuk menghitung luas segitiga')
    st.image ('https://imgs.search.brave.com/5KJsqP7W_WAIVBe5O16A1RpWJekxh9zwajS45AjyNuM/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWFn/ZS5pZG50aW1lcy5j/b20vcG9zdC8yMDIy/MDMzMS9zZWdpdGln/YS1iZWRiNmJmYTgx/ZjM1M2UxZDAwNjE5/YzE2NTdlNmJkYy5w/bmc', caption ='gambar segitiga')
    alas = st.number_input('silakan masukan alas', min_value=0)
    tinggi = st.number_input('silakan masukan tinggi', min_value=0)
    if st.button('hitung'):
        luas = 0.5 * alas * tinggi
        st.success(f'luas segitiga adalah {luas}')

elif menu == 'luas lingkaran':
    st.write ('ini halaman untuk menghitung luas lingkaran')
    st.image ('https://imgs.search.brave.com/3pyGqiuLONBl6JHZ8iKgamH7EFYUqYloW_1vF9U9cNI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9naG9z/dC1ibG9nLWFzc2V0/cy56ZW5pdXMubmV0/L3dvcmRwcmVzcy8y/MDIxLzA5L2xpbmdr/YXJhbi5wbmc', caption ='gambar lingkaran')
    jarijari = st.number_input('silakan masukan jari jari', min_value=0)
    if st.button('hitung'):
        luas = 3.14 * (jarijari **2)
        st.success(f'luas lingkaran adalah adalah {luas}')