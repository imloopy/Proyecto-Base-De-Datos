package org.openjfx;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;

import java.io.File;
import java.io.IOException;

public class SecondScreenController {

    @FXML
    private Button pythonButton;

    @FXML
    private ImageView imageView;

    @FXML
    private void ejecutarScriptPython() {
        try {
            // Ruta al archivo Python
            String pythonScriptPath = "src/main/python/mi_script.py";

            // Construir el comando para ejecutar el script Python
            ProcessBuilder pb = new ProcessBuilder("python3", pythonScriptPath);

            // Iniciar el proceso
            Process process = pb.start();

            // Esperar a que el proceso termine
            int exitCode = process.waitFor();

            // Imprimir el código de salida (opcional)
            System.out.println("Script Python ejecutado con código de salida: " + exitCode);

            // Cargar la imagen generada por Matplotlib
            File imageFile = new File("plot.png");
            Image image = new Image(imageFile.toURI().toString());
            imageView.setImage(image);

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
