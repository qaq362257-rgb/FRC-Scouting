from pydantic import BaseModel, Field
from enum import Enum
from datetime import time
from typing import Annotated

# Enums 

class TeamColor(str, Enum):
    BLUE =  'blue'
    RED = 'red'
    
class StartPos(str, Enum):
    DEPOT = 'depot'
    MIDDLE = 'middle'
    PLAYER = 'player'

class HangingState(str, Enum):
    SUCCESS = 'success'
    FAIL = 'fail' # try but fail
    NO = 'no'
    
class IntakeMethod(str, Enum):
    FLOOR = 'floor'
    PLAYER = 'player' # from human player
    BOTH = 'both'
    NO = 'no'
    
class PassMethod(str, Enum):
    BUMP = 'bump' # over
    TRENCHES = 'trenches' # under
    BOTH = 'both'
    NO = 'no'
    
class Uses(str, Enum):
    SHOOT = 'shoot'
    HANGING = 'hanging'
    DEFENSE = 'defense'
    SUPPORT = 'support'
    
# Sub Model

class BasicData(BaseModel):
    user_name: str
    filling_time: time
    time_zone: Annotated[int, Field(ge=-12, le=14)]
    team_number: Annotated[int, Field(ge=0)]
    team_color: TeamColor
  
class AutoPart(BaseModel):
    init_ball_number: Annotated[int, Field(ge=0, le=8)]
    start_pos: StartPos
    leave_line: bool
    total_hit: Annotated[int, Field(ge=0)]
    total_miss: Annotated[int, Field(ge=0)]
    auto_hanging: HangingState # only first level
    
class ManualPart(BaseModel):
    intake_method: IntakeMethod
    total_hit: Annotated[int, Field(ge=0)]
    total_miss: Annotated[int, Field(ge=0)]
    manual_hanging: Annotated[list[HangingState], Field(min_length=3, max_length=3)] # 1 ~ 3 level
    
class Others(BaseModel):
    driver: Annotated[int, Field(ge=1, le=5)]
    defense: Annotated[int, Field(ge=1, le=5)]
    is_dead: bool
    uses: Annotated[list[Uses], Field(min_length=0, max_length=4)]
    main_uses: Uses
    do_comment: bool
    comment: str|None = None
    
# Model 

class MatchData(BaseModel):
    basic_data: BasicData
    auto_part: AutoPart
    manual_part: ManualPart
    others: Others
    
# Test
    
if __name__ == '__main__':
    # 測試資料：模擬前端傳過來的 JSON 格式 (字串 Enum 自動轉換)
    try:
        test_data = {
            "basic_data": {
                "user_name": "Scouter1",
                "filling_time": "12:00:00",
                "time_zone": 8,
                "team_number": 115, 
                "team_color": "red"
            },
            "auto_part": {
                "init_ball_number": 1,
                "start_pos": "middle",
                "leave_line": True,
                "total_hit": 2,
                "total_miss": 0,
                "auto_hanging": "no"
            },
            "manual_part": {
                "intake_method": "floor",
                "total_hit": 10,
                "total_miss": 2,
                "manual_hanging": ["no", "success", "no"]
            },
            "others": {
                "driver": 5,
                "defense": 3,
                "is_dead": False,
                "uses": ["shoot", "defense"],
                "main_uses": "shoot",
                "do_comment": True,
                "comment": "Good driver"
            }
        }
        
        # 驗證整個資料結構
        match = MatchData.model_validate(test_data)
        print("資料驗證成功！")
        print(match.model_dump_json(indent=2)) 
        
    except Exception as e:
        print(f"資料驗證失敗: {e}")
