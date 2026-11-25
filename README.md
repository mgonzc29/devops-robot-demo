 Esta práctica se centra en aplicar a un código sencillo dado con tests incluidos mecanismos de desarrollo contínuo a través de herramientas de github. 

 Además, se conecta el repositorio a un webhook de discord para avisarnos de estos procesos en un canal de texto dedicado. 
 
 Preguntas de la práctica:
    

    ¿Qué ocurre exactamente en el valor límite de 0.5 metros?

    def can_move(distance: float) -> bool:
    """Return True if the robot can move safely."""
    if distance < 0:
    raise ValueError("Distance cannot be negative")
    return distance > 0.5

    Se devuelve false.
    