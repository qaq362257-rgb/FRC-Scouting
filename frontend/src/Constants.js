export const HangingState = Object.freeze({
    SUCCESS : 'success',
    FAIL : 'fail',
    NO : 'no'
})

export const IntakeMethod = Object.freeze({
    FLOOR : 'floor',
    PLAYER : 'player',  // from human player
    BOTH : 'both',
    NO : 'no',
});

export const TeamColor = Object.freeze({
    BLUE: 'blue',
    RED: 'red'
});

export const StartPos = Object.freeze({
    DEPOT: 'depot',
    MIDDLE: 'middle',
    PLAYER: 'player'
});

export const Uses = Object.freeze({
    SHOOT: 'shoot',
    HANGING: 'hanging',
    DEFENSE: 'defense',
    SUPPORT: 'support'
});

export const HangingStateArr = [
    HangingState.SUCCESS,
    HangingState.FAIL,
    HangingState.NO
];

export const IntakeMethodArr = [
    IntakeMethod.FLOOR,
    IntakeMethod.PLAYER,
    IntakeMethod.BOTH,
    IntakeMethod.NO
];

export const TeamColorArr = [
    TeamColor.BLUE,
    TeamColor.RED
];

export const StartPosArr = [
    StartPos.DEPOT,
    StartPos.MIDDLE,
    StartPos.PLAYER
];

export const UsesArr = [
    Uses.SHOOT,
    Uses.HANGING,
    Uses.DEFENSE,
    Uses.SUPPORT
]