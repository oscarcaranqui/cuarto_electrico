from pdf2image import convert_from_path
from v1.energy import Response, Medidor
from from_dict import from_dict
from fpdf import FPDF
import os
import json
import time
import pytz
import datetime

user_current_directory = os.getcwd()
directory_save_path_logo_siemav = os.path.join(user_current_directory, "v1/LOGO_SIEMAV.jpg")
directory_save_path_logo_santa_priscila = os.path.join(user_current_directory, "v1/SP.jpg")
directory_path_document = os.path.join(user_current_directory, "path_of_document")
directory_path_of_images = os.path.join(user_current_directory, "path_of_images")


class Document:

    def new_page_pdf(self):
        self.pdf.add_page()

    def save_pdf(self, name_directory):
        self.pdf.output(name=name_directory)

    def titule(self):
        self.pdf.set_font("Arial", style="", size=12)
        self.pdf.set_xy(x=110, y=10)
        self.pdf.cell(w=40, h=10, txt="REPORTE DE CUARTOS ELECTRICOS", border=0, align='C', fill=False)

    def variable_electric(self):
        line_breaks = 5
        self.pdf.set_font("Arial", style="", size=8)
        self.pdf.set_xy(x=10, y=40)

        self.pdf.set_fill_color(203, 211, 226)
        self.pdf.rect(x=10, y=42, w=297 - 20, h=15, style="F")
        self.pdf.cell(w=27, h=10, txt="Voltaje V12 [V]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="Voltaje V23 [V]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="Voltaje V31 [V]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)

        self.pdf.set_fill_color(249, 247, 210)
        self.pdf.rect(x=10, y=57, w=297 - 20, h=15, style="F")
        self.pdf.cell(w=27, h=10, txt="Voltaje V1 [V]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="Voltaje V2 [V]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="Voltaje V3 [V]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)

        self.pdf.set_fill_color(203, 211, 226)
        self.pdf.rect(x=10, y=72, w=297 - 20, h=15, style="F")
        self.pdf.cell(w=27, h=10, txt="Corriente I1 [A]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="Corriente I2 [A]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="Corriente I3 [A]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)

        self.pdf.set_fill_color(249, 247, 210)
        self.pdf.rect(x=10, y=87, w=297 - 20, h=15, style="F")
        self.pdf.cell(w=27, h=10, txt="Fp I1", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="Fp I2", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="Fp I3", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)

        self.pdf.set_fill_color(203, 211, 226)
        self.pdf.rect(x=10, y=102, w=297 - 20, h=20, style="F")
        self.pdf.cell(w=27, h=10, txt="P1 [kW]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="P2 [kW]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="P3 [kW]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="Ptotal [kW]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)

        self.pdf.set_fill_color(249, 247, 210)
        self.pdf.rect(x=10, y=122, w=297 - 20, h=20, style="F")
        self.pdf.cell(w=27, h=10, txt="Q1 [kVAR]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="Q2 [kVAR]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="Q3 [kVAR]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="Qtotal [kVAR]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)

        self.pdf.set_fill_color(203, 211, 226)
        self.pdf.rect(x=10, y=142, w=297 - 20, h=20, style="F")
        self.pdf.cell(w=27, h=10, txt="S1 [kVA]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="S2 [kVA]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="S3 [kVA]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)
        self.pdf.cell(w=27, h=10, txt="Stotal [kVA]", border=0, align='C', fill=False)
        self.pdf.ln(line_breaks)

    def border(self, offset_x=0):
        self.pdf.rect(x=10, y=10, w=297-10-10, h=210-10-10)
        self.pdf.line(x1=10, y1=30, x2=297 - 10, y2=30)

        line_horizontal = 25
        for i in range(1, line_horizontal + 1):
            self.pdf.line(x1=10 + offset_x, y1=37 + 5*i, x2=297 - 10 + offset_x, y2=37 + 5*i)

        line_vertical = 31
        for i in range(1, line_vertical + 2):
            self.pdf.line(x1=27 + 8*i + offset_x, y1=42, x2=27 + 8*i + offset_x, y2=200)

    def logos(self, offset_x=0):
        siemav = directory_save_path_logo_siemav
        self.pdf.image(siemav, x=267.5 + offset_x, y=10.5, w=17, h=17)
        santa_priscila = directory_save_path_logo_santa_priscila
        self.pdf.image(santa_priscila, x=245 + offset_x, y=10.5, w=19, h=19)

    def create_document(self, name_directory, data):
        self.pdf = FPDF(orientation="L", format="A4", unit="mm")
        self.new_page_pdf()
        self.titule()
        self.variable_electric()
        self.border(offset_x=0)
        self.logos(offset_x=0)
        self.info(data)
        self.save_pdf(name_directory=name_directory)

    def Schneider_PM5500(self, offset_x, medidor):
        self.pdf.set_font("Arial", style="", size=4)

        self.pdf.set_xy(x=30 + offset_x, y=40)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.voltage_ab)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=45)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.voltage_bc)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=50)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.voltage_ca)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=55)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.voltage_an)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=60)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.voltage_bn)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=65)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.voltage_cn)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=70)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.current_a)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=75)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.current_b)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=80)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.current_c)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=85)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.power_factor_a)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=90)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.power_factor_b)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=95)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.power_factor_c)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=100)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.active_power_a)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=105)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.active_power_b)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=110)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.active_power_c)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=115)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.active_power_total)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=120)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.reactive_power_a)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=125)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.reactive_power_b)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=130)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.reactive_power_c)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=135)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.reactive_power_total)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=140)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.apparent_power_a)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=145)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.apparent_power_b)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=150)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.apparent_power_c)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=155)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.apparent_power_total)), align='C')

    def Satec_PM135EH(self, offset_x, medidor):
        self.pdf.set_font("Arial", style="", size=4)

        self.pdf.set_xy(x=30 + offset_x, y=40)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.v12_voltage)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=45)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.v23_voltage)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=50)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.v31_voltage)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=55)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.v1_v12_demand)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=60)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.v2_v23_demand)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=65)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.v3_v31_demand)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=70)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.i1_current)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=75)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.i2_current)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=80)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.i3_current)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=85)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.power_factor_l1)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=90)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.power_factor_l2)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=95)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.power_factor_l3)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=100)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.kw_l1)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=105)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.kw_l2)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=110)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.kw_l3)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=115)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.total_kw)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=120)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.kvar_l1)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=125)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.kvar_l2)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=130)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.kvar_l3)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=135)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.total_kvar)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=140)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.kva_l1)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=145)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.kva_l2)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=150)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.kva_l3)), align='C')

        self.pdf.set_xy(x=30 + offset_x, y=155)
        self.pdf.cell(w=18, h=10, txt=str("{:.2f}".format(medidor.total_kva)), align='C')

    def info(self, message_received):
        offset_x = 0
        len_rectangular = 0

        for i in range(0, len(message_received)):
            my_dict = json.loads(message_received[i].payload)
            response: Response = from_dict(Response, my_dict)
            medidores_ok = 0
            print(response)
            for j in range(0, len(response.medidores)):
                medidor: Medidor = from_dict(Medidor, response.medidores[j])

                if medidor.status == "OK":
                    self.pdf.set_font("Arial", style="", size=5)
                    self.pdf.set_xy(x=37 + offset_x, y=182)
                    self.pdf.rotate(90)
                    application = str(medidor.address.aplicacion).upper()
                    self.pdf.cell(w=2, h=2, txt=application, align='C')
                    self.pdf.set_xy(x=37 + offset_x, y=185)
                    self.pdf.cell(w=2, h=2, txt=str(response.date), align='C')
                    self.pdf.rotate(0)

                    if message_received[i].topic.split("/")[0].upper() == "TAURA_2":
                        self.Satec_PM135EH(offset_x, medidor)
                    else:
                        self.Schneider_PM5500(offset_x, medidor)

                    offset_x = offset_x + 8
                    medidores_ok = medidores_ok + 1

            if medidores_ok > 0:
                sector = message_received[i].topic.split("/")[0]
                cantidad_de_medidores = medidores_ok
                self.pdf.set_font("Arial", style="", size=4)
                self.pdf.set_fill_color(239, 238, 224)
                self.pdf.set_xy(x=35 + len_rectangular, y=30)
                header_sector = str(sector).upper()
                self.pdf.cell(w=8 * cantidad_de_medidores, h=12, txt= header_sector, align='C', border=1, fill=True)
                # self.pdf.multi_cell(w=8 * cantidad_de_medidores, h=6, txt= header_sector, align='C', border=1, fill=True)
                len_rectangular = len_rectangular + cantidad_de_medidores * 8

    def create_name_directory(self):
        current_time = datetime.datetime.now()
        ecuador_tz = pytz.timezone('America/Guayaquil')
        ecuador_time = current_time.astimezone(ecuador_tz)
        formatted_date = ecuador_time.strftime("%d_%m_%Y__%H_%M_%S")
        name_file = formatted_date + ".pdf"
        directory_save_path_document_without_ext = formatted_date
        directory_save_path_document_pdf = os.path.join(directory_path_document, name_file)
        return [directory_save_path_document_pdf, directory_save_path_document_without_ext]

    def write_pdf(self, payload: list):
        self.create_document(name_directory=self.create_name_directory()[0],
                             data=payload)
        pages = convert_from_path(self.create_name_directory()[0])
        directory_save_image = os.path.join(directory_path_of_images, self.create_name_directory()[1]) + '.png'
        pages[0].save(directory_save_image, 'png')
        return directory_save_image

DOCUMENT = Document()
