package com.example.myapplication.network;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Build;
import android.util.Log;
import android.widget.Toast;

import androidx.annotation.RequiresApi;

import com.example.myapplication.helper.PrefManager;
import com.example.myapplication.network.model.GetTeachersModel;
import com.google.gson.Gson;
import com.kaopiz.kprogresshud.KProgressHUD;

import org.json.JSONArray;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.observers.DisposableSingleObserver;
import io.reactivex.schedulers.Schedulers;
import okhttp3.RequestBody;

public class AllRequestsAPI {
    Context mContext;
    ApiService apiService;
    PrefManager prefManager;
    String Result;
    KProgressHUD hud;
    OnComplete onComplete;

    public AllRequestsAPI(Context context) {
        this.mContext = context;
        onComplete = (OnComplete) context;
        apiService = ApiClient.getClient(mContext).create(ApiService.class);
        prefManager = new PrefManager(mContext);
        hud = KProgressHUD.create(mContext)
                .setStyle(KProgressHUD.Style.SPIN_INDETERMINATE)
                .setCancellable(false)
                .setAnimationSpeed(2)
                .setDimAmount(0.5f)
                .show();
    }

    public void Login_Method(HashMap<String, String> hashMap) {


    }
//
//    public String GetClasses_Method() {
//        Result = "0";
//        HashMap<String, String> hashMap = new HashMap<>();
//        hashMap.put("token", prefManager.getTokenreply());
//
//
//    }

    public String getAllTeachers(HashMap<String, List<String>> cars) {


        apiService.getTeachers(cars)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribeWith(new DisposableSingleObserver<GetTeachersModel.Example>() {

                    @Override
                    public void onSuccess(GetTeachersModel.Example reponsed) {
                        // Received all notes
//                        try {
                        Log.d("RRRRRRRRRRRRRRRRR", "ppppppppppppppppppppppppp" + reponsed);


                        hud.dismiss();
                        if (reponsed.getResult().getMessage().equals("success")) {
                            onComplete.onSuccess(reponsed);


                        } else
                            prefManager.setlogin(false);
//                        mContext.startActivity(new Intent(mContext, Choose_Type.class));
//                        ((Activity) mContext).finish();
                        Log.d("RRRRRRRRRRRRRRRRR", "ppppppppppppppppppppppppp");

//                        } catch (Exception e) {
//
//                        }
                    }


                    @Override
                    public void onError(Throwable e) {
                        Log.d("RRRRRRRRRRRRRRRRR", "cccccccccccccccccccccccc" + e.getMessage());

                        Toast.makeText(mContext, "Connection Timed Out", Toast.LENGTH_LONG).show();
                        Log.e("df", e.getMessage());
                        hud.dismiss();
                    }
                });
        return Result;
    }

    public interface OnComplete {
        void onSuccess(Object object);

    }
}
