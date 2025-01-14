﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    catalog=model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    loadVideos(catalog)
    loadCategoria(catalog)


def loadVideos(catalog):
    videosfile = cf.data_dir + "videos-small.csv"
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)
        model.addCountry(catalog,video)


def loadCategoria(catalog):
    categoriafile = cf.data_dir + "category-id.csv"
    input_file = csv.DictReader(open(categoriafile, encoding='utf-8'),delimiter='\t')
    for categoria in input_file:
        model.addCategoria(catalog,categoria)



# Funciones de ordenamiento

def sameCountryCategory(catalogo_pais,catalogo_categoria,country,category):
    return model.sameCountryCategory(catalogo_pais,catalogo_categoria,country,category)

def obtener_listapais(catalog, country):
    return model.obtener_listapais(catalog, country)

def sortVideoId(catalog, country):
    return model.sortVideoId(catalog, country)

def encontrar_ganador(lista_ids):
    return model.encontrar_ganador(lista_ids)
# Funciones de consulta sobre el catálogo
