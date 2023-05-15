:orphan:

:py:mod:`drinks`
================

.. py:module:: drinks


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   drinks.HotBeverage
   drinks.Coffee
   drinks.Tea




.. py:class:: HotBeverage

   Bases: :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: drinks.HotBeverage
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



.. py:class:: Coffee

   Bases: :py:obj:`drinks.hot_beverage.HotBeverage`

   .. autoapi-inheritance-diagram:: drinks.Coffee
      :parts: 1
      :private-bases:

   Class to prepare coffee

   .. seealso:: :obj:`HotBeverage`

   .. py:method:: brew()

      Drips coffee with water at `temperature`


   .. py:method:: add_extras()

      Add sugar and milk



.. py:class:: Tea

   Bases: :py:obj:`drinks.hot_beverage.HotBeverage`

   .. autoapi-inheritance-diagram:: drinks.Tea
      :parts: 1
      :private-bases:

   Class to prepare tea

   .. seealso:: :obj:`HotBeverage`

   .. py:method:: brew()

      Steeps the tea at `temperature`


   .. py:method:: add_extras()

      Add lemon to tea



