// Fill out your copyright notice in the Description page of Project Settings.


#include "WebSocketHandler.h"

// Sets default values
AWebSocketHandler::AWebSocketHandler()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

}

// Called when the game starts or when spawned
void AWebSocketHandler::BeginPlay()
{
	Super::BeginPlay();
    const FString ServerURL = TEXT("ws://127.0.0.1:3000/"); // Your server URL. You can use ws, wss or wss+insecure.
    const FString ServerProtocol = TEXT("ws");              // The WebServer protocol you want to use.
        
    TSharedPtr<IWebSocket> Socket = FWebSocketsModule::Get().CreateWebSocket(ServerURL, ServerProtocol);
    
    ServerConnect();
    SendURL("HELLO");
    UE_LOG(YourLog, Warning, TEXT("Checkpoint A!!!!!!"));

    ServerClose();
	
}

// Called every frame
void AWebSocketHandler::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

void AWebSocketHandler::ServerConnect()
{
    // We bind all available events
    Socket->OnConnected().AddLambda([]() -> void {
        // This code will run once connected.
    });
        
    Socket->OnConnectionError().AddLambda([](const FString & Error) -> void {
        // This code will run if the connection failed. Check Error to see what happened.
    });
        
    Socket->OnClosed().AddLambda([](int32 StatusCode, const FString& Reason, bool bWasClean) -> void {
        // This code will run when the connection to the server has been terminated.
        // Because of an error or a call to Socket->Close().
    });
        
    Socket->OnMessage().AddLambda([](const FString & Message) -> void {
        // This code will run when we receive a string message from the server.
    });
        
    Socket->OnRawMessage().AddLambda([](const void* Data, SIZE_T Size, SIZE_T BytesRemaining) -> void {
        // This code will run when we receive a raw (binary) message from the server.
    });
        
    Socket->OnMessageSent().AddLambda([](const FString& MessageString) -> void {
        // This code is called after we sent a message to the server.
    });
        
    // And we finally connect to the server.
    Socket->Connect();
}

void AWebSocketHandler::SendURL(FString URL)
{
    if (!Socket->IsConnected())
    {
        // Don't send if we're not connected.
        return;
    }
        
    const FString StringMessage = TEXT("Hello there !");
    const TArray BinaryMessage = { 'H', 'e', 'l', 'l', 'o', ' ', 't', 'h', 'e', 'r', 'e', ' ', '!' };
      
    Socket->Send(StringMessage);
    Socket->Send(BinaryMessage.GetData(), sizeof(uint8) * BinaryMessage.Num());
}

void AWebSocketHandler::ServerClose()
{
    Socket->Close()
}

