// Copyright Epic Games, Inc. All Rights Reserved.

#include "HowdyHackGameMode.h"
#include "HowdyHackCharacter.h"
#include "UObject/ConstructorHelpers.h"

AHowdyHackGameMode::AHowdyHackGameMode()
{
	// set default pawn class to our Blueprinted character
	static ConstructorHelpers::FClassFinder<APawn> PlayerPawnBPClass(TEXT("/Game/SideScrollerCPP/Blueprints/SideScrollerCharacter"));
	if (PlayerPawnBPClass.Class != nullptr)
	{
		DefaultPawnClass = PlayerPawnBPClass.Class;
	}
}
