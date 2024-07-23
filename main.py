from utility import read_video , save_video 
from tracker import Tracker 
import cv2
from assign_team import TeamAssigner 
from assign_ball_to_player import PlayerBallAssigner 

def main() :
    video_frames = read_video('input/08fd33_4.mp4')

    tracker = Tracker('models/best.pt')

    tracks = tracker.get_obj_tracker(video_frames , read_from_stub= True , stub_path= 'pickle/track_stubs.pkl' )

    tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])

    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0] , tracks['players'][0])

    for frame_num , player_track in enumerate(tracks['players']) :
        for player_id , track in player_track.items() :
            team = team_assigner.get_player_team(video_frames[frame_num], track['bbox'],
                                                 player_id) 
            
            tracks['players'][frame_num][player_id]['team'] = team 
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team] 


    player_assigner = PlayerBallAssigner() 
    for frame_num , player_track in enumerate(tracks['players']) :
        ball_bbox= tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_assigner.assign_ball_to_player(player_track , ball_bbox) 

        if assigned_player != -1 :
            tracks['players'][frame_num][assigned_player]['has_ball'] = True


  
    output_frames = tracker.draw_annotations(video_frames ,tracks)

    save_video( output_frames , 'output/outpu_video.avi')

if __name__ == '__main__' :
    main()