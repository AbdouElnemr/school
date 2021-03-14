package com.example.myapplication.network;

import com.example.myapplication.network.model.GetTeachersModel;

import org.json.JSONArray;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import io.reactivex.Single;
import okhttp3.RequestBody;
import retrofit2.http.Body;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.GET;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.PartMap;

public interface ApiService {

    @POST("get_teachers")
    Single<GetTeachersModel.Example> getTeachers(@Body  HashMap<String, List<String> > map);

}
