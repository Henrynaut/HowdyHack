// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class HowdyHack : ModuleRules
{
	public HowdyHack(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

		PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "WebSockets" });
	}
}
