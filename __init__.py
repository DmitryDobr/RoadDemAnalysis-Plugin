# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RoadAnalysis
                                 A QGIS plugin
 Plugin for road analysis with DEM info
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-03-26
        copyright            : (C) 2024 by Dmitry D.
        email                : dmitrdobr@mail.ru
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load RoadAnalysis class from file RoadAnalysis.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .dem_road_analysis import RoadAnalysis
    return RoadAnalysis(iface)
