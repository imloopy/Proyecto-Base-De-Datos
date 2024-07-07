package org.openjfx;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import java.io.IOException;

public class FXMLController {

    @FXML
    private Button switchButton;

    @FXML
    private void switchToSecondScreen() {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/org/openjfx/secondScreen.fxml"));
            Parent root = loader.load();
            SecondScreen controller = loader.getController();
            Stage stage = (Stage) switchButton.getScene().getWindow();
            Scene scene = new Scene(root);
            stage.setScene(scene);
            stage.setTitle("Second Screen");
            controller.initialize(); // Call initialize method of SecondScreen controller
            stage.show();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
