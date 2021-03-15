package com.example.myapplication.ui;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.DefaultItemAnimator;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import com.example.myapplication.R;
import com.example.myapplication.network.AllRequestsAPI;
import com.example.myapplication.network.model.GetTeachersModel;
import com.example.myapplication.ui.adapter.TeachersAdapter;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class MainActivity extends AppCompatActivity implements AllRequestsAPI.OnComplete {
    LinearLayoutManager mLayoutManager;
    TextView txt_view;
    List<String> newList;
    RecyclerView recyclerView;
    TeachersAdapter teachers_adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
//        txt_view = findViewById(R.id.txt_view);

//        getSupportActionBar().setDisplayOptions(ActionBar.DISPLAY_SHOW_CUSTOM);
//        getSupportActionBar().setCustomView(R.menu.toolbar);

        recyclerView = findViewById(R.id.recycler_view);
        mLayoutManager = new LinearLayoutManager(MainActivity.this, LinearLayoutManager.VERTICAL, false);
        recyclerView.setLayoutManager(mLayoutManager);
        recyclerView.setItemAnimator(new DefaultItemAnimator());
        newList = new ArrayList<>();
        HashMap<String, List<String>> map = new HashMap<>();
        map.put("params", newList);
        new AllRequestsAPI(this).getAllTeachers(map);
    }


    @Override
    public void onSuccess(Object object) {
        Log.d("RRRRRRRRRRRRRRRRR", "accept in Done Request");
        GetTeachersModel.Example teacher = (GetTeachersModel.Example) object;
//        txt_view.setText(carPricess.getResult().getResponse().get(0).getName().toString());
        teachers_adapter = new TeachersAdapter(MainActivity.this, teacher.getResult().getResponse());
        teachers_adapter.setHasStableIds(true);
        recyclerView.setAdapter(teachers_adapter);

    }
}