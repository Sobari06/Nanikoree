import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from streamlit_lottie import st_lottie
import requests 




# Google Sheets authentication
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('united-option-379311-32c22a337d18.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheets file
sheet = client.open('Keluhan Mahasiswa').sheet1
sheet1 = client.open('KepuasanUser').sheet1
#data = sheet.get_all_records()
# Define the sidebar menu options
menu = ['Halaman Utama', 'Identitas Penerima Keluhan', 'Survei Kepuasan', 'Frequently Asked Questions', 'Akses Keluhan', 'Complaint Analytics']
choice = st.sidebar.selectbox('Menu', menu)

# Define function for adding complaint to the Google Sheets file
def add_complaint(nama, nim, wa, tanggal, jenis_keluhan, deskripsi_keluhan):
    time_sent = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
    data = [nama, nim, wa, tanggal, jenis_keluhan, deskripsi_keluhan, time_sent, '', '', '']
    sheet.insert_row(data, index=2)

# Define function for updating the status of a complaint
def update_status(row, status):
    col = 9 if status == 'diterima' else 10
    sheet.update_cell(row, col, pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"))


if choice == 'Halaman Utama':
     #Mendefinisikan fungsi untuk menampilkan animasi Lottie
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Mendefinisikan URL animasi Lottie yang akan ditampilkan
    url = "https://assets8.lottiefiles.com/packages/lf20_km5er2un.json"

    # Menampilkan animasi Lottie di tampilan utama Streamlit
    st_lottie(load_lottie_url(url))

    st.title("Dashboard Pengaduan KM PKU IPB")
    st.title('Input Keluhan Mahasiswa')

    # Get input from user
    nama = st.text_input('Nama')
    nim = st.text_input('NIM')
    wa = st.text_input('No WA')
    tanggal = st.date_input('Tanggal')
    jenis_keluhan = st.selectbox('Jenis Keluhan', ['Akademik', 'Non-Akademik'])
    deskripsi_keluhan = st.text_area('Deskripsi Keluhan')

    # Add complaint to Google Sheets file
    # Add complaint to Google Sheets file
    if st.button('Kirim Keluhan'):
        if not nama:
            st.warning('Harap isi Nama.')
        elif not nim:
            st.warning('Harap isi NIM.')
        elif not wa:
            st.warning('Harap isi No WA.')
        elif not jenis_keluhan:
            st.warning('Harap pilih Jenis Keluhan.')
        elif not deskripsi_keluhan:
            st.warning('Harap isi Deskripsi Keluhan.')
        else:
            add_complaint(nama, nim, wa, str(tanggal), jenis_keluhan, deskripsi_keluhan)
            st.success('Keluhan berhasil dikirim.')

  
if choice == 'Identitas Penerima Keluhan':
    #Mendefinisikan fungsi untuk menampilkan animasi Lottie
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Mendefinisikan URL animasi Lottie yang akan ditampilkan
    url = "https://assets3.lottiefiles.com/packages/lf20_KU3FGB47d6.json"
    # Menampilkan animasi Lottie di tampilan utama Streamlit
    st_lottie(load_lottie_url(url))

    st.title('Identitas Penerima Keluhan')

    st.write('1. Nama Penerima Keluhan')
    st.write('2. NIM Penerima')

# Survei Kepuasan
if choice == 'Survei Kepuasan':
        #Mendefinisikan fungsi untuk menampilkan animasi Lottie
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    def add_survei(name, nim, date, satisfaction, response_time, resolution, friendliness, handling, effectiveness, communication, appreciation, recommendation, feedback):
        data = [name, nim, date, satisfaction, response_time, resolution, friendliness, handling, effectiveness, communication, appreciation, recommendation, feedback]
        sheet1.insert_row(data, index=2)
    # Mendefinisikan URL animasi Lottie yang akan ditampilkan
    url = "https://assets7.lottiefiles.com/private_files/lf30_VeGYYQ.json"
    # Menampilkan animasi Lottie di tampilan utama Streamlit
    st_lottie(load_lottie_url(url))
    st.title('Survei Kepuasan')
    st.write('Silahkan mengisi survei kepuasan berikut ini:')
    name = st.text_input('Nama:')
    nim = st.text_input('NIM:')
    date = st.date_input('Tanggal:', datetime.date.today())
    date_str = date.strftime('%Y-%m-%d') # ubah tipe data date menjadi string
    st.write('P1. Apakah Anda puas dengan layanan yang diberikan?')
    satisfaction = st.slider('', 1, 10, 5, key='slider1')
    st.write('P2. Apakah respon terhadap keluhan Anda cepat?')
    response_time = st.slider('', 1, 10, 5, key='slider2')
    st.write('P3. Apakah penyelesaian keluhan Anda memuaskan?')
    resolution = st.slider('', 1, 10, 5, key='slider3')
    st.write('P4. Apakah petugas yang menangani keluhan Anda ramah?')
    friendliness = st.slider('', 1, 10, 5, key='slider4')
    st.write('P5. Apakah keluhan Anda ditangani dengan baik?')
    handling = st.slider('', 1, 10, 5, key='slider5')
    st.write('P6. Apakah solusi yang diberikan efektif?')
    effectiveness = st.slider('', 1, 10, 5, key='slider6')
    st.write('P7. Apakah ada komunikasi yang baik antara petugas dan Anda?')
    communication = st.slider('', 1, 10, 5, key='slider7')
    st.write('P8. Apakah Anda merasa dihargai sebagai pelanggan?')
    appreciation = st.slider('', 1, 10, 5, key='slider8')
    st.write('P9. Apakah Anda akan merekomendasikan layanan ini ke orang lain?')
    recommendation = st.slider('', 1, 10, 5, key='slider9')
    st.write('P10. Apakah ada hal yang ingin Anda sampaikan terkait layanan ini?')
    feedback = st.text_input('', '')

    # Save survey data to Google Sheets
    # Add complaint to Google Sheets file
    if st.button('Kirim Hasil Survei'):
        if not name:
            st.warning('Harap isi Nama.')
        elif not nim:
            st.warning('Harap isi NIM.')
        elif not date:
            st.warning('Harap isi No WA.')
        elif not satisfaction:
            st.warning('Harap isi P1.')
        elif not response_time:
            st.warning('Harap isi P2.')
        elif not resolution:
            st.warning('Harap isi P3.')
        elif not friendliness:
            st.warning('Harap isi P4.')
        elif not handling:
            st.warning('Harap isi P5.')
        elif not effectiveness:
            st.warning('Harap isi P6.')
        elif not communication:
            st.warning('Harap isi P7.')
        elif not appreciation:
            st.warning('Harap isi P8.')
        elif not recommendation:
            st.warning('Harap isi P9.')
        elif not feedback:
            st.warning('Harap isi P10.')
        else:
            add_survei(name, nim, str(date), satisfaction, response_time, resolution, friendliness, handling, effectiveness, communication, appreciation, recommendation, feedback)
            st.success('Data survei telah disimpan')
  
   

if choice == 'Frequently Asked Questions':
    #Mendefinisikan fungsi untuk menampilkan animasi Lottie
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Mendefinisikan URL animasi Lottie yang akan ditampilkan
    url = "https://assets3.lottiefiles.com/packages/lf20_D7l6QPTtOL.json"
    # Menampilkan animasi Lottie di tampilan utama Streamlit
    st_lottie(load_lottie_url(url))

    st.title('Frequently Asked Questions')
    st.write('Berikut adalah beberapa pertanyaan dan jawaban yang sering ditanyakan:')
    st.write('1. Bagaimana cara melihat status keluhan saya?')
    st.write('Anda dapat melihat status keluhan Anda di menu "Akses Keluhan" setelah melakukan autentifikasi.')
    st.write('2. Berapa lama waktu yang diperlukan untuk menanggapi keluhan?')
    st.write('Kami berusaha menanggapi setiap keluhan dalam waktu 24 jam.')
    st.write('3. Apa yang harus saya lakukan jika keluhan saya tidak direspon?')
    st.write('Silakan hubungi kami melalui email atau nomor telepon yang tertera di situs kami.')
    st.write('4. Apakah saya dapat memberikan feedback tentang pelayanan yang diberikan?')
    st.write('Tentu saja! Anda dapat memberikan feedback melalui menu "Survei Kepuasan" di situs kami.')

if choice == 'Akses Keluhan':
    # Mendefinisikan fungsi untuk menampilkan animasi Lottie
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Mendefinisikan URL animasi Lottie yang akan ditampilkan
    url = "https://assets1.lottiefiles.com/packages/lf20_huqty7bz.json"
    # Menampilkan animasi Lottie di tampilan utama Streamlit
    st_lottie(load_lottie_url(url))

    # Fungsi untuk mengakses Google Spreadsheet
    def access_spreadsheet():
        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('united-option-379311-32c22a337d18.json', scope)
        client = gspread.authorize(creds)
        sheet= client.open('Keluhan Mahasiswa').sheet1 # ganti nama_spreadsheet dengan nama spreadsheet yang digunakan
        return sheet

    # # Fungsi untuk mengubah status keluhan
    # def update_complaint_status(sheet, row, status):
    #     now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     sheet.update_cell(row, 4, status)
    #     sheet.update_cell(row, 5, now)
    # Define a function to update the status of a complaint in the Google Sheet
    def update_complaint_status(sheet, row, status, penerima_keluhan=None):
        if penerima_keluhan:
            sheet.update_cell(row, 4, penerima_keluhan)
        sheet.update_cell(row, 6, status)
        sheet.update_cell(row, 7, str(datetime.datetime.now()))
    # def update_complaint_status(sheet, row, status, penerima_keluhan=''):
    #     cell = sheet.cell(row, 5)  # column 5 is the Status column
    #     cell.value = status
    #     if penerima_keluhan:
    #         sheet.update_cell(row, 6, penerima_keluhan)  # column 6 is the Penerima Keluhan column
    #     sheet.update_cell(row, 7, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # column 7 is the Waktu Tindakan column
    #     sheet.update_cell(row, 8, '=IF(ISBLANK(E{0}), "", IF(ISBLANK(G{0}), "", G{0}-E{0}))'.format(row))  # column 8 is the Durasi column
    #     sheet.update_cell(row, 9, '=IF(ISBLANK(F{0}), "", NOW()-F{0})'.format(row))  # column 9 is the Durasi Aksi column

# Define a function to get the latest complaint data from the Google Sheet
    # Fungsi untuk mengupdate durasi penyelesaian keluhan di Google Spreadsheet
    def update_complaint_duration(sheet, row, durasi_penyelesaian):
        sheet.update_cell(row, 8, str(durasi_penyelesaian))

    # Fungsi untuk mendapatkan data keluhan terbaru
    def get_latest_complaint_data(sheet):
        data = sheet.get_all_records()[-1]
        return data
    
    # Define the SessionState class
    class SessionState:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

        def get(self, key, default=None):
            return self.__dict__.get(key, default)

        def __repr__(self):
            return str(self.__dict__)
    # Define a default value for the logged_in variable
    state = SessionState(logged_in=False)
    
    def show_complaint_page(sheet):
                # Tampilkan daftar keluhan yang telah diterima
                st.header('Keluhan yang Telah Diterima')
                keluhan = sheet.get_all_records()
                df = pd.DataFrame(keluhan)
                # Menampilkan filter berdasarkan status, bulan, dan kategori keluhan
                status_list = df['Status'].unique().tolist()
                selected_status = st.selectbox('Pilih Status Keluhan', status_list, key='box1')

                bulan_list = pd.DatetimeIndex(df['Waktu Pengiriman']).month_name().unique().tolist()
                selected_bulan = st.selectbox('Pilih Bulan', bulan_list, key='box2')

                kategori_list = df['Kategori Keluhan'].unique().tolist()
                selected_kategori = st.selectbox('Pilih Kategori Keluhan', kategori_list, key='box3')

                filtered_df = df[(df['Status'] == selected_status) & (pd.DatetimeIndex(df['Waktu Pengiriman']).month_name() == selected_bulan) & (df['Kategori Keluhan'] == selected_kategori)]

                st.write('### Jumlah Keluhan: ', len(filtered_df))

                for i, data in filtered_df.iterrows():
                    if data['Status'] == '':
                        st.write('## Keluhan #{}'.format(i+1))
                        st.write('### Nama: ', data['Nama'])
                        st.write('### NIM: ', data['NIM'])
                        st.write('### Nomor WhatsApp: ', data['No WA'])
                        st.write('### Kategori Keluhan: ', data['Kategori Keluhan'])
                        st.write('### Deskripsi Keluhan: ', data['Deskripsi Keluhan'])
                        st.write('### Waktu Pengiriman: ', data['Waktu Pengiriman'])
                        waktu_pengiriman = data['Waktu Pengiriman']
                        
                        # Tambahkan tombol "Proses", "Tolak", dan "Selesai"
                        st.write('### Eksekusi Keluhan')
                        if st.button('Proses'+ str(i)):
                            # Update status keluhan menjadi "Diproses" di Google Spreadsheet
                            row = data.name + 2
                            update_complaint_status(sheet, row, 'Diproses', penerima_keluhan=state.user)
                            st.success('Keluhan telah diproses.')
                            
                        if st.button('Tolak'+ str(i)):
                            # Hapus data keluhan dari Google Spreadsheet
                            row = data.name + 2
                            sheet.delete_row(row)
                            st.success('Keluhan telah ditolak.')
                        # Tampilkan data keluhan terbaru
                            data = get_latest_complaint_data(sheet)
                            st.write('### Data Keluhan Terbaru')
                            st.write('Nama Pelapor:', data['Nama'])
                            st.write('Kategori Keluhan:', data['Kategori Keluhan'])
                            st.write('Isi Keluhan:', data['Deskripsi Keluhan'])
                            st.write('Waktu Pengiriman:', data['Waktu Pengiriman'])
                            st.write('Status Keluhan:', data['Status'])
                            st.write('Durasi Penyelesaian:', str(durasi_penyelesaian))
            
                    if data['Status'] == 'Diproses':
                        st.write('## Keluhan #{}'.format(i+1))
                        st.write('### Nama: ', data['Nama'])
                        st.write('### NIM: ', data['NIM'])
                        st.write('### Nomor WhatsApp: ', data['No WA'])
                        st.write('### Kategori Keluhan: ', data['Kategori Keluhan'])
                        st.write('### Deskripsi Keluhan: ', data['Deskripsi Keluhan'])
                        st.write('### Waktu Pengiriman: ', data['Waktu Pengiriman'])
                        waktu_pengiriman = data['Waktu Pengiriman']
                        
                        # Tambahkan tombol "Proses", "Tolak", dan "Selesai" 
                        if st.button('Selesai'):
                            # Update status keluhan menjadi "Selesai" dan hitung durasi penyelesaian di Google Spreadsheet
                            row = data.name + 2
                            waktu_selesai = datetime.datetime.now()
                            durasi_penyelesaian = waktu_selesai - waktu_pengiriman
                            update_complaint_status(sheet, row, "Selesai")
                            update_complaint_duration(sheet, row, durasi_penyelesaian)
                            st.success('Keluhan telah diselesaikan')
                        # Tampilkan data keluhan terbaru
                            data = get_latest_complaint_data(sheet)
                            st.write('### Data Keluhan Terbaru')
                            st.write('Nama Pelapor:', data['Nama'])
                            st.write('Kategori Keluhan:', data['Kategori Keluhan'])
                            st.write('Isi Keluhan:', data['Deskripsi Keluhan'])
                            st.write('Waktu Pengiriman:', data['Waktu Pengiriman'])
                            st.write('Status Keluhan:', data['Status'])
                            st.write('Durasi Penyelesaian:', str(durasi_penyelesaian))
                else:
                    st.warning('Silakan pilih kategori keluhan') 

    # Daftar email dan password penerima keluhan
    auth = {
        'Hilmy': '22092003',
        'admin2@gmail.com': 'password2',
        'admin3@gmail.com': 'password3',
        'admin4@gmail.com': 'password4',
        'admin5@gmail.com': 'password5'
    }
    # Fungsi untuk menampilkan halaman keluhan
    def main():

        # Check if the user is logged in using session
        state = SessionState.get(logged_in=False)

        # Check if the user is already logged in
        if state.logged_in:
            st.write('Anda telah berhasil login')

        else:
            st.write('Silakan masukkan email dan kata sandi Anda untuk mengakses keluhan:')
            email = st.text_input('Email')
            password = st.text_input('Kata Sandi', type='password')

            if st.button('Login'):
                if email in auth and auth[email] == password:
                    # Set a flag to indicate that the user has logged in
                    state.logged_in = True
                    st.success('Login berhasil')
                    show_complaint_page(sheet)
                    # Set cookie to store user login state
                    st.session_state['user_login_state'] = state.to_dict()
                else:
                    st.error('Email atau kata sandi Anda salah. Silakan coba lagi.')
    # Add a logout button
        if state.logged_in:
            
            if st.button('Logout'):
                # Reset the flag to indicate that the user has logged out
                state.logged_in = False
                st.write('Anda telah berhasil logout')
                # Delete cookie to remove user login state
                if 'user_login_state' in st.session_state:
                    del st.session_state['user_login_state']

    if __name__ == '__main__':
        # Check if user login state is stored in cookie
        if 'user_login_state' in st.session_state:
            state_dict = st.session_state['user_login_state']
            state = SessionState.get(**state_dict)
        else:
            state = SessionState.get(logged_in=False)

        # Run the app
        main()
        
        if state.logged_in:
            show_complaint_page(sheet)
#  # Fungsi untuk menampilkan halaman keluhan

#     def main():

#         # Check if the user is logged in using session
#         if 'logged_in' not in st.session_state:
#             st.session_state.logged_in = False

#         # Check if the user is already logged in
#         if st.session_state.logged_in:
#             st.write('Anda telah berhasil login')

#         else:
#             st.write('Silakan masukkan email dan kata sandi Anda untuk mengakses keluhan:')
#             email = st.text_input('Email')
#             password = st.text_input('Kata Sandi', type='password')

#             if st.button('Login'):
#                 if email in auth and auth[email] == password:
#                     # Set a flag to indicate that the user has logged in
#                     st.session_state.logged_in = True
#                     st.success('Login berhasil')
#                     show_complaint_page(sheet)
#                 else:
#                     st.error('Email atau kata sandi Anda salah. Silakan coba lagi.')


    #     # Add a logout button
    #     if st.session_state.logged_in:
            
    #         if st.button('Logout'):
    #             # Reset the flag to indicate that the user has logged out
    #             st.session_state.logged_in = False
    #             st.write('Anda telah berhasil logout')
    # if __name__ == '__main__':
    #     # Run the app
    #     main()
                    
    #     if state.logged_in:
    #         show_complaint_page(sheet)  
            


        



if choice == 'Complaint Analytics':
    #Mendefinisikan fungsi untuk menampilkan animasi Lottie
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Mendefinisikan URL animasi Lottie yang akan ditampilkan
    url = "https://assets9.lottiefiles.com/packages/lf20_5tl1xxnz.json"
    # Menampilkan animasi Lottie di tampilan utama Streamlit
    st_lottie(load_lottie_url(url))

