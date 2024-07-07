package org.openjfx;

import javafx.fxml.FXML;
import javafx.scene.control.Label;

public class SecondScreen {

    @FXML
    private Label secondLabel;

    public void initialize() {
        String javaVersion = System.getProperty("java.version");
        String javafxVersion = System.getProperty("javafx.version");
        secondLabel.setText("Second Screen\nJavaFX " + javafxVersion + "\nRunning on Java " + javaVersion + ".");
    }
}
