export type Park = {
    Coordinates: {
        x: number;
        y: number;
    };
    Equipment: {
        BBQArea: boolean;
        ClimbingFrame: boolean;
        RainShelter: boolean;
        RunningTrack: boolean;
        SandPlayArea: boolean;
        SleddingHill: boolean;
        SwingSet: boolean;
        WaterAvailability: boolean;
        WindShelter: boolean;
    };
    Id: number;
    Name: string;
    TypesOfPlay: {
        BalancingPlay: boolean;
        CarPlay: boolean;
        HopscotchArea: boolean;
        PlayCircuit: boolean;
        RockingPlay: boolean;
        RolePlay: boolean;
        SlidePlay: boolean;
        SoundPlay: boolean;
        SpinningPlay: boolean;
        ToddlerPlay: boolean;
        WaterPlay: boolean;
    };
    Embed : string;
};
export type DataParks = {
    parks: Park[];
    api: String;
};
