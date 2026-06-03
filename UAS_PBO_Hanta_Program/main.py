import unittest 
import sys
from repository import HantaRepository
from service import HantaService  # BARU: Mengimpor Service Layer

# CLASS-BASED APPLICATION : Membungkus aplikasi ke dalam blueprint struktur Class utuh
class MainMenu:
    # SOLID : Dependency Inversion Principle (DIP) & Single Responsibility Principle (SRP)
    def __init__(self, service: HantaService):
        self.__service = service
        
        # SOLID : Open/Closed Principle (OCP)
        self.__menu_actions = {
            "1": self.__action_load_data,
            "2": self.__action_view_data,
            "3": lambda: self.__print_clinical(detailed=True),
            "4": lambda: self.__print_demographic(detailed=True),
            "5": lambda: self.__print_transmission(detailed=True),
            "6": lambda: self.__print_environmental(detailed=True),
            "7": lambda: self.__print_quarantine(detailed=True),
            "8": self.__print_strain,
            "9": self.__action_show_all,
            "10": self.__action_run_tests,
            "11": self.__action_exit
        }

    @staticmethod
    def display_menu():
        print("╔════════════════════════════════════════════════════════╗")
        print("║       SISTEM ANALISIS MANAJEMEN WABAH HANTAVIRUS       ║")
        print("╠════════════════════════════════════════════════════════╣")
        print("║  1. Memuat Data CSV                                    ║")
        print("║  2. Lihat Data Kasus Terarah                           ║")
        print("║  3. Analisis Klinis (Hospitalisasi & Fatalitas)        ║")
        print("║  4. Analisis Demografis (Usia & Gender)                ║")
        print("║  5. Analisis Transmisi (Penyebaran & Paparan)          ║")
        print("║  6. Analisis Iklim Lingkungan (Suhu & Kelembaban)      ║")
        print("║  7. Analisis Efisiensi Karantina                       ║")
        print("║  8. Analisis Karakteristik Varian Virus (Strain)       ║")
        print("║  9. Tampilkan Semua Analisis (Laporan Lengkap)         ║")
        print("║ 10. Jalankan Pengujian Otomatis (Unit Testing)         ║")
        print("║ 11. Keluar                                             ║")
        print("╚════════════════════════════════════════════════════════╝")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Pilih menu (1-11): ")
            print()

            if choice in self.__menu_actions:
                self.__menu_actions[choice]()
            else:
                print("[!] Pilihan Menu salah. Silakan masukkan nomor menu yang tersedia.\n")

    def __action_load_data(self):
        source_name = self.__service.get_source_name()
        if not self.__service.check_file_exists(source_name):
            print(f"[X] Error: File '{source_name}' tidak ditemukan.\n")
        else:
            self.__service.load_data()
            print("[✓] Data berhasil dimuat dari file CSV!\n")

    def __action_view_data(self):
        if not self.__service.is_data_loaded():
            print("[!] Silakan muat data terlebih dahulu di Menu 1.\n")
            return
            
        cases = self.__service.get_cases()
        total_cases = len(cases)
        
        try:
            limit_input = input(f"Berapa banyak data kasus yang ingin Anda tampilkan? (1 - {total_cases}): ")
            limit = int(limit_input)
            if limit < 1 or limit > total_cases:
                print(f"[!] Peringatan: Angka di luar batas. Menampilkan 10 data default.")
                limit = 10
        except ValueError:
            print(f"[!] Error: Input wajib angka. Menampilkan 10 data default.")
            limit = 10

        print("\n" + "═" * 85)
        for c in cases[:limit]:
            print(f" {c} | Usia: {c.patient.age:<2} thn | Suhu: {c.temp}°C")
        print("═" * 85 + "\n")

    def __action_show_all(self):
        if not self.__service.is_data_loaded():
            print("[!] Silakan muat data terlebih dahulu di Menu 1.\n")
            return
            
        print("╔" + "═" * 70 + "╗")
        print(f"║{'MULAI MEMUAT LAPORAN ANALISIS':^70}║")
        print("╚" + "═" * 70 + "╝\n")
        
        self.__print_clinical(show_header=False, detailed=False)
        self.__print_separator()
        
        self.__print_demographic(show_header=False, detailed=False)
        self.__print_separator()
        
        self.__print_transmission(show_header=False, detailed=False)
        self.__print_separator()
        
        self.__print_environmental(show_header=False, detailed=False)
        self.__print_separator()
        
        self.__print_quarantine(show_header=False, detailed=False)
        self.__print_separator()
        
        self.__print_strain(show_header=False)
        self.__print_separator()
        
        self.__print_executive_summary()

    def __action_run_tests(self):
        print("╔" + "═" * 70 + "╗")
        print(f"║{'MENJALANKAN UNIT TESTING OTOMATIS (test_analyzer.py)':^70}║")
        print("╚" + "═" * 70 + "╝\n")
        
        try:
            suite = unittest.defaultTestLoader.discover(start_dir=".", pattern="test_analyzer.py")
            runner = unittest.TextTestRunner(verbosity=2)
            runner.run(suite)
        except Exception as e:
            print(f"[X] Gagal menjalankan pengujian: {e}")
        print()

    def __action_exit(self):
        print("Terima kasih telah menggunakan sistem ini. Sampai jumpa!")
        sys.exit(0)

    def __print_separator(self):
        print("\n" + "·" * 72 + "\n")

    def __print_clinical(self, show_header=True, detailed=False):
        if not self.__service.is_data_loaded():
            print("[!] Silakan muat data terlebih dahulu di Menu 1.\n")
            return
            
        if show_header: print("--- HASIL ANALISIS KLINIS KEPARAHAN ---\n")
        else: print(" [1] ANALISIS KLINIS KEPARAHAN")
            
        result = self.__service.analyze_clinical()
        print(f"  ➢  Tingkat Rawat Inap (Hospitalisasi) : {result['hospitalization_rate']:.2f}%")
        print(f"  ➢  Tingkat Fatalitas Kasus (CFR)      : {result['fatality_rate']:.2f}%")
        
        if detailed:
            print("  ➢  Detail Pasien Tercatat:")
            print(f"     - Dirawat Inap : {result['hosp_count']} orang")
            print(f"     - Meninggal    : {result['fatal_count']} orang")
            print(f"     - Sembuh       : {result['recovered_count']} orang")
            
        if show_header: print()

    def __print_demographic(self, show_header=True, detailed=False):
        if not self.__service.is_data_loaded():
            print("[!] Silakan muat data terlebih dahulu di Menu 1.\n")
            return
            
        if show_header: print("--- HASIL ANALISIS DEMOGRAFIS PASIEN ---\n")
        else: print(" [2] ANALISIS DEMOGRAFIS PASIEN")
            
        result = self.__service.analyze_demographic()
        print(f"  ➢  Rata-rata Usia Pengidap : {result['average_age']:.1f} tahun")
        print(f"  ➢  Distribusi Gender       : Pria ({result['male_count']} org) | Wanita ({result['female_count']} org)")
        
        if detailed:
            print("  ➢  Detail Kelompok Umur:")
            for group, count in result['age_groups'].items():
                print(f"     - {group:<22} : {count} pasien")
                
        if show_header: print()

    def __print_transmission(self, show_header=True, detailed=False):
        if not self.__service.is_data_loaded():
            print("[!] Silakan muat data terlebih dahulu di Menu 1.\n")
            return
            
        if show_header: print("--- HASIL ANALISIS JALUR TRANSMISI WABAH ---\n")
        else: print(" [3] ANALISIS TRANSMISI & PAPARAN")
            
        result = self.__service.analyze_transmission()
        print(f"  ➢  Metode Penularan Utama : {result['most_common_transmission']}")
        print(f"  ➢  Klaster Lokasi Paparan : {result['most_common_exposure']}")
        
        if detailed:
            print("  ➢  Detail Jalur Transmisi:")
            for k, v in result['transmission_counts'].items():
                print(f"     - {k:<22} : {v} kasus")
            print("  ➢  Detail Sumber Paparan:")
            for k, v in result['exposure_counts'].items():
                print(f"     - {k:<22} : {v} kasus")
                
        if show_header: print()

    def __print_environmental(self, show_header=True, detailed=False):
        if not self.__service.is_data_loaded():
            print("[!] Silakan muat data terlebih dahulu di Menu 1.\n")
            return
            
        if show_header: print("--- HASIL ANALISIS KLIMATOLOGI LINGKUNGAN ---\n")
        else: print(" [4] ANALISIS IKLIM & LINGKUNGAN")
            
        result = self.__service.analyze_environmental()
        print(f"  ➢  Rata-rata Iklim   : Suhu {result['avg_temperature']:.2f}°C | Kelembaban {result['avg_humidity']:.2f}%")
        
        if detailed:
            print("  ➢  Detail Rentang Cuaca Ekstrem:")
            print(f"     - Suhu Ekstrem       : {result['min_temp']}°C s/d {result['max_temp']}°C")
            print(f"     - Kelembaban Ekstrem : {result['min_humidity']}% s/d {result['max_humidity']}%")
            
        if show_header: print()

    def __print_quarantine(self, show_header=True, detailed=False):
        if not self.__service.is_data_loaded():
            print("[!] Silakan muat data terlebih dahulu di Menu 1.\n")
            return
            
        if show_header: print("--- HASIL ANALISIS MANAJEMEN ISOLASI & PEMULIHAN ---\n")
        else: print(" [5] ANALISIS MANAJEMEN KARANTINA")
            
        result = self.__service.analyze_quarantine()
        print(f"  ➢  Rata-rata Durasi  : Karantina ({result['avg_quarantine_days']:.1f} hari) | Pulih ({result['avg_recovery_days']:.1f} hari)")
        
        if detailed:
            print("  ➢  Detail Rentang Waktu (Min/Max):")
            print(f"     - Masa Karantina : {result['min_q']} hari s/d {result['max_q']} hari")
            print(f"     - Masa Pemulihan : {result['min_r']} hari s/d {result['max_r']} hari")
            
        if show_header: print()

    def __print_strain(self, show_header=True):
        if not self.__service.is_data_loaded():
            print("[!] Silakan muat data terlebih dahulu di Menu 1.\n")
            return
            
        if show_header: print("--- HASIL ANALISIS KARAKTERISTIK STRAIN VIRUS ---\n")
        else: print(" [6] ANALISIS KARAKTERISTIK STRAIN")
            
        result = self.__service.analyze_strain()
        
        border = "+-----------------+--------------+-----------------+--------------------+"
        print("  " + border)
        print("  | {:<15} | {:^12} | {:^15} | {:^18} |".format("Nama Strain", "Total Kasus", "Fatalitas (CFR)", "Rata-rata Sembuh"))
        print("  " + border)
        
        for strain_name, info in result.items():
            fatality_str = f"{info['fatality_rate']:.2f}%"
            recovery_str = f"{info['avg_recovery_days']:.1f} hari"
            print("  | {:<15} | {:>12} | {:>15} | {:>18} |".format(strain_name, info['total_cases'], fatality_str, recovery_str))
            
        print("  " + border)
        if show_header: print()

    def __print_executive_summary(self):
        res_s = self.__service.analyze_strain()
        res_t = self.__service.analyze_transmission()

        most_common_strain = max(res_s.keys(), key=lambda k: res_s[k]['total_cases'])
        most_fatal_strain = max(res_s.keys(), key=lambda k: res_s[k]['fatality_rate'])

        print(" ╔" + "═" * 70 + "╗")
        print(f" ║{'KESIMPULAN EKSEKUTIF (EXECUTIVE SUMMARY)':^70}║")
        print(" ╠" + "═" * 70 + "╣")
        print(f" ║ - Strain Paling Mendominasi  : {most_common_strain:<38}║")
        print(f" ║   (Perlu alokasi obat/vaksin terbanyak){' ':>30}║")
        print(f" ║ - Strain Paling Mematikan    : {most_fatal_strain:<38}║")
        print(f" ║   (Membutuhkan ketersediaan ruang ICU paling banyak){' ':>17}║")
        print(f" ║ - Jalur Penularan Kritis     : Melalui {res_t['most_common_transmission']} {' ':>15}║")
        print(f" ║   di area {res_t['most_common_exposure']:<59}║")
        print(" ╠" + "-" * 70 + "╣")
        print(f" ║ [Rekomendasi Tindakan]:{' ':>46}║")
        print(f" ║ Tingkatkan standar kewaspadaan tinggi di area paparan utama. {' ':>8}║")
        print(f" ║ Alokasikan sumber daya medis ekstra untuk menangani dan {' ':>13}║")
        print(f" ║ mengisolasi pasien yang terinfeksi varian mematikan. {' ':>16}║")
        print(" ╚" + "═" * 70 + "╝\n")


if __name__ == "__main__":
    # INSTANSIASI OBJEK & WIRING : Menyusun relasi antar layer
    repository = HantaRepository("global_hantavirus_surveillance_dataset_2026.csv")
    service = HantaService(repository)
    app = MainMenu(service)
    app.run()