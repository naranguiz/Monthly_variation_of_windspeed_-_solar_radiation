#Librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

#Preparacion Base de Datos

#Paths

path1 = 'C:\\Users\\naran\\OneDrive\\Escritorio\\Algoritmo_Promedidador_Viento_Sol-20240826T014630Z-001\\Algoritmo_Promedidador_Viento_Sol\\DHC_E_KEYR60.csv'
path2 = 'C:\\Users\\naran\\OneDrive\\Escritorio\\Algoritmo_Promedidador_Viento_Sol-20240826T014630Z-001\\Algoritmo_Promedidador_Viento_Sol\\Separación Anual'
path3 = 'C:\\Users\\naran\\OneDrive\\Escritorio\\Algoritmo_Promedidador_Viento_Sol-20240826T014630Z-001\\Algoritmo_Promedidador_Viento_Sol\\Separación Mensual'
path4 = 'C:\\Users\\naran\\OneDrive\\Escritorio\\Algoritmo_Promedidador_Viento_Sol-20240826T014630Z-001\\Algoritmo_Promedidador_Viento_Sol\\wrf2010_WRDYU0.csv'
path5 = 'C:\\Users\\naran\\OneDrive\\Escritorio\\Algoritmo_Promedidador_Viento_Sol-20240826T014630Z-001\\Algoritmo_Promedidador_Viento_Sol\\wrf2015_OI7ASJ.csv'
path6 = 'C:\\Users\\naran\\OneDrive\\Escritorio\\Algoritmo_Promedidador_Viento_Sol-20240826T014630Z-001\\Algoritmo_Promedidador_Viento_Sol\\SeparaciónAnual_Viento'
path7 = 'C:\\Users\\naran\\OneDrive\\Escritorio\\Algoritmo_Promedidador_Viento_Sol-20240826T014630Z-001\\Algoritmo_Promedidador_Viento_Sol\\SeparaciónMensual_Viento'

#----------------------------------------Energía Eólica 2010 y 2015--------------------------------------------------------------------------------

#Series de viento
df_completo_viento2010 = pd.read_csv(path4,na_values=[" "])
df_completo_viento2015 = pd.read_csv(path5,na_values=[" "])
df_completo_viento =  pd.concat([df_completo_viento2010[['Fecha/Hora','5.5','10','20','30','40','50','60','70','80','90','100','120','140','160','180']], df_completo_viento2015[['Fecha/Hora','5.5','10','20','30','40','50','60','70','80','90','100','120','140','160','180']]], ignore_index=True)
df_completo_viento = df_completo_viento.interpolate()
df_completo_viento['Fecha/Hora'] = pd.to_datetime(df_completo_viento['Fecha/Hora'])
df_completo_viento['año'] = df_completo_viento['Fecha/Hora'].dt.year
#df_completo_viento.to_csv('viento_completo.csv', index=False)

#Listas para almacenar los dataframes anuales y mensuales
dataframes_anuales_viento = []
dataframes_mensuales_viento = []

# Itera sobre los años  en el dataframe
for año in df_completo_viento['año'].unique():
    # Filtra el dataframe por año
    df_anual_viento = df_completo_viento[df_completo_viento['año'] == año]
    # Agrega el dataframe anual a la lista
    dataframes_anuales_viento.append(df_anual_viento)


# Itera sobre cada dataframe anual en la lista dataframes_anuales
for df_anual_viento in dataframes_anuales_viento:

    # Crea una lista para almacenar los dataframes mensuales del año actual
    dataframes_mensuales_año_viento = []
    
    # Itera sobre cada mes en el año actual
    for mes in range(1, 13):
        # Filtra el dataframe anual por mes
        df_mensual_viento = df_anual_viento[df_anual_viento['Fecha/Hora'].dt.month == mes]
        # Agregamos la columna mes con el mes que corresponda
        df_mensual_viento['Mes'] = mes
        # Agrega el dataframe mensual a la lista
        dataframes_mensuales_año_viento.append(df_mensual_viento)
    # Extiende la lista de dataframes mensuales del año actual a la lista principal
    dataframes_mensuales_viento.extend(dataframes_mensuales_año_viento)

#Guardar df en Path6 y Path7
for i, df in enumerate(dataframes_anuales_viento):
    df.to_csv(f'{path6}/MedicionVientoAño_{i}.csv', index=False)
for i, df in enumerate(dataframes_mensuales_viento):
    df.to_csv(f'{path7}/MedicionVientoMensual_{i}.csv', index=False)


#-------------------------------------------Ploteo-Energía Eólica 2010 y 2015 --------------------------------------------------------------------

#-----------------------------------------2010 -----------------------------------------------------
# Obtener el primer dataframe de la lista dataframes_anuales
df_viento_2010 = dataframes_anuales_viento[0]
# Filtrar el dataframe para el año 2010
df_viento_2010 = df_viento_2010[df_viento_2010['año'] == 2010]
# Extraer los meses de la columna de fechas
meses = df_viento_2010['Fecha/Hora'].dt.month
# Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
#viento5_5 = df_viento_2010['5.5']
#viento_10 = df_viento_2010['10']
viento_20 = df_viento_2010['20']
viento_30 = df_viento_2010['30']
viento_40 = df_viento_2010['40']
viento_50 = df_viento_2010['50']
viento_60 = df_viento_2010['60']
#viento_70 = df_viento_2010['70']
#viento_80 = df_viento_2010['80']
#viento_90 = df_viento_2010['90']
#viento_100 = df_viento_2010['100']
#viento_120 = df_viento_2010['120']
#viento_140 = df_viento_2010['140']
#viento_160 = df_viento_2010['160']
#viento_180 = df_viento_2010['180']

# Calcular los promedios mensuales
#prom_viento5_5_2010 = df_viento_2010.groupby(meses)['5.5'].mean()
#prom_viento10_2010 = df_viento_2010.groupby(meses)['10'].mean()
prom_viento20_2010 = df_viento_2010.groupby(meses)['20'].mean()
prom_viento30_2010 = df_viento_2010.groupby(meses)['30'].mean()
prom_viento40_2010 = df_viento_2010.groupby(meses)['40'].mean()
prom_viento50_2010 = df_viento_2010.groupby(meses)['50'].mean()
prom_viento60_2010 = df_viento_2010.groupby(meses)['60'].mean()
#prom_viento70_2010 = df_viento_2010.groupby(meses)['70'].mean()
#prom_viento80_2010 = df_viento_2010.groupby(meses)['80'].mean()
#prom_viento90_2010 = df_viento_2010.groupby(meses)['90'].mean()
#prom_viento100_2010 = df_viento_2010.groupby(meses)['100'].mean()
#prom_viento120_2010 = df_viento_2010.groupby(meses)['120'].mean()
#prom_viento140_2010 = df_viento_2010.groupby(meses)['140'].mean()
#prom_viento160_2010 = df_viento_2010.groupby(meses)['160'].mean()
#prom_viento180_2010 = df_viento_2010.groupby(meses)['180'].mean()


# Graficar las columnas
#plt.plot(meses.unique(), prom_viento5_5_2010)
#plt.plot(meses.unique(), prom_viento10_2010)
plt.plot(meses.unique(), prom_viento20_2010,  label='Velocidad a 20 [m] de altura')
plt.plot(meses.unique(), prom_viento30_2010,  label='Velocidad a 30 [m] de altura')
plt.plot(meses.unique(), prom_viento40_2010,  label='Velocidad a 40 [m] de altura')
plt.plot(meses.unique(), prom_viento50_2010,  label='Velocidad a 50 [m] de altura')
plt.plot(meses.unique(), prom_viento60_2010,  label='Velocidad a 60 [m] de altura')
#plt.plot(meses.unique(), prom_viento70_2010)
#plt.plot(meses.unique(), prom_viento80_2010)
#plt.plot(meses.unique(), prom_viento90_2010,  label='Velocidad a 90 [m] de altura')
#plt.plot(meses.unique(), prom_viento100_2010)
#plt.plot(meses.unique(), prom_viento120_2010)
#plt.plot(meses.unique(), prom_viento140_2010)
#plt.plot(meses.unique(), prom_viento160_2010)
#plt.plot(meses.unique(), prom_viento180_2010)

#Puntos Importantes
plt.annotate('7.49 [m/s]', xy=(1, 7.49), xytext=(0.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Enero
plt.annotate('7.99 [m/s]', xy=(2, 7.99), xytext=(1.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Febrero
plt.annotate('6.85 [m/s]', xy=(3, 6.85), xytext=(2.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Marzo
plt.annotate('5.84 [m/s]', xy=(4, 5.84), xytext=(3.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Abril
plt.annotate('6.03 [m/s]', xy=(5, 6.03), xytext=(4.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Mayo
plt.annotate('7.95 [m/s]', xy=(6, 7.95), xytext=(5.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Junio
plt.annotate('8.75 [m/s]', xy=(7, 8.75), xytext=(6.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Julio
plt.annotate('8.08 [m/s]', xy=(8, 8.08), xytext=(7.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Agosto
plt.annotate('5.48 [m/s]', xy=(9, 5.50), xytext=(8.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Septiembre
plt.annotate('7.16 [m/s]', xy=(10, 7.16), xytext=(9.65, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Octubre
plt.annotate('7.92 [m/s]', xy=(11, 7.92), xytext=(10.65, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Noviembre
plt.annotate('7.21 [m/s]', xy=(12, 7.21), xytext=(11.65, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Diciembre

plt.grid(True)  
plt.yticks(range(0, 12, 1))
plt.xlabel('Meses')
plt.ylabel('Velocidad [m/s]')
plt.title('Promedio mensual de velocidad del viento en [m/s] para diferentes alturas - Año 2010')
plt.legend()
plt.xticks(rotation=45)
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.show()

#-----------------------------------------2015 -----------------------------------------------------

# Obtener el primer dataframe de la lista dataframes_anuales
df_viento_2015 = dataframes_anuales_viento[1]
# Filtrar el dataframe para el año 2015
df_viento_2015 = df_viento_2015[df_viento_2015['año'] == 2015]
# Extraer los meses de la columna de fechas
meses = df_viento_2015['Fecha/Hora'].dt.month
# Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
#viento5_5 = df_viento_2015['5.5']
#viento_10 = df_viento_2015['10']
viento_20 = df_viento_2015['20']
viento_30 = df_viento_2015['30']
viento_40 = df_viento_2015['40']
viento_50 = df_viento_2015['50']
viento_60 = df_viento_2015['60']
#viento_70 = df_viento_2015['70']
#viento_80 = df_viento_2015['80']
#viento_90 = df_viento_2015['90']
#viento_100 = df_viento_2015['100']
#viento_120 = df_viento_2015['120']
#viento_140 = df_viento_2015['140']
#viento_160 = df_viento_2015['160']
#viento_180 = df_viento_2015['180']

# Calcular los promedios mensuales
#prom_viento5_5_2015 = df_viento_2015.groupby(meses)['5.5'].mean()
#prom_viento10_2015 = df_viento_2015.groupby(meses)['10'].mean()
prom_viento20_2015 = df_viento_2015.groupby(meses)['20'].mean()
prom_viento30_2015 = df_viento_2015.groupby(meses)['30'].mean()
prom_viento40_2015 = df_viento_2015.groupby(meses)['40'].mean()
prom_viento50_2015 = df_viento_2015.groupby(meses)['50'].mean()
prom_viento60_2015 = df_viento_2015.groupby(meses)['60'].mean()
#prom_viento70_2015 = df_viento_2015.groupby(meses)['70'].mean()
#prom_viento80_2015 = df_viento_2015.groupby(meses)['80'].mean()
#prom_viento90_2015 = df_viento_2015.groupby(meses)['90'].mean()
#prom_viento100_2015 = df_viento_2015.groupby(meses)['100'].mean()
#prom_viento120_2015 = df_viento_2015.groupby(meses)['120'].mean()
#prom_viento140_2015 = df_viento_2015.groupby(meses)['140'].mean()
#prom_viento160_2015 = df_viento_2015.groupby(meses)['160'].mean()
#prom_viento180_2015 = df_viento_2015.groupby(meses)['180'].mean()


# Graficar las columnas
#plt.plot(meses.unique(), prom_viento5_5_2015)
#plt.plot(meses.unique(), prom_viento10_2015)
plt.plot(meses.unique(), prom_viento20_2015,  label='Velocidad a 20 [m] de altura')
plt.plot(meses.unique(), prom_viento30_2015,  label='Velocidad a 30 [m] de altura')
plt.plot(meses.unique(), prom_viento40_2015,  label='Velocidad a 40 [m] de altura')
plt.plot(meses.unique(), prom_viento50_2015,  label='Velocidad a 50 [m] de altura')
plt.plot(meses.unique(), prom_viento60_2015,  label='Velocidad a 60 [m] de altura')
#plt.plot(meses.unique(), prom_viento70_2015)
#plt.plot(meses.unique(), prom_viento80_2015)
#plt.plot(meses.unique(), prom_viento90_2015,  label='Velocidad a 90 [m] de altura')
#plt.plot(meses.unique(), prom_viento100_2015)
#plt.plot(meses.unique(), prom_viento120_2015)
#plt.plot(meses.unique(), prom_viento140_2015)
#plt.plot(meses.unique(), prom_viento160_2015)
#plt.plot(meses.unique(), prom_viento180_2015)

#Puntos Importantes
plt.annotate('8.55 [m/s]', xy=(1, 8.55), xytext=(0.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Enero
plt.annotate('8.54 [m/s]', xy=(2, 8.54), xytext=(1.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Febrero
plt.annotate('6.29 [m/s]', xy=(3, 6.29), xytext=(2.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Marzo
plt.annotate('6.19 [m/s]', xy=(4, 6.19), xytext=(3.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Abril
plt.annotate('6.30 [m/s]', xy=(5, 6.30), xytext=(4.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Mayo
plt.annotate('7.90 [m/s]', xy=(6, 7.90), xytext=(5.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Junio
plt.annotate('7.57 [m/s]', xy=(7, 7.57), xytext=(6.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Julio
plt.annotate('7.70 [m/s]', xy=(8, 7.70), xytext=(7.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Agosto
plt.annotate('7.12 [m/s]', xy=(9, 7.12), xytext=(8.65, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Septiembre
plt.annotate('6.83 [m/s]', xy=(10, 6.83), xytext=(9.65, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Octubre
plt.annotate('6.59 [m/s]', xy=(11, 6.59), xytext=(10.65, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Noviembre
plt.annotate('6.91 [m/s]', xy=(12, 6.91), xytext=(11.65, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Diciembre


plt.grid(True)  
plt.yticks(range(0, 12, 1))
plt.xlabel('Meses')
plt.ylabel('Velocidad [m/s]')
plt.title('Promedio mensual de velocidad del viento en [m/s] para diferentes alturas - Año 2015')
plt.legend()
plt.xticks(rotation=45)
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.show()








#--------------------------------------------Energía Solar 2004-2016-----------------------------------------------------------------------

#Series de radiación
df_completo = pd.read_csv(path1, na_values=[" "])
df_completo= df_completo.interpolate() 
columnasdiv = ['glb','dir','dif','sct','ghi','dirh','difh','dni']
df_completo[columnasdiv] = df_completo[columnasdiv] / 1000
df_completo['Fecha/Hora'] = pd.to_datetime(df_completo['Fecha/Hora'])
df_completo['año'] = df_completo['Fecha/Hora'].dt.year

# Listas para almacenar los dataframes anuales y mensuales
dataframes_anuales = []
dataframes_mensuales = []

# Itera sobre los años únicos en el dataframe
for año in df_completo['año'].unique():
    # Filtra el dataframe por año
    df_anual = df_completo[df_completo['año'] == año]
    # Agrega el dataframe anual a la lista
    dataframes_anuales.append(df_anual)


# Itera sobre cada dataframe anual en la lista dataframes_anuales
for df_anual in dataframes_anuales:

    # Crea una lista para almacenar los dataframes mensuales del año actual
    dataframes_mensuales_año = []
    
    # Itera sobre cada mes en el año actual
    for mes in range(1, 13):
        # Filtra el dataframe anual por mes
        df_mensual = df_anual[df_anual['Fecha/Hora'].dt.month == mes]
        # Agregamos la columna mes con el mes que corresponda
        df_mensual['Mes'] = mes
        # Agrega el dataframe mensual a la lista
        dataframes_mensuales_año.append(df_mensual)
    # Extiende la lista de dataframes mensuales del año actual a la lista principal
    dataframes_mensuales.extend(dataframes_mensuales_año)

# Imprime la dimensión de las listas
#print(len(dataframes_anuales))
#print(len(dataframes_mensuales))
#print(len(dataframes_anuales_viento))

#Guardar Lista en Path2 y Path3
for i, df in enumerate(dataframes_anuales):
    df.to_csv(f'{path2}/MedicionAño_{i}.csv', index=False)
for i, df in enumerate(dataframes_mensuales):
    df.to_csv(f'{path3}/MedicionMensual_{i}.csv', index=False)



# Ploteo Solar 2004/2016
#-----------------------------------------2004 -----------------------------------------------------
# Obtener el primer dataframe de la lista dataframes_anuales
#df_2004 = dataframes_anuales[0]
# Filtrar el dataframe para el año 2004
#df_2004 = df_2004[df_2004['año'] == 2004]
# Extraer los meses de la columna de fechas
#meses = df_2004['Fecha/Hora'].dt.month
## Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
#glb2004 = df_2004['glb']
#dir2004 = df_2004['dir']
#dif2004 = df_2004['dif']
#sct2004 = df_2004['sct']
#ghi2004 = df_2004['ghi']
#dirh2004 = df_2004['dirh']
#difh2004 = df_2004['difh']
#dni2004 = df_2004['dni']
## Calcular las sum mensuales
#sum_glb2004 = df_2004.groupby(meses)['glb'].sum()
#sum_dir2004 = df_2004.groupby(meses)['dir'].sum()
#sum_dif2004 = df_2004.groupby(meses)['dif'].sum()
#sum_sct2004 = df_2004.groupby(meses)['sct'].sum()
#sum_ghi2004 = df_2004.groupby(meses)['ghi'].sum()
#sum_dirh2004 = df_2004.groupby(meses)['dirh'].sum()
#sum_difh2004 = df_2004.groupby(meses)['difh'].sum()
#sum_dni2004 = df_2004.groupby(meses)['dni'].sum()
## Graficar las columnas
#plt.plot(meses.unique(), sum_glb2004, label='Global')
#plt.plot(meses.unique(), sum_dir2004, label='Directa')
#plt.plot(meses.unique(), sum_dif2004, label='Difusa')
#plt.plot(meses.unique(), sum_sct2004, label='Difusa Reflejada')
#plt.plot(meses.unique(), sum_ghi2004, label='Global Horizontal')
#plt.plot(meses.unique(), sum_dirh2004, label='Directa Horizontal')
#plt.plot(meses.unique(), sum_difh2004, label='Difusa Horizontal')
#plt.plot(meses.unique(), sum_dni2004, label='Directa Normal')
#plt.grid(True)  
#plt.yticks(range(0, 300, 25))
#plt.xlabel('Meses')
#plt.ylabel('[kW/m^2]')
#plt.title('Total de generación mensual en w/m^2 para cada tipo de radiación en el año 2004')
#plt.legend()
#plt.xticks(rotation=45)
#plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
#plt.show()
##-----------------------------------------2005-----------------------------------------------------
## Obtener el primer dataframe de la lista dataframes_anuales
#df_2005 = dataframes_anuales[1]
## Filtrar el dataframe para el año 2005
#df_2005 = df_2005[df_2005['año'] == 2005]
## Extraer los meses de la columna de fechas
#meses = df_2005['Fecha/Hora'].dt.month
## Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
#glb2005 = df_2005['glb']
#dir2005 = df_2005['dir']
#dif2005 = df_2005['dif']
#sct2005 = df_2005['sct']
#ghi2005 = df_2005['ghi']
#dirh2005 = df_2005['dirh']
#difh2005 = df_2005['difh']
#dni2005 = df_2005['dni']
## Calcular las sumas de radiación mensuales
#sum_glb2005 = df_2005.groupby(meses)['glb'].sum()
#sum_dir2005 = df_2005.groupby(meses)['dir'].sum()
#sum_dif2005 = df_2005.groupby(meses)['dif'].sum()
#sum_sct2005 = df_2005.groupby(meses)['sct'].sum()
#sum_ghi2005 = df_2005.groupby(meses)['ghi'].sum()
#sum_dirh2005 = df_2005.groupby(meses)['dirh'].sum()
#sum_difh2005 = df_2005.groupby(meses)['difh'].sum()
#sum_dni2005 = df_2005.groupby(meses)['dni'].sum()
## Graficar las columnas
#plt.plot(meses.unique(), sum_glb2005, label='Global')
#plt.plot(meses.unique(), sum_dir2005, label='Directa')
#plt.plot(meses.unique(), sum_dif2005, label='Difusa')
#plt.plot(meses.unique(), sum_sct2005, label='Difusa Reflejada')
#plt.plot(meses.unique(), sum_ghi2005, label='Global Horizontal')
#plt.plot(meses.unique(), sum_dirh2005, label='Directa Horizontal')
#plt.plot(meses.unique(), sum_difh2005, label='Difusa Horizontal')
#plt.plot(meses.unique(), sum_dni2005,  label='Directa Normal')
#plt.grid(True)  
#plt.yticks(range(0, 300, 25))
#plt.xlabel('Meses')
#plt.ylabel('[kW/m^2]')
#plt.title('Total de generación mensual en w/m^2 para cada tipo de radiación en el año 2005')
#plt.legend()
#plt.xticks(rotation=45)
#plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
#plt.show()

##-----------------------------------------2006-----------------------------------------------------
## Obtener el primer dataframe de la lista dataframes_anuales
#df_2006 = dataframes_anuales[2]
## Filtrar el dataframe para el año 2006
#df_2006 = df_2006[df_2006['año'] == 2006]
## Extraer los meses de la columna de fechas
#meses = df_2006['Fecha/Hora'].dt.month
## Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
#glb2006 = df_2006['glb']
#dir2006 = df_2006['dir']
#dif2006 = df_2006['dif']
#sct2006 = df_2006['sct']
#ghi2006 = df_2006['ghi']
#dirh2006 = df_2006['dirh']
#difh2006 = df_2006['difh']
#dni2006 = df_2006['dni']
## Calcular las sumas de radiación mensuales
#sum_glb2006 = df_2006.groupby(meses)['glb'].sum()
#sum_dir2006 = df_2006.groupby(meses)['dir'].sum()
#sum_dif2006 = df_2006.groupby(meses)['dif'].sum()
#sum_sct2006 = df_2006.groupby(meses)['sct'].sum()
#sum_ghi2006 = df_2006.groupby(meses)['ghi'].sum()
#sum_dirh2006 = df_2006.groupby(meses)['dirh'].sum()
#sum_difh2006 = df_2006.groupby(meses)['difh'].sum()
#sum_dni2006 = df_2006.groupby(meses)['dni'].sum()
## Graficar las columnas
#plt.plot(meses.unique(), sum_glb2006, label='Global')
#plt.plot(meses.unique(), sum_dir2006, label='Directa')
#plt.plot(meses.unique(), sum_dif2006, label='Difusa')
#plt.plot(meses.unique(), sum_sct2006, label='Difusa Reflejada')
#plt.plot(meses.unique(), sum_ghi2006, label='Global Horizontal')
#plt.plot(meses.unique(), sum_dirh2006, label='Directa Horizontal')
#plt.plot(meses.unique(), sum_difh2006, label='Difusa Horizontal')
#plt.plot(meses.unique(), sum_dni2006,  label='Directa Normal')
#plt.grid(True)  
#plt.yticks(range(0, 300, 25))
#plt.xlabel('Meses')
#plt.ylabel('[kW/m^2]')
#plt.title('Total de generación mensual en w/m^2 para cada tipo de radiación en el año 2006')
#plt.legend()
#plt.xticks(rotation=45)
#plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
#plt.show()
##-----------------------------------------2007-----------------------------------------------------
## Obtener el primer dataframe de la lista dataframes_anuales
#df_2007 = dataframes_anuales[3]
# Filtrar el dataframe para el año 2007
#df_2007 = df_2007[df_2007['año'] == 2007]
## Extraer los meses de la columna de fechas
#meses = df_2007['Fecha/Hora'].dt.month
## Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
#glb2007 = df_2007['glb']
#dir2007 = df_2007['dir']
#dif2007 = df_2007['dif']
#sct2007 = df_2007['sct']
#ghi2007 = df_2007['ghi']
#dirh2007 = df_2007['dirh']
#difh2007 = df_2007['difh']
#dni2007 = df_2007['dni']
## Calcular las sumas de radiación mensuales
#sum_glb2007 = df_2007.groupby(meses)['glb'].sum()
#sum_dir2007 = df_2007.groupby(meses)['dir'].sum()
#sum_dif2007 = df_2007.groupby(meses)['dif'].sum()
#sum_sct2007 = df_2007.groupby(meses)['sct'].sum()
#sum_ghi2007 = df_2007.groupby(meses)['ghi'].sum()
#sum_dirh2007 = df_2007.groupby(meses)['dirh'].sum()
#sum_difh2007 = df_2007.groupby(meses)['difh'].sum()
#sum_dni2007 = df_2007.groupby(meses)['dni'].sum()
## Graficar las columnas
#plt.plot(meses.unique(), sum_glb2007, label='Global')
#plt.plot(meses.unique(), sum_dir2007, label='Directa')
#plt.plot(meses.unique(), sum_dif2007, label='Difusa')
#plt.plot(meses.unique(), sum_sct2007, label='Difusa Reflejada')
#plt.plot(meses.unique(), sum_ghi2007, label='Global Horizontal')
#plt.plot(meses.unique(), sum_dirh2007, label='Directa Horizontal')
#plt.plot(meses.unique(), sum_difh2007, label='Difusa Horizontal')
#plt.plot(meses.unique(), sum_dni2007,  label='Directa Normal')
#plt.grid(True)  
#plt.yticks(range(0, 300, 25))
#plt.xlabel('Meses')
#plt.ylabel('[kW/m^2]')
#plt.title('Total de generación mensual en w/m^2 para cada tipo de radiación en el año 2007')
#plt.legend()
#plt.xticks(rotation=45)
#plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
#plt.show()
#-----------------------------------------2008-----------------------------------------------------
# Obtener el primer dataframe de la lista dataframes_anuales
#df_2008 = dataframes_anuales[4]
# Filtrar el dataframe para el año 2008
#df_2008 = df_2008[df_2008['año'] == 2008]
# Extraer los meses de la columna de fechas
#meses = df_2008['Fecha/Hora'].dt.month
# Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
#glb2008 = df_2008['glb']
#dir2008 = df_2008['dir']
#dif2008 = df_2008['dif']
#sct2008 = df_2008['sct']
#ghi2008 = df_2008['ghi']
#dirh2008 = df_2008['dirh']
#difh2008 = df_2008['difh']
#dni2008 = df_2008['dni']
# Calcular las sumas de radiación mensuales
#sum_glb2008 = df_2008.groupby(meses)['glb'].sum()
#sum_dir2008 = df_2008.groupby(meses)['dir'].sum()
#sum_dif2008 = df_2008.groupby(meses)['dif'].sum()
#sum_sct2008 = df_2008.groupby(meses)['sct'].sum()
#sum_ghi2008 = df_2008.groupby(meses)['ghi'].sum()
#sum_dirh2008 = df_2008.groupby(meses)['dirh'].sum()
#sum_difh2008 = df_2008.groupby(meses)['difh'].sum()
#sum_dni2008 = df_2008.groupby(meses)['dni'].sum()
# Graficar las columnas
#plt.plot(meses.unique(), sum_glb2008, label='Global')
#plt.plot(meses.unique(), sum_dir2008, label='Directa')
#plt.plot(meses.unique(), sum_dif2008, label='Difusa')
#plt.plot(meses.unique(), sum_sct2008, label='Difusa Reflejada')
#plt.plot(meses.unique(), sum_ghi2008, label='Global Horizontal')
#plt.plot(meses.unique(), sum_dirh2008, label='Directa Horizontal')
#plt.plot(meses.unique(), sum_difh2008, label='Difusa Horizontal')
#plt.plot(meses.unique(), sum_dni2008,  label='Directa Normal')
#plt.grid(True)  
#plt.yticks(range(0, 300, 25))
#plt.xlabel('Meses')
#plt.ylabel('[kW/m^2]')
#plt.title('Total de generación mensual en w/m^2 para cada tipo de radiación en el año 2008')
#plt.legend()
#plt.xticks(rotation=45)
#plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
#plt.show()
#-----------------------------------------2009-----------------------------------------------------
# Obtener el primer dataframe de la lista dataframes_anuales
#df_2009 = dataframes_anuales[5]
# Filtrar el dataframe para el año 2009
#df_2009 = df_2009[df_2009['año'] == 2009]
# Extraer los meses de la columna de fechas
#meses = df_2009['Fecha/Hora'].dt.month
## Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
#glb2008 = df_2009['glb']
#dir2009 = df_2009['dir']
#dif2009 = df_2009['dif']
#sct2009 = df_2009['sct']
#ghi2009 = df_2009['ghi']
#dirh2009 = df_2009['dirh']
#difh2009 = df_2009['difh']
#dni2009 = df_2009['dni']
# Calcular las sumas de radiación mensuales
#sum_glb2009 = df_2009.groupby(meses)['glb'].sum()
#sum_dir2009 = df_2009.groupby(meses)['dir'].sum()
#sum_dif2009 = df_2009.groupby(meses)['dif'].sum()
#sum_sct2009 = df_2009.groupby(meses)['sct'].sum()
#sum_ghi2009 = df_2009.groupby(meses)['ghi'].sum()
#sum_dirh2009 = df_2009.groupby(meses)['dirh'].sum()
#sum_difh2009 = df_2009.groupby(meses)['difh'].sum()
#sum_dni2009 = df_2009.groupby(meses)['dni'].sum()
# Graficar las columnas
#plt.plot(meses.unique(), sum_glb2009, label='Global')
#plt.plot(meses.unique(), sum_dir2009, label='Directa')
#plt.plot(meses.unique(), sum_dif2009, label='Difusa')
#plt.plot(meses.unique(), sum_sct2009, label='Difusa Reflejada')
#plt.plot(meses.unique(), sum_ghi2009, label='Global Horizontal')
#plt.plot(meses.unique(), sum_dirh2009, label='Directa Horizontal')
#plt.plot(meses.unique(), sum_difh2009, label='Difusa Horizontal')
#plt.plot(meses.unique(), sum_dni2009,  label='Directa Normal')
#plt.grid(True)  
#plt.yticks(range(0, 300, 25))
#plt.xlabel('Meses')
#plt.ylabel('[kW/m^2]')
#plt.title('Total de generación mensual en w/m^2 para cada tipo de radiación en el año 2009')
#plt.legend()
#plt.xticks(rotation=45)
#plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
#plt.show()
#-----------------------------------------2010-----------------------------------------------------
# Obtener el primer dataframe de la lista dataframes_anuales
df_2010 = dataframes_anuales[6]
# Filtrar el dataframe para el año 2010
df_2010 = df_2010[df_2010['año'] == 2010]
# Extraer los meses de la columna de fechas
meses = df_2010['Fecha/Hora'].dt.month
# Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
glb2010 = df_2010['glb']
dir2010 = df_2010['dir']
dif2010 = df_2010['dif']
#sct2010 = df_2010['sct']
ghi2010 = df_2010['ghi']
dirh2010 = df_2010['dirh']
difh2010= df_2010['difh']
dni2010 = df_2010['dni']

# Calcular las sumas de radiación mensuales
sum_glb2010 = df_2010.groupby(meses)['glb'].sum()
sum_dir2010 = df_2010.groupby(meses)['dir'].sum()
sum_dif2010 = df_2010.groupby(meses)['dif'].sum()
#sum_sct2010 = df_2010.groupby(meses)['sct'].sum()
sum_ghi2010 = df_2010.groupby(meses)['ghi'].sum()
sum_dirh2010 = df_2010.groupby(meses)['dirh'].sum()
sum_difh2010 = df_2010.groupby(meses)['difh'].sum()
sum_dni2010 = df_2010.groupby(meses)['dni'].sum()

#Puntos Importantes
plt.annotate('237 [kW/m$^2$]', xy=(1, 236.5), xytext=(0.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Enero
plt.annotate('188 [kW/m$^2$]', xy=(2, 188), xytext=(1.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Febrero
plt.annotate('136 [kW/m$^2$]', xy=(3, 136), xytext=(2.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Marzo
plt.annotate('101 [kW/m$^2$]', xy=(4, 101), xytext=(3.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Abril
plt.annotate('79  [kW/m$^2$]', xy=(5, 80.2), xytext=(4.58, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Mayo
plt.annotate('60 [kW/m$^2$]', xy=(6, 60.4), xytext=(5.60, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Junio
plt.annotate('62 [kW/m$^2$]', xy=(7, 62), xytext=(6.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Julio
plt.annotate('85 [kW/m$^2$]', xy=(8, 85), xytext=(7.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Agosto
plt.annotate('140 [kW/m$^2$]', xy=(9, 140), xytext=(8.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Septiembre
plt.annotate('165 [kW/m$^2$]', xy=(10, 165), xytext=(9.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Octubre
plt.annotate('180 [kW/m$^2$]', xy=(11, 180), xytext=(10.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Noviembre
plt.annotate('230 [kW/m$^2$]', xy=(12, 230), xytext=(11.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Diciembre


# Graficar las columnas
plt.plot(meses.unique(), sum_glb2010, label='Global')
plt.plot(meses.unique(), sum_dir2010, label='Directa')
plt.plot(meses.unique(), sum_dif2010, label='Difusa')
#plt.plot(meses.unique(), sum_sct2010, label='Difusa Reflejada')
plt.plot(meses.unique(), sum_ghi2010, label='Global Horizontal')
plt.plot(meses.unique(), sum_dirh2010, label='Directa Horizontal')
plt.plot(meses.unique(), sum_difh2010, label='Difusa Horizontal')
plt.plot(meses.unique(), sum_dni2010,  label='Directa Normal')
plt.grid(True)  
plt.yticks(range(0, 300, 25))
plt.xlabel('Meses')
plt.ylabel('Potencia [kW/m$^2$]')
plt.title('Total de generación mensual en [kW/m$^2$] para cada tipo de radiación - Año 2010')
plt.legend()
plt.xticks(rotation=45)
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.show()
#-----------------------------------------2011-----------------------------------------------------
#Obtener el primer dataframe de la lista dataframes_anuales
df_2011 = dataframes_anuales[7]
# Filtrar el dataframe para el año 2011
df_2011 = df_2011[df_2011['año'] == 2011]
# Extraer los meses de la columna de fechas
meses = df_2011['Fecha/Hora'].dt.month
# Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
glb2011 = df_2011['glb']
dir2011 = df_2011['dir']
dif2011 = df_2011['dif']
#sct2011 = df_2011['sct']
ghi2011 = df_2011['ghi']
dirh2011 = df_2011['dirh']
difh2011= df_2011['difh']
dni2011 = df_2011['dni']
# Calcular las sumas de radiación mensuales
sum_glb2011 = df_2011.groupby(meses)['glb'].sum()
sum_dir2011 = df_2011.groupby(meses)['dir'].sum()
sum_dif2011 = df_2011.groupby(meses)['dif'].sum()
#sum_sct2011 = df_2011.groupby(meses)['sct'].sum()
sum_ghi2011 = df_2011.groupby(meses)['ghi'].sum()
sum_dirh2011 = df_2011.groupby(meses)['dirh'].sum()
sum_difh2011 = df_2011.groupby(meses)['difh'].sum()
sum_dni2011 = df_2011.groupby(meses)['dni'].sum()

#Puntos Importantes
plt.annotate('228 [kW/m$^2$]', xy=(1, 228.85), xytext=(0.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Enero
plt.annotate('178 [kW/m$^2$]', xy=(2, 178.05), xytext=(1.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Febrero
plt.annotate('145 [kW/m$^2$]', xy=(3, 145.40), xytext=(2.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Marzo
plt.annotate('106 [kW/m$^2$]', xy=(4, 106.91), xytext=(3.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Abril
plt.annotate('61  [kW/m$^2$]', xy=(5, 61.81), xytext=(4.58, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Mayo
plt.annotate('45 [kW/m$^2$]', xy=(6, 45.61), xytext=(5.60, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Junio
plt.annotate('57 [kW/m$^2$]', xy=(7, 57.10), xytext=(6.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Julio
plt.annotate('95 [kW/m$^2$]', xy=(8, 95.65), xytext=(7.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Agosto
plt.annotate('121 [kW/m$^2$]', xy=(9, 121.51), xytext=(8.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Septiembre
plt.annotate('165 [kW/m$^2$]', xy=(10, 165.06), xytext=(9.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Octubre
plt.annotate('204 [kW/m$^2$]', xy=(11, 204.09), xytext=(10.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Noviembre
plt.annotate('254 [kW/m$^2$]', xy=(12, 254.55), xytext=(11.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Diciembre

# Graficar las columnas
plt.plot(meses.unique(), sum_glb2011, label='Global')
plt.plot(meses.unique(), sum_dir2011, label='Directa')
plt.plot(meses.unique(), sum_dif2011, label='Difusa')
#plt.plot(meses.unique(), sum_sct2011, label='Difusa Reflejada')
plt.plot(meses.unique(), sum_ghi2011, label='Global Horizontal')
plt.plot(meses.unique(), sum_dirh2011, label='Directa Horizontal')
plt.plot(meses.unique(), sum_difh2011, label='Difusa Horizontal')
plt.plot(meses.unique(), sum_dni2011,  label='Directa Normal')
plt.grid(True)  
plt.yticks(range(0, 300, 25))
plt.xlabel('Meses')
plt.ylabel('Potencia [kW/m$^2$]')
plt.title('Total de generación mensual en [kW/m$^2$] para cada tipo de radiación - Año 2011')
plt.legend()
plt.xticks(rotation=45)
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.show()
#-----------------------------------------2012-----------------------------------------------------
#Obtener el primer dataframe de la lista dataframes_anuales
df_2012 = dataframes_anuales[8]
# Filtrar el dataframe para el año 2012
df_2012 = df_2012[df_2012['año'] == 2012]
# Extraer los meses de la columna de fechas
meses = df_2012['Fecha/Hora'].dt.month
# Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
glb2012 = df_2012['glb']
dir2012 = df_2012['dir']
dif2012 = df_2012['dif']
#sct2012 = df_2012['sct']
ghi2012 = df_2012['ghi']
dirh2012 = df_2012['dirh']
difh2012= df_2012['difh']
dni2012 = df_2012['dni']
# Calcular las sumas de radiación mensuales
sum_glb2012 = df_2012.groupby(meses)['glb'].sum()
sum_dir2012 = df_2012.groupby(meses)['dir'].sum()
sum_dif2012 = df_2012.groupby(meses)['dif'].sum()
#sum_sct2012 = df_2012.groupby(meses)['sct'].sum()
sum_ghi2012 = df_2012.groupby(meses)['ghi'].sum()
sum_dirh2012 = df_2012.groupby(meses)['dirh'].sum()
sum_difh2012 = df_2012.groupby(meses)['difh'].sum()
sum_dni2012 = df_2012.groupby(meses)['dni'].sum()
#Puntos Importantes
plt.annotate('225[kW/m$^2$]', xy=(1, 225.49), xytext=(0.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Enero
plt.annotate('178 [kW/m$^2$]', xy=(2, 178.78), xytext=(1.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Febrero
plt.annotate('146 [kW/m$^2$]', xy=(3, 146.10), xytext=(2.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Marzo
plt.annotate('99 [kW/m$^2$]', xy=(4, 99.32), xytext=(3.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Abril
plt.annotate('47  [kW/m$^2$]', xy=(5, 47.68), xytext=(4.58, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Mayo
plt.annotate('38 [kW/m$^2$]', xy=(6, 38.00), xytext=(5.60, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Junio
plt.annotate('53 [kW/m$^2$]', xy=(7, 53.96), xytext=(6.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Julio
plt.annotate('55 [kW/m$^2$]', xy=(8, 55.55), xytext=(7.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Agosto
plt.annotate('122 [kW/m$^2$]', xy=(9, 122.57), xytext=(8.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Septiembre
plt.annotate('201 [kW/m$^2$]', xy=(10, 201.55), xytext=(9.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Octubre
plt.annotate('216 [kW/m$^2$]', xy=(11, 216.23), xytext=(10.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Noviembre
plt.annotate('207 [kW/m$^2$]', xy=(12, 207.56), xytext=(11.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Diciembre
# Graficar las columnas
plt.plot(meses.unique(), sum_glb2012, label='Global')
plt.plot(meses.unique(), sum_dir2012, label='Directa')
plt.plot(meses.unique(), sum_dif2012, label='Difusa')
#plt.plot(meses.unique(), sum_sct2012, label='Difusa Reflejada')
plt.plot(meses.unique(), sum_ghi2012, label='Global Horizontal')
plt.plot(meses.unique(), sum_dirh2012, label='Directa Horizontal')
plt.plot(meses.unique(), sum_difh2012, label='Difusa Horizontal')
plt.plot(meses.unique(), sum_dni2012,  label='Directa Normal')
plt.grid(True)  
plt.yticks(range(0, 300, 25))
plt.xlabel('Meses')
plt.ylabel('Potencia [kW/m$^2$]')
plt.title('Total de generación mensual en [kW/m$^2$] para cada tipo de radiación - Año 2012')
plt.legend()
plt.xticks(rotation=45)
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.show()
#-----------------------------------------2013-----------------------------------------------------
#Obtener el primer dataframe de la lista dataframes_anuales
df_2013 = dataframes_anuales[9]
# Filtrar el dataframe para el año 2013
df_2013 = df_2013[df_2013['año'] == 2013]
# Extraer los meses de la columna de fechas
meses = df_2013['Fecha/Hora'].dt.month
# Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
glb2013 = df_2013['glb']
dir2013 = df_2013['dir']
dif2013 = df_2013['dif']
#sct2013 = df_2013['sct']
ghi2013 = df_2013['ghi']
dirh2013 = df_2013['dirh']
difh2013= df_2013['difh']
dni2013 = df_2013['dni']
# Calcular las sumas de radiación mensuales
sum_glb2013 = df_2013.groupby(meses)['glb'].sum()
sum_dir2013 = df_2013.groupby(meses)['dir'].sum()
sum_dif2013 = df_2013.groupby(meses)['dif'].sum()
#sum_sct2013 = df_2013.groupby(meses)['sct'].sum()
sum_ghi2013 = df_2013.groupby(meses)['ghi'].sum()
sum_dirh2013 = df_2013.groupby(meses)['dirh'].sum()
sum_difh2013 = df_2013.groupby(meses)['difh'].sum()
sum_dni2013 = df_2013.groupby(meses)['dni'].sum()
#Puntos Importantes
plt.annotate('233 [kW/m$^2$]', xy=(1, 233.40), xytext=(0.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Enero
plt.annotate('176 [kW/m$^2$]', xy=(2, 176.28), xytext=(1.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Febrero
plt.annotate('158 [kW/m$^2$]', xy=(3, 158.57), xytext=(2.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Marzo
plt.annotate('81 [kW/m$^2$]', xy=(4, 81.5), xytext=(3.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Abril
plt.annotate('68  [kW/m$^2$]', xy=(5, 68.4), xytext=(4.58, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Mayo
plt.annotate('50 [kW/m$^2$]', xy=(6, 50.12), xytext=(5.60, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Junio
plt.annotate('46 [kW/m$^2$]', xy=(7, 46.49), xytext=(6.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Julio
plt.annotate('71 [kW/m$^2$]', xy=(8, 71.13), xytext=(7.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Agosto
plt.annotate('111 [kW/m$^2$]', xy=(9, 111.49), xytext=(8.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Septiembre
plt.annotate('150 [kW/m$^2$]', xy=(10, 150.00), xytext=(9.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Octubre
plt.annotate('202 [kW/m$^2$]', xy=(11, 202.43), xytext=(10.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Noviembre
plt.annotate('259 [kW/m$^2$]', xy=(12, 259.63), xytext=(11.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Diciembre
# Graficar las columnas
plt.plot(meses.unique(), sum_glb2013, label='Global')
plt.plot(meses.unique(), sum_dir2013, label='Directa')
plt.plot(meses.unique(), sum_dif2013, label='Difusa')
#plt.plot(meses.unique(), sum_sct2013, label='Difusa Reflejada')
plt.plot(meses.unique(), sum_ghi2013, label='Global Horizontal')
plt.plot(meses.unique(), sum_dirh2013, label='Directa Horizontal')
plt.plot(meses.unique(), sum_difh2013, label='Difusa Horizontal')
plt.plot(meses.unique(), sum_dni2013,  label='Directa Normal')
plt.grid(True)  
plt.yticks(range(0, 300, 25))
plt.xlabel('Meses')
plt.ylabel('Potencia [kW/m$^2$]')
plt.title('Total de generación mensual en [kW/m$^2$] para cada tipo de radiación- Año 2013')
plt.legend()
plt.xticks(rotation=45)
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.show()
#-----------------------------------------2014-----------------------------------------------------
#Obtener el primer dataframe de la lista dataframes_anuales
df_2014 = dataframes_anuales[10]
# Filtrar el dataframe para el año 2014
df_2014 = df_2014[df_2014['año'] == 2014]
# Extraer los meses de la columna de fechas
meses = df_2014['Fecha/Hora'].dt.month
# Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
glb2014 = df_2014['glb']
dir2014 = df_2014['dir']
dif2014 = df_2014['dif']
#sct2014 = df_2014['sct']
ghi2014 = df_2014['ghi']
dirh2014 = df_2014['dirh']
difh2014= df_2014['difh']
dni2014 = df_2014['dni']
# Calcular las sumas de radiación mensuales
sum_glb2014 = df_2014.groupby(meses)['glb'].sum()
sum_dir2014 = df_2014.groupby(meses)['dir'].sum()
sum_dif2014 = df_2014.groupby(meses)['dif'].sum()
#sum_sct2014 = df_2014.groupby(meses)['sct'].sum()
sum_ghi2014 = df_2014.groupby(meses)['ghi'].sum()
sum_dirh2014 = df_2014.groupby(meses)['dirh'].sum()
sum_difh2014 = df_2014.groupby(meses)['difh'].sum()
sum_dni2014 = df_2014.groupby(meses)['dni'].sum()
#Puntos Importantes
plt.annotate('242 [kW/m$^2$]', xy=(1, 242.07), xytext=(0.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Enero
plt.annotate('190 [kW/m$^2$]', xy=(2, 190.68), xytext=(1.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Febrero
plt.annotate('137 [kW/m$^2$]', xy=(3, 137.96), xytext=(2.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Marzo
plt.annotate('83 [kW/m$^2$]', xy=(4, 83.82), xytext=(3.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Abril
plt.annotate('44  [kW/m$^2$]', xy=(5, 44.80), xytext=(4.58, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Mayo
plt.annotate('35 [kW/m$^2$]', xy=(6, 35.28), xytext=(5.60, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Junio
plt.annotate('43 [kW/m$^2$]', xy=(7, 43.01), xytext=(6.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Julio
plt.annotate('60 [kW/m$^2$]', xy=(8, 60.23), xytext=(7.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Agosto
plt.annotate('97 [kW/m$^2$]', xy=(9, 97.44), xytext=(8.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Septiembre
plt.annotate('172 [kW/m$^2$]', xy=(10, 172.70), xytext=(9.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Octubre
plt.annotate('200 [kW/m$^2$]', xy=(11, 200.88), xytext=(10.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Noviembre
plt.annotate('243 [kW/m$^2$]', xy=(12, 243.21), xytext=(11.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Diciembre
# Graficar las columnas
plt.plot(meses.unique(), sum_glb2014, label='Global')
plt.plot(meses.unique(), sum_dir2014, label='Directa')
plt.plot(meses.unique(), sum_dif2014, label='Difusa')
#plt.plot(meses.unique(), sum_sct2014, label='Difusa Reflejada')
plt.plot(meses.unique(), sum_ghi2014, label='Global Horizontal')
plt.plot(meses.unique(), sum_dirh2014, label='Directa Horizontal')
plt.plot(meses.unique(), sum_difh2014, label='Difusa Horizontal')
plt.plot(meses.unique(), sum_dni2014,  label='Directa Normal')
plt.grid(True)  
plt.yticks(range(0, 300, 25))
plt.xlabel('Meses')
plt.ylabel('Potencia [kW/m$^2$]')
plt.title('Total de generación mensual en [kW/m$^2$] para cada tipo de radiación - Año 2014')
plt.legend()
plt.xticks(rotation=45)
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.show()
#-----------------------------------------2015-----------------------------------------------------
#Obtener el primer dataframe de la lista dataframes_anuales
df_2015 = dataframes_anuales[11]
# Filtrar el dataframe para el año 2015
df_2015 = df_2015[df_2015['año'] == 2015]
# Extraer los meses de la columna de fechas
meses = df_2015['Fecha/Hora'].dt.month
# Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
glb2015 = df_2015['glb']
dir2015 = df_2015['dir']
dif2015 = df_2015['dif']
#sct2015 = df_2015['sct']
ghi2015 = df_2015['ghi']
dirh2015 = df_2015['dirh']
difh2015= df_2015['difh']
dni2015 = df_2015['dni']
# Calcular las sumas de radiación mensuales
sum_glb2015 = df_2015.groupby(meses)['glb'].sum()
sum_dir2015 = df_2015.groupby(meses)['dir'].sum()
sum_dif2015 = df_2015.groupby(meses)['dif'].sum()
#sum_sct2015 = df_2015.groupby(meses)['sct'].sum()
sum_ghi2015 = df_2015.groupby(meses)['ghi'].sum()
sum_dirh2015 = df_2015.groupby(meses)['dirh'].sum()
sum_difh2015 = df_2015.groupby(meses)['difh'].sum()
sum_dni2015 = df_2015.groupby(meses)['dni'].sum()
#Puntos Importantes
plt.annotate('260 [kW/m$^2$]', xy=(1, 260.50), xytext=(0.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Enero
plt.annotate('201 [kW/m$^2$]', xy=(2, 201.82), xytext=(1.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Febrero
plt.annotate('176 [kW/m$^2$]', xy=(3, 176.39), xytext=(2.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Marzo
plt.annotate('92 [kW/m$^2$]', xy=(4, 92.08), xytext=(3.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Abril
plt.annotate('57  [kW/m$^2$]', xy=(5, 57.57), xytext=(4.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Mayo
plt.annotate('43 [kW/m$^2$]', xy=(6, 43.65), xytext=(5.60, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Junio
plt.annotate('44 [kW/m$^2$]', xy=(7, 44.11), xytext=(6.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Julio
plt.annotate('60 [kW/m$^2$]', xy=(8, 60.53), xytext=(7.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Agosto
plt.annotate('112 [kW/m$^2$]', xy=(9, 112.52), xytext=(8.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Septiembre
plt.annotate('182 [kW/m$^2$]', xy=(10, 182.77), xytext=(9.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Octubre
plt.annotate('199 [kW/m$^2$]', xy=(11, 199.79), xytext=(10.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Noviembre
plt.annotate('249 [kW/m$^2$]', xy=(12, 249.57), xytext=(11.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Diciembre
# Graficar las columnas
plt.plot(meses.unique(), sum_glb2015, label='Global')
plt.plot(meses.unique(), sum_dir2015, label='Directa')
plt.plot(meses.unique(), sum_dif2015, label='Difusa')
#plt.plot(meses.unique(), sum_sct2015, label='Difusa Reflejada')
plt.plot(meses.unique(), sum_ghi2015, label='Global Horizontal')
plt.plot(meses.unique(), sum_dirh2015, label='Directa Horizontal')
plt.plot(meses.unique(), sum_difh2015, label='Difusa Horizontal')
plt.plot(meses.unique(), sum_dni2015,  label='Directa Normal')
plt.grid(True)  
plt.yticks(range(0, 300, 25))
plt.xlabel('Meses')
plt.ylabel('Potencia [kW/m$^2$]')
plt.title('Total de generación mensual en [kW/m$^2$] para cada tipo de radiación - Año 2015')
plt.legend()
plt.xticks(rotation=45)
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.show()
#-----------------------------------------2016-----------------------------------------------------
#Obtener el primer dataframe de la lista dataframes_anuales
df_2016 = dataframes_anuales[12]
# Filtrar el dataframe para el año 2016
df_2016 = df_2016[df_2016['año'] == 2016]
# Extraer los meses de la columna de fechas
meses = df_2016['Fecha/Hora'].dt.month
# Obtener los valores de las columnas 'glb', 'dir', 'dif', 'sct', 'ghi', 'dirh' y 'dni'
glb2016 = df_2016['glb']
dir2016 = df_2016['dir']
dif2016 = df_2016['dif']
#sct2016 = df_2016['sct']
ghi2016 = df_2016['ghi']
dirh2016 = df_2016['dirh']
difh2016= df_2016['difh']
dni2016 = df_2016['dni']
# Calcular las sumas de radiación mensuales
sum_glb2016 = df_2016.groupby(meses)['glb'].sum()
sum_dir2016 = df_2016.groupby(meses)['dir'].sum()
sum_dif2016 = df_2016.groupby(meses)['dif'].sum()
#sum_sct2016 = df_2016.groupby(meses)['sct'].sum()
sum_ghi2016 = df_2016.groupby(meses)['ghi'].sum()
sum_dirh2016 = df_2016.groupby(meses)['dirh'].sum()
sum_difh2016 = df_2016.groupby(meses)['difh'].sum()
sum_dni2016 = df_2016.groupby(meses)['dni'].sum()
#Puntos Importantes
plt.annotate('244 [kW/m$^2$]', xy=(1, 244.56), xytext=(0.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Enero
plt.annotate('206 [kW/m$^2$]', xy=(2, 206.96), xytext=(1.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Febrero
plt.annotate('171 [kW/m$^2$]', xy=(3, 171.73), xytext=(2.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Marzo
plt.annotate('101 [kW/m$^2$]', xy=(4, 101.70), xytext=(3.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Abril
plt.annotate('53  [kW/m$^2$]', xy=(5, 53.05), xytext=(4.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Mayo
plt.annotate('63 [kW/m$^2$]', xy=(6, 63.55), xytext=(5.60, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Junio
plt.annotate('45 [kW/m$^2$]', xy=(7, 45.60), xytext=(6.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Julio
plt.annotate('75 [kW/m$^2$]', xy=(8, 75.50), xytext=(7.59, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Agosto
plt.annotate('116 [kW/m$^2$]', xy=(9, 116.52), xytext=(8.55, 1), arrowprops=dict(color='black',arrowstyle='simple')) #Septiembre
plt.annotate('154 [kW/m$^2$]', xy=(10, 154.95), xytext=(9.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Octubre
plt.annotate('208 [kW/m$^2$]', xy=(11, 208.65), xytext=(10.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Noviembre
plt.annotate('209 [kW/m$^2$]', xy=(12, 209.90), xytext=(11.55, 1), arrowprops=dict(color='black',arrowstyle='simple'))#Diciembre
# Graficar las columnas
plt.plot(meses.unique(), sum_glb2016, label='Global')
plt.plot(meses.unique(), sum_dir2016, label='Directa')
plt.plot(meses.unique(), sum_dif2016, label='Difusa')
#plt.plot(meses.unique(), sum_sct2016, label='Difusa Reflejada')
plt.plot(meses.unique(), sum_ghi2016, label='Global Horizontal')
plt.plot(meses.unique(), sum_dirh2016, label='Directa Horizontal')
plt.plot(meses.unique(), sum_difh2016, label='Difusa Horizontal')
plt.plot(meses.unique(), sum_dni2016,  label='Directa Normal')
plt.grid(True)  
plt.yticks(range(0, 300, 25))
plt.xlabel('Meses')
plt.ylabel('Potencia [kW/m$^2$]')
plt.title('Total de generación mensual en [kW/m$^2$] para cada tipo de radiación - Año 2016')
plt.legend()
plt.xticks(rotation=45)
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.show()


#Testing

#Comprobación2005
sumagbla2005 = dataframes_mensuales[12]
suma_gblb2005 = sumagbla2005['glb'].sum() +  sumagbla2005['dir'].sum() +  sumagbla2005['dif'].sum() + sumagbla2005['sct'].sum() +  sumagbla2005['ghi'].sum() + sumagbla2005['dirh'].sum() +  sumagbla2005['difh'].sum() + sumagbla2005['dni'].sum()
suma_gblb22005 = sumagbla2005['glb'].sum()
print("La suma de todas las radiaciones para el mes de enero del año 2005 es:", suma_gblb2005, '[kW/m^2]')
print("La suma de toda la columna de radiación global para el mes de enero del año 2005 es:", suma_gblb22005, '[kW/m^2]')

#Comprobación2010_viento
promediogbla2010 = dataframes_mensuales_viento[0]
promedio_gblb2010 = promediogbla2010['5.5'].mean()
promedio_gblb22010 = promediogbla2010['30'].mean()
print("La velocidad promedio del viento a 5.5[m] en el mes de enero del año 2010 es:", promedio_gblb2010, '[m/s]')
print("La velocidad promedio del viento a 10[m] en el mes de enero del año 2010 es:" , promedio_gblb22010, '[m/s]')
