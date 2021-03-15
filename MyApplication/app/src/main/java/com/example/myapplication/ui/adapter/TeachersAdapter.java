package com.example.myapplication.ui.adapter;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.drawable.Drawable;
import android.media.Image;
import android.os.Build;
import android.util.Base64;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Switch;
import android.widget.TextView;

import androidx.annotation.RequiresApi;
import androidx.recyclerview.widget.RecyclerView;


import com.example.myapplication.R;
import com.example.myapplication.network.model.GetTeachersModel;
import com.squareup.picasso.Picasso;

import java.util.List;

import de.hdodenhof.circleimageview.CircleImageView;

import static com.example.myapplication.network.Const.BASE_URL;

public class TeachersAdapter extends RecyclerView.Adapter<TeachersAdapter.MyViewHolder> {
    public static String id;
    private TeachersAdapter.OnItemClickListener mAdapterListener;
    private Context mContext;
    private List<GetTeachersModel.Response> albumList;

    public class MyViewHolder extends RecyclerView.ViewHolder {
        public TextView name_text, phone_text, subject_text;
        public CircleImageView imageView;

        public MyViewHolder(View view) {
            super(view);
            name_text = view.findViewById(R.id.name_text);
            phone_text = view.findViewById(R.id.phone_text);
            subject_text = view.findViewById(R.id.subject_text);
            imageView = view.findViewById(R.id.image);


        }
    }


    public TeachersAdapter(Context mContext, List<GetTeachersModel.Response> albumList) {
        this.mContext = mContext;
        this.albumList = albumList;
    }

    @Override
    public TeachersAdapter.MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.teacher_row, parent, false);

        return new TeachersAdapter.MyViewHolder(itemView);
    }

    @RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
    @Override
    public void onBindViewHolder(final TeachersAdapter.MyViewHolder holder, int position) {
        GetTeachersModel.Response service = albumList.get(position);
        holder.name_text.setText(service.getName());
        holder.phone_text.setText(service.getPhone());
        holder.subject_text.setText(service.getSubject());


        if(service.getImage().equals("false")){
            holder.imageView.setImageDrawable(mContext.getResources().getDrawable(R.drawable.avatar));
        }else {
            Log.d("RRRRRRRRRREEEEEEEEEE", service.getImage());
            byte[] decodedString = Base64.decode(service.getImage().trim(), Base64.DEFAULT);
            Bitmap decodedByte = BitmapFactory.decodeByteArray(decodedString, 0, decodedString.length);
            Drawable d = new BitmapDrawable(mContext.getResources(), decodedByte);
            holder.imageView.setImageDrawable(d);
        }

        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            }
        });


    }


    @Override
    public int getItemCount() {
        return albumList.size();
    }

    public interface OnItemClickListener {
        void OnSelecetd(int pos, String type);
    }
}



