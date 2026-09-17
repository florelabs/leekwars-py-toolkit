// --- API de combat orientée objet (LeekScript v5-style) ---
// Les signatures écrivent les unions EN TOUTES LETTRES (`Cell | Entity | number`) au lieu d'un alias
// nommé : le survol dit alors directement ce qu'on peut passer, et surtout on n'ajoute AUCUN nom au
// scope global. Un `type Position` global entrerait en collision avec un `class Position` écrit par
// un joueur (TS2300 -> IA marquée invalide via le pont de diagnostics). Les alias historiques sont
// conservés ci-dessous, dépréciés, pour ne casser aucune IA existante qui les annote.
/** @deprecated Écrire `Cell | Entity | number`. */
type CellLike = Cell | Entity | number;
/** @deprecated Écrire `Entity | number`. */
type EntityLike = Entity | number;
/** @deprecated Écrire `Weapon | number`. */
type WeaponLike = Weapon | number;
/** @deprecated Écrire `Chip | number`. */
type ChipLike = Chip | number;

/** Un effet actif ou lancé sur une entité (Effect.DAMAGE, Effect.HEAL...). */
declare class Effect {
	/** Tableau brut [type, value, caster, turns, critical, item, target, modifiers]. */
	readonly raw: any[];
	readonly type: Effect.Type;
	readonly value: number;
	readonly caster: Entity | null;
	readonly turns: number;
	readonly critical: boolean;
	/** Arme ou puce qui a appliqué l'effet, null si aucune. L'id brut reste dans raw[5]. */
	readonly item: Weapon | Chip | null;
	readonly target: Entity | null;
	/** Bitmask de modificateurs (Effect.Modifier.STACKABLE...). */
	readonly modifiers: Effect.Modifier;
	/** Liste des ids de TYPES d'effets existants (Effect.DAMAGE, Effect.HEAL...). */
	static getAll(): Effect.Type[];
}

/** Un message d'équipe reçu (cf Network.getMessages). */
declare class Message {
	/** Tableau brut [auteur, type, params]. */
	readonly raw: any[];
	/** Entité alliée qui a envoyé le message. Toujours définie. */
	readonly author: Entity;
	/** Type du message (Message.Type.*). */
	readonly type: Message.Type;
	readonly params: any;
}

/** Une caractéristique déclarée par une arme/puce (ou un effet passif) : ce que l'item peut faire
 *  quand il touche (dégâts, poison, téléport, inversion...). Potentiel, fourchette de valeurs.
 *  À distinguer d'Effect (un effet actif sur une entité). */
declare class Feature {
	/** Tableau brut [type, minValue, maxValue, turns, targets, modifiers]. */
	readonly raw: any[];
	readonly type: Effect.Type;
	readonly minValue: number;
	readonly maxValue: number;
	readonly turns: number;
	/** Bitmask des cibles visées (Effect.Target.ALLIES, ENEMIES...). */
	readonly targets: Effect.Target;
	/** Bitmask de modificateurs (Effect.Modifier.STACKABLE...). */
	readonly modifiers: Effect.Modifier;
}

declare class Cell {
	readonly id: number;
	readonly x: number;
	readonly y: number;
	readonly empty: boolean;
	readonly obstacle: boolean;
	readonly entity: Entity | null;
	/** Une entité occupe-t-elle la case. */
	readonly hasEntity: boolean;
	/** Contenu de la case (Cell.Type.EMPTY/PLAYER/ENTITY/OBSTACLE). */
	readonly content: Cell.Type;
	distance(target: Cell | Entity | number): number;
	pathLength(target: Cell | Entity | number, ignoredCells?: (Cell | Entity | number)[]): number;
	lineOfSight(target: Cell | Entity | number, ignoredEntities?: Entity | number | (Entity | number)[]): boolean;
	/** Chemin (liste de cellules) jusqu'à la cible, en évitant 'ignoredCells'. */
	path(target: Cell | Entity | number, ignoredCells?: (Cell | Entity | number)[]): Cell[];
	/** La case est-elle alignée (même ligne ou colonne) avec la cible. */
	onSameLine(target: Cell | Entity | number): boolean;
	/** Cellule d'id 'id', ou null s'il est invalide. L'API accepte des ids partout : voici le chemin
	 *  inverse, indispensable dès qu'on relit un id rangé dans un registre. */
	static get(id: number): Cell | null;
}

/** Base commune aux armes et puces : tout ce qu'une arme ET une puce savent faire (coût, portée,
 *  zone, caractéristiques...). Permet d'écrire du code générique sur un équipement quelconque
 *  (`function best(item: Item) { return item.cost }`). Porte aussi les constantes partagées
 *  (Item.LaunchType, Item.Area). Weapon et Chip redéclarent ces membres pour garder CHACUN sa
 *  documentation propre (getWeaponCost vs getChipCost), pas parce qu'ils diffèrent. */
declare class Item {
	readonly id: number;
	/** Coût en PT d'une utilisation. */
	readonly cost: number;
	/** Portée minimale, en nombre de cases. */
	readonly minRange: number;
	/** Portée maximale, en nombre de cases. */
	readonly maxRange: number;
	/** Nom de l'item (Pistolet, Bandage...). */
	readonly name: string;
	/** Forme de la zone d'effet (Item.Area.SINGLE_CELL, CIRCLE_2...). */
	readonly area: Item.Area;
	/** Contrainte de visée (Item.LaunchType.LINE, STAR, CIRCLE...). */
	readonly launchType: Item.LaunchType;
	/** Nombre maximal d'utilisations par tour (0 = illimité). */
	readonly maxUses: number;
	/** L'item ne peut viser que dans l'alignement de l'entité. */
	readonly inline: boolean;
	/** L'item exige une ligne de vue dégagée jusqu'à la cible. */
	readonly needsLos: boolean;
	/** Pourcentage d'échec. */
	readonly failure: number;
	/** Caractéristiques déclarées de l'item (dégâts, poison, téléport...). cf Feature. */
	readonly features: Feature[];
	/** Zone d'effet réelle de l'item sur 'cell', utilisé depuis 'from' (défaut : position courante). */
	effectiveArea(cell: Cell | Entity | number, from?: Cell | Entity | number): Cell[];
	/** L'item (arme OU puce) d'id 'id', ou null si l'id n'en désigne aucun. */
	static get(id: number): Weapon | Chip | null;
}

declare class Weapon extends Item {
	readonly cost: number;
	readonly minRange: number;
	readonly maxRange: number;
	readonly name: string;
	readonly area: Item.Area;
	readonly launchType: Item.LaunchType;
	readonly maxUses: number;
	readonly inline: boolean;
	readonly needsLos: boolean;
	/** Pourcentage d'échec de l'arme. */
	readonly failure: number;
	/** Caractéristiques déclarées de l'arme (dégâts, poison, téléport...). cf Feature. */
	readonly features: Feature[];
	/** Caractéristiques passives de l'arme (bonus quand elle est équipée). */
	readonly passiveFeatures: Feature[];
	/** Zone d'effet réelle de l'arme sur 'cell', tirée depuis 'from' (défaut : position courante). */
	effectiveArea(cell: Cell | Entity | number, from?: Cell | Entity | number): Cell[];
	/** L'arme d'id 'id', ou null si l'id n'est pas celui d'une arme. */
	static get(id: number): Weapon | null;
	/** Toutes les armes du jeu. */
	static getAll(): Weapon[];
	/** La valeur est-elle un id d'arme valide. */
	static isWeapon(value: any): boolean;
}

declare class Chip extends Item {
	readonly cost: number;
	readonly cooldown: number;
	readonly currentCooldown: number;
	readonly minRange: number;
	readonly maxRange: number;
	readonly minScope: number;
	readonly maxScope: number;
	readonly name: string;
	readonly area: Item.Area;
	readonly launchType: Item.LaunchType;
	readonly maxUses: number;
	readonly inline: boolean;
	readonly needsLos: boolean;
	/** Pourcentage d'échec de la puce. */
	readonly failure: number;
	/** Caractéristiques déclarées de la puce. cf Feature. */
	readonly features: Feature[];
	/** Pour une puce d'INVOCATION : puces du bulbe invoqué. */
	readonly bulbChips: Chip[];
	/** Pour une puce d'INVOCATION : caractéristiques du bulbe invoqué. */
	readonly bulbCharacteristics: any;
	/** Pour une puce d'INVOCATION : statistiques du bulbe invoqué. */
	readonly bulbStats: any;
	/** Cooldown restant de la puce pour une AUTRE entité que soi. */
	currentCooldownOf(entity: Entity | number): number;
	/** Zone d'effet réelle de la puce sur 'cell', lancée depuis 'from' (défaut : position courante). */
	effectiveArea(cell: Cell | Entity | number, from?: Cell | Entity | number): Cell[];
	/** La puce d'id 'id', ou null si l'id n'est pas celui d'une puce. */
	static get(id: number): Chip | null;
	/** Toutes les puces du jeu. */
	static getAll(): Chip[];
	/** La valeur est-elle un id de puce valide. */
	static isChip(value: any): boolean;
}

// Sous-types d'entité. Héritage exprimé par 'interface X extends Entity' (côté INSTANCE, structurel)
// plutôt que 'class X extends Entity' : ainsi le static side d'Entity (Entity.Type, Entity.Stat)
// n'est PAS propagé aux sous-classes, ce qui évite le conflit TS entre Entity.Type et
// Chest/Bulb/Mob.Type. 'x instanceof Bulb', l'assignabilité à Entity et les propriétés héritées
// fonctionnent identiquement (le runtime, lui, fait un vrai class extends).
/** Un poireau. */
declare class Leek {}
interface Leek extends Entity {}
/** Une tourelle d'équipe. */
declare class Turret {}
interface Turret extends Entity {}
/** Un bulbe invoqué. */
declare class Bulb {
	/** Sous-type de bulbe (Bulb.Type.PUNY...). */
	readonly type: Bulb.Type;
}
interface Bulb extends Entity {}
/** Un coffre (chasse aux coffres). */
declare class Chest {
	/** Sous-type de coffre (Chest.Type.WOOD...). */
	readonly type: Chest.Type;
}
interface Chest extends Entity {}
/** Un monstre / boss. */
declare class Mob {
	/** Sous-type de monstre (Mob.Type.GRAAL...). */
	readonly type: Mob.Type;
}
interface Mob extends Entity {}
/** Une plante invoquée (enracinée : elle ne joue pas son tour). */
declare class Plant {
	/** Espèce de plante (Plant.Type.CORN...). */
	readonly type: Plant.Type;
}
interface Plant extends Entity {}

declare class Entity {
	readonly id: number;
	/** Genre d'entité (Entity.Type.LEEK/BULB/TURRET/CHEST/MOB/PLANT). À ne pas confondre avec le .type des sous-classes (sous-variante : Bulb.Type.*...). */
	readonly entityType: Entity.Type;
	readonly life: number;
	readonly maxLife: number;
	readonly tp: number;
	readonly maxTP: number;
	readonly mp: number;
	readonly maxMP: number;
	readonly strength: number;
	readonly agility: number;
	readonly wisdom: number;
	readonly resistance: number;
	readonly science: number;
	readonly magic: number;
	readonly power: number;
	readonly level: number;
	readonly name: string;
	readonly absoluteShield: number;
	readonly relativeShield: number;
	readonly damageReturn: number;
	readonly frequency: number;
	readonly cores: number;
	readonly ram: number;
	readonly cell: Cell;
	readonly weapon: Weapon | null;
	readonly weapons: Weapon[];
	readonly chips: Chip[];
	readonly effects: Effect[];
	readonly launchedEffects: Effect[];
	readonly passiveEffects: Feature[];
	readonly states: State.Type[];
	readonly summons: Entity[];
	readonly summoner: Entity | null;
	readonly summoned: boolean;
	readonly alive: boolean;
	readonly dead: boolean;
	/** L'entité ne peut pas bouger (tourelle, coffre...). */
	readonly isStatic: boolean;
	readonly birthTurn: number;
	readonly turnOrder: number;
	/** Rayon de la zone d'Éveil, 0 pour une entité qui joue son tour. */
	readonly awakeningZone: number;
	readonly side: number;
	readonly leekID: number;
	readonly teamID: number;
	readonly teamName: string;
	readonly compositionName: string;
	readonly farmerID: number;
	readonly farmerName: string;
	readonly farmerCountry: string;
	readonly aiID: number;
	readonly aiName: string;
	isAlly(): boolean;
	isEnemy(): boolean;
	/** Valeur d'une caractéristique par sa constante (Entity.Stat.STRENGTH...). */
	stat(stat: Entity.Stat): number;
	distance(target: Cell | Entity | number): number;
	/** Entité d'id 'id' (typée : Leek, Bulb, Mob...), ou null s'il est invalide. Chemin inverse des
	 *  ids acceptés partout par l'API : relire un id d'entité rangé dans un registre, par exemple. */
	static get(id: number): Entity | null;
}

declare class Me extends Entity {
	/** Se rapproche de 'target' en dépensant au plus 'mp' PM (défaut : tous). */
	moveToward(target: Cell | Entity | number, mp?: number): number;
	moveAwayFrom(target: Cell | Entity | number, mp?: number): number;
	moveTowardCells(cells: (Cell | Entity | number)[], mp?: number): number;
	moveTowardEntities(entities: (Entity | number)[], mp?: number): number;
	moveTowardLine(a: Cell | Entity | number, b: Cell | Entity | number, mp?: number): number;
	moveAwayFromCells(cells: (Cell | Entity | number)[], mp?: number): number;
	moveAwayFromEntities(entities: (Entity | number)[], mp?: number): number;
	moveAwayFromLine(a: Cell | Entity | number, b: Cell | Entity | number, mp?: number): number;
	useWeapon(target: Entity | number): Fight.Use;
	useWeaponOnCell(cell: Cell | Entity | number): Fight.Use;
	useChip(chip: Chip | number, target?: Entity | number): Fight.Use;
	useChipOnCell(chip: Chip | number, cell: Cell | Entity | number): Fight.Use;
	setWeapon(weapon: Weapon | number): boolean;
	say(message: any): boolean;
	/** Fait dire « lama » à ton entité. */
	lama(): void;
	// Les canUse* renvoient un BOOLÉEN (moteur : Type.BOOL), pas un code Fight.Use : ce sont des
	// prédicats « est-ce possible », pas des tentatives. Seules les actions réelles (useWeapon,
	// useChip, resurrect, summon) renvoient un Fight.Use.
	// Même forme que weaponCell/weaponTargets : la cible d'abord, l'arme optionnelle ensuite (l'arme
	// équipée par défaut). L'ordre historique arme-en-premier reste accepté quand l'arme est un OBJET.
	/** Peut-on utiliser l'arme (celle équipée, ou 'weapon') sur 'target'. */
	canUseWeapon(target: Entity | number, weapon?: Weapon | number): boolean;
	canUseWeapon(weapon: Weapon, target: Entity | number): boolean;
	/** Peut-on utiliser l'arme (celle équipée, ou 'weapon') sur la case 'cell'. */
	canUseWeaponOnCell(cell: Cell | Entity | number, weapon?: Weapon | number): boolean;
	canUseWeaponOnCell(weapon: Weapon, cell: Cell | Entity | number): boolean;
	canUseChip(chip: Chip | number, target: Entity | number): boolean;
	canUseChipOnCell(chip: Chip | number, cell: Cell | Entity | number): boolean;
	resurrect(target: Entity | number, cell: Cell | Entity | number): Fight.Use;
	/** Nombre d'utilisations de l'item (arme ou puce) ce tour. */
	itemUses(item: Item | number): number;
	/** Change l'équipement courant (nom du loadout). 'changeStats' (défaut true) applique aussi sa répartition de capital. */
	setLoadout(name: string, changeStats?: boolean): boolean;
	/** Invoque un bulbe : 'callback' est rejouée à chaque tour du bulbe (me désigne alors le bulbe). */
	summon(chip: Chip | number, cell: Cell | Entity | number, callback: () => void, name?: string): Fight.Use;
	// Les six helpers de ciblage ci-dessous sont AUSSI (et plus logiquement) sur Fight : ils calculent
	// sur la carte sans rien devoir à l'entité courante, sinon le défaut de l'arme équipée. Ce sont les
	// mêmes fonctions, gardées ici parce que l'API les y a publiées en premier.
	/** Cellule d'où utiliser l'arme (courante ou 'weapon') sur 'target' (une entité OU une case). */
	weaponCell(target: Cell | Entity | number, weapon?: Weapon | number, ignoredCells?: (Cell | Entity | number)[]): Cell | null;
	/** Toutes les cellules d'où utiliser l'arme sur 'target'. */
	weaponCells(target: Cell | Entity | number, weapon?: Weapon | number, ignoredCells?: (Cell | Entity | number)[]): Cell[];
	/** Cellule d'où utiliser 'chip' sur 'target' (une entité OU une case). */
	chipCell(chip: Chip | number, target: Cell | Entity | number, ignoredCells?: (Cell | Entity | number)[]): Cell | null;
	/** Toutes les cellules d'où utiliser 'chip' sur 'target'. */
	chipCells(chip: Chip | number, target: Cell | Entity | number, ignoredCells?: (Cell | Entity | number)[]): Cell[];
	/** Entités touchées si l'arme (courante ou 'weapon') est utilisée sur la case 'cell'. */
	weaponTargets(cell: Cell | Entity | number, weapon?: Weapon | number): Entity[];
	/** Entités touchées si 'chip' est utilisée sur la case 'cell'. */
	chipTargets(chip: Chip | number, cell: Cell | Entity | number): Entity[];
}

// Stockage persistant de l'IA. Reste un `declare const` (et pas un namespace) : `delete` est un mot
// réservé, donc `function delete(...)` serait une erreur de syntaxe dans un namespace.
declare const Registers: {
	/** Valeur du registre 'key', ou null s'il n'existe pas. Les registres ne stockent que du texte. */
	get(key: string): string | null;
	/** Écrit un registre (la valeur est convertie en texte). false si la limite de registres est atteinte. */
	set(key: string, value: any): boolean;
	delete(key: string): void;
	/** Tous les registres de l'entité, clé -> valeur. */
	all(): Record<string, string>;
};

declare namespace Fight {
	/** L'IA courante (votre entité). */
	const me: Me;
	const turn: number;
	/** Id du combat. */
	const id: number;
	/** Type de combat (Fight.Type.SOLO...). */
	const type: Fight.Type;
	/** Contexte du combat (Fight.Context.GARDEN...). */
	const context: Fight.Context;
	/** Le combat fait-il partie d'un lot ? Un combat de lot a le même type et le même contexte qu'un combat lancé seul. */
	const batched: boolean;
	/** Boss du combat (Fight.Boss.*), s'il y en a un. */
	const boss: Fight.Boss;
	const winner: number;
	/** Somme des PV des alliés / des ennemis. */
	const alliesLife: number;
	const enemiesLife: number;
	function getNearestEnemy(): Entity | null;
	function getNearestAlly(): Entity | null;
	function getFarthestEnemy(): Entity | null;
	function getFarthestAlly(): Entity | null;
	function getNearestEnemyTo(target: Entity | number): Entity | null;
	function getNearestAllyTo(target: Entity | number): Entity | null;
	function getEnemies(): Entity[];
	function getAllies(): Entity[];
	function getAliveEnemies(): Entity[];
	function getAliveAllies(): Entity[];
	function getDeadEnemies(): Entity[];
	function getDeadAllies(): Entity[];
	function getEnemiesCount(): number;
	function getAlliesCount(): number;
	function getAliveEnemiesCount(): number;
	function getAliveAlliesCount(): number;
	function getDeadEnemiesCount(): number;
	function getAlliedTurret(): Entity | null;
	function getEnemyTurret(): Entity | null;
	/** Entité alliée/ennemie la plus proche d'une CELLULE. */
	function getNearestEnemyToCell(cell: Cell | Entity | number): Entity | null;
	function getNearestAllyToCell(cell: Cell | Entity | number): Entity | null;
	/** Joueur suivant / précédent dans l'ordre de jeu (défaut : relatif à soi). */
	function getNextPlayer(entity?: Entity | number): Entity | null;
	function getPreviousPlayer(entity?: Entity | number): Entity | null;
	/** Paroles prononcées (say) par les entités : liste de [entité, message]. */
	function listen(): any[][];
	// Ciblage : d'où peut-on atteindre une cible, et qui serait touché. Ces six fonctions ne dépendent
	// d'aucune entité en particulier — l'arme équipée n'y est qu'un DÉFAUT — d'où leur place ici :
	// Fight.weaponCells(cell, enemy.weapon) dit où l'ENNEMI peut frapper. Elles restent aussi
	// accessibles depuis me (ce sont les mêmes fonctions).
	/** Cellule d'où utiliser l'arme (celle équipée, ou 'weapon') sur 'target' (une entité OU une case). */
	function weaponCell(target: Cell | Entity | number, weapon?: Weapon | number, ignoredCells?: (Cell | Entity | number)[]): Cell | null;
	/** Toutes les cellules d'où utiliser l'arme sur 'target'. */
	function weaponCells(target: Cell | Entity | number, weapon?: Weapon | number, ignoredCells?: (Cell | Entity | number)[]): Cell[];
	/** Cellule d'où utiliser 'chip' sur 'target' (une entité OU une case). */
	function chipCell(chip: Chip | number, target: Cell | Entity | number, ignoredCells?: (Cell | Entity | number)[]): Cell | null;
	/** Toutes les cellules d'où utiliser 'chip' sur 'target'. */
	function chipCells(chip: Chip | number, target: Cell | Entity | number, ignoredCells?: (Cell | Entity | number)[]): Cell[];
	/** Entités touchées si l'arme (celle équipée, ou 'weapon') est utilisée sur la case 'cell'. */
	function weaponTargets(cell: Cell | Entity | number, weapon?: Weapon | number): Entity[];
	/** Entités touchées si 'chip' est utilisée sur la case 'cell'. */
	function chipTargets(chip: Chip | number, cell: Cell | Entity | number): Entity[];
}

declare namespace Field {
	const type: Field.Type;
	function cellFromXY(x: number, y: number): Cell | null;
	function getObstacles(): Cell[];
	/** Distance en nombre de cases, comme Cell.distance et Entity.distance (alias : cellDistance). */
	function distance(a: Cell | Entity | number, b: Cell | Entity | number): number;
	function cellDistance(a: Cell | Entity | number, b: Cell | Entity | number): number;
	/** Distance à vol d'oiseau (réel, non entier). */
	function euclideanDistance(a: Cell | Entity | number, b: Cell | Entity | number): number;
	function pathLength(a: Cell | Entity | number, b: Cell | Entity | number, ignoredCells?: (Cell | Entity | number)[]): number;
	function lineOfSight(a: Cell | Entity | number, b: Cell | Entity | number, ignoredEntities?: Entity | number | (Entity | number)[]): boolean;
	/** Les deux cases sont-elles alignées (même ligne ou colonne). */
	function onSameLine(a: Cell | Entity | number, b: Cell | Entity | number): boolean;
	/** Chemin (liste de cellules) de 'from' à 'to', en évitant 'ignoredCells'. */
	function path(from: Cell | Entity | number, to: Cell | Entity | number, ignoredCells?: (Cell | Entity | number)[]): Cell[];
}

declare const Network: {
	/** Envoie un message typé (Message.Type.*) à une entité alliée. */
	sendTo(entity: Entity | number, type: Message.Type, params: any): boolean;
	/** Envoie un message typé à toutes les entités alliées. */
	sendAll(type: Message.Type, params: any): void;
	/** Messages reçus (de 'entity' seulement si fourni). */
	getMessages(entity?: Entity | number): Message[];
};

declare const Debug: {
	/** Écrit dans le journal de combat, éventuellement en couleur (cf Color). console.log existe aussi. */
	log(value: any, color?: Color.Value): void;
	mark(cells: Cell | Entity | number | (Cell | Entity | number)[], color?: Color.Value, duration?: number): boolean;
	markText(cells: Cell | Entity | number | (Cell | Entity | number)[], text: any, color?: Color.Value, duration?: number): boolean;
	clearMarks(): void;
	show(cell: Cell | Entity | number, color?: Color.Value): boolean;
	pause(): void;
};

declare namespace System {
	/** Opérations consommées ce tour (à comparer à maxOperations pour borner une recherche). */
	const operations: number;
	const maxOperations: number;
	const instructionsCount: number;
	const usedRAM: number;
	const maxRAM: number;
	const date: string;
	const time: string;
	const timestamp: number;
}

declare namespace Color {
	/** Compose une couleur depuis ses composantes 0-255. */
	function rgb(r: number, g: number, b: number): Color.Value;
	function red(color: Color.Value): number;
	function green(color: Color.Value): number;
	function blue(color: Color.Value): number;
}

interface Math {
	/** Vrai si les deux entiers ont exactement les mêmes chiffres, dans un ordre quelconque. */
	isPermutation(a: number, b: number): boolean;
	/** Convertit des radians en degrés. */
	toDegrees(radians: number): number;
	/** Convertit des degrés en radians. */
	toRadians(degrees: number): number;
	/** Entier aléatoire dans [a, b) — borne haute EXCLUE, comme en LeekScript. */
	randInt(a: number, b: number): number;
	/** Réel aléatoire dans [a, b). */
	randReal(a: number, b: number): number;
	isInfinite(x: number): boolean;
	/** Nombre de bits à 1. Opère sur 64 bits, contrairement aux opérateurs bitwise de JS. */
	bitCount(x: number): number;
	bitLength(x: number): number;
	testBit(x: number, bit: number): boolean;
	setBit(x: number, bit: number, value?: boolean): number;
	bitReverse(x: number): number;
	byteReverse(x: number): number;
	rotateLeft(x: number, count: number): number;
	rotateRight(x: number, count: number): number;
	leadingZeros(x: number): number;
	trailingZeros(x: number): number;
	/** Représentation binaire brute du réel, en entier 64 bits. */
	realBits(x: number): number;
	bitsToReal(bits: number): number;
}
