#include "raylib.h"

int main(void)
{
  // Initialize raylib
  InitWindow(300, 300, "Raylib Test");
  SetTargetFPS(60);

  // Define color constants
  Color red = {255, 0, 0, 255};

  while (!WindowShouldClose())
  {
    // Update and draw
    BeginDrawing();
      ClearBackground(RAYWHITE);
      DrawRectangle(100, 100, 100, 50, red); // Draw red rectangle at (100, 100) with size (100, 50)
    EndDrawing();
  }

  // Close raylib
  CloseWindow();

  return 0;
}
