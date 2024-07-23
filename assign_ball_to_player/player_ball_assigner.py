import sys
sys.path.append('../')

from utility import get_center_of_boxes , measure_dist

class PlayerBallAssigner()  :
    def __init__(self)  :
        self.max_player_ball_dist = 70 

    def assign_ball_to_player(self, players, ball_bbox) :
        ball_position = get_center_of_boxes(ball_bbox) 

        minimum_dist = 99999 
        assigned_player =- 1 

        for player_id , player in players.items() : 
            player_bbox = player['bbox'] 

            distance_left = measure_dist((player_bbox[0] , player_bbox[-1]), ball_position )
            distance_right = measure_dist((player_bbox[2] , player_bbox[-1]), ball_position )

            distance =  min(distance_left , distance_right ) 

            if distance < self.max_player_ball_dist : 
                if distance < minimum_dist : 
                    minimum_dist  = distance 
                    assigned_player = player_id 
        
        return assigned_player 

