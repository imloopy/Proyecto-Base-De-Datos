package org.openjfx;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class LoginController {

    @FXML
    private TextField usernameField;

    @FXML
    private PasswordField passwordField;

    @FXML
    private Button loginButton;

    @FXML
    private void login() {
        // Aquí implementarás la lógica para la autenticación con la base de datos más tarde
        String username = usernameField.getText();
        String password = passwordField.getText();

        // Por ahora, simplemente imprimimos los datos
        System.out.println("Username: " + username);
        System.out.println("Password: " + password);

        // Simulación de autenticación exitosa (deberás implementar la lógica real aquí)
        boolean authenticationSuccess = true;

        if (authenticationSuccess) {
            // Cargar la segunda pantalla (SecondScreen.fxml)
            switchToSecondScreen();
        } else {
            // Mostrar mensaje de error o hacer otra acción según sea necesario
            System.out.println("Autenticación fallida. Verifica tus credenciales.");
        }
    }

    private void switchToSecondScreen() {
        try {
            // Cargar la segunda pantalla (SecondScreen.fxml)
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/org/openjfx/secondScreen.fxml"));
            Parent root = loader.load();
            Scene scene = new Scene(root);
            
            // Obtener la referencia al Stage actual (ventana)
            Stage stage = (Stage) loginButton.getScene().getWindow();
            
            // Configurar la nueva escena en el Stage
            stage.setScene(scene);
            stage.setTitle("Second Screen");
            stage.show();
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
