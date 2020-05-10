package com.davidbv.restapi;
import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MenuActivity extends AppCompatActivity implements View.OnClickListener{

    private Button btnCamara, btnRest;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);
        btnCamara = (Button) findViewById(R.id.btnCamara);
        btnRest = (Button) findViewById(R.id.btnRest);
        btnCamara.setOnClickListener(this);
        btnRest.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
     if (v.getId() == R.id.btnCamara){
         Intent intent = new Intent(this, CamaraActivity.class);
         startActivity(intent);
     }if (v.getId() == R.id.btnRest){
         Intent intent = new Intent(this, MainActivity.class);
         startActivity(intent);
        }
    }
}
