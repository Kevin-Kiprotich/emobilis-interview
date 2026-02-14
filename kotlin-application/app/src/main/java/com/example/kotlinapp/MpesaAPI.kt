package com.example.kotlinapp

import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.POST

data class MpesaRequest(
    val phone: String,
    val amount: String
)

data class MpesaResponse(
    val message: String
)

interface MpesaApi {

    @POST("stkpush/")
    suspend fun sendPayment(
        @Body request: MpesaRequest
    ): Response<MpesaResponse>
}
