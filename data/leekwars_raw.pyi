# Auto-généré depuis les game data Leek Wars (API de combat, 100% objet). Ne pas éditer à la main.
from typing import Any, Callable

CellLike = Cell | Entity | int
EntityLike = Entity | int
WeaponLike = Weapon | int
ChipLike = Chip | int

class Effect:
    raw: list
    type: int
    value: int
    caster: Entity
    turns: int
    critical: bool
    item: Weapon | Chip
    target: Entity
    modifiers: int
    @staticmethod
    def getAll() -> list[int]: ...
    ABSOLUTE_SHIELD: int
    ABSOLUTE_VULNERABILITY: int
    ADD_STATE: int
    AFTEREFFECT: int
    ALLY_KILLED_TO_AGILITY: int
    ANTIDOTE: int
    ATTRACT: int
    BOOST_MAX_LIFE: int
    BUFF_AGILITY: int
    BUFF_MP: int
    BUFF_RESISTANCE: int
    BUFF_STRENGTH: int
    BUFF_TP: int
    BUFF_WISDOM: int
    CRITICAL_TO_HEAL: int
    DAMAGE: int
    DAMAGE_RETURN: int
    DAMAGE_TO_ABSOLUTE_SHIELD: int
    DAMAGE_TO_RESISTANCE: int
    DAMAGE_TO_STRENGTH: int
    DEBUFF: int
    HEAL: int
    INVERT: int
    KILL: int
    KILL_TO_TP: int
    LIFE_DAMAGE: int
    MOVED_TO_MP: int
    MULTIPLY_STATS: int
    NOVA_DAMAGE: int
    NOVA_DAMAGE_TO_MAGIC: int
    NOVA_VITALITY: int
    POISON: int
    POISON_TO_SCIENCE: int
    PROPAGATION: int
    PUSH: int
    RAW_ABSOLUTE_SHIELD: int
    RAW_BUFF_AGILITY: int
    RAW_BUFF_MAGIC: int
    RAW_BUFF_MP: int
    RAW_BUFF_POWER: int
    RAW_BUFF_RESISTANCE: int
    RAW_BUFF_SCIENCE: int
    RAW_BUFF_STRENGTH: int
    RAW_BUFF_TP: int
    RAW_BUFF_WISDOM: int
    RAW_HEAL: int
    RAW_RELATIVE_SHIELD: int
    RELATIVE_SHIELD: int
    REMOVE_SHACKLES: int
    REPEL: int
    RESURRECT: int
    SHACKLE_AGILITY: int
    SHACKLE_MAGIC: int
    SHACKLE_MP: int
    SHACKLE_STRENGTH: int
    SHACKLE_TP: int
    SHACKLE_WISDOM: int
    STEAL_ABSOLUTE_SHIELD: int
    STEAL_LIFE: int
    SUMMON: int
    SUPERINFECTION: int
    TELEPORT: int
    TOTAL_DEBUFF: int
    VULNERABILITY: int
    class Modifier:
        IRREDUCTIBLE: int
        MULTIPLIED_BY_TARGETS: int
        NOT_REPLACEABLE: int
        ON_CASTER: int
        STACKABLE: int
    class Target:
        ALLIES: int
        CASTER: int
        ENEMIES: int
        NON_SUMMONS: int
        SUMMONS: int

class Feature:
    raw: list
    type: int
    minValue: int
    maxValue: int
    turns: int
    targets: int
    modifiers: int

class Message:
    raw: list
    author: Entity
    type: int
    params: Any
    class Type:
        ATTACK: int
        BUFF_AGILITY: int
        BUFF_MP: int
        BUFF_STRENGTH: int
        BUFF_TP: int
        CUSTOM: int
        DEBUFF: int
        HEAL: int
        MOVE_AWAY: int
        MOVE_AWAY_CELL: int
        MOVE_TOWARD: int
        MOVE_TOWARD_CELL: int
        SHIELD: int

class Cell:
    id: int
    x: int
    y: int
    empty: bool
    obstacle: bool
    entity: Entity
    hasEntity: bool
    content: int
    def distance(self, target: CellLike) -> int: ...
    def pathLength(self, target: CellLike, ignoredCells: list = ...) -> int: ...
    def lineOfSight(self, target: CellLike, ignoredEntities: Any = ...) -> bool: ...
    def path(self, target: CellLike, ignoredCells: list = ...) -> list[Cell]: ...
    def onSameLine(self, target: CellLike) -> bool: ...
    @staticmethod
    def get(id: int) -> Cell: ...
    class Type:
        EMPTY: int
        ENTITY: int
        OBSTACLE: int

class Item:
    id: int
    cost: int
    minRange: int
    maxRange: int
    name: str
    area: int
    launchType: int
    maxUses: int
    inline: bool
    needsLos: bool
    failure: int
    features: list[Feature]
    def effectiveArea(self, cell: CellLike, frm: CellLike = ...) -> list[Cell]: ...
    @staticmethod
    def get(id: int) -> Weapon | Chip: ...
    class Area:
        ALLIES: int
        CIRCLE_1: int
        CIRCLE_2: int
        CIRCLE_3: int
        ENEMIES: int
        FIRST_INLINE: int
        LASER_LINE: int
        PLUS_1: int
        PLUS_2: int
        PLUS_3: int
        POINT: int
        SQUARE_1: int
        SQUARE_2: int
        X_1: int
        X_2: int
        X_3: int
    class LaunchType:
        CIRCLE: int
        DIAGONAL: int
        DIAGONAL_INVERTED: int
        LINE: int
        LINE_INVERTED: int
        STAR: int
        STAR_INVERTED: int

class Weapon(Item):
    cost: int
    minRange: int
    maxRange: int
    name: str
    area: int
    launchType: int
    maxUses: int
    inline: bool
    needsLos: bool
    failure: int
    features: list[Feature]
    passiveFeatures: list[Feature]
    def effectiveArea(self, cell: CellLike, frm: CellLike = ...) -> list[Cell]: ...
    @staticmethod
    def get(id: int) -> Weapon: ...
    @staticmethod
    def getAll() -> list[Weapon]: ...
    @staticmethod
    def isWeapon(value: Any) -> bool: ...
    axe: Weapon
    bazooka: Weapon
    bLaser: Weapon
    broadsword: Weapon
    darkKatana: Weapon
    desertSaber: Weapon
    destroyer: Weapon
    doubleGun: Weapon
    electrisor: Weapon
    enhancedLightninger: Weapon
    explorerRifle: Weapon
    flameThrower: Weapon
    gazor: Weapon
    grenadeLauncher: Weapon
    heavySword: Weapon
    illicitGrenadeLauncher: Weapon
    jLaser: Weapon
    katana: Weapon
    laser: Weapon
    lightninger: Weapon
    machineGun: Weapon
    magnum: Weapon
    mLaser: Weapon
    mysteriousElectrisor: Weapon
    neutrino: Weapon
    pistol: Weapon
    plutoniumBazooka: Weapon
    quantumRifle: Weapon
    revokedMLaser: Weapon
    rhino: Weapon
    rifle: Weapon
    shotgun: Weapon
    sunSpear: Weapon
    sword: Weapon
    unbridledGazor: Weapon
    unstableDestroyer: Weapon
    odachi: Weapon
    excalibur: Weapon
    scythe: Weapon

class Chip(Item):
    cost: int
    cooldown: int
    currentCooldown: int
    minRange: int
    maxRange: int
    minScope: int
    maxScope: int
    name: str
    area: int
    launchType: int
    maxUses: int
    inline: bool
    needsLos: bool
    failure: int
    features: list[Feature]
    bulbChips: list[Chip]
    bulbCharacteristics: dict
    bulbStats: dict
    def currentCooldownOf(self, entity: EntityLike) -> int: ...
    def effectiveArea(self, cell: CellLike, frm: CellLike = ...) -> list[Cell]: ...
    @staticmethod
    def get(id: int) -> Chip: ...
    @staticmethod
    def getAll() -> list[Chip]: ...
    @staticmethod
    def isChip(value: Any) -> bool: ...
    acceleration: Chip
    adrenaline: Chip
    alteration: Chip
    antidote: Chip
    apocalypse: Chip
    armor: Chip
    armoring: Chip
    arsenic: Chip
    awakening: Chip
    awekening: Chip
    ballAndChain: Chip
    bandage: Chip
    bark: Chip
    boxingGlove: Chip
    brainwashing: Chip
    bramble: Chip
    burning: Chip
    capsaicin: Chip
    carapace: Chip
    chilliPepper: Chip
    collar: Chip
    corn: Chip
    covetousness: Chip
    covid: Chip
    crushing: Chip
    cure: Chip
    desintegration: Chip
    devilStrike: Chip
    divineProtection: Chip
    dome: Chip
    doping: Chip
    drip: Chip
    elevation: Chip
    exasperation: Chip
    ferocity: Chip
    fertilizer: Chip
    fireBall: Chip
    fireBulb: Chip
    flame: Chip
    flash: Chip
    fortress: Chip
    fracture: Chip
    grapple: Chip
    healerBulb: Chip
    helmet: Chip
    hemorrhage: Chip
    ice: Chip
    iceberg: Chip
    icedBulb: Chip
    inversion: Chip
    jump: Chip
    kemuridama: Chip
    kill: Chip
    knowledge: Chip
    leatherBoots: Chip
    liberation: Chip
    lightning: Chip
    lightningBulb: Chip
    loam: Chip
    manumission: Chip
    maturation: Chip
    metallicBulb: Chip
    meteorite: Chip
    mirror: Chip
    motivation: Chip
    mutation: Chip
    pebble: Chip
    piquant: Chip
    plague: Chip
    plasma: Chip
    popcorn: Chip
    precipitation: Chip
    prism: Chip
    protein: Chip
    prototaxite: Chip
    punishment: Chip
    punyBulb: Chip
    rage: Chip
    rampart: Chip
    reflexes: Chip
    regeneration: Chip
    remission: Chip
    repotting: Chip
    resurrection: Chip
    rock: Chip
    rockfall: Chip
    rockyBulb: Chip
    savantBulb: Chip
    serum: Chip
    sevenLeagueBoots: Chip
    shield: Chip
    shock: Chip
    shuriken: Chip
    slowDown: Chip
    solidification: Chip
    soporific: Chip
    spark: Chip
    stalactite: Chip
    steroid: Chip
    sugar: Chip
    stretching: Chip
    superinfection: Chip
    tacticianBulb: Chip
    teleportation: Chip
    therapy: Chip
    thorn: Chip
    thunder: Chip
    toxin: Chip
    tranquilizer: Chip
    transmutation: Chip
    trebuchet: Chip
    vaccine: Chip
    vampirization: Chip
    venom: Chip
    wall: Chip
    warmUp: Chip
    whip: Chip
    wingedBoots: Chip
    wizardBulb: Chip
    wizardry: Chip

class Entity:
    id: int
    entityType: int
    life: int
    maxLife: int
    tp: int
    maxTP: int
    mp: int
    maxMP: int
    strength: int
    agility: int
    wisdom: int
    resistance: int
    science: int
    magic: int
    power: int
    level: int
    name: str
    absoluteShield: int
    relativeShield: int
    damageReturn: int
    frequency: int
    cores: int
    ram: int
    cell: Cell
    weapon: Weapon
    weapons: list[Weapon]
    chips: list[Chip]
    effects: list[Effect]
    launchedEffects: list[Effect]
    passiveEffects: list[Feature]
    states: list
    summons: list[Entity]
    summoner: Entity
    summoned: bool
    alive: bool
    dead: bool
    isStatic: bool
    birthTurn: int
    turnOrder: int
    awakeningZone: int
    side: int
    leekID: int
    teamID: int
    teamName: str
    compositionName: str
    farmerID: int
    farmerName: str
    farmerCountry: str
    aiID: int
    aiName: str
    def isAlly(self) -> bool: ...
    def isEnemy(self) -> bool: ...
    def stat(self, stat: int) -> int: ...
    @staticmethod
    def get(id: int) -> Entity: ...
    def distance(self, target: CellLike) -> int: ...
    class Type:
        BULB: int
        CHEST: int
        LEEK: int
        MOB: int
        PLANT: int
        TURRET: int
    class Stat:
        ABSOLUTE_SHIELD: int
        AGILITY: int
        CORES: int
        DAMAGE_RETURN: int
        FREQUENCY: int
        LIFE: int
        MAGIC: int
        MP: int
        POWER: int
        RAM: int
        RELATIVE_SHIELD: int
        RESISTANCE: int
        SCIENCE: int
        STRENGTH: int
        TP: int
        WISDOM: int

class Me(Entity):
    def moveToward(self, target: CellLike, mp: int = ...) -> int: ...
    def moveAwayFrom(self, target: CellLike, mp: int = ...) -> int: ...
    def moveTowardCells(self, cells: list, mp: int = ...) -> int: ...
    def moveTowardEntities(self, entities: list, mp: int = ...) -> int: ...
    def moveTowardLine(self, a: CellLike, b: CellLike, mp: int = ...) -> int: ...
    def moveAwayFromCells(self, cells: list, mp: int = ...) -> int: ...
    def moveAwayFromEntities(self, entities: list, mp: int = ...) -> int: ...
    def moveAwayFromLine(self, a: CellLike, b: CellLike, mp: int = ...) -> int: ...
    def useWeapon(self, target: EntityLike) -> int: ...
    def useWeaponOnCell(self, cell: CellLike) -> int: ...
    def useChip(self, chip: ChipLike, target: EntityLike = ...) -> int: ...
    def useChipOnCell(self, chip: ChipLike, cell: CellLike) -> int: ...
    def setWeapon(self, weapon: WeaponLike) -> bool: ...
    def say(self, message: Any) -> bool: ...
    def lama(self) -> None: ...
    def canUseWeapon(self, target: EntityLike | WeaponLike, weapon: WeaponLike | EntityLike = ...) -> bool: ...
    def canUseWeaponOnCell(self, cell: CellLike | WeaponLike, weapon: WeaponLike | CellLike = ...) -> bool: ...
    def canUseChip(self, chip: ChipLike, target: EntityLike) -> bool: ...
    def canUseChipOnCell(self, chip: ChipLike, cell: CellLike) -> bool: ...
    def resurrect(self, target: EntityLike, cell: CellLike) -> int: ...
    def itemUses(self, item: WeaponLike | ChipLike) -> int: ...
    def setLoadout(self, name: str, changeStats: bool = ...) -> bool: ...
    def summon(self, chip: ChipLike, cell: CellLike, callback: Callable[..., Any], name: str = ...) -> int: ...
    def weaponCell(self, target: EntityLike | CellLike, weapon: WeaponLike = ..., ignoredCells: list = ...) -> Cell: ...
    def weaponCells(self, target: EntityLike | CellLike, weapon: WeaponLike = ..., ignoredCells: list = ...) -> list[Cell]: ...
    def chipCell(self, chip: ChipLike, target: EntityLike | CellLike, ignoredCells: list = ...) -> Cell: ...
    def chipCells(self, chip: ChipLike, target: EntityLike | CellLike, ignoredCells: list = ...) -> list[Cell]: ...
    def weaponTargets(self, cell: CellLike, weapon: WeaponLike = ...) -> list[Entity]: ...
    def chipTargets(self, chip: ChipLike, cell: CellLike) -> list[Entity]: ...

class Leek(Entity):
    pass

class Turret(Entity):
    pass

class Bulb(Entity):
    type: int
    class Type:
        FIRE: int
        HEALER: int
        ICED: int
        LIGHTNING: int
        METALLIC: int
        PUNY: int
        ROCKY: int
        SAVANT: int
        TACTICIAN: int
        WIZARD: int

class Chest(Entity):
    type: int
    class Type:
        DIAMOND: int
        IRON: int
        WOOD: int

class Mob(Entity):
    type: int
    class Type:
        BLUE_CRYSTAL: int
        EVIL_PUMPKIN: int
        FENNEL_KING: int
        FENNEL_KNIGHT: int
        FENNEL_SCRIBE: int
        FENNEL_SQUIRE: int
        GRAAL: int
        GREEN_CRYSTAL: int
        HUBBARD: int
        NASU_RONIN: int
        NASU_SAMURAI: int
        NASU_SEITO: int
        NASU_WARRIOR: int
        OFFSPRING: int
        RED_CRYSTAL: int
        TURBAN: int
        WARTY: int
        YELLOW_CRYSTAL: int

class Plant(Entity):
    type: int
    class Type:
        CHILLI_PEPPER: int
        CORN: int
        PROTOTAXITE: int

class State:
    INVINCIBLE: int
    PACIFIST: int
    ROOTED: int
    STATIC: int
    STERILE: int
    UNHEALABLE: int

class _Registers:
    def get(self, key: str) -> str: ...
    def set(self, key: str, value: Any) -> bool: ...
    def delete(self, key: str) -> None: ...
    def all(self) -> dict[str, str]: ...

Registers: _Registers

class _Fight:
    me: Me
    turn: int
    id: int
    type: int
    context: int
    batched: bool
    boss: int
    winner: int
    alliesLife: int
    enemiesLife: int
    def getNearestEnemy(self) -> Entity: ...
    def getNearestAlly(self) -> Entity: ...
    def getFarthestEnemy(self) -> Entity: ...
    def getFarthestAlly(self) -> Entity: ...
    def getNearestEnemyTo(self, target: EntityLike) -> Entity: ...
    def getNearestAllyTo(self, target: EntityLike) -> Entity: ...
    def getEnemies(self) -> list[Entity]: ...
    def getAllies(self) -> list[Entity]: ...
    def getAliveEnemies(self) -> list[Entity]: ...
    def getAliveAllies(self) -> list[Entity]: ...
    def getDeadEnemies(self) -> list[Entity]: ...
    def getDeadAllies(self) -> list[Entity]: ...
    def getEnemiesCount(self) -> int: ...
    def getAlliesCount(self) -> int: ...
    def getAliveEnemiesCount(self) -> int: ...
    def getAliveAlliesCount(self) -> int: ...
    def getDeadEnemiesCount(self) -> int: ...
    def getAlliedTurret(self) -> Entity: ...
    def getEnemyTurret(self) -> Entity: ...
    def getNearestEnemyToCell(self, cell: CellLike) -> Entity: ...
    def getNearestAllyToCell(self, cell: CellLike) -> Entity: ...
    def getNextPlayer(self, entity: EntityLike = ...) -> Entity: ...
    def getPreviousPlayer(self, entity: EntityLike = ...) -> Entity: ...
    def listen(self) -> list: ...
    def weaponCell(self, target: EntityLike | CellLike, weapon: WeaponLike = ..., ignoredCells: list = ...) -> Cell: ...
    def weaponCells(self, target: EntityLike | CellLike, weapon: WeaponLike = ..., ignoredCells: list = ...) -> list[Cell]: ...
    def chipCell(self, chip: ChipLike, target: EntityLike | CellLike, ignoredCells: list = ...) -> Cell: ...
    def chipCells(self, chip: ChipLike, target: EntityLike | CellLike, ignoredCells: list = ...) -> list[Cell]: ...
    def weaponTargets(self, cell: CellLike, weapon: WeaponLike = ...) -> list[Entity]: ...
    def chipTargets(self, chip: ChipLike, cell: CellLike) -> list[Entity]: ...
    CRITICAL_FACTOR: int
    MAX_TURNS: int
    SUMMON_LIMIT: int
    class Use:
        CRITICAL: int
        INVALID_COOLDOWN: int
        INVALID_POSITION: int
        INVALID_TARGET: int
        MAX_USES: int
        NOT_ENOUGH_TP: int
        RESURRECT_INVALID_ENTITY: int
        SUCCESS: int
        TOO_MANY_SUMMONS: int
    class Erosion:
        CRITICAL_BONUS: int
        DAMAGE: int
        POISON: int
    class Boss:
        EVIL_PUMPKIN: int
        FENNEL_KING: int
        NASU_SAMOURAI: int
        NASU_SAMURAI: int
    class Context:
        CHALLENGE: int
        GARDEN: int
        TEST: int
        TOURNAMENT: int
    class Type:
        BATTLE_ROYALE: int
        BOSS: int
        CHEST_HUNT: int
        COLOSSUS: int
        FARMER: int
        SOLO: int
        TEAM: int
        WAR: int

Fight: _Fight

class _Field:
    type: int
    def cellFromXY(self, x: int, y: int) -> Cell: ...
    def getObstacles(self) -> list[Cell]: ...
    def distance(self, a: CellLike, b: CellLike) -> int: ...
    def cellDistance(self, a: CellLike, b: CellLike) -> int: ...
    def euclideanDistance(self, a: CellLike, b: CellLike) -> float: ...
    def pathLength(self, a: CellLike, b: CellLike, ignoredCells: list = ...) -> int: ...
    def lineOfSight(self, a: CellLike, b: CellLike, ignoredEntities: Any = ...) -> bool: ...
    def onSameLine(self, a: CellLike, b: CellLike) -> bool: ...
    def path(self, a: CellLike, b: CellLike, ignoredCells: list = ...) -> list[Cell]: ...
    NEXUS: int
    FACTORY: int
    DESERT: int
    FOREST: int
    GLACIER: int
    BEACH: int
    TEMPLE: int
    CASTLE: int
    CEMETERY: int
    TEIEN: int

Field: _Field

class _Network:
    def sendTo(self, entity: EntityLike, type: int, params: Any) -> bool: ...
    def sendAll(self, type: int, params: Any) -> None: ...
    def getMessages(self, entity: EntityLike = ...) -> list[Message]: ...

Network: _Network

class _Debug:
    def log(self, value: Any, color: int = ...) -> None: ...
    def mark(self, cells: Any, color: int = ..., duration: int = ...) -> bool: ...
    def markText(self, cells: Any, text: Any, color: int = ..., duration: int = ...) -> bool: ...
    def clearMarks(self) -> None: ...
    def show(self, cell: CellLike, color: int = ...) -> bool: ...
    def pause(self) -> None: ...

Debug: _Debug

class _System:
    operations: int
    maxOperations: int
    instructionsCount: int
    usedRAM: int
    maxRAM: int
    date: str
    time: str
    timestamp: int

System: _System

class _Color:
    def rgb(self, r: int, g: int, b: int) -> int: ...
    def red(self, color: int) -> int: ...
    def green(self, color: int) -> int: ...
    def blue(self, color: int) -> int: ...
    BLUE: int
    GREEN: int
    RED: int

Color: _Color

class _Math:
    def isPermutation(self, a: int, b: int) -> bool: ...
    def signum(self, x: float) -> int: ...
    def setBit(self, x: int, bit: int, value: bool = True) -> int: ...
    def testBit(self, x: int, bit: int) -> bool: ...
    def bitReverse(self, x: int) -> int: ...
    def byteReverse(self, x: int) -> int: ...
    def rotateLeft(self, x: int, count: int) -> int: ...
    def rotateRight(self, x: int, count: int) -> int: ...
    def leadingZeros(self, x: int) -> int: ...
    def trailingZeros(self, x: int) -> int: ...
    def realBits(self, x: float) -> int: ...
    def bitsToReal(self, bits: int) -> float: ...

Math: _Math

__all__ = ['Cell', 'Entity', 'Weapon', 'Chip', 'Item', 'Effect', 'Feature', 'Message', 'Me', 'Leek', 'Turret', 'Bulb', 'Chest', 'Mob', 'Plant', 'State', 'CellLike', 'EntityLike', 'WeaponLike', 'ChipLike', 'Registers', 'Fight', 'Field', 'Network', 'Debug', 'System', 'Color', 'Math']
