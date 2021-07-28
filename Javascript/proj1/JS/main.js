import Paddle from '/JS/paddle'

let canvas = document.getElementById('gameScreen')
let ctx = canvas.getContext('2d')

const GAME_WIDTH = canvas.width
const GAME_HEIGHT = canvas.height

let rectX = 100
let rectY = 100

ctx.clearRect(0, 0, canvas.width, canvas.height)
let paddle = new Paddle(GAME_WIDTH, GAME_HEIGHT)
paddle.draw(ctx)

