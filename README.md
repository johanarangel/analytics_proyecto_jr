Autor: Johana Rangel
johanarang@hotmail.com\

![logo_permiso](/static/media/delitos.jpg)

# Proyecto_Data_Analytics_python
Último proyecto integrador.

# Título del proyecto.
Predicción de tipos de delitos que pueden ocurrir en CABA-Argentina en una determinada zona ingresando como datos hora, dia, mes y barrio.

# Descripción. 
Es un modelo de inteligencia artificial basado en el sistema de clasificación KNN (K-Nearest-Neighbor), el cual es un algoritmo basado en instancia de tipo supervisado de Machine Learning. Que en este caso, se usó para clasificar un conjunto de datos que corresponden a los delitos ocurrido en CABA-Argentina durante el 2018, con el ojetivo de predecir los tipos de delitos que pueden ocurrir por un determinado barrio considerando el día, hora, mes y barrio. 
Está realizado con el lenguaje de programación Python. Funciona con una sola pagina que muestra el formulario para ingresar los datos anteriormente mencionados con el objetivo de realizar la búsqueda mostrando el resultado en la misma pagina.


# Ejemplo de algunos códigos realizados en colab.

# Convirtiendo los valores string  de las columnas franja_horaria, dia_delito, mes_delito en formato numérico.
s = pd.Series(df2['franja_horaria'])
df2['franja_horaria'] = pd.to_numeric(s, errors='coerce')

# Para contar cuántos tipos de delitos suceden por barrio.
df4_grupo = df4.groupby(['barrio'])['tipo_delito'].value_counts()

# Una vez los valores listos se ingresan en las variables para entrenar modelo.
X = df7.drop('Tipo_Delito', axis=1).values
y = df7['Tipo_Delito'].values

# Obtener la salida según el modelo base
random_model = RandomBaseModel()
random_model.fit(X_train, y_train)
y_hat_base = random_model.predict(X_test)
random_model.classes_
    
# Muchas gracias!
Cualquier duda o sugerencia pueden contartarse con Johana Rangel al mail johanarangeldo@gmail.com 

# Fecha de última actualización.
12 de abril 2020