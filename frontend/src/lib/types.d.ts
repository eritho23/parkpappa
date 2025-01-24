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
};
export type DataParks = {
    parks: Park[];
    api: String;
    goToPark: string;
};

export type ChipTranslations = {
    equipment: {
        BBQArea: string;
        ClimbingFrame: string;
        RainShelter: string;
        RunningTrack: string;
        SandPlayArea: string;
        SleddingHill: string;
        SwingSet: string;
        WaterAvailability: string;
        WindShelter: string;
    };
    typesofplay: {
        BalancingPlay: string;
        CarPlay: string;
        HopscotchArea: string;
        PlayCircuit: string;
        RockingPlay: string;
        RolePlay: string;
        SlidePlay: string;
        SoundPlay: string;
        SpinningPlay: string;
        ToddlerPlay: string;
        WaterPlay: string;
    };
};
