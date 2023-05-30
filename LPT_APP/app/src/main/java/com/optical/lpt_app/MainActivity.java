package com.optical.lpt_app;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class MainActivity extends Activity {

    private Button mountButton;
    private Button unmountButton;
    private TextView consoleTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mountButton = findViewById(R.id.mount);
        unmountButton = findViewById(R.id.umount);
        consoleTextView = findViewById(R.id.console);

        mountButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mountFileSystem();
            }
        });

        unmountButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                unmountFileSystem();
            }
        });
    }

    private void mountFileSystem() {
        // Mount command
        String mountCommand = "./data/LPT/scripts/mount.sh";

        try {
            // Execute mount command with SuperSU privileges
            String output = executeCommandAsRoot(mountCommand);
            // Display the output in the consoleTextView
            System.out.println(output);
            consoleTextView.setText(output);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void unmountFileSystem() {
        // Unmount command
        // String unmountCommand = "./data/LPT/scripts/mount.sh -u";


        String unmountCommand = "chroot /data/LPT /bin/bash -c 'echo 1' --rcfile ./scripts/env.sh";
        try {
            // Execute unmount command with SuperSU privileges
            String output = executeCommandAsRoot(unmountCommand);
            // Display the output in the consoleTextView
            consoleTextView.setText(output);
            System.out.println(output);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    private String executeCommandAsRoot(String command) throws IOException, InterruptedException {
        StringBuilder output = new StringBuilder();

        Process process = Runtime.getRuntime().exec("su");
        DataOutputStream outputStream = new DataOutputStream(process.getOutputStream());
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));

        outputStream.writeBytes(command + "\n");
        outputStream.writeBytes("exit\n");
        outputStream.flush();

        String line;
        while ((line = reader.readLine()) != null) {
            output.append(line).append("\n");
        }

        process.waitFor();

        return output.toString();
    }
}
