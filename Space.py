keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT] and self.position.x > 0:
    self.position.x -= max(1, st.SCREEN_WIDTH // 500)
if keys[pygame.K_RIGHT] and self.position.x < st.SCREEN_WIDTH - self.rect.width:
    self.position.x += max(1, st.SCREEN_WIDTH // 500)

