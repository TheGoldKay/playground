package main

import (
	"github.com/hajimehoshi/ebiten/v2"
	"github.com/hajimehoshi/ebiten/v2/vector"
	"log"
	"image/color"
)

type Player struct{
	x, y float32
	ln float32
	color color.RGBA
}

type Game struct{
	player Player
	bg_color color.RGBA
	win_w int 
	win_h int
}

func (g *Game) Update() error {
	// Close the game when the Escape key is pressed
	if ebiten.IsKeyPressed(ebiten.KeyEscape) {
		return ebiten.Termination
	}
	return nil
}

func (g *Game) Draw(screen *ebiten.Image) {
	// Fill the screen with green
	vector.DrawFilledRect(screen, 0, 0, float32(g.win_w), float32(g.win_h), g.bg_color, true)
	vector.DrawFilledRect(screen, g.player.x, g.player.y, g.player.ln, g.player.ln, g.player.color, true)
}

func (g *Game) Layout(outsideWidth, outsideHeight int) (int, int) {
	return outsideWidth, outsideHeight
}

func main() {
	window_width := 640
	window_height := 480
	ebiten.SetWindowSize(window_width, window_height)
	ebiten.SetWindowTitle("Green Screen Game")
	game := &Game{
		player: Player{
			x: float32(window_width / 2),
			y: float32(window_height / 2),
			ln: 50,
			color: color.RGBA{G: 255, B: 220, A: 255},
		},
		bg_color: color.RGBA{G: 255, B: 100, A: 255},
		win_w: window_width,
		win_h: window_height,
	}
	if err := ebiten.RunGame(game); err != nil {
		log.Fatal(err)
	}
}

