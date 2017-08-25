class RolePlayer(object):

    def calculate_hitpoints(self, battlefield):

        hitpoints = 1
        damage = 0
        while damage < 1:
            damage = hitpoints
            for points in battlefield:
                damage += points
                if damage < 1:
                    hitpoints += 1
                    break

        return hitpoints

    def calculate_hitpoints_zac_style(self, battlefield):
        damage = 0
        health = 1
        first_negative = True
        for points in battlefield:
            damage += points
            if damage < 0:
                health = abs(damage) + 1
            else:
                health = 1

        return health

    def calculate_hitpoints_zac_attack(self, hitpointarray):
        health = 1
        currentDamage = maxDamage = 0
        for points in hitpointarray:
            currentDamage = currentDamage + points
            if currentDamage < maxDamage:
                maxDamage = currentDamage

            health = abs(maxDamage) + 1

        return health