if men == 1:
        fondo1 = pygame.image.load('png/1.png')
        fondo2 = pygame.image.load('png/4.png')
        playf = pygame.image.load('png/playunp.png')
        playn = pygame.image.load('png/playp.png')
        quitf = pygame.image.load('png/quitunp.png')
        quitn = pygame.image.load('png/quitp.png')
        mouse = pygame.mouse.get_pos()
        pantalla.blit(fondo1,[0,0])
        if 100+183 > mouse[0] > 100 and 300+93 > mouse[1] > 300:
            pantalla.blit(playn,[100,300])
        else:
            pantalla.blit(playf,[100,300])

        if 300+192 > mouse[0] > 300 and 305+102 > mouse[1] > 305:
            pantalla.blit(quitn,[300,305])
        else:
            pantalla.blit(quitf,[300,305])


        men = 0




j1.doblet = False
            ShowMenu(men)
            if event.type == pygame.MOUSEBUTTONDOWN:

                p = event.pos
                if 300+192 > p[0] > 300 and 305+102 > p[1] > 305:
                    end = True

                if 100+183 > p[0] > 100 and 300+93 > p[1] > 300:
                    sound.stop()
                    inicio()
                    for p in Puntos:
                        Puntos.remove(p)
                    men = 1.5

 if (self.velx>0 and self.rect.y>350  ):
        
            if(self.clock % 500 == 0):
                self.vely = auxVely
                self.velx = 0

            if(self.clock % 257 == 0):
                self.vely = 0
                self.velx = auxVelx
        
            self.rect.x += self.velx
            self.rect.y -= self.vely

        elif (self.velx>0 and self.rect.y > 650):
            
            self.rect.x += self.velx
            self.rect.y -= self.vely

        else:
            self.rect.x += self.velx
            self.rect.y += self.vely














if (self.velx>0 and self.rect.y>350  ):
    
            if(self.clock % 500 == 0):
                self.vely = auxVely
                self.velx = 0

                if (self.velx>0 and self.rect.y>350  ):
                    self.rect.x += self.velx
                    self.rect.y -= self.vely

                elif (self.velx>0 and self.rect.y > 600):
                    self.rect.x += self.velx
                    self.rect.y -= self.vely
            
                else:
                    self.rect.x += self.velx
                    self.rect.y += self.vely
            
            if(self.clock % 257 == 0):
                self.vely = 0
                self.velx = auxVelx
        
                if (self.velx>0 and self.rect.y>350  ):
                    self.rect.x += self.velx
                    self.rect.y -= self.vely

                elif (self.velx>0 and self.rect.y > 600):
                    self.rect.x += self.velx
                    self.rect.y -= self.vely      

                else:                    
                    self.rect.x += self.velx
                    self.rect.y += self.vely
                
            else:
                self.rect.x += auxVelx            