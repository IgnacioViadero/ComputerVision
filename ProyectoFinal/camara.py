def stream_video():
    # Configurar Picamera2
    picam = Picamera2()
    picam.preview_configuration.main.size = (320, 240)
    picam.preview_configuration.main.format = "RGB888"
    picam.preview_configuration.align()
    picam.configure("preview")
    picam.start()

    # Configurar grabación de video
    output_file = "video.avi"
    fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Codec para AVI
    out = cv2.VideoWriter(output_file, fourcc, 30, (320, 240))

    print(f"Grabando video durante 10 segundos en: {output_file}")
    start_time = time.time()

    n_frames = 0

    try:
      while True:
        # Capturar frame desde Picamera2
        frame = picam.capture_array()


        if n_frames == 0:
          initial_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          n_frames += 1

        processed_frame = Procesamiento_Frames(initial_frame, frame)
        # Guardar el frame en el archivo
        out.write(frame)

        # Mostrar video original
        cv2.imshow("Picamera Stream - Original", frame)

        # Procesar el frame (por ejemplo, convertir a escala de grises)
        cv2.imshow("Picamera Stream - Procesado", processed_frame)

        # Salir después de 10 segundos o si se presiona 'q'
        if time.time() - start_time > 30 or cv2.waitKey(1) & 0xFF == ord('q'):
            break
    finally:
      # Liberar recursos
      out.release()
      picam.stop()
      cv2.destroyAllWindows()
      print("Grabación finalizada y recursos liberados.")
