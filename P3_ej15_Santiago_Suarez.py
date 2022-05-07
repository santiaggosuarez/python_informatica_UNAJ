def calculo_dosis(dias,veces_por_dia,cantidad):
  return cantidad >= dias*veces_por_dia

print(calculo_dosis(5,2,10))
