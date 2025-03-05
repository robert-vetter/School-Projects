void setup() {
   size(200, 200);
  
}

void draw() {
     background(255);
   
stroke (0);
fill(175);
rectMode (CENTER);
rect(mouseX, mouseY, 50, 50);

}

/*Als background() noch in der Prozedur void draw() war und man dann auf "starten" gedrückt hat, sah man dort ein Rechteck in der Zeichenfläche,
dass immer dem Mauszeiger gefolgt ist. Wenn man mit dem Mauszeiger außerhalb des Sketchfensters gegangen ist, ist das Rechteck ganz außen am
Rand geblieben. Sobald man aber background() in die Prozedur void setup() hineingefügt hat und dann den Mauszeiger in der Zeichenfläche 
bewegt hat, sind sehr viele Rechtecke hinter dem Mauszeiger entstanden. Wenn man den Mauszeiger jedoch sehr schnell über die Zeichenfläche gezogen 
hat, sind viel weniger Rechtecke hinter dem Mauszeiger gewesen als wenn man langsam die Maus bewegt hat. Das liegt daran, dass nur eine bestimmte
Anzahl Rechtecke pro Sekunde erscheint. Zudem werden die Rechtecke wenn man die Maus langsamer bewegt schwarz. Das könnte daran liegen, dass
dann sehr viele Rechtecke auf einer Stelle sind und sie dadurch schwarz werden. Wenn man mit dem Mauszeiger aus der Sketchfläche rausgeht und 
dann wieder rein, erstarrt das Sketchfenster. Sobald man aber wieder hineingeht, fängt man mit einem neuen Rechteck an. Wenn man die Maus
schneller bewegt, werden die Rechtecke auch in größeren Abständen angezeigt.*/
