package com.example.kotlinapp

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object MpesaRepository {

    private val retrofit = Retrofit.Builder()
        .baseUrl("http://localhost:8000/")
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    private val api = retrofit.create(MpesaApi::class.java)

    suspend fun pay(phone: String, amount: String): String {
        return try {
            val response = api.sendPayment(MpesaRequest(phone, amount))
            if (response.isSuccessful) {
                response.body()?.message ?: "No response"
            } else {
                "Payment failed"
            }
        } catch (e: Exception) {
            "Error: ${e.message}"
        }
    }
}
