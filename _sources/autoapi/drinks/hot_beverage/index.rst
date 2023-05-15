:orphan:

:py:mod:`drinks.hot_beverage`
=============================

.. py:module:: drinks.hot_beverage


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   drinks.hot_beverage.HotBeverage




.. py:class:: HotBeverage

   Bases: :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: drinks.hot_beverage.HotBeverage
      :parts: 1
      :private-bases:

   Abstract class to prepare hot beverages

   .. attribute:: temperature

      Temperature at which the hot beverage is prepared.

      :type: float

   .. py:method:: prepare_recipe()

      Prepares the hot beverage


   .. py:method:: boil_water()

      Boils water


   .. py:method:: pour()

      Pours beverage into cup



