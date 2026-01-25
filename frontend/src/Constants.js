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