package com.davidbv.restapi;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{
    private Button mButtonDo, btnCamara;
    private TextView mTextView;
    //Esta url se edita dependiendo de la url del servidor
    String url = "http://192.168.1.74:8000/api/Analisis/?format=json";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mButtonDo = (Button) findViewById(R.id.btn_do);
        mTextView = (TextView) findViewById(R.id.tv);
        mButtonDo.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        if(v.getId()==R.id.btn_do){
            consumirREST(url);
        }
    }

    public void consumirREST(String url){
        mTextView.setText("");
        RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
        JsonArrayRequest jsonArrayRequest = new JsonArrayRequest(Request.Method.GET, url,
                null, new Response.Listener<JSONArray>() {
            @Override
            public void onResponse(JSONArray response) {
                //mTextView.setText(response.toString());
                try {
                    for (int i = 0; i < response.length(); i++) {
                        JSONObject imagen = response.getJSONObject(i);
                        String id = imagen.getString("id");
                        String titulo = imagen.getString("titulo");
                        mTextView.append(id +": " + titulo);
                        mTextView.append("\n\n");
                    }
                } catch (JSONException e) {
                    Toast.makeText(MainActivity.this, "No se proceso bien" +
                            e.getMessage(), Toast.LENGTH_SHORT).show();
                }
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Toast.makeText(MainActivity.this, "Error"+error.getMessage(),
                        Toast.LENGTH_SHORT).show();
            }
        }
    );
        requestQueue.add(jsonArrayRequest);
    }

}
