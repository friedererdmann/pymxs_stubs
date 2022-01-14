class MXSWrapperBase():
    ...
    def getmxsprop(self, key: str): ...
    def setmxsprop(self, key: str, value): ...
class MXSWrapperObjectSet():
    ...
    def getmxsprop(self, key: str): ...
    def setmxsprop(self, key: str, value): ...
class MXSWrapperObjectSetIter():
    ...
    def getmxsprop(self, key: str): ...
    def setmxsprop(self, key: str, value): ...
def _bootstrap_mxs(): ...
def animate(onoff): ...
def atlevel(node_name): ...
def attime(time): ...
def byref(o): ...
def contextmanager(func): ...
def mxsreference(o): ...
def mxstoken(): ...
def print_(*args): ...
def quiet(onoff): ...
def redraw(onoff): ...
def run_redo(): ...
def run_undo(): ...
class runtime():
    ...
    class A360Renderer(RendererClass):
        ALPHA: bool
        EXPOSURE: str
        FORMAT: str
        HEIGHT: int
        NOTIFYBYEMAIL: bool
        QUALITY: str
        RENDERTYPE: str
        WIDTH: int
        ...
    class A360RendererPresetsHelper(ReferenceTarget):
        ...
    class A360_Cloud_Rendering(RendererClass):
        ALPHA: bool
        EXPOSURE: str
        FORMAT: str
        HEIGHT: int
        NOTIFYBYEMAIL: bool
        QUALITY: str
        RENDERTYPE: str
        WIDTH: int
        ...
    class ACIS_SAT(ExporterPlugin):
        ...
    class ADTCategory(ReferenceTarget):
        ...
    class ADTObjMgrWrapper(FloatController):
        ...
    class ADTStyle(ReferenceTarget):
        ...
    class ADTStyleComp(ReferenceTarget):
        ...
    class ADT_Category(ReferenceTarget):
        ...
    class ADT_Object_Manager(ReferenceTarget):
        ...
    class ADT_Object_Manager_Wrapper(FloatController):
        ...
    class ADT_Style(ReferenceTarget):
        ...
    class ADT_StyleComposite(ReferenceTarget):
        ...
    class ADT_SyleLeaf(ReferenceTarget):
        ...
    class APEXSaveFBX(MAXScriptFunction):
        ...
    class ART_Renderer(RendererClass):
        ANTI_ALIASING_FILTER_DIAMETER: float
        ENABLE_ANIMATED_NOISE: bool
        ENABLE_ITERATIONS: bool
        ENABLE_NOISE_FILTER: bool
        ENABLE_OUTLIER_CLAMP: bool
        ENABLE_TIME: bool
        ITERATIONS: int
        MAXIMUM_INTERACTIVE_DOWN_RES_FACTOR: int
        MOTION_BLUR_ALL_OBJECTS: bool
        NOISE_FILTER_STRENGTH: float
        NOISE_FILTER_STRENGTH_PERCENTAGE: float
        POINT_LIGHT_DIAMETER: float
        QUALITY_DB: float
        RENDER_METHOD: int
        TEXTURE_BAKE_RESOLUTION: int
        TIME_IN_SECONDS: int
        TIME_SPLIT_HOURS: int
        TIME_SPLIT_MINUTES: int
        TIME_SPLIT_SECONDS: int
        ...
    class ART_Renderer_Noise_Filter(RenderElement):
        BITMAP: bool
        ELEMENTNAME: str
        ENABLED: bool
        STRENGTH: float
        STRENGTH_PERCENTAGE: float
        ...
    class ASec_Element(ReferenceTarget):
        ALPHA: int
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        APPLYLIGHTS: bool
        APPLYNOISE: bool
        AXIS: float
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        CIRCULARCOLORMIX: float
        CIRCULARMAP: None
        CIRCULARMTL: None
        COLORRADIUS1: float
        COLORRADIUS2: float
        COLORRADIUS3: float
        COLORRADIUS4: float
        COLORSOURCE: float
        EFFECTSID: int
        ELEMENTNAME: str
        FILTERALL: bool
        FILTERBRIGHTNESS: bool
        FILTEREDGE: bool
        FILTERHUE: bool
        FILTERPERIMETER: bool
        FILTERPERIMETERALPHA: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        INTENSITY: float
        MAXSIZE: float
        MINSIZE: float
        NOISEMAP: None
        OBJECTID: int
        OCCLUSION: float
        ON: bool
        PRESETS: int
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        QUADRANT4COLOR: MXSWrapperBase
        QUANTITY: int
        RADIALCOLOR1: MXSWrapperBase
        RADIALCOLOR2: MXSWrapperBase
        RADIALCOLOR3: MXSWrapperBase
        RADIALCOLOR4: MXSWrapperBase
        RADIALDENSITY: None
        RADIALMAP: None
        RADIALMTL: None
        RADIALSIZEMAP: None
        SIDES: int
        SOURCEALPHA: bool
        SOURCEEFFECTSID: bool
        SOURCEOBJECTID: bool
        SOURCESURFACENORMAL: bool
        SOURCEUNCLAMPEDCOLOR: bool
        SOURCEWHOLE: bool
        SOURCEZBUFFER: bool
        SQUEEZE: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        USECIRCULARMAP: bool
        USECIRCULARMTL: bool
        USERADIALDENSITY: bool
        USERADIALMAP: bool
        USERADIALMTL: bool
        USERADIALSIZEMAP: bool
        ZHI: float
        ZLO: float
        ...
    class ATF_Alias_Import(ImporterPlugin):
        ...
    class ATF_Alias_Importer(ImporterPlugin):
        ...
    class ATF_CATIA_V4_Import(ImporterPlugin):
        ...
    class ATF_CATIA_V4_Importer(ImporterPlugin):
        ...
    class ATF_CATIA_V5_Import(ImporterPlugin):
        ...
    class ATF_CATIA_V5_Importer(ImporterPlugin):
        ...
    class ATF_IGES_Import(ImporterPlugin):
        ...
    class ATF_IGES_Importer(ImporterPlugin):
        ...
    class ATF_JT_Import(ImporterPlugin):
        ...
    class ATF_JT_Importer(ImporterPlugin):
        ...
    class ATF_ProE_Import(ImporterPlugin):
        ...
    class ATF_ProE_Importer(ImporterPlugin):
        ...
    class ATF_SKETCHUP_Import(ImporterPlugin):
        ...
    class ATF_STEP_Import(ImporterPlugin):
        ...
    class ATF_STEP_Importer(ImporterPlugin):
        ...
    class ATF_Solidworks_Import(ImporterPlugin):
        ...
    class ATF_Solidworks_Importer(ImporterPlugin):
        ...
    class ATF_UG_NX_Import(ImporterPlugin):
        ...
    class ATF_UG_NX_Importer(ImporterPlugin):
        ...
    class ATSCustomDepsOps(Interface):
        ...
    class ATSMax(GlobalUtilityPlugin):
        ...
    class ATSOps(Interface):
        ...
    class AVI(BitmapIO):
        ...
    class ActionCreateFlow(MAXScriptFunction):
        ...
    class ActionEditFlow(MAXScriptFunction):
        ...
    class ActionExtendFlow(MAXScriptFunction):
        ...
    class ActionIdleAddMode(MAXScriptFunction):
        ...
    class ActionIdleSubtractMode(MAXScriptFunction):
        ...
    class ActionItemOverrideManager(Interface):
        ...
    class ActionOverlayManager(Interface):
        ...
    class ActionPredicate(Value):
        ...
    class ActivateTimeWarp(BipedGeneric):
        ...
    class ActiveShadeFragment(GraphicsFragmentPlugin):
        ...
    class ActiveShadeFragmentManager(Interface):
        ...
    class ActiveXControl(RolloutControl):
        ...
    class Adaptive_Halton(SamplerClass):
        ADAPTIVE_THRESHOLD: float
        ENABLE: bool
        ENABLE_ADAPTIVE: bool
        QUALITY: float
        ...
    class Adaptive_Uniform(SamplerClass):
        ADAPTIVE_THRESHOLD: float
        ENABLE: bool
        ENABLE_ADAPTIVE: bool
        QUALITY: float
        ...
    class AddConstraint(MAXScriptFunction):
        ...
    class AddListController(MAXScriptFunction):
        ...
    class AddMod(MAXScriptFunction):
        ...
    class AddPModObjects(MAXScriptFunction):
        ...
    class AddSubRollout(Primitive):
        ...
    class AdjustColorTool(UserDataTypeClass):
        ...
    class Adjust_Color_Tool(UserDataTypeClass):
        ...
    class AdobeT1(BezierFontLoaderClass):
        ...
    class Adobe_Illustrator(ExporterPlugin):
        ...
    class Adobe_Illustrator_Shape(ImporterPlugin):
        ...
    class AdtObjTranslator(ReferenceMaker):
        ...
    class Adv__Ray_Traced(Shadow):
        AA_THRESHOLD: MXSWrapperBase
        BLUR: float
        COPLANAR_THRESHOLD: float
        JITTER_AMT: float
        NOAREASHADOWS: bool
        PASS1: int
        PASS2: int
        RAY_BIAS: float
        SHADOW_MODE: int
        SHADOW_TRANSPARENT: bool
        SKIP_COPLANAR: bool
        SUPPRESS_MAT_AA: bool
        SUPPRESS_REFLT_AA: bool
        TWOSIDEDSHADOWS: bool
        ...
    class AdvancedWood(TextureMap):
        AXIS: int
        COORDS: MXSWrapperBase
        DIFFUSE_LOBE_WEIGHT: float
        DIFFUSE_PERLIN_PROF: str
        DIFFUSE_PERLIN_SCALE_Z: float
        EARLY_WOOD_COLOR: MXSWrapperBase
        EARLY_WOOD_COLOR_MAP: None
        EARLY_WOOD_COLOR_PERLIN_PROF: str
        EARLY_WOOD_SHARPNESS: float
        FIBER_COSINE_PROF: str
        FIBER_PERLIN_PROF: str
        FIBER_PERLIN_SCALE_Z: float
        GROOVE_ROUGHNESS: float
        GROWTH_PERLIN_PROF: str
        LATE_WOOD_BUMP_DEPTH: float
        LATE_WOOD_COLOR_PERLIN_PROF: str
        LATE_WOOD_COLOR_POWER: float
        LATE_WOOD_RATIO: float
        LATE_WOOD_SHARPNESS: float
        MANUAL_LATE_WOOD_COLOR: MXSWrapperBase
        MANUAL_LATE_WOOD_COLOR_MAP: None
        PORE_CELL_DIM: float
        PORE_COLOR_POWER: float
        PORE_DEPTH: float
        PORE_RADIUS: float
        PORE_TYPE: int
        PRESET: int
        RAY_COLOR_POWER: float
        RAY_ELLIPSE_SCALE_X: float
        RAY_ELLIPSE_Z2X: float
        RAY_NUM_SLICES: int
        RAY_SEG_LENGTH_Z: float
        RING_THICKNESS: float
        ROUGHNESS: float
        SCALE: float
        UNIT_DEPENDENT: bool
        USE_DIFFUSE_PERLIN: bool
        USE_EARLY_WOOD_COLOR_PERLIN: bool
        USE_FIBER_COSINE: bool
        USE_FIBER_PERLIN: bool
        USE_GROOVE_ROUGHNESS: bool
        USE_GROWTH_PERLIN: bool
        USE_LATE_WOOD_BUMP: bool
        USE_LATE_WOOD_COLOR_PERLIN: bool
        USE_MANUAL_LATE_WOOD_COLOR: bool
        USE_PORES: bool
        USE_RAYS: bool
        ...
    class Advanced_Lighting_Override(Material):
        BASEMATERIAL: MXSWrapperBase
        BUMPSCALE: float
        COLORBLEED: float
        LUMINANCESCALE: float
        REFLECTANCESCALE: float
        TRANSMITTANCESCALE: float
        ...
    class Advanced_Ray_Traced(Shadow):
        AA_THRESHOLD: MXSWrapperBase
        BLUR: float
        COPLANAR_THRESHOLD: float
        JITTER_AMT: float
        NOAREASHADOWS: bool
        PASS1: int
        PASS2: int
        RAY_BIAS: float
        SHADOW_MODE: int
        SHADOW_TRANSPARENT: bool
        SKIP_COPLANAR: bool
        SUPPRESS_MAT_AA: bool
        SUPPRESS_REFLT_AA: bool
        TWOSIDEDSHADOWS: bool
        ...
    class Affect_Region(Modifier):
        BUBBLE: float
        FALLOFF: float
        IGNOREBACKFACING: int
        PINCH: float
        ...
    class Age_Test(Helper):
        ADJUSTABLE_AGE: bool
        CONDITION_TYPE: int
        RANDOM_SEED: int
        SUBFRAME_SAMPLING: bool
        TEST_TYPE: int
        TEST_VALUE: int
        VARIATION: int
        ...
    class AlembicCamera(Camera):
        ...
    class AlembicContainer(GeometryClass):
        ICONSCALE: float
        NODES: MXSWrapperBase
        SHOWICON: bool
        ...
    class AlembicDummyObject(Helper):
        ...
    class AlembicExport(ExporterPlugin):
        ...
    class AlembicFloat(FloatController):
        IMPORTVISIBILITY: bool
        OBJECT: None
        PLAYBACKEND: float
        PLAYBACKENDGEN: int
        PLAYBACKFRAME: float
        PLAYBACKFRAMEGEN: int
        PLAYBACKSTART: float
        PLAYBACKSTARTGEN: int
        PLAYBACKTYPE: int
        PLAYBACKTYPEGEN: int
        PROPERTYPATH: None
        RANKINDEX: int
        SOURCE: str
        VISCONTROL: bool
        ...
    class AlembicImport(ImporterPlugin):
        ...
    class AlembicObject(GeometryClass):
        GENERATIONID: int
        IMPORTCUSTOMATTRIBUTES: bool
        IMPORTEXTRACHANNELS: bool
        IMPORTMATERIALIDS: bool
        IMPORTNORMALS: bool
        IMPORTUVS: bool
        IMPORTVELOCITY: bool
        IMPORTVERTEXCOLORS: bool
        OBJECT: None
        PLAYBACKEND: float
        PLAYBACKENDGEN: int
        PLAYBACKFRAME: float
        PLAYBACKFRAMEGEN: int
        PLAYBACKSTART: float
        PLAYBACKSTARTGEN: int
        PLAYBACKTYPE: int
        PLAYBACKTYPEGEN: int
        SOURCE: str
        ...
    class AlembicXform(Matrix3Controller):
        MAXCOORDS: bool
        OBJECT: None
        PLAYBACKEND: float
        PLAYBACKENDGEN: int
        PLAYBACKFRAME: float
        PLAYBACKFRAMEGEN: int
        PLAYBACKSTART: float
        PLAYBACKSTARTGEN: int
        PLAYBACKTYPE: int
        PLAYBACKTYPEGEN: int
        SOURCE: str
        ...
    class Alembic_Export(ExporterPlugin):
        ...
    class Alembic_Import(ImporterPlugin):
        ...
    class AlignObject(MappedPrimitive):
        ...
    class AlignPivot(MappedPrimitive):
        ...
    class AlignToParent(MappedPrimitive):
        ...
    class AlphaMap(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        TARGETMAPSLOTNAME: str
        ...
    class AlwaysEqualFilter(ReferenceMaker):
        ...
    class AmbientOcclusionBakeElement(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        BRIGHT: MXSWrapperBase
        DARK: MXSWrapperBase
        ELEMENTNAME: str
        ENABLED: bool
        FALLOFF: float
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAXDISTANCE: float
        OUTPUTSZX: int
        OUTPUTSZY: int
        SAMPLES: int
        SPREAD: float
        TARGETMAPSLOTNAME: str
        ...
    class Ambient_Occlusion(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        BRIGHT: MXSWrapperBase
        DARK: MXSWrapperBase
        ELEMENTNAME: str
        ENABLED: bool
        FALLOFF: float
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAXDISTANCE: float
        OUTPUTSZX: int
        OUTPUTSZY: int
        SAMPLES: int
        SPREAD: float
        TARGETMAPSLOTNAME: str
        ...
    class AmountChange(ReferenceTarget):
        CURRENT_FIRST_SPAWN_ID_DATA_CHANNEL: None
        CURRENT_SPAWN_COUNT_DATA_CHANNEL: None
        CURRENT_SPAWN_ORDER_DATA_CHANNEL: None
        EXECUTION_ORDER: int
        FILTER: None
        FIRST_SPAWN_ID_DATA_CHANNEL: None
        HISTORY_DEPENDENT: bool
        INPUT_1: None
        IS_CURRENT_PARENT_DATA_CHANNEL: None
        IS_CURRENT_SPAWN_DATA_CHANNEL: None
        LAST_SPAWN_ID_DATA_CHANNEL: None
        OLDER_SIBLING_ID_DATA_CHANNEL: None
        PARENT_ID_DATA_CHANNEL: None
        PROCEED_TYPE: int
        RESET_PARTICLE_AGE: bool
        SPAWNS_AS_NEW_IN_EVENT: bool
        SUB_TYPE: int
        TOTAL_SPAWN_COUNT_DATA_CHANNEL: None
        TYPE: int
        USE_CURRENT_FIRST_SPAWN_ID: bool
        USE_CURRENT_SPAWN_COUNT: bool
        USE_CURRENT_SPAWN_ORDER: bool
        USE_FIRST_SPAWN_ID: bool
        USE_IS_CURRENT_PARENT: bool
        USE_IS_CURRENT_SPAWN: bool
        USE_LAST_SPAWN_ID: bool
        USE_OLDER_SIBLING_ID: bool
        USE_PARENT_ID: bool
        USE_TOTAL_SPAWN_COUNT: bool
        ...
    class AnaglyphFragment(GraphicsFragmentPlugin):
        ...
    class Anchor(Helper):
        ...
    class AnchorCustomAttribute(CustAttrib):
        ...
    class AngleAxis(Value):
        ...
    class AngleControl(RolloutControl):
        ...
    class AnimLayerManager(Interface):
        ...
    class AnimTrack(ReferenceMaker):
        ...
    class Anisotropic(Shader):
        ...
    class Apollo_Effect(RenderEffect):
        AFFECTALPHA: bool
        AFFECTBYATMOSPHERE: bool
        AFFECTZBUFFER: bool
        ANGLE: float
        CENTERAFFECTSINTENSITY: bool
        CENTERAFFECTSSIZE: bool
        DISTAFFECTSINTENSITY: bool
        DISTAFFECTSSIZE: bool
        INNEROCCLUSIONRADIUS: float
        INTENSITY: float
        LIGHTDIRECTIONAFFECTSINTENSITY: bool
        LIGHTDIRECTIONAFFECTSSIZE: bool
        OCCLUSIONAFFECTSINTENSITY: bool
        OCCLUSIONAFFECTSSIZE: bool
        OUTEROCCLUSIONRADIUS: float
        SEED: int
        SIZE: float
        SQUEEZE: float
        ...
    class Apollo_Param_Container(GeometryClass):
        ...
    class AppendSubSelSet(Primitive):
        ...
    class ApplyOperation(MAXScriptFunction):
        ...
    class ApplyUVAsColor(Modifier):
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        _DUMMY: bool
        ...
    class ApplyUVAsHSLColor(Modifier):
        HUE_MAXIMUM: float
        HUE_MINIMUM: float
        LUMINANCE_MAXIMUM: float
        LUMINANCE_MINIMUM: float
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        SATURATION_MAXIMUM: float
        SATURATION_MINIMUM: float
        _DUMMY: bool
        ...
    class ApplyUVAsHSLGradient(Modifier):
        COLOR_1: MXSWrapperBase
        COLOR_2: MXSWrapperBase
        COLOR_3: MXSWrapperBase
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        USE_V_FOR_HUE: bool
        USE_V_FOR_LIGHTNESS: bool
        USE_V_FOR_SATURATION: bool
        _DUMMY: bool
        ...
    class ApplyUVAsHSLGradientWithMidpoint(Modifier):
        COLOR_1: MXSWrapperBase
        COLOR_2: MXSWrapperBase
        COLOR_3: MXSWrapperBase
        EASE_A: float
        EASE_B: float
        MIDPOINT: float
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        USE_V_FOR_HUE: bool
        USE_V_FOR_LIGHTNESS: bool
        USE_V_FOR_SATURATION: bool
        _DUMMY: bool
        ...
    class ArbAxis(Primitive):
        ...
    class ArbBone(Matrix3Controller):
        ...
    class ArbBoneTrans(Matrix3Controller):
        ...
    class Arc(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        FROM: float
        MAPCOORDS: bool
        OPTIMIZE: bool
        PIE: bool
        QUAD_CAP: bool
        RADIUS: float
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        REVERSE: bool
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        TO: float
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        ...
    class Architectural(Material):
        BUMPMAP: None
        BUMPMAPAMOUNT: float
        BUMPMAPENABLE: bool
        COLORBLEED: float
        CUTOUTMAP: None
        CUTOUTMAPAMOUNT: float
        CUTOUTMAPENABLE: bool
        DIFFUSE: MXSWrapperBase
        DIFFUSEMAP: None
        DIFFUSEMAPAMOUNT: float
        DIFFUSEMAPENABLE: bool
        DISPLACEMENTMAP: None
        DISPLACEMENTMAPAMOUNT: float
        DISPLACEMENTMAPENABLE: bool
        EMITLUMINANCE: bool
        FILTERMAP: None
        INDIRECTBUMPAMOUNT: float
        INTENSITYMAP: None
        INTENSITYMAPAMOUNT: float
        INTENSITYMAPENABLE: bool
        IOR: float
        LUMINANCE: float
        LUMINANCEMAP: None
        LUMINANCEMAPENABLE: bool
        MAPAMOUNTS: MXSWrapperBase
        MAPS: MXSWrapperBase
        MAPSENABLES: MXSWrapperBase
        RAWDIFFUSETEXTURE: bool
        REFLECTANCESCALE: float
        SAMPLER: int
        SAMPLERADAPTON: bool
        SAMPLERADAPTTHRESHOLD: float
        SAMPLERADVANCEDOPTIONS: bool
        SAMPLERBYNAME: str
        SAMPLERENABLE: bool
        SAMPLERQUALITY: float
        SAMPLERUSEGLOBAL: bool
        SHININESS: float
        SHININESSMAP: None
        SHININESSMAPENABLE: bool
        SUBSAMPLETEXTUREON: bool
        TEMPLATE: str
        TEXTUREHEIGHT: float
        TEXTUREUOFFSET: float
        TEXTUREVOFFSET: float
        TEXTUREWIDTH: float
        TRANSLUCENCY: float
        TRANSLUCENCYENABLE: bool
        TRANSLUCENCYMAP: None
        TRANSMITTANCESCALE: float
        TRANSPARENCY: float
        TRANSPARENCYMAPENABLE: bool
        TWOSIDED: bool
        USERPARAM0: float
        USERPARAM1: float
        USETEXTURESIZE: bool
        ...
    class ArchitecturalMaterial(Material):
        BUMPMAP: None
        BUMPMAPAMOUNT: float
        BUMPMAPENABLE: bool
        COLORBLEED: float
        CUTOUTMAP: None
        CUTOUTMAPAMOUNT: float
        CUTOUTMAPENABLE: bool
        DIFFUSE: MXSWrapperBase
        DIFFUSEMAP: None
        DIFFUSEMAPAMOUNT: float
        DIFFUSEMAPENABLE: bool
        DISPLACEMENTMAP: None
        DISPLACEMENTMAPAMOUNT: float
        DISPLACEMENTMAPENABLE: bool
        EMITLUMINANCE: bool
        FILTERMAP: None
        INDIRECTBUMPAMOUNT: float
        INTENSITYMAP: None
        INTENSITYMAPAMOUNT: float
        INTENSITYMAPENABLE: bool
        IOR: float
        LUMINANCE: float
        LUMINANCEMAP: None
        LUMINANCEMAPENABLE: bool
        MAPAMOUNTS: MXSWrapperBase
        MAPS: MXSWrapperBase
        MAPSENABLES: MXSWrapperBase
        RAWDIFFUSETEXTURE: bool
        REFLECTANCESCALE: float
        SAMPLER: int
        SAMPLERADAPTON: bool
        SAMPLERADAPTTHRESHOLD: float
        SAMPLERADVANCEDOPTIONS: bool
        SAMPLERBYNAME: str
        SAMPLERENABLE: bool
        SAMPLERQUALITY: float
        SAMPLERUSEGLOBAL: bool
        SHININESS: float
        SHININESSMAP: None
        SHININESSMAPENABLE: bool
        SUBSAMPLETEXTUREON: bool
        TEMPLATE: str
        TEXTUREHEIGHT: float
        TEXTUREUOFFSET: float
        TEXTUREVOFFSET: float
        TEXTUREWIDTH: float
        TRANSLUCENCY: float
        TRANSLUCENCYENABLE: bool
        TRANSLUCENCYMAP: None
        TRANSMITTANCESCALE: float
        TRANSPARENCY: float
        TRANSPARENCYMAPENABLE: bool
        TWOSIDED: bool
        USERPARAM0: float
        USERPARAM1: float
        USETEXTURESIZE: bool
        ...
    class Area(Filter):
        ...
    class Area_Shadows(Shadow):
        AA_THRESHOLD: MXSWrapperBase
        BLUR: float
        COPLANAR_THRESHOLD: float
        JITTER_AMT: float
        PASS1: int
        PASS2: int
        RAY_BIAS: float
        SHADOW_HEIGHT: float
        SHADOW_LENGTH: float
        SHADOW_MODE: int
        SHADOW_TRANSPARENT: bool
        SHADOW_WIDTH: float
        SKIP_COPLANAR: bool
        SUPPRESS_MAT_AA: bool
        SUPPRESS_REFLT_AA: bool
        TWOSIDEDSHADOWS: bool
        ...
    class Arnold(RendererClass):
        AA_SAMPLES: int
        AA_SAMPLES_MAX: int
        AA_SAMPLE_CLAMP: float
        AA_SAMPLE_CLAMP_AFFECTS_AOVS: bool
        AA_SAMPLE_CLAMP_ENABLED: bool
        ABORT_ON_ERROR: bool
        ABORT_ON_ERROR_ACTIVESHADE: bool
        ABORT_ON_LICENSE_FAIL: bool
        ADAPTIVE_THRESHOLD: float
        AOV_MANAGER: None
        AOV_SHADERS_MAP_0: None
        AOV_SHADERS_MAP_1: None
        AOV_SHADERS_MAP_2: None
        AOV_SHADERS_MAT_0: None
        AOV_SHADERS_MAT_1: None
        AOV_SHADERS_MAT_2: None
        ASS_FILE_PATH: None
        ATMOSPHERE: None
        AUTODETECT_THREADS: bool
        AUTO_SHUTTER: bool
        AUTO_TRANSPARENCY_DEPTH: int
        BUCKET_SCANNING: int
        BUCKET_SIZE: int
        CURVES_DEFAULT_BASIS: int
        CURVES_DEFAULT_MIN_PIXEL_WIDTH: float
        CURVES_DEFAULT_MODE: int
        DEFAULT_GPU_MIN_MEMORY_MB: int
        DEFAULT_GPU_NAMES: str
        DEFORM_KEYS: int
        DIELECTRIC_PRIORITIES: bool
        DISPLACEMENT_DEFAULT_SUBDIV_ADAPTIVE_ERROR: float
        DISPLACEMENT_DEFAULT_SUBDIV_ITERATIONS: int
        DISPLACEMENT_DEFAULT_SUBDIV_TYPE: int
        DRIVER_TYPE: None
        ENABLE_ADAPTIVE_SAMPLING: bool
        ENABLE_DEFORM_KEYS: bool
        ENABLE_TRANSFORM_KEYS: bool
        ENABLE_USER_OPTIONS: bool
        ENV_ADV_BGND_CUSTOM_COLOR: MXSWrapperBase
        ENV_ADV_BGND_CUSTOM_MAP: None
        ENV_ADV_BGND_CUSTOM_SHADER: None
        ENV_ADV_BGND_MODE: int
        ENV_ADV_BGND_VISIBLE_TO_CAMERA: bool
        ENV_ADV_BGND_VISIBLE_TO_DIFFUSE_REFLECTIONS: bool
        ENV_ADV_BGND_VISIBLE_TO_DIFFUSE_TRANSMISSION: bool
        ENV_ADV_BGND_VISIBLE_TO_SPECULAR_REFLECTIONS: bool
        ENV_ADV_BGND_VISIBLE_TO_SPECULAR_TRANSMISSION: bool
        ENV_ADV_BGND_VISIBLE_TO_VOLUME_SCATTERING: bool
        ENV_ADV_IBL_AFFECT_INDIRECT: bool
        ENV_ADV_IBL_AFFECT_SSS: bool
        ENV_ADV_IBL_AFFECT_VOLUME: bool
        ENV_ADV_IBL_CAMERA_MULT: float
        ENV_ADV_IBL_CAST_SHADOWS: bool
        ENV_ADV_IBL_DIFFUSE_MULT: float
        ENV_ADV_IBL_EMIT_CAMERA: bool
        ENV_ADV_IBL_EMIT_DIFFUSE: bool
        ENV_ADV_IBL_EMIT_SPECULAR: bool
        ENV_ADV_IBL_EMIT_TRANSMISSION: bool
        ENV_ADV_IBL_INDIRECT_MULT: float
        ENV_ADV_IBL_MAX_BOUNCES: int
        ENV_ADV_IBL_MULTIPLIER: float
        ENV_ADV_IBL_PORTAL_MODE: int
        ENV_ADV_IBL_RESOLUTION: int
        ENV_ADV_IBL_RESOLUTION_ENABLE: bool
        ENV_ADV_IBL_SHADOW_COLOR: MXSWrapperBase
        ENV_ADV_IBL_SHADOW_DENSITY: float
        ENV_ADV_IBL_SPECULAR_MULT: float
        ENV_ADV_IBL_SSS_MULT: float
        ENV_ADV_IBL_TRANSMISSION_MULT: float
        ENV_ADV_IBL_VOLUME_MULT: float
        ENV_ADV_IBL_VOLUME_SAMPLES: int
        ENV_IBL_ENABLE: bool
        ENV_IBL_SAMPLES: int
        ENV_MODE: int
        ENV_PHYS_BGND_COLOR: MXSWrapperBase
        ENV_PHYS_BGND_MAP: None
        ENV_PHYS_BGND_MODE: int
        ERROR_COLOR_BAD_PIXEL: MXSWrapperBase
        ERROR_COLOR_BAD_SHADER: MXSWrapperBase
        ERROR_COLOR_BAD_TEXTURE: MXSWrapperBase
        EXPAND_PROCEDURALS: bool
        EXPORT_BINARY: bool
        EXPORT_CAMERAS: bool
        EXPORT_DRIVERSFILTERS: bool
        EXPORT_GEOMETRY: bool
        EXPORT_LIGHTS: bool
        EXPORT_OPERATORS: bool
        EXPORT_OPTION: bool
        EXPORT_SHADERS: bool
        EXPORT_TO_ASS: bool
        EXPORT_TO_ASS_ORIGIN: int
        EXPORT_TO_MTLX: bool
        FILTER: int
        FILTER_WIDTH: float
        GEOMETRY_DICING_CAMERA: None
        GI_DIFFUSE_DEPTH: int
        GI_DIFFUSE_SAMPLES: int
        GI_SPECULAR_DEPTH: int
        GI_SPECULAR_SAMPLES: int
        GI_SSS_SAMPLES: int
        GI_TOTAL_DEPTH: int
        GI_TRANSMISSION_DEPTH: int
        GI_TRANSMISSION_SAMPLES: int
        GI_VOLUME_DEPTH: int
        GI_VOLUME_SAMPLES: int
        GPU_AUTO_SELECTION: bool
        GPU_MAX_TEXTURE_RESOLUTION: int
        GPU_RENDERING: bool
        GPU_SELECTION: MXSWrapperBase
        IGNORE_ATMOSPHERE: bool
        IGNORE_BUMP: bool
        IGNORE_DISPLACEMENT: bool
        IGNORE_DOF: bool
        IGNORE_LIGHTS: bool
        IGNORE_MOTION: bool
        IGNORE_MOTION_BLUR: bool
        IGNORE_OPERATORS: bool
        IGNORE_SHADERS: bool
        IGNORE_SHADOWS: bool
        IGNORE_SMOOTHING: bool
        IGNORE_SSS: bool
        IGNORE_SUBDIVISION: bool
        IGNORE_TEXTURES: bool
        IMAGER_0: None
        INDIRECT_SAMPLE_CLAMP: float
        INDIRECT_SPECULAR_BLUR: float
        LEGACY_3DS_MAX_MAP_SUPPORT: bool
        LOCK_SAMPLING_PATTERN: bool
        LOG_FILE: None
        LOG_RENDER_PROFILE: bool
        LOG_RENDER_STATS: bool
        LOG_TO_CONSOLE: bool
        LOG_TO_FILE: bool
        LOW_LIGHT_THRESHOLD: float
        MATERIAL_EXPORT_LIST: MXSWrapperBase
        MAX_SUBDIVISIONS: int
        MAX_WARNINGS: int
        MTLX_FILE_PATH: None
        MTLX_LOOK: str
        MTLX_PROPERTIES: None
        MTLX_RELATIVE: bool
        MTLX_USE_CURRENT_SELECTION: bool
        NOICE_ADDITIONAL_FRAMES: int
        NOICE_ANIM_RANGE: int
        NOICE_END_FRAME: int
        NOICE_INPUT: str
        NOICE_LIGHT_AOV_NAMES: str
        NOICE_OUTPUT: str
        NOICE_PATCH_RADIUS: int
        NOICE_SEARCH_RADIUS: int
        NOICE_START_FRAME: int
        NOICE_VARIANCE: float
        OPERATOR_EXPORT_LIST: MXSWrapperBase
        OPERATOR_EXPORT_TREE: bool
        OPERATOR_ROOT: None
        OUTPUT_DENOISING_AOVS: bool
        PHYSICAL_MATERIAL_SSS_TYPE: int
        PLUGIN_SEARCHPATH: None
        PREPASS_ENABLED: bool
        PREPASS_SAMPLES: int
        PROCEDURAL_SEARCHPATH: None
        PROGRESSIVE_RENDER: bool
        RENDER_DEVICE: int
        RENDER_DEVICE_FALLBACK: int
        RENDER_PROFILE_FILE: None
        RENDER_STATS_FILE: None
        RENDER_STATS_MODE: int
        RENDER_VIEW_SETTINGS: str
        RESPECT_PHYSICAL_CAMERA_MOTION_BLUR: bool
        RETRANSLATE_ALL_FRAMES: bool
        SHADER_OVERRIDE: None
        SHADER_OVERRIDE_ENABLED: bool
        SHOW_BUCKET_CORNERS_AS: bool
        SHOW_BUCKET_CORNERS_PROD: bool
        SHUTTER_CLOSE: float
        SHUTTER_LENGTH: float
        SHUTTER_OPEN: float
        SHUTTER_POSITION: int
        SHUTTER_TYPE: int
        SKIP_LICENSE_CHECK: bool
        SSS_USE_AUTOBUMP: bool
        SUBDIV_FRUSTUM_CULLING: bool
        SUBDIV_FRUSTUM_PADDING: float
        TEXTURE_ACCEPT_UNMIPPED: bool
        TEXTURE_ACCEPT_UNTILED: bool
        TEXTURE_AUTOMIP: bool
        TEXTURE_AUTOTILE: int
        TEXTURE_ENABLE_AUTOTILE: bool
        TEXTURE_MAX_MEMORY_MB: int
        TEXTURE_MAX_OPEN_FILES: int
        TEXTURE_PER_FILE_STATS: bool
        TEXTURE_SEARCHPATH: None
        THREADS: int
        TRANSFORM_KEYS: int
        USER_OPTIONS: None
        USE_EXISTING_TX: bool
        USE_OPTIX_ON_BEAUTY: bool
        USE_QUADS: int
        USE_RENDER_VIEW: bool
        VERBOSITY_LEVEL: int
        ...
    class ArnoldAOV(ReferenceTarget):
        ACTIVE: bool
        DATA: str
        DENOISED: bool
        FILTER: str
        FILTERWIDTH: float
        LAYERENABLEFILTERING: bool
        LAYERHALFPRECISION: bool
        LAYERTOLERANCE: float
        LIGHTGROUP: str
        NAME: None
        ...
    class ArnoldAOVsManager(ReferenceTarget):
        ...
    class ArnoldAOVsManagerClassDescCreator(Interface):
        ...
    class ArnoldDEEPEXRDriver(ReferenceTarget):
        ACTIVE: bool
        ALPHAHALFPRECISION: bool
        ALPHATOLERANCE: float
        AOVLIST: MXSWrapperBase
        APPEND: bool
        CUSTOMATTRIBUTES: None
        DEPTHHALFPRECISION: bool
        DEPTHTOLERANCE: float
        FILENAMESUFFIX: None
        LIGHTGROUP: str
        NAME: None
        SUBPIXELMERGE: bool
        TILED: bool
        USEAOVNAME: bool
        USERGBOPACITY: bool
        ...
    class ArnoldEXRDriver(ReferenceTarget):
        ACTIVE: bool
        AOVLIST: MXSWrapperBase
        APPEND: bool
        AUTOCROP: bool
        COMPRESSION: str
        CUSTOMATTRIBUTES: None
        FILENAMESUFFIX: None
        HALFPRECISION: bool
        LIGHTGROUP: str
        NAME: None
        PRESERVELAYERNAME: bool
        TILED: bool
        USEAOVNAME: bool
        ...
    class ArnoldFluidUtility(Interface):
        ...
    class ArnoldGeometryPropertiesModifier(Modifier):
        AUTOBUMP_CAMERA: bool
        AUTOBUMP_DIFFUSE_REFLECTIONS: bool
        AUTOBUMP_DIFFUSE_TRANSMISSION: bool
        AUTOBUMP_SPECULAR_REFLECTIONS: bool
        AUTOBUMP_SPECULAR_TRANSMISSION: bool
        AUTOBUMP_VOLUME_SCATTERING: bool
        CASTS_SHADOWS: bool
        DISPLACEMENT_BOUNDS_PADDING: float
        DISPLACEMENT_ENABLE_AUTOBUMP: bool
        DISPLACEMENT_HEIGHT: float
        DISPLACEMENT_MAP: None
        DISPLACEMENT_MAP_ON: bool
        DISPLACEMENT_ZERO: float
        DOUBLE_SIDED: bool
        ENABLE_CAMERA: bool
        ENABLE_DISPLACEMENT_OPTIONS: bool
        ENABLE_FILTERMAP: bool
        ENABLE_GENERAL_OPTIONS: bool
        ENABLE_LIGHT_GROUP: bool
        ENABLE_MIKKT: bool
        ENABLE_POINTS: bool
        ENABLE_SHADOW_GROUP: bool
        ENABLE_SHADOW_OPTIONS: bool
        ENABLE_SSS_OPTIONS: bool
        ENABLE_SUBDIVISION_OPTIONS: bool
        ENABLE_TOON_OPTIONS: bool
        ENABLE_USER_OPTIONS: bool
        ENABLE_UV_REMAP: bool
        ENABLE_VISIBILITY_OPTIONS: bool
        ENABLE_VOLUME: bool
        FILTERMAP: None
        INVERT_NORMALS: bool
        LIGHT_GROUP: MXSWrapperBase
        MATTE: bool
        MIKKT_UV_CHANNEL: int
        MIN_PIXEL_WIDTH: float
        MODE: int
        MOTION_BLUR_DEFORMATION_KEYS: int
        MOTION_BLUR_TRANSFORM_KEYS: int
        MOTION_BLUR_USE_DEFORMATION: bool
        MOTION_BLUR_USE_TRANSFORM: bool
        OPAQUE: bool
        PARTICLE_SYS_AS_POINTS: bool
        PRIMARY_VISIBILITY: bool
        RADIAL_DISTORTION: float
        RADIAL_DISTORTION_TYPE: int
        RECEIVE_SHADOWS: bool
        SELF_SHADOWS: bool
        SHADOW_GROUP: MXSWrapperBase
        SSS_SET_NAME: None
        STEP_SIZE: float
        SUBDIVISION_ADAPTIVE_ERROR: float
        SUBDIVISION_ITERATIONS: int
        SUBDIVISION_METRIC: int
        SUBDIVISION_SMOOTH_TANGENTS: bool
        SUBDIVISION_SPACE: int
        SUBDIVISION_TYPE: int
        SUBDIVISION_UV_TYPE: int
        SUBDIV_FRUSTUM_IGNORE: bool
        TOON_ID: None
        TRACE_SETS: None
        USER_OPTIONS: None
        UV_REMAP: None
        VISIBLE_TO_DIFFUSE_REFLECTIONS: bool
        VISIBLE_TO_DIFFUSE_TRANSMISSION: bool
        VISIBLE_TO_SPECULAR_REFLECTIONS: bool
        VISIBLE_TO_SPECULAR_TRANSMISSION: bool
        VISIBLE_TO_VOLUME_SCATTERING: bool
        VOLUME_PADDING: float
        ...
    class ArnoldJPEGDriver(ReferenceTarget):
        ACTIVE: bool
        AOVLIST: MXSWrapperBase
        COLOR_SPACE: int
        DITHER: bool
        FILENAMESUFFIX: None
        LIGHTGROUP: str
        NAME: None
        OUTPUTPADDED: bool
        QUALITY: int
        USEAOVNAME: bool
        ...
    class ArnoldLightBlockerFilterModifier(Modifier):
        AXIS: int
        DENSITY: float
        GEOMETRY_TYPE: int
        HEIGHT_EDGE: float
        OBJECT: None
        POSITIONX: float
        POSITIONY: float
        POSITIONZ: float
        RAMP: float
        ROTATIONX: float
        ROTATIONY: float
        ROTATIONZ: float
        ROUNDNESS: float
        SCALEX: float
        SCALEY: float
        SCALEZ: float
        SHADER: None
        USESHADER: bool
        WIDTH_EDGE: float
        ...
    class ArnoldLightFilterModifier(Modifier):
        LIGHTFILTER: None
        VIEWPORTDATA: None
        VIEWPORTSHAPE: None
        ...
    class ArnoldMapToMtl(Material):
        OPAQUEENABLED: bool
        SURFACESHADER: None
        SURFACESHADERENABLED: bool
        ...
    class ArnoldPNGDriver(ReferenceTarget):
        ACTIVE: bool
        AOVLIST: MXSWrapperBase
        COLOR_SPACE: int
        DITHER: bool
        FILENAMESUFFIX: None
        FORMAT: None
        LIGHTGROUP: str
        NAME: None
        OUTPUTPADDED: bool
        USEAOVNAME: bool
        ...
    class ArnoldSceneSourceExport(ExporterPlugin):
        ...
    class ArnoldShadersLoader(GlobalUtilityPlugin):
        ...
    class ArnoldTIFFDriver(ReferenceTarget):
        ACTIVE: bool
        AOVLIST: MXSWrapperBase
        APPEND: bool
        COLOR_SPACE: int
        COMPRESSION: str
        DITHER: bool
        FILENAMESUFFIX: None
        FORMAT: None
        LIGHTGROUP: str
        NAME: None
        OUTPUTPADDED: bool
        SKIPALPHA: bool
        TILED: bool
        UNPREMULTALPHA: bool
        USEAOVNAME: bool
        ...
    class Arnold_A(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Alembic_Object(GeometryClass):
        ANIMANIMEND: int
        ANIMANIMSTART: int
        ANIMATED: bool
        ANIMATION_CACHE: int
        ANIMEXTEND: bool
        ANIMLOOP: bool
        ANIMPINGPONG: bool
        ANIMSEQUENCEEND: int
        ANIMSEQUENCESTART: int
        ANIMSPEED: float
        BBOXHI: MXSWrapperBase
        BBOXLOW: MXSWrapperBase
        BBOX_THRESHOLD: float
        EXCLUDE_XFORM: bool
        EXPAND_HIDDEN: bool
        FILENAME: str
        FLIP_V: bool
        FPS: float
        FRAME: float
        LAYERS: MXSWrapperBase
        MAKE_INSTANCE: bool
        NAMEPREFIX: str
        NAME_SPACE: str
        OBJECTPATH: str
        OPERATOR: None
        PULL_USER_PARAMS: bool
        RADIUS_ATTRIBUTE: str
        RADIUS_DEFAULT: float
        RADIUS_SCALE: float
        SCENE_CAMERA: str
        SUBDIV_ITERATIONS: int
        UPAXIS: int
        USE_ANIMATION_CACHE: bool
        USE_BBOX_THRESHOLD: bool
        USE_VP_ANIMATION: bool
        VELOCITY_IGNORE: bool
        VELOCITY_SCALE: float
        VIEWPORT_MODE: int
        VISIBILITY_IGNORE: bool
        ...
    class Arnold_Barndoor(Modifier):
        ARNOLD_NODE: str
        ARNOLD_NODE_BARNDOOR_BOTTOM_EDGE: float
        ARNOLD_NODE_BARNDOOR_BOTTOM_LEFT: float
        ARNOLD_NODE_BARNDOOR_BOTTOM_RIGHT: float
        ARNOLD_NODE_BARNDOOR_LEFT_BOTTOM: float
        ARNOLD_NODE_BARNDOOR_LEFT_EDGE: float
        ARNOLD_NODE_BARNDOOR_LEFT_TOP: float
        ARNOLD_NODE_BARNDOOR_RIGHT_BOTTOM: float
        ARNOLD_NODE_BARNDOOR_RIGHT_EDGE: float
        ARNOLD_NODE_BARNDOOR_RIGHT_TOP: float
        ARNOLD_NODE_BARNDOOR_TOP_EDGE: float
        ARNOLD_NODE_BARNDOOR_TOP_LEFT: float
        ARNOLD_NODE_BARNDOOR_TOP_RIGHT: float
        ...
    class Arnold_Light(Light):
        AFFECTVIEWPORT: bool
        ALWAYSVISIBLEINVIEWPORT: bool
        ANGLE: float
        AOV: str
        AOV_INDIRECT: bool
        ASPECT_RATIO: float
        CAMERA: float
        CAST_SHADOWS: bool
        CAST_VOLUMETRIC_SHADOWS: bool
        COLOR: MXSWrapperBase
        CONE_ANGLE: float
        DIFFUSE: float
        EXPOSURE: float
        FILENAME: str
        FILTER: MXSWrapperBase
        FORMAT: int
        HEIGHT: float
        INDIRECT: float
        INTENSITY: float
        KELVIN: float
        LENS_RADIUS: float
        LIGHTMESH: None
        LIGHTRADIUS: float
        LIGHTSHAPEVISIBLE: bool
        MAX_BOUNCES: int
        NORMALIZE: bool
        ON: bool
        PENUMBRA_ANGLE: float
        PHOTOMETRICRADIUS: float
        PORTAL: bool
        PORTAL_MODE: int
        PRESET: int
        QUADROUNDNESS: float
        QUADX: float
        QUADY: float
        RESOLUTION: int
        SAMPLES: int
        SHADOW_COLOR: MXSWrapperBase
        SHADOW_DENSITY: float
        SHAPETYPE: int
        SOFT_EDGE: float
        SPECULAR: float
        SPOTROUNDNESS: float
        SPREAD: float
        SSS: float
        TARGDIST: float
        TARGETED: bool
        TEXMAP: None
        TRANSMISSION: float
        USECOLOR: bool
        USEKELVIN: bool
        USEPRESET: bool
        USEROPTIONS: None
        USETEXMAP: bool
        VOLUME: float
        VOLUME_SAMPLES: int
        ...
    class Arnold_Light_Decay(Modifier):
        ARNOLD_NODE: str
        ARNOLD_NODE_FAR_END: float
        ARNOLD_NODE_FAR_START: float
        ARNOLD_NODE_NEAR_END: float
        ARNOLD_NODE_NEAR_START: float
        ARNOLD_NODE_USE_FAR_ATTEN: bool
        ARNOLD_NODE_USE_NEAR_ATTEN: bool
        SHOW_FAR_ATTEN: bool
        SHOW_NEAR_ATTEN: bool
        ...
    class Arnold_Light_Gobo(Modifier):
        ARNOLD_LINK_SLIDEMAP: None
        ARNOLD_NODE: str
        ARNOLD_NODE_DENSITY: float
        ARNOLD_NODE_FILTER_MODE: int
        ARNOLD_NODE_OFFSET: MXSWrapperBase
        ARNOLD_NODE_SLIDEMAP: MXSWrapperBase
        ARNOLD_NODE_SSCALE: float
        ARNOLD_NODE_SWRAP: int
        ARNOLD_NODE_TSCALE: float
        ARNOLD_NODE_TWRAP: int
        ...
    class Arnold_N(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_P(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Procedural_Object(GeometryClass):
        ANIMANIMEND: int
        ANIMANIMSTART: int
        ANIMATED: bool
        ANIMATION_CACHE: int
        ANIMEXTEND: bool
        ANIMFRAMES: int
        ANIMLOOP: bool
        ANIMOFFSET: int
        ANIMPINGPONG: bool
        ANIMSEQUENCEEND: int
        ANIMSEQUENCESTART: int
        ANIMSPEED: float
        AUTO_INSTANCING: bool
        BBOXHI: MXSWrapperBase
        BBOXLOW: MXSWrapperBase
        BBOX_THRESHOLD: float
        NAME_SPACE: str
        OPERATOR: None
        PROCEDURAL: str
        UPAXIS: int
        USE_ANIMATION_CACHE: bool
        USE_BBOX_THRESHOLD: bool
        VIEWPORT_MODE: int
        ...
    class Arnold_RGBA(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_RGBA_Denoise(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Shape(Helper):
        ACQUIRE_MAPPING: bool
        ACQUIRE_MATERIAL: bool
        ACQUIRE_SHAPE: bool
        ADD_RANDOM_OFFSET: bool
        ANIMATED_SHAPE: bool
        FAST_SHAPE_EVALUATION: bool
        GROUP_MEMBERS: bool
        HANDLES_TO_REPORT: MXSWrapperBase
        OBJECT_AND_CHILDREN: bool
        OBJECT_ELEMENTS: bool
        RANDOM_OFFSET: int
        RANDOM_SEED: int
        RANDOM_SHAPE: bool
        REPORT_NODE_HANDLES: int
        SCALE_VALUE: float
        SET_SCALE: bool
        SHAPE_OBJECT: None
        SUBMTL_ID_OFFSET: int
        SYNC_TYPE: int
        VARIATION: float
        ...
    class Arnold_USD_Object(GeometryClass):
        ANIMATION_CACHE: int
        BBOXHI: MXSWrapperBase
        BBOXLOW: MXSWrapperBase
        BBOX_THRESHOLD: float
        DEBUG: bool
        FILENAME: str
        FRAME: float
        NAME_SPACE: str
        OBJECTPATH: str
        OPERATOR: None
        UPAXIS: int
        USE_ANIMATION_CACHE: bool
        USE_BBOX_THRESHOLD: bool
        USE_VP_ANIMATION: bool
        VIEWPORT_MODE: int
        ...
    class Arnold_Volume_Object(GeometryClass):
        ANIMANIMEND: int
        ANIMANIMSTART: int
        ANIMATED: bool
        ANIMEXTEND: bool
        ANIMFRAMES: int
        ANIMLOOP: bool
        ANIMOFFSET: int
        ANIMPINGPONG: bool
        ANIMSEQUENCEEND: int
        ANIMSEQUENCESTART: int
        ANIMSPEED: float
        BBOXAUTO: bool
        BBOXHI: MXSWrapperBase
        BBOXLOW: MXSWrapperBase
        BBOXPADDING: float
        GRIDS: str
        SHADER: None
        STEPMODE: int
        STEPSCALE: float
        STEPSIZE: float
        UPAXIS: int
        VDBFILE: str
        VELGRIDS: str
        VELOCITYOUTLIERTHRESHOLD: float
        VELOCITYSCALE: float
        ...
    class Arnold_Advanced_Map(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Albedo(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Coat(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Coat_Albedo(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Coat_Direct(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Coat_Indirect(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Denoise_Albedo(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Diffuse(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Diffuse_Albedo(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Diffuse_Direct(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Diffuse_Indirect(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Direct(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Emission(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Indirect(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Map_Override(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Metalness(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Roughness(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Shadow_Matte(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Sheen(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Sheen_Albedo(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Sheen_Direct(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Sheen_Indirect(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Specular(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Sss(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Sss_Albedo(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Sss_Direct(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Sss_Indirect(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Arnold_Volume_Z(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        MAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        PARAMETER: str
        SHADERS: str
        TARGETMAPSLOTNAME: str
        ...
    class Array(Value):
        ...
    class ArrayParameter(Value):
        ...
    class ArrowHelper(Helper):
        COLOR: MXSWrapperBase
        ICONSIZE: float
        ...
    class AsciiExp(ExporterPlugin):
        ...
    class AssetLibraryLauncher(GlobalUtilityPlugin):
        ...
    class AssetManager(Interface):
        ...
    class Asset_Library_Launcher(GlobalUtilityPlugin):
        ...
    class AssignConstraintSelection(MAXScriptFunction):
        ...
    class AssignControllerSelection(MAXScriptFunction):
        ...
    class AssignNewName(Primitive):
        ...
    class AssignVertexColors(Interface):
        ...
    class Assign_Vertex_Colors(UtilityPlugin):
        ...
    class Atmosphere(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class AtmosphericClass(Value):
        ...
    class AttachObjects(Primitive):
        ...
    class Attachment(PositionController):
        ALIGN: bool
        MANUPDATE: bool
        NODE: None
        ...
    class AttributeDef(Value):
        ...
    class AudioClip(Helper):
        ...
    class AudioFile(SoundClass):
        ...
    class AudioFloat(FloatController):
        ...
    class AudioPoint3(Point3Controller):
        ...
    class AudioPosition(PositionController):
        ...
    class AudioRotation(RotationController):
        ...
    class AudioScale(ScaleController):
        ...
    class AutoCADImport(ImporterPlugin):
        ...
    class AutoCam(GlobalUtilityPlugin):
        ...
    class AutoTangentMan(Interface):
        ...
    class Auto_Secondary_Element(ReferenceTarget):
        ALPHA: int
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        APPLYLIGHTS: bool
        APPLYNOISE: bool
        AXIS: float
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        CIRCULARCOLORMIX: float
        CIRCULARMAP: None
        CIRCULARMTL: None
        COLORRADIUS1: float
        COLORRADIUS2: float
        COLORRADIUS3: float
        COLORRADIUS4: float
        COLORSOURCE: float
        EFFECTSID: int
        ELEMENTNAME: str
        FILTERALL: bool
        FILTERBRIGHTNESS: bool
        FILTEREDGE: bool
        FILTERHUE: bool
        FILTERPERIMETER: bool
        FILTERPERIMETERALPHA: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        INTENSITY: float
        MAXSIZE: float
        MINSIZE: float
        NOISEMAP: None
        OBJECTID: int
        OCCLUSION: float
        ON: bool
        PRESETS: int
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        QUADRANT4COLOR: MXSWrapperBase
        QUANTITY: int
        RADIALCOLOR1: MXSWrapperBase
        RADIALCOLOR2: MXSWrapperBase
        RADIALCOLOR3: MXSWrapperBase
        RADIALCOLOR4: MXSWrapperBase
        RADIALDENSITY: None
        RADIALMAP: None
        RADIALMTL: None
        RADIALSIZEMAP: None
        SIDES: int
        SOURCEALPHA: bool
        SOURCEEFFECTSID: bool
        SOURCEOBJECTID: bool
        SOURCESURFACENORMAL: bool
        SOURCEUNCLAMPEDCOLOR: bool
        SOURCEWHOLE: bool
        SOURCEZBUFFER: bool
        SQUEEZE: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        USECIRCULARMAP: bool
        USECIRCULARMTL: bool
        USERADIALDENSITY: bool
        USERADIALMAP: bool
        USERADIALMTL: bool
        USERADIALSIZEMAP: bool
        ZHI: float
        ZLO: float
        ...
    class Autodesk360(Interface):
        ...
    class AutodeskMap(TextureMap):
        ...
    class AutodeskMaterial(Material):
        AMBIENT_OCCLUSION_ENABLE: bool
        AMBIENT_OCCLUSION_MAX_DISTANCE: float
        AMBIENT_OCCLUSION_SAMPLES: int
        AMBIENT_OCCLUSION_USE_COLOR_FROM_OTHER_MATERIALS: bool
        BUMP_AMOUNT: float
        BUMP_AMOUNT_MAP: None
        BUMP_AMOUNT_OPTION: int
        BUMP_ENABLE: bool
        BUMP_IMAGE: None
        CUTOUTS_ENABLE: bool
        CUTOUTS_IMAGE: None
        GENERIC_COLOR: MXSWrapperBase
        GENERIC_COLOR_OPTION: int
        GENERIC_GLOSSINESS: float
        GENERIC_GLOSSINESS_MAP: None
        GENERIC_GLOSSINESS_OPTION: int
        GENERIC_HIGHLIGHTS: bool
        GENERIC_IMAGE: None
        GENERIC_IMAGE_FADE: float
        OVERRIDE_REFRACTION_DEPTH_ENABLE: bool
        OVERRIDE_REFRACTION_DEPTH_REFRACTION_MAX_TRACE_DEPTH: int
        PERFORMANCE_TUNING_REFLECTION_GLOSSY_SAMPLES: int
        PERFORMANCE_TUNING_REFLECTION_MAX_TRACE_DEPTH: int
        PERFORMANCE_TUNING_REFRACTION_GLOSSY_SAMPLES: int
        REFLECTIVITY_DIRECT: float
        REFLECTIVITY_DIRECT_MAP: None
        REFLECTIVITY_DIRECT_OPTION: int
        REFLECTIVITY_ENABLE: bool
        REFLECTIVITY_OBLIQUE: float
        REFLECTIVITY_OBLIQUE_MAP: None
        REFLECTIVITY_OBLIQUE_OPTION: int
        ROUND_CORNERS_BLEND_WITH_OTHER_MATERIALS: bool
        ROUND_CORNERS_ENABLE: bool
        ROUND_CORNERS_SOURCE: float
        ROUND_CORNERS_SOURCE_MAP: None
        ROUND_CORNERS_SOURCE_OPTION: int
        SELF_ILLUMINATION_COLOR_TEMPERATURE: float
        SELF_ILLUMINATION_ENABLE: bool
        SELF_ILLUMINATION_FILTER_COLOR: MXSWrapperBase
        SELF_ILLUMINATION_FILTER_COLOR_MAP: None
        SELF_ILLUMINATION_FILTER_COLOR_OPTION: int
        SELF_ILLUMINATION_LUMINANCE: float
        TRANSPARENCY_AMOUNT: float
        TRANSPARENCY_ENABLE: bool
        TRANSPARENCY_IMAGE: None
        TRANSPARENCY_IMAGE_FADE: float
        TRANSPARENCY_REFRACTION: float
        TRANSPARENCY_TRANSLUCENCY: float
        TRANSPARENCY_TRANSLUCENCY_MAP: None
        TRANSPARENCY_TRANSLUCENCY_OPTION: int
        ...
    class AutodeskMaterialManager(Interface):
        ...
    class Autodesk_Map(TextureMap):
        ...
    class Autodesk_Material(Material):
        AMBIENT_OCCLUSION_ENABLE: bool
        AMBIENT_OCCLUSION_MAX_DISTANCE: float
        AMBIENT_OCCLUSION_SAMPLES: int
        AMBIENT_OCCLUSION_USE_COLOR_FROM_OTHER_MATERIALS: bool
        BUMP_AMOUNT: float
        BUMP_AMOUNT_MAP: None
        BUMP_AMOUNT_OPTION: int
        BUMP_ENABLE: bool
        BUMP_IMAGE: None
        CUTOUTS_ENABLE: bool
        CUTOUTS_IMAGE: None
        GENERIC_COLOR: MXSWrapperBase
        GENERIC_COLOR_OPTION: int
        GENERIC_GLOSSINESS: float
        GENERIC_GLOSSINESS_MAP: None
        GENERIC_GLOSSINESS_OPTION: int
        GENERIC_HIGHLIGHTS: bool
        GENERIC_IMAGE: None
        GENERIC_IMAGE_FADE: float
        OVERRIDE_REFRACTION_DEPTH_ENABLE: bool
        OVERRIDE_REFRACTION_DEPTH_REFRACTION_MAX_TRACE_DEPTH: int
        PERFORMANCE_TUNING_REFLECTION_GLOSSY_SAMPLES: int
        PERFORMANCE_TUNING_REFLECTION_MAX_TRACE_DEPTH: int
        PERFORMANCE_TUNING_REFRACTION_GLOSSY_SAMPLES: int
        REFLECTIVITY_DIRECT: float
        REFLECTIVITY_DIRECT_MAP: None
        REFLECTIVITY_DIRECT_OPTION: int
        REFLECTIVITY_ENABLE: bool
        REFLECTIVITY_OBLIQUE: float
        REFLECTIVITY_OBLIQUE_MAP: None
        REFLECTIVITY_OBLIQUE_OPTION: int
        ROUND_CORNERS_BLEND_WITH_OTHER_MATERIALS: bool
        ROUND_CORNERS_ENABLE: bool
        ROUND_CORNERS_SOURCE: float
        ROUND_CORNERS_SOURCE_MAP: None
        ROUND_CORNERS_SOURCE_OPTION: int
        SELF_ILLUMINATION_COLOR_TEMPERATURE: float
        SELF_ILLUMINATION_ENABLE: bool
        SELF_ILLUMINATION_FILTER_COLOR: MXSWrapperBase
        SELF_ILLUMINATION_FILTER_COLOR_MAP: None
        SELF_ILLUMINATION_FILTER_COLOR_OPTION: int
        SELF_ILLUMINATION_LUMINANCE: float
        TRANSPARENCY_AMOUNT: float
        TRANSPARENCY_ENABLE: bool
        TRANSPARENCY_IMAGE: None
        TRANSPARENCY_IMAGE_FADE: float
        TRANSPARENCY_REFRACTION: float
        TRANSPARENCY_TRANSLUCENCY: float
        TRANSPARENCY_TRANSLUCENCY_MAP: None
        TRANSPARENCY_TRANSLUCENCY_OPTION: int
        ...
    class AutomaticAdaptiveExposureControl(ToneOperator):
        ACTIVE: bool
        BRIGHTESS: float
        CHROMATICADAPTATION: bool
        COLORDIFFERENTIATION: bool
        CONTRAST: float
        EXPOSUREVALUE: float
        PHYSICALSCALE: float
        PROCESSBG: bool
        WHITECOLOR: MXSWrapperBase
        ...
    class AutomaticLinearExposureControl(ToneOperator):
        ACTIVE: bool
        BRIGHTESS: float
        CHROMATICADAPTATION: bool
        COLORDIFFERENTIATION: bool
        CONTRAST: float
        EXPOSUREVALUE: float
        PHYSICALSCALE: float
        PROCESSBG: bool
        WHITECOLOR: MXSWrapperBase
        ...
    class Automatic_Exposure_Control(ToneOperator):
        ACTIVE: bool
        BRIGHTESS: float
        CHROMATICADAPTATION: bool
        COLORDIFFERENTIATION: bool
        CONTRAST: float
        EXPOSUREVALUE: float
        PHYSICALSCALE: float
        PROCESSBG: bool
        WHITECOLOR: MXSWrapperBase
        ...
    class AverageSelVertCenter(Primitive):
        ...
    class AverageSelVertNormal(Primitive):
        ...
    class AvoidBehavior(ReferenceTarget):
        BRAKEPRESSURE: float
        DETOURANGLE: float
        DISPLAYFORCE: bool
        FORCECOLOR: MXSWrapperBase
        HARDRADIUS: float
        LOOKAHEAD: int
        NAME: str
        OBSTACLES: MXSWrapperBase
        REPELFALLOFF: float
        REPELRADIUS: float
        REPELSTRENGTH: float
        SHOWHARDRADIUS: bool
        SHOWLOOKAHEAD: bool
        SHOWPOTENTIALCOLS: bool
        SHOWREPELACTIVITY: bool
        SHOWREPELRADIUS: bool
        VFIELDFALLOFF: float
        VFIELDSTRENGTH: float
        ...
    class Avoid_Behavior(ReferenceTarget):
        BRAKEPRESSURE: float
        DETOURANGLE: float
        DISPLAYFORCE: bool
        FORCECOLOR: MXSWrapperBase
        HARDRADIUS: float
        LOOKAHEAD: int
        NAME: str
        OBSTACLES: MXSWrapperBase
        REPELFALLOFF: float
        REPELRADIUS: float
        REPELSTRENGTH: float
        SHOWHARDRADIUS: bool
        SHOWLOOKAHEAD: bool
        SHOWPOTENTIALCOLS: bool
        SHOWREPELACTIVITY: bool
        SHOWREPELRADIUS: bool
        VFIELDFALLOFF: float
        VFIELDSTRENGTH: float
        ...
    class Awning(GeometryClass):
        DEPTH: float
        FRAME_THICKNESS: float
        GENERATE_MAPPING_COORDS: bool
        GLAZING_THICKNESS: float
        HEIGHT: float
        HORIZONTAL_FRAME_WIDTH: float
        NUMBER_OF_PANELS: int
        PERCENT_OPEN: int
        RAIL_WIDTH: float
        VERTICAL_FRAME_WIDTH: float
        WIDTH: float
        ...
    class AxisDisplayClass(MAXWrapper):
        ...
    class AxisHelperObj(Helper):
        ...
    class AxisTripodLocked(Primitive):
        ...
    class Axis_Helper(Helper):
        ...
    class BMP(BitmapIO):
        ...
    class Background(Helper):
        ...
    class BackgroundFragment(GraphicsFragmentPlugin):
        ...
    class BackgroundRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class BakeElement(MAXWrapper):
        ...
    class BakeSetupController(MAXScriptFunction):
        ...
    class BakeToTexture(UtilityPlugin):
        ...
    class BakeToTextureData(CtrlUserDataTypeClass):
        ...
    class BakeUnsetupController(MAXScriptFunction):
        ...
    class Barycentric_Morph_Controller(MorphController):
        ...
    class Base_Layer(MAXWrapper):
        ...
    class Base_LayerBase_Layer(Base_Layer):
        ...
    class BatchProOptimizer(Interface):
        ...
    class Batch_ProOptimizer(UtilityPlugin):
        ...
    class Batch_Render_Manager(UtilityPlugin):
        ...
    class Batch_Render_ManagerCtrlUserDataTypeClass(CtrlUserDataTypeClass):
        ...
    class Beauty(RenderElement):
        ...
    class Bend(Modifier):
        BENDANGLE: float
        BENDAXIS: int
        BENDDIR: float
        BENDFROM: float
        BENDTO: float
        FROMTO: bool
        ...
    class BendMod(Modifier):
        BENDANGLE: float
        BENDAXIS: int
        BENDDIR: float
        BENDFROM: float
        BENDTO: float
        FROMTO: bool
        ...
    class BendModWSM(SpacewarpObject):
        ...
    class Bevel(Modifier):
        CAP_BOTTOM: int
        CAP_TOP: int
        CAP_TYPE: int
        KEEP_LINES_FROM_CROSSING: int
        LEVEL_1_HEIGHT: float
        LEVEL_1_OUTLINE: float
        LEVEL_2_HEIGHT: float
        LEVEL_2_OUTLINE: float
        LEVEL_3_HEIGHT: float
        LEVEL_3_OUTLINE: float
        PRODUCE_MAPPING_COORDS: int
        SEGMENTS: int
        SEPARATION_BETWEEN_LINES: float
        SIDE_TYPE: int
        SMOOTH_LEVELS: int
        STARTING_OUTLINE: float
        USE_LEVEL_2: int
        USE_LEVEL_3: int
        ...
    class BevelProfileMod(Modifier):
        BEVELDEPTH: float
        BEVELOFFSET: float
        BEVELOPTIMIZE: bool
        BEVELPUSH: float
        BEVELSTEPS: int
        BEVELWIDTH: float
        CAPEND: int
        CAPENDCONSTRAIN: bool
        CAPSTART: int
        CAPSTARTCONSTRAIN: bool
        CAPTYPE: int
        CAP_BOTTOM: bool
        CAP_TOP: bool
        CAP_TYPE: int
        CLASSICORIMPROVED: int
        ENDBEVELMATERIAL: int
        ENDCAPMATERIAL: int
        EXTRUDEAMOUNT: float
        EXTRUDESEGMENTS: int
        KEEP_LINES_FROM_CROSSING: bool
        PRODUCE_MAPPING_COORDS: bool
        SEPARATION_BETWEEN_LINES: float
        SIDEMATERIAL: int
        STARTBEVELMATERIAL: int
        STARTCAPMATERIAL: int
        USEBEVELWIDTH: bool
        ...
    class BevelProfileUtilityInterface(UtilityPlugin):
        ...
    class Bevel_Profile(Modifier):
        BEVELDEPTH: float
        BEVELOFFSET: float
        BEVELOPTIMIZE: bool
        BEVELPUSH: float
        BEVELSTEPS: int
        BEVELWIDTH: float
        CAPEND: int
        CAPENDCONSTRAIN: bool
        CAPSTART: int
        CAPSTARTCONSTRAIN: bool
        CAPTYPE: int
        CAP_BOTTOM: bool
        CAP_TOP: bool
        CAP_TYPE: int
        CLASSICORIMPROVED: int
        ENDBEVELMATERIAL: int
        ENDCAPMATERIAL: int
        EXTRUDEAMOUNT: float
        EXTRUDESEGMENTS: int
        KEEP_LINES_FROM_CROSSING: bool
        PRODUCE_MAPPING_COORDS: bool
        SEPARATION_BETWEEN_LINES: float
        SIDEMATERIAL: int
        STARTBEVELMATERIAL: int
        STARTCAPMATERIAL: int
        USEBEVELWIDTH: bool
        ...
    class BezierFontLoaderClass(MAXWrapperNonRefTarg):
        ...
    class BezierShapeValue(Value):
        ...
    class Bezier_Point2(Point2Controller):
        ...
    class BiFold(GeometryClass):
        BEVEL_ANGLE: float
        BOTTOM_RAIL: float
        CREATE_FRAME: bool
        DEPTH: float
        DOOR_OFFSET: float
        DOUBLE_DOORS: int
        FLIP_HINGE: bool
        FLIP_SWING: bool
        FRAME_DEPTH: float
        FRAME_WIDTH: float
        GENERATE_MAPPING_COORDS: bool
        GLASS_THICKNESS: float
        HEIGHT: float
        LEAF_THICKNESS: float
        MUNTIN: float
        NUMBER_OF_PANELS_HORIZONTALLY: int
        NUMBER_OF_PANELS_VERTICALLY: int
        OPEN: float
        PANEL_MIDDLE_THICKNESS: float
        PANEL_THICKNESS_1: float
        PANEL_THICKNESS_2: float
        PANEL_TYPE: int
        PANEL_WIDTH_1: float
        PANEL_WIDTH_2: float
        STILES_TOP_RAIL: float
        WIDTH: float
        ...
    class BigMatrix(Value):
        ...
    class BigMatrixRowArray(Value):
        ...
    class Billboard(Helper):
        ...
    class BinStream(Value):
        ...
    class BipAnalyzer(Interface):
        ...
    class BipFilter(Interface):
        ...
    class BipFixer(Interface):
        ...
    class BipSlave_Control(Matrix3Controller):
        ...
    class BipWorkBench(Interface):
        ...
    class BipedCopy(Value):
        ...
    class BipedFSKey(Value):
        ...
    class BipedGeneric(Value):
        ...
    class BipedKey(Value):
        ...
    class Biped_Object(GeometryClass):
        ...
    class Biped_SubAnim(FloatController):
        KEEP: bool
        PERFRAME: bool
        POSACTIVE: bool
        ROTACTIVE: bool
        SCALEACTIVE: bool
        ...
    class Birth(Helper):
        AMOUNT: int
        EMIT_START: int
        EMIT_STOP: int
        RATE: float
        SUBFRAME_SAMPLING: bool
        TYPE: int
        ...
    class BirthGrid(Helper):
        COLOR_TYPE: bool
        COMPACT_VERTICAL_SIZE: bool
        DELETE_INTERNAL_PARTICLES: bool
        EMIT_TIME: int
        EXTERNAL_LAYERS: int
        GRID_BASE_TYPE: int
        GRID_HEIGHT: float
        GRID_LENGTH: float
        GRID_OFFSET: float
        GRID_SIZE: float
        GRID_WIDTH: float
        ICON_HEIGHT: float
        ICON_LENGTH: float
        ICON_WIDTH: float
        INTERACTIVE_UPDATE: bool
        RANDOM_SEED: int
        REFERENCE_GEOMETRY: None
        RESTRICT_BY_MESH_VOLUME: bool
        SAVE_GRID_DATA_WITH_FILE: bool
        UPPER_LIMIT: int
        USE_ALTERNATING_LATERAL_OFFSET: bool
        USE_NON_UNIFORM_GRID: bool
        USE_RANDOM_VERTICAL_OFFSET: bool
        ...
    class BirthGroup(Helper):
        ACQUIRE_MAPPING: bool
        ACQUIRE_MATERIAL: bool
        ACQUIRE_SHAPES: bool
        EMIT_TIME: int
        HANDLES_TO_REPORT: MXSWrapperBase
        PARTICLE_OBJECTS: MXSWrapperBase
        REPORT_NODE_HANDLES: int
        SPLIT_BY_CHILDREN: bool
        SPLIT_BY_ELEMENTS: bool
        SPLIT_BY_GROUP_MEMBERS: bool
        SUBMTL_ID_OFFSET: int
        ...
    class BirthStream(Helper):
        COLOR_TYPE: bool
        DELAY_BIRTH_IF_OVERLAP: bool
        EMIT_START: int
        EMIT_STOP: int
        ICON_LENGTH: float
        ICON_TYPE: int
        ICON_WIDTH: float
        INHERIT_ICON_MOVEMENT: bool
        MAX_ATTEMPTS: int
        MULTIPLIER: float
        RANDOM_SEED: int
        RATE: float
        SEPARATION: float
        SPEED: float
        ...
    class BirthTexture(Helper):
        ADJUST_SEPARATION_BY_SCALE_FACTOR: bool
        AMOUNT_LIMIT: int
        ANIMATED_SHAPE: bool
        BLACK_SCALE: float
        COLOR_COORDINATED: bool
        DATA_START: int
        DATA_STOP: int
        DELAY_VARIATION: int
        DISPLAY_TYPE: int
        EMISSION_BY: int
        EMISSION_RGB_CHANNELS: MXSWrapperBase
        EMISSION_TEXTURE_SUBMATERIAL_ID: int
        EMISSION_TYPE: int
        EMITTER_OBJECTS: MXSWrapperBase
        EMIT_START: int
        EMIT_STOP: int
        FAST_APPROXIMATE_SEPARATION: bool
        ICON_SIZE: float
        LATENCY: int
        LOCK_ON_EMITTER: bool
        MAXIMUM_AMOUNT: int
        MAXIMUM_RATE: float
        PRECISION: int
        RANDOM_SEED: int
        SCALE_FACTOR_SUBMTL_ID: int
        SCALE_TYPE: int
        SEPARATE_DISTANCE: float
        SHOW_ONLY_WHEN_SELECTED: bool
        SHOW_PARTICLES: bool
        SUBDIVISION_LENGTH: float
        SURFACE_NORMAL_OFFSET: bool
        SURFACE_OFFSET_MAXIMUM: float
        SURFACE_OFFSET_MINIMUM: float
        USE_LATENCY: bool
        USE_SUBDIVISION: bool
        WHITENESS: float
        WHITE_SCALE: float
        ...
    class Birth_File(Helper):
        COLOR_MAP_CHANNEL: int
        DATAFILE_THISFRAME: None
        EMIT_START: int
        EXTRAPOLATION_TYPE: int
        FILETIME: int
        FILE_CHANNEL_MASK: int
        FILE_END: int
        FILE_NB_FRAMES: int
        FILE_RATE: float
        FILE_START: int
        NB_PARTICLES_THISFRAME: int
        OPACITY_MAP_CHANNEL: int
        ORIENTATION_UP_VECTOR: int
        PARTICLE_FILE: str
        PARTICLE_FILE_VALID: bool
        RANGE_END: int
        RANGE_START: int
        RANGE_TYPE: int
        SPEED_FACTOR: float
        USE_COLOR_CHANNEL: bool
        USE_OPACITY_CHANNEL: bool
        USE_ORIENTATION_CHANNEL: bool
        USE_POSITION_CHANNEL: bool
        USE_SCALE_CHANNEL: bool
        USE_SPEED_CHANNEL: bool
        ...
    class Birth_Group(Helper):
        ACQUIRE_MAPPING: bool
        ACQUIRE_MATERIAL: bool
        ACQUIRE_SHAPES: bool
        EMIT_TIME: int
        HANDLES_TO_REPORT: MXSWrapperBase
        PARTICLE_OBJECTS: MXSWrapperBase
        REPORT_NODE_HANDLES: int
        SPLIT_BY_CHILDREN: bool
        SPLIT_BY_ELEMENTS: bool
        SPLIT_BY_GROUP_MEMBERS: bool
        SUBMTL_ID_OFFSET: int
        ...
    class Birth_Paint(Helper):
        ACQUIRE_SELECTION: bool
        DURATION: int
        EMIT_START: int
        EMIT_STOP: int
        EMIT_TYPE: int
        LOCK_POSITION: bool
        LOCK_ROTATION: bool
        PARTICLE_PAINT_HELPER: None
        SELECTION_TYPE: int
        SUBFRAME_SAMPLING: bool
        ...
    class Birth_Script(Helper):
        EMIT_START: int
        PROCEED_SCRIPT: str
        RANDOM_SEED: int
        ...
    class Birth_Texture(Helper):
        ADJUST_SEPARATION_BY_SCALE_FACTOR: bool
        AMOUNT_LIMIT: int
        ANIMATED_SHAPE: bool
        BLACK_SCALE: float
        COLOR_COORDINATED: bool
        DATA_START: int
        DATA_STOP: int
        DELAY_VARIATION: int
        DISPLAY_TYPE: int
        EMISSION_BY: int
        EMISSION_RGB_CHANNELS: MXSWrapperBase
        EMISSION_TEXTURE_SUBMATERIAL_ID: int
        EMISSION_TYPE: int
        EMITTER_OBJECTS: MXSWrapperBase
        EMIT_START: int
        EMIT_STOP: int
        FAST_APPROXIMATE_SEPARATION: bool
        ICON_SIZE: float
        LATENCY: int
        LOCK_ON_EMITTER: bool
        MAXIMUM_AMOUNT: int
        MAXIMUM_RATE: float
        PRECISION: int
        RANDOM_SEED: int
        SCALE_FACTOR_SUBMTL_ID: int
        SCALE_TYPE: int
        SEPARATE_DISTANCE: float
        SHOW_ONLY_WHEN_SELECTED: bool
        SHOW_PARTICLES: bool
        SUBDIVISION_LENGTH: float
        SURFACE_NORMAL_OFFSET: bool
        SURFACE_OFFSET_MAXIMUM: float
        SURFACE_OFFSET_MINIMUM: float
        USE_LATENCY: bool
        USE_SUBDIVISION: bool
        WHITENESS: float
        WHITE_SCALE: float
        ...
    class BitArray(Value):
        ...
    class BitmapControl(RolloutControl):
        ...
    class BitmapFilterClass(MAXWrapperNonRefTarg):
        ...
    class BitmapIO(MAXWrapperNonRefTarg):
        ...
    class BitmapLayerManager(Interface):
        ...
    class BitmapPagerData(UserDataTypeClass):
        ...
    class BitmapProxyConfigDialog(UserDataTypeClass):
        ...
    class BitmapProxyManagerImpLatch(UserDataTypeClass):
        ...
    class BitmapProxyManagerImp_Latch(UserDataTypeClass):
        ...
    class BitmapProxyMgr(Interface):
        ...
    class BitmapProxyTools(Interface):
        ...
    class BitmapProxy_Config_Dialog(UserDataTypeClass):
        ...
    class BitmapStorageClass(MAXWrapperNonRefTarg):
        ...
    class Bitmap_Photometric_Paths(UtilityPlugin):
        ...
    class Bitmaptexture(TextureMap):
        ALPHASOURCE: int
        APPLY: bool
        BITMAP: None
        CLIPH: float
        CLIPU: float
        CLIPV: float
        CLIPW: float
        COORDS: MXSWrapperBase
        CROPPLACE: int
        ENDCONDITION: int
        FILENAME: str
        FILTERING: int
        JITTER: float
        MONOOUTPUT: int
        OUTPUT: MXSWrapperBase
        PLAYBACKRATE: float
        PREMULTALPHA: bool
        RGBOUTPUT: int
        STARTTIME: MXSWrapperBase
        TIETIMETOMATIDS: bool
        USEJITTER: bool
        ...
    class Blackman(Filter):
        ...
    class Blend(Material):
        INTERACTIVE: int
        LOWER: float
        MAP1: MXSWrapperBase
        MAP1ENABLED: bool
        MAP2: MXSWrapperBase
        MAP2ENABLED: bool
        MASK: None
        MASKENABLED: bool
        MIXAMOUNT: float
        UPPER: float
        USECURVE: bool
        ...
    class BlendFragment(GraphicsFragmentPlugin):
        ...
    class BlendMap(BakeElement):
        AMBIENTON: bool
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        DIFFUSEON: bool
        ELEMENTNAME: str
        EMISSIONON: bool
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        LIGHTINGON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        REFLECTIONON: bool
        REFRACTIONON: bool
        SHADOWSON: bool
        SPECULARON: bool
        TARGETMAPSLOTNAME: str
        ...
    class BlendRenderElement(RenderElement):
        AMBIENTON: bool
        ATMOSPHEREON: bool
        BITMAP: None
        DIFFUSEON: bool
        ELEMENTNAME: str
        EMISSIONON: bool
        ENABLED: bool
        FILTERON: bool
        INKON: bool
        PAINTON: bool
        REFLECTIONON: bool
        REFRACTIONON: bool
        SHADOWON: bool
        SPECULARON: bool
        ...
    class BlendedBoxMap(TextureMap):
        BLEND: float
        BLENDMAPSTRENGTH: float
        COLORS: MXSWrapperBase
        COORDS: MXSWrapperBase
        CUBE: bool
        CUBEMODE: int
        CUBENODE: None
        CUBESIZE: float
        FORSEED: int
        LOCKFRAME: int
        LOCKTOFRAME: bool
        MAPENABLED: MXSWrapperBase
        MAPSCALE: float
        MODE: int
        NODE: None
        POSLOCK: bool
        POSU2: float
        POSU: float
        POSV2: float
        POSV: float
        RANDX: bool
        RANDY: bool
        RANDZ: bool
        RENDERRESOLUTION: int
        ROTA2: float
        ROTA: float
        ROTB2: float
        ROTB: float
        ROTC2: float
        ROTC: float
        ROTLOCK: bool
        SCALELOCK: bool
        SCALEU2: float
        SCALEU: float
        SCALEV2: float
        SCALEV: float
        SEED: int
        TEX: MXSWrapperBase
        TEXTURESPACE: int
        USERANDOM: bool
        ...
    class Blendfilter(Filter):
        BLEND: float
        ...
    class Blinn(Shader):
        ...
    class Blinn2(Shader):
        ...
    class BlitFragment(GraphicsFragmentPlugin):
        ...
    class Blizzard(GeometryClass):
        BIRTH_RATE: int
        BUBBLE_PHASE_VARIATION: int
        DIE__X_FRAMES_AFTER_COLLISION: MXSWrapperBase
        DIE__X_FRAMES_AFTER_COLLISION_VARIATION: float
        DISPLAY_UNTIL: MXSWrapperBase
        EMITTERHIDDEN: bool
        EMITTER_LENGTH: float
        EMITTER_START: MXSWrapperBase
        EMITTER_STOP: MXSWrapperBase
        EMITTER_WIDTH: float
        FADE_TIME: MXSWrapperBase
        GROWTH_TIME: MXSWrapperBase
        INSTANCEFRAMEOFFSET: int
        INSTANCEKEYOFFSETTYPE: int
        INSTANCESUBTREE: bool
        INSTANCINGOBJECT: None
        INTERPARTICLE_COLLISIONS_ON: int
        INTERPARTICLE_COLLISION_BOUNCE: float
        INTERPARTICLE_COLLISION_BOUNCE_VARIATION: float
        INTERPARTICLE_COLLISION_STEPS: int
        LIFE: MXSWrapperBase
        LIFESPANVALUEQUEUE: MXSWrapperBase
        LIFE_VARIATION: MXSWrapperBase
        MAPPINGTYPE: int
        MAPPING_DISTANCE_BASE: float
        MAPPING_TIME_BASE: MXSWrapperBase
        MATERIALSOURCE: int
        METABALLAUTOCOARSNESS: bool
        METABALLRENDERCOARSNESS: float
        METABALLVIEWCOARSNESS: float
        METAPARTICLE_TENSION: float
        METAPARTICLE_TENSION_VARIATION: float
        MOTIONINFLUENCE: float
        MOTIONMULTIPLIER: float
        MOTIONVARIATION: float
        OBJECTMUTATIONQUEUE: MXSWrapperBase
        PARTICLETYPE: int
        QUANTITYMETHOD: int
        SEED: int
        SIZE: float
        SIZE_VARIATION: float
        SPAWNINHERITVELOCITY: bool
        SPAWNSCALEFIXED: bool
        SPAWNSCALETYPE: int
        SPAWNSPEEDFIXED: bool
        SPAWNSPEEDTYPE: int
        SPAWNTYPE: int
        SPAWN_AFFECTS: int
        SPAWN_DIRECTION_CHAOS: float
        SPAWN_MULTIPLIER_VARIATION: float
        SPAWN_SCALE_CHAOS: float
        SPAWN_SPEED_CHAOS: float
        SPEED: float
        SPEED_VARIATION: float
        SPINAXISTYPE: int
        SPIN_AXIS_VARIATION: float
        SPIN_PHASE: float
        SPIN_PHASE_VARIATION: float
        SPIN_TIME: MXSWrapperBase
        SPIN_TIME_VARIATION: float
        STANDARDPARTICLE: int
        SUBSAMPLECREATIONTIME: bool
        SUBSAMPLEEMITTERROTATION: bool
        SUBSAMPLEEMITTERTRANSLATION: bool
        TOTAL_NUMBER: int
        TUMBLE: float
        TUMBLE_RATE: float
        VIEWPERCENT: float
        VIEWTYPE: int
        X_SPIN_VECTOR: float
        Y_SPIN_VECTOR: float
        Z_SPIN_VECTOR: float
        ...
    class BlobMesh(GeometryClass):
        LARGEDATASETOPTIMIZATION: bool
        MINSIZE: float
        NODELIST: MXSWrapperBase
        OFFINVIEW: bool
        PFEVENTLIST: MXSWrapperBase
        RELATIVECOARSENESS: bool
        RENDERCOARSENESS: float
        SIZE: float
        TENSION: float
        USEALLPFEVENTS: bool
        USESOFTSELECTION: bool
        VIEWPORTCOARSENESS: float
        ...
    class Block(FloatController):
        ...
    class BlockInstanceFilter(ReferenceMaker):
        ...
    class BlockMgrWrapper(FloatController):
        ...
    class Block_Control(MasterBlockController):
        ...
    class Block_Manager_Wrapper(FloatController):
        ...
    class BloomAdsk(GraphicsFragmentPlugin):
        ...
    class BlurWind(Helper):
        ...
    class Body_Cutter(GeometryClass):
        AUTOEXTRACT: bool
        CUTTEROUTSIDE: bool
        GROUPRESULTS: bool
        STOCKINSIDE: bool
        STOCKOUTSIDE: bool
        ...
    class Body_Join(GeometryClass):
        BREPOPERATION: int
        MAKEINTOSOLID: bool
        TOBREPOBJECTHELP: bool
        ...
    class Body_Object(GeometryClass):
        ...
    class Body_Utility(GeometryClass):
        APPROXIMATEARCFAO: bool
        BLENDSTRENGTHFAO: float
        CLEANMESHVDS: bool
        CONSTANTDISTANCEFAO: bool
        CORNEREXTENSIONFAO: bool
        CURVATUREDENSITYSA: float
        CURVATURESCALESA: float
        CURVECURVATURETYPESA: int
        DISPLAYCONTROLMESHSA: bool
        DISPLAYCONTROLPOINTSSA: bool
        DISPLAYCURVECURVATURESA: bool
        DISPLAYRADIOVDS: int
        DISPLAYSURFACECURVATURESA: bool
        DISPLAYSURFACEKNOTSVDS: bool
        EDGEAPPROXANGLERA: float
        EDGEAPPROXANGLEVDS: float
        EDGECHORDHEIGHTVDS: float
        EDGECHORDRA: float
        EXTRTOBREPNQ: bool
        EXTRTOCURVENQ: bool
        EXTRTONURBSNQ: bool
        FACEAPPROXANGLERA: float
        FACEAPPROXANGLEVDS: float
        FACECHORDHEIGHTVDS: float
        FACECHORDRA: float
        FAO_NOT_USED1: bool
        FAO_NOT_USED2: bool
        FAO_NOT_USED3: bool
        FAO_NOT_USED4: bool
        FASTEDITOP: bool
        FILLETALLEDGESFAO: bool
        FILLETRADIUSFAO: float
        FIRSTORENDEDGESFAO: bool
        HIGHQUALITYRA: bool
        HIGHQUALITYVDS: bool
        ISOANGLEDS: float
        ISOCHORDHEIGHTVDS: float
        LINEARCROSSSECTIONFAO: bool
        LOWQUALITYRA: bool
        LOWQUALITYVDS: bool
        MAXEDGELENGTHPCTVDS: float
        MAXEDGERA: float
        MEDIUMQUALITYRA: bool
        MEDIUMQUALITYVDS: bool
        NQ_NOT_USED1: bool
        NQ_NOT_USED2: bool
        NQ_NOT_USED3: bool
        NQ_NOT_USED4: bool
        NQ_NOT_USED5: bool
        OFFSETRADIUSFAO: float
        OP_NOT_USED1: int
        OP_NOT_USED2: bool
        OP_NOT_USED3: bool
        OP_NOT_USED4: bool
        RENDERRADIORA: int
        RENDERVIEWPORTMESHRA: bool
        SAVEBREPSOP: bool
        SAVERENDERMESHRA: bool
        SECONDORSIDEEDGESFAO: bool
        SECTIONTYPEFAO: int
        SHELLENDFACEFAO: bool
        SHELLRADIOFAO: int
        SHELLSTARTFACEFAO: bool
        SHOWALLOPERANDSOP: bool
        SHOWRESULTOP: bool
        SHOWSELECTEDOPERANDSOP: bool
        SMOOTHINGPASSESVDS: float
        STDDEVMAXRANGESA: float
        STDDEVMINRANGESA: float
        STDDEVMULTIPLESSA: float
        SUBDMESHVDS: bool
        SURFACECURVATURETYPESA: int
        SURFANALYSISQUICKHELPSA: bool
        THIRDORSTARTEDGESFAO: bool
        TWOSIDEDMESHESOP: bool
        ULINESVDS: float
        USEMINMAXRANGESA: bool
        VDS_NOT_USED1: bool
        VLINESVDS: float
        WELDANDSMOOTHRA: bool
        ...
    class Bomb(SpacewarpObject):
        CHAOS: float
        DETONATION: MXSWrapperBase
        FALLOFF: float
        FALLOFFENABLE: bool
        GRAVITY: float
        MAXFRAGMENTSIZE: int
        MINFRAGMENTSIZE: int
        SEED: int
        SPIN: float
        STRENGTH: float
        ...
    class Bombbinding(SpacewarpModifier):
        ...
    class Bone(Helper):
        ...
    class BoneData(FloatController):
        ...
    class BoneGeometry(GeometryClass):
        ...
    class BoneObj(GeometryClass):
        ...
    class BoneSegTrans(Matrix3Controller):
        ...
    class BoneSys(Interface):
        ...
    class Bones(System):
        ...
    class BoolPacket(ReferenceMaker):
        ...
    class Boolean2(GeometryClass):
        ...
    class Boolean2ObjectManager(BooleanObjectManagerClass):
        ...
    class Boolean3(GeometryClass):
        ...
    class BooleanClass(Value):
        ...
    class BooleanExplorerManager(Interface):
        ...
    class BooleanObject2(GeometryClass):
        ...
    class BooleanObjectManager(Interface):
        ...
    class BooleanObjectManagerClass(MAXWrapper):
        ...
    class Box(GeometryClass):
        HEIGHT: float
        HEIGHTSEGS: int
        LENGTH: float
        LENGTHSEGS: int
        MAPCOORDS: bool
        TYPEINCREATIONMETHOD: int
        TYPEINHEIGHT: float
        TYPEINLENGTH: float
        TYPEINPOS: MXSWrapperBase
        TYPEINWIDTH: float
        WIDTH: float
        WIDTHSEGS: int
        ...
    class Box2(Value):
        ...
    class Box3(Value):
        ...
    class BoxGizmo(Helper):
        HEIGHT: float
        LENGTH: float
        SEED: int
        WIDTH: float
        ...
    class BoxPickNode(Primitive):
        ...
    class Box_2_Global_Utility(GlobalUtilityPlugin):
        ...
    class Bricks(TextureMap):
        BRICKS: None
        BRICKS_MAP: None
        BRICK_COLOR: MXSWrapperBase
        CHANGE_COLUMN: float
        CHANGE_ROW: float
        COLOR_VARIANCE: float
        EDGE_ROUGHNESS: float
        FADE_VARIANCE: float
        HOLES: int
        HORIZONTAL_COUNT: float
        HORIZONTAL_GAP: float
        LINE_SHIFT: float
        LOCK_GAP_SYMMETRY: int
        MORTAR: None
        MORTAR_COLOR: MXSWrapperBase
        MORTAR_MAP: None
        PER_COLUMN: int
        PER_ROW: int
        RANDOM_SEED: int
        RANDOM_SHIFT: float
        SHOW_TEXTURE_SWATCHES: int
        TILE_TYPE: int
        USE_COLUMN_EDIT: int
        USE_ROW_EDIT: int
        VERTICAL_COUNT: float
        VERTICAL_GAP: float
        ...
    class Brightness_And_Contrast(RenderEffect):
        BRIGHTNESS: float
        CONTRAST: float
        IGNOREBACK: bool
        ...
    class BrushPresetMgr(Interface):
        ...
    class Bulge_Angle_Deformer(ReferenceTarget):
        ...
    class ButtonControl(RolloutControl):
        ...
    class CATBone(GeometryClass):
        ...
    class CATBoneData(FloatController):
        ...
    class CATBoneDataMatrix3Controller(Matrix3Controller):
        ...
    class CATBoneSegTrans(Matrix3Controller):
        ...
    class CATClipFloat(FloatController):
        ...
    class CATClipMatrix3(Matrix3Controller):
        ...
    class CATClipRoot(FloatController):
        ...
    class CATClipWeights(FloatController):
        ...
    class CATCollapseLayers(MAXScriptFunction):
        ...
    class CATCollarBone(Matrix3Controller):
        ...
    class CATDigitSegTrans(Matrix3Controller):
        ...
    class CATDummyMoveMask(Matrix3Controller):
        ...
    class CATFootBend(FloatController):
        ...
    class CATFootLift(FloatController):
        ...
    class CATFootTrans2(Matrix3Controller):
        ...
    class CATGizmoTransform(Matrix3Controller):
        ...
    class CATHDPivotTrans(Matrix3Controller):
        PIVOTLOCATIONS: MXSWrapperBase
        ...
    class CATHIPivotTrans(Matrix3Controller):
        ...
    class CATHierarchyBranch(FloatController):
        ...
    class CATHierarchyBranch2(FloatController):
        ...
    class CATHierarchyLeaf(FloatController):
        ...
    class CATHierarchyRoot(FloatController):
        ...
    class CATImportBVH(MAXScriptFunction):
        ...
    class CATImportBip(MAXScriptFunction):
        ...
    class CATImportHTR(MAXScriptFunction):
        ...
    class CATKneeAngle(FloatController):
        ...
    class CATLegWeight(FloatController):
        ...
    class CATLiftOffset(FloatController):
        ...
    class CATLiftPlantMod(FloatController):
        ...
    class CATLimbData2(ReferenceTarget):
        ...
    class CATLimbData2FloatController(FloatController):
        ...
    class CATMonoGraph(FloatController):
        ...
    class CATMotionDigitRot(RotationController):
        ...
    class CATMotionHub2(Matrix3Controller):
        ...
    class CATMotionLayer(FloatController):
        ...
    class CATMotionLimb(FloatController):
        ...
    class CATMotionPlatform(Matrix3Controller):
        ...
    class CATMotionRot(RotationController):
        ...
    class CATMotionRotRotationController(RotationController):
        ...
    class CATMotionTail(Point3Controller):
        ...
    class CATMotionTailRot(RotationController):
        ...
    class CATMuscle(Helper):
        ...
    class CATParent(Helper):
        ...
    class CATParentSetupMode(MAXScriptFunction):
        ...
    class CATParentTrans(Matrix3Controller):
        ...
    class CATPivotPos(FloatController):
        ...
    class CATPivotRot(FloatController):
        ...
    class CATPoint3(Point3Controller):
        ...
    class CATRigRootNodeCtrl(Matrix3Controller):
        ...
    class CATSpineData2(ReferenceTarget):
        ...
    class CATSpineData2FloatController(FloatController):
        ...
    class CATSpineTrans2(Matrix3Controller):
        ...
    class CATStepShape(FloatController):
        ...
    class CATTransformOffset(Matrix3Controller):
        ...
    class CATUnitsPosition(PositionController):
        ...
    class CATUnitsScale(ScaleController):
        ...
    class CATWeight(FloatController):
        ...
    class CATWeightShift(FloatController):
        ...
    class CAT_LiftOffset(FloatController):
        ...
    class CAT_LiftPlantMod(FloatController):
        ...
    class CAT_OnMaxShutdown(MAXScriptFunction):
        ...
    class CAT_OnMaxStartup(MAXScriptFunction):
        ...
    class CATp3(Point3Controller):
        ...
    class CCRootClass(Value):
        ...
    class CFDColorVerticesMod(Modifier):
        CFDIMPORT_OBJECT: None
        NUM_SAMPLES: int
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        RED_AMOUNT: float
        X_COL: int
        Y_COL: int
        Z_COL: int
        _DUMMY: bool
        ...
    class CFDImportData(GeometryClass):
        CSV_FILE: str
        DEFAULT_VALUE: float
        FORCE_RELOAD_SIGNAL: bool
        NBBOTTOMLINES: int
        NBHEADERLINES: int
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        SEPARATOR: str
        WELD_DST: float
        X_POS__CHN: int
        Y_POS__CHN: int
        Z_POS__CHN: int
        _DUMMY: bool
        ...
    class CFDInterpOnSpline(GeometryClass):
        AMOUNT: float
        CLONE: None
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        RED_AMOUNT: float
        SPLINES: None
        _DUMMY: bool
        ...
    class CFDKeepNVertices(Modifier):
        N: int
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        _DUMMY: bool
        ...
    class CFDSplineNode(Shape):
        BAKESPLINE_SIGNAL: bool
        CFD_POINTS: None
        FIELD_INTERPOLATION: int
        FIELD_SAMPLING: float
        MATERIAL_ANIMATION: int
        MATERIAL_ID_COUNT: int
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        REFRESH_DATA_SIGNAL: bool
        SMOOTHING: float
        SPLINE_ORIGIN_HELPER: None
        SPLINE_VERTICES: int
        _DUMMY: bool
        ...
    class CFDSplinePaths(Shape):
        CFDIMPORT_OBJECT: None
        DISABLE: bool
        NUM_SAMPLES: int
        NUM_STEPS: int
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        PROFILE: None
        STEP_SIZE: float
        X_COL: int
        Y_COL: int
        Z_COL: int
        _DUMMY: bool
        ...
    class CFDVelocityField(GeometryClass):
        ARROW_SCALE: float
        CFDIMPORT_OBJECT: None
        MAX_LENGTH: float
        MIN_LENGTH: float
        NORMALIZED_LENGTHS: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        RED_AMOUNT: float
        X_COL: int
        Y_COL: int
        Z_COL: int
        _DUMMY: bool
        ...
    class CFDVertexPaintChannel(Modifier):
        CFDPOINTS: None
        CHANNELID: int
        LOCAL_NORM: bool
        NBCLOSEST: int
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        SMOOTH_FACTOR: float
        UPDATE_CACHES: bool
        _DUMMY: bool
        ...
    class CFDVertexPaintVelocity(Modifier):
        CFDPOINTS: None
        LOCAL_NORM: bool
        NBCLOSEST: int
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        SMOOTH_FACTOR: float
        UPDATE_CACHES: bool
        VX_CHN: int
        VY_CHN: int
        VZ_CHN: int
        _DUMMY: bool
        ...
    class CIN(BitmapIO):
        ...
    class CMB(BitmapIO):
        ...
    class COM_DCOM_Server_Control(UtilityPlugin):
        ...
    class CRTCheckAssert(Primitive):
        ...
    class CRTCheckMemory(Primitive):
        ...
    class CRTCorruptHeap(Primitive):
        ...
    class CRTheapcheck(Primitive):
        ...
    class CTBitMap(Value):
        ...
    class CTMotionTracker(Value):
        ...
    class CUIMouseConfigManagerImplement(Interface):
        ...
    class CV_Curve(Shape):
        CAP_SEGMENTS: int
        RENDER_ANGLE2: float
        RENDER_ANGLE: float
        RENDER_LENGTH: float
        RENDER_SIDES: int
        RENDER_THICKNESS: float
        RENDER_THRESHOLD: float
        RENDER_WIDTH: float
        SPHERE_CAP: float
        ...
    class CV_Curveshape(Shape):
        ...
    class CV_Surf(GeometryClass):
        ...
    class C_Ext(GeometryClass):
        BACK_LENGTH: float
        BACK_SEGMENTS: int
        BACK_WIDTH: float
        CENTERCREATE: bool
        FRONT_LENGTH: float
        FRONT_SEGMENTS: int
        FRONT_WIDTH: float
        HEIGHT: float
        HEIGHT_SEGMENTS: int
        MAPCOORDS: bool
        SIDE_LENGTH: float
        SIDE_SEGMENTS: int
        SIDE_WIDTH: float
        TYPEINBACKLENGTH: float
        TYPEINBACKWIDTH: float
        TYPEINCREATIONMETHOD: int
        TYPEINFRONTLENGTH: float
        TYPEINFRONTWIDTH: float
        TYPEINHEIGHT: float
        TYPEINPOS: MXSWrapperBase
        TYPEINSIDELENGTH: float
        TYPEINSIDEWIDTH: float
        WIDTH_SEGMENTS: int
        ...
    class Cache(Helper):
        CACHE_TEST_RESULTS: bool
        CACHE_WITH_FILE: bool
        CACHE_WITH_HOLD: bool
        CLEAR_END_TIME: MXSWrapperBase
        CLEAR_RANGE_TYPE: int
        CLEAR_START_TIME: MXSWrapperBase
        END_TIME: MXSWrapperBase
        EVERY_NTH_FRAME: int
        MEMORY_FOR_CURRENT_FRAME: int
        MEMORY_LIMIT: int
        MEMORY_TOTAL: int
        RANGE_TYPE: int
        SAMPLING_TYPE: int
        START_TIME: MXSWrapperBase
        UPDATE_TYPE: int
        UPDATE_VIEWPORTS: bool
        USE_AT: int
        ...
    class CacheDisk(Helper):
        CACHE_TEST_RESULTS: bool
        END_TIME: MXSWrapperBase
        EVERY_NTH_FRAME: int
        EXCLUDE_MAPPING: bool
        EXCLUDE_MATERIAL_ID: bool
        EXCLUDE_ROTATION: bool
        EXCLUDE_SCALE: bool
        EXCLUDE_SCRIPT_DATA: bool
        EXCLUDE_SHAPE: bool
        MEMORY_LIMIT: int
        POST_CACHE_OPERATORS: MXSWrapperBase
        RANGE_TYPE: int
        SAMPLING_TYPE: int
        START_TIME: MXSWrapperBase
        UPDATE_CLEAR_END_TIME: MXSWrapperBase
        UPDATE_CLEAR_RANGE_TYPE: int
        UPDATE_CLEAR_START_TIME: MXSWrapperBase
        UPDATE_VIEWPORTS: bool
        USE_AT: int
        USE_POST_CACHE_OPERATORS: bool
        WRITE_TO_FILE: None
        ...
    class CacheFile(ReferenceTarget):
        ...
    class CacheSelective(Helper):
        CACHE_TEST_RESULTS: bool
        END_TIME: MXSWrapperBase
        EVERY_NTH_FRAME: int
        EXCLUDE_MAPPING: bool
        EXCLUDE_MATERIAL_ID: bool
        EXCLUDE_ROTATION: bool
        EXCLUDE_SCALE: bool
        EXCLUDE_SCRIPT_DATA: bool
        EXCLUDE_SHAPE: bool
        MEMORY_LIMIT: int
        POST_CACHE_OPERATORS: MXSWrapperBase
        RANGE_TYPE: int
        SAMPLING_TYPE: int
        SAVE_CACHE_WITH_FILE: bool
        SAVE_CACHE_WITH_HOLD: bool
        START_TIME: MXSWrapperBase
        UPDATE_CLEAR_END_TIME: MXSWrapperBase
        UPDATE_CLEAR_RANGE_TYPE: int
        UPDATE_CLEAR_START_TIME: MXSWrapperBase
        UPDATE_VIEWPORTS: bool
        USE_AT: int
        USE_POST_CACHE_OPERATORS: bool
        ...
    class CacheSubGraphOutputFragment(GraphicsFragmentPlugin):
        ...
    class Cache_Disk(Helper):
        CACHE_TEST_RESULTS: bool
        END_TIME: MXSWrapperBase
        EVERY_NTH_FRAME: int
        EXCLUDE_MAPPING: bool
        EXCLUDE_MATERIAL_ID: bool
        EXCLUDE_ROTATION: bool
        EXCLUDE_SCALE: bool
        EXCLUDE_SCRIPT_DATA: bool
        EXCLUDE_SHAPE: bool
        MEMORY_LIMIT: int
        POST_CACHE_OPERATORS: MXSWrapperBase
        RANGE_TYPE: int
        SAMPLING_TYPE: int
        START_TIME: MXSWrapperBase
        UPDATE_CLEAR_END_TIME: MXSWrapperBase
        UPDATE_CLEAR_RANGE_TYPE: int
        UPDATE_CLEAR_START_TIME: MXSWrapperBase
        UPDATE_VIEWPORTS: bool
        USE_AT: int
        USE_POST_CACHE_OPERATORS: bool
        WRITE_TO_FILE: None
        ...
    class Cache_Selective(Helper):
        CACHE_TEST_RESULTS: bool
        END_TIME: MXSWrapperBase
        EVERY_NTH_FRAME: int
        EXCLUDE_MAPPING: bool
        EXCLUDE_MATERIAL_ID: bool
        EXCLUDE_ROTATION: bool
        EXCLUDE_SCALE: bool
        EXCLUDE_SCRIPT_DATA: bool
        EXCLUDE_SHAPE: bool
        MEMORY_LIMIT: int
        POST_CACHE_OPERATORS: MXSWrapperBase
        RANGE_TYPE: int
        SAMPLING_TYPE: int
        SAVE_CACHE_WITH_FILE: bool
        SAVE_CACHE_WITH_HOLD: bool
        START_TIME: MXSWrapperBase
        UPDATE_CLEAR_END_TIME: MXSWrapperBase
        UPDATE_CLEAR_RANGE_TYPE: int
        UPDATE_CLEAR_START_TIME: MXSWrapperBase
        UPDATE_VIEWPORTS: bool
        USE_AT: int
        USE_POST_CACHE_OPERATORS: bool
        ...
    class Caddy(GlobalUtilityPlugin):
        ...
    class CallbackFn1(MAXScriptFunction):
        ...
    class CamMatchDataCustAttrib(CustAttrib):
        AXIS_MODE: int
        VIEWPORT_SIZE_X: int
        VIEWPORT_SIZE_Y: int
        XLINE1_B: MXSWrapperBase
        XLINE1_E: MXSWrapperBase
        XLINE2_B: MXSWrapperBase
        XLINE2_E: MXSWrapperBase
        YLINE1_B: MXSWrapperBase
        YLINE1_E: MXSWrapperBase
        YLINE2_B: MXSWrapperBase
        YLINE2_E: MXSWrapperBase
        ZLINE1_B: MXSWrapperBase
        ZLINE1_E: MXSWrapperBase
        ZLINE2_B: MXSWrapperBase
        ZLINE2_E: MXSWrapperBase
        ...
    class CamPerspCorrect(Modifier):
        PARAMPERSPECTCORRECTAMOUNT: float
        PARAMPERSPECTCORRECTDIR: float
        ...
    class CamPoint(Helper):
        AXISLENGTH: float
        SHOWAXIS: bool
        ...
    class CameraCulling(Helper):
        CAMERA: None
        CULLING_TYPE: int
        FAR_CLIP_DISTANCE: float
        NEAR_CLIP_DISTANCE: float
        RENDER_CULLING: bool
        SELECTION_TYPE: int
        SUBFRAME_PRECISION: bool
        USE_ACTIVE_CAMERA: bool
        USE_CAMERA_CLIPPING_PLANES: bool
        USE_FAR_CLIP: bool
        USE_FOR_GROUP_SELECTION: bool
        USE_NEAR_CLIP: bool
        VIEWPORT_CULLING: bool
        ...
    class CameraMBlur(Helper):
        CAMERA: None
        MULTIPLIER: float
        USE_ACTIVE_CAMERA: bool
        USE_EVENT_MULTIPLIER: bool
        ...
    class CameraMap(Modifier):
        ...
    class CameraMapSpaceWarp(SpacewarpObject):
        ...
    class CameraMapTexture(TextureMap):
        AFFECTBEHINDCAM: bool
        ANGLETHRESHOLD: float
        ASPECTMODE: int
        BACKFACE: bool
        CAMERA: None
        HASPECT: float
        MAPCHANNEL: int
        MASK: None
        MASKUSESPROJECTION: bool
        TEXTURE: None
        USEMASK: bool
        USEZBUFFER: bool
        VASPECT: float
        ZBUFFER: None
        ZFUDGE: float
        ...
    class Camera_Culling(Helper):
        CAMERA: None
        CULLING_TYPE: int
        FAR_CLIP_DISTANCE: float
        NEAR_CLIP_DISTANCE: float
        RENDER_CULLING: bool
        SELECTION_TYPE: int
        SUBFRAME_PRECISION: bool
        USE_ACTIVE_CAMERA: bool
        USE_CAMERA_CLIPPING_PLANES: bool
        USE_FAR_CLIP: bool
        USE_FOR_GROUP_SELECTION: bool
        USE_NEAR_CLIP: bool
        VIEWPORT_CULLING: bool
        ...
    class Camera_IMBlur(Helper):
        CAMERA: None
        MULTIPLIER: float
        USE_ACTIVE_CAMERA: bool
        USE_EVENT_MULTIPLIER: bool
        ...
    class Camera_Map_Per_Pixel(TextureMap):
        AFFECTBEHINDCAM: bool
        ANGLETHRESHOLD: float
        ASPECTMODE: int
        BACKFACE: bool
        CAMERA: None
        HASPECT: float
        MAPCHANNEL: int
        MASK: None
        MASKUSESPROJECTION: bool
        TEXTURE: None
        USEMASK: bool
        USEZBUFFER: bool
        VASPECT: float
        ZBUFFER: None
        ZFUDGE: float
        ...
    class Camera_Match(UtilityPlugin):
        ...
    class Camera_Tracker(UtilityPlugin):
        ...
    class Cap_Holes(Modifier):
        SMOOTH: bool
        SM_ENDS: bool
        VIS_EDGES: bool
        ...
    class Capsule(GeometryClass):
        HEIGHT: float
        HEIGHTSEGS: int
        HEIGHTTYPE: int
        MAPCOORDS: bool
        RADIUS: float
        SIDES: int
        SLICEFROM: float
        SLICEON: bool
        SLICETO: float
        SMOOTH: bool
        ...
    class CaptureAnimation(MAXScriptFunction):
        ...
    class CaptureCallStack(Primitive):
        ...
    class Captured_Object_State(ReferenceTarget):
        ...
    class Casement(GeometryClass):
        DEPTH: float
        FRAME_THICKNESS: float
        GENERATE_MAPPING_COORDS: bool
        GLAZING_THICKNESS: float
        HEIGHT: float
        HORIZONTAL_FRAME_WIDTH: float
        NUMBER_OF_CASEMENTS: int
        OPENS_TO_INSIDE: bool
        PANEL_WIDTH: float
        PERCENT_OPEN: int
        VERTICAL_FRAME_WIDTH: float
        WIDTH: float
        ...
    class Catmull_Rom(Filter):
        ...
    class Cellular(TextureMap):
        ADAPTIVE: bool
        CELLCOLOR: MXSWrapperBase
        CELLMAP: None
        COORDS: MXSWrapperBase
        DIVCOLOR1: MXSWrapperBase
        DIVCOLOR2: MXSWrapperBase
        DIVMAP1: None
        DIVMAP2: None
        FRACTAL: bool
        HIGHTHRESH: float
        ITERATION: float
        LOWTHRESH: float
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        MAP3ENABLED: bool
        MIDTHRESH: float
        OUTPUT: MXSWrapperBase
        ROUGHNESS: float
        SIZE: float
        SMOOTH: float
        SPREAD: float
        TYPE: int
        VARIATION: float
        ...
    class CenterObject(MappedPrimitive):
        ...
    class CenterPivot(MappedPrimitive):
        ...
    class Chair(GeometryClass):
        GENDER: int
        HEIGHT: float
        ID: int
        MOTIONSEED: int
        SINGLE: bool
        ...
    class Chamfer(Modifier):
        ADDINSET: bool
        AMOUNT: float
        AMOUNTTYPE: int
        ANGLEFACTORVERTEX: float
        BIASENDPOINTS: bool
        CHAMFERTYPE: int
        DEPTH: float
        DEPTHTYPE: int
        FORCEPOSITIVEOFFSET: bool
        INSETAMOUNT: float
        INSETOFFSET: float
        INSETSEGMENTS: int
        INSETTYPE: int
        INVERT: bool
        LIMITEFFECT: bool
        MATERIALID: int
        MATERIALOPTION: int
        MAXAMOUNT: float
        MAXANGLE: float
        MINAMOUNT: float
        MINANGLE: float
        MITERENDBIAS: float
        MITERINGTYPE: int
        OPENCHAMFER: bool
        PRESETOPTIONSCOMBOBOX: int
        QUADINTERSECTIONMODE: bool
        RADIUSBIAS: float
        SCALE: float
        SEGMENTS: int
        SELECTIONOPTION: int
        SETMATERIAL: bool
        SMOOTH: bool
        SMOOTHINGOPTION: int
        SMOOTHTHRESHOLD: float
        SMOOTHTOADJACENT: bool
        SMOOTHTYPE: int
        TENSION: float
        USECONSTANTOFFSET: bool
        USEMAXANGLE: bool
        USEMINANGLE: bool
        ...
    class ChamferBox(GeometryClass):
        FILLET: float
        FILLET_SEGMENTS: int
        HEIGHT: float
        HEIGHT_SEGMENTS: int
        LENGTH: float
        LENGTH_SEGMENTS: int
        MAPCOORDS: bool
        SMOOTH: bool
        TYPEINCREATIONMETHOD: int
        TYPEINFILLET: float
        TYPEINHEIGHT: float
        TYPEINLENGTH: float
        TYPEINPOS: MXSWrapperBase
        TYPEINWIDTH: float
        WIDTH: float
        WIDTH_SEGMENTS: int
        ...
    class ChamferCyl(GeometryClass):
        CAP_SEGMENTS: int
        FILLET: float
        FILLET_SEGMENTS: int
        HEIGHT: float
        HEIGHT_SEGMENTS: int
        MAPCOORDS: bool
        RADIUS: float
        SIDES: int
        SLICE_FROM: float
        SLICE_ON: bool
        SLICE_TO: float
        SMOOTH_ON: bool
        TYPEINCREATIONMETHOD: int
        TYPEINFILLET: float
        TYPEINHEIGHT: float
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS: float
        ...
    class ChamferMod(Modifier):
        ADDINSET: bool
        AMOUNT: float
        AMOUNTTYPE: int
        ANGLEFACTORVERTEX: float
        BIASENDPOINTS: bool
        CHAMFERTYPE: int
        DEPTH: float
        DEPTHTYPE: int
        FORCEPOSITIVEOFFSET: bool
        INSETAMOUNT: float
        INSETOFFSET: float
        INSETSEGMENTS: int
        INSETTYPE: int
        INVERT: bool
        LIMITEFFECT: bool
        MATERIALID: int
        MATERIALOPTION: int
        MAXAMOUNT: float
        MAXANGLE: float
        MINAMOUNT: float
        MINANGLE: float
        MITERENDBIAS: float
        MITERINGTYPE: int
        OPENCHAMFER: bool
        PRESETOPTIONSCOMBOBOX: int
        QUADINTERSECTIONMODE: bool
        RADIUSBIAS: float
        SCALE: float
        SEGMENTS: int
        SELECTIONOPTION: int
        SETMATERIAL: bool
        SMOOTH: bool
        SMOOTHINGOPTION: int
        SMOOTHTHRESHOLD: float
        SMOOTHTOADJACENT: bool
        SMOOTHTYPE: int
        TENSION: float
        USECONSTANTOFFSET: bool
        USEMAXANGLE: bool
        USEMINANGLE: bool
        ...
    class ChamferModGlobal(Interface):
        ...
    class ChangeHandler(Value):
        ...
    class ChannelInfo(Interface):
        ...
    class Channel_Info(UtilityPlugin):
        ...
    class CharStream(Value):
        ...
    class Character(Helper):
        ...
    class CharacterAssembly(Helper):
        CHARACTERID: int
        DISPLAYRES: int
        ICONSIZE: int
        ...
    class CharacterHelper(Helper):
        ...
    class CheckBoxControl(RolloutControl):
        ...
    class CheckButtonControl(RolloutControl):
        ...
    class CheckForSave(Primitive):
        ...
    class Checker(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COORDS: MXSWrapperBase
        MAP1: None
        MAP1ENABLED: bool
        MAP2: None
        MAP2ENABLED: bool
        SOFTEN: float
        ...
    class Circle(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        MAPCOORDS: bool
        OPTIMIZE: bool
        QUAD_CAP: bool
        RADIUS: float
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        ...
    class CirclePickNode(Primitive):
        ...
    class CivilView_Alignment(Shape):
        ALIGNENTTYPEARRAY: MXSWrapperBase
        CURRENTDATASET: int
        DATASETNAMEARRAY: MXSWrapperBase
        DATASETSIZEARRAY: MXSWrapperBase
        DESIGNSPEEDCOMMENTS: MXSWrapperBase
        DESIGNSPEEDSTATIONS: MXSWrapperBase
        DESIGNSPEEDVALUES: MXSWrapperBase
        ENDSTATION: float
        ISALIGNENTSTARTEND: MXSWrapperBase
        ISPROFILEENTSTARTEND: MXSWrapperBase
        PROFILEENTTYPEARRAY: MXSWrapperBase
        RADBEARGRADEARRAY: MXSWrapperBase
        STARTSTATION: float
        XYZSTATIONARRAY: MXSWrapperBase
        ...
    class CivilView_Pipe(Shape):
        BEARING: float
        CROSSSECTIONALSHAPE: int
        DESCRIPTION: str
        DISPLAYNAME: str
        ENDSTRUCTUREHANDLE: str
        FLOWDIRECTION: int
        FLOWDIRECTIONMETHOD: int
        HORTYPE: int
        INNERDIAMETERORWIDTH: float
        INNERHEIGHT: float
        LENGTH2DCENTERTOCENTER: float
        LENGTH2DTOINSIDEEDGE: float
        LENGTH3DCENTERTOCENTER: float
        LENGTH3DTOINSIDEEDGE: float
        MAXIMUMCOVER: float
        MINIMUMCOVER: float
        OUTERDIAMETERORWIDTH: float
        OUTERHEIGHT: float
        PARTDESCRIPTION: str
        PARTSIZENAME: str
        PARTSUBTYPE: str
        PSETYPE: int
        RADIUS: float
        SLOPE: float
        STARTSTRUCTUREHANDLE: str
        ...
    class Civil_Structure(GeometryClass):
        BARRELPIPECLEARANCE: float
        CONCENTRIC_OFFSET_X: float
        CONCENTRIC_OFFSET_Y: float
        CONE_HEIGHT: float
        CONE_LENGTH: float
        CONE_WIDTHORDIA: float
        CONNECTEDPARTCOUNT: int
        CONNECTEDPIPESCOUNT: int
        COVER: None
        DISPLAYNAME: None
        FLOOR_THICKNESS: float
        FRAME: None
        FRAME_HEIGHT: float
        FRAME_LENGTH: float
        FRAME_TYPE: int
        FRAME_WIDTHORDIA: float
        GRATE: None
        MAPCOORDS: bool
        MATERIALNAME: None
        NETWORKID: None
        NETWORKNAME: None
        PARTDEFID: None
        PARTDESC: None
        PARTSIZENAME: None
        PARTSUBTYPE: None
        PARTTYPE: int
        RIM_THICKNESS: float
        STRUCTURE_HEIGHT: float
        STRUCTURE_LENGTH: float
        STRUCTURE_WIDTHORDIA: float
        TYPE: int
        USE_MATID: bool
        WALL_THICKNESS: float
        ...
    class Civil_View_Divide_Spline(Modifier):
        ...
    class Civil_View_Guard_Rail(Modifier):
        ...
    class Civil_View_Path___Surface_Constraint(Matrix3Controller):
        ...
    class Civil_View_Path___Surface_ConstraintMatrix3Controller(Matrix3Controller):
        ...
    class Civil_View_Path___Surface_ConstraintMatrix3ControllerMatrix3Controller(Matrix3Controller):
        ...
    class Civil_View_Road_Marking(Modifier):
        ...
    class Civil_View_Sight_Checker__Calc(RenderEffect):
        ...
    class Civil_View_Spline_To_Mesh(Modifier):
        ...
    class Civil_View_Swept_Object(SpacewarpModifier):
        ...
    class Civil_View_Traffic_Data_Constraint(ScaleController):
        ...
    class ClayFragment(GraphicsFragmentPlugin):
        ...
    class CleanUp(Helper):
        DUMMY: int
        ...
    class Clean_MultiMaterial(UtilityPlugin):
        ...
    class ClearCurSelSet(Primitive):
        ...
    class ClearNodeSelection(Primitive):
        ...
    class ClearSubSelSets(Primitive):
        ...
    class ClipAssigner(ReferenceTarget):
        ...
    class ClipAssociation(ReferenceTarget):
        ...
    class ClipState(ReferenceTarget):
        ...
    class Clip_Associations(ReferenceTarget):
        ...
    class Clone_And_Align_Tool(UtilityPlugin):
        ...
    class CloseActiveShade(Primitive):
        ...
    class Cloth(Modifier):
        ADVANCEDPINCHING: bool
        CHECKINTERSECTIONS: bool
        CLOTHCLOTHMETHOD: int
        ENABLEENDFRAME: bool
        ENDFRAME: int
        GRAVITY: float
        IGNOREBACKFACING: bool
        RELATIVEVELOCITY: float
        SCALE: float
        SELFCOLLISION: bool
        SHOWCURRENTSTATE: bool
        SHOWENABLEDCLOTHCOLLISION: bool
        SHOWENABLEDSOLIDCOLLISION: bool
        SHOWSEWINGSPRINGS: bool
        SHOWTARGETSTATE: bool
        SHOWTENSION: bool
        SIMONMOUSEDOWN: bool
        SIMONRENDER: bool
        SIMPRIORITY: int
        SOLIDCOLLISION: bool
        STARTFRAME: int
        SUBSAMPLE: int
        TENSIONSCALE: float
        TIMESCALE: float
        TIMESTEP: float
        USEGRAVITY: bool
        USESEWINGSPRINGS: bool
        WELDMETHOD: int
        ...
    class CmdPanelOptimization(Interface):
        ...
    class CogControl(ReferenceTarget):
        NAME: str
        STARTSTATE: None
        STATES: MXSWrapperBase
        ...
    class CollarBoneTrans(Matrix3Controller):
        ...
    class Collision(Helper):
        COLLISION_COUNT: int
        COLLISION_COUNT_OPTIONS: int
        COLLISION_NODES: MXSWrapperBase
        MAX_SPEED: float
        MIN_SPEED: float
        RANDOM_SEED: int
        SPEED_OPTION: int
        TEST_TYPE: int
        WILL_COLLIDE_FRAME: int
        ...
    class Collision_Spawn(Helper):
        COLLISION_NODES: MXSWrapperBase
        DELETE_PARENT: bool
        DIVERGENCE: float
        NUMBER_OF_COLLISIONS: int
        NUMBER_OF_OFFSPRINGS: int
        OFFSPRINGS_VARIATION: float
        OFFSPRING_SPEED: int
        PARENT_SPEED: int
        RANDOM_SEED: int
        RESTART_PARTICLE_AGE: bool
        SCALE_FACTOR: float
        SCALE_VARIATION: float
        SPAWN_ABLE: float
        SPAWN_TYPE: int
        SPEED: float
        SPEED_INHERITED: float
        SPEED_TYPE: int
        SPEED_VARIATION: float
        SYNC_TYPE: int
        TRUE_FOR_PARTICLES_COLLIDED: bool
        TRUE_FOR_SPAWN_PARTICLES: bool
        ...
    class ColorCorrection(TextureMap):
        BRIGHTNESS: float
        COLOR: MXSWrapperBase
        CONTRAST: float
        ENABLEB: bool
        ENABLEG: bool
        ENABLER: bool
        EXPOSUREMODE: int
        GAINB: float
        GAING: float
        GAINR: float
        GAINRGB: float
        GAMMAB: float
        GAMMAG: float
        GAMMAR: float
        GAMMARGB: float
        HUESHIFT: float
        LIFTB: float
        LIFTG: float
        LIFTR: float
        LIFTRGB: float
        LIGHTNESSMODE: int
        MAP: None
        PIVOTB: float
        PIVOTG: float
        PIVOTR: float
        PIVOTRGB: float
        PRINTERLIGHTS: float
        REWIREA: int
        REWIREB: int
        REWIREG: int
        REWIREMODE: int
        REWIRER: int
        SATURATION: float
        TINT: MXSWrapperBase
        TINTSTRENGTH: float
        ...
    class ColorMap(TextureMap):
        GAIN: float
        GAMMA: float
        MAP: None
        MAPENABLED: bool
        REVERSEGAMMA: bool
        SOLIDCOLOR: MXSWrapperBase
        ...
    class ColorPickerControl(RolloutControl):
        ...
    class ColorTargetToPresentableTargetFragment(GraphicsFragmentPlugin):
        ...
    class Color_Balance(RenderEffect):
        BLUE: int
        GREEN: int
        IGNOREBACK: bool
        PRESERVELUM: bool
        RED: int
        ...
    class Color_Clipboard(UtilityPlugin):
        ...
    class Color_Correction(TextureMap):
        BRIGHTNESS: float
        COLOR: MXSWrapperBase
        CONTRAST: float
        ENABLEB: bool
        ENABLEG: bool
        ENABLER: bool
        EXPOSUREMODE: int
        GAINB: float
        GAING: float
        GAINR: float
        GAINRGB: float
        GAMMAB: float
        GAMMAG: float
        GAMMAR: float
        GAMMARGB: float
        HUESHIFT: float
        LIFTB: float
        LIFTG: float
        LIFTR: float
        LIFTRGB: float
        LIGHTNESSMODE: int
        MAP: None
        PIVOTB: float
        PIVOTG: float
        PIVOTR: float
        PIVOTRGB: float
        PRINTERLIGHTS: float
        REWIREA: int
        REWIREB: int
        REWIREG: int
        REWIREMODE: int
        REWIRER: int
        SATURATION: float
        TINT: MXSWrapperBase
        TINTSTRENGTH: float
        ...
    class Color_RGB(Point3Controller):
        ...
    class Color_RGBA(Point4Controller):
        ...
    class ComboBoxControl(RolloutControl):
        ...
    class Combustion(TextureMap):
        HEIGHT: int
        WIDTH: int
        ...
    class CommitControllerValue(Primitive):
        ...
    class Compass(Helper):
        ...
    class CompleteMap(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        SHADOWSON: bool
        TARGETMAPSLOTNAME: str
        ...
    class CompleteRedraw(Primitive):
        ...
    class CompositeMap(TextureMap):
        BLENDMODE: MXSWrapperBase
        DLGOPENED: MXSWrapperBase
        LAYERNAME: MXSWrapperBase
        MAPENABLED: MXSWrapperBase
        MAPLIST: MXSWrapperBase
        MASK: MXSWrapperBase
        MASKENABLED: MXSWrapperBase
        OPACITY: MXSWrapperBase
        ...
    class CompositeTexturemap(TextureMap):
        BLENDMODE: MXSWrapperBase
        DLGOPENED: MXSWrapperBase
        LAYERNAME: MXSWrapperBase
        MAPENABLED: MXSWrapperBase
        MAPLIST: MXSWrapperBase
        MASK: MXSWrapperBase
        MASKENABLED: MXSWrapperBase
        OPACITY: MXSWrapperBase
        ...
    class Condition(ReferenceTarget):
        ANGLE_A: float
        ANGLE_AS_ORIENTATION: bool
        ANGLE_B: float
        CONDITION_TYPE_INT: int
        CONDITION_TYPE_REAL: int
        FILTER: None
        FLOAT_A: float
        FLOAT_B: float
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INTEGER_A: int
        INTEGER_B: int
        PERCENT_A: float
        PERCENT_B: float
        SYNC_TYPE: int
        TIME_A: int
        TIME_B: int
        TYPE: int
        UNITS_PER_TYPE: int
        USE_AS_ACCELERATION: bool
        USE_AS_SPEED_OR_SPIN_RATE: bool
        USE_E4: bool
        USE_INPUT_AS_A: bool
        USE_INPUT_AS_B: bool
        USE_SECOND_CONDITION: bool
        WORLD_A: float
        WORLD_B: float
        ...
    class Cone(GeometryClass):
        CAPSEGS: int
        HEIGHT: float
        HEIGHTSEGS: int
        MAPCOORDS: bool
        RADIUS1: float
        RADIUS2: float
        SIDES: int
        SLICE: bool
        SLICEFROM: float
        SLICEON: bool
        SLICETO: float
        SMOOTH: bool
        TYPEINCREATIONMETHOD: int
        TYPEINHEIGHT: float
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS1: float
        TYPEINRADIUS2: float
        ...
    class ConeAngleManip(Helper):
        ANGLE: float
        ASPECT: float
        DIRECTION: MXSWrapperBase
        DISTANCE: float
        ORIGIN: MXSWrapperBase
        USESQUARE: bool
        ...
    class Cone_Angle(Helper):
        ANGLE: float
        ASPECT: float
        DIRECTION: MXSWrapperBase
        DISTANCE: float
        ORIGIN: MXSWrapperBase
        USESQUARE: bool
        ...
    class ConfigureBitmapPaths(Primitive):
        ...
    class Conform(GeometryClass):
        ...
    class ConformSpaceWarp(SpacewarpObject):
        ICON_SIZE: float
        PROJECTION_DISTANCE: float
        SELECTED_VERTS: int
        STANDOFF_DISTANCE: float
        ...
    class Conjugate(Generic):
        ...
    class Connect(GeometryClass):
        ...
    class ConstrFilterFn(MAXScriptFunction):
        ...
    class Container(Helper):
        ACCESSCONTENT: bool
        ACCESSPUBLISHEDCONTENT: bool
        ALLOWINPLACEEDITING: bool
        ALTERNATEDEFINITIONFILENAME: MXSWrapperBase
        AUTOUPDATECLOSED: bool
        CONTENTBOUNDINGBOX: bool
        CURRENTALTERNATEDEFINITION: int
        DISPLAYLABEL: bool
        DISPLAYSTATUS: bool
        DUPLICATEMATCHINGLAYERS: bool
        EDITINGUSER: str
        LOCALDEFINITIONFILENAME: str
        OVERRIDENODEPROPERTIES: bool
        SIZE: float
        SOURCEDEFINITIONFILENAME: str
        UNLOADED: bool
        UPDATENEEDED: bool
        ...
    class ContainerHelper(Helper):
        ACCESSCONTENT: bool
        ACCESSPUBLISHEDCONTENT: bool
        ALLOWINPLACEEDITING: bool
        ALTERNATEDEFINITIONFILENAME: MXSWrapperBase
        AUTOUPDATECLOSED: bool
        CONTENTBOUNDINGBOX: bool
        CURRENTALTERNATEDEFINITION: int
        DISPLAYLABEL: bool
        DISPLAYSTATUS: bool
        DUPLICATEMATCHINGLAYERS: bool
        EDITINGUSER: str
        LOCALDEFINITIONFILENAME: str
        OVERRIDENODEPROPERTIES: bool
        SIZE: float
        SOURCEDEFINITIONFILENAME: str
        UNLOADED: bool
        UPDATENEEDED: bool
        ...
    class ContainerPreferences(Interface):
        ...
    class Containers(Interface):
        ...
    class Contour_Data_Packet(ReferenceMaker):
        ...
    class Contour_Translator(ReferenceMaker):
        ...
    class Control(Value):
        ...
    class ControlContainer(GeometryClass):
        ...
    class ControlContainerGeometry(GeometryClass):
        ...
    class Convert(ReferenceTarget):
        BOOLEAN_CONVERSION: int
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INTEGER_TIME_CONVERSION: int
        MATRIX_VECTOR_CONVERSION: int
        NEGATIVE_UP_TOWARD_ZERO: bool
        PAIR_INTEGER_CONVERSION: int
        QUATERNION_REAL_CONVERSION: int
        QUATERNION_VECTOR_CONVERSION: int
        REAL_INTEGER_CONVERSION: int
        REAL_TIME_CONVERSION: int
        REAL_VECTOR_CONVERSION: int
        TYPE: int
        USE_I3_AS_OBJECT_INDEX: bool
        VECTOR_PAIR_CONVERSION: int
        VECTOR_QUATERNION_CONVERSION: int
        VECTOR_REAL_CONVERSION: int
        ...
    class ConvertDirIDToInt(Primitive):
        ...
    class ConvertIntToDirID(Primitive):
        ...
    class ConvertKelvinToRGB(Primitive):
        ...
    class ConvertToBody(Primitive):
        ...
    class ConvertToBodyCutter(Primitive):
        ...
    class ConvertToJoinBodies(Primitive):
        ...
    class ConvertToPatch(Modifier):
        QUADSTOQUADS: bool
        SELECTIONCONVERSION: int
        SELECTIONLEVEL: int
        USESOFTSELECTION: int
        ...
    class Cook_Variable(Filter):
        ...
    class Cookie(VideoPostFilter):
        ...
    class CopyCollection(Value):
        ...
    class Copy_Out(Helper):
        NUMBER_OF_COPIES: int
        ...
    class Crease(Modifier):
        CREASE: float
        CREASECOLOR: MXSWrapperBase
        DISPLAYCOLOR: bool
        SELECTIONOPTION: int
        ...
    class CreaseExplorerManager(Interface):
        ...
    class CreaseMod(Modifier):
        CREASE: float
        CREASECOLOR: MXSWrapperBase
        DISPLAYCOLOR: bool
        SELECTIONOPTION: int
        ...
    class CreaseSet(Modifier):
        ANGLEA: float
        ANGLEB: float
        ANGLESELECTTYPE: int
        AUTOSELECTNODES: bool
        CREASESETCOLOR: MXSWrapperBase
        CREASESETCREASE: MXSWrapperBase
        CREASESETNAME: MXSWrapperBase
        CREASESETSELECT: MXSWrapperBase
        CREASESETTYPE: MXSWrapperBase
        DISPLAYSETCOLORS: bool
        IGNOREBACKFACING: bool
        KEEPEXISTINGSETS: bool
        TOLERANCE: float
        ...
    class CreaseSetManager(Interface):
        ...
    class CreaseSetMod(Modifier):
        ANGLEA: float
        ANGLEB: float
        ANGLESELECTTYPE: int
        AUTOSELECTNODES: bool
        CREASESETCOLOR: MXSWrapperBase
        CREASESETCREASE: MXSWrapperBase
        CREASESETNAME: MXSWrapperBase
        CREASESETSELECT: MXSWrapperBase
        CREASESETTYPE: MXSWrapperBase
        DISPLAYSETCOLORS: bool
        IGNOREBACKFACING: bool
        KEEPEXISTINGSETS: bool
        TOLERANCE: float
        ...
    class CreateCameraFromView(MAXScriptFunction):
        ...
    class CreateDefaultDaylightSimulationMaterial(MAXScriptFunction):
        ...
    class CreateDialog(Primitive):
        ...
    class CreateLockKey(Primitive):
        ...
    class CreatePreview(Primitive):
        ...
    class CreateValidDaylightSimulationLightCallback(MAXScriptFunction):
        ...
    class Create_Out_Of_Range_Keys(TrackViewUtility):
        ...
    class CrosFade(VideoPostFilter):
        ...
    class CrossSection(Modifier):
        ...
    class Crowd(Helper):
        ASSIGNMENTS: MXSWrapperBase
        BACKTRACKING: bool
        BEHAVIORS: MXSWrapperBase
        COGCONTROLS: MXSWrapperBase
        COLLISIONCOLOR: MXSWrapperBase
        DELETEKEYS: bool
        FLASHING: bool
        FUNCTIONNAME: str
        ICONSIZE: float
        OBJASSOC: MXSWrapperBase
        PRIORITY: MXSWrapperBase
        SAVENTHPOS: int
        SAVENTHROT: int
        SCATTER: MXSWrapperBase
        SCRIPT: None
        SHOWCOLLISIONS: bool
        SIMSTART: int
        SMOOTH: MXSWrapperBase
        SOLVEEND: int
        SOLVEFORBIPEDS: bool
        SOLVESTART: int
        TEAMS: MXSWrapperBase
        UPDATE: bool
        UPDATEFREQUENCY: int
        USEPRIORITIES: bool
        USESCRIPT: bool
        VECTORSCALE: float
        WHENTOSHOWCOLLISIONS: int
        ...
    class CrowdAreaDrawing(Primitive):
        ...
    class CrowdAreaEnd(Primitive):
        ...
    class CrowdAreaEndTools(MAXScriptFunction):
        ...
    class CrowdAreaGetActiveTool(Primitive):
        ...
    class CrowdAreaGetAddMode(Primitive):
        ...
    class CrowdAreaGetBrushSize(Primitive):
        ...
    class CrowdAreaGetBrushSizePath(Primitive):
        ...
    class CrowdAreaGetCircleSides(Primitive):
        ...
    class CrowdAreaGetConstriant(Primitive):
        ...
    class CrowdAreaGetNode(Primitive):
        ...
    class CrowdAreaSetAddMode(Primitive):
        ...
    class CrowdAreaSetBrushSize(Primitive):
        ...
    class CrowdAreaSetBrushSizePath(Primitive):
        ...
    class CrowdAreaSetCircleSides(Primitive):
        ...
    class CrowdAreaSetConstriant(Primitive):
        ...
    class CrowdAreaSetup(Primitive):
        ...
    class CrowdAreaToolToggle(MAXScriptFunction):
        ...
    class CrowdAssignment(ReferenceTarget):
        ACTIVE: bool
        BEHAVIOR: None
        COGCONTROL: None
        DELEGATE: None
        TEAM: None
        WEIGHT: float
        ...
    class CrowdDelegate(Helper):
        ACTIVE: bool
        AVERAGESPEED: float
        BANKPERTURN: float
        BEHAVIORS: MXSWrapperBase
        BIPED: None
        DECLINEACCEL: float
        DECLINEACCELANGLE: float
        DEPTH: float
        DURATION: int
        HEIGHT: float
        INCLINEDECEL: float
        INCLINEDECELANGLE: float
        INDEX: int
        MAXACCEL: float
        MAXBANK: float
        MAXBANKVEL: float
        MAXDECLINE: float
        MAXINCLINE: float
        MAXTURNACCEL: float
        MAXTURNVEL: float
        PRIORITY: int
        RANDID: int
        SHOWCOGSTATES: bool
        SHOWFORCES: bool
        SHOWVELOCITY: bool
        SIMPOS: MXSWrapperBase
        STARTCLIP: int
        STARTFRAME: int
        TURNDECEL: float
        TURNDECELANGLE: float
        USEBIPED: bool
        USEHIERBBOX: bool
        VELOCITYCOLOR: MXSWrapperBase
        WEIGHTS: MXSWrapperBase
        WIDTH: float
        XYCONSTRAIN: bool
        ...
    class CrowdDoRestartPathTool(Primitive):
        ...
    class CrowdGroup(ReferenceTarget):
        MEMBERS: MXSWrapperBase
        NAME: str
        ...
    class CrowdPathDrawing(Primitive):
        ...
    class CrowdPathExtend(Primitive):
        ...
    class CrowdPathSetDefaultWidth(Primitive):
        ...
    class CrowdState(ReferenceTarget):
        BEHAVIORS: MXSWrapperBase
        NAME: str
        TRANSITIONS: MXSWrapperBase
        WEIGHTS: MXSWrapperBase
        ...
    class CrowdTeam(ReferenceTarget):
        MEMBERS: MXSWrapperBase
        NAME: str
        ...
    class CrowdTransition(ReferenceTarget):
        DURATION: int
        EASEIN: float
        EASEOUT: float
        FROM: None
        FUNCTIONNAME: str
        PRIORITY: int
        SCRIPT: None
        TO: None
        ...
    class CtrlUserDataTypeClass(MAXWrapper):
        ...
    class Cubic_Morph_Controller(MorphController):
        ...
    class CurveClass(ReferenceTarget):
        ...
    class CurveControl(ReferenceTarget):
        ...
    class CurveCtlGeneric(Value):
        ...
    class CurvePointsArray(Value):
        ...
    class CustAttrib(MAXWrapper):
        ...
    class CustAttribContainer(ReferenceMaker):
        ...
    class CustomAttributesPresets(AttributeDef):
        ...
    class CustomControlsOptions(Interface):
        ...
    class CustomFileStream(Interface):
        ...
    class CustomSceneStreamManager(Interface):
        ...
    class CylGizmo(Helper):
        HEIGHT: float
        RADIUS: float
        SEED: int
        ...
    class Cylinder(GeometryClass):
        CAPSEGS: int
        HEIGHT: float
        HEIGHTSEGS: int
        MAPCOORDS: bool
        RADIUS: float
        SIDES: int
        SLICE: bool
        SLICEFROM: float
        SLICEON: bool
        SLICETO: float
        SMOOTH: bool
        TYPEINCREATIONMETHOD: int
        TYPEINHEIGHT: float
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS: float
        ...
    class D6Joint(Helper):
        ...
    class DAEEXP(ExporterPlugin):
        ...
    class DAEIMP(ImporterPlugin):
        ...
    class DDS(BitmapIO):
        ...
    class DOFEffect(RenderEffect):
        AFFECTALPHA: bool
        CAMNODEINDEX: int
        FOCALLIMIT: float
        FOCALNODEINDEX: int
        FOCALPOINT: int
        FOCALRANGE: float
        FOCALTYPE: int
        HORIZFOCALLOSS: float
        VERTFOCALLOSS: float
        ...
    class DOSCommand(Primitive):
        ...
    class DSIMDSCC(ScaleController):
        ...
    class DVSPxForm(MAXScriptFunction):
        ...
    class DVSPxFormCam(MAXScriptFunction):
        ...
    class DWF_Exporter(ExporterPlugin):
        ...
    class DWG_Export(ExporterPlugin):
        ...
    class DWG_ExportExporterPlugin(ExporterPlugin):
        ...
    class DYNFUNbakeXFCCtoPRS(MAXScriptFunction):
        ...
    class DYNFUNcolorChangedCallback(MAXScriptFunction):
        ...
    class DYNFUNdisplayEditText(MAXScriptFunction):
        ...
    class DYNFUNdisplayProgressPanel(MAXScriptFunction):
        ...
    class DYNFUNdnColor(MAXScriptFunction):
        ...
    class DYNFUNdnTreeViewStyle(MAXScriptFunction):
        ...
    class DYNFUNdoesFolderExist(MAXScriptFunction):
        ...
    class DYNFUNdynamiteInitialise(MAXScriptFunction):
        ...
    class DYNFUNfilePostMergeCallback(MAXScriptFunction):
        ...
    class DYNFUNfilePostOpenCallback(MAXScriptFunction):
        ...
    class DYNFUNfilePostSaveCallback(MAXScriptFunction):
        ...
    class DYNFUNgetCivilViewCategorizedNodeArrays(MAXScriptFunction):
        ...
    class DYNFUNgetDaylightMembers(MAXScriptFunction):
        ...
    class DYNFUNgetcountrykits(MAXScriptFunction):
        ...
    class DYNFUNgetfiles(MAXScriptFunction):
        ...
    class DYNFUNiniBaseClear(MAXScriptFunction):
        ...
    class DYNFUNiniReadFromFolder(MAXScriptFunction):
        ...
    class DYNFUNinitializeCivilView(MAXScriptFunction):
        ...
    class DYNFUNisVueOrScanlineProductionRenderer(MAXScriptFunction):
        ...
    class DYNFUNlistLibraryMaps(MAXScriptFunction):
        ...
    class DYNFUNloadMapPaths(MAXScriptFunction):
        ...
    class DYNFUNloadVSPnodeCallBacks(MAXScriptFunction):
        ...
    class DYNFUNloadVSPsceneCallBacks(MAXScriptFunction):
        ...
    class DYNFUNmakeCivilViewSurfaces(MAXScriptFunction):
        ...
    class DYNFUNmakeCivilViewVehicles(MAXScriptFunction):
        ...
    class DYNFUNmakeResourceKitStructure(MAXScriptFunction):
        ...
    class DYNFUNmaxBakingControl(MAXScriptFunction):
        ...
    class DYNFUNmaxXForm(MAXScriptFunction):
        ...
    class DYNFUNmaxXformCam(MAXScriptFunction):
        ...
    class DYNFUNnodeCreatedCallback(MAXScriptFunction):
        ...
    class DYNFUNnodeRenamedCallback(MAXScriptFunction):
        ...
    class DYNFUNnormalizeMenuName(MAXScriptFunction):
        ...
    class DYNFUNpostImportCallback(MAXScriptFunction):
        ...
    class DYNFUNpostRendererChangeCallback(MAXScriptFunction):
        ...
    class DYNFUNpreSystemShutdownCallback(MAXScriptFunction):
        ...
    class DYNFUNrebuildExplorerTreeNodes(MAXScriptFunction):
        ...
    class DYNFUNremoveCSProllouts(MAXScriptFunction):
        ...
    class DYNFUNremoveCivilViewFromMainMenu(MAXScriptFunction):
        ...
    class DYNFUNresetEnvironmentMap(MAXScriptFunction):
        ...
    class DYNFUNresetFogParams(MAXScriptFunction):
        ...
    class DYNFUNresetXformControllers(MAXScriptFunction):
        ...
    class DYNFUNsceneRedoCallback(MAXScriptFunction):
        ...
    class DYNFUNsceneUndoCallback(MAXScriptFunction):
        ...
    class DYNFUNselectedNodesPostDeleteCallback(MAXScriptFunction):
        ...
    class DYNFUNselectedNodesPreDeleteCallback(MAXScriptFunction):
        ...
    class DYNFUNsetCountryPaths(MAXScriptFunction):
        ...
    class DYNFUNsetUpMaterialLibraries(MAXScriptFunction):
        ...
    class DYNFUNsetupRootNode(MAXScriptFunction):
        ...
    class DYNFUNsystemPostNewCallback(MAXScriptFunction):
        ...
    class DYNFUNsystemPostResetCallback(MAXScriptFunction):
        ...
    class DYNFUNupdateExplorer(MAXScriptFunction):
        ...
    class DYNFUNupperCase(MAXScriptFunction):
        ...
    class DYNFUNviewportSetup(MAXScriptFunction):
        ...
    class DYNFUNvizXform(MAXScriptFunction):
        ...
    class DYNFUNvizXformCam(MAXScriptFunction):
        ...
    class DYNINIendMarkerColor(Color):
        ...
    class DYNINIgreyedOutColor(Color):
        ...
    class DYNINIhighlightColor(Color):
        ...
    class DYNINImarkingColor(Color):
        ...
    class DYNINIspeedValue(Point2):
        ...
    class DYNINIstartMarkerColor(Color):
        ...
    class DYNXFCCM3(Matrix3Controller):
        ...
    class DYNglobalShiftCustomAttributes(AttributeDef):
        ...
    class DYNimportCatsArray(Array):
        ...
    class DYNimportSuperClassArray(Array):
        ...
    class DYNobjHandles(Array):
        ...
    class DYNrootNodeStore(AttributeDef):
        ...
    class DYNsightToolFont(Array):
        ...
    class DYNuiResourcesCivilViewGlobal(Array):
        ...
    class DYNuiResourcesCvExplorer(Array):
        ...
    class DYNuiResourcesObjClasses(Array):
        ...
    class DYNwheelRotationControllerAttributes(AttributeDef):
        ...
    class DaeExporter(ExporterPlugin):
        ...
    class DaeImporter(ImporterPlugin):
        ...
    class Damper(GeometryClass):
        BASE_STUD_DIAMETER: float
        BASE_STUD_HEIGHT: float
        BOOT_FOLDS: int
        BOOT_FOLD_RESOLUTION: int
        BOOT_LARGE_DIAMETER: float
        BOOT_SIDES: int
        BOOT_SMALL_DIAMETER: float
        BOOT_STOP_DIAMETER: float
        BOOT_STOP_FILLET: float
        BOOT_STOP_FILLET_SEGEMENTS: int
        BOOT_STOP_HEIGHT: float
        BOOT_STOP_SETBACK: float
        CYLINDER_DIAMETER: float
        CYLINDER_FILLET_1: float
        CYLINDER_FILLET_1_SEGMENTS: int
        CYLINDER_FILLET_2: float
        CYLINDER_FILLET_2_SEGMENTS: int
        CYLINDER_HEIGHT: float
        CYLINDER_SIDES: int
        DAMPER_DIRECTION: int
        DRAG: float
        DRAG_UNITS: int
        DYNAMICS_OBJECT_TYPE: int
        ENABLE_BOOT: int
        END_PLACEMENT_METHOD: int
        FORCE: float
        FORCE_UNITS: int
        FREE_DAMPER_HEIGHT: float
        GENERATE_MAPPING_COORDINATES: int
        INSIDE_DIAMETER: float
        PISTON_DIAMETER: float
        PISTON_HEIGHT: float
        PISTON_SIDES: int
        RENDERABLE_SPRING: int
        SMOOTH_BOOT: int
        SMOOTH_CYLINDER: int
        SMOOTH_PISTON: int
        ...
    class DataChannelModifier(Modifier):
        DEBUGINFO: bool
        DISPLAY: bool
        FLOATDISPLAY: int
        MAXCOLOR: MXSWrapperBase
        MIDCOLOR: MXSWrapperBase
        MINCOLOR: MXSWrapperBase
        NORMALIZEDISPLAY: bool
        NUMERIC_DRAWDIST: int
        NUMERIC_MAX: int
        OPERATORS: MXSWrapperBase
        OPERATOR_ENABLED: MXSWrapperBase
        OPERATOR_FROZEN: MXSWrapperBase
        OPERATOR_OPS: MXSWrapperBase
        OPERATOR_ORDER: MXSWrapperBase
        POINT3DISPLAY: int
        SHOWNUMERICDATA: bool
        TICKSIZE: int
        ...
    class DataOpDeleteCatcher(ReferenceTarget):
        ...
    class DataOperIcon(Helper):
        ACTIVITY_TYPE: int
        ANIMATABLE_ACTIVE: bool
        AUTO_UPDATE: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        COLOR_COORDINATED: bool
        DEFAULT_HEIGHT: int
        DEFAULT_OFFSET: int
        DEFAULT_RANGE_MAX: float
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_TYPE: int
        DEFAULT_WIDTH: int
        ENABLE_BY_SWITCH: bool
        GROUPS: MXSWrapperBase
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        ICON_TYPE: int
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_DIVIDER: int
        PDVIEW_HEIGHT: int
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_SHOW_PARAMETERS: bool
        PDVIEW_WIDTH: int
        REPEATS: int
        SELECTED_SUBOPERATORS: MXSWrapperBase
        SUBOPERATORS: MXSWrapperBase
        TIME_OFF: int
        TIME_ON: int
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        VISIBLE_ICON: bool
        ...
    class DataOperator(Helper):
        ACTIVITY_TYPE: int
        ANIMATABLE_ACTIVE: bool
        AUTO_UPDATE: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        COLOR_COORDINATED: bool
        DEFAULT_HEIGHT: int
        DEFAULT_OFFSET: int
        DEFAULT_RANGE_MAX: float
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_TYPE: int
        DEFAULT_WIDTH: int
        ENABLE_BY_SWITCH: bool
        GROUPS: MXSWrapperBase
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        ICON_TYPE: int
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_DIVIDER: int
        PDVIEW_HEIGHT: int
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_SHOW_PARAMETERS: bool
        PDVIEW_WIDTH: int
        REPEATS: int
        SELECTED_SUBOPERATORS: MXSWrapperBase
        SUBOPERATORS: MXSWrapperBase
        TIME_OFF: int
        TIME_ON: int
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        VISIBLE_ICON: bool
        ...
    class DataPair(Value):
        ...
    class DataTest(Helper):
        ACTIVITY_TYPE: int
        ANIMATABLE_ACTIVE: bool
        AUTO_UPDATE: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        COLOR_COORDINATED: bool
        DEFAULT_HEIGHT: int
        DEFAULT_OFFSET: int
        DEFAULT_RANGE_MAX: float
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_TYPE: int
        DEFAULT_WIDTH: int
        ENABLE_BY_SWITCH: bool
        GROUPS: MXSWrapperBase
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        ICON_TYPE: int
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_DIVIDER: int
        PDVIEW_HEIGHT: int
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_SHOW_PARAMETERS: bool
        PDVIEW_WIDTH: int
        REPEATS: int
        SELECTED_SUBOPERATORS: MXSWrapperBase
        SUBOPERATORS: MXSWrapperBase
        TIME_OFF: int
        TIME_ON: int
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        VISIBLE_ICON: bool
        ...
    class DataTestIcon(Helper):
        ACTIVITY_TYPE: int
        ANIMATABLE_ACTIVE: bool
        AUTO_UPDATE: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        COLOR_COORDINATED: bool
        DEFAULT_HEIGHT: int
        DEFAULT_OFFSET: int
        DEFAULT_RANGE_MAX: float
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_TYPE: int
        DEFAULT_WIDTH: int
        ENABLE_BY_SWITCH: bool
        GROUPS: MXSWrapperBase
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        ICON_TYPE: int
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_DIVIDER: int
        PDVIEW_HEIGHT: int
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_SHOW_PARAMETERS: bool
        PDVIEW_WIDTH: int
        REPEATS: int
        SELECTED_SUBOPERATORS: MXSWrapperBase
        SUBOPERATORS: MXSWrapperBase
        TIME_OFF: int
        TIME_ON: int
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        VISIBLE_ICON: bool
        ...
    class DataViewGroup(ReferenceTarget):
        ...
    class Data_Icon(Helper):
        ACTIVITY_TYPE: int
        ANIMATABLE_ACTIVE: bool
        AUTO_UPDATE: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        COLOR_COORDINATED: bool
        DEFAULT_HEIGHT: int
        DEFAULT_OFFSET: int
        DEFAULT_RANGE_MAX: float
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_TYPE: int
        DEFAULT_WIDTH: int
        ENABLE_BY_SWITCH: bool
        GROUPS: MXSWrapperBase
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        ICON_TYPE: int
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_DIVIDER: int
        PDVIEW_HEIGHT: int
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_SHOW_PARAMETERS: bool
        PDVIEW_WIDTH: int
        REPEATS: int
        SELECTED_SUBOPERATORS: MXSWrapperBase
        SUBOPERATORS: MXSWrapperBase
        TIME_OFF: int
        TIME_ON: int
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        VISIBLE_ICON: bool
        ...
    class Data_Operator(Helper):
        ACTIVITY_TYPE: int
        ANIMATABLE_ACTIVE: bool
        AUTO_UPDATE: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        COLOR_COORDINATED: bool
        DEFAULT_HEIGHT: int
        DEFAULT_OFFSET: int
        DEFAULT_RANGE_MAX: float
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_TYPE: int
        DEFAULT_WIDTH: int
        ENABLE_BY_SWITCH: bool
        GROUPS: MXSWrapperBase
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        ICON_TYPE: int
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_DIVIDER: int
        PDVIEW_HEIGHT: int
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_SHOW_PARAMETERS: bool
        PDVIEW_WIDTH: int
        REPEATS: int
        SELECTED_SUBOPERATORS: MXSWrapperBase
        SUBOPERATORS: MXSWrapperBase
        TIME_OFF: int
        TIME_ON: int
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        VISIBLE_ICON: bool
        ...
    class Data_Test(Helper):
        ACTIVITY_TYPE: int
        ANIMATABLE_ACTIVE: bool
        AUTO_UPDATE: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        COLOR_COORDINATED: bool
        DEFAULT_HEIGHT: int
        DEFAULT_OFFSET: int
        DEFAULT_RANGE_MAX: float
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_TYPE: int
        DEFAULT_WIDTH: int
        ENABLE_BY_SWITCH: bool
        GROUPS: MXSWrapperBase
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        ICON_TYPE: int
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_DIVIDER: int
        PDVIEW_HEIGHT: int
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_SHOW_PARAMETERS: bool
        PDVIEW_WIDTH: int
        REPEATS: int
        SELECTED_SUBOPERATORS: MXSWrapperBase
        SUBOPERATORS: MXSWrapperBase
        TIME_OFF: int
        TIME_ON: int
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        VISIBLE_ICON: bool
        ...
    class Daylight(System):
        ...
    class DaylightAssemblyHead(Helper):
        ...
    class DaylightSimulationUIOps(Interface):
        ...
    class DaylightSimulationUtilities(Interface):
        ...
    class DaylightSystemFactory(Interface):
        ...
    class DaylightSystemFactory2(Interface):
        ...
    class Daylight_Slave_Controller(Matrix3Controller):
        ...
    class Daylight_Slave_Intensity_Controller(FloatController):
        ...
    class DeSelectNode(Primitive):
        ...
    class DeactivateTimeWarp(BipedGeneric):
        ...
    class DefaultLightWorldGenFragment(GraphicsFragmentPlugin):
        ...
    class DefaultParamInterface(Interface):
        ...
    class DefaultScanlineRenderer(RendererClass):
        ...
    class DefaultSource(ReferenceTarget):
        ...
    class Default_Color_Picker(ColorPicker):
        ...
    class Default_Scanline_Renderer(RendererClass):
        ...
    class Default_Sound(SoundClass):
        ...
    class Deflector(SpacewarpObject):
        BOUNCE: float
        CHAOS: float
        FRICTION: float
        INHERITVELOCITY: float
        LENGTH: float
        VARIATION: float
        WIDTH: float
        ...
    class Deflectorbinding(SpacewarpModifier):
        ...
    class Deform_Curve(ReferenceMaker):
        ...
    class Deformable_GPoly(GeometryClass):
        ...
    class DegToRad(Primitive):
        ...
    class Delegate(Helper):
        ACTIVE: bool
        AVERAGESPEED: float
        BANKPERTURN: float
        BEHAVIORS: MXSWrapperBase
        BIPED: None
        DECLINEACCEL: float
        DECLINEACCELANGLE: float
        DEPTH: float
        DURATION: int
        HEIGHT: float
        INCLINEDECEL: float
        INCLINEDECELANGLE: float
        INDEX: int
        MAXACCEL: float
        MAXBANK: float
        MAXBANKVEL: float
        MAXDECLINE: float
        MAXINCLINE: float
        MAXTURNACCEL: float
        MAXTURNVEL: float
        PRIORITY: int
        RANDID: int
        SHOWCOGSTATES: bool
        SHOWFORCES: bool
        SHOWVELOCITY: bool
        SIMPOS: MXSWrapperBase
        STARTCLIP: int
        STARTFRAME: int
        TURNDECEL: float
        TURNDECELANGLE: float
        USEBIPED: bool
        USEHIERBBOX: bool
        VELOCITYCOLOR: MXSWrapperBase
        WEIGHTS: MXSWrapperBase
        WIDTH: float
        XYCONSTRAIN: bool
        ...
    class DeleteMesh(Modifier):
        ...
    class DeleteParticles(Helper):
        LIFE_SPAN: int
        RANDOM_SEED: int
        TYPE: int
        VARIATION: int
        ...
    class DeletePatch(Modifier):
        ...
    class DeleteSplineModifier(Modifier):
        ...
    class DeleteTw(BipedGeneric):
        ...
    class DeleteWeight(BipedGeneric):
        ...
    class Dent(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COORDS: MXSWrapperBase
        ITERATIONS: int
        MAP1: None
        MAP1ENABLED: bool
        MAP2: None
        MAP2ENABLED: bool
        SIZE: float
        STRENGTH: float
        ...
    class DepthFragment(GraphicsFragmentPlugin):
        ...
    class Depth_Of_Field(RenderEffect):
        AFFECTALPHA: bool
        CAMNODEINDEX: int
        FOCALLIMIT: float
        FOCALNODEINDEX: int
        FOCALPOINT: int
        FOCALRANGE: float
        FOCALTYPE: int
        HORIZFOCALLOSS: float
        VERTFOCALLOSS: float
        ...
    class Depth_Of_FieldMPassCamEffect(MPassCamEffect):
        DISABLEANTIALIASING: bool
        DISABLEFILTERING: bool
        DISPLAYPASSES: bool
        DITHERSTRENGTH: float
        FOCALDEPTH: float
        NORMALIZEWEIGHTS: bool
        SAMPLEBIAS: float
        SAMPLERADIUS: float
        TILESIZE: int
        TOTALPASSES: int
        USEORIGINALLOCATION: bool
        USETARGETDISTANCE: bool
        ...
    class DeselectHiddenEdges(Primitive):
        ...
    class DeselectHiddenFaces(Primitive):
        ...
    class DestroyDialog(Primitive):
        ...
    class DialogMonitor(GlobalUtilityPlugin):
        ...
    class DialogMonitorOPS(Interface):
        ...
    class Dictionary(Value):
        ...
    class Diffuse(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        LIGHTINGON: bool
        ...
    class DigitData(ReferenceTarget):
        ...
    class DigitDataFloatController(FloatController):
        ...
    class DigitSegTrans(Matrix3Controller):
        ...
    class DirectX_9_Shader(Material):
        EFFECTFILE: str
        ENGINERESOURCE: None
        PARENTMATERIAL: None
        PRESETMATERIAL: int
        RENDERENABLED: bool
        RENDERMATERIAL: MXSWrapperBase
        SHADERFXGRAPH: None
        TECHNIQUE: int
        USESHADERFX: int
        ...
    class DirectX_9_ShaderReferenceTarget(ReferenceTarget):
        ...
    class Directionallight(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ASPECT: float
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        ATTENDECAY: int
        CASTSHADOWS: bool
        COLOR: MXSWrapperBase
        CONESHAPE: int
        CONTRAST: float
        DECAYRADIUS: float
        ENABLED: bool
        EXCLUDELIST: MXSWrapperBase
        FALLOFF: float
        FARATTENEND: float
        FARATTENSTART: float
        HOTSPOT: float
        HSV: MXSWrapperBase
        HUE: int
        INCLEXCLTYPE: int
        INCLUDELIST: None
        LIGHTAFFECTSSHADOW: bool
        LIGHTSHAPE: int
        MULTIPLIER: float
        NEARATTENEND: float
        NEARATTENSTART: float
        ON: bool
        OVERSHOOT: bool
        PROJECTOR: bool
        PROJECTORMAP: None
        RAYTRACEDSHADOWS: bool
        RGB: MXSWrapperBase
        SATURATION: int
        SHADOWCOLOR: MXSWrapperBase
        SHADOWGENERATOR: MXSWrapperBase
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHOWCONE: bool
        SHOWFARATTEN: bool
        SHOWNEARATTEN: bool
        SOFTENDIFFUSEEDGE: float
        TYPE: MXSWrapperBase
        USEFARATTEN: bool
        USEGLOBALSHADOWSETTINGS: bool
        USENEARATTEN: bool
        USESHADOWPROJECTORMAP: bool
        VALUE: int
        ...
    class DisableSceneRedraw(Primitive):
        ...
    class DisableStatusXYZ(Primitive):
        ...
    class DiscreetRadiosityMaterial(Material):
        BASEMATERIAL: MXSWrapperBase
        BUMPSCALE: float
        COLORBLEED: float
        LUMINANCESCALE: float
        REFLECTANCESCALE: float
        TRANSMITTANCESCALE: float
        ...
    class Discreet_Radiosity(RadiosityEffect):
        CONTRASTTHRESHOLD: float
        ELAPSEDTIME: int
        INCLUDEAREALIGHTS: bool
        INCLUDELINEARLIGHTS: bool
        INCLUDEPOINTLIGHTS: bool
        INCLUDESELFEMITTINGLIGHTS: bool
        INCLUDESKYLIGHT: bool
        INITIALMESHSIZE: float
        LIGHTPAINTINGINTENSITY: float
        LIGHTPAINTINGPRESSURE: float
        LIGHTUNITSUSED: int
        MESHINGENABLED: bool
        MESHINGSIZE: float
        MINIMUMMESHSIZE: float
        MINIMUMSELFEMITTINGSIZE: float
        RADDIRECTFILTERING: int
        RADDISPLAYINVIEWPORT: bool
        RADFILTERING: int
        RADGLOBALREFINESTEPS: int
        RADINITIALQUALITY: float
        RADPROCESSINRENDERONLY: bool
        RADPROCESSOBJECTREFINESTEPS: bool
        RADSELECTIONREFINESTEPS: int
        RMADAPTIVEENABLED: bool
        RMCLAMPENABLED: bool
        RMCLAMPVALUE: float
        RMFILTERRADIUS: float
        RMMINSAMPLESPACING: int
        RMRAYSPERSAMPLE: int
        RMREGATHER: bool
        RMREUSEDIRECTILLUMINATION: bool
        RMSAMPLESPACING: int
        RMSHOWSAMPLES: bool
        RMSUBDIVISIONCONTRAST: float
        SHOOTDIRECTLIGHTS: bool
        STATMESHSIZE: float
        STATNUMFACES: int
        STATNUMGEOMOBJECTS: int
        STATNUMLIGHTOBJECTS: int
        STATREFINEITERATIONS: int
        STATSOLUTIONQUALITY: float
        USEADAPTIVEMESHING: bool
        ...
    class Discretizator(ReferenceTarget):
        BASE_ANGLE: float
        BASE_FLOAT: float
        BASE_INTEGER: int
        BASE_PERCENT: float
        BASE_TIME: int
        BASE_WORLD: float
        FILTER: None
        INPUT: None
        STEP_ANGLE: float
        STEP_FLOAT: float
        STEP_INTEGER: int
        STEP_PERCENT: float
        STEP_TIME: int
        STEP_WORLD: float
        TYPE: int
        UNITS_PER_TYPE: int
        USE_AS_SPEED_OR_SPIN_RATE: bool
        ...
    class Disp_Approx(Modifier):
        ...
    class Displace(Modifier):
        APPLYMAP: bool
        AXIS: int
        BITMAP: None
        BLUR: float
        CAP: bool
        DECAY: float
        HEIGHT: float
        LENGTH: float
        LUMCENTER: float
        LUMCENTERENABLE: bool
        MAP: None
        MAPTYPE: int
        MAP_CHANNEL: int
        MAP_OR_VERTEX_COLOR: int
        STRENGTH: float
        USEMAP: bool
        U_FLIP: bool
        U_TILE: float
        V_FLIP: bool
        V_TILE: float
        WIDTH: float
        W_FLIP: bool
        W_TILE: float
        ...
    class Displace_Mesh(SpacewarpModifier):
        ...
    class Displace_NURBS(SpacewarpModifier):
        ...
    class Displacebinding(SpacewarpModifier):
        ...
    class DisplayAdaptiveDegradeResultFragment(GraphicsFragmentPlugin):
        ...
    class DisplayCulling(UtilityPlugin):
        ...
    class DisplayData(Helper):
        ADD_PREFIX: bool
        COLOR: MXSWrapperBase
        COMPLEX_SHOW_AS: int
        DATA_CHANNEL: None
        DATA_HANDLE: int
        EXECUTION_ORDER: int
        FILTER_TYPE: int
        GROUP_SELECTION: None
        MATRIX_SHOW_AS: int
        OFFSET_INOUT: int
        OFFSET_LEFTRIGHT: int
        OFFSET_UPDOWN: int
        PAIR_SHOW_AS: int
        PRECISION: int
        PREFIX_TEXT: str
        QUATERNION_SHOW_AS: int
        RATE_VALUE: bool
        REAL_SHOW_AS: int
        SHOW_NUMBERING: bool
        UNITS_PER_TYPE: int
        VECTOR_SHOW_AS: int
        ...
    class DisplayManager(Interface):
        ...
    class DisplayParticles(Helper):
        COLOR: MXSWrapperBase
        SELECTED_TYPE: int
        SHOW_NUMBERING: bool
        TYPE: int
        VISIBLE: float
        ...
    class DisplayScriptParticles(Helper):
        ADD_PREFIX: bool
        COLOR: MXSWrapperBase
        EXECUTION_ORDER: int
        FILTER_TYPE: int
        GROUP_SELECTION: None
        OFFSET_INOUT: int
        OFFSET_LEFTRIGHT: int
        OFFSET_UPDOWN: int
        PRECISION: int
        PREFIX_TEXT: str
        SCRIPT_DATA_TYPE: int
        SHOW_NUMBERING: bool
        ...
    class DisplayTempPrompt(Primitive):
        ...
    class Display_Script(Helper):
        ADD_PREFIX: bool
        COLOR: MXSWrapperBase
        EXECUTION_ORDER: int
        FILTER_TYPE: int
        GROUP_SELECTION: None
        OFFSET_INOUT: int
        OFFSET_LEFTRIGHT: int
        OFFSET_UPDOWN: int
        PRECISION: int
        PREFIX_TEXT: str
        SCRIPT_DATA_TYPE: int
        SHOW_NUMBERING: bool
        ...
    class DoesSelectedContainInterface(MAXScriptFunction):
        ...
    class Donut(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        MAPCOORDS: bool
        OPTIMIZE: bool
        QUAD_CAP: bool
        RADIUS1: float
        RADIUS2: float
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        ...
    class Double(Value):
        ...
    class DoublePacket(ReferenceMaker):
        ...
    class DoubleSided(Material):
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        MATERIAL1: MXSWrapperBase
        MATERIAL2: MXSWrapperBase
        TRANSLUCENCY: float
        ...
    class Drag(SpacewarpObject):
        DAMPINGAX: float
        DAMPINGC: float
        DAMPINGGC: float
        DAMPINGR: float
        DAMPINGRC: float
        DAMPINGX: float
        DAMPINGY: float
        DAMPINGZ: float
        FALLOFFAX: float
        FALLOFFC: float
        FALLOFFGC: float
        FALLOFFR: float
        FALLOFFRC: float
        FALLOFFX: float
        FALLOFFY: float
        FALLOFFZ: float
        ICONSIZE: float
        RANGEAX: float
        RANGEC: float
        RANGEGC: float
        RANGELESS: bool
        RANGER: float
        RANGERC: float
        RANGEX: float
        RANGEY: float
        RANGEZ: float
        SYMMETRY: int
        TIMEOFF: MXSWrapperBase
        TIMEON: MXSWrapperBase
        ...
    class DragMod(SpacewarpModifier):
        ...
    class Dummy(Helper):
        BOXSIZE: MXSWrapperBase
        ...
    class DummyBitmapFilterClass(BitmapFilterClass):
        ...
    class DummyRadMapClass(ReferenceTarget):
        ...
    class DwfExportPreferences(Interface):
        ...
    class DwgAlwaysEqualFilter(ReferenceMaker):
        ...
    class DwgBlockDefinitionFilter(ReferenceMaker):
        ...
    class DwgBlockInsAsNodeHierarchyFilter(ReferenceMaker):
        ...
    class DwgBlockInsertFilter(ReferenceMaker):
        ...
    class DwgCameraPacket(ReferenceMaker):
        ...
    class DwgColorFilter(ReferenceMaker):
        ...
    class DwgColorMaterialPacket(ReferenceMaker):
        ...
    class DwgColorSplitByMaterialFilter(ReferenceMaker):
        ...
    class DwgEnhColorPacket(ReferenceMaker):
        ...
    class DwgEnhLayerPacket(ReferenceMaker):
        ...
    class DwgEnhancedLayerFilter(ReferenceMaker):
        ...
    class DwgEntityPacket(ReferenceMaker):
        ...
    class DwgExtrusionFilter(ReferenceMaker):
        ...
    class DwgExtrusionPacket(ReferenceMaker):
        ...
    class DwgFactory(ReferenceMaker):
        ...
    class DwgFilterList(ReferenceMaker):
        ...
    class DwgGridPacket(ReferenceMaker):
        ...
    class DwgHandleFilter(ReferenceMaker):
        ...
    class DwgLayerFilter(ReferenceMaker):
        ...
    class DwgLayerTable(ReferenceTarget):
        ...
    class DwgLightPacket(ReferenceMaker):
        ...
    class DwgMaterialFilter(ReferenceMaker):
        ...
    class DwgMaterialFilterReferenceMaker(ReferenceMaker):
        ...
    class DwgMaterialPacket(ReferenceMaker):
        ...
    class DwgMaterialPacketReferenceMaker(ReferenceMaker):
        ...
    class DwgPluginTranslatorForwardingFilter(ReferenceMaker):
        ...
    class DwgPointTrans(ReferenceMaker):
        ...
    class DwgSunPacket(ReferenceMaker):
        ...
    class DwgTableEntryPacket(ReferenceMaker):
        ...
    class DwgTableRecord(ReferenceMaker):
        ...
    class DxMaterial(Material):
        CALCULATEBITANGENTPERPIXEL: bool
        EFFECTFILE: str
        ENGINERESOURCE: None
        G_ADDVERTEXCOLOR: bool
        G_ALPHAVERTEX: bool
        G_AMBIENTOCCENABLE: bool
        G_AMBIENTOCCTEXTURE: None
        G_BOTTOMDIFFUSEENABLE: bool
        G_BOTTOMTEXTURE: None
        G_BOTTOMTEXTUREMAPCHANNEL: int
        G_BUMPSCALE: float
        G_FLIPGREEN: bool
        G_NORMALENABLE: bool
        G_NORMALTEXTURE: None
        G_PARALLAXBIAS: float
        G_PARALLAXSCALE: float
        G_REFLECTAMOUNT: float
        G_REFLECTIONENABLE: bool
        G_REFLECTIONTEXTURE: None
        G_SPECULARENABLE: bool
        G_SPECULARTEXTURE: None
        G_TOPDIFFUSEENABLE: bool
        G_TOPTEXTURE: None
        G_TOPTEXTUREMAPCHANNEL: int
        G_USEPARALLAX: bool
        K_A: MXSWrapperBase
        K_D: MXSWrapperBase
        K_S: MXSWrapperBase
        LAMP0POS: int
        N: int
        ORTHOGONALIZETANGENTBITANGENTPERPIXEL: bool
        PARENTMATERIAL: None
        PRESETMATERIAL: int
        RENDERENABLED: bool
        RENDERMATERIAL: MXSWrapperBase
        SHADERFXGRAPH: None
        TECHNIQUE: int
        USEMIKKT: bool
        USESHADERFX: int
        ...
    class DynBuilding(Modifier):
        XAMOUNT: float
        XCAPEND: bool
        XCAPSTART: bool
        XCAPTYPE: int
        XFLOORS: int
        XMAPCOORDS: bool
        XMAPTYPE: int
        XMAPWIDTH: float
        XMATIDS: bool
        XOUTPUT: int
        XREALWORLDMAPSIZE: bool
        XSEGS: int
        XSMOOTH: bool
        XUSESHAPEIDS: bool
        XWALLMATIDS: int
        ...
    class DynDiv(Modifier):
        ...
    class DynGRail(Modifier):
        ...
    class DynLXCollapse(Primitive):
        ...
    class DynLXGetDVSPNodeArrays(Primitive):
        ...
    class DynLXGetDVSPNodeArraysNoPF(Primitive):
        ...
    class DynLXGetNodesByAppData(Primitive):
        ...
    class DynLXSplineInterp(Primitive):
        ...
    class DynLXSplineInterpCam(Primitive):
        ...
    class DynMarks(Modifier):
        ...
    class DynSMesh(Modifier):
        ...
    class DynSOS(SpacewarpModifier):
        ...
    class DynXFCC(Matrix3Controller):
        ...
    class DynXFCCV3(Matrix3Controller):
        ...
    class EPS_Image(BitmapIO):
        ...
    class EPolyManipGrip(Interface):
        ...
    class Ease(FloatController):
        ...
    class EdgeSelection(Value):
        ...
    class EditAtmosphere(Primitive):
        ...
    class EditNormals(Modifier):
        DISPLAYLENGTH: float
        IGNOREBACKFACING: bool
        SELECTBY: int
        SHOWHANDLES: bool
        ...
    class EditPolyMod(Modifier):
        AFFECTBACKFACING: bool
        ALIGNPLANENORMAL: MXSWrapperBase
        ALIGNPLANEOFFSET: float
        ALIGNTYPE: int
        ANIMATIONMODE: int
        AUTOSMOOTHTHRESHOLD: float
        BEVELFACEBIAS: float
        BEVELHEIGHT: float
        BEVELOUTLINE: float
        BEVELTYPE: int
        BREAKDISTANCE: float
        BRIDGEBIAS: float
        BRIDGEEDGEADJACENT: float
        BRIDGEREVERSETRIANGLE: int
        BRIDGESEGMENTS: int
        BRIDGESELECTED: int
        BRIDGESMOOTHTHRESHOLD: float
        BRIDGETAPER: float
        BRIDGETARGET1: int
        BRIDGETARGET2: int
        BRIDGETWIST1: int
        BRIDGETWIST2: int
        BUBBLE: float
        CAGECOLOR: MXSWrapperBase
        CHAMFEREDGEAMOUNT: float
        CHAMFEREDGEOPEN: bool
        CHAMFERVERTEXAMOUNT: float
        CHAMFERVERTEXDEPTH: float
        CHAMFERVERTEXOPEN: bool
        CHAMFERVERTEXSEGMENTS: int
        CHAMFERVERTEXSMOOTH: bool
        CHAMFERVERTEXSMOOTHTHRESHOLD: float
        CHAMFERVERTEXSMOOTHTYPE: int
        CONNECTEDGEPINCH: int
        CONNECTEDGESEGMENTS: int
        CONNECTEDGESLIDE: int
        CONSTRAINTYPE: int
        CURRENTOPERATION: int
        DATACHANNEL: int
        DATAVALUE: float
        DELETEISOLATEDVERTS: bool
        EDGECHAMFERDEPTH: float
        EDGECHAMFERENDBIAS: float
        EDGECHAMFERINVERT: bool
        EDGECHAMFERMITERINGTYPE: int
        EDGECHAMFERQUADINTERSECTIONSOBSOLETE: bool
        EDGECHAMFERRADIALBIAS: float
        EDGECHAMFERSEGMENTS: int
        EDGECHAMFERSMOOTH: bool
        EDGECHAMFERSMOOTHTHRESHOLD: float
        EDGECHAMFERSMOOTHTYPE: int
        EDGECHAMFERTENSION: float
        EDGECHAMFERTYPEOBSOLETE: int
        EXTRUDEALONGSPLINEALIGN: bool
        EXTRUDEALONGSPLINENODE: None
        EXTRUDEALONGSPLINEROTATION: float
        EXTRUDEALONGSPLINESEGMENTS: int
        EXTRUDEALONGSPLINETAPER: float
        EXTRUDEALONGSPLINETAPERCURVE: float
        EXTRUDEALONGSPLINETWIST: float
        EXTRUDEEDGEHEIGHT: float
        EXTRUDEEDGEWIDTH: float
        EXTRUDEFACEBIAS: float
        EXTRUDEFACEHEIGHT: float
        EXTRUDEFACETYPE: int
        EXTRUDEVERTEXHEIGHT: float
        EXTRUDEVERTEXWIDTH: float
        FALLOFF: float
        HARDEDGEDISPLAY: int
        HARDEDGEDISPLAYCOLOR: MXSWrapperBase
        HINGEANGLE: float
        HINGEBASE: MXSWrapperBase
        HINGEDIRECTION: MXSWrapperBase
        HINGESEGMENTS: int
        IGNOREBACKFACING: bool
        INSETAMOUNT: float
        INSETTYPE: int
        LASTDELTAINDEX: int
        LOCKSOFTSEL: bool
        MATERIALIDTOSET: int
        OUTLINEAMOUNT: float
        PAINTDEFORMAXIS: int
        PAINTDEFORMMODE: int
        PAINTDEFORMSIZE: float
        PAINTDEFORMSTRENGTH: float
        PAINTDEFORMVALUE: float
        PAINTSELMODE: int
        PAINTSELSIZE: float
        PAINTSELSTRENGTH: float
        PAINTSELVALUE: float
        PINCH: float
        PRESERVEUVS: bool
        RELAXAMOUNT: float
        RELAXHOLDBOUNDARYPOINTS: bool
        RELAXHOLDOUTERPOINTS: bool
        RELAXITERATIONS: int
        REMVEEDGECTRLKEY: bool
        SELECTANGLE: float
        SELECTBYANGLE: bool
        SELECTBYMATERIALCLEAR: bool
        SELECTBYMATERIALID: int
        SELECTBYSMOOTHINGGROUP: int
        SELECTBYSMOOTHINGGROUPCLEAR: bool
        SELECTBYVERTEX: bool
        SELECTEDCAGECOLOR: MXSWrapperBase
        SELECTMODE: int
        SEPARATEBYMATERIAL: bool
        SEPARATEBYSMOOTHING: bool
        SHOWCAGE: bool
        SMOOTHINGGROUPSTOCLEAR: int
        SMOOTHINGGROUPSTOSET: int
        SMOOTHNESS: float
        SPLIT: bool
        SSEDGEDIST: int
        SSUSEEDGEDIST: bool
        TESSELLATEBYFACE: int
        TESSTENSION: float
        USESOFTSEL: bool
        USESTACKSELECTION: bool
        WELDEDGETHRESHOLD: float
        WELDVERTEXTHRESHOLD: float
        WORLDTOOBJECTTRANSFORM: MXSWrapperBase
        ...
    class EditPolyModReadyToBridge(Primitive):
        ...
    class EditRenderRegion(Interface):
        ...
    class EditTextControl(RolloutControl):
        ...
    class Edit_Mesh(Modifier):
        ...
    class Edit_Normals(Modifier):
        DISPLAYLENGTH: float
        IGNOREBACKFACING: bool
        SELECTBY: int
        SHOWHANDLES: bool
        ...
    class Edit_Patch(Modifier):
        ...
    class Edit_Poly(Modifier):
        AFFECTBACKFACING: bool
        ALIGNPLANENORMAL: MXSWrapperBase
        ALIGNPLANEOFFSET: float
        ALIGNTYPE: int
        ANIMATIONMODE: int
        AUTOSMOOTHTHRESHOLD: float
        BEVELFACEBIAS: float
        BEVELHEIGHT: float
        BEVELOUTLINE: float
        BEVELTYPE: int
        BREAKDISTANCE: float
        BRIDGEBIAS: float
        BRIDGEEDGEADJACENT: float
        BRIDGEREVERSETRIANGLE: int
        BRIDGESEGMENTS: int
        BRIDGESELECTED: int
        BRIDGESMOOTHTHRESHOLD: float
        BRIDGETAPER: float
        BRIDGETARGET1: int
        BRIDGETARGET2: int
        BRIDGETWIST1: int
        BRIDGETWIST2: int
        BUBBLE: float
        CAGECOLOR: MXSWrapperBase
        CHAMFEREDGEAMOUNT: float
        CHAMFEREDGEOPEN: bool
        CHAMFERVERTEXAMOUNT: float
        CHAMFERVERTEXDEPTH: float
        CHAMFERVERTEXOPEN: bool
        CHAMFERVERTEXSEGMENTS: int
        CHAMFERVERTEXSMOOTH: bool
        CHAMFERVERTEXSMOOTHTHRESHOLD: float
        CHAMFERVERTEXSMOOTHTYPE: int
        CONNECTEDGEPINCH: int
        CONNECTEDGESEGMENTS: int
        CONNECTEDGESLIDE: int
        CONSTRAINTYPE: int
        CURRENTOPERATION: int
        DATACHANNEL: int
        DATAVALUE: float
        DELETEISOLATEDVERTS: bool
        EDGECHAMFERDEPTH: float
        EDGECHAMFERENDBIAS: float
        EDGECHAMFERINVERT: bool
        EDGECHAMFERMITERINGTYPE: int
        EDGECHAMFERQUADINTERSECTIONSOBSOLETE: bool
        EDGECHAMFERRADIALBIAS: float
        EDGECHAMFERSEGMENTS: int
        EDGECHAMFERSMOOTH: bool
        EDGECHAMFERSMOOTHTHRESHOLD: float
        EDGECHAMFERSMOOTHTYPE: int
        EDGECHAMFERTENSION: float
        EDGECHAMFERTYPEOBSOLETE: int
        EXTRUDEALONGSPLINEALIGN: bool
        EXTRUDEALONGSPLINENODE: None
        EXTRUDEALONGSPLINEROTATION: float
        EXTRUDEALONGSPLINESEGMENTS: int
        EXTRUDEALONGSPLINETAPER: float
        EXTRUDEALONGSPLINETAPERCURVE: float
        EXTRUDEALONGSPLINETWIST: float
        EXTRUDEEDGEHEIGHT: float
        EXTRUDEEDGEWIDTH: float
        EXTRUDEFACEBIAS: float
        EXTRUDEFACEHEIGHT: float
        EXTRUDEFACETYPE: int
        EXTRUDEVERTEXHEIGHT: float
        EXTRUDEVERTEXWIDTH: float
        FALLOFF: float
        HARDEDGEDISPLAY: int
        HARDEDGEDISPLAYCOLOR: MXSWrapperBase
        HINGEANGLE: float
        HINGEBASE: MXSWrapperBase
        HINGEDIRECTION: MXSWrapperBase
        HINGESEGMENTS: int
        IGNOREBACKFACING: bool
        INSETAMOUNT: float
        INSETTYPE: int
        LASTDELTAINDEX: int
        LOCKSOFTSEL: bool
        MATERIALIDTOSET: int
        OUTLINEAMOUNT: float
        PAINTDEFORMAXIS: int
        PAINTDEFORMMODE: int
        PAINTDEFORMSIZE: float
        PAINTDEFORMSTRENGTH: float
        PAINTDEFORMVALUE: float
        PAINTSELMODE: int
        PAINTSELSIZE: float
        PAINTSELSTRENGTH: float
        PAINTSELVALUE: float
        PINCH: float
        PRESERVEUVS: bool
        RELAXAMOUNT: float
        RELAXHOLDBOUNDARYPOINTS: bool
        RELAXHOLDOUTERPOINTS: bool
        RELAXITERATIONS: int
        REMVEEDGECTRLKEY: bool
        SELECTANGLE: float
        SELECTBYANGLE: bool
        SELECTBYMATERIALCLEAR: bool
        SELECTBYMATERIALID: int
        SELECTBYSMOOTHINGGROUP: int
        SELECTBYSMOOTHINGGROUPCLEAR: bool
        SELECTBYVERTEX: bool
        SELECTEDCAGECOLOR: MXSWrapperBase
        SELECTMODE: int
        SEPARATEBYMATERIAL: bool
        SEPARATEBYSMOOTHING: bool
        SHOWCAGE: bool
        SMOOTHINGGROUPSTOCLEAR: int
        SMOOTHINGGROUPSTOSET: int
        SMOOTHNESS: float
        SPLIT: bool
        SSEDGEDIST: int
        SSUSEEDGEDIST: bool
        TESSELLATEBYFACE: int
        TESSTENSION: float
        USESOFTSEL: bool
        USESTACKSELECTION: bool
        WELDEDGETHRESHOLD: float
        WELDVERTEXTHRESHOLD: float
        WORLDTOOBJECTTRANSFORM: MXSWrapperBase
        ...
    class Edit_Spline(Modifier):
        ...
    class EditablePolyMesh(GeometryClass):
        ...
    class Editable_Patch(GeometryClass):
        ...
    class Editable_Poly(GeometryClass):
        ...
    class Editable_Mesh(GeometryClass):
        ...
    class EffectClass(Value):
        ...
    class Egg(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        EGG_ANGLE: float
        EGG_LENGTH: float
        EGG_OUTLINE: bool
        EGG_THICKNESS: float
        EGG_WIDTH: float
        MAPCOORDS: bool
        OPTIMIZE: bool
        QUAD_CAP: bool
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        ...
    class ElementFileDialog(Primitive):
        ...
    class ElementGetCustomGamma(Primitive):
        ...
    class ElementGetMetaData(Primitive):
        ...
    class ElementSetCustomGamma(Primitive):
        ...
    class ElementSetMetaData(Primitive):
        ...
    class Ellipse(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        ELLIPSE_OUTLINE: bool
        ELLIPSE_THICKNESS: float
        LENGTH: float
        MAPCOORDS: bool
        OPTIMIZE: bool
        QUAD_CAP: bool
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        WIDTH: float
        ...
    class EmptyClass(Value):
        ...
    class EmptyModifier(Modifier):
        ...
    class EmptyModifier_Old(Modifier):
        MYPARAM: str
        ...
    class EmptySource(ReferenceTarget):
        ...
    class Empty_Flow(ReferenceTarget):
        ...
    class Emulator(TextureMap):
        ...
    class EnableCoordCenter(Primitive):
        ...
    class EnableRefCoordSys(Primitive):
        ...
    class EnableSceneRedraw(Primitive):
        ...
    class EnableShowEndRes(Primitive):
        ...
    class EnableStatusXYZ(Primitive):
        ...
    class EnableSubObjSel(Primitive):
        ...
    class EulerAngles(Value):
        ...
    class Euler_Filter(TrackViewUtility):
        ...
    class Euler_XYZ(RotationController):
        AXISORDER: int
        ...
    class Event(Helper):
        ...
    class ExchangeStorePackageManager(Interface):
        ...
    class ExclusionListDlg(Primitive):
        ...
    class ExportHTR(ExporterPlugin):
        ...
    class ExportMesh(MAXScriptFunction):
        ...
    class ExporterPlugin(MAXWrapperNonRefTarg):
        ...
    class ExposeTm(Helper):
        ANGLE: float
        AXISTRIPOD: bool
        BOX: bool
        CENTERMARKER: bool
        CONSTANTSCREENSIZE: bool
        CROSS: bool
        DISPLAYEXPOSEDVALS: bool
        DISTANCE: float
        DRAWONTOP: bool
        EULERXORDER: int
        EULERYORDER: int
        EULERZORDER: int
        EXPOSENODE: None
        LOCALEULER: MXSWrapperBase
        LOCALEULERX: float
        LOCALEULERY: float
        LOCALEULERZ: float
        LOCALPOSITION: MXSWrapperBase
        LOCALPOSITIONX: float
        LOCALPOSITIONY: float
        LOCALPOSITIONZ: float
        LOCALREFERENCENODE: None
        SIZE: float
        STRIPNUSCALE: bool
        TIMEOFFSET: MXSWrapperBase
        USEPARENT: bool
        USETIMEOFFSET: bool
        WORLDBOUNDINGBOXHEIGHT: float
        WORLDBOUNDINGBOXLENGTH: float
        WORLDBOUNDINGBOXSIZE: MXSWrapperBase
        WORLDBOUNDINGBOXWIDTH: float
        WORLDEULER: MXSWrapperBase
        WORLDEULERX: float
        WORLDEULERY: float
        WORLDEULERZ: float
        WORLDPOSITION: MXSWrapperBase
        WORLDPOSITIONX: float
        WORLDPOSITIONY: float
        WORLDPOSITIONZ: float
        ...
    class ExposeTransform(Helper):
        ANGLE: float
        AXISTRIPOD: bool
        BOX: bool
        CENTERMARKER: bool
        CONSTANTSCREENSIZE: bool
        CROSS: bool
        DISPLAYEXPOSEDVALS: bool
        DISTANCE: float
        DRAWONTOP: bool
        EULERXORDER: int
        EULERYORDER: int
        EULERZORDER: int
        EXPOSENODE: None
        LOCALEULER: MXSWrapperBase
        LOCALEULERX: float
        LOCALEULERY: float
        LOCALEULERZ: float
        LOCALPOSITION: MXSWrapperBase
        LOCALPOSITIONX: float
        LOCALPOSITIONY: float
        LOCALPOSITIONZ: float
        LOCALREFERENCENODE: None
        SIZE: float
        STRIPNUSCALE: bool
        TIMEOFFSET: MXSWrapperBase
        USEPARENT: bool
        USETIMEOFFSET: bool
        WORLDBOUNDINGBOXHEIGHT: float
        WORLDBOUNDINGBOXLENGTH: float
        WORLDBOUNDINGBOXSIZE: MXSWrapperBase
        WORLDBOUNDINGBOXWIDTH: float
        WORLDEULER: MXSWrapperBase
        WORLDEULERX: float
        WORLDEULERY: float
        WORLDEULERZ: float
        WORLDPOSITION: MXSWrapperBase
        WORLDPOSITIONX: float
        WORLDPOSITIONY: float
        WORLDPOSITIONZ: float
        ...
    class Expose_Euler_Control(RotationController):
        ...
    class Expose_Float_Control(FloatController):
        ...
    class Expose_Point3_Control(Point3Controller):
        ...
    class ExpressSave(Helper):
        ...
    class Express_Save(Helper):
        ...
    class Extrude(Modifier):
        AMOUNT: float
        CAPEND: bool
        CAPSTART: bool
        CAPTYPE: int
        MAPCOORDS: bool
        MATIDS: bool
        OUTPUT: int
        SEGS: int
        SMOOTH: bool
        USESHAPEIDS: bool
        ...
    class FBXEXP(ExporterPlugin):
        ...
    class FBXExporterGetParam(Primitive):
        ...
    class FBXExporterSetParam(Primitive):
        ...
    class FBXIMP(ImporterPlugin):
        ...
    class FBXImportOCMerge(Primitive):
        ...
    class FBXImporterFileLinkVersion(Primitive):
        ...
    class FBXImporterGetParam(Primitive):
        ...
    class FBXImporterSetParam(Primitive):
        ...
    class FFD2X2X2(Modifier):
        DEFORMTYPE: int
        DISPLATTICE: bool
        DISPSOURCE: bool
        INPOINTS: bool
        OFFSET: float
        OUTPOINTS: bool
        ...
    class FFD3X3X3(Modifier):
        DEFORMTYPE: int
        DISPLATTICE: bool
        DISPSOURCE: bool
        INPOINTS: bool
        OFFSET: float
        OUTPOINTS: bool
        ...
    class FFD4X4X4(Modifier):
        DEFORMTYPE: int
        DISPLATTICE: bool
        DISPSOURCE: bool
        INPOINTS: bool
        OFFSET: float
        OUTPOINTS: bool
        ...
    class FFDBox(Modifier):
        CONTINUITY: float
        DEFORMTYPE: int
        DISPLATTICE: bool
        DISPSOURCE: bool
        FALLOFF: float
        INPOINTS: bool
        OFFSET: float
        OUTPOINTS: bool
        TENSION: float
        ...
    class FFDCyl(Modifier):
        CONTINUITY: float
        DEFORMTYPE: int
        DISPLATTICE: bool
        DISPSOURCE: bool
        FALLOFF: float
        INPOINTS: bool
        OFFSET: float
        OUTPOINTS: bool
        TENSION: float
        ...
    class FFD_2X2X2(Modifier):
        DEFORMTYPE: int
        DISPLATTICE: bool
        DISPSOURCE: bool
        INPOINTS: bool
        OFFSET: float
        OUTPOINTS: bool
        ...
    class FFD_3X3X3(Modifier):
        DEFORMTYPE: int
        DISPLATTICE: bool
        DISPSOURCE: bool
        INPOINTS: bool
        OFFSET: float
        OUTPOINTS: bool
        ...
    class FFD_4X4X4(Modifier):
        DEFORMTYPE: int
        DISPLATTICE: bool
        DISPSOURCE: bool
        INPOINTS: bool
        OFFSET: float
        OUTPOINTS: bool
        ...
    class FFD_Binding(SpacewarpModifier):
        ...
    class FFD_Select(Modifier):
        ...
    class FaceSelection(Value):
        ...
    class Face_Extrude(Modifier):
        AMOUNT: float
        EXTRUDEFROMCENTER: bool
        SCALE: float
        ...
    class FacesOrientation(Interface):
        ...
    class Faces_Orientation(GlobalUtilityPlugin):
        ...
    class Fade(VideoPostFilter):
        ...
    class FalloffManip(Helper):
        ...
    class Falloff_Manipulator(Helper):
        ...
    class FastShadingFragment(GraphicsFragmentPlugin):
        ...
    class FbxExporter(ExporterPlugin):
        ...
    class FbxImporter(ImporterPlugin):
        ...
    class FbxMaxByMaterialFilter(ReferenceMaker):
        ...
    class FbxMaxByObjectFilter(ReferenceMaker):
        ...
    class FbxMaxByRevitCategoryFilter(ReferenceMaker):
        ...
    class FbxMaxByRevitTypeFilter(ReferenceMaker):
        ...
    class FbxMaxFactory(ReferenceMaker):
        ...
    class FbxMaxFilterList(ReferenceMaker):
        ...
    class FbxMaxObjTranslator(ReferenceMaker):
        ...
    class FbxMaxOneObjectFilter(ReferenceMaker):
        ...
    class FbxMaxRevitFactory(ReferenceMaker):
        ...
    class FbxMaxTableRecord(ReferenceMaker):
        ...
    class FbxMaxTableRecordReferenceMaker(ReferenceMaker):
        ...
    class FbxMaxWrapper(GeometryClass):
        ...
    class FbxRevitMaxTableRec(ReferenceMaker):
        ...
    class FencePickNode(Primitive):
        ...
    class FileLinkAsDwgImporter(ImporterPlugin):
        ...
    class FileLinkMgr(Interface):
        ...
    class FileLink_DwgLayerTable(ReferenceTarget):
        ...
    class FileLink_LinkTable(FloatController):
        ...
    class FileLink_VzMaterialTable(ReferenceTarget):
        ...
    class FileOpenMatLib(Primitive):
        ...
    class FileResolutionManager(Interface):
        ...
    class FileSaveAsMatLib(Primitive):
        ...
    class FileSaveMatLib(Primitive):
        ...
    class FileStream(Value):
        ...
    class File_Link_Manager(UtilityPlugin):
        ...
    class File_Output(RenderEffect):
        ACTIVE: bool
        AFFECTSOURCE: bool
        CAMERANODE: None
        CHANNELTYPE: int
        FARZ: float
        FITSCENE: bool
        NEARZ: float
        ...
    class Fillet_Chamfer(Modifier):
        ...
    class FilmGrain(RenderEffect):
        GRAIN: float
        MASK_BACKGROUND: bool
        ...
    class Film_Grain(RenderEffect):
        GRAIN: float
        MASK_BACKGROUND: bool
        ...
    class FilterMeshColorsByHue(Modifier):
        FILTER_DEPTH: float
        FILTER_VALUE: float
        FILTER_WIDTH: float
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        _DUMMY: bool
        ...
    class FilterString(Primitive):
        ...
    class Filter_Kernel_Plug_In_Not_Found(Filter):
        ...
    class FindLengthSegAndParam(Primitive):
        ...
    class FindPMod(MAXScriptFunction):
        ...
    class FindPathSegAndParam(Primitive):
        ...
    class Find_Target(Helper):
        ACCELERATION_LIMIT: float
        AIM_POINT_TYPE: int
        ANIMATED_SHAPE: bool
        ASSIGNMENT_TYPE: int
        COLOR_TYPE: bool
        CRUISE_SPEED: float
        CRUISE_SPEED_VARIATION: float
        DOCKING_DISTANCE: float
        DOCKING_SPEED: float
        DOCKING_SPEED_VARIATION: float
        DOCKING_TYPE: int
        EASE_IN: float
        FOLLOW_TARGET: bool
        ICON_SIZE: float
        LOCK_ON_TARGET: bool
        RANDOM_SEED: int
        SPEED_TYPE: int
        SUBFRAME_SAMPLING: bool
        SYNC_TYPE: int
        TARGET_OBJECTS: MXSWrapperBase
        TARGET_SYNC_TYPE: int
        TARGET_TYPE: int
        TEST_DISTANCE: float
        TEST_TYPE: int
        TIME: int
        TIME_VARIATION: int
        TIMING_TYPE: int
        USE_CRUISE_SPEED: bool
        USE_DOCKING_SPEED: bool
        ...
    class Fire_Effect(Atmospheric):
        DENSITY: float
        DRIFT: float
        EXPLOSION: int
        FLAME_DETAIL: float
        FLAME_SIZE: float
        FLAME_TYPE: int
        FURY: float
        INNER_COLOR: MXSWrapperBase
        OUTER_COLOR: MXSWrapperBase
        PHASE: float
        REGULARITY: float
        SAMPLES: int
        SMOKE: int
        SMOKE_COLOR: MXSWrapperBase
        STRETCH: float
        ...
    class FixAmbient(UtilityPlugin):
        ...
    class FixInvalidMaterialsForDaylightSimulation(MAXScriptFunction):
        ...
    class Fix_Ambient(UtilityPlugin):
        ...
    class Fixed(GeometryClass):
        CHAMFERED_PROFILE: bool
        DEPTH: float
        FRAME_THICKNESS: float
        GENERATE_MAPPING_COORDS: bool
        GLAZING_THICKNESS: float
        HEIGHT: float
        HORIZONTAL_FRAME_WIDTH: float
        NUMBER_OF_PANELS_HORIZONTALLY: int
        NUMBER_OF_PANELS_VERTICALLY: int
        RAIL_WIDTH: float
        VERTICAL_FRAME_WIDTH: float
        WIDTH: float
        ...
    class FlashNodes(Primitive):
        ...
    class Flat_Mirror(TextureMap):
        APPLYBLUR: bool
        APPLYTOFACEID: bool
        BLURAMOUNT: float
        DISTORTIONAMOUNT: float
        DISTORTIONTYPE: int
        FACEID: int
        FRAME: int
        LEVEL: float
        NOISETYPE: int
        NTHFRAME: int
        PHASE: float
        SIZE: float
        USEENVIROMENT: bool
        ...
    class Flex(Modifier):
        ABSOLUTE: bool
        ADDMODE: int
        AFFECTALL: bool
        CHASE: bool
        COLLIDERNODE: MXSWrapperBase
        CREATESPRINGDEPTH: int
        CREATESPRINGMULT: float
        CUSTOMSPRINGDISPLAY: MXSWrapperBase
        DISPLAYSPRINGS: bool
        ENABLEADVANCESPRINGS: bool
        ENABLECENTER: bool
        ENABLEENDFRAME: bool
        ENDFRAME: int
        EXTRASTRENGTH: MXSWrapperBase
        EXTRASWAY: MXSWrapperBase
        FLEX: float
        FORCENODE: MXSWrapperBase
        HOLDLENGTH: bool
        HOLDLENGTHPERCENT: float
        HOLDRADIUS: float
        LAZYEVAL: bool
        PAINTBACKFACE: bool
        PAINTFEATHER: float
        PAINTRADIUS: float
        PAINTSTRENGTH: float
        REFERENCEFRAME: int
        SAMPLES: int
        SOLVER: int
        SPRINGCOLORS: MXSWrapperBase
        STIFFNESS: float
        STRENGTH: float
        STRETCH: float
        STRETCHSTRENGTH: float
        STRETCHSWAY: float
        SWAY: float
        TORQUESTRENGTH: float
        TORQUESWAY: float
        ...
    class FlightStudio(Interface):
        ...
    class FlightStudioExport(Interface):
        ...
    class FlightStudioImport(Interface):
        ...
    class Flight_Studio(UtilityPlugin):
        ...
    class Flight_Studio_Bitmap_Class_Name(CustAttrib):
        TEXENV: int
        ...
    class FlippedFacesClass(GlobalUtilityPlugin):
        ...
    class FlippedUVWFaces(Interface):
        ...
    class FlippedUVWFacesClass(GlobalUtilityPlugin):
        ...
    class Flipped_UVW_Faces(GlobalUtilityPlugin):
        ...
    class FloatLimitCtrl(FloatController):
        ENABLE: bool
        LOWER_LIMIT: float
        LOWER_LIMIT_ENABLED: bool
        LOWER_SMOOTHING: float
        STATIC_VALUE: float
        UPPER_LIMIT: float
        UPPER_LIMIT_ENABLED: bool
        UPPER_SMOOTHING: float
        ...
    class FloatList(FloatController):
        AVERAGE: bool
        WEIGHT: MXSWrapperBase
        ...
    class FloatPacket(ReferenceMaker):
        ...
    class FloatReactor(FloatController):
        ...
    class FloatXRefCtrl(FloatController):
        ...
    class Float_Expression(FloatController):
        ...
    class Float_Layer(FloatController):
        ...
    class Float_Mixer_Controller(FloatController):
        ...
    class Float_Motion_Capture(FloatController):
        ...
    class Float_Reactor(FloatController):
        ...
    class Float_Wire(FloatController):
        ...
    class Float_XRef_Controller(FloatController):
        ...
    class Flow(GeometryClass):
        DENSITY2: float
        DENSITY: float
        DIRECTIONINDEX: int
        GENDER2: float
        GENDER: float
        GENDERSAMPLE: int
        LANEWIDTH: float
        LINKPORTALS: bool
        POSITIONSAMPLE: int
        RUNNING2: float
        RUNNING: float
        SPEED2: float
        SPEED: float
        WIDTH: float
        ...
    class FlowRaytraceInterface(Interface):
        ...
    class FltGUP(GlobalUtilityPlugin):
        ...
    class FltImport(ImporterPlugin):
        ...
    class FltTextureAttrCustAttrib(CustAttrib):
        TEXENV: int
        ...
    class FluidLoader(GeometryClass):
        ARNOLDDROPLETRADIUS: float
        ARNOLDDROPLETREVEALFACTOR: float
        ARNOLDFILTERINGDILATE: float
        ARNOLDFILTERINGERODE: float
        ARNOLDFILTERINGSMOOTH: float
        ARNOLDFILTERINGSMOOTHITERATIONS: int
        ARNOLDFILTERINGSMOOTHMODE: int
        ARNOLDFOAMDROPLETRADIUS: float
        ARNOLDFOAMDROPLETREVEALFACTOR: float
        ARNOLDFOAMFILTERINGDILATE: float
        ARNOLDFOAMFILTERINGERODE: float
        ARNOLDFOAMFILTERINGSMOOTH: float
        ARNOLDFOAMFILTERINGSMOOTHITERATIONS: int
        ARNOLDFOAMFILTERINGSMOOTHMODE: int
        ARNOLDFOAMHOLEKILLTHRESHOLD: float
        ARNOLDFOAMIMPLICITSAMPLES: int
        ARNOLDFOAMIMPLICITSTEPSIZE: float
        ARNOLDFOAMMESHSMOOTHING: bool
        ARNOLDFOAMMESHSUBDIVISIONS: int
        ARNOLDFOAMOCEANBLENDINGBOUNDARYRADIUS: float
        ARNOLDFOAMOCEANMESHPLANE: None
        ARNOLDFOAMRESOLUTIONFACTOR: float
        ARNOLDFOAMSURFACERADIUS: float
        ARNOLDFOAMSURFACETYPE: int
        ARNOLDFOAMUSEOCEANBLENDING: bool
        ARNOLDHOLEKILLTHRESHOLD: float
        ARNOLDIMPLICITSAMPLES: int
        ARNOLDIMPLICITSTEPSIZE: float
        ARNOLDMESHSMOOTHING: bool
        ARNOLDMESHSUBDIVISIONS: int
        ARNOLDOCEANBLENDINGBOUNDARYRADIUS: float
        ARNOLDOCEANMESHPLANE: None
        ARNOLDPOINTCHUNKSIZE: int
        ARNOLDPOINTRADIUS: float
        ARNOLDPOINTRADIUSCHANNEL: int
        ARNOLDPOINTSTEPSIZE: float
        ARNOLDRENDERCOMPONENTTYPE: int
        ARNOLDRESOLUTIONFACTOR: float
        ARNOLDSURFACECHANNELNAMETAB: MXSWrapperBase
        ARNOLDSURFACERADIUS: float
        ARNOLDSURFACETYPE: int
        ARNOLDUSEOCEANBLENDING: bool
        CACHEFLAGSTAB: MXSWrapperBase
        CACHENAMETAB: MXSWrapperBase
        CACHETAB: MXSWrapperBase
        COLORCHANNELMAX: MXSWrapperBase
        COLORCHANNELMIN: MXSWrapperBase
        COLORCHANNELMODE: int
        CUSTOMNODE: None
        DISPLAYCACHELIMIT: float
        DISPLAYCACHELIMITENABLE: bool
        DISPLAYTYPEMODE: int
        ENABLEGPUPOINTS: bool
        ENDFRAMEINDIRECT: int
        ENDFRAME_TAB: MXSWrapperBase
        FOAMCOLORCHANNELMAX: MXSWrapperBase
        FOAMCOLORCHANNELMIN: MXSWrapperBase
        FOAMCOLORCHANNELMODE: int
        FOAMCUSTOMRENDERNODE: None
        FOAMDISPLAYTYPEMODE: int
        FOAMOPACITYCHANNELMAX: float
        FOAMOPACITYCHANNELMIN: float
        FOAMOPACITYCHANNELMODE: int
        FOAMRENDERSIZECHANNEL: str
        FOAMRENDERSIZEMAX: float
        FOAMRENDERSIZEMAXDOMAIN: float
        FOAMRENDERSIZEMIN: float
        FOAMRENDERSIZEMINDOMAIN: float
        FOAMRENDERSTATICSIZE: float
        FOAMRENDERTYPE: int
        FOAMSIZECHANNELMAX: float
        FOAMSIZECHANNELMIN: float
        FOAMSIZECHANNELMODE: int
        FOAMSIZECHANNELTYPE: int
        FOAMSTATICCOLOR: MXSWrapperBase
        FOAMSTATICOPACITY: float
        FOAMSTATICSIZE: float
        FOAMVIEWPORTPERCENTACCESSOR: float
        ICONSIZE: float
        LIQUIDCUSTOMRENDERNODE: None
        LIQUIDRENDERSIZECHANNEL: str
        LIQUIDRENDERSIZEMAX: float
        LIQUIDRENDERSIZEMAXDOMAIN: float
        LIQUIDRENDERSIZEMIN: float
        LIQUIDRENDERSIZEMINDOMAIN: float
        LIQUIDRENDERSTATICSIZE: float
        LIQUIDRENDERTYPE: int
        LIQUIDSIZECHANNELTYPE: int
        MATERIALIDINDIRECT: int
        MATERIALID_TAB: MXSWrapperBase
        MESHINGDROPLETRADIUSACCESSOR: float
        MESHINGDROPLETRADIUSTAB: MXSWrapperBase
        MESHINGDROPLETREVEALFACTORACCESSOR: float
        MESHINGDROPLETREVEALFACTORTAB: MXSWrapperBase
        MESHINGFLIPFACENORMALACCESSOR: bool
        MESHINGFLIPFACENORMALTAB: MXSWrapperBase
        MESHINGHOLEKILLTHRESHOLDACCESSOR: float
        MESHINGHOLEKILLTHRESHOLDTAB: MXSWrapperBase
        MESHINGKERNELFACTORACCESSOR: float
        MESHINGKERNELFACTORTAB: MXSWrapperBase
        MESHINGRESOLUTIONFACTORACCESSOR: float
        MESHINGRESOLUTIONFACTORTAB: MXSWrapperBase
        MESHINGSMOOTHINGACCESSOR: int
        MESHINGSMOOTHINGTAB: MXSWrapperBase
        MESHINGSURFACERADIUSACCESSOR: float
        MESHINGSURFACERADIUSTAB: MXSWrapperBase
        OPACITYCHANNELMAX: float
        OPACITYCHANNELMIN: float
        OPACITYCHANNELMODE: float
        PLAYBACKFRAMEINDIRECT: int
        PLAYBACKFRAME_TAB: MXSWrapperBase
        PLAYBACKMODEINDIRECT: int
        PLAYBACKMODE_TAB: MXSWrapperBase
        RENDERCHANNELMAPINDEX: MXSWrapperBase
        RENDERCHANNELMAPNAME: MXSWrapperBase
        SHOWICON: int
        SIZECHANNELMAX: float
        SIZECHANNELMIN: float
        SIZECHANNELMODE: float
        STARTFRAMEINDIRECT: int
        STARTFRAME_TAB: MXSWrapperBase
        STARTONLYINDIRECT: int
        STARTONLY_TAB: MXSWrapperBase
        STATICCOLOR: MXSWrapperBase
        STATICOPACITY: float
        STATICSIZE: float
        USELOADEROBJECTTRANSFORM: bool
        VIEWPORTPERCENTACCESSOR: float
        ...
    class FluidSimObjectManager(Interface):
        ...
    class Fog(Atmospheric):
        ANGLE: float
        BOTTOM: float
        DENSITY: float
        EXPONENTIAL: int
        FALLOFF: int
        FAR: float
        FOG_BACKGROUND: int
        FOG_COLOR: MXSWrapperBase
        FOG_TYPE: int
        HORIZON_NOISE: int
        NEAR: float
        PHASE: float
        SIZE: float
        TOP: float
        USE_COLOR_MAP: int
        USE_OPACITY_MAP: int
        ...
    class FogHelper(Helper):
        ...
    class Foliage(GeometryClass):
        CANOPYMODE: int
        DENSITY: float
        GENUV: bool
        HEIGHT: float
        LEVELOFDETAIL: int
        PRUNING: float
        SEED: int
        SHOWBRANCHES: bool
        SHOWFLOWERS: bool
        SHOWFRUIT: bool
        SHOWLEAVES: bool
        SHOWROOTS: bool
        SHOWTRUNK: bool
        ...
    class FoliagetextureMap(TextureMap):
        ...
    class Follow_Bank(UtilityPlugin):
        ...
    class FootBend(FloatController):
        ...
    class FootLift(FloatController):
        ...
    class FootTrans(Matrix3Controller):
        ...
    class Footsteps(MAXWrapper):
        ...
    class Force(Helper):
        FORCE_OVERLAPPING: int
        FORCE_SPACE_WARPS: MXSWrapperBase
        INFLUENCE: float
        SYNC: int
        USE_SCRIPT_FLOAT: int
        ...
    class ForceCompleteRedraw(Primitive):
        ...
    class FragmentGraph(GraphicsFragmentPlugin):
        ...
    class FrameTagManager(Interface):
        ...
    class Free_Area(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Free_Cylinder(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Free_Disc(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Free_Light(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Free_Linear(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Free_Point(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Free_Rectangle(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Free_Sphere(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Freecamera(Camera):
        CLIPMANUALLY: bool
        CURFOV: float
        FARCLIP: float
        FARRANGE: float
        FAR_CLIP: float
        FOV: float
        FOVTYPE: int
        MPASSEFFECT: MXSWrapperBase
        MPASSENABLED: bool
        MPASSRENDERPERPASS: bool
        NEARCLIP: float
        NEARRANGE: float
        NEAR_CLIP: float
        ORTHOPROJECTION: bool
        SHOWCONE: bool
        SHOWHORIZON: bool
        SHOWRANGES: bool
        TARGETDISTANCE: None
        TYPE: MXSWrapperBase
        ...
    class FreehandSpline(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        CONSTRAINOFFSET: float
        CURVETYPE: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        ENABLECLOSEDCURVE: bool
        ENABLECONSTRAIN: bool
        ENABLECONSTRAINSHOWNORMALS: bool
        ENDCREATEONBUTTONUP: bool
        GRANULARITY: int
        KNOTS: MXSWrapperBase
        MAPCOORDS: bool
        NORMALS: MXSWrapperBase
        OPTIMIZE: bool
        QUAD_CAP: bool
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SAMPLING: int
        SHAPE_KNOTS: MXSWrapperBase
        SHOWKNOTS: bool
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        THRESHOLD: int
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        ...
    class Function(Value):
        ...
    class FunctionReferenceTarget(ReferenceTarget):
        FACTOR_FOR_FIRST_OPERAND: float
        FACTOR_FOR_SECOND_OPERAND: float
        FILTER: None
        FIRST_OPERAND_TYPE: int
        FUNCTION_TYPE_FOR_BOOLEAN_AND_BOOLEAN: int
        FUNCTION_TYPE_FOR_BOOLEAN_SINGLE: int
        FUNCTION_TYPE_FOR_INTEGER_AND_REAL: int
        FUNCTION_TYPE_FOR_INTEGER_REAL_SINGLE: int
        FUNCTION_TYPE_FOR_MATRIX_AND_MATRIX: int
        FUNCTION_TYPE_FOR_MATRIX_SINGLE: int
        FUNCTION_TYPE_FOR_QUATERNION_AND_INTEGER_TIME: int
        FUNCTION_TYPE_FOR_QUATERNION_AND_QUATERNION: int
        FUNCTION_TYPE_FOR_QUATERNION_AND_REAL: int
        FUNCTION_TYPE_FOR_QUATERNION_SINGLE: int
        FUNCTION_TYPE_FOR_TIME_AND_TIME: int
        FUNCTION_TYPE_FOR_TIME_SINGLE: int
        FUNCTION_TYPE_FOR_VECTOR_AND_INTEGER_TIME: int
        FUNCTION_TYPE_FOR_VECTOR_AND_MATRIX: int
        FUNCTION_TYPE_FOR_VECTOR_AND_QUATERNION: int
        FUNCTION_TYPE_FOR_VECTOR_AND_REAL: int
        FUNCTION_TYPE_FOR_VECTOR_AND_VECTOR: int
        FUNCTION_TYPE_FOR_VECTOR_SINGLE: int
        GROUP_ID_DATA_CHANNEL: None
        GROUP_ID_DATA_HANDLE: int
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INTEGER_FACTOR_FOR_FIRST_OPERAND: int
        INTEGER_FACTOR_FOR_SECOND_OPERAND: int
        INTEGER_OFFSET_FOR_FIRST_OPERAND: int
        INTEGER_POST_FACTOR: int
        OFFSET_FOR_FIRST_OPERAND: float
        POST_FACTOR: float
        RESTRICT_BY_GROUP_ID: bool
        SECOND_OPERAND_TYPE_FOR_INTEGER_REAL: int
        SECOND_OPERAND_TYPE_FOR_QUATERNION: int
        SECOND_OPERAND_TYPE_FOR_VECTOR: int
        SYNC_TYPE: int
        USE_E5: bool
        USE_R_AS_FACTOR_FOR_FIRST_OPERAND: bool
        USE_R_AS_FACTOR_FOR_SECOND_OPERAND: bool
        USE_SECOND_OPERAND: bool
        ...
    class GIF(BitmapIO):
        ...
    class GameExporter(UtilityPlugin):
        ...
    class GameExporterOpenDialog(Primitive):
        ...
    class GameExporterShown(Primitive):
        ...
    class GameNavGup(GlobalUtilityPlugin):
        ...
    class GammaCorrectionFragment(GraphicsFragmentPlugin):
        ...
    class Garment_Maker(Modifier):
        AUTOMESH: bool
        DENSITY: float
        FIGURE: None
        OUTPUTTYPE: int
        PRESERVE: bool
        RELAX: bool
        SHOWMESH: bool
        SHOWSEAMS: bool
        STRETCHMAPPING: bool
        STRIPTEXTURESCALE: float
        STRIPWIDTH: float
        ...
    class Garmentize2(Modifier):
        AUTOMESH: bool
        DENSITY: float
        FIGURE: None
        OUTPUTTYPE: int
        PRESERVE: bool
        RELAX: bool
        SHOWMESH: bool
        SHOWSEAMS: bool
        STRETCHMAPPING: bool
        STRIPTEXTURESCALE: float
        STRIPWIDTH: float
        ...
    class GenDerivedObjectClass(MAXWrapper):
        ...
    class GenerateControlChangedFn(MAXScriptFunction):
        ...
    class GenerateControlEventHandler(MAXScriptFunction):
        ...
    class GenerateControlSection(MAXScriptFunction):
        ...
    class GenerateFullRolloutString(MAXScriptFunction):
        ...
    class GenerateGroupChangedFunctions(MAXScriptFunction):
        ...
    class GenerateLoadValuesFn(MAXScriptFunction):
        ...
    class GenerateMCGToolFromTemplate(MAXScriptFunction):
        ...
    class GenerateMeshGraphCompoundForSelection(MAXScriptFunction):
        ...
    class GenerateSaveValuesFn(MAXScriptFunction):
        ...
    class GenerateStandinDictionary(Primitive):
        ...
    class GenerateUndoFunction(MAXScriptFunction):
        ...
    class Generic(Value):
        ...
    class Gengon(GeometryClass):
        FILLET: float
        FILLET_SEGMENTS: int
        HEIGHT: float
        HEIGHT_SEGMENTS: int
        MAPCOORDS: int
        RADIUS: float
        SIDES: int
        SIDE_SEGMENTS: int
        SMOOTH: int
        ...
    class GeoSphere(GeometryClass):
        BASETOPIVOT: bool
        BASETYPE: int
        CREATIONMETHOD: int
        HEMISPHERE: bool
        MAPCOORDS: bool
        RADIUS: float
        SEGS: int
        SMOOTH: bool
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS: float
        ...
    class GeomFilterFn(MAXScriptFunction):
        ...
    class GeomObject(Value):
        ...
    class GeometryCheckerManager(GlobalUtilityPlugin):
        ...
    class GeometryClass(Node):
        ...
    class GepCanMakeRamp(Primitive):
        ...
    class GepGetDisplayType(Primitive):
        ...
    class GepMakeRamp(Primitive):
        ...
    class GetActiveShadeBitmap(Primitive):
        ...
    class GetBackGround(Primitive):
        ...
    class GetBackGroundController(Primitive):
        ...
    class GetBkgFrameNum(Primitive):
        ...
    class GetBkgImageAnimate(Primitive):
        ...
    class GetBkgImageAspect(Primitive):
        ...
    class GetBkgORType(Primitive):
        ...
    class GetBkgRangeVal(Primitive):
        ...
    class GetBkgStartTime(Primitive):
        ...
    class GetBkgSyncFrame(Primitive):
        ...
    class GetCATNodeGroup(MAXScriptFunction):
        ...
    class GetCATParent(MAXScriptFunction):
        ...
    class GetCVertMode(Primitive):
        ...
    class GetCommandPanelTaskMode(Primitive):
        ...
    class GetCoordCenter(Primitive):
        ...
    class GetCrossing(Primitive):
        ...
    class GetCurrentThreadId(Primitive):
        ...
    class GetDefaultUIColor(Primitive):
        ...
    class GetDialogBitmap(Primitive):
        ...
    class GetDialogPos(Primitive):
        ...
    class GetDialogSize(Primitive):
        ...
    class GetDictKeyType(Primitive):
        ...
    class GetDictKeys(Primitive):
        ...
    class GetDictValue(Primitive):
        ...
    class GetDir(Primitive):
        ...
    class GetDisplayFilter(Primitive):
        ...
    class GetDisplayFilterName(Primitive):
        ...
    class GetEnableEditFbxSetting(Primitive):
        ...
    class GetEulerMatAngleRatio(Primitive):
        ...
    class GetEulerQuatAngleRatio(Primitive):
        ...
    class GetFileNameForMCGUserTool(MAXScriptFunction):
        ...
    class GetGridMajorLines(Primitive):
        ...
    class GetGridSpacing(Primitive):
        ...
    class GetImageBlurMultController(Primitive):
        ...
    class GetInheritVisibility(Primitive):
        ...
    class GetKeyStepsPos(Primitive):
        ...
    class GetKeyStepsRot(Primitive):
        ...
    class GetKeyStepsScale(Primitive):
        ...
    class GetKeyStepsSelOnly(Primitive):
        ...
    class GetKeyStepsUseTrans(Primitive):
        ...
    class GetMAXIniFile(Primitive):
        ...
    class GetMasterController(Primitive):
        ...
    class GetMatLibFileName(Primitive):
        ...
    class GetMaxAssertDisplay(Primitive):
        ...
    class GetMaxAssertLogFileName(Primitive):
        ...
    class GetMixerInterval(BipedGeneric):
        ...
    class GetNamedSelSetItem(Primitive):
        ...
    class GetNamedSelSetItemCount(Primitive):
        ...
    class GetNamedSelSetName(Primitive):
        ...
    class GetNodes(BipedGeneric):
        ...
    class GetNumAxis(Primitive):
        ...
    class GetNumNamedSelSets(Primitive):
        ...
    class GetNumberDisplayFilters(Primitive):
        ...
    class GetNumberSelectFilters(Primitive):
        ...
    class GetOptimizeDependentNotificationsStatistics(Primitive):
        ...
    class GetOrgTimeAtWarpedTime(BipedGeneric):
        ...
    class GetPModObjectNames(MAXScriptFunction):
        ...
    class GetPatchSteps(Primitive):
        ...
    class GetPersWorldPosForMouse(MAXScriptFunction):
        ...
    class GetPolygonCount(Primitive):
        ...
    class GetPosTaskWeight(Primitive):
        ...
    class GetQuietMode(Primitive):
        ...
    class GetRefCoordSys(Primitive):
        ...
    class GetRendApertureWidth(Primitive):
        ...
    class GetRendImageAspect(Primitive):
        ...
    class GetRenderID(Primitive):
        ...
    class GetRenderType(Primitive):
        ...
    class GetRotTaskWeight(Primitive):
        ...
    class GetScreenScaleFactor(Primitive):
        ...
    class GetSelectFilter(Primitive):
        ...
    class GetSelectFilterName(Primitive):
        ...
    class GetSelectedCATParent(MAXScriptFunction):
        ...
    class GetSelectedSubAnim(MAXScriptFunction):
        ...
    class GetShadeCVerts(Primitive):
        ...
    class GetSnapMode(Primitive):
        ...
    class GetSnapState(Primitive):
        ...
    class GetStandinProperty(Primitive):
        ...
    class GetStandinPropertyNames(Primitive):
        ...
    class GetTMController(Primitive):
        ...
    class GetTaskAxisState(Primitive):
        ...
    class GetToolBtnState(Primitive):
        ...
    class GetTrackInterval(BipedGeneric):
        ...
    class GetTrackgroupInterval(BipedGeneric):
        ...
    class GetTrajectoryON(Primitive):
        ...
    class GetTriMeshFaceCount(Primitive):
        ...
    class GetTwOrgTime(BipedGeneric):
        ...
    class GetTwWarpTime(BipedGeneric):
        ...
    class GetUIColor(Primitive):
        ...
    class GetUIScaleFactor(Primitive):
        ...
    class GetUseEnvironmentMap(Primitive):
        ...
    class GetVPortBGColor(Primitive):
        ...
    class GetVisController(Primitive):
        ...
    class GetWarpedTimeAtOrgTime(BipedGeneric):
        ...
    class GetWeight(BipedGeneric):
        ...
    class GetWeightAtTime(BipedGeneric):
        ...
    class GetWeightTime(BipedGeneric):
        ...
    class GhostFrameFragment(GraphicsFragmentPlugin):
        ...
    class GhostRenderFragment(GraphicsFragmentPlugin):
        ...
    class GhostWorldGenFragment(GraphicsFragmentPlugin):
        ...
    class GhostingManager(Interface):
        ...
    class GizmoFragment(GraphicsFragmentPlugin):
        ...
    class GlobalClipAssociation(ReferenceTarget):
        ...
    class GlobalMotionClip(MasterBlockController):
        ...
    class GlobalUtilityPlugin(MAXWrapperNonRefTarg):
        ...
    class Global_Clip_Associations(ReferenceTarget):
        ...
    class Global_Container(GeometryClass):
        ...
    class Global_Motion_Clip(MasterBlockController):
        ...
    class Glow_Element(ReferenceTarget):
        ALPHA: int
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        APPLYLIGHTS: bool
        APPLYNOISE: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        CENTERCOLOR: MXSWrapperBase
        CIRCULARCOLORMIX: float
        CIRCULARMAP: None
        CIRCULARMTL: None
        EDGECOLOR: MXSWrapperBase
        EFFECTSID: int
        ELEMENTNAME: str
        FILTERALL: bool
        FILTERBRIGHTNESS: bool
        FILTEREDGE: bool
        FILTERHUE: bool
        FILTERPERIMETER: bool
        FILTERPERIMETERALPHA: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        INTENSITY: float
        NOISEMAP: None
        OBJECTID: int
        OBJECTSHIDE: bool
        OCCLUSION: float
        ON: bool
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        QUADRANT4COLOR: MXSWrapperBase
        RADIALDENSITY: None
        RADIALMAP: None
        RADIALMTL: None
        RADIALSIZEMAP: None
        SIZE: float
        SOURCEALPHA: bool
        SOURCEEFFECTSID: bool
        SOURCEOBJECTID: bool
        SOURCESURFACENORMAL: bool
        SOURCEUNCLAMPEDCOLOR: bool
        SOURCEWHOLE: bool
        SOURCEZBUFFER: bool
        SQUEEZE: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        USECIRCULARMAP: bool
        USECIRCULARMTL: bool
        USERADIALDENSITY: bool
        USERADIALMAP: bool
        USERADIALMTL: bool
        USERADIALSIZEMAP: bool
        USESOURCECOLOR: float
        ZHI: float
        ZLO: float
        ...
    class Gnormal(TextureMap):
        BUMP_MAP: None
        BUMP_SPIN: float
        FLIPGREEN: bool
        FLIPRED: bool
        MAP1ON: bool
        MAP2ON: bool
        METHOD: int
        MULT_SPIN: float
        NORMAL_MAP: None
        SWAP_RG: bool
        ...
    class Go_To_Rotation(Helper):
        EASE_IN: float
        MATCH_INITIAL_SPIN: bool
        RANDOM_SEED: int
        SEND_OUT: bool
        SPINRATE: float
        SPIN_RATE_VARIATION: float
        STOP_SPINNING: bool
        TARGET_ROTATION: int
        TIME: int
        TRANSITION_TYPE: int
        VARIATION: int
        ...
    class Gradient(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COLOR2POS: float
        COLOR3: MXSWrapperBase
        COORDS: MXSWrapperBase
        GRADIENTTYPE: int
        MAP1: None
        MAP1ENABLED: bool
        MAP2: None
        MAP2ENABLED: bool
        MAP3: None
        MAP3ENABLED: bool
        NOISEAMOUNT: float
        NOISELEVELS: float
        NOISEPHASE: float
        NOISESIZE: float
        NOISETHRESHOLDHIGH: float
        NOISETHRESHOLDLOW: float
        NOISETHRESHOLDSMOOTH: float
        NOISETYPE: int
        OUTPUT: MXSWrapperBase
        ...
    class Gradient_GradCtlData(ReferenceTarget):
        ...
    class Gradient_Ramp(TextureMap):
        AMOUNT: float
        GRADIENT_TYPE: int
        HIGH_THRESHOLD: float
        LEVELS: float
        LOW_THRESHOLD: float
        NOISE_TYPE: int
        PHASE: float
        SIZE: float
        SOURCE_MAP_ON: int
        THRESHOLD_SMOOTHING: float
        ...
    class GraphicsFragmentPlugin(MAXWrapperNonRefTarg):
        ...
    class Gravitybinding(SpacewarpModifier):
        ...
    class Grip(Interface):
        ...
    class GripManager(GlobalUtilityPlugin):
        ...
    class GroupBoxControl(RolloutControl):
        ...
    class GroupEndControl(RolloutControl):
        ...
    class GroupOperator(Helper):
        EVENT_WITH_OPERATORS: None
        GROUP_SELECTION: None
        GROUP_SELECTION_OPERATORS: MXSWrapperBase
        SELECTION_CONDITION: int
        ...
    class GroupSelection(Helper):
        AGE_FROM: int
        AGE_TO: int
        AGE_VARIATION: int
        ANIMATED_SHAPE: bool
        CHANCE: float
        COLOR_COORDINATED: bool
        COMBINE_TYPE: int
        DIVERGENCE: float
        DIVERGENCE_VARIATION: float
        FLOAT_FROM: float
        FLOAT_TO: float
        FLOAT_VARIATION: float
        GROUP_A: None
        GROUP_B: None
        ICON_SIZE: float
        ICON_TYPE: int
        INDEX_FROM: int
        INDEX_TO: int
        INDEX_VARIATION: int
        INSIDE_OBJECT: None
        LOGO_SIZE: float
        PROPERTY_TYPE: int
        RANDOM_SEED: int
        REVERSE_SELECTION: bool
        SCALE_FROM: float
        SCALE_TO: float
        SCALE_VARIATION: float
        SELECTION_TYPE: int
        SIZE_FROM: float
        SIZE_TO: float
        SIZE_VARIATION: float
        SNAPSHOT_INDICES: MXSWrapperBase
        SNAPSHOT_PARTICLE_SYSTEM: int
        SNAPSHOT_TYPE: int
        SPEED_FROM: float
        SPEED_TO: float
        SPEED_VARIATION: float
        SUBFRAME_SAMPLING: bool
        UPDATE_TYPE: int
        ...
    class GroupStartControl(RolloutControl):
        ...
    class Group_Operator(Helper):
        EVENT_WITH_OPERATORS: None
        GROUP_SELECTION: None
        GROUP_SELECTION_OPERATORS: MXSWrapperBase
        SELECTION_CONDITION: int
        ...
    class Group_Select(Helper):
        AGE_FROM: int
        AGE_TO: int
        AGE_VARIATION: int
        ANIMATED_SHAPE: bool
        CHANCE: float
        COLOR_COORDINATED: bool
        COMBINE_TYPE: int
        DIVERGENCE: float
        DIVERGENCE_VARIATION: float
        FLOAT_FROM: float
        FLOAT_TO: float
        FLOAT_VARIATION: float
        GROUP_A: None
        GROUP_B: None
        ICON_SIZE: float
        ICON_TYPE: int
        INDEX_FROM: int
        INDEX_TO: int
        INDEX_VARIATION: int
        INSIDE_OBJECT: None
        LOGO_SIZE: float
        PROPERTY_TYPE: int
        RANDOM_SEED: int
        REVERSE_SELECTION: bool
        SCALE_FROM: float
        SCALE_TO: float
        SCALE_VARIATION: float
        SELECTION_TYPE: int
        SIZE_FROM: float
        SIZE_TO: float
        SIZE_VARIATION: float
        SNAPSHOT_INDICES: MXSWrapperBase
        SNAPSHOT_PARTICLE_SYSTEM: int
        SNAPSHOT_TYPE: int
        SPEED_FROM: float
        SPEED_TO: float
        SPEED_VARIATION: float
        SUBFRAME_SAMPLING: bool
        UPDATE_TYPE: int
        ...
    class HDIKSys(Interface):
        ...
    class HDRI(BitmapIO):
        ...
    class HKEY_CLASSES_ROOT(HKey):
        ...
    class HKEY_CURRENT_CONFIG(HKey):
        ...
    class HKEY_CURRENT_USER(HKey):
        ...
    class HKEY_LOCAL_MACHINE(HKey):
        ...
    class HKEY_PERFORMANCE_DATA(HKey):
        ...
    class HKEY_USERS(HKey):
        ...
    class HKey(Value):
        ...
    class HSDS(Modifier):
        AFFECTBACKFACE: bool
        BUBBLE: float
        CREASE: float
        DISPLAYLEVEL: int
        EDGEDISTANCE: int
        FALLOFF: float
        FORCEQUADS: bool
        IGNOREBACKFACE: bool
        LEVELOFDETAIL: int
        MATID: int
        ONLYCURRENTLEVEL: bool
        PINCH: float
        SMOOTHRESULT: bool
        USEEDGEDIST: bool
        USESOFTSEL: bool
        VERTEXTYPE: int
        ...
    class HSDSObject(Modifier):
        AFFECTBACKFACE: bool
        BUBBLE: float
        CREASE: float
        DISPLAYLEVEL: int
        EDGEDISTANCE: int
        FALLOFF: float
        FORCEQUADS: bool
        IGNOREBACKFACE: bool
        LEVELOFDETAIL: int
        MATID: int
        ONLYCURRENTLEVEL: bool
        PINCH: float
        SMOOTHRESULT: bool
        USEEDGEDIST: bool
        USESOFTSEL: bool
        VERTEXTYPE: int
        ...
    class HSDS_Modifier(Modifier):
        AFFECTBACKFACE: bool
        BUBBLE: float
        CREASE: float
        DISPLAYLEVEL: int
        EDGEDISTANCE: int
        FALLOFF: float
        FORCEQUADS: bool
        IGNOREBACKFACE: bool
        LEVELOFDETAIL: int
        MATID: int
        ONLYCURRENTLEVEL: bool
        PINCH: float
        SMOOTHRESULT: bool
        USEEDGEDIST: bool
        USESOFTSEL: bool
        VERTEXTYPE: int
        ...
    class HSUtil(ReferenceMaker):
        ...
    class Hair(Interface):
        ...
    class HairAtmospheric(Atmospheric):
        ...
    class HairAtmosphericGizmo(Helper):
        ...
    class HairEffect(RenderEffect):
        APPLYGI: bool
        COMPOSITIONMETHOD: int
        GI_MULTIPLIER: float
        HAIRMODE: int
        LIGHTINGMODE: int
        MBDURATION: float
        MBINTERVALTYPE: int
        MRVOXELRES: int
        OCCLUSIONNODES: MXSWrapperBase
        OCCLUSIONSETTYPE: int
        OVERSAMPLING: int
        RAYTRACE_REFLECTIONS_REFRACTIONS: bool
        SHADOWDENSITY: float
        TILEMEMORYUSAGE: int
        TRANSPARENCYDEPTH: int
        USEALLLIGHTS: bool
        ...
    class HairGIAtmospheric(Atmospheric):
        ...
    class HairLightAttr(CustAttrib):
        LIGHTHAIR: bool
        SHADOWFUZZ: float
        SHADOWRESOLUTION: int
        ...
    class HairMRGeomShader(TextureMap):
        ...
    class HairMRIntanceGeomShader(TextureMap):
        ...
    class HairMRObj(GeometryClass):
        ...
    class HairMaxUtility(UtilityPlugin):
        ...
    class HairMod(SpacewarpModifier):
        AUTOCOLLISION: bool
        BYVERTEX: bool
        CLUMPS: int
        CLUMPSCOLORS: float
        CLUMPSFLAT: float
        CLUMPSOFFSET: float
        CLUMPSRAND: float
        CLUMPSROT: float
        CLUMPSSCRUFF: float
        CLUMPSSTREN: float
        COLLISIONMETHOD: int
        COLLISIONNODES: MXSWrapperBase
        DISPLAYGUIDECOLOR: MXSWrapperBase
        DISPLAYHAIRASGEOMETRY: bool
        DISPLAYHAIRCOLOR: MXSWrapperBase
        DISPLAYHAIRPERCENT: float
        DISPLAYMAXHAIRS: int
        DISPLAYOVERRIDEHAIRCOLOR: bool
        DISPLAYSHOWGUIDES: bool
        DISPLAYSHOWHAIRS: bool
        DYNAMICSDAMPEN: float
        DYNAMICSGRAVITY: float
        DYNAMICSMODE: int
        DYNAMICSROOTHOLD: float
        DYNAMICSSTIFFNESS: float
        FLYAWAYPERC: int
        FLYAWAYSTREN: float
        FORCEFIELDS: MXSWrapperBase
        FRIZZANIM: float
        FRIZZANIMDIR: MXSWrapperBase
        FRIZZANIMSPEED: float
        FRIZZFREQX: float
        FRIZZFREQY: float
        FRIZZFREQZ: float
        FRIZZROOT: float
        FRIZZTIP: float
        HAIRCOUNT: int
        HAIRCUTLENGTH: float
        HAIRDENSITY: float
        HAIRDISPLACEMENT: float
        HAIRINTERPOLATEGUIDES: bool
        HAIRPASSES: int
        HAIRRANDSCALE: float
        HAIRROOTTHICKNESS: float
        HAIRSCALE: float
        HAIRSEGMENTS: int
        HAIRTIPTHICKNESS: float
        IGNOREBACKFACING: bool
        INSTANCEGEOMNAME: str
        KINKFREQX: float
        KINKFREQY: float
        KINKFREQZ: float
        KINKROOT: float
        KINKTIP: float
        MAPENABLES: MXSWrapperBase
        MAPS: MXSWrapperBase
        MATERIALGEOMMTLID: int
        MATERIALGEOMSHADOW: float
        MATERIALGLOSSNESS: float
        MATERIALHUEVARIATION: float
        MATERIALMUTANTHAIRCOLOR: MXSWrapperBase
        MATERIALOCCLUDEDAMB: float
        MATERIALPERCENTMUTANTHAIR: float
        MATERIALROOTCOLOR: MXSWrapperBase
        MATERIALSELFSHADOW: float
        MATERIALSPECTINT2: MXSWrapperBase
        MATERIALSPECTINT: MXSWrapperBase
        MATERIALSPECULAR: float
        MATERIALSQUIRREL: bool
        MATERIALTIPCOLOR: MXSWrapperBase
        MATERIALTIPFADE: bool
        MATERIALVALUEVARIATION: float
        MERGEINSTANCEMATERIAL: bool
        MESSSTREN: float
        MR_APPLYSHADER: bool
        MR_SHADER: None
        MR_SUBMTLSTOREPLACE: MXSWrapperBase
        MULTIRANDOMIZE: float
        MULTISTRANDASPECT: float
        MULTISTRANDCOUNT: int
        MULTISTRANDOFFSET: float
        MULTISTRANDROOTSPLAY: float
        MULTISTRANDTIPSPLAY: float
        MULTISTRANDTWIST: float
        RANDOMSEED: int
        SIMULATIONEND: int
        SIMULATIONSTART: int
        TOOLSSPLINELOCKNODE: None
        ...
    class HairRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class Hair_Atmospheric(Atmospheric):
        ...
    class Hair_Atmospheric_Gizmo(Helper):
        ...
    class Hair_GI_Atmospheric(Atmospheric):
        ...
    class Hair_Instanced_Geometry_MR_Shader(TextureMap):
        ...
    class Hair_MR_Geom_Shader(TextureMap):
        ...
    class Hair_MR_Object(GeometryClass):
        ...
    class HalfRound(Shape):
        ...
    class Hammersley(SamplerClass):
        ENABLE: bool
        QUALITY: float
        SUB_SAMPLE_TEXTURES: bool
        ...
    class HasDictValue(Primitive):
        ...
    class HashTable(Value):
        ...
    class HdlObjObj(Helper):
        ...
    class HdlTrans(Matrix3Controller):
        ...
    class Hedra(GeometryClass):
        FAMILY: int
        MAPCOORDS: bool
        P: float
        Q: float
        RADIUS: float
        SCALEP: float
        SCALEQ: float
        SCALER: float
        VERTICES: MXSWrapperBase
        VERTTYPE: int
        ...
    class HeightMap(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        TARGETMAPSLOTNAME: str
        ...
    class Helix(Shape):
        ANGLE: float
        BIAS: float
        CAP: bool
        CAP_SEGMENTS: int
        DIRECTION: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        HEIGHT: float
        MAPCOORDS: bool
        QUAD_CAP: bool
        RADIUS1: float
        RADIUS2: float
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        THICKNESS: float
        TURNS: float
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        ...
    class HelpSystem(Interface):
        ...
    class HiddenDOSCommand(Primitive):
        ...
    class HiddenUnselectedNodeCache(ReferenceTarget):
        ...
    class HitByNameDlg(Primitive):
        ...
    class Hose(GeometryClass):
        BOTTOM_TENSION: float
        D_SECTION_HOSE_DEPTH: float
        D_SECTION_HOSE_FILLET_SEGS: int
        D_SECTION_HOSE_FILLET_SIZE: float
        D_SECTION_HOSE_ROUND_SEGS: int
        D_SECTION_HOSE_SECTION_ROTATION: float
        D_SECTION_HOSE_WIDTH: float
        END_PLACEMENT_METHOD: int
        FLEX_CYCLE_COUNT: int
        FLEX_SECTION_DIAMETER: float
        FLEX_SECTION_ENABLED: int
        FLEX_SECTION_START: float
        FLEX_SECTION_STOP: float
        GENERATE_MAPPING_COORDINATES: int
        HOSE_CROSS_SECTION_TYPE: int
        HOSE_HEIGHT: float
        RECTANGULAR_HOSE_DEPTH: float
        RECTANGULAR_HOSE_FILLET_SEGS: int
        RECTANGULAR_HOSE_FILLET_SIZE: float
        RECTANGULAR_HOSE_SECTION_ROTATION: float
        RECTANGULAR_HOSE_WIDTH: float
        RENDERABLE_HOSE: int
        ROUND_HOSE_DIAMETER: float
        ROUND_HOSE_SIDES: int
        SEGMENTS_ALONG_HOSE: int
        SMOOTH_SPRING: int
        TOP_TENSION: float
        ...
    class HotspotManip(Helper):
        ...
    class Hotspot_Manip(Helper):
        ...
    class Hub(Matrix3Controller):
        ...
    class HubObject(GeometryClass):
        ...
    class HubTrans(Matrix3Controller):
        ...
    class IAutoCamMax(Interface):
        ...
    class IBitmapPager(Interface):
        ...
    class ICEFlowFileBirthSetup(Interface):
        ...
    class ICEFlowShapeControl(Interface):
        ...
    class ICEFlowSystemFactory(Interface):
        ...
    class IContainerManagerPrivate(Interface):
        ...
    class IDataChannelEngineClass(MAXWrapper):
        ...
    class IES_Sky(Light):
        CASTSHADOWS: bool
        COLOR: MXSWrapperBase
        MULTIPLIER: float
        ON: bool
        RAYS_PER_SAMPLE: int
        RAY_BIAS: float
        SKY_COVER: float
        ...
    class IES_Sun(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        HASTARGET: bool
        MULTIPLIER: float
        ON: bool
        RGB: MXSWrapperBase
        SHADOWMULTIPLIER: float
        SOFTENDIFFUSEEDGE: float
        TARGETDISTANCE: None
        USEGLOBALSHADOWSETTINGS: bool
        ...
    class IFL(BitmapIO):
        ...
    class IFL_Manager(UtilityPlugin):
        ...
    class IGES_Export(ExporterPlugin):
        ...
    class IInteractionMode(Interface):
        ...
    class IKChainControl(Matrix3Controller):
        ...
    class IKControl(Matrix3Controller):
        ...
    class IKEndSpTwistManip(Helper):
        ...
    class IKHISolver(IKSolver):
        ...
    class IKLimb(IKSolver):
        ...
    class IKSolver(MAXWrapperNonRefTarg):
        ...
    class IKStartSpTwistManip(Helper):
        ...
    class IKSwivelManip(Helper):
        ...
    class IKSys(Interface):
        ...
    class IKTargTrans(Matrix3Controller):
        ...
    class IKTarget(Helper):
        ...
    class IKTargetObj(Helper):
        ...
    class IK_Chain_Object(Helper):
        ...
    class IK_Controller(ReferenceTarget):
        ...
    class IK_ControllerMatrix3Controller(Matrix3Controller):
        ...
    class IK_Position_Controller(PositionController):
        ...
    class IK_Spline_End_Twist_Manip(Helper):
        ...
    class IK_Spline_Start_Twist_Manip(Helper):
        ...
    class IK_Swivel_Manip(Helper):
        ...
    class ILightRef(Interface):
        ...
    class IMetaDataManager(Interface):
        ...
    class IObject(Value):
        ...
    class IPathConfigMgr(Interface):
        ...
    class IRTShadeTreeCompiler(Interface):
        ...
    class IShaderManagerCreator(Interface):
        ...
    class ISubstance(Interface):
        ...
    class ITabDialogManager(Interface):
        ...
    class IViewportShadingMgr(Interface):
        ...
    class Identity(MappedGeneric):
        ...
    class IdleAreaAddArea(Primitive):
        ...
    class IdleAreaCreateCircle(Primitive):
        ...
    class IdleAreaCreateFreeform(Primitive):
        ...
    class IdleAreaCreateRectangle(Primitive):
        ...
    class IdleAreaObj(GeometryClass):
        DENSITY: float
        GENDER: float
        GROUPS: float
        ID: int
        LOOKAT: None
        LOOKATOBJ: None
        ORIENT: float
        ORIENTSPREAD: float
        PAIR: float
        RANDSEEDGEN: int
        RANDSEEDGROUP: int
        RANDSEEDINDIV: int
        RANDSEEDMTN: int
        RANDSEEDROT: int
        ...
    class IdleAreaSubtractArea(Primitive):
        ...
    class IesSkyLight(Light):
        CASTSHADOWS: bool
        COLOR: MXSWrapperBase
        MULTIPLIER: float
        ON: bool
        RAYS_PER_SAMPLE: int
        RAY_BIAS: float
        SKY_COVER: float
        ...
    class IlluminanceFragment(GraphicsFragmentPlugin):
        ...
    class IlluminanceRenderElement(RenderElement):
        ATMOSPHEREON: bool
        BITMAP: None
        ELEMENTNAME: str
        ENABLEDON: bool
        FILTERON: bool
        SCALEFACTOR: float
        SHADOWON: bool
        ...
    class Illuminance_HDR_Data(RenderElement):
        ATMOSPHEREON: bool
        BITMAP: None
        ELEMENTNAME: str
        ENABLEDON: bool
        FILTERON: bool
        SCALEFACTOR: float
        SHADOWON: bool
        ...
    class Illuminance_Render_Element(RenderElement):
        ...
    class Illumination_Render_Element(RenderElement):
        ...
    class ImgTag(RolloutControl):
        ...
    class ImportHTR(ImporterPlugin):
        ...
    class ImportTRC(ImporterPlugin):
        ...
    class ImporterPlugin(MAXWrapperNonRefTarg):
        ...
    class InchesToSystemScale(MAXScriptFunction):
        ...
    class IndirectRefTargContainer(ReferenceTarget):
        ...
    class InfluenceHelper(Helper):
        BIAS: float
        BIASSELECTED: bool
        ENABLEBIAS: bool
        FALLOFFTYPE: int
        FARCOLOR: MXSWrapperBase
        FARDIST: float
        INVERT: bool
        NEARCOLOR: MXSWrapperBase
        NEARDIST: float
        ON: bool
        SHOWFAR: bool
        SHOWNEAR: bool
        ...
    class InitialState(Helper):
        AUTO_SYNC_EMIT_TIME: bool
        COLOR_COORDINATED: bool
        DIVERGENCE: float
        EMIT_TIME: int
        ICON_SIZE: float
        LOCK_POSITION: bool
        LOCK_SPEED: bool
        MAGNITUDE_VARIATION: float
        MAX_SPREAD: float
        PARTICLE_SYSTEM: None
        RANDOM_SEED: int
        SELECTED_EVENTS: MXSWrapperBase
        STATE_FROM_TYPE: int
        USE_AGE: bool
        USE_MAPPING: bool
        USE_MATERIAL_ID: bool
        USE_ROTATION: bool
        USE_SCALE: bool
        USE_SCRIPT_DATA: bool
        USE_SELECTION: bool
        USE_SHAPE: bool
        USE_SPEED: bool
        USE_SPIN: bool
        ...
    class Initial_State(Helper):
        AUTO_SYNC_EMIT_TIME: bool
        COLOR_COORDINATED: bool
        DIVERGENCE: float
        EMIT_TIME: int
        ICON_SIZE: float
        LOCK_POSITION: bool
        LOCK_SPEED: bool
        MAGNITUDE_VARIATION: float
        MAX_SPREAD: float
        PARTICLE_SYSTEM: None
        RANDOM_SEED: int
        SELECTED_EVENTS: MXSWrapperBase
        STATE_FROM_TYPE: int
        USE_AGE: bool
        USE_MAPPING: bool
        USE_MATERIAL_ID: bool
        USE_ROTATION: bool
        USE_SCALE: bool
        USE_SCRIPT_DATA: bool
        USE_SELECTION: bool
        USE_SHAPE: bool
        USE_SPEED: bool
        USE_SPIN: bool
        ...
    class InitializeTimeWarp(BipedGeneric):
        ...
    class Ink(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class InkNPaint(Material):
        BACKFACE_ERROR_COLOR: MXSWrapperBase
        BACKFACE_ERROR_ON: bool
        BUMP_MAP: None
        BUMP_MAP_AMT: float
        BUMP_MAP_ON: bool
        COLOR1: MXSWrapperBase
        DSP_MAP: None
        DSP_MAP_AMT: float
        DSP_MAP_ON: bool
        EDGE_ANG_INK_COLOR: MXSWrapperBase
        EDGE_ANG_INK_MAP: None
        EDGE_ANG_INK_MAP_AMT: float
        EDGE_ANG_INK_MAP_ON: bool
        EDGE_ANG_INK_ON: bool
        EDGE_ANG_THRESH: float
        FACETED_ON: bool
        FACE_MAP_ON: bool
        FOG_BG: bool
        INIT_FAIL_COLOR: MXSWrapperBase
        INIT_FAIL_ON: bool
        INK_AUTO_VARY_ON: bool
        INK_ON: bool
        INK_QUALITY: int
        INK_WIDTH_CLAMP_ON: bool
        INTERSECT_BIAS: float
        MAT1: None
        MAT1_ON: bool
        MATID_ADJ_REQ_ON: bool
        MATID_INK_COLOR: MXSWrapperBase
        MATID_INK_ON: bool
        MATID_INTERSECT_BIAS: float
        MATID_MAP: None
        MATID_MAP_AMT: float
        MATID_MAP_ON: bool
        MAX_INK_WIDTH: float
        MIN_INK_WIDTH: float
        MISSED_RAYS_ERROR_COLOR: MXSWrapperBase
        MISSED_RAYS_ERROR_ON: bool
        OPAQUE_ALPHA_ON: bool
        OUT_INK_MAP: None
        OUT_INK_MAP_AMT: float
        OUT_INK_MAP_ON: bool
        OUT_INK_ON: bool
        PAINT_COLOR: MXSWrapperBase
        PAINT_LEVELS: int
        PAINT_MAP: None
        PAINT_MAP_AMT: float
        PAINT_MAP_ON: bool
        PAINT_ON: bool
        PIXEL_GRID_ON: bool
        SAMPLER: int
        SAMPLERADAPTON: bool
        SAMPLERADAPTTHRESHOLD: float
        SAMPLERADVANCEDOPTIONS: bool
        SAMPLERBYNAME: str
        SAMPLERENABLE: bool
        SAMPLERQUALITY: float
        SAMPLERUSEGLOBAL: bool
        SELF_OVERLAP_BIAS: float
        SELF_OVERLAP_INK_COLOR: MXSWrapperBase
        SELF_OVERLAP_INK_MAP: None
        SELF_OVERLAP_INK_MAP_AMT: float
        SELF_OVERLAP_INK_MAP_ON: bool
        SELF_OVERLAP_INK_ON: bool
        SELF_UNDERLAP_BIAS: float
        SELF_UNDERLAP_INK_COLOR: MXSWrapperBase
        SELF_UNDERLAP_INK_MAP: None
        SELF_UNDERLAP_INK_MAP_AMT: float
        SELF_UNDERLAP_INK_MAP_ON: bool
        SELF_UNDERLAP_INK_ON: bool
        SHADE_AMT: float
        SHADE_AMT_ON: bool
        SHADE_COLOR: MXSWrapperBase
        SHADE_COLOR_MAP: None
        SHADE_COLOR_MAP_AMT: float
        SHADE_COLOR_MAP_ON: bool
        SMGROUP_EDGE_INK_COLOR: MXSWrapperBase
        SMGROUP_EDGE_INK_ON: bool
        SMGROUP_EDGE_MAP: None
        SMGROUP_EDGE_MAP_AMT: float
        SMGROUP_EDGE_MAP_ON: bool
        SPEC_COLOR: MXSWrapperBase
        SPEC_GLOSS: float
        SPEC_MAP: None
        SPEC_MAP_AMT: float
        SPEC_MAP_ON: bool
        SPEC_ON: bool
        SUBSAMPLETEXTUREON: bool
        SUB_MTL_AMT: float
        TWO_SIDE_ON: bool
        USERPARAM0: float
        USERPARAM1: float
        WIDTH_MAP: None
        WIDTH_MAP_AMT: float
        WIDTH_MAP_ON: bool
        ...
    class InkRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class Inline(Helper):
        ...
    class InputCustom(ReferenceTarget):
        DATA_CHANNEL: None
        DATA_HANDLE: int
        FILTER: None
        I3_USAGE: int
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        USE_I2: bool
        USE_PROXY_PARTICLES: bool
        ...
    class InputPhysX(ReferenceTarget):
        COLLISION_TYPE: int
        DATA_TYPE: int
        FILTER: None
        MATCH_TYPE: int
        THRESHOLD_TYPE: int
        ...
    class InputProxy(ReferenceTarget):
        ACCELERATION_TYPE: int
        ADJUSTED_BY_SCALE: bool
        DATA_TYPE: int
        FILTER: None
        GROUP_SELECTION_OPERATOR: None
        GROUP_TYPE: int
        I3_USAGE: int
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        MAPPING_TYPE: int
        MAP_CHANNEL: int
        PARTICLEID_TYPE: int
        POSITION_TYPE: int
        ROTATION_TYPE: int
        SCALE_TYPE: int
        SCRIPT_TYPE: int
        SHAPE_TYPE: int
        SIZE_TYPE: int
        SPEED_TYPE: int
        SPIN_TYPE: int
        TIME_TYPE: int
        TM_TYPE: int
        USE_E4: bool
        USE_I2: bool
        ...
    class InputStandard(ReferenceTarget):
        ACCELERATION_TYPE: int
        ADJUSTED_BY_SCALE: bool
        DATA_TYPE: int
        FILTER: None
        GROUP_SELECTION_OPERATOR: None
        GROUP_TYPE: int
        INPUT_1: None
        INPUT_2: None
        MAPPING_TYPE: int
        MAP_CHANNEL: int
        PARTICLEID_TYPE: int
        POSITION_TYPE: int
        ROTATION_TYPE: int
        SCALE_TYPE: int
        SCRIPT_TYPE: int
        SHAPE_TYPE: int
        SIZE_TYPE: int
        SPEED_TYPE: int
        SPIN_TYPE: int
        TIME_TYPE: int
        TM_TYPE: int
        USE_E1: bool
        VIEWPORT_RENDER_OPERATOR: None
        VISIBILITY_TYPE: int
        ...
    class Input_Proxy(ReferenceTarget):
        ACCELERATION_TYPE: int
        ADJUSTED_BY_SCALE: bool
        DATA_TYPE: int
        FILTER: None
        GROUP_SELECTION_OPERATOR: None
        GROUP_TYPE: int
        I3_USAGE: int
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        MAPPING_TYPE: int
        MAP_CHANNEL: int
        PARTICLEID_TYPE: int
        POSITION_TYPE: int
        ROTATION_TYPE: int
        SCALE_TYPE: int
        SCRIPT_TYPE: int
        SHAPE_TYPE: int
        SIZE_TYPE: int
        SPEED_TYPE: int
        SPIN_TYPE: int
        TIME_TYPE: int
        TM_TYPE: int
        USE_E4: bool
        USE_I2: bool
        ...
    class Input_MParticles(ReferenceTarget):
        COLLISION_TYPE: int
        DATA_TYPE: int
        FILTER: None
        MATCH_TYPE: int
        THRESHOLD_TYPE: int
        ...
    class InsertWarpAtOrgTime(BipedGeneric):
        ...
    class InstanceDuplMap(UtilityPlugin):
        ...
    class InstanceMgr(Interface):
        ...
    class InstanceMgrWrapper(FloatController):
        ...
    class Instance_Duplicate_Maps(UtilityPlugin):
        ...
    class Instance_Manager_Wrapper(FloatController):
        ...
    class Int64Packet(ReferenceMaker):
        ...
    class IntPacket(ReferenceMaker):
        ...
    class Integer64(Value):
        ...
    class IntegerPtr(Value):
        ...
    class Interface(Value):
        ...
    class InterfaceFunction(Value):
        ...
    class InterfaceIDRegistry(Interface):
        ...
    class IntersectRayEx(Primitive):
        ...
    class Interval(Value):
        ...
    class InvalidateAllBackgrounds(Primitive):
        ...
    class InventorImport(ImporterPlugin):
        ...
    class Inverse(Generic):
        ...
    class InverseHighPrecision(Primitive):
        ...
    class IsBoneOnly(Primitive):
        ...
    class IsCATEntity(MAXScriptFunction):
        ...
    class IsCPEdgeOnInView(Primitive):
        ...
    class IsCwsImgType(MAXScriptFunction):
        ...
    class IsDialogVisible(Primitive):
        ...
    class IsFloatController(MAXScriptFunction):
        ...
    class IsLayerControl(MAXScriptFunction):
        ...
    class IsModuleLoaded(Primitive):
        ...
    class IsNetServer(Primitive):
        ...
    class IsNetworkRenderServer(Primitive):
        ...
    class IsPointSelected(Primitive):
        ...
    class IsSceneRedrawDisabled(Primitive):
        ...
    class IsSelectionSubAnimClassOf(MAXScriptFunction):
        ...
    class IsShapeObject(Primitive):
        ...
    class IsSpaceWarpValid(Primitive):
        ...
    class IsSubSelEnabled(Primitive):
        ...
    class IsSurfaceUVClosed(Primitive):
        ...
    class IsTimeWarpActive(BipedGeneric):
        ...
    class IsUndoDisabled(Primitive):
        ...
    class IsValidControllerSelection(MAXScriptFunction):
        ...
    class IsValidMorpherMod(Primitive):
        ...
    class IsolateSelection(Interface):
        ...
    class IsolatedVertexClass(GlobalUtilityPlugin):
        ...
    class IsolatedVertices(Interface):
        ...
    class Isolated_Vertices(GlobalUtilityPlugin):
        ...
    class JAngleData(ReferenceTarget):
        ...
    class JBinaryData(ReferenceTarget):
        ...
    class JBoolData(ReferenceTarget):
        ...
    class JColor3Data(ReferenceTarget):
        ...
    class JColorData(ReferenceTarget):
        ...
    class JFlagCtlData(ReferenceTarget):
        ...
    class JFlagSetData(ReferenceTarget):
        ...
    class JFloat3Data(ReferenceTarget):
        ...
    class JFloatData(ReferenceTarget):
        ...
    class JGradCtlData(ReferenceTarget):
        ...
    class JPEG(BitmapIO):
        ...
    class JPercent3Data(ReferenceTarget):
        ...
    class JPercentData(ReferenceTarget):
        ...
    class JSubtex(ReferenceTarget):
        ...
    class JWorld3Data(ReferenceTarget):
        ...
    class JWorldData(ReferenceTarget):
        ...
    class Join_Bodies(GeometryClass):
        BREPOPERATION: int
        MAKEINTOSOLID: bool
        TOBREPOBJECTHELP: bool
        ...
    class Joint_Angle_Deformer(ReferenceTarget):
        ...
    class Joystick_Input_Device(ReferenceTarget):
        ...
    class Joystick_Input_DeviceMotionCaptureDeviceBindingClass(MotionCaptureDeviceBindingClass):
        ...
    class Joystick_Input_DeviceMotionCaptureDeviceClass(MotionCaptureDeviceClass):
        ...
    class Keep_Apart(Helper):
        ACCEL_LIMIT: float
        CORE_PERCENTAGE: float
        CORE_SIZE: float
        FALLOFF_PERCENTAGE: float
        FALLOFF_SIZE: float
        FORCE: float
        RANDOM_SEED: int
        RANGE_TYPE: int
        SCOPE_TYPE: int
        SELECTED_EVENTS: MXSWrapperBase
        SELECTED_SYSTEMS: MXSWrapperBase
        SPEED_LIMIT: float
        USE_ACCEL_LIMIT: bool
        USE_SCRIPT_FLOAT: int
        USE_SCRIPT_VECTOR: int
        USE_SPEED_LIMIT: bool
        VARIATION: float
        ...
    class KeyValueUtility(TrackViewUtility):
        ...
    class Keyboard_Input_Device(MotionCaptureDeviceClass):
        ...
    class Keyboard_Input_DeviceMotionCaptureDeviceBindingClass(MotionCaptureDeviceBindingClass):
        ...
    class KindOfRenderElement(MAXScriptFunction):
        ...
    class KneeAngle(FloatController):
        ...
    class LOD(Helper):
        ...
    class LOD_Controller(FloatController):
        ...
    class LTypeStair(GeometryClass):
        ANGLE: float
        CARRIAGECONTEXT: int
        CARRIAGECOUNT: int
        CARRIAGEEXTOFFS: float
        CARRIAGEHEIGHT: float
        CARRIAGEINTOFFS: float
        CARRIAGESPACE: float
        CARRIAGESPACINGTYPE: int
        CARRIAGESPRINGFLOOR: bool
        CARRIAGEWIDTH: float
        GENERATECARRIAGE: bool
        GENERATEINSIDERAILING: bool
        GENERATEMAPPING: bool
        GENERATEOUTSIDERAILING: bool
        GENERATESTRINGERS: bool
        LENGTH2: float
        LENGTH: float
        RAILINGHEIGHT: float
        RAILINGOFFS: float
        RAILINGRADIUS: float
        RAILINGSEGMENTS: int
        STEPCOUNT: int
        STEPDEPTH: float
        STEPDEPTH_X: bool
        STEPHEIGHT: float
        STEPTHICKNESS: float
        STEPTYPE: int
        STEPWIDTH: float
        STRINGERDEPTH: float
        STRINGEROFFSET: float
        STRINGERSPRINGFLOOR: bool
        STRINGERWIDTH: float
        UPPEROFFSET: float
        ...
    class LZFlare_AutoSec_Base(ReferenceTarget):
        ...
    class LZFlare_AutoSec_Data(ReferenceTarget):
        ...
    class LZFlare_Aux_Data(ReferenceTarget):
        ...
    class LZFlare_Data(ReferenceTarget):
        ...
    class LZFlare_Glow_Data(ReferenceTarget):
        ...
    class LZFlare_Inferno_Data(ReferenceTarget):
        ...
    class LZFlare_ManSec_Base(ReferenceTarget):
        ...
    class LZFlare_ManSec_Data(ReferenceTarget):
        ...
    class LZFlare_Prefs_Data(ReferenceTarget):
        ...
    class LZFlare_Rays_Data(ReferenceTarget):
        ...
    class LZFlare_Rend_Data(ReferenceTarget):
        ...
    class LZFlare_Ring_Data(ReferenceTarget):
        ...
    class LZFlare_Star_Data(ReferenceTarget):
        ...
    class LZFlare_Streak_Data(ReferenceTarget):
        ...
    class LZFocus_Data(ReferenceTarget):
        ...
    class LZGlow_Aux_Data(ReferenceTarget):
        ...
    class LZGlow_Data(ReferenceTarget):
        ...
    class LZGlow_Rend_Data(ReferenceTarget):
        ...
    class LZHilight_Aux_Data(ReferenceTarget):
        ...
    class LZHilight_Data(ReferenceTarget):
        ...
    class LZHilight_Rend_Data(ReferenceTarget):
        ...
    class L_Ext(GeometryClass):
        CENTERCREATE: bool
        FRONT_LENGTH: float
        FRONT_SEGMENTS: int
        FRONT_WIDTH: float
        HEIGHT: float
        HEIGHT_SEGMENTS: int
        MAPCOORDS: bool
        SIDE_LENGTH: float
        SIDE_SEGMENTS: int
        SIDE_WIDTH: float
        TYPEINCREATIONMETHOD: int
        TYPEINFRONTLENGTH: float
        TYPEINFRONTWIDTH: float
        TYPEINHEIGHT: float
        TYPEINPOS: MXSWrapperBase
        TYPEINSIDELENGTH: float
        TYPEINSIDEWIDTH: float
        WIDTH_SEGMENTS: int
        ...
    class L_Type_Stair(GeometryClass):
        ANGLE: float
        CARRIAGECONTEXT: int
        CARRIAGECOUNT: int
        CARRIAGEEXTOFFS: float
        CARRIAGEHEIGHT: float
        CARRIAGEINTOFFS: float
        CARRIAGESPACE: float
        CARRIAGESPACINGTYPE: int
        CARRIAGESPRINGFLOOR: bool
        CARRIAGEWIDTH: float
        GENERATECARRIAGE: bool
        GENERATEINSIDERAILING: bool
        GENERATEMAPPING: bool
        GENERATEOUTSIDERAILING: bool
        GENERATESTRINGERS: bool
        LENGTH2: float
        LENGTH: float
        RAILINGHEIGHT: float
        RAILINGOFFS: float
        RAILINGRADIUS: float
        RAILINGSEGMENTS: int
        STEPCOUNT: int
        STEPDEPTH: float
        STEPDEPTH_X: bool
        STEPHEIGHT: float
        STEPTHICKNESS: float
        STEPTYPE: int
        STEPWIDTH: float
        STRINGERDEPTH: float
        STRINGEROFFSET: float
        STRINGERSPRINGFLOOR: bool
        STRINGERWIDTH: float
        UPPEROFFSET: float
        ...
    class LabelControl(RolloutControl):
        ...
    class LandXMLImport(ImporterPlugin):
        ...
    class LandXML___DEM_Model_Import(ImporterPlugin):
        ...
    class Lathe(Modifier):
        CAPEND: bool
        CAPSTART: bool
        CAPTYPE: int
        DEGREES: float
        FLIPNORMALS: bool
        MAPCOORDS: bool
        MATIDS: bool
        OUTPUT: int
        SEGS: int
        SMOOTH: bool
        USESHAPEIDS: bool
        WELDCORE: bool
        ...
    class Lattice(Modifier):
        JOINT_RADIUS: float
        JOINT_SEGS: int
        STRUT_RADIUS: float
        STRUT_SEGMENTS: int
        STRUT_SIDES: int
        ...
    class LayerFloat(FloatController):
        ...
    class LayerInfo(FloatController):
        ...
    class LayerManager(Interface):
        ...
    class LayerMatrix3(Matrix3Controller):
        ...
    class LayerRoot(FloatController):
        ...
    class LayerTransform(Matrix3Controller):
        ...
    class LayerWeights(FloatController):
        ...
    class Layer_Manager(ReferenceTarget):
        ...
    class Layer_Output(FloatController):
        ...
    class LegWeight(FloatController):
        ...
    class Lens_Effects(RenderEffect):
        AFFECTALPHA: bool
        AFFECTBYATMOSPHERE: bool
        AFFECTZBUFFER: bool
        ANGLE: float
        CENTERAFFECTSINTENSITY: bool
        CENTERAFFECTSSIZE: bool
        DISTAFFECTSINTENSITY: bool
        DISTAFFECTSSIZE: bool
        INNEROCCLUSIONRADIUS: float
        INTENSITY: float
        LIGHTDIRECTIONAFFECTSINTENSITY: bool
        LIGHTDIRECTIONAFFECTSSIZE: bool
        OCCLUSIONAFFECTSINTENSITY: bool
        OCCLUSIONAFFECTSSIZE: bool
        OUTEROCCLUSIONRADIUS: float
        SEED: int
        SIZE: float
        SQUEEZE: float
        ...
    class Lens_Effects_Flare_Filter(VideoPostFilter):
        ...
    class Lens_Effects_Focus_Filter(VideoPostFilter):
        ...
    class Lens_Effects_Glow_Filter(VideoPostFilter):
        ...
    class Lens_Effects_Hilight_Filter(VideoPostFilter):
        ...
    class Level_Of_Detail(UtilityPlugin):
        ...
    class LightCreationZHeight(MAXScriptFunction):
        ...
    class LightMap(ReferenceTarget):
        DIFFUSE_FILENAME: str
        DIFFUSE_MAPPING: int
        DIFFUSE_ON: bool
        DIFFUSE_TEXTURE: None
        LIGHTMAP_FILENAME: str
        LIGHTMAP_MAPPING: int
        LIGHTMAP_ON: bool
        LIGHTMAP_TEXTURE: None
        ...
    class LightMeter(Helper):
        ...
    class LightMeterManager(Interface):
        ...
    class LightTrace(RadiosityEffect):
        ADAPTIVE_UNDERSAMPLING_ON: bool
        BOUNCES: int
        COLOR_BLEED: float
        COLOR_FILTER: MXSWrapperBase
        CONE_ANGLE: float
        EXTRA_AMBIENT: MXSWrapperBase
        FILTER_SIZE: float
        GLOBAL_MULTIPLIER: float
        INITIAL_SAMPLE_SPACING: int
        OBJECT_MULTIPLIER: float
        RAYS: int
        RAY_BIAS: float
        SHOW_SAMPLES: bool
        SKY_LIGHTS: float
        SKY_LIGHTS_ON: bool
        SUBDIVIDE_DOWN_TO: int
        SUBDIVISION_CONTRAST: float
        VOLUMES: float
        VOLUMES_ON: bool
        ...
    class Light_RollAngle_Manipulator(Helper):
        ...
    class Light_Tracer(RadiosityEffect):
        ADAPTIVE_UNDERSAMPLING_ON: bool
        BOUNCES: int
        COLOR_BLEED: float
        COLOR_FILTER: MXSWrapperBase
        CONE_ANGLE: float
        EXTRA_AMBIENT: MXSWrapperBase
        FILTER_SIZE: float
        GLOBAL_MULTIPLIER: float
        INITIAL_SAMPLE_SPACING: int
        OBJECT_MULTIPLIER: float
        RAYS: int
        RAY_BIAS: float
        SHOW_SAMPLES: bool
        SKY_LIGHTS: float
        SKY_LIGHTS_ON: bool
        SUBDIVIDE_DOWN_TO: int
        SUBDIVISION_CONTRAST: float
        VOLUMES: float
        VOLUMES_ON: bool
        ...
    class Lighting(RenderElement):
        BITMAP: None
        DIRECTON: bool
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        INDIRECTON: bool
        SHADOWSON: bool
        ...
    class LightingAnalysisOverlay(RenderEffect):
        ...
    class LightingAnalysisOverlayFactory(Interface):
        ...
    class LightingMap(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        DIRECTON: bool
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        INDIRECTON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        SHADOWSON: bool
        TARGETMAPSLOTNAME: str
        ...
    class LightingRenderElement(RenderElement):
        BITMAP: None
        DIRECTON: bool
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        INDIRECTON: bool
        SHADOWSON: bool
        ...
    class LightingUnits(Interface):
        ...
    class Lighting_Analysis_Data(RenderElement):
        ...
    class Lighting_Analysis_Overlay(RenderEffect):
        ...
    class LightscapeExposureControl(ToneOperator):
        ACTIVE: bool
        BRIGHTNESS: float
        CHROMATICADAPTATION: bool
        COLORDIFFERENTIATION: bool
        CONTRAST: float
        DAYLIGHT: bool
        EXTERIOR: bool
        EXTERIORDAYLIGHT: bool
        INDIRECTONLY: bool
        MIDTONES: float
        PHYSICALSCALE: float
        PROCESSBG: bool
        USELEGACYALGORITHM: bool
        WHITECOLOR: MXSWrapperBase
        ...
    class LimbData2(ReferenceTarget):
        ...
    class LinearShape(Shape):
        ...
    class Linear_Exposure_Control(ToneOperator):
        ACTIVE: bool
        BRIGHTESS: float
        CHROMATICADAPTATION: bool
        COLORDIFFERENTIATION: bool
        CONTRAST: float
        EXPOSUREVALUE: float
        PHYSICALSCALE: float
        PROCESSBG: bool
        WHITECOLOR: MXSWrapperBase
        ...
    class Lines(Shape):
        ...
    class Link(Matrix3Controller):
        KEY_HIERARCHY_MODE: int
        KEY_MODE: int
        KEY_NODES_MODE: int
        ...
    class LinkBlockInstance(GeometryClass):
        ...
    class LinkBlockInstanceshape(Shape):
        ...
    class LinkComposite(GeometryClass):
        ...
    class LinkCompositeshape(Shape):
        ...
    class LinkControl(RolloutControl):
        ...
    class LinkLeaf(GeometryClass):
        ...
    class LinkLeafshape(Shape):
        ...
    class LinkOriginPtHelper(Helper):
        ...
    class LinkTimeControl(FloatController):
        ...
    class Link_Constraint(Matrix3Controller):
        KEY_HIERARCHY_MODE: int
        KEY_MODE: int
        KEY_NODES_MODE: int
        ...
    class Link_Inheritance__Selected(UtilityPlugin):
        ...
    class Link_Transform(Matrix3Controller):
        ...
    class LinkedXForm(Modifier):
        BACKTRANSFORM: bool
        ...
    class Linked_XForm(Modifier):
        BACKTRANSFORM: bool
        ...
    class ListBoxControl(RolloutControl):
        ...
    class LnDif(Generic):
        ...
    class LoadDefaultMatLib(Primitive):
        ...
    class LoadSaveAnimation(Interface):
        ...
    class Local_Euler_XYZ(RotationController):
        AXISORDER: int
        ...
    class LockAxisTripods(Primitive):
        ...
    class Lock_Bond(Helper):
        ANIMATED_SURFACE: bool
        BREAK_IF_OUTWARDS_ONLY: bool
        BREAK_OFF_ACCELERATION: float
        BREAK_OFF_SPEED: float
        BREAK_OFF_TYPE: int
        BREAK_OFF_VARIATION: float
        DAMPENING_FRICTION: float
        DAMPENING_RESISTANCE: float
        INDUCED_BY_SPEED_CHANGE: bool
        INERTIAL_SIZE: float
        LOCK_ON_OBJECTS: MXSWrapperBase
        LOCK_TYPE: int
        POSITION_DAMPENING_TYPE: int
        POSITION_FORCE: float
        POSITION_OFFSET_LIMIT: float
        RANDOM_SEED: int
        RESTRICT_POSITION_TO_SURFACE: bool
        ROTATION_DAMPENING: float
        ROTATION_FORCE: float
        ROTATION_OFFSET_LIMIT: float
        SNAP_TO_SURFACE: bool
        SPEED_LIMIT: float
        SPEED_UNIT: float
        SPIN_LIMIT: float
        SYNC_TYPE: int
        USE_BREAK_OFF_TEST: bool
        USE_NO_ACCELERATION_ZONE: bool
        USE_NO_DAMPENING_ZONE: bool
        USE_POSITION_OFFSET_LIMIT: bool
        USE_ROTATION_OFFSET_LIMIT: bool
        USE_SPEED_LIMIT: bool
        USE_SPIN_LIMIT: bool
        ZONE_RADIUS: float
        ...
    class LockedComponentsMan(Interface):
        ...
    class LockedMapWrapper(TextureMap):
        ...
    class LockedMaterialWrapper(Material):
        ...
    class LockedModifierWrapper(Modifier):
        ...
    class LockedObjectWrapper(Helper):
        ...
    class LockedObjectWrapper_Obsolete(System):
        ...
    class LockedTracksMan(Interface):
        ...
    class Loft(GeometryClass):
        ...
    class LoftObject(GeometryClass):
        ...
    class LogN(Generic):
        ...
    class Logarithmic_Exposure_Control(ToneOperator):
        ACTIVE: bool
        BRIGHTNESS: float
        CHROMATICADAPTATION: bool
        COLORDIFFERENTIATION: bool
        CONTRAST: float
        DAYLIGHT: bool
        EXTERIOR: bool
        EXTERIORDAYLIGHT: bool
        INDIRECTONLY: bool
        MIDTONES: float
        PHYSICALSCALE: float
        PROCESSBG: bool
        USELEGACYALGORITHM: bool
        WHITECOLOR: MXSWrapperBase
        ...
    class LookAt_Constraint(RotationController):
        LOOKAT_VECTOR_LENGTH: float
        PICKUPNODE: None
        RELATIVE: bool
        SET_ORIENTATION: bool
        STOUP_AXIS: int
        STOUP_AXISFLIP: bool
        TARGET_AXIS: int
        TARGET_AXISFLIP: bool
        UPNODE_AXIS: int
        UPNODE_CTRL: int
        UPNODE_WORLD: bool
        VIEWLINE_LENGTH_ABS: bool
        WEIGHT: MXSWrapperBase
        ...
    class Luminaire(Helper):
        DIMMER: float
        FILTERCOLOR: MXSWrapperBase
        ...
    class LuminaireHelper(Helper):
        DIMMER: float
        FILTERCOLOR: MXSWrapperBase
        ...
    class LuminanceRenderElement(RenderElement):
        ATMOSPHEREON: bool
        BITMAP: None
        ELEMENTNAME: str
        ENABLEDON: bool
        FILTERON: bool
        SCALEFACTOR: float
        SHADOWON: bool
        ...
    class Luminance_HDR_Data(RenderElement):
        ATMOSPHEREON: bool
        BITMAP: None
        ELEMENTNAME: str
        ENABLEDON: bool
        FILTERON: bool
        SCALEFACTOR: float
        SHADOWON: bool
        ...
    class Luminance_Render_Element(RenderElement):
        ...
    class Lumination_Render_Element(RenderElement):
        ...
    class LuminosityUtil(Interface):
        ...
    class MACUtilities(UtilityPlugin):
        ...
    class MAXAKey(Value):
        ...
    class MAXBezierShapeClass(Value):
        ...
    class MAXClass(Value):
        ...
    class MAXCurveCtl(RolloutControl):
        ...
    class MAXCustAttrib(Value):
        ...
    class MAXCustAttribArray(Value):
        ...
    class MAXFilterClass(Value):
        ...
    class MAXKey(Value):
        ...
    class MAXKeyArray(Value):
        ...
    class MAXMeshClass(Value):
        ...
    class MAXModifierArray(Value):
        ...
    class MAXNoteKey(Value):
        ...
    class MAXNoteKeyArray(Value):
        ...
    class MAXObject(Value):
        ...
    class MAXRefTarg(Value):
        ...
    class MAXRootNode(Value):
        ...
    class MAXRootScene(Value):
        ...
    class MAXScript(UtilityPlugin):
        ...
    class MAXScriptFunction(Value):
        ...
    class MAXSuperClass(Value):
        ...
    class MAXTVNode(Value):
        ...
    class MAXTVUtility(Value):
        ...
    class MAXWrapper(Value):
        ...
    class MAXWrapperNonRefTarg(Value):
        ...
    class MAX_File_Finder(UtilityPlugin):
        ...
    class MAXtoA(RendererClass):
        AA_SAMPLES: int
        AA_SAMPLES_MAX: int
        AA_SAMPLE_CLAMP: float
        AA_SAMPLE_CLAMP_AFFECTS_AOVS: bool
        AA_SAMPLE_CLAMP_ENABLED: bool
        ABORT_ON_ERROR: bool
        ABORT_ON_ERROR_ACTIVESHADE: bool
        ABORT_ON_LICENSE_FAIL: bool
        ADAPTIVE_THRESHOLD: float
        AOV_MANAGER: None
        AOV_SHADERS_MAP_0: None
        AOV_SHADERS_MAP_1: None
        AOV_SHADERS_MAP_2: None
        AOV_SHADERS_MAT_0: None
        AOV_SHADERS_MAT_1: None
        AOV_SHADERS_MAT_2: None
        ASS_FILE_PATH: None
        ATMOSPHERE: None
        AUTODETECT_THREADS: bool
        AUTO_SHUTTER: bool
        AUTO_TRANSPARENCY_DEPTH: int
        BUCKET_SCANNING: int
        BUCKET_SIZE: int
        CURVES_DEFAULT_BASIS: int
        CURVES_DEFAULT_MIN_PIXEL_WIDTH: float
        CURVES_DEFAULT_MODE: int
        DEFAULT_GPU_MIN_MEMORY_MB: int
        DEFAULT_GPU_NAMES: str
        DEFORM_KEYS: int
        DIELECTRIC_PRIORITIES: bool
        DISPLACEMENT_DEFAULT_SUBDIV_ADAPTIVE_ERROR: float
        DISPLACEMENT_DEFAULT_SUBDIV_ITERATIONS: int
        DISPLACEMENT_DEFAULT_SUBDIV_TYPE: int
        DRIVER_TYPE: None
        ENABLE_ADAPTIVE_SAMPLING: bool
        ENABLE_DEFORM_KEYS: bool
        ENABLE_TRANSFORM_KEYS: bool
        ENABLE_USER_OPTIONS: bool
        ENV_ADV_BGND_CUSTOM_COLOR: MXSWrapperBase
        ENV_ADV_BGND_CUSTOM_MAP: None
        ENV_ADV_BGND_CUSTOM_SHADER: None
        ENV_ADV_BGND_MODE: int
        ENV_ADV_BGND_VISIBLE_TO_CAMERA: bool
        ENV_ADV_BGND_VISIBLE_TO_DIFFUSE_REFLECTIONS: bool
        ENV_ADV_BGND_VISIBLE_TO_DIFFUSE_TRANSMISSION: bool
        ENV_ADV_BGND_VISIBLE_TO_SPECULAR_REFLECTIONS: bool
        ENV_ADV_BGND_VISIBLE_TO_SPECULAR_TRANSMISSION: bool
        ENV_ADV_BGND_VISIBLE_TO_VOLUME_SCATTERING: bool
        ENV_ADV_IBL_AFFECT_INDIRECT: bool
        ENV_ADV_IBL_AFFECT_SSS: bool
        ENV_ADV_IBL_AFFECT_VOLUME: bool
        ENV_ADV_IBL_CAMERA_MULT: float
        ENV_ADV_IBL_CAST_SHADOWS: bool
        ENV_ADV_IBL_DIFFUSE_MULT: float
        ENV_ADV_IBL_EMIT_CAMERA: bool
        ENV_ADV_IBL_EMIT_DIFFUSE: bool
        ENV_ADV_IBL_EMIT_SPECULAR: bool
        ENV_ADV_IBL_EMIT_TRANSMISSION: bool
        ENV_ADV_IBL_INDIRECT_MULT: float
        ENV_ADV_IBL_MAX_BOUNCES: int
        ENV_ADV_IBL_MULTIPLIER: float
        ENV_ADV_IBL_PORTAL_MODE: int
        ENV_ADV_IBL_RESOLUTION: int
        ENV_ADV_IBL_RESOLUTION_ENABLE: bool
        ENV_ADV_IBL_SHADOW_COLOR: MXSWrapperBase
        ENV_ADV_IBL_SHADOW_DENSITY: float
        ENV_ADV_IBL_SPECULAR_MULT: float
        ENV_ADV_IBL_SSS_MULT: float
        ENV_ADV_IBL_TRANSMISSION_MULT: float
        ENV_ADV_IBL_VOLUME_MULT: float
        ENV_ADV_IBL_VOLUME_SAMPLES: int
        ENV_IBL_ENABLE: bool
        ENV_IBL_SAMPLES: int
        ENV_MODE: int
        ENV_PHYS_BGND_COLOR: MXSWrapperBase
        ENV_PHYS_BGND_MAP: None
        ENV_PHYS_BGND_MODE: int
        ERROR_COLOR_BAD_PIXEL: MXSWrapperBase
        ERROR_COLOR_BAD_SHADER: MXSWrapperBase
        ERROR_COLOR_BAD_TEXTURE: MXSWrapperBase
        EXPAND_PROCEDURALS: bool
        EXPORT_BINARY: bool
        EXPORT_CAMERAS: bool
        EXPORT_DRIVERSFILTERS: bool
        EXPORT_GEOMETRY: bool
        EXPORT_LIGHTS: bool
        EXPORT_OPERATORS: bool
        EXPORT_OPTION: bool
        EXPORT_SHADERS: bool
        EXPORT_TO_ASS: bool
        EXPORT_TO_ASS_ORIGIN: int
        EXPORT_TO_MTLX: bool
        FILTER: int
        FILTER_WIDTH: float
        GEOMETRY_DICING_CAMERA: None
        GI_DIFFUSE_DEPTH: int
        GI_DIFFUSE_SAMPLES: int
        GI_SPECULAR_DEPTH: int
        GI_SPECULAR_SAMPLES: int
        GI_SSS_SAMPLES: int
        GI_TOTAL_DEPTH: int
        GI_TRANSMISSION_DEPTH: int
        GI_TRANSMISSION_SAMPLES: int
        GI_VOLUME_DEPTH: int
        GI_VOLUME_SAMPLES: int
        GPU_AUTO_SELECTION: bool
        GPU_MAX_TEXTURE_RESOLUTION: int
        GPU_RENDERING: bool
        GPU_SELECTION: MXSWrapperBase
        IGNORE_ATMOSPHERE: bool
        IGNORE_BUMP: bool
        IGNORE_DISPLACEMENT: bool
        IGNORE_DOF: bool
        IGNORE_LIGHTS: bool
        IGNORE_MOTION: bool
        IGNORE_MOTION_BLUR: bool
        IGNORE_OPERATORS: bool
        IGNORE_SHADERS: bool
        IGNORE_SHADOWS: bool
        IGNORE_SMOOTHING: bool
        IGNORE_SSS: bool
        IGNORE_SUBDIVISION: bool
        IGNORE_TEXTURES: bool
        IMAGER_0: None
        INDIRECT_SAMPLE_CLAMP: float
        INDIRECT_SPECULAR_BLUR: float
        LEGACY_3DS_MAX_MAP_SUPPORT: bool
        LOCK_SAMPLING_PATTERN: bool
        LOG_FILE: None
        LOG_RENDER_PROFILE: bool
        LOG_RENDER_STATS: bool
        LOG_TO_CONSOLE: bool
        LOG_TO_FILE: bool
        LOW_LIGHT_THRESHOLD: float
        MATERIAL_EXPORT_LIST: MXSWrapperBase
        MAX_SUBDIVISIONS: int
        MAX_WARNINGS: int
        MTLX_FILE_PATH: None
        MTLX_LOOK: str
        MTLX_PROPERTIES: None
        MTLX_RELATIVE: bool
        MTLX_USE_CURRENT_SELECTION: bool
        NOICE_ADDITIONAL_FRAMES: int
        NOICE_ANIM_RANGE: int
        NOICE_END_FRAME: int
        NOICE_INPUT: str
        NOICE_LIGHT_AOV_NAMES: str
        NOICE_OUTPUT: str
        NOICE_PATCH_RADIUS: int
        NOICE_SEARCH_RADIUS: int
        NOICE_START_FRAME: int
        NOICE_VARIANCE: float
        OPERATOR_EXPORT_LIST: MXSWrapperBase
        OPERATOR_EXPORT_TREE: bool
        OPERATOR_ROOT: None
        OUTPUT_DENOISING_AOVS: bool
        PHYSICAL_MATERIAL_SSS_TYPE: int
        PLUGIN_SEARCHPATH: None
        PREPASS_ENABLED: bool
        PREPASS_SAMPLES: int
        PROCEDURAL_SEARCHPATH: None
        PROGRESSIVE_RENDER: bool
        RENDER_DEVICE: int
        RENDER_DEVICE_FALLBACK: int
        RENDER_PROFILE_FILE: None
        RENDER_STATS_FILE: None
        RENDER_STATS_MODE: int
        RENDER_VIEW_SETTINGS: str
        RESPECT_PHYSICAL_CAMERA_MOTION_BLUR: bool
        RETRANSLATE_ALL_FRAMES: bool
        SHADER_OVERRIDE: None
        SHADER_OVERRIDE_ENABLED: bool
        SHOW_BUCKET_CORNERS_AS: bool
        SHOW_BUCKET_CORNERS_PROD: bool
        SHUTTER_CLOSE: float
        SHUTTER_LENGTH: float
        SHUTTER_OPEN: float
        SHUTTER_POSITION: int
        SHUTTER_TYPE: int
        SKIP_LICENSE_CHECK: bool
        SSS_USE_AUTOBUMP: bool
        SUBDIV_FRUSTUM_CULLING: bool
        SUBDIV_FRUSTUM_PADDING: float
        TEXTURE_ACCEPT_UNMIPPED: bool
        TEXTURE_ACCEPT_UNTILED: bool
        TEXTURE_AUTOMIP: bool
        TEXTURE_AUTOTILE: int
        TEXTURE_ENABLE_AUTOTILE: bool
        TEXTURE_MAX_MEMORY_MB: int
        TEXTURE_MAX_OPEN_FILES: int
        TEXTURE_PER_FILE_STATS: bool
        TEXTURE_SEARCHPATH: None
        THREADS: int
        TRANSFORM_KEYS: int
        USER_OPTIONS: None
        USE_EXISTING_TX: bool
        USE_OPTIX_ON_BEAUTY: bool
        USE_QUADS: int
        USE_RENDER_VIEW: bool
        VERBOSITY_LEVEL: int
        ...
    class MAXtoA_Menu(GlobalUtilityPlugin):
        ...
    class MAXtoA_OperatorCustomAttribute(CustAttrib):
        ...
    class MCG_Donut(Shape):
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        RADIUS1: float
        RADIUS2: float
        _DUMMY: bool
        ...
    class MCG_MeshEdgesToSpline(Shape):
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        _DUMMY: bool
        ...
    class MCG_SinWave(Shape):
        AMPLITUDE: float
        CLOSED: bool
        DOMAIN: float
        OFFSET: float
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        RANGE: float
        SEGMENTS: int
        SMOOTHING_FACTOR: float
        _DUMMY: bool
        ...
    class MCG_LookAt(RotationController):
        BILLBOARD: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ROTXOFFSET: float
        ROTYOFFSET: float
        ROTZOFFSET: float
        SRCUPNODEAXISFLIP: bool
        TARGETAXIS: int
        TARGETAXISFLIP: bool
        TARGETS_TAB: MXSWrapperBase
        UPNODE: None
        UPNODEALIGNAXIS: int
        UPNODEAXIS: int
        UPNODECONTROL: int
        UPNODEWORLD: bool
        WEIGHTS_TAB: MXSWrapperBase
        _DUMMY: bool
        ...
    class MCG_RayToSurfaceOrientation(RotationController):
        FLIP: bool
        FORWARD_OBJECT: None
        LCLFWDAXIS: int
        LCLUPAXIS: int
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        RAY_AXIS: int
        RAY_ORIGIN: None
        RAY_TO_SURFACE_PIVOT: bool
        SURFACES_TAB: MXSWrapperBase
        USE_FORWARD_OBJECT: bool
        USE_SURFACE_NORMAL: bool
        WORLD_AXIS: int
        _DUMMY: bool
        ...
    class MCG_RayToSurfacePosition(PositionController):
        FLIP: bool
        OFFSET: float
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        RAY_AXIS: int
        RAY_ORIGIN: None
        RAY_TO_SURFACE_PIVOT: bool
        SURFACES_TAB: MXSWrapperBase
        USE_SURFACE_NORMAL: bool
        _DUMMY: bool
        ...
    class MCG_RayToSurfaceTransform(Matrix3Controller):
        FLIP: bool
        FORWARD_OBJECT: None
        LCLFWDAXIS: int
        LCLUPAXIS: int
        OFFSET: float
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        RAY_AXIS: int
        RAY_ORIGIN: None
        RAY_TO_SURFACE_PIVOT: bool
        SURFACES_TAB: MXSWrapperBase
        USE_FORWARD_OBJECT: bool
        USE_SURFACE_NORMAL: bool
        WORLD_AXIS: int
        _DUMMY: bool
        ...
    class MCG_RotationalSpring1DOFTransform(Matrix3Controller):
        AXIS_XYZ: int
        BOUNCE: float
        DAMPING: float
        DEACTIVATE_SPRING: bool
        GEOMETRY_HULL: None
        GRAVITY: float
        LIMITISREVERSED: bool
        LOWERLIMIT: float
        MASS: float
        PARENT_OBJECT: None
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        STEPSPERFRAME: float
        STIFFNESS: float
        UPPERLIMIT: float
        _DUMMY: bool
        ...
    class MCG_RotationalSpring3DOFTransform(Matrix3Controller):
        BOUNCE: float
        DAMPING: float
        DEACTIVATE_SPRING: bool
        GEOMETRY_HULL: None
        GRAVITY: float
        LOWERLIMITX: float
        LOWERLIMITY: float
        LOWERLIMITZ: float
        MASS: float
        PARENT_OBJECT: None
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        STEPSPERFRAME: float
        STIFFNESS: float
        UPPERLIMITX: float
        UPPERLIMITY: float
        UPPERLIMITZ: float
        USEAXISLIMITS: bool
        _DUMMY: bool
        ...
    class MEditBkgnd(TextureMap):
        ...
    class MIDI_Device(ReferenceTarget):
        ...
    class MIDI_DeviceMotionCaptureDeviceBindingClass(MotionCaptureDeviceBindingClass):
        ...
    class MIDI_DeviceMotionCaptureDeviceClass(MotionCaptureDeviceClass):
        ...
    class MMClean(UtilityPlugin):
        ...
    class MPG(BitmapIO):
        ...
    class MPassCamEffect(MAXWrapper):
        ...
    class MPassCamEffectClass(Value):
        ...
    class MSBipedRootClass(Value):
        ...
    class MSComMethod(Value):
        ...
    class MSCustAttribDef(Value):
        ...
    class MSDispatch(Value):
        ...
    class MSEmulator(TextureMap):
        ...
    class MSPluginClass(Value):
        ...
    class MSec_Element(ReferenceTarget):
        ALPHA: int
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        APPLYLIGHTS: bool
        APPLYNOISE: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        CIRCULARCOLORMIX: float
        CIRCULARMAP: None
        CIRCULARMTL: None
        COLORRADIUS1: float
        COLORRADIUS2: float
        COLORRADIUS3: float
        COLORRADIUS4: float
        COLORSOURCE: float
        EFFECTSID: int
        ELEMENTNAME: str
        FILTERALL: bool
        FILTERBRIGHTNESS: bool
        FILTEREDGE: bool
        FILTERHUE: bool
        FILTERPERIMETER: bool
        FILTERPERIMETERALPHA: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        INTENSITY: float
        NOISEMAP: None
        OBJECTID: int
        OCCLUSION: float
        ON: bool
        PLANE: float
        PRESETS: int
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        QUADRANT4COLOR: MXSWrapperBase
        RADIALCOLOR1: MXSWrapperBase
        RADIALCOLOR2: MXSWrapperBase
        RADIALCOLOR3: MXSWrapperBase
        RADIALCOLOR4: MXSWrapperBase
        RADIALDENSITY: None
        RADIALMAP: None
        RADIALMTL: None
        RADIALSIZEMAP: None
        SIDES: int
        SIZE: float
        SOURCEALPHA: bool
        SOURCEEFFECTSID: bool
        SOURCEOBJECTID: bool
        SOURCESURFACENORMAL: bool
        SOURCEUNCLAMPEDCOLOR: bool
        SOURCEWHOLE: bool
        SOURCEZBUFFER: bool
        SQUEEZE: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        USECIRCULARMAP: bool
        USECIRCULARMTL: bool
        USERADIALDENSITY: bool
        USERADIALMAP: bool
        USERADIALMTL: bool
        USERADIALSIZEMAP: bool
        ZHI: float
        ZLO: float
        ...
    class MXClip(Value):
        ...
    class MXSDebugger(Interface):
        ...
    class MXSParticleContainer(ReferenceTarget):
        ...
    class MXSProtector(Value):
        ...
    class MXS_IsSceneEmptyForNodePick(Primitive):
        ...
    class MXTrack(Value):
        ...
    class MXTrackgroup(Value):
        ...
    class MainThreadTaskManager(Interface):
        ...
    class MakeNURBSConeSurface(Primitive):
        ...
    class MakeNURBSCylinderSurface(Primitive):
        ...
    class MakeNURBSLatheSurface(Primitive):
        ...
    class MakeNURBSSphereSurface(Primitive):
        ...
    class MakeNURBSTorusSurface(Primitive):
        ...
    class Manual_Secondary_Element(ReferenceTarget):
        ALPHA: int
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        APPLYLIGHTS: bool
        APPLYNOISE: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        CIRCULARCOLORMIX: float
        CIRCULARMAP: None
        CIRCULARMTL: None
        COLORRADIUS1: float
        COLORRADIUS2: float
        COLORRADIUS3: float
        COLORRADIUS4: float
        COLORSOURCE: float
        EFFECTSID: int
        ELEMENTNAME: str
        FILTERALL: bool
        FILTERBRIGHTNESS: bool
        FILTEREDGE: bool
        FILTERHUE: bool
        FILTERPERIMETER: bool
        FILTERPERIMETERALPHA: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        INTENSITY: float
        NOISEMAP: None
        OBJECTID: int
        OCCLUSION: float
        ON: bool
        PLANE: float
        PRESETS: int
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        QUADRANT4COLOR: MXSWrapperBase
        RADIALCOLOR1: MXSWrapperBase
        RADIALCOLOR2: MXSWrapperBase
        RADIALCOLOR3: MXSWrapperBase
        RADIALCOLOR4: MXSWrapperBase
        RADIALDENSITY: None
        RADIALMAP: None
        RADIALMTL: None
        RADIALSIZEMAP: None
        SIDES: int
        SIZE: float
        SOURCEALPHA: bool
        SOURCEEFFECTSID: bool
        SOURCEOBJECTID: bool
        SOURCESURFACENORMAL: bool
        SOURCEUNCLAMPEDCOLOR: bool
        SOURCEWHOLE: bool
        SOURCEZBUFFER: bool
        SQUEEZE: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        USECIRCULARMAP: bool
        USECIRCULARMTL: bool
        USERADIALDENSITY: bool
        USERADIALMAP: bool
        USERADIALMTL: bool
        USERADIALSIZEMAP: bool
        ZHI: float
        ZLO: float
        ...
    class MapButtonControl(Value):
        ...
    class MapChannelAdd(Modifier):
        ...
    class MapChannelDelete(Modifier):
        MAPID: int
        ...
    class MapChannelPaste(Modifier):
        ...
    class MapMtlClipboard(GlobalUtilityPlugin):
        ...
    class MapOverride_BTT_Only(BakeElement):
        ...
    class MapScaler(SpacewarpModifier):
        CHANNEL: int
        SCALE: float
        UOFFSET: float
        UPDIRECTION: int
        VOFFSET: float
        WRAP: bool
        WRAPUSINGSMOOTHINGGROUPS: bool
        ...
    class MapScalerModifier(Modifier):
        CHANNEL: int
        SCALE: float
        UOFFSET: float
        VOFFSET: float
        WRAP: bool
        WRAPUSINGSMOOTHINGGROUPS: bool
        ...
    class MapScalerOSM(Modifier):
        CHANNEL: int
        SCALE: float
        UOFFSET: float
        VOFFSET: float
        WRAP: bool
        WRAPUSINGSMOOTHINGGROUPS: bool
        ...
    class MapScalerSpaceWarp(SpacewarpObject):
        ...
    class MapScalerSpacewarpModifier(SpacewarpModifier):
        CHANNEL: int
        SCALE: float
        UOFFSET: float
        UPDIRECTION: int
        VOFFSET: float
        WRAP: bool
        WRAPUSINGSMOOTHINGGROUPS: bool
        ...
    class MapSupportClass(Value):
        ...
    class Map_To_Material_Conversion(Material):
        SHADER: None
        SHADER_ON: bool
        ...
    class MappedGeneric(Value):
        ...
    class MappedPrimitive(Value):
        ...
    class MappingObject(Helper):
        ACQUIRE_FROM_MAPPING_CHANNELS: MXSWrapperBase
        ACQUIRE_SUBMATERIAL_INDEX: bool
        ANIMATED_SURFACE: bool
        BLEND_MAPPING_BY_DISTANCE: bool
        BLEND_MAPPING_BY_TIME: bool
        BLEND_TIME: int
        BLEND_TYPE: int
        EXCLUDE_TILING: bool
        FINISH_DISTANCE: float
        MAPPING_FROM_OBJECTS: MXSWrapperBase
        MAPPING_TYPE: int
        RANDOM_SEED: int
        SHOW_MAP_IN_VIEWPORT: bool
        STATIC_OBJECTS: bool
        UNIFORM_COLOR_PER_PARTICLE: bool
        USE_VERTEX_COLOR: bool
        U_VARIATION: float
        V_VARIATION: float
        W_VARIATION: float
        ...
    class Mapping_Object(Helper):
        ACQUIRE_FROM_MAPPING_CHANNELS: MXSWrapperBase
        ACQUIRE_SUBMATERIAL_INDEX: bool
        ANIMATED_SURFACE: bool
        BLEND_MAPPING_BY_DISTANCE: bool
        BLEND_MAPPING_BY_TIME: bool
        BLEND_TIME: int
        BLEND_TYPE: int
        EXCLUDE_TILING: bool
        FINISH_DISTANCE: float
        MAPPING_FROM_OBJECTS: MXSWrapperBase
        MAPPING_TYPE: int
        RANDOM_SEED: int
        SHOW_MAP_IN_VIEWPORT: bool
        STATIC_OBJECTS: bool
        UNIFORM_COLOR_PER_PARTICLE: bool
        USE_VERTEX_COLOR: bool
        U_VARIATION: float
        V_VARIATION: float
        W_VARIATION: float
        ...
    class Marble(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COORDS: MXSWrapperBase
        MAP1: None
        MAP1ENABLED: bool
        MAP2: None
        MAP2ENABLED: bool
        SIZE: float
        WIDTH: float
        ...
    class Mask(TextureMap):
        MAP: None
        MAPENABLED: bool
        MASK: None
        MASKENABLED: bool
        MASKINVERTED: bool
        ...
    class MassFX_Loader_Linkage(GlobalUtilityPlugin):
        ...
    class MassFX_RBody(Modifier):
        ANGULARDAMPING: float
        BAKED: int
        BOUNCINESS: float
        COLLIDEWITHRIGIDBODIES: bool
        COMPOSITEHIGHQUALITY: bool
        COMPOSITEMAXCONCAVITY: float
        COMPOSITEMAXVERTICES: int
        CONTACTSHELLCONTACTDISTANCE: float
        CONTACTSHELLOVERRIDEGLOBALS: bool
        CONTACTSHELLRESTDEPTH: float
        CONTINUOUSCOLLISIONDETECTION: bool
        DENSITY: float
        DYNAMICFRICTION: float
        ENABLEADVANCEDSETTINGS: int
        ENABLEBACKFACECOLLISION: bool
        ENABLEGRAVITY: bool
        ENABLESOLIDMESHES: bool
        EXTRASHAPES: None
        FORCESLIST: MXSWrapperBase
        INITIALMOTIONSTYLE: int
        INITIALSPINX: float
        INITIALSPINY: float
        INITIALSPINZ: float
        INITIALVELOCITYX: float
        INITIALVELOCITYY: float
        INITIALVELOCITYZ: float
        LINEARDAMPING: float
        MANUALSETUP: bool
        MASS: float
        MASSCENTERMODE: int
        MASSCENTERX: float
        MASSCENTERY: float
        MASSCENTERZ: float
        MATERIALID: int
        MESHCONVEXSTYLE: int
        MESHCUSTOMMESH: None
        MESHHEIGHT: float
        MESHINFLATION: float
        MESHLENGTH: float
        MESHOVERRIDEMATERIAL: bool
        MESHRADIUS: float
        MESHTYPE: int
        MESHVERTICESLIMIT: int
        MESHWIDTH: float
        SHOWPHYSICALMESH: bool
        SLEEPATSTART: bool
        SMALLCLUSTERTHRESHOLD: float
        SOLVERITER: bool
        SOLVERITERVALUE: int
        SPINSPEED: float
        STATICFRICTION: float
        SWITCHTYPE: bool
        SWITCHTYPEATFRAME: int
        TYPE: int
        VELOCITYSPEED: float
        VOLUME: float
        ...
    class MasterBlock(MasterBlockController):
        ...
    class MasterBlockController(MAXWrapper):
        ...
    class MasterClip(MasterBlockController):
        ...
    class MasterLayer(CtrlUserDataTypeClass):
        ...
    class MasterLayerControlManager(CtrlUserDataTypeClass):
        ...
    class MasterList(MasterBlockController):
        ...
    class MasterPointController(MAXWrapper):
        ...
    class Master_Controller_Plugin_Not_Found(MasterBlockController):
        ...
    class Master_Layer(CtrlUserDataTypeClass):
        ...
    class Master_Motion_Clip(MasterBlockController):
        ...
    class Master_Point_Controller(MasterPointController):
        ...
    class MatchPattern(Primitive):
        ...
    class MaterialBrowseDlg(Primitive):
        ...
    class MaterialByElement(Modifier):
        MATERIAL_ID_COUNT: int
        MATERIAL_ID__1: float
        MATERIAL_ID__2: float
        MATERIAL_ID__3: float
        MATERIAL_ID__4: float
        MATERIAL_ID__5: float
        MATERIAL_ID__6: float
        MATERIAL_ID__7: float
        MATERIAL_ID__8: float
        METHOD: int
        RANDOM_SEED: int
        ...
    class MaterialCategory(ReferenceMaker):
        ...
    class MaterialExplorerManager(Interface):
        ...
    class MaterialLibrary(Value):
        ...
    class MaterialPreviewSystem(Interface):
        ...
    class MaterialPreviewer(GlobalUtilityPlugin):
        ...
    class MaterialPreviewerGUP(GlobalUtilityPlugin):
        ...
    class Material_Dynamic(Helper):
        ADD_RANDOM_OFFSET: bool
        ASSIGNED_MATERIAL: None
        ASSIGN_MATERIAL: bool
        ASSIGN_MATERIAL_ID: bool
        LOOP: bool
        MATERIAL_ID: int
        MAX_AGE_OFFSET: MXSWrapperBase
        NUMBER_OF_SUB_MATERIALS: int
        RANDOMIZE_AGE: bool
        RANDOM_OFFSET: int
        RANDOM_SEED: int
        RESET_PARTICLE_AGE: bool
        SHOW_IN_VIEWPORT: bool
        SUBMTL_ID_OFFSET: int
        SUB_MATERIALS_RATE: float
        SYNC_TYPE: int
        TYPE: int
        ...
    class Material_Editor(Value):
        ...
    class Material_EditorReferenceMaker(ReferenceMaker):
        ...
    class Material_Frequency(Helper):
        ASSIGNED_MATERIAL: None
        ASSIGN_MATERIAL: bool
        ASSIGN_MATERIAL_ID: bool
        MTL_ID_10: float
        MTL_ID_1: float
        MTL_ID_2: float
        MTL_ID_3: float
        MTL_ID_4: float
        MTL_ID_5: float
        MTL_ID_6: float
        MTL_ID_7: float
        MTL_ID_8: float
        MTL_ID_9: float
        RANDOM_SEED: int
        SHOW_IN_VIEWPORT: bool
        SUBMTL_ID_OFFSET: int
        ...
    class Material_ID(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class Material_Static(Helper):
        ASSIGNED_MATERIAL: None
        ASSIGN_MATERIAL: bool
        ASSIGN_MATERIAL_ID: bool
        LOOP: bool
        MATERIAL_ID: int
        NUMBER_OF_SUB_MATERIALS: int
        RANDOM_SEED: int
        RATE_PER_PARTICLE: float
        RATE_PER_SECOND: float
        RATE_TYPE: int
        SHOW_IN_VIEWPORT: bool
        SUBMTL_ID_OFFSET: int
        TYPE: int
        ...
    class Materialmodifier(Modifier):
        MATERIALID: int
        ...
    class Matrix3(Value):
        ...
    class Matrix3Controller(MAXWrapper):
        ...
    class Matrix3_Mixer_Controller(Matrix3Controller):
        ...
    class MatrixFromNormal(Primitive):
        ...
    class Matte(Material):
        ADDITIVEREFLECTION: int
        AFFECTALPHA: bool
        AMOUNT: float
        APPLYATMOSPHERE: bool
        ATMOSPHEREDEPTH: int
        COLOR: MXSWrapperBase
        MAP: None
        OPAQUEALPHA: bool
        RECEIVESHADOWS: bool
        SHADOWBRIGHTNESS: float
        USEREFLMAP: bool
        ...
    class MatteRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        GBUFID: int
        GBUFIDON: bool
        INCLUDEON: bool
        MTLID: int
        MTLIDON: bool
        ...
    class MatteShadow(Material):
        ADDITIVEREFLECTION: int
        AFFECTALPHA: bool
        AMOUNT: float
        APPLYATMOSPHERE: bool
        ATMOSPHEREDEPTH: int
        COLOR: MXSWrapperBase
        MAP: None
        OPAQUEALPHA: bool
        RECEIVESHADOWS: bool
        SHADOWBRIGHTNESS: float
        USEREFLMAP: bool
        ...
    class MaxFluidSolverClass(MAXWrapper):
        ...
    class MaxLiquid(GeometryClass):
        ACCELERATOR_MESHES: MXSWrapperBase
        CACHEOUTPUTFILEPATTERN: str
        CHANNELFIELD_MESHES: MXSWrapperBase
        COLLIDER_MESHES: MXSWrapperBase
        DISPLAYCACHELIMIT: float
        DISPLAYCACHELIMITENABLE: bool
        EMITTERHEIGHT: float
        EMITTERLENGTH: float
        EMITTERTYPE: int
        EMITTERWIDTH: float
        EMITTER_MESHES: MXSWrapperBase
        ENABLEGPUPOINTS: bool
        EXPORTPRTFILES: bool
        FIELD_MESHES: MXSWrapperBase
        FOAMMASK_MESHES: MXSWrapperBase
        GUIDEEMITTER_MESHES: MXSWrapperBase
        GUIDE_MESHES: MXSWrapperBase
        ICONSIZE: float
        KILLPLANES: MXSWrapperBase
        KILLVOLUMENODE: None
        LASTSELECTEDSOLVERINDEX: int
        MAXSCRATCHCACHERAM: float
        RENDERSOLVEINDEX: int
        RENDERSOLVELOCK: bool
        ROOTSIMDIRECTORY: str
        SCRATCHCACHE: str
        SHOWICON: bool
        SHOWVOXELGRID: bool
        SOLVERS: MXSWrapperBase
        USEPROJECTFOLDERS: bool
        ...
    class MaxLiquidSolver(MaxFluidSolverClass):
        ...
    class MaxMotionClipImp(MasterBlockController):
        CLIPASSOCIATIONS: MXSWrapperBase
        GLOBALCLIPASSOCIATIONS: MXSWrapperBase
        ...
    class MaxMotionClipMaster(CtrlUserDataTypeClass):
        ...
    class MaxMotionField(SpacewarpObject):
        ALONGAXISMAGNITUDE: float
        AROUNDAXISMAGNITUDE: float
        AWAYFROMAXISMAGNITUDE: float
        BOUNDARYFALLOFF: float
        BOUNDARYSHAPE: int
        CLAMPSPEED: bool
        COLOROPTIONS: int
        CONCENTRICMAGNITUDE: float
        DIRECTION: MXSWrapperBase
        DIRECTIONMAGNITUDE: float
        DIRECTIONX: float
        DIRECTIONY: float
        DIRECTIONZ: float
        DRAG: float
        DRAWADDITIVEVELOCITY: bool
        DRAWTIMESPAN: int
        DRAWVELOCITYARROWS: bool
        ENABLE: bool
        ENABLEALONGAXIS: bool
        ENABLEAROUNDAXIS: bool
        ENABLEAWAYFROMAXIS: bool
        ENABLEBOUNDARY: bool
        ENABLECONCENTRIC: bool
        ENABLEDIRECTION: bool
        ENABLEDIRECTIONROLLUP: bool
        ENABLEDISPLAY: bool
        ENABLEDRAG: bool
        ENABLEGEOMETRY: bool
        ENABLEGEOMETRYFALLOFF: bool
        ENABLEMAXDEPTH: bool
        ENABLENOISE: bool
        ENABLETURBULENCE: bool
        ENABLEVELOCITYROLLUP: bool
        ENABLEVELOCITYSCALE: bool
        ENABLEVELOCITYSPEED: bool
        ENDCOLOR: MXSWrapperBase
        EVALUATIONTYPE: int
        FIELDMAXDEPTH: float
        GEOMETRYALONGNORMAL: float
        GEOMETRYFRICTION: float
        GEOMETRYMAXDISTANCE: float
        GEOMETRYMINDISTANCE: float
        HEIGHT: float
        ICONSIZE: float
        INHERITVELOCITY: float
        INVERTFALLOFF: bool
        LENGTH: float
        MAGNITUDE: float
        MAGNITUDEUI: float
        MAXSPEED: float
        MINSPEED: float
        MOTIONFIELDS_BOUNDARYSHAPE: int
        MOTIONFIELDS_ENABLEBOUNDARY: bool
        MOTIONFIELDS_INVERT: bool
        MOTIONFIELDS_MESHES: None
        MOTIONFIELDS_PROXYOBJECTNAME: str
        MOTIONFIELDS_TRANSFORM: MXSWrapperBase
        MOTIONFIELDS_VOXELSCALE: float
        NOISEMAGNITUDE: float
        NORMALDRAG: float
        RADIUS: float
        SAMPLEOPTIONS: int
        SCALEAFFECTSSPEED: bool
        SECTIONRADIUS: float
        STARTCOLOR: MXSWrapperBase
        TEMPSPEEDFIX: int
        TRANSFORM: MXSWrapperBase
        TURBULENCEFREQUENCY: float
        TURBULENCEMAGNITUDE: float
        TURBULENCEOFFSET: MXSWrapperBase
        TURBULENCEOFFSETX: float
        TURBULENCEOFFSETY: float
        TURBULENCEOFFSETZ: float
        TURBULENCESCALE: MXSWrapperBase
        TURBULENCESCALEX: float
        TURBULENCESCALEY: float
        TURBULENCESCALEZ: float
        TURBULENCESPEED: float
        TURBULENCETIME: float
        TURBULENCETYPE: int
        VELOCITYDRAWSCALE: float
        VELOCITYGRID: bool
        VELOCITYGRIDRESOLUTION: int
        VELOCITYSCALE: MXSWrapperBase
        VELOCITYSCALEX: float
        VELOCITYSCALEY: float
        VELOCITYSCALEZ: float
        WIDTH: float
        WORLDSPACETURBULENCE: bool
        ...
    class MaxNetWorkerInterface(Interface):
        ...
    class MaxPlusINodeFromNode(MAXScriptFunction):
        ...
    class MaxRenderer_COM_Server(GlobalUtilityPlugin):
        ...
    class MaxRibbon(Interface):
        ...
    class MaxTabletManager(Interface):
        ...
    class MaxThumbnailMgr(Interface):
        ...
    class MaxToAOps(Interface):
        ...
    class MaxVectorFieldMod(SpacewarpModifier):
        ...
    class Max_2_5_Star(SamplerClass):
        ENABLE: bool
        QUALITY: float
        SUB_SAMPLE_TEXTURES: bool
        ...
    class Max_Master_Clip(ReferenceTarget):
        ...
    class Max_Mixer_Clip(CtrlUserDataTypeClass):
        ...
    class Max_MotionClip_Implementation(MasterBlockController):
        CLIPASSOCIATIONS: MXSWrapperBase
        GLOBALCLIPASSOCIATIONS: MXSWrapperBase
        ...
    class MaxscriptParticleContainer(ReferenceTarget):
        ...
    class Mb_Select(GlobalUtilityPlugin):
        ...
    class Measure(UtilityPlugin):
        ...
    class Melt(Modifier):
        AXIS: int
        CONFINE_TO_GIZMO: int
        CUT_OFF__OBSOLETE: float
        MELT_AMOUNT: float
        NEGATIVE_AXIS: int
        SOLIDITY_CUSTOM_VALUE: float
        SOLIDITY_PRESET: int
        SPREAD: float
        ...
    class MemoryTargetToOGSTargetFragment(GraphicsFragmentPlugin):
        ...
    class MeshCollision(ReferenceMaker):
        ...
    class MeshDeformPW(Modifier):
        BLEND: bool
        BLENDDISTANCE: float
        DISTANCE: float
        ENGINE: int
        FACELIMIT: int
        FALLOFF: float
        MESH: None
        MESHLIST: MXSWrapperBase
        MIRROROFFSET: float
        MIRRORPLANE: int
        MIRRORTHRESHOLD: float
        SHOWAXIS: bool
        SHOWFACELIMIT: bool
        SHOWLOOPS: bool
        SHOWMIRRORDATA: bool
        SHOWUNASSIGNEDVERTS: bool
        SHOWVERTS: bool
        THRESHOLD: float
        WEIGHTALLVERTS: bool
        ...
    class MeshINI(Interface):
        ...
    class MeshInspector(Interface):
        ...
    class MeshProjIntersect(ReferenceTarget):
        ...
    class MeshSelect(Modifier):
        BYVERTEX: bool
        IGNOREBACKFACING: bool
        IGNOREVISIBLEEDGES: bool
        MATERIALID: int
        PLANARTHRESHOLD: float
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELBUBBLE: float
        SOFTSELEDGEDIST: int
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELUSEEDGEDISTANCE: bool
        USESOFTSELECTION: bool
        ...
    class Mesh_Select(Modifier):
        BYVERTEX: bool
        IGNOREBACKFACING: bool
        IGNOREVISIBLEEDGES: bool
        MATERIALID: int
        PLANARTHRESHOLD: float
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELBUBBLE: float
        SOFTSELEDGEDIST: int
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELUSEEDGEDISTANCE: bool
        USESOFTSELECTION: bool
        ...
    class Mesher(GeometryClass):
        BOUNDSMAX: MXSWrapperBase
        BOUNDSMIN: MXSWrapperBase
        PFEVENTLIST: MXSWrapperBase
        PICK: None
        RADIUS: float
        RENDERTIMEONLY: bool
        TIME: float
        USEALLPFEVENTS: bool
        USECUSTOMBOUNDS: bool
        ...
    class MetaSLProxyMaterial(Material):
        SHADER: None
        SHADER_ON: bool
        ...
    class Metal2(Shader):
        ...
    class MetalShader(Shader):
        ...
    class Metal_Bump(ReferenceTarget):
        ALPHA_ON: bool
        BUMP: None
        BUMP_ON: bool
        COLOR_AMBIENT: MXSWrapperBase
        COLOR_DIFFUSE: MXSWrapperBase
        COLOR_SPECULAR: MXSWrapperBase
        DETAIL: None
        DETAIL_ON: bool
        DIFFUSE: None
        DIFFUSE_ON: bool
        MAP_BUMP: int
        MAP_DIFFUSE1: int
        MAP_DIFFUSE2: int
        MAP_SPECULAR: int
        MASK: None
        MASK_ON: bool
        NORMAL: None
        NORMAL_ON: bool
        REFLECTION: None
        REFLECTION_ON: bool
        SPECULAR_ON: bool
        SPIN_ALPHA: float
        SPIN_BUMPSCALE: int
        SPIN_REFLECTSCALE: int
        SPIN_TEXSCALE: int
        SYNC: bool
        ...
    class Metal_Bump9(ReferenceTarget):
        ALPHA_ON: bool
        BUMP: None
        BUMP_ON: bool
        COLOR_AMBIENT: MXSWrapperBase
        COLOR_DIFFUSE: MXSWrapperBase
        COLOR_SPECULAR: MXSWrapperBase
        DETAIL: None
        DETAIL_ON: bool
        DIFFUSE: None
        DIFFUSE_ON: bool
        MAP_BUMP: int
        MAP_DIFFUSE1: int
        MAP_DIFFUSE2: int
        MAP_SPECULAR: int
        MASK: None
        MASK_ON: bool
        NORMAL: None
        NORMAL_ON: bool
        REFLECTION: None
        REFLECTION_ON: bool
        SPECULAR_ON: bool
        SPIN_ALPHA: float
        SPIN_BUMPSCALE: int
        SPIN_REFLECTSCALE: int
        SPIN_TEXSCALE: int
        SYNC: bool
        ...
    class Metronome(SoundClass):
        ...
    class MinMaxAvg(ReferenceTarget):
        ...
    class MirrorIKConstraints(Primitive):
        ...
    class MissingUVCoordinates(Interface):
        ...
    class MissingUVCoordinatesClass(GlobalUtilityPlugin):
        ...
    class Missing_Atmospheric(Atmospheric):
        ...
    class Missing_Camera(Camera):
        ...
    class Missing_Custom_Attribute_Plugin(CustAttrib):
        ...
    class Missing_DataChannelEngine(IDataChannelEngineClass):
        ...
    class Missing_Exposure_Control(ToneOperator):
        ...
    class Missing_Float_Control(FloatController):
        ...
    class Missing_GeomObject(GeometryClass):
        ...
    class Missing_Helper(Helper):
        ...
    class Missing_Light(Light):
        ...
    class Missing_Matrix3_Control(Matrix3Controller):
        ...
    class Missing_MaxFluid_Solver(MaxFluidSolverClass):
        ...
    class Missing_Morph_Control(MorphController):
        ...
    class Missing_MotCapDev(MotionCaptureDeviceBindingClass):
        ...
    class Missing_Mtl(Material):
        ...
    class Missing_OSM(Modifier):
        ...
    class Missing_Point3_Control(Point3Controller):
        ...
    class Missing_Point4_Control(Point4Controller):
        ...
    class Missing_Position_Control(PositionController):
        ...
    class Missing_Radiosity(RadiosityEffect):
        ...
    class Missing_RefMaker(ReferenceMaker):
        ...
    class Missing_RefTarget(ReferenceTarget):
        ...
    class Missing_Render_Effect(RenderEffect):
        ...
    class Missing_Render_Element_Plug_In(RenderElement):
        ...
    class Missing_Renderer(RendererClass):
        ...
    class Missing_Rotation_Control(RotationController):
        ...
    class Missing_Sampler(SamplerClass):
        ...
    class Missing_Scale_Control(ScaleController):
        ...
    class Missing_Shader_Plug_In(Shader):
        ...
    class Missing_Shadow_Type(Shadow):
        ...
    class Missing_Shape(Shape):
        ...
    class Missing_SoundObj(SoundClass):
        ...
    class Missing_System(System):
        ...
    class Missing_TextureMap(TextureMap):
        ...
    class Missing_Texture_Bake_Element(BakeElement):
        ...
    class Missing_Texture_Output_Plug_In(TexOutputClass):
        ...
    class Missing_UVGen(UVGenClass):
        ...
    class Missing_UVW_Coordinates(GlobalUtilityPlugin):
        ...
    class Missing_User_Type_Control(CtrlUserDataTypeClass):
        ...
    class Missing_WSM(SpacewarpModifier):
        ...
    class Missing_WSM_Object(SpacewarpObject):
        ...
    class Missing_XYZGen(XYZGenClass):
        ...
    class Mitchell_Netravali(Filter):
        BLUR: float
        RINGING: float
        ...
    class Mix(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        LOWER: float
        MAP1: None
        MAP1ENABLED: bool
        MAP2: None
        MAP2ENABLED: bool
        MASK: None
        MASKENABLED: bool
        MIXAMOUNT: float
        OUTPUT: MXSWrapperBase
        UPPER: float
        USECURVE: bool
        ...
    class Mixer(Value):
        ...
    class MixinInterface(Value):
        ...
    class MoFlow(Value):
        ...
    class MoFlowScript(Value):
        ...
    class MoFlowSnippet(Value):
        ...
    class MoFlowTranInfo(Value):
        ...
    class MoFlowTransition(Value):
        ...
    class MocapLayer(FloatController):
        ...
    class MocapLayerInfo(FloatController):
        ...
    class ModRBClass(Modifier):
        ANGULARDAMPING: float
        BAKED: int
        BOUNCINESS: float
        COLLIDEWITHRIGIDBODIES: bool
        COMPOSITEHIGHQUALITY: bool
        COMPOSITEMAXCONCAVITY: float
        COMPOSITEMAXVERTICES: int
        CONTACTSHELLCONTACTDISTANCE: float
        CONTACTSHELLOVERRIDEGLOBALS: bool
        CONTACTSHELLRESTDEPTH: float
        CONTINUOUSCOLLISIONDETECTION: bool
        DENSITY: float
        DYNAMICFRICTION: float
        ENABLEADVANCEDSETTINGS: int
        ENABLEBACKFACECOLLISION: bool
        ENABLEGRAVITY: bool
        ENABLESOLIDMESHES: bool
        EXTRASHAPES: None
        FORCESLIST: MXSWrapperBase
        INITIALMOTIONSTYLE: int
        INITIALSPINX: float
        INITIALSPINY: float
        INITIALSPINZ: float
        INITIALVELOCITYX: float
        INITIALVELOCITYY: float
        INITIALVELOCITYZ: float
        LINEARDAMPING: float
        MANUALSETUP: bool
        MASS: float
        MASSCENTERMODE: int
        MASSCENTERX: float
        MASSCENTERY: float
        MASSCENTERZ: float
        MATERIALID: int
        MESHCONVEXSTYLE: int
        MESHCUSTOMMESH: None
        MESHHEIGHT: float
        MESHINFLATION: float
        MESHLENGTH: float
        MESHOVERRIDEMATERIAL: bool
        MESHRADIUS: float
        MESHTYPE: int
        MESHVERTICESLIMIT: int
        MESHWIDTH: float
        SHOWPHYSICALMESH: bool
        SLEEPATSTART: bool
        SMALLCLUSTERTHRESHOLD: float
        SOLVERITER: bool
        SOLVERITERVALUE: int
        SPINSPEED: float
        STATICFRICTION: float
        SWITCHTYPE: bool
        SWITCHTYPEATFRAME: int
        TYPE: int
        VELOCITYSPEED: float
        VOLUME: float
        ...
    class ModifierClass(Value):
        ...
    class MonoGraph(FloatController):
        ...
    class Morph(GeometryClass):
        ...
    class MorphByBone(Modifier):
        BONES: MXSWrapperBase
        BONESIZE: float
        EDGELIMIT: int
        ENABLED: bool
        FALLOFF: int
        FALLOFFGRAPHS: MXSWrapperBase
        INFLUENCEANGLE: float
        JOINTTYPE: int
        MATRIXSIZE: float
        MIRROROFFSET: float
        MIRRORPLANE: int
        MIRRORTHRESHOLD: float
        MORPHNAME: None
        PREVIEWBONE: bool
        PREVIEWVERTS: bool
        RELOADSELECTED: bool
        SAFEMODE: bool
        SELECTIONRADIUS: float
        SHOWCURRENTANGLE: bool
        SHOWDELTAS: bool
        SHOWDRIVERBONE: bool
        SHOWEDGES: bool
        SHOWLIMITANGLE: bool
        SHOWMIRRORPLANE: bool
        SHOWMORPHBONE: bool
        SHOWX: bool
        SHOWY: bool
        SHOWZ: bool
        SOFTSELECTIONGRAPH: MXSWrapperBase
        TARGETNODES: MXSWrapperBase
        USEEDGELIMIT: bool
        USESOFTSELECTION: bool
        ...
    class MorphController(MAXWrapper):
        ...
    class Morph_Angle_Deformer(ReferenceTarget):
        ...
    class Morpher(Modifier):
        AUTOLOAD_OF_TARGETS: int
        SPINNER_MAXIMUM: float
        SPINNER_MINIMUM: float
        USE_LIMITS: int
        USE_SELECTION: int
        VALUE_INCREMENTS: int
        ...
    class MorpherMaterial(Material):
        BASE: MXSWrapperBase
        CHANNEL_0: float
        CHANNEL_100: int
        CHANNEL_10: float
        CHANNEL_11: float
        CHANNEL_12: float
        CHANNEL_13: float
        CHANNEL_14: float
        CHANNEL_15: float
        CHANNEL_16: float
        CHANNEL_17: float
        CHANNEL_18: float
        CHANNEL_19: float
        CHANNEL_1: float
        CHANNEL_20: float
        CHANNEL_21: float
        CHANNEL_22: float
        CHANNEL_23: float
        CHANNEL_24: float
        CHANNEL_25: float
        CHANNEL_26: float
        CHANNEL_27: float
        CHANNEL_28: float
        CHANNEL_29: float
        CHANNEL_2: float
        CHANNEL_30: float
        CHANNEL_31: float
        CHANNEL_32: float
        CHANNEL_33: float
        CHANNEL_34: float
        CHANNEL_35: float
        CHANNEL_36: float
        CHANNEL_37: float
        CHANNEL_38: float
        CHANNEL_39: float
        CHANNEL_3: float
        CHANNEL_40: float
        CHANNEL_41: float
        CHANNEL_42: float
        CHANNEL_43: float
        CHANNEL_44: float
        CHANNEL_45: float
        CHANNEL_46: float
        CHANNEL_47: float
        CHANNEL_48: float
        CHANNEL_49: float
        CHANNEL_4: float
        CHANNEL_50: float
        CHANNEL_51: float
        CHANNEL_52: float
        CHANNEL_53: float
        CHANNEL_54: float
        CHANNEL_55: float
        CHANNEL_56: float
        CHANNEL_57: float
        CHANNEL_58: float
        CHANNEL_59: float
        CHANNEL_5: float
        CHANNEL_60: float
        CHANNEL_61: float
        CHANNEL_62: float
        CHANNEL_63: float
        CHANNEL_64: float
        CHANNEL_65: float
        CHANNEL_66: float
        CHANNEL_67: float
        CHANNEL_68: float
        CHANNEL_69: float
        CHANNEL_6: float
        CHANNEL_70: float
        CHANNEL_71: float
        CHANNEL_72: float
        CHANNEL_73: float
        CHANNEL_74: float
        CHANNEL_75: float
        CHANNEL_76: float
        CHANNEL_77: float
        CHANNEL_78: float
        CHANNEL_79: float
        CHANNEL_7: float
        CHANNEL_80: float
        CHANNEL_81: float
        CHANNEL_82: float
        CHANNEL_83: float
        CHANNEL_84: float
        CHANNEL_85: float
        CHANNEL_86: float
        CHANNEL_87: float
        CHANNEL_88: float
        CHANNEL_89: float
        CHANNEL_8: float
        CHANNEL_90: float
        CHANNEL_91: float
        CHANNEL_92: float
        CHANNEL_93: float
        CHANNEL_94: float
        CHANNEL_95: float
        CHANNEL_96: float
        CHANNEL_97: float
        CHANNEL_98: float
        CHANNEL_99: float
        CHANNEL_9: float
        MAT_100: None
        MAT_10: None
        MAT_11: None
        MAT_12: None
        MAT_13: None
        MAT_14: None
        MAT_15: None
        MAT_16: None
        MAT_17: None
        MAT_18: None
        MAT_19: None
        MAT_1: None
        MAT_20: None
        MAT_21: None
        MAT_22: None
        MAT_23: None
        MAT_24: None
        MAT_25: None
        MAT_26: None
        MAT_27: None
        MAT_28: None
        MAT_29: None
        MAT_2: None
        MAT_30: None
        MAT_31: None
        MAT_32: None
        MAT_33: None
        MAT_34: None
        MAT_35: None
        MAT_36: None
        MAT_37: None
        MAT_38: None
        MAT_39: None
        MAT_3: None
        MAT_40: None
        MAT_41: None
        MAT_42: None
        MAT_43: None
        MAT_44: None
        MAT_45: None
        MAT_46: None
        MAT_47: None
        MAT_48: None
        MAT_49: None
        MAT_4: None
        MAT_50: None
        MAT_51: None
        MAT_52: None
        MAT_53: None
        MAT_54: None
        MAT_55: None
        MAT_56: None
        MAT_57: None
        MAT_58: None
        MAT_59: None
        MAT_5: None
        MAT_60: None
        MAT_61: None
        MAT_62: None
        MAT_63: None
        MAT_64: None
        MAT_65: None
        MAT_66: None
        MAT_67: None
        MAT_68: None
        MAT_69: None
        MAT_6: None
        MAT_70: None
        MAT_71: None
        MAT_72: None
        MAT_73: None
        MAT_74: None
        MAT_75: None
        MAT_76: None
        MAT_77: None
        MAT_78: None
        MAT_79: None
        MAT_7: None
        MAT_80: None
        MAT_81: None
        MAT_82: None
        MAT_83: None
        MAT_84: None
        MAT_85: None
        MAT_86: None
        MAT_87: None
        MAT_88: None
        MAT_89: None
        MAT_8: None
        MAT_90: None
        MAT_91: None
        MAT_92: None
        MAT_93: None
        MAT_94: None
        MAT_95: None
        MAT_96: None
        MAT_97: None
        MAT_98: None
        MAT_99: None
        MAT_9: None
        ...
    class MotionCaptureDeviceBindingClass(MAXWrapper):
        ...
    class MotionCaptureDeviceClass(MAXWrapperNonRefTarg):
        ...
    class MotionRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        VELOCITYMAX: float
        VELOCITYON: bool
        ...
    class MotionTracker(Value):
        ...
    class Motion_Blur(RenderEffect):
        DURATION: float
        TRANSPARENCY: bool
        ...
    class Motion_BlurMPassCamEffect(MPassCamEffect):
        BIAS: float
        DISABLEANTIALIASING: bool
        DISABLEFILTERING: bool
        DISPLAYPASSES: bool
        DITHERSTRENGTH: float
        DURATION: float
        NORMALIZEWEIGHTS: bool
        TILESIZE: int
        TOTALPASSES: int
        ...
    class Motion_Capture(UtilityPlugin):
        ...
    class Motion_Clip(FloatController):
        ...
    class Motion_ClipFloatController(FloatController):
        ...
    class Motion_Clip_SlaveFloat(FloatController):
        ...
    class Motion_Clip_SlavePoint3(Point3Controller):
        ...
    class Motion_Clip_SlavePos(PositionController):
        ...
    class Motion_Clip_SlaveRotation(RotationController):
        ...
    class Motion_Clip_SlaveScale(ScaleController):
        ...
    class Motor(SpacewarpObject):
        AMPLITUDE_1: float
        AMPLITUDE_2: float
        BASIC_TORQUE: float
        CONTROL_GAIN: float
        ENABLE_VARIATION: int
        FEEDBACK_ON: int
        ICON_SIZE: float
        OFF_TIME: MXSWrapperBase
        ON_TIME: MXSWrapperBase
        RANGE_ENABLE: int
        RANGE_VALUE: float
        REVERSIBLE: int
        REVS_UNITS: int
        TARGET_REVS: float
        UNITS: int
        VARIATION_PERIOD_1: MXSWrapperBase
        VARIATION_PERIOD_2: MXSWrapperBase
        VARIATION_PHASE_1: float
        VARIATION_PHASE_2: float
        ...
    class MotorMod(SpacewarpModifier):
        ...
    class MouseConfigManager(Interface):
        ...
    class MouseTool(Value):
        ...
    class Mouse_Input_Device(ReferenceTarget):
        ...
    class Mouse_Input_DeviceMotionCaptureDeviceBindingClass(MotionCaptureDeviceBindingClass):
        ...
    class Mouse_Input_DeviceMotionCaptureDeviceClass(MotionCaptureDeviceClass):
        ...
    class MrmMod(Modifier):
        BASEVERTICES: bool
        BOUNDARYMETRIC: bool
        CREASEANGLE: float
        MERGETHRESHOLD: float
        MERGEVERTEX: bool
        MERGEWITHINMESH: bool
        MULTIVERTNORM: bool
        REQGENERATE: bool
        RESETPARAMS: bool
        VERTEXCOUNT: int
        VERTEXPERCENT: float
        ...
    class MtlBaseLib(ReferenceMaker):
        ...
    class MtlBrowserFilter_Manager(Interface):
        ...
    class MtlButtonControl(Value):
        ...
    class MtlLib(ReferenceMaker):
        ...
    class MultDeleg(ReferenceTarget):
        ACTIVE: bool
        ANIMOBJNODE: None
        AVERAGESPEED1: float
        AVERAGESPEED2: float
        BANKFACTOR1: float
        BANKFACTOR2: float
        BIPEDASSOCIATIONTYPE: bool
        BIPEDASSOCIATIONUSEBIP: bool
        BIPEDDELEGATES: MXSWrapperBase
        BIPEDS: MXSWrapperBase
        DECLINEDECEL1: float
        DECLINEDECEL2: float
        DECLINEDECELANGLE1: float
        DECLINEDECELANGLE2: float
        DELEGATES: MXSWrapperBase
        EDITSETTING: MXSWrapperBase
        INCLINEDECEL1: float
        INCLINEDECEL2: float
        INCLINEDECELANGLE1: float
        INCLINEDECELANGLE2: float
        MAXACCEL1: float
        MAXACCEL2: float
        MAXBANK1: float
        MAXBANK2: float
        MAXBANKRATE1: float
        MAXBANKRATE2: float
        MAXDECLINE1: float
        MAXDECLINE2: float
        MAXHEADING1: float
        MAXHEADING2: float
        MAXHEADINGRATE1: float
        MAXHEADINGRATE2: float
        MAXINCLINE1: float
        MAXINCLINE2: float
        PRIORITY1: int
        PRIORITY2: int
        RAND10: bool
        RAND11: bool
        RAND12: bool
        RAND13: bool
        RAND14: bool
        RAND15: bool
        RAND17: bool
        RAND18: bool
        RAND1: bool
        RAND2: bool
        RAND3: bool
        RAND4: bool
        RAND5: bool
        RAND6: bool
        RAND7: bool
        RAND8: bool
        RAND9: bool
        SET10: bool
        SET11: bool
        SET12: bool
        SET13: bool
        SET14: bool
        SET15: bool
        SET16: bool
        SET17: bool
        SET18: bool
        SET19: bool
        SET1: bool
        SET20: bool
        SET21: bool
        SET22: bool
        SET24: bool
        SET25: bool
        SET26: bool
        SET2: bool
        SET3: bool
        SET4: bool
        SET5: bool
        SET6: bool
        SET7: bool
        SET8: bool
        SET9: bool
        SETTINGS: MXSWrapperBase
        SHOWCOGSTATES: bool
        SHOWFORCES: bool
        SHOWVELOCITY: bool
        STARTCLIP: int
        STARTFRAME1: int
        STARTFRAME2: int
        TURNDECEL1: float
        TURNDECEL2: float
        TURNDECELANGLE1: float
        TURNDECELANGLE2: float
        USEBIPED: bool
        USEHIERBBOX: bool
        VELOCITYCOLOR: MXSWrapperBase
        XYCONSTRAIN: bool
        ...
    class MultiLayer(Shader):
        ...
    class MultiListBoxControl(RolloutControl):
        ...
    class MultiMaterialClass(Value):
        ...
    class MultiOutputChannelTexmapToTexmap(TextureMap):
        OUTPUTCHANNELINDEX: int
        SOURCEMAP: None
        ...
    class MultiRes(Modifier):
        BASEVERTICES: bool
        BOUNDARYMETRIC: bool
        CREASEANGLE: float
        MERGETHRESHOLD: float
        MERGEVERTEX: bool
        MERGEWITHINMESH: bool
        MULTIVERTNORM: bool
        REQGENERATE: bool
        RESETPARAMS: bool
        VERTEXCOUNT: int
        VERTEXPERCENT: float
        ...
    class MultiTile(TextureMap):
        ...
    class MultiTileMap(TextureMap):
        ...
    class Multi_Layer(Shader):
        ...
    class Multimaterial(Material):
        MAPENABLED: MXSWrapperBase
        MATERIALIDLIST: MXSWrapperBase
        MATERIALLIST: MXSWrapperBase
        NAMES: MXSWrapperBase
        ...
    class Multimaterial_Empty(Material):
        ...
    class MultipleEdgeClass(GlobalUtilityPlugin):
        ...
    class MultipleEdges(Interface):
        ...
    class MultipleFSParams(Value):
        ...
    class Multiple_Delegate_Settings(ReferenceTarget):
        ACTIVE: bool
        AVERAGESPEED1: float
        AVERAGESPEED2: float
        BANKFACTOR1: float
        BANKFACTOR2: float
        DECLINEDECEL1: float
        DECLINEDECEL2: float
        DECLINEDECELANGLE1: float
        DECLINEDECELANGLE2: float
        DELEGATES: MXSWrapperBase
        INCLINEDECEL1: float
        INCLINEDECEL2: float
        INCLINEDECELANGLE1: float
        INCLINEDECELANGLE2: float
        MAXACCEL1: float
        MAXACCEL2: float
        MAXBANK1: float
        MAXBANK2: float
        MAXBANKACCEL1: float
        MAXBANKACCEL2: float
        MAXDECLINE1: float
        MAXDECLINE2: float
        MAXINCLINE1: float
        MAXINCLINE2: float
        MAXTURN1: float
        MAXTURN2: float
        MAXTURNACCEL1: float
        MAXTURNACCEL2: float
        NAME: None
        PRIORITY1: int
        PRIORITY2: int
        RAND10: bool
        RAND11: bool
        RAND12: bool
        RAND13: bool
        RAND14: bool
        RAND15: bool
        RAND16: bool
        RAND17: bool
        RAND18: bool
        RAND1: bool
        RAND2: bool
        RAND3: bool
        RAND4: bool
        RAND5: bool
        RAND6: bool
        RAND7: bool
        RAND8: bool
        RAND9: bool
        SET10: bool
        SET11: bool
        SET12: bool
        SET13: bool
        SET14: bool
        SET15: bool
        SET16: bool
        SET17: bool
        SET18: bool
        SET19: bool
        SET1: bool
        SET20: bool
        SET21: bool
        SET22: bool
        SET23: bool
        SET24: bool
        SET25: bool
        SET26: bool
        SET2: bool
        SET3: bool
        SET4: bool
        SET5: bool
        SET6: bool
        SET7: bool
        SET8: bool
        SET9: bool
        SHOWCOGSTATES: bool
        SHOWFORCES: bool
        SHOWVELOCITY: bool
        STARTCLIP: int
        STARTFRAME1: int
        STARTFRAME2: int
        TURNDECEL1: float
        TURNDECEL2: float
        TURNDECELANGLE1: float
        TURNDECELANGLE2: float
        USEBIPED: bool
        USEHIERBBOX: bool
        VELOCITYCOLOR: MXSWrapperBase
        XYCONSTRAIN: bool
        ...
    class Multiple_Delegates(ReferenceTarget):
        ACTIVE: bool
        ANIMOBJNODE: None
        AVERAGESPEED1: float
        AVERAGESPEED2: float
        BANKFACTOR1: float
        BANKFACTOR2: float
        BIPEDASSOCIATIONTYPE: bool
        BIPEDASSOCIATIONUSEBIP: bool
        BIPEDDELEGATES: MXSWrapperBase
        BIPEDS: MXSWrapperBase
        DECLINEDECEL1: float
        DECLINEDECEL2: float
        DECLINEDECELANGLE1: float
        DECLINEDECELANGLE2: float
        DELEGATES: MXSWrapperBase
        EDITSETTING: MXSWrapperBase
        INCLINEDECEL1: float
        INCLINEDECEL2: float
        INCLINEDECELANGLE1: float
        INCLINEDECELANGLE2: float
        MAXACCEL1: float
        MAXACCEL2: float
        MAXBANK1: float
        MAXBANK2: float
        MAXBANKRATE1: float
        MAXBANKRATE2: float
        MAXDECLINE1: float
        MAXDECLINE2: float
        MAXHEADING1: float
        MAXHEADING2: float
        MAXHEADINGRATE1: float
        MAXHEADINGRATE2: float
        MAXINCLINE1: float
        MAXINCLINE2: float
        PRIORITY1: int
        PRIORITY2: int
        RAND10: bool
        RAND11: bool
        RAND12: bool
        RAND13: bool
        RAND14: bool
        RAND15: bool
        RAND17: bool
        RAND18: bool
        RAND1: bool
        RAND2: bool
        RAND3: bool
        RAND4: bool
        RAND5: bool
        RAND6: bool
        RAND7: bool
        RAND8: bool
        RAND9: bool
        SET10: bool
        SET11: bool
        SET12: bool
        SET13: bool
        SET14: bool
        SET15: bool
        SET16: bool
        SET17: bool
        SET18: bool
        SET19: bool
        SET1: bool
        SET20: bool
        SET21: bool
        SET22: bool
        SET24: bool
        SET25: bool
        SET26: bool
        SET2: bool
        SET3: bool
        SET4: bool
        SET5: bool
        SET6: bool
        SET7: bool
        SET8: bool
        SET9: bool
        SETTINGS: MXSWrapperBase
        SHOWCOGSTATES: bool
        SHOWFORCES: bool
        SHOWVELOCITY: bool
        STARTCLIP: int
        STARTFRAME1: int
        STARTFRAME2: int
        TURNDECEL1: float
        TURNDECEL2: float
        TURNDECELANGLE1: float
        TURNDECELANGLE2: float
        USEBIPED: bool
        USEHIERBBOX: bool
        VELOCITYCOLOR: MXSWrapperBase
        XYCONSTRAIN: bool
        ...
    class Multiple_Edges(GlobalUtilityPlugin):
        ...
    class MusclePatch(Helper):
        ...
    class MuscleStrand(Helper):
        ...
    class Muscle_Handle(Helper):
        ...
    class Muscle_Strand(Helper):
        ...
    class MxsUnitResults(Interface):
        ...
    class NCurve_Sel(Modifier):
        ...
    class NLAInfo(FloatController):
        ...
    class NPRFragment(GraphicsFragmentPlugin):
        ...
    class NSurf_Sel(Modifier):
        ...
    class NURBS1RailSweepSurface(NURBSSurface):
        ...
    class NURBS2RailSweepSurface(NURBSSurface):
        ...
    class NURBSBlendCurve(NURBSCurve):
        ...
    class NURBSBlendSurface(NURBSSurface):
        ...
    class NURBSCVCurve(NURBSCurve):
        ...
    class NURBSCVSurface(NURBSSurface):
        ...
    class NURBSCapSurface(NURBSSurface):
        ...
    class NURBSChamferCurve(NURBSCurve):
        ...
    class NURBSControlVertex(NURBSObject):
        ...
    class NURBSCurve(NURBSObject):
        ...
    class NURBSCurveConstPoint(NURBSPoint):
        ...
    class NURBSCurveIntersectPoint(NURBSPoint):
        ...
    class NURBSCurveOnSurface(NURBSCVCurve):
        ...
    class NURBSCurveSurfaceIntersectPoint(NURBSPoint):
        ...
    class NURBSCurveshape(Shape):
        ...
    class NURBSDisplay(Value):
        ...
    class NURBSExtrudeNode(Primitive):
        ...
    class NURBSExtrudeSurface(NURBSSurface):
        ...
    class NURBSFilletCurve(NURBSCurve):
        ...
    class NURBSFilletSurface(NURBSSurface):
        ...
    class NURBSGenericMethods(Value):
        ...
    class NURBSGenericMethodsWrapper(Value):
        ...
    class NURBSIndependentPoint(NURBSPoint):
        ...
    class NURBSIsoCurve(NURBSCurve):
        ...
    class NURBSLatheNode(Primitive):
        ...
    class NURBSLatheSurface(NURBSSurface):
        ...
    class NURBSMirrorCurve(NURBSCurve):
        ...
    class NURBSMirrorSurface(NURBSSurface):
        ...
    class NURBSMultiCurveTrimSurface(NURBSSurface):
        ...
    class NURBSNBlendSurface(NURBSSurface):
        ...
    class NURBSNode(Primitive):
        ...
    class NURBSObject(Value):
        ...
    class NURBSOffsetCurve(NURBSCurve):
        ...
    class NURBSOffsetSurface(NURBSSurface):
        ...
    class NURBSPoint(NURBSObject):
        ...
    class NURBSPointConstPoint(NURBSPoint):
        ...
    class NURBSPointCurve(NURBSCurve):
        ...
    class NURBSPointCurveOnSurface(NURBSPointCurve):
        ...
    class NURBSPointSurface(NURBSSurface):
        ...
    class NURBSProjectNormalCurve(NURBSCurve):
        ...
    class NURBSProjectVectorCurve(NURBSCurve):
        ...
    class NURBSRuledSurface(NURBSSurface):
        ...
    class NURBSSelection(Value):
        ...
    class NURBSSelector(Value):
        ...
    class NURBSSet(Value):
        ...
    class NURBSSurf(GeometryClass):
        ...
    class NURBSSurfConstPoint(NURBSPoint):
        ...
    class NURBSSurfSurfIntersectionCurve(NURBSCurve):
        ...
    class NURBSSurface(NURBSObject):
        ...
    class NURBSSurfaceApproximation(Value):
        ...
    class NURBSSurfaceEdgeCurve(NURBSCurve):
        ...
    class NURBSSurfaceNormalCurve(NURBSCurve):
        ...
    class NURBSTexturePoint(NURBSObject):
        ...
    class NURBSTextureSurface(Value):
        ...
    class NURBSULoftSurface(NURBSSurface):
        ...
    class NURBSUVLoftSurface(NURBSSurface):
        ...
    class NURBSXFormCurve(NURBSCurve):
        ...
    class NURBSXFormSurface(NURBSSurface):
        ...
    class NURBS_Imported_Objects(GeometryClass):
        ...
    class NVIDIARenderersHelper(Interface):
        ...
    class NamedSelSetList(ReferenceMaker):
        ...
    class NamedSelSetListChanged(Primitive):
        ...
    class NamedSelectionSetManager(Interface):
        ...
    class NavInfo(Helper):
        ...
    class NetCreateHelpers(Interface):
        ...
    class NetworkLicenseStatusManager(Interface):
        ...
    class NetworkManager(Interface):
        ...
    class NetworkRTT(Primitive):
        ...
    class NewDefaultBoolController(Primitive):
        ...
    class NewDefaultColorController(Primitive):
        ...
    class NewDefaultFRGBAController(Primitive):
        ...
    class NewDefaultFloatController(Primitive):
        ...
    class NewDefaultMasterPointController(Primitive):
        ...
    class NewDefaultMatrix3Controller(Primitive):
        ...
    class NewDefaultPoint2Controller(Primitive):
        ...
    class NewDefaultPoint3Controller(Primitive):
        ...
    class NewDefaultPoint4Controller(Primitive):
        ...
    class NewDefaultPositionController(Primitive):
        ...
    class NewDefaultRotationController(Primitive):
        ...
    class NewDefaultScaleController(Primitive):
        ...
    class Ngon(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        CIRCULAR: bool
        CORNERRADIUS: float
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        MAPCOORDS: bool
        NSIDES: int
        OPTIMIZE: bool
        QUAD_CAP: bool
        RADIUS: float
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SCRIBE: int
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        ...
    class NitrousGraphicsManager(Interface):
        ...
    class NitrousLightWorldGenFragment(GraphicsFragmentPlugin):
        ...
    class NitrousPostSceneWorldGenFragment(GraphicsFragmentPlugin):
        ...
    class NitrousPreSceneWorldGenFragment(GraphicsFragmentPlugin):
        ...
    class NitrousRenderWorldGenFragment(GraphicsFragmentPlugin):
        ...
    class NoMaterial(Material):
        ...
    class NoTexture(TextureMap):
        ...
    class NoValueClass(Value):
        ...
    class NodeChildrenArray(Value):
        ...
    class NodeCloneMgrTest(Interface):
        ...
    class NodeColorPicker(Primitive):
        ...
    class NodeEventCallback(Value):
        ...
    class NodeGeneric(Value):
        ...
    class NodeIKParamsChanged(Primitive):
        ...
    class NodeInvalRect(Primitive):
        ...
    class NodeJoeAttrDef(AttributeDef):
        ...
    class NodeJoeNodeAttrDef(AttributeDef):
        ...
    class NodeJoeNodeViewAttrDef(AttributeDef):
        ...
    class NodeMonitor(ReferenceTarget):
        ...
    class NodeNamedSelSet(ReferenceMaker):
        ...
    class NodeObject(Node):
        ...
    class NodeTrajectoryTest(Interface):
        ...
    class NodeTransformMonitor(ReferenceTarget):
        ...
    class Noise(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COORDS: MXSWrapperBase
        LEVELS: float
        MAP1: None
        MAP1ENABLED: bool
        MAP2: None
        MAP2ENABLED: bool
        OUTPUT: MXSWrapperBase
        PHASE: float
        SIZE: float
        THRESHOLDHIGH: float
        THRESHOLDLOW: float
        TYPE: int
        ...
    class Noise_Float(FloatController):
        FRACTAL: bool
        FREQUENCY: float
        POSITIVE: bool
        RAMPIN: MXSWrapperBase
        RAMPOUT: MXSWrapperBase
        ROUGHNESS: float
        SEED: int
        ...
    class Noise_Point3(Point3Controller):
        FRACTAL: bool
        FREQUENCY: float
        RAMPIN: MXSWrapperBase
        RAMPOUT: MXSWrapperBase
        ROUGHNESS: float
        SEED: int
        X_POSITIVE: bool
        Y_POSITIVE: bool
        Z_POSITIVE: bool
        ...
    class Noise_Position(PositionController):
        FRACTAL: bool
        FREQUENCY: float
        RAMPIN: MXSWrapperBase
        RAMPOUT: MXSWrapperBase
        ROUGHNESS: float
        SEED: int
        X_POSITIVE: bool
        Y_POSITIVE: bool
        Z_POSITIVE: bool
        ...
    class Noise_Rotation(RotationController):
        FRACTAL: bool
        FREQUENCY: float
        RAMPIN: MXSWrapperBase
        RAMPOUT: MXSWrapperBase
        ROUGHNESS: float
        SEED: int
        X_POSITIVE: bool
        Y_POSITIVE: bool
        Z_POSITIVE: bool
        ...
    class Noise_Scale(ScaleController):
        FRACTAL: bool
        FREQUENCY: float
        RAMPIN: MXSWrapperBase
        RAMPOUT: MXSWrapperBase
        ROUGHNESS: float
        SEED: int
        X_POSITIVE: bool
        Y_POSITIVE: bool
        Z_POSITIVE: bool
        ...
    class Noisemodifier(Modifier):
        ANIMATE: bool
        FRACTAL: bool
        FREQUENCY: float
        ITERATIONS: float
        PHASE: MXSWrapperBase
        ROUGHNESS: float
        SCALE: float
        SEED: int
        STRENGTH: MXSWrapperBase
        ...
    class NormalMappingManager(Interface):
        ...
    class Normal_Bump(TextureMap):
        BUMP_MAP: None
        BUMP_SPIN: float
        FLIPGREEN: bool
        FLIPRED: bool
        MAP1ON: bool
        MAP2ON: bool
        METHOD: int
        MULT_SPIN: float
        NORMAL_MAP: None
        SWAP_RG: bool
        ...
    class Normalize_Spl(Modifier):
        ...
    class Normalize_Spline(Modifier):
        ...
    class Normalize_Spline2(Modifier):
        FOREACHSPLINE: bool
        INSERTNUM: int
        LENGTH: float
        MAXKNOTS: int
        NORMALIZETYPE: int
        NUMKNOTS: int
        RETAINKNOTS: bool
        RETAINPERCENT: int
        RETAINTANGENTS: bool
        SHOWKNOTS: bool
        SIMPLEINTERPOLATION: bool
        USEMAXKNOTS: bool
        USESTRAIGHTSEGMENTS: bool
        WEIGHTED: bool
        ...
    class Normalmodifier(Modifier):
        FLIP: bool
        UNIFY: bool
        ...
    class NormalsMap(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        TARGETMAPSLOTNAME: str
        USEHEIGHTASALPHA: bool
        USENORMALBUMP: bool
        ...
    class NoteTrack(Value):
        ...
    class Notes(Helper):
        COMMENTS: None
        ...
    class NotesReferenceTarget(ReferenceTarget):
        COMMENTS: None
        FILTER: None
        ...
    class NullFilter(ReferenceMaker):
        ...
    class NullInterface(Interface):
        ...
    class NumMapsUsed(Primitive):
        ...
    class NumSurfaces(Primitive):
        ...
    class Number(Value):
        ...
    class OBJPaintGetSetting(Primitive):
        ...
    class OBJPaintSetSetting(Primitive):
        ...
    class OGSDiagnostics(Interface):
        ...
    class OKToBindToNode(Primitive):
        ...
    class OLEMethod(Value):
        ...
    class OLEObject(Value):
        ...
    class OSLGlobalInterface(Interface):
        ...
    class OSLMap(TextureMap):
        A: MXSWrapperBase
        B: MXSWrapperBase
        INPUT_A: MXSWrapperBase
        INPUT_A_MAP: None
        INPUT_B: MXSWrapperBase
        INPUT_B_MAP: None
        MIXER: float
        MIXER_MAP: None
        OSLAUTOUPDATE: bool
        OSLCODE: str
        OSLPATH: str
        OSLSHADERNAME: str
        ...
    class OSnap(Primitive):
        ...
    class ObRefModAppClass(MAXWrapper):
        ...
    class ObjAssoc(ReferenceTarget):
        ALIGNSCALE: bool
        DELEGATES: MXSWrapperBase
        OBJECTS: MXSWrapperBase
        ...
    class ObjExp(ExporterPlugin):
        ...
    class ObjImp(ImporterPlugin):
        ...
    class ObjectParameter(ReferenceTarget):
        FILTER: None
        INPUT: None
        OBJECT: None
        SUBFRAME_SAMPLING: bool
        UNITS_PER_TYPE: int
        USE_AS_SPEED_OR_SPIN_RATE: bool
        ...
    class ObjectSet(Set):
        ...
    class ObjectSpaceSubdivideMod(Modifier):
        ADAPTIVEEDGELENGTH: float
        ADAPTIVEREGULARITY: float
        ADAPTIVETHRESHOLD: float
        DELAUNAYRELAXATIONCOEFF: float
        DELAUNAYRELAXATIONITERATIONS: int
        DELAUNAYSIZE: float
        MANUALUPDATE: int
        PRESERVEDMAPINDEX: int
        PRESERVEDSHARPEDGEANGLE: float
        PRESERVEMESHDATA: bool
        PRESERVESHARPEDGESBYANGLE: bool
        REMESHTYPE: int
        SHOWALLTRIANGLES: bool
        SIZE: float
        SUBDIVIDEDIAGONALRATIO: float
        SUBDIVIDEDOENFORCEQUALITY: bool
        SUBDIVIDEDOFORMQUADS: bool
        SUBDIVIDEDOSUBDIVIDETRIANGLES: bool
        SUBDIVIDEMAXSTEINERPOINTS: int
        SUBDIVIDENUMBUCKETS: int
        SUBDIVIDEQUADAREARATIO: float
        SUBDIVIDEREFINEMENTTYPE: int
        VARIABLECURVATUREEDGELENGTH: float
        VARIABLECURVATUREITERATIONS: int
        VARIABLECURVATUREREGULARITY: float
        VARIABLECURVATURETHRESHOLD: float
        VARIABLECURVATURETRANSITION: float
        VARIABLECURVATUREVARIABLEDENSITY: float
        ...
    class Object_Display_Culling(UtilityPlugin):
        ...
    class Object_ID(RenderElement):
        BITMAP: None
        COLORMODE: int
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class ObtainRenderTargetFragment(GraphicsFragmentPlugin):
        ...
    class OffsetManager(Interface):
        ...
    class OffsetManagerGUP(GlobalUtilityPlugin):
        ...
    class Offset_Manager_GUP(GlobalUtilityPlugin):
        ...
    class OilTank(GeometryClass):
        BLEND: float
        CAP_HEIGHT: float
        HEIGHT: float
        HEIGHT_SEGMENTS: int
        MAPCOORDS: int
        RADIUS: float
        SIDES: int
        SLICE_FROM: float
        SLICE_ON: int
        SLICE_TO: float
        SMOOTH_ON: int
        ...
    class OkClass(Value):
        ...
    class OkMtlForScene(Primitive):
        ...
    class OldBoolean(GeometryClass):
        ...
    class OldVertexPaint(Modifier):
        ...
    class Old_PointCache(Modifier):
        ...
    class Old_PointCacheWSM(SpacewarpModifier):
        ...
    class Old_Point_Cache(Modifier):
        ...
    class Old_Point_CacheSpacewarpModifier(SpacewarpModifier):
        ...
    class Omnilight(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        ATTENDECAY: int
        CASTSHADOWS: bool
        COLOR: MXSWrapperBase
        CONTRAST: float
        DECAYRADIUS: float
        ENABLED: bool
        EXCLUDELIST: MXSWrapperBase
        FARATTENEND: float
        FARATTENSTART: float
        HSV: MXSWrapperBase
        HUE: int
        INCLEXCLTYPE: int
        INCLUDELIST: None
        LIGHTAFFECTSSHADOW: bool
        MULTIPLIER: float
        NEARATTENEND: float
        NEARATTENSTART: float
        ON: bool
        PROJECTOR: bool
        PROJECTORMAP: None
        RAYTRACEDSHADOWS: bool
        RGB: MXSWrapperBase
        SATURATION: int
        SHADOWCOLOR: MXSWrapperBase
        SHADOWGENERATOR: MXSWrapperBase
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHOWFARATTEN: bool
        SHOWNEARATTEN: bool
        SOFTENDIFFUSEEDGE: float
        TYPE: MXSWrapperBase
        USEFARATTEN: bool
        USEGLOBALSHADOWSETTINGS: bool
        USENEARATTEN: bool
        USESHADOWPROJECTORMAP: bool
        VALUE: int
        ...
    class On_Off(FloatController):
        ...
    class OneClick(GlobalUtilityPlugin):
        ...
    class OneClickSource(ReferenceTarget):
        ...
    class One_Click_Particle_Flow(ReferenceTarget):
        ...
    class OpenEXR(BitmapIO):
        ...
    class OpenEdgesClass(GlobalUtilityPlugin):
        ...
    class OpenFbxSetting(Primitive):
        ...
    class OpenFltExport(ExporterPlugin):
        ...
    class OpenSubdiv(Modifier):
        ADAPTIVE: bool
        ADAPTIVEITERATIONS: int
        CREASEMETHOD: int
        FVARBOUNDARY: int
        ISOLINEDISPLAY: bool
        ITERATIONS: int
        MODE: int
        PROPAGATECORNERS: bool
        RENDERITERATIONS: int
        SMOOTHTRIANGLES: bool
        SOLVERTYPE: int
        UPDATE: int
        USERENDERITERATIONS: bool
        VERTBOUNDARY: int
        ...
    class OpenSubdivMod(Modifier):
        ADAPTIVE: bool
        ADAPTIVEITERATIONS: int
        CREASEMETHOD: int
        FVARBOUNDARY: int
        ISOLINEDISPLAY: bool
        ITERATIONS: int
        MODE: int
        PROPAGATECORNERS: bool
        RENDERITERATIONS: int
        SMOOTHTRIANGLES: bool
        SOLVERTYPE: int
        UPDATE: int
        USERENDERITERATIONS: bool
        VERTBOUNDARY: int
        ...
    class Open_Edges(GlobalUtilityPlugin):
        ...
    class OperatorGraph(ReferenceTarget):
        DATA: str
        NODES: MXSWrapperBase
        ...
    class OperatorGraphCustomAttribute(CustAttrib):
        GRAPH: None
        ...
    class OperatorGraphNode(ReferenceTarget):
        OPERATOR_ID: int
        OPERATOR_MAP: None
        ...
    class Operator_Clamp(IDataChannelEngineClass):
        ...
    class Operator_ColorElements(IDataChannelEngineClass):
        ...
    class Operator_ComponentSpace(IDataChannelEngineClass):
        ...
    class Operator_ConvertToSubObjectType(IDataChannelEngineClass):
        ...
    class Operator_Curvature(IDataChannelEngineClass):
        ...
    class Operator_Curve(IDataChannelEngineClass):
        ...
    class Operator_Decay(IDataChannelEngineClass):
        ...
    class Operator_DeltaMush(IDataChannelEngineClass):
        ...
    class Operator_Distort(IDataChannelEngineClass):
        ...
    class Operator_EdgeInput(IDataChannelEngineClass):
        ...
    class Operator_EdgeOutput(IDataChannelEngineClass):
        ...
    class Operator_FaceInput(IDataChannelEngineClass):
        ...
    class Operator_FaceOutput(IDataChannelEngineClass):
        ...
    class Operator_GeoQuantize(IDataChannelEngineClass):
        ...
    class Operator_Invert(IDataChannelEngineClass):
        ...
    class Operator_Maxscript(IDataChannelEngineClass):
        ...
    class Operator_NodeInfluence(IDataChannelEngineClass):
        ...
    class Operator_Normalize(IDataChannelEngineClass):
        ...
    class Operator_Point3_To_Float(IDataChannelEngineClass):
        ...
    class Operator_Scale(IDataChannelEngineClass):
        ...
    class Operator_Smooth(IDataChannelEngineClass):
        ...
    class Operator_TensionDeform(IDataChannelEngineClass):
        ...
    class Operator_TransformElements(IDataChannelEngineClass):
        ...
    class Operator_Vector(IDataChannelEngineClass):
        ...
    class Operator_Velocity(IDataChannelEngineClass):
        ...
    class Operator_VertexInput(IDataChannelEngineClass):
        ...
    class Operator_VertexOutput(IDataChannelEngineClass):
        ...
    class Operator_XYZSpace(IDataChannelEngineClass):
        ...
    class Optimize_Spline(Modifier):
        ADAPTIVE: bool
        ITERATIONS: int
        PERCENT: int
        REDUCEDMAXKNOTS: int
        REDUCEDMINKNOTS: int
        REDUCE_METHOD: int
        SHOWKNOTS: bool
        SUBSEGMENT: int
        ...
    class Orbaz_Mix(VideoPostFilter):
        ...
    class OrenNayarBlinn(Shader):
        ...
    class Oren_Nayar_Blinn(Shader):
        ...
    class OrientationBehavior(ReferenceTarget):
        BANKPERTURN: float
        HEADINGRELATIVE: bool
        HEADINGRESPONSE: float
        MAXBANK: float
        MAXBANKVEL: float
        MAXHEADING: float
        MAXHEADINGVEL: float
        MAXPITCH: float
        MAXPITCHVEL: float
        MINHEADING: float
        MINPITCH: float
        NAME: str
        PITCHRELATIVE: bool
        PITCHRESPONSE: float
        ...
    class Orientation_Behavior(ReferenceTarget):
        BANKPERTURN: float
        HEADINGRELATIVE: bool
        HEADINGRESPONSE: float
        MAXBANK: float
        MAXBANKVEL: float
        MAXHEADING: float
        MAXHEADINGVEL: float
        MAXPITCH: float
        MAXPITCHVEL: float
        MINHEADING: float
        MINPITCH: float
        NAME: str
        PITCHRELATIVE: bool
        PITCHRESPONSE: float
        ...
    class Orientation_Constraint(RotationController):
        LOCAL_WORLD: int
        RELATIVE: bool
        WEIGHT: MXSWrapperBase
        ...
    class Orthogonalize(MappedGeneric):
        ...
    class OutputCustom(ReferenceTarget):
        DATA_CHANNEL: None
        DATA_HANDLE: int
        EXECUTION_ORDER: int
        FILTER: None
        HISTORY_DEPENDENT: bool
        INPUT_1: None
        PRIORITY_ORDER: int
        PROCEED_TYPE: int
        ...
    class OutputNew(ReferenceTarget):
        DATA_HANDLE: int
        DATA_TYPE: int
        EXECUTION_ORDER: int
        FILTER: None
        HISTORY_DEPENDENT: bool
        INPUT_1: None
        PRIORITY_ORDER: int
        PROCEED_TYPE: int
        SCOPE_TYPE: int
        ...
    class OutputPhysX(ReferenceTarget):
        DATA_TYPE: int
        EXECUTION_ORDER: int
        FILTER: None
        HISTORY_DEPENDENT: bool
        INPUT: None
        MATCH_TYPE: int
        PRIORITY_ORDER: int
        PROCEED_TYPE: int
        THRESHOLD_TYPE: int
        ...
    class OutputStandard(ReferenceTarget):
        ACCELERATION_TYPE: int
        DATA_TYPE: int
        EXECUTION_ORDER: int
        FILTER: None
        HISTORY_DEPENDENT: bool
        INPUT_1: None
        INPUT_2: None
        MAPPING_TYPE: int
        MAP_CHANNEL: int
        POSITION_TYPE: int
        PRIORITY_ORDER: int
        PROCEED_TYPE: int
        ROTATION_TYPE: int
        SCALE_TYPE: int
        SCRIPT_TYPE: int
        SPEED_TYPE: int
        SPIN_TYPE: int
        TIME_TYPE: int
        TM_TYPE: int
        USE_E2: bool
        USE_T2: bool
        VIEWPORT_RENDER_OPERATOR: None
        VISIBILITY_TYPE: int
        ...
    class OutputTest(ReferenceTarget):
        EXECUTION_ORDER: int
        FILTER: None
        HISTORY_DEPENDENT: bool
        INPUT_1: None
        INPUT_2: None
        PRIORITY_ORDER: int
        PROCEED_TYPE: int
        TYPE: int
        USE_T2: bool
        ...
    class Output_MParticles(ReferenceTarget):
        DATA_TYPE: int
        EXECUTION_ORDER: int
        FILTER: None
        HISTORY_DEPENDENT: bool
        INPUT: None
        MATCH_TYPE: int
        PRIORITY_ORDER: int
        PROCEED_TYPE: int
        THRESHOLD_TYPE: int
        ...
    class OverlappedUVWFaces(Interface):
        ...
    class OverlappedUVWFacesClass(GlobalUtilityPlugin):
        ...
    class Overlapped_UVW_Faces(GlobalUtilityPlugin):
        ...
    class OverlappingFaces(Interface):
        ...
    class OverlappingFacesClass(GlobalUtilityPlugin):
        ...
    class OverlappingVertices(Interface):
        ...
    class OverlappingVerticesClass(GlobalUtilityPlugin):
        ...
    class Overlapping_Faces(GlobalUtilityPlugin):
        ...
    class Overlapping_Vertices(GlobalUtilityPlugin):
        ...
    class OverlayFragment(GraphicsFragmentPlugin):
        ...
    class PArray(GeometryClass):
        BIRTH_RATE: int
        BLUR_STRETCH: int
        BUBBLE_AMPLITUDE: float
        BUBBLE_AMPLITUDE_VARIATION: float
        BUBBLE_PERIOD: MXSWrapperBase
        BUBBLE_PERIOD_VARIATION: float
        BUBBLE_PHASE: float
        BUBBLE_PHASE_VARIATION: float
        DIE__X_FRAMES_AFTER_COLLISION: MXSWrapperBase
        DIE__X_FRAMES_AFTER_COLLISION_VARIATION: float
        DISPLAY_UNTIL: MXSWrapperBase
        DIVERGENCE_ANGLE: float
        EMITTER: None
        EMITTER_START: MXSWrapperBase
        EMITTER_STOP: MXSWrapperBase
        FADE_TIME: MXSWrapperBase
        FORMATION: int
        FRAGBACKMATID: int
        FRAGCHUNKMINIMUM: int
        FRAGEDGEMATID: int
        FRAGMENTMETHOD: int
        FRAGMENT_THICKNESS: float
        FRAGOUTSIDEMATID: int
        FRAGSMOOTHINGANGLE: float
        GROWTH_TIME: MXSWrapperBase
        ICONHIDDEN: bool
        ICONSIZE: float
        INSTANCEFRAMEOFFSET: int
        INSTANCEKEYOFFSETTYPE: int
        INSTANCESUBTREE: bool
        INSTANCINGOBJECT: None
        INTERPARTICLE_COLLISIONS_ON: int
        INTERPARTICLE_COLLISION_BOUNCE: float
        INTERPARTICLE_COLLISION_BOUNCE_VARIATION: float
        INTERPARTICLE_COLLISION_STEPS: int
        LIFE: MXSWrapperBase
        LIFESPANVALUEQUEUE: MXSWrapperBase
        LIFE_VARIATION: MXSWrapperBase
        MAPPINGTYPE: int
        MAPPING_DISTANCE_BASE: float
        MAPPING_TIME_BASE: MXSWrapperBase
        MATERIALSOURCE: int
        METABALLAUTOCOARSNESS: bool
        METABALLRENDERCOARSNESS: float
        METABALLVIEWCOARSNESS: float
        METAPARTICLE_TENSION: float
        METAPARTICLE_TENSION_VARIATION: float
        MOTIONINFLUENCE: float
        MOTIONMULTIPLIER: float
        MOTIONVARIATION: float
        NUMDISTINCTPOINTS: int
        OBJECTMUTATIONQUEUE: MXSWrapperBase
        PARTICLETYPE: int
        QUANTITYMETHOD: int
        SEED: int
        SIZE: float
        SIZE_VARIATION: float
        SPAWNINHERITVELOCITY: bool
        SPAWNSCALEFIXED: bool
        SPAWNSCALETYPE: int
        SPAWNSPEEDFIXED: bool
        SPAWNSPEEDTYPE: int
        SPAWNTYPE: int
        SPAWN_AFFECTS: int
        SPAWN_DIRECTION_CHAOS: float
        SPAWN_GENERATIONS: int
        SPAWN_LIFESPAN: int
        SPAWN_MULTIPLIER: int
        SPAWN_MULTIPLIER_VARIATION: float
        SPAWN_SCALE_CHAOS: float
        SPAWN_SPEED_CHAOS: float
        SPEED: float
        SPEED_VARIATION: float
        SPINAXISTYPE: int
        SPIN_AXIS_VARIATION: float
        SPIN_PHASE: float
        SPIN_PHASE_VARIATION: float
        SPIN_TIME: MXSWrapperBase
        SPIN_TIME_VARIATION: float
        STANDARDPARTICLE: int
        SUBSAMPLECREATIONTIME: bool
        SUBSAMPLEEMITTERROTATION: bool
        SUBSAMPLEEMITTERTRANSLATION: bool
        TOTAL_NUMBER: int
        USE_SELECTED_SUBOBJECTS: int
        VIEWPERCENT: float
        VIEWTYPE: int
        X_SPIN_VECTOR: float
        Y_SPIN_VECTOR: float
        Z_SPIN_VECTOR: float
        ...
    class PB2Parameter(ReferenceTarget):
        ...
    class PBEndTrack(Primitive):
        ...
    class PBRImporter(UtilityPlugin):
        ...
    class PBRMetalRough(Material):
        AO_AFFECTS_DIFFUSE: bool
        AO_AFFECTS_REFLECTION: bool
        AO_MAP: None
        BASECOLOR: MXSWrapperBase
        BASE_COLOR_MAP: None
        BUMP_MAP_AMT: float
        DISPLACEMENT_AMT: float
        DISPLACEMENT_MAP: None
        EMIT_COLOR: MXSWrapperBase
        EMIT_COLOR_MAP: None
        METALNESS: float
        METALNESS_MAP: None
        NORMAL_FLIP_GREEN: bool
        NORMAL_FLIP_RED: bool
        NORM_MAP: None
        OPACITY_MAP: None
        ROUGHNESS: float
        ROUGHNESS_MAP: None
        USEGLOSSINESS: int
        ...
    class PBRSpecGloss(Material):
        AO_AFFECTS_DIFFUSE: bool
        AO_AFFECTS_REFLECTION: bool
        AO_MAP: None
        BASECOLOR: MXSWrapperBase
        BASE_COLOR_MAP: None
        BUMP_MAP_AMT: float
        DISPLACEMENT_AMT: float
        DISPLACEMENT_MAP: None
        EMIT_COLOR: MXSWrapperBase
        EMIT_COLOR_MAP: None
        GLOSSINESS: float
        GLOSSINESS_MAP: None
        NORMAL_FLIP_GREEN: bool
        NORMAL_FLIP_RED: bool
        NORM_MAP: None
        OPACITY_MAP: None
        SPECULAR: MXSWrapperBase
        SPECULAR_MAP: None
        USEGLOSSINESS: int
        ...
    class PBStartTrack(Primitive):
        ...
    class PBTrackGetToolActive(Primitive):
        ...
    class PBomb(SpacewarpObject):
        CHAOS: float
        DECAY_TYPE: int
        ICON_SIZE: float
        LASTS_FOR: MXSWrapperBase
        RANGE: float
        START_TIME: MXSWrapperBase
        STRENGTH: float
        SYMMETRY: int
        ...
    class PBombMod(SpacewarpModifier):
        ...
    class PCloud(GeometryClass):
        BIRTH_RATE: int
        BLUR_STRETCH: int
        BUBBLE_AMPLITUDE: float
        BUBBLE_AMPLITUDE_VARIATION: float
        BUBBLE_PERIOD: MXSWrapperBase
        BUBBLE_PERIOD_VARIATION: float
        BUBBLE_PHASE: float
        BUBBLE_PHASE_VARIATION: float
        DIE__X_FRAMES_AFTER_COLLISION: MXSWrapperBase
        DIE__X_FRAMES_AFTER_COLLISION_VARIATION: float
        DIRECTIONVARIATION: float
        DIRECTION_VECTOR_X: float
        DIRECTION_VECTOR_Y: float
        DIRECTION_VECTOR_Z: float
        DISPLAY_UNTIL: MXSWrapperBase
        EMITTER: None
        EMITTERHIDDEN: bool
        EMITTER_HEIGHT: float
        EMITTER_RAD_LEN: float
        EMITTER_START: MXSWrapperBase
        EMITTER_STOP: MXSWrapperBase
        EMITTER_WIDTH: float
        FADE_TIME: MXSWrapperBase
        FORMATION: int
        GROWTH_TIME: MXSWrapperBase
        INSTANCEFRAMEOFFSET: int
        INSTANCEKEYOFFSETTYPE: int
        INSTANCESUBTREE: bool
        INSTANCINGOBJECT: None
        INTERPARTICLE_COLLISIONS_ON: int
        INTERPARTICLE_COLLISION_BOUNCE: float
        INTERPARTICLE_COLLISION_BOUNCE_VARIATION: float
        INTERPARTICLE_COLLISION_STEPS: int
        LIFE: MXSWrapperBase
        LIFESPANVALUEQUEUE: MXSWrapperBase
        LIFE_VARIATION: MXSWrapperBase
        MAPPINGTYPE: int
        MAPPING_DISTANCE_BASE: float
        MAPPING_TIME_BASE: MXSWrapperBase
        MATERIALSOURCE: int
        METABALLAUTOCOARSNESS: bool
        METABALLRENDERCOARSNESS: float
        METABALLVIEWCOARSNESS: float
        METAPARTICLE_TENSION: float
        METAPARTICLE_TENSION_VARIATION: float
        MOTIONINFLUENCE: float
        MOTIONMULTIPLIER: float
        MOTIONREFERENCEOBJECT: None
        MOTIONTYPE: int
        MOTIONVARIATION: float
        OBJECTMUTATIONQUEUE: MXSWrapperBase
        PARTICLETYPE: int
        QUANTITYMETHOD: int
        SEED: int
        SIZE: float
        SIZE_VARIATION: float
        SPAWNINHERITVELOCITY: bool
        SPAWNSCALEFIXED: bool
        SPAWNSCALETYPE: int
        SPAWNSPEEDFIXED: bool
        SPAWNSPEEDTYPE: int
        SPAWNTYPE: int
        SPAWN_DIRECTION_CHAOS: float
        SPAWN_GENERATIONS: int
        SPAWN_LIFESPAN: int
        SPAWN_MULTIPLIER: int
        SPAWN_SCALE_CHAOS: float
        SPAWN_SPEED_CHAOS: float
        SPEED: float
        SPEED_VARIATION: float
        SPINAXISTYPE: int
        SPIN_AXIS_VARIATION: float
        SPIN_PHASE: float
        SPIN_PHASE_VARIATION: float
        SPIN_TIME: MXSWrapperBase
        SPIN_TIME_VARIATION: float
        STANDARDPARTICLE: int
        TOTAL_NUMBER: int
        VIEWPERCENT: float
        VIEWTYPE: int
        X_SPIN_VECTOR: float
        Y_SPIN_VECTOR: float
        Z_SPIN_VECTOR: float
        ...
    class PDAlpha(VideoPostFilter):
        ...
    class PENCopyPaste_Vr(Array):
        ...
    class PFActionListPool(ReferenceTarget):
        ...
    class PFArrow(Helper):
        ...
    class PFBoxMeshWrapper(ReferenceTarget):
        ...
    class PFCapsuleMeshWrapper(ReferenceTarget):
        ...
    class PFConvexMeshWrapper(ReferenceTarget):
        ...
    class PFDataOperatorState(ReferenceTarget):
        ...
    class PFEngine(Helper):
        ...
    class PFFileBirth__State(ReferenceTarget):
        ...
    class PFHelperPhysXWorldState(ReferenceTarget):
        ...
    class PFIntegrator(ReferenceTarget):
        ...
    class PFNotifyDepCatcher(ReferenceTarget):
        ...
    class PFOperatorArnoldShapeState(ReferenceTarget):
        ...
    class PFOperatorBirthStreamState(ReferenceTarget):
        ...
    class PFOperatorFacingShapeState(ReferenceTarget):
        ...
    class PFOperatorInstanceShapeState(ReferenceTarget):
        ...
    class PFOperatorMarkShapeState(ReferenceTarget):
        ...
    class PFOperatorMaterialDynamicState(ReferenceTarget):
        ...
    class PFOperatorMaterialFrequencyState(ReferenceTarget):
        ...
    class PFOperatorMaterialState(ReferenceTarget):
        ...
    class PFOperatorMaterialStaticState(ReferenceTarget):
        ...
    class PFOperatorPositionOnObjectState(ReferenceTarget):
        ...
    class PFOperatorSimpleBirthState(ReferenceTarget):
        ...
    class PFOperatorSimplePositionState(ReferenceTarget):
        ...
    class PFOperatorSprayBirthState(ReferenceTarget):
        ...
    class PFOperatorSprayPlacementState(ReferenceTarget):
        ...
    class PFPlaneMeshWrapper(ReferenceTarget):
        ...
    class PFSimpleActionState(ReferenceTarget):
        ...
    class PFSphereMeshWrapper(ReferenceTarget):
        ...
    class PFSystemPool(ReferenceTarget):
        ...
    class PFTestPhysXGlueState(ReferenceTarget):
        ...
    class PFTestSplitByAmountState(ReferenceTarget):
        ...
    class PFTriangleMeshWrapper(ReferenceTarget):
        ...
    class PF_NotifyDep_Catcher(ReferenceTarget):
        ...
    class PF_Source(GeometryClass):
        CLEAR_SELECTION: bool
        EMITTER_HEIGHT: float
        EMITTER_LENGTH: float
        EMITTER_TYPE: int
        EMITTER_WIDTH: float
        ENABLE_PARTICLES: bool
        ENABLE_SCRIPT_FOR_EVERY_STEP_UPDATE: bool
        ENABLE_SCRIPT_FOR_FINAL_STEP_UPDATE: bool
        EVERY_STEP_UPDATE_SCRIPT: str
        EVERY_STEP_UPDATE_SCRIPT_FILE: str
        FINAL_STEP_UPDATE_SCRIPT: str
        FINAL_STEP_UPDATE_SCRIPT_FILE: str
        INTEGRATION_FOR_RENDER: int
        INTEGRATION_FOR_VIEWPORT: int
        LOGO_SIZE: float
        PARTICLE_AMOUNT_LIMIT: int
        QUANTITY_RENDER: float
        QUANTITY_VIEWPORT: float
        SELECTED_PARTICLES: MXSWrapperBase
        SELECTION_LEVEL: int
        SELECT_BY_PARTICLE_ID: int
        SHOW_EMITTER: bool
        SHOW_LOGO: bool
        USE_FILE_FOR_EVERY_STEP_UPDATE: bool
        USE_FILE_FOR_FINAL_STEP_UPDATE: bool
        WIDTH: int
        X_COORD: int
        Y_COORD: int
        Z_ORDER: int
        ...
    class PFlow_Collision_Shape(SpacewarpModifier):
        ACTIVE: bool
        DYNAMIC_FRICTION: float
        NORMAL_OFFSET: float
        PLACEMENT_EDGES: bool
        PLACEMENT_POLYGONS: bool
        PLACEMENT_VERTICES: bool
        PRIMITIVE_SIZE_TYPE: int
        RESTITUTION: float
        SELECTED_ONLY: bool
        SHAPE: int
        SIDE_OVERLAP: float
        SMOOTH_SURFACE: bool
        STATIC_FRICTION: float
        THICKNESS: float
        VISUALIZE_COLLISION_SHAPE: bool
        ...
    class PMAlpha(VideoPostFilter):
        ...
    class POmniFlect(SpacewarpObject):
        AFFECTS: float
        BOUNCE: float
        BOUNCEVAR: float
        CHAOS: float
        DECELERATION: float
        DECELVAR: float
        DIFFUSION: float
        DIFFUSIONVAR: float
        FRICTION: float
        HEIGHT: float
        INHERITVELOCITY: float
        PASSVELOCITY: float
        PASSVELOCITYVAR: float
        REFRACTION: float
        REFRACTIONVAR: float
        REFRACTS: float
        SPAWN: float
        TIMEOFF: MXSWrapperBase
        TIMEON: MXSWrapperBase
        WIDTH: float
        ...
    class POmniFlectMod(SpacewarpModifier):
        ...
    class PRTExport(Interface):
        ...
    class PSD_I_O(BitmapIO):
        ...
    class PViewManager(ReferenceTarget):
        ...
    class PView_Manager(ReferenceTarget):
        ...
    class PX_CreateBoundingBox(MAXScriptFunction):
        ...
    class PX_CreateBoundingCapsule(MAXScriptFunction):
        ...
    class PX_CreateBoundingConvex(MAXScriptFunction):
        ...
    class PX_CreateBoundingConvexForNodes(MAXScriptFunction):
        ...
    class PX_CreateBoundingSphere(MAXScriptFunction):
        ...
    class PX_CreateConvexHullFromPoints(MAXScriptFunction):
        ...
    class Paint(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class PaintLayerMod(Modifier):
        CASTSHADOWS: bool
        COLORBY: int
        HIDEUNSELSUBOBJS: bool
        IGNOREBACKFACING: bool
        LAYERISOLATED: bool
        LAYERMODE: str
        LAYEROPACITY: float
        LIGHTINGMODEL: int
        MAPCHANNEL: int
        RADIOSITYONLY: bool
        RADIOSITYOPTION: int
        SURVIVECONDENSE: bool
        USEMAPS: bool
        USERADIOSITY: bool
        ...
    class PaintRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class PaintSoftSelPresetContext(Interface):
        ...
    class Paintbox(UserDataTypeClass):
        ...
    class PaintboxStartup(GlobalUtilityPlugin):
        ...
    class PainterInterface(ReferenceTarget):
        ADDITIVEMODE: bool
        BUILDVNORMALS: bool
        DRAWNORMAL: bool
        DRAWRING: bool
        DRAWTRACE: bool
        FALLOFFGRAPH: MXSWrapperBase
        LAGRATE: int
        MARKER: float
        MARKERENABLE: bool
        MAXSIZE: float
        MAXSTR: float
        MINSIZE: float
        MINSTR: float
        MIRRORAXIS: int
        MIRRORENABLE: bool
        MIRRORGIZMOSIZE: float
        MIRROROFFSET: float
        NODES: MXSWrapperBase
        NORMALSCALE: float
        OFFMESHHITPOS: MXSWrapperBase
        OFFMESHHITTYPE: bool
        OFFMESHHITZDEPTH: float
        POINTGATHERENABLE: bool
        PREDEFINEDSIZEENABLE: bool
        PREDEFINEDSIZEGRAPH: MXSWrapperBase
        PREDEFINEDSTRENABLE: bool
        PREDEFINEDSTRGRAPH: MXSWrapperBase
        PRESSUREAFFECTS: int
        PRESSUREENABLE: bool
        QUADDEPTH: int
        SPLINECONSTRAINTNODE: None
        STRDRAGLIMITMAX: float
        STRDRAGLIMITMIN: float
        UPDATEONMOUSEUP: bool
        ...
    class PalmTrans(Matrix3Controller):
        ...
    class Panorama_Exporter(UtilityPlugin):
        ...
    class ParamBlock(MAXWrapper):
        ...
    class ParamBlock2(MAXWrapper):
        ...
    class ParamBlock2ParamBlock2(ParamBlock2):
        ...
    class ParamBlockParamBlock(ParamBlock):
        ...
    class ParamCollectorOps(Interface):
        ...
    class ParameterCollectorCA(CustAttrib):
        ...
    class ParameterEditor(GlobalUtilityPlugin):
        ...
    class ParserLoader(GlobalUtilityPlugin):
        ...
    class ParticleCache(SpacewarpModifier):
        ...
    class ParticleChannelAngAxis(ReferenceTarget):
        ...
    class ParticleChannelBindingInfo(ReferenceTarget):
        ...
    class ParticleChannelBool(ReferenceTarget):
        ...
    class ParticleChannelComplex(ReferenceTarget):
        ...
    class ParticleChannelDeleteTracker(ReferenceTarget):
        ...
    class ParticleChannelFloat(ReferenceTarget):
        ...
    class ParticleChannelID(ReferenceTarget):
        ...
    class ParticleChannelINode(ReferenceTarget):
        ...
    class ParticleChannelINodeHandle(ReferenceTarget):
        ...
    class ParticleChannelIObject(ReferenceTarget):
        ...
    class ParticleChannelInt(ReferenceTarget):
        ...
    class ParticleChannelMap(ReferenceTarget):
        ...
    class ParticleChannelMatrix3(ReferenceTarget):
        ...
    class ParticleChannelMesh(ReferenceTarget):
        ...
    class ParticleChannelMeshMap(ReferenceTarget):
        ...
    class ParticleChannelMeshVis(ReferenceTarget):
        ...
    class ParticleChannelNew(ReferenceTarget):
        ...
    class ParticleChannelPTV(ReferenceTarget):
        ...
    class ParticleChannelPair(ReferenceTarget):
        ...
    class ParticleChannelPoint3(ReferenceTarget):
        ...
    class ParticleChannelQuat(ReferenceTarget):
        ...
    class ParticleChannelSel(ReferenceTarget):
        ...
    class ParticleChannelSimulationState(ReferenceTarget):
        ...
    class ParticleChannelTabTVFace(ReferenceTarget):
        ...
    class ParticleChannelTabUVVert(ReferenceTarget):
        ...
    class ParticleChannelTest(ReferenceTarget):
        ...
    class ParticleContainer(ReferenceTarget):
        ...
    class ParticleCreatorOSM(Modifier):
        ABSOLUTE_PRECISION: float
        AFTER_HIDE: bool
        ALL_PARTICLE_FLOW_EVENTS: bool
        BEFORE_HIDE: bool
        BLEND_PARTICLES: bool
        MULTIPLY_BY_SCALE: bool
        PARTICLE_FLOW_EVENTS: MXSWrapperBase
        PARTICLE_FLOW_SYSTEMS: MXSWrapperBase
        RELATIVE_PRECISION: float
        SCALE_INFLUENCE: float
        SPLIT_PRECISION_TYPE: int
        SYNC_TYPE: int
        TIME_OFF: int
        TIME_ON: int
        TYPE: int
        USE_TIME_OFF: bool
        ZONE_SIZE: float
        ZONE_WEIGHT: float
        ...
    class ParticleGroup(GeometryClass):
        ...
    class ParticleSkinnerOSM(Modifier):
        ABSOLUTE_DISTANCE: float
        ABSOLUTE_INFLUENCE: float
        ABSOLUTE_PRECISION: float
        AFTER_HIDE: bool
        ALL_PARTICLE_FLOW_EVENTS: bool
        BEFORE_HIDE: bool
        BINDING_INFLUENCE: float
        BINDING_LIST_TYPE: int
        CONTROLLERS_LIMIT: int
        CONTROL_BY_INSIDE_INCLUSION: bool
        DATA_CHANNEL_CREATOR: None
        DISPLAY_CONTROL_PARTICLES: bool
        DISPLAY_INFLUENCE: bool
        DISPLAY_UNASSIGNED_POINTS: bool
        DISTANCE_INFLUENCE_TYPE: int
        DISTANCE_TYPE: int
        FALLOFF: float
        INTERVAL_TICKS: int
        MAP_CHANNEL: int
        MAP_CHANNEL_TYPE: int
        PARTICLE_FLOW_EVENTS: MXSWrapperBase
        PARTICLE_FLOW_SYSTEMS: MXSWrapperBase
        PHYSX_GLUE_TESTS: MXSWrapperBase
        RELATIVE_DISTANCE: float
        RELATIVE_PRECISION: float
        REMOVE_UNCONTROLLED: bool
        RIP_SURFACE_APART: int
        SIZE_INFLUENCE: float
        SPLIT_PRECISION_TYPE: int
        SUSTAIN_TOPOLOGY: bool
        TIME_OFF: int
        TIME_ON: int
        USE_DATA_CHANNEL: bool
        USE_TIME_OFF: bool
        USE_VISIBILITY_DATA_CHANNEL: bool
        VISIBILITY_DATA_CREATOR: None
        ...
    class ParticleView(Helper):
        ...
    class Particle_Age(TextureMap):
        AGE1: float
        AGE2: float
        AGE3: float
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COLOR3: MXSWrapperBase
        MAP1: None
        MAP1ENABLED: bool
        MAP2: None
        MAP2ENABLED: bool
        MAP3: None
        MAP3ENABLED: bool
        OUTPUT: MXSWrapperBase
        ...
    class Particle_Bitmap(TextureMap):
        ...
    class Particle_Cache(SpacewarpModifier):
        ...
    class Particle_Face_Creator(Modifier):
        ABSOLUTE_PRECISION: float
        AFTER_HIDE: bool
        ALL_PARTICLE_FLOW_EVENTS: bool
        BEFORE_HIDE: bool
        BLEND_PARTICLES: bool
        MULTIPLY_BY_SCALE: bool
        PARTICLE_FLOW_EVENTS: MXSWrapperBase
        PARTICLE_FLOW_SYSTEMS: MXSWrapperBase
        RELATIVE_PRECISION: float
        SCALE_INFLUENCE: float
        SPLIT_PRECISION_TYPE: int
        SYNC_TYPE: int
        TIME_OFF: int
        TIME_ON: int
        TYPE: int
        USE_TIME_OFF: bool
        ZONE_SIZE: float
        ZONE_WEIGHT: float
        ...
    class Particle_Flow_Global_Actions(GlobalUtilityPlugin):
        ...
    class Particle_Flow_Tools_Global_Utility(GlobalUtilityPlugin):
        ...
    class Particle_Flow_Utility(UtilityPlugin):
        ...
    class Particle_MBlur(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        SHARP: float
        ...
    class Particle_Paint(Helper):
        ACQUIRE_SUB_MATERIAL_INDEX: bool
        ADJUST_GLOBAL_TIMING: bool
        ASSIGN_TO_MAPPING_CHANNELS: MXSWrapperBase
        AUTOADJUST_CURRENT_FRAME: bool
        AUTO_SYNC_TIMING_BY_SELECTED_STROKE: bool
        DENSITY_CENTER: float
        DENSITY_SIDES: float
        DISPLAY_SIZE: float
        DISPLAY_TYPE: int
        DISTANCE: float
        DISTANCE_VARIATION: float
        DIVERGENCE_FOR_X_AXIS: float
        DIVERGENCE_FOR_Z_AXIS: float
        EDITING_ADJUST_GLOBAL_TIMING: bool
        EDITING_DURATION: int
        EDITING_START_AT: int
        EDITING_STOP_AT: int
        EDITING_STOP_TYPE: int
        GENERATE_MAPPING: bool
        GENERATE_ROTATION: bool
        ICON_SIZE: float
        INCLUDE_MASK_CHILDREN: bool
        INCLUDE_MASK_GROUP_MEMBERS: bool
        INCLUDE_SPRAY_CHILDREN: bool
        INCLUDE_SPRAY_GROUP_MEMBERS: bool
        JET_DURATION: int
        JET_START_TIME: int
        JET_START_TYPE: int
        JET_STOP_TIME: int
        JET_STOP_TYPE: int
        LATE_COLOR: MXSWrapperBase
        LOCATION_TYPE: int
        MAPPING_END_VALUE: float
        MAPPING_OFFSET_VALUE_PER_DROP: float
        MAPPING_OFFSET_VALUE_PER_SECOND: float
        MAPPING_START_VALUE: float
        MAPPING_TYPE: int
        MASKS: MXSWrapperBase
        MAXIMUM_NUMBER_OF_ATTEMPTS: int
        OBJECTS_ANIMATED_SURFACE: bool
        ORIENTATION_TYPE_FOR_X_AXIS: int
        ORIENTATION_TYPE_FOR_Z_AXIS: int
        PER_JET_LIMIT: int
        PRIORITY_AXIS: int
        RANDOM_SEED: int
        RATE_DROPS_PER_JET: int
        RATE_DROPS_PER_LENGTH_UNIT: float
        RATE_DROPS_PER_SECOND: float
        RATE_TYPE: int
        REVERSE_X_AXIS: bool
        REVERSE_Z_AXIS: bool
        SELECTED_STROKES: MXSWrapperBase
        SELECTION_FILTER_TYPE: int
        SEPARATION_DISTANCE: float
        SHOW_PARTICLE_TIMING: bool
        SPRAY_AT_OBJECTS: MXSWrapperBase
        SPRAY_AT_TYPE: int
        SPRAY_RADIUS: float
        SPRAY_RADIUS_GRAPH: None
        SPRAY_RADIUS_RATE: None
        STACK_UP_FOR_SEPARATION: bool
        TIME_SCALE: float
        USE_MASK_OBJECTS: bool
        USE_RADIUS_GRAPH: bool
        USE_RATE_GRAPH: bool
        USE_SEPARATION: bool
        ...
    class Particle_Paint_Cursor(GeometryClass):
        ...
    class Particle_Skinner(Modifier):
        ABSOLUTE_DISTANCE: float
        ABSOLUTE_INFLUENCE: float
        ABSOLUTE_PRECISION: float
        AFTER_HIDE: bool
        ALL_PARTICLE_FLOW_EVENTS: bool
        BEFORE_HIDE: bool
        BINDING_INFLUENCE: float
        BINDING_LIST_TYPE: int
        CONTROLLERS_LIMIT: int
        CONTROL_BY_INSIDE_INCLUSION: bool
        DATA_CHANNEL_CREATOR: None
        DISPLAY_CONTROL_PARTICLES: bool
        DISPLAY_INFLUENCE: bool
        DISPLAY_UNASSIGNED_POINTS: bool
        DISTANCE_INFLUENCE_TYPE: int
        DISTANCE_TYPE: int
        FALLOFF: float
        INTERVAL_TICKS: int
        MAP_CHANNEL: int
        MAP_CHANNEL_TYPE: int
        PARTICLE_FLOW_EVENTS: MXSWrapperBase
        PARTICLE_FLOW_SYSTEMS: MXSWrapperBase
        PHYSX_GLUE_TESTS: MXSWrapperBase
        RELATIVE_DISTANCE: float
        RELATIVE_PRECISION: float
        REMOVE_UNCONTROLLED: bool
        RIP_SURFACE_APART: int
        SIZE_INFLUENCE: float
        SPLIT_PRECISION_TYPE: int
        SUSTAIN_TOPOLOGY: bool
        TIME_OFF: int
        TIME_ON: int
        USE_DATA_CHANNEL: bool
        USE_TIME_OFF: bool
        USE_VISIBILITY_DATA_CHANNEL: bool
        VISIBILITY_DATA_CREATOR: None
        ...
    class Particle_View(Helper):
        ...
    class Particle_View_Global_Actions(GlobalUtilityPlugin):
        ...
    class Particles(ReferenceTarget):
        APPLY_DOUBLE_FILTERING: bool
        CORE_RADIUS: float
        FIELD_OF_VISION: float
        FILTER: None
        FILTER_DATA_CHANNEL: None
        FILTER_DATA_HANDLE: int
        FOV_DIRECTION_TYPE: int
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        OUTER_RADIUS: float
        PREVALENT_DATA_CHANNEL: None
        PREVALENT_DATA_HANDLE: int
        TYPE: int
        USE_CORE_RADIUS: bool
        USE_CUSTOM_PARTICLE_WEIGHT: bool
        USE_PROXY_FILTER: bool
        USE_PROXY_PARTICLES: bool
        USE_R2: bool
        USE_R3: bool
        USE_R4: bool
        USE_V6: bool
        WEIGHT_DATA_CHANNEL: None
        WEIGHT_DATA_HANDLE: int
        ...
    class PasteSkinWeights(Modifier):
        ...
    class Paste_Skin_Weights(Modifier):
        ...
    class PatchDeform(Modifier):
        FLIP_DEFORMATION_AXIS: int
        PLANE_TO_PATCH_DEFORM: int
        ROTATION: float
        U_PERCENT: float
        U_STRETCH: float
        V_PERCENT: float
        V_STRETCH: float
        ...
    class Patch_Select(Modifier):
        ...
    class PathDeform(Modifier):
        AXIS: int
        FLIP_DEFORMATION_AXIS: int
        PATH: None
        PERCENT_ALONG_PATH: float
        ROTATION: float
        STRETCH: float
        TWIST: float
        ...
    class PathDeformSpaceWarp(SpacewarpObject):
        ...
    class PathFollowBehavior(ReferenceTarget):
        AWAREDEVIATION: float
        AWARENESS: float
        DIRECTION: int
        DISPLAYFORCE: bool
        DISPLAYTARGET: bool
        ENDACTION: int
        FORCECOLOR: MXSWrapperBase
        NAME: str
        PATH: None
        RADIUS: float
        SEED: int
        START: int
        TARGETCOLOR: MXSWrapperBase
        TARGETSCALE: float
        ...
    class PathName(Value):
        ...
    class Path_Constraint(PositionController):
        ALLOWUPSIDEDOWN: bool
        AXIS: int
        AXISFLIP: bool
        BANK: bool
        BANKAMOUNT: float
        CONSTANTVEL: bool
        FOLLOW: bool
        LOOP: bool
        PATH: None
        PERCENT: float
        RELATIVE: bool
        SMOOTHNESS: float
        WEIGHT: MXSWrapperBase
        ...
    class Path_Deform2(Modifier):
        ACROSSSHAPES: int
        ADAPTIVEUPVECTOR: bool
        ADOPTMATID: bool
        APPLY_U: bool
        APPLY_V: bool
        APPLY_W: bool
        AUTO_AMOUNT: float
        AUTO_STRETCH: bool
        AXIS: int
        BY_ELEMENT: bool
        CHANNEL: int
        DRIVINGROTSCALE: float
        DRIVINGSCALESCALE: float
        FLIP: bool
        LOOKATNODE: None
        LOOPBACK: bool
        MOVEBEFOREROTATION: bool
        PERCENT_ALONG_PATH: float
        PRESERVEFORM: bool
        ROTATION: float
        ROTATIONCURVE: MXSWrapperBase
        ROTATIONENABLE: bool
        ROUNDMATID: int
        SCALECURVE: MXSWrapperBase
        SCALEENABLE: bool
        SPLINE: None
        STRETCH: float
        TWIST: float
        UNIFORM: bool
        UPVECTOR: int
        USEPIVOTPOINT: bool
        USE_LEGACY: bool
        X_OFFSET: float
        Y_OFFSET: float
        Z_OFFSET: float
        ...
    class Path_Follow(SpacewarpObject):
        CONSTANT_SPEED: int
        ICON_SIZE: float
        RANGE_LIMITED: int
        RANGE_VALUE: float
        SPIRAL_CHAOS: float
        SPIRAL_CHAOS_VAR: float
        SPIRAL_DIR: int
        SPLINE_FOLLOW_TYPE: int
        START_TIME: MXSWrapperBase
        STOP_TIME: MXSWrapperBase
        TANGENT_CHAOS: float
        TANGENT_DIR: int
        TANG_CHAOS_VAR: float
        TRAVEL_TIME: MXSWrapperBase
        TRAVEL_VAR: float
        ...
    class Path_FollowMod(SpacewarpModifier):
        ...
    class Path_Follow_Behavior(ReferenceTarget):
        AWAREDEVIATION: float
        AWARENESS: float
        DIRECTION: int
        DISPLAYFORCE: bool
        DISPLAYTARGET: bool
        ENDACTION: int
        FORCECOLOR: MXSWrapperBase
        NAME: str
        PATH: None
        RADIUS: float
        SEED: int
        START: int
        TARGETCOLOR: MXSWrapperBase
        TARGETSCALE: float
        ...
    class PerezAllWeather(Interface):
        ...
    class Perlin_Marble(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COORDS: MXSWrapperBase
        LEVEL: float
        MAP1: None
        MAP1ENABLED: bool
        MAP2: None
        MAP2ENABLED: bool
        SATURATION1: float
        SATURATION2: float
        SIZE: float
        ...
    class PersistentIsolationData(ReferenceTarget):
        ...
    class PersistentNodeSet(ReferenceTarget):
        ...
    class Perspective_Match(UtilityPlugin):
        ...
    class PhilBitmap(TextureMap):
        ...
    class Phong(Shader):
        ...
    class Phong2(Shader):
        ...
    class PhysSunSky_ShaderGenerator(Interface):
        ...
    class PhysXBuoyancy(Helper):
        ANGULAR_DRAG: float
        COLOR_COORDINATED: bool
        DENSITY: float
        GRID_GEOMETRY: None
        ICON_HEIGHT: float
        ICON_LENGTH: float
        ICON_SHAPE: int
        ICON_WIDTH: float
        LEVEL_HEIGHT: float
        LEVEL_TYPE: int
        LIMIT_BUOYANCY_BY_ICON: bool
        LINEAR_DRAG: float
        QUADRATIC_DRAG: float
        SURFACE_UNIT: float
        USE_ANGULAR_DRAG: bool
        USE_LINEAR_DRAG: bool
        USE_QUADRATIC_DRAG: bool
        ...
    class PhysXCollision(Helper):
        ADDITIVE_COUNT: bool
        COLLISION_COUNT: int
        COLLISION_GROUP: int
        DEFLECTORS: MXSWrapperBase
        MAX_SPEED: float
        MIN_SPEED: float
        REPORT_TO_DATA_OPERATOR: bool
        TEST_TRUE: bool
        TEST_TYPE: int
        ...
    class PhysXDrag(Helper):
        ANGULAR_DAMPING: float
        ANGULAR_DAMPING_DATA_CREATOR: None
        ANGULAR_DAMPING_FROM_DATA: bool
        APPLY_ANGULAR_DAMPING: bool
        APPLY_LINEAR_DAMPING: bool
        LINEAR_DAMPING: float
        LINEAR_DAMPING_DATA_CREATOR: None
        LINEAR_DAMPING_FROM_DATA: bool
        SPEED_MULTIPLIER: bool
        SPEED_UNIT: float
        SPIN_UNIT: float
        SYNC: int
        TIMING_TYPE: int
        USE_DATA_WIRING: bool
        ...
    class PhysXFlow(ReferenceTarget):
        ...
    class PhysXForce(Helper):
        EXPONENT: int
        FORCE_OVERLAPPING: int
        FORCE_SPACE_WARPS: MXSWrapperBase
        FORCE_TYPE: int
        FORCE_VARIATION_THRESHOLD: bool
        IMPULSE_ON_EVENT_ENTRY: bool
        INFLUENCE: float
        SHAPE_SIZE: float
        SYNC: int
        TIME_WARP: int
        USE_SCRIPT_FLOAT: int
        ...
    class PhysXGlue(Helper):
        ADJUST_BY_PARTICLE_MASS: bool
        ALIGN_MARGIN: float
        ALLOW_BINDING_PENETRATION: bool
        AVERAGE_BINDING_LENGTH_DATA_CREATOR: None
        AVERAGE_BINDING_LENGTH_TO_DATA: bool
        AVERAGE_BREAKING_IMPULSE_DATA_CREATOR: None
        AVERAGE_BREAKING_IMPULSE_TO_DATA: bool
        BINDING_GROUPS_DATA_CREATOR: None
        BINDING_GROUPS_FROM_DATA: bool
        BIND_CENTER_ALIGNED_ONLY: bool
        BIND_DISTANCE: float
        BIND_DISTANCE_DATA_CREATOR: None
        BIND_DISTANCE_FROM_DATA: bool
        BIND_GAP: float
        BIND_GAP_DATA_CREATOR: None
        BIND_GAP_FROM_DATA: bool
        BIND_IN_CURRENT_EVENT: bool
        BIND_WITH_DEFLECTORS: bool
        BIND_WITH_GROUND: bool
        BIND_WITH_OTHER_EVENTS: bool
        BREAKABILITY_MAX_FORCE_DATA_CREATOR: None
        BREAKABILITY_MAX_FORCE_FROM_DATA: bool
        BREAKABILITY_MAX_TORQUE_DATA_CREATOR: None
        BREAKABILITY_MAX_TORQUE_FROM_DATA: bool
        BREAKABLE_BY_FORCE: bool
        BREAKABLE_BY_OVERSTRETCH: bool
        BURY_BINDING_ANCHORS: bool
        COLOR: MXSWrapperBase
        CONTINUOUS_ADJUSTMENT: bool
        DAMPER_COEF: float
        DEFLECTORS_TO_BIND_WITH: MXSWrapperBase
        DEPTH: float
        DISTANCE_UNIT: float
        ENABLE_SPRING_FORCE: bool
        EVENTS_TO_BIND_WITH: MXSWrapperBase
        MAXIMUM_ABSOLUTE_DISTANCE: float
        MAXIMUM_BINDING_LENGTH_DATA_CREATOR: None
        MAXIMUM_BINDING_LENGTH_TO_DATA: bool
        MAXIMUM_BREAKING_IMPULSE_DATA_CREATOR: None
        MAXIMUM_BREAKING_IMPULSE_TO_DATA: bool
        MAXIMUM_DISTANCE_LIMIT_DATA_CREATOR: None
        MAXIMUM_DISTANCE_LIMIT_FROM_DATA: bool
        MAXIMUM_DISTANCE_TYPE: int
        MAXIMUM_RELATIVE_DISTANCE: float
        MAX_BINDS_PER_PARTICLE: int
        MAX_BINDS_PER_PARTICLE_DATA_CREATOR: None
        MAX_BINDS_PER_PARTICLE_FROM_DATA: bool
        MAX_BY_BIND_DISTANCE: bool
        MAX_FORCE: float
        MAX_TORQUE: float
        MINIMUM_ABSOLUTE_DISTANCE: float
        MINIMUM_BINDING_LENGTH_DATA_CREATOR: None
        MINIMUM_BINDING_LENGTH_TO_DATA: bool
        MINIMUM_DISTANCE_LIMIT_DATA_CREATOR: None
        MINIMUM_DISTANCE_LIMIT_FROM_DATA: bool
        MINIMUM_DISTANCE_TYPE: int
        MINIMUM_RELATIVE_DISTANCE: float
        NUM_ACTIVE_BINDINGS_DATA_CREATOR: None
        NUM_ACTIVE_BINDINGS_TO_DATA: bool
        NUM_BROKEN_BINDINGS_DATA_CREATOR: None
        NUM_BROKEN_BINDINGS_TO_DATA: bool
        NUM_BROKEN_BY_FORCE_DATA_CREATOR: None
        NUM_BROKEN_BY_FORCE_TO_DATA: bool
        OVERSTRETCH_ABSOLUTE_LIMIT: float
        OVERSTRETCH_DISTANCE_LIMIT_DATA_CREATOR: None
        OVERSTRETCH_DISTANCE_LIMIT_FROM_DATA: bool
        OVERSTRETCH_RELATIVE_LIMIT: float
        OVERSTRETCH_TYPE: int
        RIGID_BINDING_ANCHOR_TYPE: int
        SIMPLIFIED_BINDING_ANCHOR_TYPE: int
        SOLVER_FACTOR: float
        SPRING_COEF: float
        SPRING_DAMPER_COEF_DATA_CREATOR: None
        SPRING_DAMPER_COEF_FROM_DATA: bool
        SPRING_FORCE_COEF_DATA_CREATOR: None
        SPRING_FORCE_COEF_FROM_DATA: bool
        SYNC: int
        TEST_TRUE: bool
        TEST_TYPE: int
        TIMING_TYPE: int
        TYPE: int
        USE_BIND_GAP_CONDITION: bool
        USE_MAXIMUM_DISTANCE_LIMIT: bool
        USE_MINIMUM_DISTANCE_LIMIT: bool
        VISUALIZE_BINDING: bool
        ...
    class PhysXInterCollision(Helper):
        ADDITIVE_COUNT: bool
        COLLISION_COUNT: int
        MAX_SPEED: float
        MIN_SPEED: float
        REPORT_TO_DATA_OPERATOR: bool
        SCOPE_TYPE: int
        SELECTED_EVENTS: MXSWrapperBase
        TEST_TYPE: int
        ...
    class PhysXModRB(Modifier):
        ANGULARDAMPING: float
        BAKED: int
        BOUNCINESS: float
        COLLIDEWITHRIGIDBODIES: bool
        COMPOSITEHIGHQUALITY: bool
        COMPOSITEMAXCONCAVITY: float
        COMPOSITEMAXVERTICES: int
        CONTACTSHELLCONTACTDISTANCE: float
        CONTACTSHELLOVERRIDEGLOBALS: bool
        CONTACTSHELLRESTDEPTH: float
        CONTINUOUSCOLLISIONDETECTION: bool
        DENSITY: float
        DYNAMICFRICTION: float
        ENABLEADVANCEDSETTINGS: int
        ENABLEBACKFACECOLLISION: bool
        ENABLEGRAVITY: bool
        ENABLESOLIDMESHES: bool
        EXTRASHAPES: None
        FORCESLIST: MXSWrapperBase
        INITIALMOTIONSTYLE: int
        INITIALSPINX: float
        INITIALSPINY: float
        INITIALSPINZ: float
        INITIALVELOCITYX: float
        INITIALVELOCITYY: float
        INITIALVELOCITYZ: float
        LINEARDAMPING: float
        MANUALSETUP: bool
        MASS: float
        MASSCENTERMODE: int
        MASSCENTERX: float
        MASSCENTERY: float
        MASSCENTERZ: float
        MATERIALID: int
        MESHCONVEXSTYLE: int
        MESHCUSTOMMESH: None
        MESHHEIGHT: float
        MESHINFLATION: float
        MESHLENGTH: float
        MESHOVERRIDEMATERIAL: bool
        MESHRADIUS: float
        MESHTYPE: int
        MESHVERTICESLIMIT: int
        MESHWIDTH: float
        SHOWPHYSICALMESH: bool
        SLEEPATSTART: bool
        SMALLCLUSTERTHRESHOLD: float
        SOLVERITER: bool
        SOLVERITERVALUE: int
        SPINSPEED: float
        STATICFRICTION: float
        SWITCHTYPE: bool
        SWITCHTYPEATFRAME: int
        TYPE: int
        VELOCITYSPEED: float
        VOLUME: float
        ...
    class PhysXPanel(ReferenceTarget):
        BODYANGULARVEL: bool
        BODYAXIS: bool
        BODYLINEARVEL: bool
        BOUNCEMINSPEEDAUTOMATIC: int
        BOUNCEMINSPEEDTHRESHOLD: float
        CCDEPSILON: float
        CCDMINSPEEDAUTOMATIC: int
        CCDMINSPEEDTHRESHOLD: float
        COLLISIONCOMPOUNDS: bool
        COLLISIONSHAPES: bool
        COLLISIONSPHERES: bool
        CONTACTFORCE: bool
        CONTACTNORMAL: bool
        CONTACTPOINTS: bool
        CONTACTSHELLCONTACTDISTANCE: float
        CONTACTSHELLLEGACYMODE: bool
        DESTRUCTIONDAMAGE: float
        DESTRUCTIONMOMENTUM: float
        DESTRUCTIONRADIUS: float
        DYNAMICFRICTIONSCALE: float
        ENABLECCD: bool
        ENABLEGRAVITY: bool
        EXPORTERMODE: int
        GEOMETRYSCALE: float
        GRAVITY: float
        GRAVITYDIRECTION: int
        GRAVITYMODE: int
        GRAVITYOBJECT: None
        GROUNDHEIGHT: float
        JOINTLIMITS: bool
        JOINTLOCALAXIS: bool
        JOINTWORLDAXIS: bool
        LOOPANIMATION: int
        MAXANGLEVELOCITY: float
        ONLASTFRAME: int
        PHYSICALMESHES: int
        PLUGINBUILD: str
        PLUGINPROPERTYVERSION: int
        RESTOREORIGINALPOSE: bool
        SHAPEPERELEMENT: bool
        SKINWIDTH: float
        SLEEPENERGY: float
        SLEEPSPEED: float
        SLEEPSPIN: float
        SLEEPTHRESHOLDSAUTOMATIC: int
        SOLVERITERATION: int
        STATICFRICTIONSCALE: float
        SUBSTEPS: int
        UNITSCALE: float
        UNITTYPE: int
        USEADAPTIVEFORCE: bool
        USEFIRST: bool
        USEGROUNDPLANE: bool
        USEHARDWARESCENE: bool
        USEMULTITHREAD: bool
        VISUALIZERENABLE: bool
        VISUALIZERSCALE: float
        ...
    class PhysXPanelGUP(GlobalUtilityPlugin):
        ...
    class PhysXPanelGlobalUtilityPlugin(GlobalUtilityPlugin):
        ...
    class PhysXPanelInterface(Interface):
        ...
    class PhysXPanelReferenceTarget(ReferenceTarget):
        BODYANGULARVEL: bool
        BODYAXIS: bool
        BODYLINEARVEL: bool
        BOUNCEMINSPEEDAUTOMATIC: int
        BOUNCEMINSPEEDTHRESHOLD: float
        CCDEPSILON: float
        CCDMINSPEEDAUTOMATIC: int
        CCDMINSPEEDTHRESHOLD: float
        COLLISIONCOMPOUNDS: bool
        COLLISIONSHAPES: bool
        COLLISIONSPHERES: bool
        CONTACTFORCE: bool
        CONTACTNORMAL: bool
        CONTACTPOINTS: bool
        CONTACTSHELLCONTACTDISTANCE: float
        CONTACTSHELLLEGACYMODE: bool
        DESTRUCTIONDAMAGE: float
        DESTRUCTIONMOMENTUM: float
        DESTRUCTIONRADIUS: float
        DYNAMICFRICTIONSCALE: float
        ENABLECCD: bool
        ENABLEGRAVITY: bool
        EXPORTERMODE: int
        GEOMETRYSCALE: float
        GRAVITY: float
        GRAVITYDIRECTION: int
        GRAVITYMODE: int
        GRAVITYOBJECT: None
        GROUNDHEIGHT: float
        JOINTLIMITS: bool
        JOINTLOCALAXIS: bool
        JOINTWORLDAXIS: bool
        LOOPANIMATION: int
        MAXANGLEVELOCITY: float
        ONLASTFRAME: int
        PHYSICALMESHES: int
        PLUGINBUILD: str
        PLUGINPROPERTYVERSION: int
        RESTOREORIGINALPOSE: bool
        SHAPEPERELEMENT: bool
        SKINWIDTH: float
        SLEEPENERGY: float
        SLEEPSPEED: float
        SLEEPSPIN: float
        SLEEPTHRESHOLDSAUTOMATIC: int
        SOLVERITERATION: int
        STATICFRICTIONSCALE: float
        SUBSTEPS: int
        UNITSCALE: float
        UNITTYPE: int
        USEADAPTIVEFORCE: bool
        USEFIRST: bool
        USEGROUNDPLANE: bool
        USEHARDWARESCENE: bool
        USEMULTITHREAD: bool
        VISUALIZERENABLE: bool
        VISUALIZERSCALE: float
        ...
    class PhysXShape(Helper):
        COLLIDE_TYPE: int
        COLLISION_GROUP: int
        COLOR: MXSWrapperBase
        CONFORM_TO_PARTICLE_SHAPE: bool
        DENSITY: float
        DISPLAY_TYPE: int
        DYNAMIC_FRICTION: float
        GENERATE_TOLERANCE_CHANNEL: bool
        INFLATE_WIDTH: float
        INTERPENETRATION_TOLERANCE: float
        MASS: float
        MASS_TYPE: int
        RESTITUTION: float
        SCALE: MXSWrapperBase
        SCALE_MARGIN: float
        SCALE_TYPE: int
        SHAPE_HEIGHT: float
        SHAPE_LENGTH: float
        SHAPE_WIDTH: float
        STATIC_FRICTION: float
        WELD_THRESHOLD: float
        ...
    class PhysXShapeConvex(GeometryClass):
        ...
    class PhysXShapeWSM(SpacewarpModifier):
        ACTIVE: bool
        DYNAMIC_FRICTION: float
        NORMAL_OFFSET: float
        PLACEMENT_EDGES: bool
        PLACEMENT_POLYGONS: bool
        PLACEMENT_VERTICES: bool
        PRIMITIVE_SIZE_TYPE: int
        RESTITUTION: float
        SELECTED_ONLY: bool
        SHAPE: int
        SIDE_OVERLAP: float
        SMOOTH_SURFACE: bool
        STATIC_FRICTION: float
        THICKNESS: float
        VISUALIZE_COLLISION_SHAPE: bool
        ...
    class PhysXSolvent(Helper):
        COLOR_COORDINATED: bool
        DATA_CHANNEL: None
        GLUE_TESTS: MXSWrapperBase
        ICON_SHAPE: int
        ICON_SIZE: float
        LIMIT_SOLVENT_BY_DATA: bool
        LIMIT_SOLVENT_BY_ICON: bool
        LIMIT_SOLVENT_BY_LIST: bool
        LIMIT_SOLVENT_BY_TIME: bool
        MODE: int
        PARTICLES_TO_DEFLECTORS: bool
        PARTICLES_TO_GROUND: bool
        PARTICLES_TO_PARTICLES: bool
        START: int
        STOP: int
        ...
    class PhysXSwitch(Helper):
        ANTIGRAVITY_ACTIVE: bool
        ANTIGRAVITY_START: int
        ANTIGRAVITY_STOP: int
        ANTIGRAVITY_TYPE: int
        ANTI_GRAVITY_SYNC_TYPE: int
        APPLY_ANTI_GRAVITY: bool
        MATCH_POSITION: bool
        MATCH_ROTATION: bool
        MATCH_SPEED: bool
        MATCH_SPIN: bool
        POSITION_SPEED_ACTIVE: bool
        POSITION_SPEED_MATCH_TYPE: int
        POSITION_SPEED_START: int
        POSITION_SPEED_STOP: int
        POSITION_SPEED_SYNC_TYPE: int
        ROTATION_SPIN_ACTIVE: bool
        ROTATION_SPIN_MATCH_TYPE: int
        ROTATION_SPIN_START: int
        ROTATION_SPIN_STOP: int
        ROTATION_SPIN_SYNC_TYPE: int
        SPEED_LIMIT: float
        SPIN_LIMIT: float
        TURN_OFF_ACTIVE: bool
        TURN_OFF_SIMULATION: bool
        TURN_OFF_SIMULATION_TYPE: int
        TURN_OFF_START: int
        TURN_OFF_STOP: int
        TURN_OFF_SYNC_TYPE: int
        USE_SPEED_LIMIT: bool
        USE_SPIN_LIMIT: bool
        ...
    class PhysXWorld(Helper):
        APPLY_GRAVITY: bool
        BOUNCE_THRESHOLD: float
        CALCULATION_LIMIT: int
        COLLISION_GROUP: int
        DEFAULT_DYNAMIC_FRICTION: float
        DEFAULT_RESTITUTION: float
        DEFAULT_STATIC_FRICTION: float
        ENABLE_MULTI_THREADING: bool
        ENERGY_THRESHOLD: float
        GRAVITY_ACCELERATION: float
        GROUND_COLLISION_PLANE: bool
        HIDE_ICON: bool
        HIDE_PARTICLE_BINDINGS: bool
        ICON_HEIGHT: float
        ICON_LENGTH: float
        ICON_WIDTH: float
        RANGE_FINISH: int
        RANGE_START: int
        RANGE_TYPE: int
        RESTRICTED_BROADPHASE: bool
        RUN_BAKED_SIMULATION: bool
        SAFE_MODE_SIMULATION: bool
        SET_WORLD_LIMITS: bool
        SHOW_BAKE_DIALOG: int
        SLEEP_THRESHOLD_TYPE: int
        SPEED_THRESHOLD: float
        SPIN_RATE_THRESHOLD: float
        SUBFRAME_FACTOR: int
        SUBFRAME_TYPE: int
        THREAD_COUNT: int
        TIME_SCALE: float
        UPDATE_VIEWPORTS: bool
        USE_HARDWARE_PPU: bool
        USE_TIME_SCALE: bool
        ...
    class PhysX_Debug_Visualizer(UtilityPlugin):
        ...
    class PhysX_Shape_Convex(GeometryClass):
        ...
    class PhysX_World(Helper):
        PHYSX_DRIVER_TYPE: int
        PHYSX_WORLD_DRIVER: None
        SUPPRESS_EXPRESS_SAVE: bool
        ...
    class PhysX_And_APEX_Exporter(ExporterPlugin):
        ...
    class Physical(Camera):
        AUTO_VERTICAL_TILT_CORRECTION: bool
        BOKEH_ANISOTROPY: float
        BOKEH_BLADES_NUMBER: int
        BOKEH_CENTER_BIAS: float
        BOKEH_OPTICAL_VIGNETTING: float
        BOKEH_SHAPE: int
        BOKEH_TEXTURE: None
        BOKEH_TEXTURE_AFFECT_EXPOSURE: bool
        CLIP_FAR: float
        CLIP_NEAR: float
        CLIP_ON: bool
        DISTORTION_CUBIC_AMOUNT: float
        DISTORTION_TEXTURE: None
        DISTORTION_TYPE: int
        ENVIRONMENT_FAR: float
        ENVIRONMENT_NEAR: float
        EXPOSURE_GAIN_TYPE: int
        EXPOSURE_VALUE: float
        FILM_PRESET: str
        FILM_WIDTH_MM: float
        FOCAL_LENGTH_MM: float
        FOCUS_DISTANCE: float
        FOV: float
        F_NUMBER: float
        HORIZONTAL_SHIFT: float
        HORIZONTAL_TILT_CORRECTION: float
        HORIZON_ON: bool
        ISO: float
        LENS_BREATHING_AMOUNT: float
        MOTION_BLUR_ENABLED: bool
        PB_BOKEH_BLADES_ROTATION_DEGREES: float
        SHOW_CAMERA_CONE: int
        SHOW_FOCUS_PLANE_IN_CAM_VIEW: bool
        SHUTTER_LENGTH_FRAMES: float
        SHUTTER_LENGTH_SECONDS: float
        SHUTTER_OFFSET_ENABLED: bool
        SHUTTER_OFFSET_FRAMES: float
        SHUTTER_OFFSET_SECONDS: float
        SHUTTER_UNIT_TYPE: int
        SPECIFY_FOCUS: int
        SPECIFY_FOV: bool
        TARGETED: bool
        TARGET_DISTANCE: float
        USE_DOF: bool
        VERTICAL_SHIFT: float
        VERTICAL_TILT_CORRECTION: float
        VIGNETTING_AMOUNT: float
        VIGNETTING_ENABLED: bool
        WHITE_BALANCE_CUSTOM: MXSWrapperBase
        WHITE_BALANCE_ILLUMINANT: int
        WHITE_BALANCE_KELVIN: float
        WHITE_BALANCE_TYPE: int
        ZOOM_FACTOR: float
        ...
    class PhysicalMaterial(Material):
        ANISOANGLE: float
        ANISOTROPY: float
        ANISOTROPY_MAP: None
        ANISOTROPY_MAP_ON: bool
        ANISO_ANGLE_MAP: None
        ANISO_ANGLE_MAP_ON: bool
        ANISO_CHANNEL: int
        ANISO_MODE: int
        BASE_COLOR: MXSWrapperBase
        BASE_COLOR_MAP: None
        BASE_COLOR_MAP_ON: bool
        BASE_WEIGHT: float
        BASE_WEIGHT_MAP: None
        BASE_WEIGHT_MAP_ON: bool
        BRDF_CURVE: float
        BRDF_HIGH: float
        BRDF_LOW: float
        BRDF_MODE: bool
        BUMP_MAP: None
        BUMP_MAP_AMT: float
        BUMP_MAP_ON: bool
        CLEARCOAT_BUMP_MAP_AMT: float
        COATING: float
        COAT_AFFECT_COLOR: float
        COAT_AFFECT_ROUGHNESS: float
        COAT_BUMP_MAP: None
        COAT_BUMP_MAP_ON: bool
        COAT_COLOR: MXSWrapperBase
        COAT_COLOR_MAP: None
        COAT_COLOR_MAP_ON: bool
        COAT_IOR: float
        COAT_MAP: None
        COAT_MAP_ON: bool
        COAT_ROUGHNESS: float
        COAT_ROUGHNESS_INV: bool
        COAT_ROUGH_MAP: None
        COAT_ROUGH_MAP_ON: bool
        CUTOUT_MAP: None
        CUTOUT_MAP_ON: bool
        DIFF_ROUGHNESS: float
        DIFF_ROUGH_MAP: None
        DIFF_ROUGH_MAP_ON: bool
        DISPLACEMENT_MAP: None
        DISPLACEMENT_MAP_AMT: float
        DISPLACEMENT_MAP_ON: bool
        EMISSION: float
        EMISSION_MAP: None
        EMISSION_MAP_ON: bool
        EMIT_COLOR: MXSWrapperBase
        EMIT_COLOR_MAP: None
        EMIT_COLOR_MAP_ON: bool
        EMIT_KELVIN: float
        EMIT_LUMINANCE: float
        MATERIAL_MODE: int
        METALNESS: float
        METALNESS_MAP: None
        METALNESS_MAP_ON: bool
        REFLECTIVITY: float
        REFLECTIVITY_MAP: None
        REFLECTIVITY_MAP_ON: bool
        REFL_COLOR: MXSWrapperBase
        REFL_COLOR_MAP: None
        REFL_COLOR_MAP_ON: bool
        ROUGHNESS: float
        ROUGHNESS_INV: bool
        ROUGHNESS_MAP: None
        ROUGHNESS_MAP_ON: bool
        SCATTERING: float
        SCATTERING_MAP: None
        SCATTERING_MAP_ON: bool
        SSS_COLOR: MXSWrapperBase
        SSS_COLOR_MAP: None
        SSS_COLOR_MAP_ON: bool
        SSS_DEPTH: float
        SSS_SCALE: float
        SSS_SCALE_MAP: None
        SSS_SCALE_MAP_ON: bool
        SSS_SCATTER_COLOR: MXSWrapperBase
        THIN_WALLED: bool
        TRANSPARENCY: float
        TRANSPARENCY_MAP: None
        TRANSPARENCY_MAP_ON: bool
        TRANS_COLOR: MXSWrapperBase
        TRANS_COLOR_MAP: None
        TRANS_COLOR_MAP_ON: bool
        TRANS_DEPTH: float
        TRANS_IOR: float
        TRANS_IOR_MAP: None
        TRANS_IOR_MAP_ON: bool
        TRANS_ROUGHNESS: float
        TRANS_ROUGHNESS_INV: bool
        TRANS_ROUGHNESS_LOCK: bool
        TRANS_ROUGH_MAP: None
        TRANS_ROUGH_MAP_ON: bool
        ...
    class PhysicalMaterialManager(GlobalUtilityPlugin):
        ...
    class PhysicalSunSkyEnv(TextureMap):
        GLOBAL_INTENSITY: float
        GROUND_COLOR: MXSWrapperBase
        HAZE: float
        HORIZON_BLUR_DEG: float
        HORIZON_HEIGHT_DEG: float
        ILLUMINANCE_MODEL: int
        NIGHT_COLOR: MXSWrapperBase
        NIGHT_INTENSITY: float
        PEREZ_DIFFUSE_HORIZONTAL_ILLUMINANCE: float
        PEREZ_DIRECT_NORMAL_ILLUMINANCE: float
        SATURATION: float
        SKY_INTENSITY: float
        SUN_DISC_INTENSITY: float
        SUN_DISC_SCALE: float
        SUN_DISC_SCALE_PERCENT: float
        SUN_ENABLED: bool
        SUN_GLOW_INTENSITY: float
        SUN_POSITION_OBJECT: None
        TINT: MXSWrapperBase
        ...
    class Physical_Camera(Camera):
        AUTO_VERTICAL_TILT_CORRECTION: bool
        BOKEH_ANISOTROPY: float
        BOKEH_BLADES_NUMBER: int
        BOKEH_CENTER_BIAS: float
        BOKEH_OPTICAL_VIGNETTING: float
        BOKEH_SHAPE: int
        BOKEH_TEXTURE: None
        BOKEH_TEXTURE_AFFECT_EXPOSURE: bool
        CLIP_FAR: float
        CLIP_NEAR: float
        CLIP_ON: bool
        DISTORTION_CUBIC_AMOUNT: float
        DISTORTION_TEXTURE: None
        DISTORTION_TYPE: int
        ENVIRONMENT_FAR: float
        ENVIRONMENT_NEAR: float
        EXPOSURE_GAIN_TYPE: int
        EXPOSURE_VALUE: float
        FILM_PRESET: str
        FILM_WIDTH_MM: float
        FOCAL_LENGTH_MM: float
        FOCUS_DISTANCE: float
        FOV: float
        F_NUMBER: float
        HORIZONTAL_SHIFT: float
        HORIZONTAL_TILT_CORRECTION: float
        HORIZON_ON: bool
        ISO: float
        LENS_BREATHING_AMOUNT: float
        MOTION_BLUR_ENABLED: bool
        PB_BOKEH_BLADES_ROTATION_DEGREES: float
        SHOW_CAMERA_CONE: int
        SHOW_FOCUS_PLANE_IN_CAM_VIEW: bool
        SHUTTER_LENGTH_FRAMES: float
        SHUTTER_LENGTH_SECONDS: float
        SHUTTER_OFFSET_ENABLED: bool
        SHUTTER_OFFSET_FRAMES: float
        SHUTTER_OFFSET_SECONDS: float
        SHUTTER_UNIT_TYPE: int
        SPECIFY_FOCUS: int
        SPECIFY_FOV: bool
        TARGETED: bool
        TARGET_DISTANCE: float
        USE_DOF: bool
        VERTICAL_SHIFT: float
        VERTICAL_TILT_CORRECTION: float
        VIGNETTING_AMOUNT: float
        VIGNETTING_ENABLED: bool
        WHITE_BALANCE_CUSTOM: MXSWrapperBase
        WHITE_BALANCE_ILLUMINANT: int
        WHITE_BALANCE_KELVIN: float
        WHITE_BALANCE_TYPE: int
        ZOOM_FACTOR: float
        ...
    class Physical_Camera_Exposure_Control(ToneOperator):
        ACTIVE: bool
        EV_COMPENSATION: float
        GLOBAL_EV: float
        HIGHLIGHTS: float
        MIDTONES: float
        PHYSICAL_SCALE: float
        PHYSICAL_SCALE_MODE: int
        PROCESSBG: bool
        SATURATION: float
        SHADOWS: float
        USE_GLOBAL_EV: int
        USE_PHYSICAL_CAMERA_CONTROLS: bool
        VIGNETTING_AMOUNT: float
        VIGNETTING_ENABLED: bool
        WHITE_BALANCE_CUSTOM: MXSWrapperBase
        WHITE_BALANCE_ILLUMINANT: int
        WHITE_BALANCE_ILLUMINANT_COLORPREVIEW: MXSWrapperBase
        WHITE_BALANCE_KELVIN: float
        WHITE_BALANCE_KELVIN_COLORPREVIEW: MXSWrapperBase
        WHITE_BALANCE_TYPE: int
        ...
    class Physical_Material(Material):
        ANISOANGLE: float
        ANISOTROPY: float
        ANISOTROPY_MAP: None
        ANISOTROPY_MAP_ON: bool
        ANISO_ANGLE_MAP: None
        ANISO_ANGLE_MAP_ON: bool
        ANISO_CHANNEL: int
        ANISO_MODE: int
        BASE_COLOR: MXSWrapperBase
        BASE_COLOR_MAP: None
        BASE_COLOR_MAP_ON: bool
        BASE_WEIGHT: float
        BASE_WEIGHT_MAP: None
        BASE_WEIGHT_MAP_ON: bool
        BRDF_CURVE: float
        BRDF_HIGH: float
        BRDF_LOW: float
        BRDF_MODE: bool
        BUMP_MAP: None
        BUMP_MAP_AMT: float
        BUMP_MAP_ON: bool
        CLEARCOAT_BUMP_MAP_AMT: float
        COATING: float
        COAT_AFFECT_COLOR: float
        COAT_AFFECT_ROUGHNESS: float
        COAT_BUMP_MAP: None
        COAT_BUMP_MAP_ON: bool
        COAT_COLOR: MXSWrapperBase
        COAT_COLOR_MAP: None
        COAT_COLOR_MAP_ON: bool
        COAT_IOR: float
        COAT_MAP: None
        COAT_MAP_ON: bool
        COAT_ROUGHNESS: float
        COAT_ROUGHNESS_INV: bool
        COAT_ROUGH_MAP: None
        COAT_ROUGH_MAP_ON: bool
        CUTOUT_MAP: None
        CUTOUT_MAP_ON: bool
        DIFF_ROUGHNESS: float
        DIFF_ROUGH_MAP: None
        DIFF_ROUGH_MAP_ON: bool
        DISPLACEMENT_MAP: None
        DISPLACEMENT_MAP_AMT: float
        DISPLACEMENT_MAP_ON: bool
        EMISSION: float
        EMISSION_MAP: None
        EMISSION_MAP_ON: bool
        EMIT_COLOR: MXSWrapperBase
        EMIT_COLOR_MAP: None
        EMIT_COLOR_MAP_ON: bool
        EMIT_KELVIN: float
        EMIT_LUMINANCE: float
        MATERIAL_MODE: int
        METALNESS: float
        METALNESS_MAP: None
        METALNESS_MAP_ON: bool
        REFLECTIVITY: float
        REFLECTIVITY_MAP: None
        REFLECTIVITY_MAP_ON: bool
        REFL_COLOR: MXSWrapperBase
        REFL_COLOR_MAP: None
        REFL_COLOR_MAP_ON: bool
        ROUGHNESS: float
        ROUGHNESS_INV: bool
        ROUGHNESS_MAP: None
        ROUGHNESS_MAP_ON: bool
        SCATTERING: float
        SCATTERING_MAP: None
        SCATTERING_MAP_ON: bool
        SSS_COLOR: MXSWrapperBase
        SSS_COLOR_MAP: None
        SSS_COLOR_MAP_ON: bool
        SSS_DEPTH: float
        SSS_SCALE: float
        SSS_SCALE_MAP: None
        SSS_SCALE_MAP_ON: bool
        SSS_SCATTER_COLOR: MXSWrapperBase
        THIN_WALLED: bool
        TRANSPARENCY: float
        TRANSPARENCY_MAP: None
        TRANSPARENCY_MAP_ON: bool
        TRANS_COLOR: MXSWrapperBase
        TRANS_COLOR_MAP: None
        TRANS_COLOR_MAP_ON: bool
        TRANS_DEPTH: float
        TRANS_IOR: float
        TRANS_IOR_MAP: None
        TRANS_IOR_MAP_ON: bool
        TRANS_ROUGHNESS: float
        TRANS_ROUGHNESS_INV: bool
        TRANS_ROUGHNESS_LOCK: bool
        TRANS_ROUGH_MAP: None
        TRANS_ROUGH_MAP_ON: bool
        ...
    class Physical_Sun___Sky_Environment(TextureMap):
        GLOBAL_INTENSITY: float
        GROUND_COLOR: MXSWrapperBase
        HAZE: float
        HORIZON_BLUR_DEG: float
        HORIZON_HEIGHT_DEG: float
        ILLUMINANCE_MODEL: int
        NIGHT_COLOR: MXSWrapperBase
        NIGHT_INTENSITY: float
        PEREZ_DIFFUSE_HORIZONTAL_ILLUMINANCE: float
        PEREZ_DIRECT_NORMAL_ILLUMINANCE: float
        SATURATION: float
        SKY_INTENSITY: float
        SUN_DISC_INTENSITY: float
        SUN_DISC_SCALE: float
        SUN_DISC_SCALE_PERCENT: float
        SUN_ENABLED: bool
        SUN_GLOW_INTENSITY: float
        SUN_POSITION_OBJECT: None
        TINT: MXSWrapperBase
        ...
    class Physique(Modifier):
        ...
    class PickerControl(RolloutControl):
        ...
    class Pipe(Shape):
        ...
    class PipeReferenceTarget(ReferenceTarget):
        ANGLE_CONDITIONS: MXSWrapperBase
        CONDITION_IS_RATE: bool
        DATA_TYPE: int
        FILTER: None
        FLOAT_CONDITIONS: MXSWrapperBase
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        INPUT_7: None
        INPUT_8: None
        INPUT_VALVE: None
        INTEGER_CONDITIONS: MXSWrapperBase
        INTEGER_VALVE_TYPE: int
        PERCENT_CONDITIONS: MXSWrapperBase
        TIME_CONDITIONS: MXSWrapperBase
        UNITS_PER_TYPE: int
        VALVE_TYPE: int
        VECTOR_VALVE_TYPE: int
        WORLD_UNIT_CONDITIONS: MXSWrapperBase
        ...
    class PivotPos(FloatController):
        ...
    class PivotRot(FloatController):
        ...
    class Pivoted(GeometryClass):
        DEPTH: float
        FRAME_THICKNESS: float
        GENERATE_MAPPING_COORDS: bool
        GLAZING_THICKNESS: float
        HEIGHT: float
        HORIZONTAL_FRAME_WIDTH: float
        PERCENT_OPEN: int
        RAIL_WIDTH: float
        VERTICAL_FRAME_WIDTH: float
        VERTICAL_ROTATION: bool
        WIDTH: float
        ...
    class PlacementTool(Interface):
        ...
    class Placement_Paint(Helper):
        ACQUIRE_PAINT_MAPPING: bool
        ACQUIRE_PAINT_MATERIALID: bool
        ACQUIRE_PAINT_POSITION: bool
        ACQUIRE_PAINT_ROTATION: bool
        ACQUIRE_PAINT_SELECTION: bool
        BLENDIN_ROTATION: bool
        FAR_DISTANCE: float
        NEAR_DISTANCE: float
        OBEY_QUANTITY_MULTIPLIER: bool
        ORDER_TYPE: int
        PARTICLE_PAINT_HELPER: None
        POSITION_TYPE: int
        RANDOM_SEED: int
        SELECTION_TYPE: int
        SEPARATE_STREAMS_INDEXING: bool
        SNAP_DISTANCE: float
        SNAP_IF_CLOSE: bool
        STOP_IF_COUNT_OVERFLOW: bool
        UPDATE_TYPE: int
        ...
    class PlanarCollision(ReferenceMaker):
        ...
    class Plane(GeometryClass):
        DENSITY: float
        LENGTH: float
        LENGTHSEGS: int
        MAPCOORDS: bool
        RENDERSCALE: float
        TYPEINCREATIONMETHOD: int
        TYPEINLENGTH: float
        TYPEINPOS: MXSWrapperBase
        TYPEINWIDTH: float
        WIDTH: float
        WIDTHSEGS: int
        ...
    class PlaneAngleManip(Helper):
        ANGLE: float
        DISTANCE: float
        NORMALVEC: MXSWrapperBase
        ORIGIN: MXSWrapperBase
        SIZE: float
        UPVEC: MXSWrapperBase
        ...
    class Plane_Angle(Helper):
        ANGLE: float
        DISTANCE: float
        NORMALVEC: MXSWrapperBase
        ORIGIN: MXSWrapperBase
        SIZE: float
        UPVEC: MXSWrapperBase
        ...
    class Planet(TextureMap):
        BLENDWATERLAND: bool
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COLOR3: MXSWrapperBase
        COLOR4: MXSWrapperBase
        COLOR5: MXSWrapperBase
        COLOR6: MXSWrapperBase
        COLOR7: MXSWrapperBase
        COLOR8: MXSWrapperBase
        CONTINENTSIZE: float
        COORDS: MXSWrapperBase
        ISLANDFACTOR: float
        OCEANPERCENT: float
        RANDOMSEED: int
        ...
    class Plate_Match_MAX_R2(Filter):
        ...
    class Plug_In_Manager(GlobalUtilityPlugin):
        ...
    class PluginMarkerForBox3(ReferenceTarget):
        ...
    class PluginPackageManager(Interface):
        ...
    class Point(Helper):
        AXISTRIPOD: bool
        BOX: bool
        CENTERMARKER: bool
        CONSTANTSCREENSIZE: bool
        CROSS: bool
        DRAWONTOP: bool
        SIZE: float
        ...
    class Point2(Value):
        ...
    class Point2Controller(MAXWrapper):
        ...
    class Point3Layer(Point3Controller):
        ...
    class Point3List(Point3Controller):
        AVERAGE: bool
        WEIGHT: MXSWrapperBase
        ...
    class Point3Reactor(Point3Controller):
        ...
    class Point3Spring(Point3Controller):
        EFFECTHOW: int
        FORCENODE: MXSWrapperBase
        START: int
        STEPS: int
        X_EFFECT: float
        Y_EFFECT: float
        Z_EFFECT: float
        ...
    class Point3XRefCtrl(Point3Controller):
        ...
    class Point3_Expression(Point3Controller):
        ...
    class Point3_Layer(Point3Controller):
        ...
    class Point3_Mixer_Controller(Point3Controller):
        ...
    class Point3_Motion_Capture(Point3Controller):
        ...
    class Point3_Reactor(Point3Controller):
        ...
    class Point3_Wire(Point3Controller):
        ...
    class Point3_XRef_Controller(Point3Controller):
        ...
    class Point3_XYZ(Point3Controller):
        ...
    class Point4(Value):
        ...
    class Point4Layer(Point4Controller):
        ...
    class Point4List(Point4Controller):
        AVERAGE: bool
        WEIGHT: MXSWrapperBase
        ...
    class Point4XRefCtrl(Point4Controller):
        ...
    class Point4_Layer(Point4Controller):
        ...
    class Point4_Mixer_Controller(Point4Controller):
        ...
    class Point4_Wire(Point4Controller):
        ...
    class Point4_XRef_Controller(Point4Controller):
        ...
    class Point4_XYZW(Point4Controller):
        ...
    class PointCache(Modifier):
        APPLYMESHTOSPLINE: bool
        APPLYTOWHOLEOBJECT: bool
        CLAMPGRAPH: bool
        FILECOUNT: int
        FILENAME: str
        FORCEUNCPATH: bool
        INTERPOLATIONTYPE: int
        LOADTYPE: int
        LOADTYPESLAVE: int
        PLAYBACKEND: float
        PLAYBACKFRAME: float
        PLAYBACKORTAFTER: int
        PLAYBACKORTBEFORE: int
        PLAYBACKSTART: float
        PLAYBACKTYPE: int
        PRELOADCACHE: bool
        RECORDEND: float
        RECORDSTART: float
        RELATIVEOFFSET: bool
        SAMPLERATE: float
        STRENGTH: float
        ...
    class PointCacheWSM(SpacewarpModifier):
        APPLYMESHTOSPLINE: bool
        APPLYTOWHOLEOBJECT: bool
        CLAMPGRAPH: bool
        FILECOUNT: int
        FILENAME: str
        FORCEUNCPATH: bool
        INTERPOLATIONTYPE: int
        LOADTYPE: int
        LOADTYPESLAVE: int
        PLAYBACKEND: float
        PLAYBACKFRAME: float
        PLAYBACKORTAFTER: int
        PLAYBACKORTBEFORE: int
        PLAYBACKSTART: float
        PLAYBACKTYPE: int
        PRELOADCACHE: bool
        RECORDEND: float
        RECORDSTART: float
        RELATIVEOFFSET: bool
        SAMPLERATE: float
        STRENGTH: float
        ...
    class PointCloud(GeometryClass):
        ASPIXELPOINTSIZE: float
        DISPLAYTECHNIQUE: int
        ENABLELIMITPLANES: bool
        FILENAME: str
        FIXEDLODENABLE: bool
        FIXEDLODLEVEL: int
        GLOBALENABLEVOLUMES: bool
        GLOBALINVERTVOLUMES: bool
        GRADIENTTEXMAP: MXSWrapperBase
        PERFORMANCEQUALITY: int
        POINTSIZETYPE: int
        PTSVISIBLE: MXSWrapperBase
        REALWORLDSCALEPOINTSIZE: float
        SCANFILES: MXSWrapperBase
        SHADER: None
        SINGLECOLOR: MXSWrapperBase
        VOLUMEOBJECTS: MXSWrapperBase
        VOXELSIZE: float
        ...
    class PointHelperObj(Helper):
        AXISTRIPOD: bool
        BOX: bool
        CENTERMARKER: bool
        CONSTANTSCREENSIZE: bool
        CROSS: bool
        DRAWONTOP: bool
        SIZE: float
        ...
    class PointPacket(ReferenceMaker):
        ...
    class PointSelection(Primitive):
        ...
    class Point_Cache(Modifier):
        APPLYMESHTOSPLINE: bool
        APPLYTOWHOLEOBJECT: bool
        CLAMPGRAPH: bool
        FILECOUNT: int
        FILENAME: str
        FORCEUNCPATH: bool
        INTERPOLATIONTYPE: int
        LOADTYPE: int
        LOADTYPESLAVE: int
        PLAYBACKEND: float
        PLAYBACKFRAME: float
        PLAYBACKORTAFTER: int
        PLAYBACKORTBEFORE: int
        PLAYBACKSTART: float
        PLAYBACKTYPE: int
        PRELOADCACHE: bool
        RECORDEND: float
        RECORDSTART: float
        RELATIVEOFFSET: bool
        SAMPLERATE: float
        STRENGTH: float
        ...
    class Point_CacheSpacewarpModifier(SpacewarpModifier):
        APPLYMESHTOSPLINE: bool
        APPLYTOWHOLEOBJECT: bool
        CLAMPGRAPH: bool
        FILECOUNT: int
        FILENAME: str
        FORCEUNCPATH: bool
        INTERPOLATIONTYPE: int
        LOADTYPE: int
        LOADTYPESLAVE: int
        PLAYBACKEND: float
        PLAYBACKFRAME: float
        PLAYBACKORTAFTER: int
        PLAYBACKORTBEFORE: int
        PLAYBACKSTART: float
        PLAYBACKTYPE: int
        PRELOADCACHE: bool
        RECORDEND: float
        RECORDSTART: float
        RELATIVEOFFSET: bool
        SAMPLERATE: float
        STRENGTH: float
        ...
    class Point_Curve(Shape):
        CAP_SEGMENTS: int
        RENDER_ANGLE2: float
        RENDER_ANGLE: float
        RENDER_LENGTH: float
        RENDER_SIDES: int
        RENDER_THICKNESS: float
        RENDER_THRESHOLD: float
        RENDER_WIDTH: float
        SPHERE_CAP: float
        ...
    class Point_Curveshape(Shape):
        ...
    class Point_Surf(GeometryClass):
        ...
    class Point_SurfGeometry(GeometryClass):
        ...
    class PolyBAdjustCancel(Primitive):
        ...
    class PolyBAdjustSpinner1(Primitive):
        ...
    class PolyBAdjustSpinner2(Primitive):
        ...
    class PolyBAdjustUndo(Primitive):
        ...
    class PolyBCavityMap(Primitive):
        ...
    class PolyBDensityMap(Primitive):
        ...
    class PolyBDrawNodeInit(Primitive):
        ...
    class PolyBDrawNodeReset(Primitive):
        ...
    class PolyBDustMap(Primitive):
        ...
    class PolyBGetSel(Primitive):
        ...
    class PolyBModeLoopRing(Primitive):
        ...
    class PolyBOBJEndPaint(Primitive):
        ...
    class PolyBOBJFill(Primitive):
        ...
    class PolyBOBJInterActiveUpdate(Primitive):
        ...
    class PolyBOBJPaint(Primitive):
        ...
    class PolyBOBJPaintClear(Primitive):
        ...
    class PolyBOBJPaintCommit(Primitive):
        ...
    class PolyBOBJPaintGetStrokeFromEdges(Primitive):
        ...
    class PolyBOBJPaintSetNumFillNodes(Primitive):
        ...
    class PolyBOBJPaintSetup(Primitive):
        ...
    class PolyBOBJSpacingChangeEnd(Primitive):
        ...
    class PolyBOBJSpacingChangeStart(Primitive):
        ...
    class PolyBOcclusionMap(Primitive):
        ...
    class PolyBPolyDrawBorder(Primitive):
        ...
    class PolyBPolyDrawBuild(Primitive):
        ...
    class PolyBPolyDrawConnect(Primitive):
        ...
    class PolyBPolyDrawMove(Primitive):
        ...
    class PolyBPolyDrawOptimizer(Primitive):
        ...
    class PolyBPolyDrawPolyBranch(Primitive):
        ...
    class PolyBPolyDrawPolyShapes(Primitive):
        ...
    class PolyBPolyDrawPolyStrips(Primitive):
        ...
    class PolyBPolyDrawPolySurf(Primitive):
        ...
    class PolyBPolyDrawSplines(Primitive):
        ...
    class PolyBPolyDrawSwiftLoop(Primitive):
        ...
    class PolyBPolyDrawTopo(Primitive):
        ...
    class PolyBPolyDrawTopoSetup(Primitive):
        ...
    class PolyBPolyDrawUnitTest(Primitive):
        ...
    class PolyBPolyDrawUpdateValues(Primitive):
        ...
    class PolyBPolyShift(Primitive):
        ...
    class PolyBPolyShiftReset(Primitive):
        ...
    class PolyBPolyShiftSettings(Primitive):
        ...
    class PolyBPolySplinesEnd(Primitive):
        ...
    class PolyBPolyToUV(Primitive):
        ...
    class PolyBPolyTopoEnd(Primitive):
        ...
    class PolyBSculptCancelBuffer(Primitive):
        ...
    class PolyBSculptCommitBuffer(Primitive):
        ...
    class PolyBSculptEnd(Primitive):
        ...
    class PolyBSculptRefreshNormals(Primitive):
        ...
    class PolyBSculptSettings(Primitive):
        ...
    class PolyBSculptStart(Primitive):
        ...
    class PolyBSculptValidBuffer(Primitive):
        ...
    class PolyBSelToBitmap(Primitive):
        ...
    class PolyBSetFlowSpinner(Primitive):
        ...
    class PolyBSetSel(Primitive):
        ...
    class PolyBSetSize(Primitive):
        ...
    class PolyBShiftSetup(Primitive):
        ...
    class PolyBSolveSurf(Primitive):
        ...
    class PolyBSubSurfaceMap(Primitive):
        ...
    class PolyBTextureWrap(Primitive):
        ...
    class PolyBUVGrowLoop(Primitive):
        ...
    class PolyBUVGrowRing(Primitive):
        ...
    class PolyBUVLineup(Primitive):
        ...
    class PolyBUVLoop(Primitive):
        ...
    class PolyBUVRing(Primitive):
        ...
    class PolyBUVShrinkLoop(Primitive):
        ...
    class PolyBUVSpace(Primitive):
        ...
    class PolyBUVStitch(Primitive):
        ...
    class PolyBUVToPoly(Primitive):
        ...
    class PolyBUVWTweak(Primitive):
        ...
    class PolyBUVWTweakEnd(Primitive):
        ...
    class PolyBUVWTweakSettings(Primitive):
        ...
    class PolyBUVWTweakSetup(Primitive):
        ...
    class PolyBValidObject(Primitive):
        ...
    class PolyMeshObject(GeometryClass):
        ...
    class PolyMesh_Select(Modifier):
        BYVERTEX: bool
        IGNOREBACKFACING: bool
        LOCKSOFTSEL: bool
        MATERIALID: int
        PAINTSELMODE: int
        PAINTSELSIZE: float
        PAINTSELSTRENGTH: float
        PAINTSELVALUE: float
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELBUBBLE: float
        SOFTSELEDGEDIST: int
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELUSEEDGEDISTANCE: bool
        USESOFTSELECTION: bool
        ...
    class PolyShiftSetupConformNormals(Primitive):
        ...
    class PolyToolsModeling(GlobalUtilityPlugin):
        ...
    class PolyToolsPaintDeform(GlobalUtilityPlugin):
        ...
    class PolyToolsPolyDraw(GlobalUtilityPlugin):
        ...
    class PolyToolsSelect(GlobalUtilityPlugin):
        ...
    class PolyToolsShift(GlobalUtilityPlugin):
        ...
    class PolyToolsTopology(GlobalUtilityPlugin):
        ...
    class PolyToolsUVWTweak(GlobalUtilityPlugin):
        ...
    class Poly_Select(Modifier):
        BYVERTEX: bool
        IGNOREBACKFACING: bool
        LOCKSOFTSEL: bool
        MATERIALID: int
        PAINTSELMODE: int
        PAINTSELSIZE: float
        PAINTSELSTRENGTH: float
        PAINTSELVALUE: float
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELBUBBLE: float
        SOFTSELEDGEDIST: int
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELUSEEDGEDISTANCE: bool
        USESOFTSELECTION: bool
        ...
    class Polygon_Counter(UtilityPlugin):
        ...
    class PolymorphicGeom(GeometryClass):
        ...
    class PolymorphicGeomshape(Shape):
        ...
    class PopCharacter(ReferenceTarget):
        ...
    class PopPrompt(Primitive):
        ...
    class PopQtTranslationFromFile(Primitive):
        ...
    class PopRefUtil(UtilityPlugin):
        ...
    class PopSegControl(Matrix3Controller):
        ...
    class PopSkinControl(Matrix3Controller):
        ...
    class PopSkinObject(GeometryClass):
        ...
    class Populate(FloatController):
        ...
    class PopupMenu(Primitive):
        ...
    class Portable_Network_Graphics(BitmapIO):
        ...
    class PositionLayer(PositionController):
        ...
    class PositionList(PositionController):
        AVERAGE: bool
        WEIGHT: MXSWrapperBase
        ...
    class PositionManip(Helper):
        ...
    class PositionReactor(PositionController):
        ...
    class PositionSpring(PositionController):
        EFFECTHOW: int
        FORCENODE: MXSWrapperBase
        START: int
        STEPS: int
        X_EFFECT: float
        Y_EFFECT: float
        Z_EFFECT: float
        ...
    class PositionValueManip(Helper):
        ...
    class Position_Constraint(PositionController):
        RELATIVE: bool
        WEIGHT: MXSWrapperBase
        ...
    class Position_Expression(PositionController):
        ...
    class Position_Icon(Helper):
        DISTINCT_POINTS_ONLY: bool
        INHERIT_EMITTER_MOVEMENT: bool
        LOCATION: int
        LOCK_ON_EMITTER: bool
        MULTIPLIER: float
        RANDOM_SEED: int
        SUBFRAME_SAMPLING: bool
        TOTAL_DISTINCT_POINTS: int
        ...
    class Position_Layer(PositionController):
        ...
    class Position_Manip(Helper):
        ...
    class Position_Mixer_Controller(PositionController):
        ...
    class Position_Motion_Capture(PositionController):
        ...
    class Position_Object(Helper):
        ANIMATED_SHAPE: bool
        APART_DISTANCE: float
        APART_PLACEMENT: bool
        DELETE: bool
        DENSITY_BY_EMITTER_MATERIAL: bool
        DENSITY_TYPE: int
        DISTINCT_POINTS_ONLY: bool
        EMITTER_OBJECTS: MXSWrapperBase
        INHERIT_EMITTER_MOVEMENT: bool
        LOCATION: int
        LOCK_ON_EMITTER: bool
        MATERIAL_ID: int
        MAXIMUM_NUMBER_OF_ATTEMPTS: int
        MULTIPLIER: float
        RANDOM_SEED: int
        SUBFRAME_SAMPLING: bool
        SURFACE_OFFSET_MAXIMUM: float
        SURFACE_OFFSET_MINIMUM: float
        TOTAL_DISTINCT_POINTS: int
        USE_SUB_MATERIAL: bool
        USE_SURFACE_OFFSET: bool
        VARIATION: float
        ...
    class Position_Reactor(PositionController):
        ...
    class Position_Value(Helper):
        ...
    class Position_Wire(PositionController):
        ...
    class Position_XYZ(PositionController):
        ...
    class PostSceneFragment(GraphicsFragmentPlugin):
        ...
    class PreRotate(MappedGeneric):
        ...
    class PreRotateX(MappedGeneric):
        ...
    class PreRotateY(MappedGeneric):
        ...
    class PreRotateZ(MappedGeneric):
        ...
    class PreScale(MappedGeneric):
        ...
    class PreSceneFragment(GraphicsFragmentPlugin):
        ...
    class PreTranslate(MappedGeneric):
        ...
    class Preserve(Modifier):
        APPLY_TO_WHOLE_MESH: int
        EDGE_LENGTH_WEIGHT: float
        FACE_ANGLE_WEIGHT: float
        INVERT_SELECTION: int
        ITERATIONS: int
        SELECTED_VERTS_ONLY: int
        VOLUME_WEIGHT: float
        ...
    class PresetDummyOperIcon(Helper):
        ...
    class PresetDummyOperator(Helper):
        ...
    class PresetDummyTest(Helper):
        ...
    class PresetFlow(ReferenceTarget):
        ...
    class PresetOperIcon(Helper):
        ACTIVITY_TYPE: int
        ANIMATABLE_ACTIVE: bool
        AUTO_UPDATE: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        COLOR_COORDINATED: bool
        DEFAULT_HEIGHT: int
        DEFAULT_OFFSET: int
        DEFAULT_RANGE_MAX: float
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_TYPE: int
        DEFAULT_WIDTH: int
        ENABLE_BY_SWITCH: bool
        GROUPS: MXSWrapperBase
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        ICON_TYPE: int
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_DIVIDER: int
        PDVIEW_HEIGHT: int
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_SHOW_PARAMETERS: bool
        PDVIEW_WIDTH: int
        REPEATS: int
        SELECTED_SUBOPERATORS: MXSWrapperBase
        SUBOPERATORS: MXSWrapperBase
        TIME_OFF: int
        TIME_ON: int
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        ...
    class PresetOperator(Helper):
        ACTIVITY_TYPE: int
        ANIMATABLE_ACTIVE: bool
        AUTO_UPDATE: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        COLOR_COORDINATED: bool
        DEFAULT_HEIGHT: int
        DEFAULT_OFFSET: int
        DEFAULT_RANGE_MAX: float
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_TYPE: int
        DEFAULT_WIDTH: int
        ENABLE_BY_SWITCH: bool
        GROUPS: MXSWrapperBase
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        ICON_TYPE: int
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_DIVIDER: int
        PDVIEW_HEIGHT: int
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_SHOW_PARAMETERS: bool
        PDVIEW_WIDTH: int
        REPEATS: int
        SELECTED_SUBOPERATORS: MXSWrapperBase
        SUBOPERATORS: MXSWrapperBase
        TIME_OFF: int
        TIME_ON: int
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        ...
    class PresetTest(Helper):
        ACTIVITY_TYPE: int
        ANIMATABLE_ACTIVE: bool
        AUTO_UPDATE: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        COLOR_COORDINATED: bool
        DEFAULT_HEIGHT: int
        DEFAULT_OFFSET: int
        DEFAULT_RANGE_MAX: float
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_TYPE: int
        DEFAULT_WIDTH: int
        ENABLE_BY_SWITCH: bool
        GROUPS: MXSWrapperBase
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        ICON_TYPE: int
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_DIVIDER: int
        PDVIEW_HEIGHT: int
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_SHOW_PARAMETERS: bool
        PDVIEW_WIDTH: int
        REPEATS: int
        SELECTED_SUBOPERATORS: MXSWrapperBase
        SUBOPERATORS: MXSWrapperBase
        TIME_OFF: int
        TIME_ON: int
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        ...
    class PresetTestIcon(Helper):
        ACTIVITY_TYPE: int
        ANIMATABLE_ACTIVE: bool
        AUTO_UPDATE: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        COLOR_COORDINATED: bool
        DEFAULT_HEIGHT: int
        DEFAULT_OFFSET: int
        DEFAULT_RANGE_MAX: float
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_TYPE: int
        DEFAULT_WIDTH: int
        ENABLE_BY_SWITCH: bool
        GROUPS: MXSWrapperBase
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        ICON_TYPE: int
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_DIVIDER: int
        PDVIEW_HEIGHT: int
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_SHOW_PARAMETERS: bool
        PDVIEW_WIDTH: int
        REPEATS: int
        SELECTED_SUBOPERATORS: MXSWrapperBase
        SUBOPERATORS: MXSWrapperBase
        TIME_OFF: int
        TIME_ON: int
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        ...
    class Preset_Flow(ReferenceTarget):
        ...
    class Preset_Maker(Modifier):
        ...
    class Primitive(Value):
        ...
    class Priority(ReferenceTarget):
        DELEGATES: MXSWrapperBase
        GRID: None
        INCREMENT: int
        OBJECT: None
        SHOWPRIORITIES: bool
        SHOWSTARTFRAMES: bool
        START: int
        ...
    class Prism(GeometryClass):
        HEIGHT: float
        HEIGHTSEGS: int
        MAPCOORDS: bool
        SIDE1LENGTH: float
        SIDE1SEGS: int
        SIDE2LENGTH: float
        SIDE2SEGS: int
        SIDE3LENGTH: float
        SIDE3SEGS: int
        TYPEINCREATIONMETHOD: int
        TYPEINHEIGHT: float
        TYPEINPOS: MXSWrapperBase
        TYPEINSIDE1LENGTH: float
        TYPEINSIDE2LENGTH: float
        TYPEINSIDE3LENGTH: float
        ...
    class ProBoolObj(GeometryClass):
        ...
    class ProBoolean(GeometryClass):
        ...
    class ProCutter(GeometryClass):
        ...
    class ProOptimizer(Modifier):
        CALCULATE: bool
        COMPACTFACES: bool
        INVERTSELECTION: bool
        KEEPNORMALS: bool
        KEEPUV: bool
        KEEPVC: bool
        LOCKMAT: bool
        LOCKPOINTS: bool
        LOCKUV: bool
        LOCKVC: bool
        MERGEFACES: bool
        MERGEFACESANGLE: float
        MERGEPOINTS: bool
        MERGEPOINTSTHRESHOLD: float
        NORMALMODE: int
        NORMALTHRESHOLD: float
        OPTIMIZATIONMODE: int
        PRESERVESELECTION: bool
        PREVENTFLIP: bool
        SYMMETRYMODE: int
        SYMMETRYTOLERANCE: float
        TOLERANCEUV: float
        TOLERANCEVC: int
        VERTEXCOUNT: int
        VERTEXPERCENT: float
        ...
    class ProSound(SoundClass):
        ...
    class Project_Mapping(ReferenceTarget):
        ...
    class Project_Mapping_Holder(Modifier):
        ...
    class Projection(Modifier):
        AUTOWRAPALWAYSUPDATE: bool
        AUTOWRAPTOLERANCE: float
        CLEARSELECTION: bool
        DISPLAYCAGE: bool
        DISPLAYCAGEOFFSET: bool
        DISPLAYCAGESHADED: bool
        DISPLAYTOGGLEENABLE: bool
        DISPLAYTOGGLEMODE: int
        GEOMNAMES: MXSWrapperBase
        GEOMNODEIDS: MXSWrapperBase
        GEOMNODES: MXSWrapperBase
        GEOMNODEVISIBLE: MXSWrapperBase
        IDS: MXSWrapperBase
        IGNOREBACKFACING: bool
        MAPCHANNEL: int
        MAPPROPORTIONS: MXSWrapperBase
        MATERIALID: int
        PROJECTIONTYPES: MXSWrapperBase
        PUSHPERCENT: float
        PUSHVALUE: float
        SELECTIONCHECKSELFACES: bool
        SELECTIONCHECKTYPE: int
        SELLEVELS: MXSWrapperBase
        SMOOTHGROUP: int
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELBUBBLE: float
        SOFTSELEDGEDIST: int
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELUSEEDGEDISTANCE: bool
        USESOFTSELECTION: bool
        ...
    class ProjectionHolderUVW(Modifier):
        ...
    class ProjectionIntersectorMgr(Interface):
        ...
    class ProjectionMod(Modifier):
        AUTOWRAPALWAYSUPDATE: bool
        AUTOWRAPTOLERANCE: float
        CLEARSELECTION: bool
        DISPLAYCAGE: bool
        DISPLAYCAGEOFFSET: bool
        DISPLAYCAGESHADED: bool
        DISPLAYTOGGLEENABLE: bool
        DISPLAYTOGGLEMODE: int
        GEOMNAMES: MXSWrapperBase
        GEOMNODEIDS: MXSWrapperBase
        GEOMNODES: MXSWrapperBase
        GEOMNODEVISIBLE: MXSWrapperBase
        IDS: MXSWrapperBase
        IGNOREBACKFACING: bool
        MAPCHANNEL: int
        MAPPROPORTIONS: MXSWrapperBase
        MATERIALID: int
        PROJECTIONTYPES: MXSWrapperBase
        PUSHPERCENT: float
        PUSHVALUE: float
        SELECTIONCHECKSELFACES: bool
        SELECTIONCHECKTYPE: int
        SELLEVELS: MXSWrapperBase
        SMOOTHGROUP: int
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELBUBBLE: float
        SOFTSELEDGEDIST: int
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELUSEEDGEDISTANCE: bool
        USESOFTSELECTION: bool
        ...
    class ProjectionModTypeUVW(ReferenceTarget):
        ...
    class ProjectionRenderMgr(Interface):
        ...
    class PromptForNameRollout(RolloutClass):
        ...
    class Protractor(Helper):
        ...
    class ProxSensor(Helper):
        ...
    class PseudoColorManager(Interface):
        ...
    class Pseudo_Color_Exposure_Control(ToneOperator):
        ACTIVE: bool
        AUTOMATIC: bool
        DISPLAY: int
        MAXIMUM: float
        MINIMUM: float
        PHYSICALSCALE: float
        PROCESSBG: bool
        QUANTITY: int
        SCALEFUNCTION: int
        UNITSYSTEMUSED: int
        ...
    class Publish(Modifier):
        ...
    class Push(Modifier):
        PUSH_VALUE: float
        ...
    class PushMod(SpacewarpModifier):
        ...
    class PushPrompt(Primitive):
        ...
    class PushQtTranslationFromFile(Primitive):
        ...
    class PushSpaceWarp(SpacewarpObject):
        AMPLITUDE_1: float
        AMPLITUDE_2: float
        BASIC_FORCE: float
        CONTROL_GAIN: float
        ENABLE_VARIATION: int
        FEEDBACK_ON: int
        ICON_SIZE: float
        OFF_TIME: MXSWrapperBase
        ON_TIME: MXSWrapperBase
        RANGE_ENABLE: int
        RANGE_VALUE: float
        REVERSIBLE: int
        TARGET_SPEED: float
        UNITS: int
        VARIATION_PERIOD_1: MXSWrapperBase
        VARIATION_PERIOD_2: MXSWrapperBase
        VARIATION_PHASE_1: float
        VARIATION_PHASE_2: float
        ...
    class PutDictValue(Primitive):
        ...
    class PxAddAllPhysXObjects(MAXScriptFunction):
        ...
    class PxAddApexClothingMod(MAXScriptFunction):
        ...
    class PxAddApexClothingToNodes(MAXScriptFunction):
        ...
    class PxAddApexSBClothingMod(MAXScriptFunction):
        ...
    class PxAddApexSBClothingToNodes(MAXScriptFunction):
        ...
    class PxAddD6Joint(MAXScriptFunction):
        ...
    class PxAddModifierToTrash(MAXScriptFunction):
        ...
    class PxAddSpring(MAXScriptFunction):
        ...
    class PxApexModifierPostAdded(MAXScriptFunction):
        ...
    class PxApexModifierPreAdded(MAXScriptFunction):
        ...
    class PxApexModifierPreDelete(MAXScriptFunction):
        ...
    class PxApexModsToDelete(Array):
        ...
    class PxApexModsToDeleteForce(Array):
        ...
    class PxCalcJointLimits(MAXScriptFunction):
        ...
    class PxCalculateConstraintPose(MAXScriptFunction):
        ...
    class PxCaptureTransform(MAXScriptFunction):
        ...
    class PxCheckFileVersion(MAXScriptFunction):
        ...
    class PxCheckOldVersionMenus(MAXScriptFunction):
        ...
    class PxCheckSDK3(MAXScriptFunction):
        ...
    class PxClearSavedRBKeys(MAXScriptFunction):
        ...
    class PxCloseAllUI(MAXScriptFunction):
        ...
    class PxCloseMenu(MAXScriptFunction):
        ...
    class PxClothModifierPostAdded(MAXScriptFunction):
        ...
    class PxClothModifierPreAdded(MAXScriptFunction):
        ...
    class PxClothModifierPreDelete(MAXScriptFunction):
        ...
    class PxClothNodes(MAXScriptFunction):
        ...
    class PxColorDynamicRB(Color):
        ...
    class PxColorKinematicRB(Color):
        ...
    class PxColorStaticRB(Color):
        ...
    class PxConstraintDefaultName(MAXScriptFunction):
        ...
    class PxConvertOldJoint(MAXScriptFunction):
        ...
    class PxConvertOldRB(MAXScriptFunction):
        ...
    class PxCreateAs(MAXScriptFunction):
        ...
    class PxCreateAsCloth(MAXScriptFunction):
        ...
    class PxCreateAsDynamic(MAXScriptFunction):
        ...
    class PxCreateAsKinetic(MAXScriptFunction):
        ...
    class PxCreateAsStatic(MAXScriptFunction):
        ...
    class PxCreateBox(MAXScriptFunction):
        ...
    class PxCreateCapsule(MAXScriptFunction):
        ...
    class PxCreateConstraint(MAXScriptFunction):
        ...
    class PxCreateConstraintAt(MAXScriptFunction):
        ...
    class PxCreateConstraintForNodes(MAXScriptFunction):
        ...
    class PxCreateConstrintBallSocket(MAXScriptFunction):
        ...
    class PxCreateConstrintGear(MAXScriptFunction):
        ...
    class PxCreateConstrintHinge(MAXScriptFunction):
        ...
    class PxCreateConstrintRigid(MAXScriptFunction):
        ...
    class PxCreateConstrintSlide(MAXScriptFunction):
        ...
    class PxCreateConstrintTwist(MAXScriptFunction):
        ...
    class PxCreateConstrintUniv(MAXScriptFunction):
        ...
    class PxCreateDynamicRagdoll(MAXScriptFunction):
        ...
    class PxCreateDynamicRagdollHelper(MAXScriptFunction):
        ...
    class PxCreateKinematicRagdoll(MAXScriptFunction):
        ...
    class PxCreateKinematicRagdollHelper(MAXScriptFunction):
        ...
    class PxCreatePhysXScene(MAXScriptFunction):
        ...
    class PxCreateSphere(MAXScriptFunction):
        ...
    class PxCreationPlaceAndSizeTool(MouseTool):
        ...
    class PxDeleteBrokenRBs(MAXScriptFunction):
        ...
    class PxDeleteRB(MAXScriptFunction):
        ...
    class PxDynamicRBNodes(MAXScriptFunction):
        ...
    class PxEmptyModifierTrash(MAXScriptFunction):
        ...
    class PxExistFileProperty(MAXScriptFunction):
        ...
    class PxExportFBX(MAXScriptFunction):
        ...
    class PxExportPxProj(MAXScriptFunction):
        ...
    class PxExportPxProj_Prompting(MAXScriptFunction):
        ...
    class PxExportTemplate(MAXScriptFunction):
        ...
    class PxExporterLoadLastParameters(MAXScriptFunction):
        ...
    class PxExporterSaveLastParameters(MAXScriptFunction):
        ...
    class PxFindApexGraphicalMod(MAXScriptFunction):
        ...
    class PxFindApexLODMod(MAXScriptFunction):
        ...
    class PxFindGeometryChange(MAXScriptFunction):
        ...
    class PxForceCreatePhysXScene(MAXScriptFunction):
        ...
    class PxGenerateApexClothingDebugVisualizerRollout(MAXScriptFunction):
        ...
    class PxGeneratePhysXClothingDebugVisualizerRollout(MAXScriptFunction):
        ...
    class PxGetAllChildrenNodes(MAXScriptFunction):
        ...
    class PxGetCurrentNode(MAXScriptFunction):
        ...
    class PxGetCurrentNodeType(MAXScriptFunction):
        ...
    class PxGetDisplayUnitFactor(MAXScriptFunction):
        ...
    class PxGetFileProperty(MAXScriptFunction):
        ...
    class PxGetGroupNodes(MAXScriptFunction):
        ...
    class PxGetGroupNodesCount(MAXScriptFunction):
        ...
    class PxGetIniFilename(MAXScriptFunction):
        ...
    class PxGetMeterToUnit(MAXScriptFunction):
        ...
    class PxGetModCloth(MAXScriptFunction):
        ...
    class PxGetModClothByClass(MAXScriptFunction):
        ...
    class PxGetModRB(MAXScriptFunction):
        ...
    class PxGetModRBByClass(MAXScriptFunction):
        ...
    class PxGetNodeByHandle(MAXScriptFunction):
        ...
    class PxGetNodeHandle(MAXScriptFunction):
        ...
    class PxGetNodePivot(MAXScriptFunction):
        ...
    class PxGetNodePosition(MAXScriptFunction):
        ...
    class PxGetNodeType(MAXScriptFunction):
        ...
    class PxGetNodeUserProp(MAXScriptFunction):
        ...
    class PxGetOldRagdoll(MAXScriptFunction):
        ...
    class PxGetPhysXPanelTab(MAXScriptFunction):
        ...
    class PxGetRagdollHelper(MAXScriptFunction):
        ...
    class PxGetRagdollHelperNode(MAXScriptFunction):
        ...
    class PxGetRagdollHelperRootBone(MAXScriptFunction):
        ...
    class PxGetRagdollRootBone(MAXScriptFunction):
        ...
    class PxGetRootParent(MAXScriptFunction):
        ...
    class PxGetSelectedDummyHelpers(MAXScriptFunction):
        ...
    class PxGetSelectedDummyHelpersCount(MAXScriptFunction):
        ...
    class PxGetSelectedHelpers(MAXScriptFunction):
        ...
    class PxGetSelectedHelpersCount(MAXScriptFunction):
        ...
    class PxGetSelectedNodes(MAXScriptFunction):
        ...
    class PxGetSelectionCount(MAXScriptFunction):
        ...
    class PxGetSimPlaybackSetting(MAXScriptFunction):
        ...
    class PxGetSingleNodes(MAXScriptFunction):
        ...
    class PxGetSystemCommandMode(MAXScriptFunction):
        ...
    class PxGrabPositions(MAXScriptFunction):
        ...
    class PxGrabRotations(MAXScriptFunction):
        ...
    class PxImportAllHelperMeshes(MAXScriptFunction):
        ...
    class PxImportMesh(MAXScriptFunction):
        ...
    class PxImportRagdollHelperMesh(MAXScriptFunction):
        ...
    class PxImportTemplate(MAXScriptFunction):
        ...
    class PxInitGlobalParamsForNewFile(MAXScriptFunction):
        ...
    class PxInitJointParams(MAXScriptFunction):
        ...
    class PxInitializePlugin(MAXScriptFunction):
        ...
    class PxIsApexGraphicalMod(MAXScriptFunction):
        ...
    class PxIsBakeable(MAXScriptFunction):
        ...
    class PxIsBakeableAtTime(MAXScriptFunction):
        ...
    class PxIsBaked(MAXScriptFunction):
        ...
    class PxIsBone(MAXScriptFunction):
        ...
    class PxIsBuildInShape(MAXScriptFunction):
        ...
    class PxIsClothMod(MAXScriptFunction):
        ...
    class PxIsClothingModifierSelected(MAXScriptFunction):
        ...
    class PxIsDynamicRB(MAXScriptFunction):
        ...
    class PxIsKinematicRB(MAXScriptFunction):
        ...
    class PxIsPhysXMod(MAXScriptFunction):
        ...
    class PxIsPhysicsObject(MAXScriptFunction):
        ...
    class PxIsRB(MAXScriptFunction):
        ...
    class PxIsRigidBody(MAXScriptFunction):
        ...
    class PxIsSimulationRunning(MAXScriptFunction):
        ...
    class PxIsStaticRB(MAXScriptFunction):
        ...
    class PxKeepGlobalParametersUnchanged(MAXScriptFunction):
        ...
    class PxKeepPhysicsValuesUnchanged(MAXScriptFunction):
        ...
    class PxKinematicRBNodes(MAXScriptFunction):
        ...
    class PxListenGeneralEvents(MAXScriptFunction):
        ...
    class PxLoadFileProperties(MAXScriptFunction):
        ...
    class PxLoadGlobalParam(MAXScriptFunction):
        ...
    class PxLoadRolloutInfoList(MAXScriptFunction):
        ...
    class PxLoadSavedPose(MAXScriptFunction):
        ...
    class PxMakeCloth(MAXScriptFunction):
        ...
    class PxMakeDynamicRB(MAXScriptFunction):
        ...
    class PxMakeKinematicRB(MAXScriptFunction):
        ...
    class PxMakeStaticRB(MAXScriptFunction):
        ...
    class PxMatHullDynamicRB(Shell_Material):
        ...
    class PxMatHullKinematicRB(Shell_Material):
        ...
    class PxMatHullStaticRB(Shell_Material):
        ...
    class PxMaxIsEditing(MAXScriptFunction):
        ...
    class PxModRBCloneHappend(MAXScriptFunction):
        ...
    class PxModRBMirrorHappened(MAXScriptFunction):
        ...
    class PxModRBPostAdded(MAXScriptFunction):
        ...
    class PxModRBPreAdded(MAXScriptFunction):
        ...
    class PxModRBPreDelete(MAXScriptFunction):
        ...
    class PxNeedSolveCompatibility(MAXScriptFunction):
        ...
    class PxNeedToBake(MAXScriptFunction):
        ...
    class PxNodeIsConvex(MAXScriptFunction):
        ...
    class PxPanelClose(MAXScriptFunction):
        ...
    class PxPanelUndo(MAXScriptFunction):
        ...
    class PxParseModRB(MAXScriptFunction):
        ...
    class PxPauseSimulation(MAXScriptFunction):
        ...
    class PxPotentialRagdoll(MAXScriptFunction):
        ...
    class PxPotentialRagdollHelper(MAXScriptFunction):
        ...
    class PxPrepareConstraintName(MAXScriptFunction):
        ...
    class PxPrintExtraShapes(MAXScriptFunction):
        ...
    class PxRBGetVolume(MAXScriptFunction):
        ...
    class PxRagFilePostOpen(MAXScriptFunction):
        ...
    class PxRagdollList(Array):
        ...
    class PxReadMaxUnit(MAXScriptFunction):
        ...
    class PxReadSystemUnit(MAXScriptFunction):
        ...
    class PxRebuildSelectedClothing(MAXScriptFunction):
        ...
    class PxRecordExistingPhysXMod(MAXScriptFunction):
        ...
    class PxRefreshD6PropertyPanels(MAXScriptFunction):
        ...
    class PxRefreshPhysXToolPanel(MAXScriptFunction):
        ...
    class PxRefreshRBPropertyPanels(MAXScriptFunction):
        ...
    class PxRemoveCloth(MAXScriptFunction):
        ...
    class PxRemoveClothMod(MAXScriptFunction):
        ...
    class PxRemoveFormerPhysXMod(MAXScriptFunction):
        ...
    class PxRemoveOldRagdoll(MAXScriptFunction):
        ...
    class PxRemovePhysXMods(MAXScriptFunction):
        ...
    class PxRemoveRagdollByNode(MAXScriptFunction):
        ...
    class PxRemoveRagdollHelper(MAXScriptFunction):
        ...
    class PxResetGlobalParams(MAXScriptFunction):
        ...
    class PxResetPhysXScene(MAXScriptFunction):
        ...
    class PxResetRBKeys(MAXScriptFunction):
        ...
    class PxRunSimulation(MAXScriptFunction):
        ...
    class PxSaveGlobalParams(MAXScriptFunction):
        ...
    class PxSaveRBKeys(MAXScriptFunction):
        ...
    class PxSaveRolloutInfoList(MAXScriptFunction):
        ...
    class PxScaleHelperSize(MAXScriptFunction):
        ...
    class PxSelectBoneDialogList(Array):
        ...
    class PxSelectBoneDialogResult(Array):
        ...
    class PxSelectBonesDialog(MAXScriptFunction):
        ...
    class PxSeletionCanCreateCloth(MAXScriptFunction):
        ...
    class PxSeletionCanCreateRB(MAXScriptFunction):
        ...
    class PxSetCCDMotionThreshold(MAXScriptFunction):
        ...
    class PxSetContactDistanceFromRestDepth(MAXScriptFunction):
        ...
    class PxSetGeometryScale(MAXScriptFunction):
        ...
    class PxSetGlobalParamsFromPhysXPanelInterface(MAXScriptFunction):
        ...
    class PxSetPhysXPanelInterfaceFromGlobalParams(MAXScriptFunction):
        ...
    class PxSetProperty(MAXScriptFunction):
        ...
    class PxSetRBHullNodeColor(MAXScriptFunction):
        ...
    class PxSetSimPlaybackSetting(MAXScriptFunction):
        ...
    class PxSetSystemCommandMode(MAXScriptFunction):
        ...
    class PxShowAbout(MAXScriptFunction):
        ...
    class PxShowExportOptions(MAXScriptFunction):
        ...
    class PxShowExportOptionsDialog(MAXScriptFunction):
        ...
    class PxShowPhysicsPanel(MAXScriptFunction):
        ...
    class PxShowPluginBuild(MAXScriptFunction):
        ...
    class PxShowViewer(MAXScriptFunction):
        ...
    class PxSimClock(MAXScriptFunction):
        ...
    class PxSimulateNFrames(MAXScriptFunction):
        ...
    class PxSimulateOneFrame(MAXScriptFunction):
        ...
    class PxSolveCompatibilityIssues(MAXScriptFunction):
        ...
    class PxStartPlugin(MAXScriptFunction):
        ...
    class PxStaticRBNodes(MAXScriptFunction):
        ...
    class PxStepSimulation(MAXScriptFunction):
        ...
    class PxStopSecond(MAXScriptFunction):
        ...
    class PxStopSimulation(MAXScriptFunction):
        ...
    class PxSwitchSDK(MAXScriptFunction):
        ...
    class PxSwitchSDKSilent(MAXScriptFunction):
        ...
    class PxSystemUnitChangeFactor(MAXScriptFunction):
        ...
    class PxUnitEnumToType(MAXScriptFunction):
        ...
    class PxUnitTypeToEnum(MAXScriptFunction):
        ...
    class PxUnitsChange(MAXScriptFunction):
        ...
    class PxUpdateGravity(MAXScriptFunction):
        ...
    class PxUpdateGroundPlane(MAXScriptFunction):
        ...
    class PxUpdateModRBMassForGeometryChange(MAXScriptFunction):
        ...
    class PxUpdatePhysXParameters(MAXScriptFunction):
        ...
    class PxUpdateRolloutInfoList(MAXScriptFunction):
        ...
    class PxUseHardwareScene(MAXScriptFunction):
        ...
    class PxUseMultiThread(MAXScriptFunction):
        ...
    class PyWrapperBase(Value):
        ...
    class Pyramid(GeometryClass):
        DEPTH: float
        DEPTHSEGS: int
        HEIGHT: float
        HEIGHTSEGS: int
        MAPCOORDS: bool
        TYPEINCREATIONMETHOD: int
        TYPEINDEPTH: float
        TYPEINHEIGHT: float
        TYPEINPOS: MXSWrapperBase
        TYPEINWIDTH: float
        WIDTH: float
        WIDTHSEGS: int
        ...
    class PyramidBitmapFilterClass(BitmapFilterClass):
        ...
    class Python3Host(UtilityPlugin):
        ...
    class QCompA(Generic):
        ...
    class QTime(BitmapIO):
        ...
    class QtUISample(Primitive):
        ...
    class QuadMesh(Modifier):
        QUADSIZE: float
        ...
    class Quadify_Mesh(Modifier):
        QUADSIZE: float
        ...
    class Quadratic(Filter):
        ...
    class QuarterRound(Shape):
        ...
    class Quat(Value):
        ...
    class Quicksilver_Hardware_Renderer(RendererClass):
        ...
    class RAMPlayer(Primitive):
        ...
    class RCMenu(Value):
        ...
    class RElements2Cws(MAXScriptFunction):
        ...
    class RGB_Multiply(TextureMap):
        ALPHAFROM: int
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1: None
        MAP1ENABLED: bool
        MAP2: None
        MAP2ENABLED: bool
        ...
    class RGB_Tint(TextureMap):
        BLUE: MXSWrapperBase
        GREEN: MXSWrapperBase
        MAP1: None
        MAP1ENABLED: bool
        RED: MXSWrapperBase
        ...
    class RLA(BitmapIO):
        ...
    class RPF(BitmapIO):
        ...
    class RadioControl(RolloutControl):
        ...
    class Radiosity(RadiosityEffect):
        CONTRASTTHRESHOLD: float
        ELAPSEDTIME: int
        INCLUDEAREALIGHTS: bool
        INCLUDELINEARLIGHTS: bool
        INCLUDEPOINTLIGHTS: bool
        INCLUDESELFEMITTINGLIGHTS: bool
        INCLUDESKYLIGHT: bool
        INITIALMESHSIZE: float
        LIGHTPAINTINGINTENSITY: float
        LIGHTPAINTINGPRESSURE: float
        LIGHTUNITSUSED: int
        MESHINGENABLED: bool
        MESHINGSIZE: float
        MINIMUMMESHSIZE: float
        MINIMUMSELFEMITTINGSIZE: float
        RADDIRECTFILTERING: int
        RADDISPLAYINVIEWPORT: bool
        RADFILTERING: int
        RADGLOBALREFINESTEPS: int
        RADINITIALQUALITY: float
        RADPROCESSINRENDERONLY: bool
        RADPROCESSOBJECTREFINESTEPS: bool
        RADSELECTIONREFINESTEPS: int
        RMADAPTIVEENABLED: bool
        RMCLAMPENABLED: bool
        RMCLAMPVALUE: float
        RMFILTERRADIUS: float
        RMMINSAMPLESPACING: int
        RMRAYSPERSAMPLE: int
        RMREGATHER: bool
        RMREUSEDIRECTILLUMINATION: bool
        RMSAMPLESPACING: int
        RMSHOWSAMPLES: bool
        RMSUBDIVISIONCONTRAST: float
        SHOOTDIRECTLIGHTS: bool
        STATMESHSIZE: float
        STATNUMFACES: int
        STATNUMGEOMOBJECTS: int
        STATNUMLIGHTOBJECTS: int
        STATREFINEITERATIONS: int
        STATSOLUTIONQUALITY: float
        USEADAPTIVEMESHING: bool
        ...
    class RadiosityEffect(MAXWrapper):
        ...
    class RadiosityPreferences(Interface):
        ...
    class Radiosity_Override(Material):
        BASEMATERIAL: MXSWrapperBase
        BUMPSCALE: float
        COLORBLEED: float
        LUMINANCESCALE: float
        REFLECTANCESCALE: float
        TRANSMITTANCESCALE: float
        ...
    class RagdollHelper(Helper):
        ...
    class RagdollVisualizer(Helper):
        ...
    class Railing(GeometryClass):
        FENCING_TYPE: int
        FILL_BOTTOM_OFFSET: float
        FILL_LEFT_OFFSET: float
        FILL_RIGHT_OFFSET: float
        FILL_THICKNESS: float
        FILL_TOP_OFFSET: float
        FIRST_PICKET_OFFSET: float
        FIRST_POST_OFFSET: float
        LAST_PICKET_SPACING_TO_POST: float
        LAST_POST_OFFSET: float
        LOWER_RAIL_DEPTH: float
        LOWER_RAIL_PROFILE: int
        LOWER_RAIL_SPACING: float
        LOWER_RAIL_WIDTH: float
        LOWEST_RAIL_HEIGHT: float
        NUMBER_OF_LOWER_RAILS: int
        NUMBER_OF_PICKETS_BETWEEN_EACH_PAIR_OF_POSTS: int
        NUMBER_OF_POSTS: int
        NUMBER_OF_SEGMENTS_BETWEEN_EACH_PAIR_OF_POSTS: int
        PICKETS_ORIENTED_WITH_CURVED_RAILING: bool
        PICKET_BOTTOM_OFFSET: float
        PICKET_DEPTH: float
        PICKET_EXTENSION_BEYOND_BOTTOM_OF_TOP_RAIL: float
        PICKET_PROFILE: int
        PICKET_SPACING: float
        PICKET_WIDTH: float
        POSTS_ORIENTED_WITH_CURVED_RAILING: bool
        POST_DEPTH: float
        POST_EXTENSION_BEYOND_BOTTOM_OF_TOP_RAIL: float
        POST_PROFILE: int
        POST_SPACING: float
        POST_WIDTH: float
        RAILING_LENGTH: float
        RESPECT_PATH_CORNERS_IN_RAILS: bool
        TEXTURE_MAPPED: bool
        TOP_RAIL_DEPTH: float
        TOP_RAIL_PROFILE: int
        TOP_RAIL_SPACING_TO_NEXT_RAIL: float
        TOP_RAIL_WIDTH: float
        TOP_SURFACE_OF_TOP_RAIL_HEIGHT: float
        ...
    class RandomWalk(Helper):
        ...
    class Randomize_Keys(TrackViewUtility):
        ...
    class RapidRT_Noise_Filter(RenderElement):
        BITMAP: bool
        ELEMENTNAME: str
        ENABLED: bool
        STRENGTH: float
        STRENGTH_PERCENTAGE: float
        ...
    class Raster_Image_Packet(ReferenceMaker):
        ...
    class Raster_Image_Translator(ReferenceMaker):
        ...
    class Ray(Value):
        ...
    class RayFX(UtilityPlugin):
        ...
    class RayFXUtil(UtilityPlugin):
        ...
    class RayMeshGridIntersect(ReferenceTarget):
        NODELIST: MXSWrapperBase
        ...
    class Ray_Element(ReferenceTarget):
        ALPHA: int
        ANGLE: float
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        APPLYLIGHTS: bool
        APPLYNOISE: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        CENTERCOLOR: MXSWrapperBase
        CIRCULARCOLORMIX: float
        CIRCULARMAP: None
        CIRCULARMTL: None
        COLORSOURCE: float
        EDGECOLOR: MXSWrapperBase
        EFFECTSID: int
        ELEMENTNAME: str
        FILTERALL: bool
        FILTERBRIGHTNESS: bool
        FILTEREDGE: bool
        FILTERHUE: bool
        FILTERPERIMETER: bool
        FILTERPERIMETERALPHA: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        INTENSITY: float
        NOISEMAP: None
        NUMBER: int
        OBJECTID: int
        OBJECTSHIDE: bool
        OCCLUSION: float
        ON: bool
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        QUADRANT4COLOR: MXSWrapperBase
        RADIALDENSITY: None
        RADIALMAP: None
        RADIALMTL: None
        RADIALSIZEMAP: None
        SHARPNESS: float
        SIZE: float
        SOURCEALPHA: bool
        SOURCEEFFECTSID: bool
        SOURCEOBJECTID: bool
        SOURCESURFACENORMAL: bool
        SOURCEUNCLAMPEDCOLOR: bool
        SOURCEWHOLE: bool
        SOURCEZBUFFER: bool
        SQUEEZE: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        USECIRCULARMAP: bool
        USECIRCULARMTL: bool
        USERADIALDENSITY: bool
        USERADIALMAP: bool
        USERADIALMTL: bool
        USERADIALSIZEMAP: bool
        ZHI: float
        ZLO: float
        ...
    class Ray_Engine(ReferenceTarget):
        ...
    class Raytrace(TextureMap):
        ...
    class RaytraceGlobalSettings(ReferenceTarget):
        ADAPTIVE_ANTIALIASING_ENABLE_FLAG: bool
        ADAPTIVE_ANTIALIASING_THRESHOLD: float
        ADAPTIVE_RAY_DEPTH_THRESHOLD: float
        ANTIALIASING_MAXIMUM_RAYS_TO_FIRE: int
        ANTIALIASING_MINIMUM_RAYS_TO_FIRE: int
        BLURRING_AMOUNT: float
        BLURRING_ASPECT_RATIO: float
        DEFOCUSING_AMOUNT: float
        DEFOCUSING_ASPECT_RATIO: float
        ENABLE_ANTIALIASING: bool
        ENABLE_ATMOSPHERE: bool
        ENABLE_ATMOSPHERE_IN_RAYTRACE_OBJECTS: bool
        ENABLE_MATERIAL_ID_RENDERING_SUPPORT: bool
        ENABLE_OBJECTS_IN_RAYTRACE_OBJECTS: bool
        ENABLE_RAYTRACING: bool
        ENABLE_REFRACT_SPECIAL_EFFECTS: bool
        ENABLE_SELF_REFLECT_REFRACT: bool
        EXCLUDELIST: MXSWrapperBase
        INCLUDELIST: None
        MAX_LEVELS_COLOR_MODE: int
        MAX_LEVELS_SPECIFY_COLOR: MXSWrapperBase
        MAX_RAY_DEPTH: int
        SHOWMESSAGES: bool
        SHOWPROGRESSDLG: bool
        VOX_DIM: int
        VOX_FACE_LIMIT: int
        VOX_MAXDEPTH: int
        VOX_PREVIS: float
        ...
    class RaytraceMaterial(Material):
        ADAPTIVE_ANTIALIASING_ON: bool
        AMBIENT: MXSWrapperBase
        AMBIENTMAP: None
        AMBIENTMAPAMOUNT: float
        AMBIENTMAPENABLE: bool
        AMBIENT_AMOUNT: float
        AMBIENT_COLOR_ON: bool
        ANISOTROPY: float
        ATTENUATION_COLOR: MXSWrapperBase
        ATTENUATION_COLOR_MODE: int
        ATTENUATION_CONTROL_1: float
        ATTENUATION_CONTROL_2: float
        ATTENUATION_EXPONENT: float
        ATTENUATION_FAR: float
        ATTENUATION_NEAR: float
        ATTENUATION_START: float
        BLUR_MAP: bool
        BOUNCE_COEFFICIENT: float
        BUMPMAP: None
        BUMPMAPAMOUNT: float
        BUMPMAPENABLE: bool
        BUMP_MAP_EFFECT: float
        COLORDENSITYMAP: None
        COLORDENSITYMAPAMOUNT: float
        COLORDENSITYMAPENABLE: bool
        COLOR_DENSITY_AMOUNT: float
        COLOR_DENSITY_COLOR: MXSWrapperBase
        COLOR_DENSITY_ENABLE: bool
        COLOR_DENSITY_END: float
        COLOR_DENSITY_START: float
        DEFOCUS_MAP: bool
        DIFFUSE: MXSWrapperBase
        DIFFUSEMAP: None
        DIFFUSEMAPAMOUNT: float
        DIFFUSEMAPENABLE: bool
        DIFFUSIONMAP: None
        DIFFUSIONMAPAMOUNT: float
        DIFFUSIONMAPENABLE: bool
        DISPLACEMENTMAP: None
        DISPLACEMENTMAPAMOUNT: float
        DISPLACEMENTMAPENABLE: bool
        EFFECTSCHANNEL: int
        ENABLE_RAYTRACED_REFLECTIONS: bool
        ENABLE_RAYTRACED_REFRACTIONS: bool
        ENABLE_REFLECTION_FALLOFF: bool
        ENABLE_REFRACTION_FALLOFF: bool
        ENVIRONMENTMAP: None
        ENVIRONMENTMAPAMOUNT: float
        ENVIRONMENTMAPENABLE: bool
        EXTRALIGHTINGMAP: None
        EXTRALIGHTINGMAPAMOUNT: float
        EXTRALIGHTINGMAPENABLE: bool
        EXTRA_LIGHTING: MXSWrapperBase
        FACEMAP: bool
        FLUORESCENCE: MXSWrapperBase
        FLUORESCENCEMAP: None
        FLUORESCENCEMAPAMOUNT: float
        FLUORESCENCEMAPENABLE: bool
        FLUORESCENCE_BIAS: float
        FOGCOLORMAP: None
        FOGCOLORMAPAMOUNT: float
        FOGCOLORMAPENABLE: bool
        FOG_AMOUNT: float
        FOG_COLOR: MXSWrapperBase
        FOG_ENABLE: bool
        FOG_END: float
        FOG_START: float
        GLOSSINESS: float
        GLOSSINESSMAP: None
        GLOSSINESSMAPAMOUNT: float
        GLOSSINESSMAPENABLE: bool
        INDEX_OF_REFRACTION: float
        IORMAP: None
        IORMAPAMOUNT: float
        IORMAPENABLE: bool
        LOCAL_BLUR_ASPECT: float
        LOCAL_BLUR_OFFSET: float
        LOCAL_DEFOCUS: float
        LOCAL_DEFOCUS_ASPECT: float
        LOCAL_MAX__RAYS: int
        LOCAL_MIN__RAYS: int
        LOCAL_THRESHOLD: float
        LUMINOSITY: MXSWrapperBase
        LUMINOSITYMAP: None
        LUMINOSITYMAPAMOUNT: float
        LUMINOSITYMAPENABLE: bool
        LUMINOSITY_COLOR_ON: bool
        OPTIONS___ANTIALIASING_ENABLE: bool
        OPTIONS___COLOR_DENSITY___FOG_ENABLE: bool
        OPTIONS___RAYTRACER_ENABLE: bool
        OPTIONS___RAYTRACE_ATMOSPHERICS: bool
        OPTIONS___RAYTRACE_ATMOSPHERICS_IN_GLASS: bool
        OPTIONS___RAYTRACE_OBJECTS_IN_GLASS: bool
        OPTIONS___REFLECT_REFRACT_MATERIAL_ID_S: bool
        OPTIONS___SELF_REFLECT_REFRACT: bool
        ORIENTATION: float
        OVERRIDE_GLOBAL_ANTIALIASING_SETTINGS: bool
        REFLECT: MXSWrapperBase
        REFLECTIONMAP: None
        REFLECTIONMAPAMOUNT: float
        REFLECTIONMAPENABLE: bool
        REFLECTION_FALLOFF_DISTANCE: float
        REFLECTION_FALLOFF_END_DISTANCE: float
        REFLECTION_FALLOFF_MODE: int
        REFLECTION_GAIN: float
        REFLECTION_TYPE: int
        REFLECT_AMOUNT: float
        REFLECT_COLOR_ON: int
        REFRACTION_FALLOFF_DISTANCE: float
        REFRACTION_FALLOFF_END_DISTANCE: float
        REFRACTION_FALLOFF_MODE: int
        SELF_ILLUM_AMOUNT: float
        SHADERBYNAME: str
        SHADERTYPE: int
        SLIDING_FRICTION: float
        SOFTEN: float
        SPECULARLEVELMAP: None
        SPECULARLEVELMAPAMOUNT: float
        SPECULARLEVELMAPENABLE: bool
        SPECULARMAP: None
        SPECULARMAPAMOUNT: float
        SPECULARMAPENABLE: bool
        SPECULAR_LEVEL: float
        SPEC__COLOR: MXSWrapperBase
        STATIC_FRICTION: float
        SUPERSAMPLE: bool
        TRANSENVMAP: None
        TRANSENVMAPAMOUNT: float
        TRANSENVMAPENABLE: bool
        TRANSLUCENCY: MXSWrapperBase
        TRANSLUCENCYMAP: None
        TRANSLUCENCYMAPAMOUNT: float
        TRANSLUCENCYMAPENABLE: bool
        TRANSPARECY: MXSWrapperBase
        TRANSPARENCYMAP: None
        TRANSPARENCYMAPAMOUNT: float
        TRANSPARENCYMAPENABLE: bool
        TRANSPARENCY_AMOUNT: float
        TRANSPARENCY_COLOR_ON: bool
        TWOSIDED: bool
        WIRE: bool
        WIREUNITS: int
        WIRE_SIZE: float
        ...
    class Raytrace_Texture_ParamBlock(ReferenceTarget):
        ...
    class ReactionManager(ReferenceMaker):
        ...
    class ReactionMaster(ReferenceMaker):
        ...
    class ReactionSet(ReferenceMaker):
        ...
    class Reaction_Manager(ReferenceMaker):
        ...
    class Reaction_Master(ReferenceMaker):
        ...
    class Reaction_Set(ReferenceMaker):
        ...
    class ReactorAngleManip(Helper):
        ...
    class Reactor_Angle_Manip(Helper):
        ...
    class ReadByte(Primitive):
        ...
    class ReadDouble(Primitive):
        ...
    class ReadDoubleAsFloat(Primitive):
        ...
    class ReadFloat(Primitive):
        ...
    class ReadLong(Primitive):
        ...
    class ReadLongLong(Primitive):
        ...
    class ReadShort(Primitive):
        ...
    class ReadString(Primitive):
        ...
    class Rectangle(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        CORNERRADIUS: float
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        LENGTH: float
        MAPCOORDS: bool
        OPTIMIZE: bool
        QUAD_CAP: bool
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        WIDTH: float
        ...
    class RefTargContainer(ReferenceTarget):
        ...
    class RefTargMonitor(ReferenceTarget):
        ...
    class ReferenceMaker(MAXWrapper):
        ...
    class ReferenceTarget(MAXWrapper):
        ...
    class Reflect_Refract(TextureMap):
        APPLY: bool
        BITMAPNAME: MXSWrapperBase
        BLUR: float
        BLUROFFSET: float
        FAR: float
        FRAMETYPE: int
        NEAR: float
        NTHFRAME: int
        OUTPUTNAME: None
        SIZE: int
        SOURCE: int
        USEATMOSPHERICMAP: bool
        ...
    class Reflection(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class ReflectionFragment(GraphicsFragmentPlugin):
        ...
    class Refraction(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class Relax(Modifier):
        ITERATIONS: int
        KEEP_BOUNDARY_PTS_FIXED: int
        RELAX_VALUE: float
        ...
    class RemoveDictValue(Primitive):
        ...
    class RemoveSubRollout(Primitive):
        ...
    class RemoveTempPrompt(Primitive):
        ...
    class RendSpline(Modifier):
        ANGLE2: float
        ANGLE: float
        AUTOSMOOTH: bool
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERSETTINGS: bool
        LENGTH: float
        LOCKASPECT: bool
        MAPCOORDS: bool
        QUAD_CAP: bool
        RENDERABLE: bool
        SIDES: int
        SPHERE_CAP: float
        SYMMETRICALORRECTANGULAR: int
        THICKNESS: float
        THRESHOLD: float
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORTORRENDER: int
        VIEWPORT_ANGLE2: float
        VIEWPORT_ANGLE: float
        VIEWPORT_LENGTH: float
        VIEWPORT_LOCKASPECT: bool
        VIEWPORT_SIDES: int
        VIEWPORT_SYMMETRICALORRECTANGULAR: int
        VIEWPORT_THICKNESS: float
        VIEWPORT_WIDTH: float
        WIDTH: float
        ...
    class RenderElement(MAXWrapper):
        ...
    class RenderElementMgr(ReferenceTarget):
        ...
    class RenderEnhancements(Interface):
        ...
    class RenderEnvironment(Atmospheric):
        ...
    class RenderParticles(Helper):
        MESH_COUNT: int
        PARTICLES_PER_MESH: int
        SPLIT_TYPE: int
        TYPE: int
        VISIBLE: float
        ...
    class Renderable_Spline(Modifier):
        ANGLE2: float
        ANGLE: float
        AUTOSMOOTH: bool
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERSETTINGS: bool
        LENGTH: float
        LOCKASPECT: bool
        MAPCOORDS: bool
        QUAD_CAP: bool
        RENDERABLE: bool
        SIDES: int
        SPHERE_CAP: float
        SYMMETRICALORRECTANGULAR: int
        THICKNESS: float
        THRESHOLD: float
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORTORRENDER: int
        VIEWPORT_ANGLE2: float
        VIEWPORT_ANGLE: float
        VIEWPORT_LENGTH: float
        VIEWPORT_LOCKASPECT: bool
        VIEWPORT_SIDES: int
        VIEWPORT_SYMMETRICALORRECTANGULAR: int
        VIEWPORT_THICKNESS: float
        VIEWPORT_WIDTH: float
        WIDTH: float
        ...
    class RendererClass(MAXWrapper):
        ...
    class RepelBehavior(ReferenceTarget):
        DISPLAYFORCE: bool
        FALLOFF: float
        FORCECOLOR: MXSWrapperBase
        INNERRADIUS: float
        NAME: str
        OUTERRADIUS: float
        REPELMETHOD: int
        REPULSIONSOURCES: MXSWrapperBase
        SHOWRADII: bool
        TARGETCOMP: int
        USERADII: bool
        ...
    class Repel_Behavior(ReferenceTarget):
        DISPLAYFORCE: bool
        FALLOFF: float
        FORCECOLOR: MXSWrapperBase
        INNERRADIUS: float
        NAME: str
        OUTERRADIUS: float
        REPELMETHOD: int
        REPULSIONSOURCES: MXSWrapperBase
        SHOWRADII: bool
        TARGETCOMP: int
        USERADII: bool
        ...
    class ReplacePrompt(Primitive):
        ...
    class RescaleWorldUnits(Primitive):
        ...
    class Rescale_World_Units(UtilityPlugin):
        ...
    class Reservoir(FloatController):
        ...
    class ResetOptimizeDependentNotificationsStatistics(Primitive):
        ...
    class ResetPivot(MappedPrimitive):
        ...
    class ResetScale(MappedPrimitive):
        ...
    class ResetTransform(MappedPrimitive):
        ...
    class ResetXForm(MappedPrimitive):
        ...
    class Reset_XForm(UtilityPlugin):
        ...
    class Resource_Collector(UtilityPlugin):
        ...
    class RestoreControllerValue(Primitive):
        ...
    class ResumeEditing(Primitive):
        ...
    class Retimer(FloatController):
        ...
    class RetimerCtrl(FloatController):
        ...
    class RetimerMan(Interface):
        ...
    class RetimerMasterCtrl(CtrlUserDataTypeClass):
        ...
    class RevitDBManager(Interface):
        ...
    class RevitImportWorkflow(Interface):
        ...
    class RevitImporterGetOption(Primitive):
        ...
    class RevitImporterSetOption(Primitive):
        ...
    class Revit_Import(ImporterPlugin):
        ...
    class Revit_Importer(ImporterPlugin):
        ...
    class RingArray(Interface):
        ...
    class RingWave(GeometryClass):
        DISPLAY_UNTIL: int
        HEIGHT: float
        HEIGHT_SEGS: int
        INNER_EDGE_BREAKUP: bool
        MAJOR_CYCLES_INNER: int
        MAJOR_CYCLES_OUTER: int
        MAJOR_CYCLE_FLUX_INNER: float
        MAJOR_CYCLE_FLUX_OUTER: float
        MAJOR_CYCLE_FLUX_PER_INNER: int
        MAJOR_CYCLE_FLUX_PER_OUTER: int
        MAPPING_COORDS: bool
        MAX_DIAMETER: float
        MINOR_CYCLES_INNER: int
        MINOR_CYCLES_OUTER: int
        MINOR_CYCLE_FLUX_INNER: float
        MINOR_CYCLE_FLUX_OUTER: float
        MINOR_CYCLE_FLUX_PER_INNER: int
        MINOR_CYCLE_FLUX_PER_OUTER: int
        OUTER_EDGE_BREAKUP: bool
        RADIUS_SEGS: int
        REPEATS: int
        RING_SEGMENTS: int
        RING_WIDTH: float
        SMOOTHING: bool
        TIME_GROWING: int
        TIME_ON: int
        ...
    class Ring_Array(System):
        ...
    class Ring_Element(ReferenceTarget):
        ALPHA: int
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        APPLYLIGHTS: bool
        APPLYNOISE: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        CENTERCOLOR: MXSWrapperBase
        CIRCULARCOLORMIX: float
        CIRCULARMAP: None
        CIRCULARMTL: None
        COLORSOURCE: float
        EDGECOLOR: MXSWrapperBase
        EFFECTSID: int
        ELEMENTNAME: str
        FILTERALL: bool
        FILTERBRIGHTNESS: bool
        FILTEREDGE: bool
        FILTERHUE: bool
        FILTERPERIMETER: bool
        FILTERPERIMETERALPHA: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        INTENSITY: float
        NOISEMAP: None
        OBJECTID: int
        OBJECTSHIDE: bool
        OCCLUSION: float
        ON: bool
        PLANE: float
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        QUADRANT4COLOR: MXSWrapperBase
        RADIALDENSITY: None
        RADIALMAP: None
        RADIALMTL: None
        RADIALSIZEMAP: None
        SIZE: float
        SOURCEALPHA: bool
        SOURCEEFFECTSID: bool
        SOURCEOBJECTID: bool
        SOURCESURFACENORMAL: bool
        SOURCEUNCLAMPEDCOLOR: bool
        SOURCEWHOLE: bool
        SOURCEZBUFFER: bool
        SQUEEZE: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        THICKNESS: float
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        USECIRCULARMAP: bool
        USECIRCULARMTL: bool
        USERADIALDENSITY: bool
        USERADIALMAP: bool
        USERADIALMTL: bool
        USERADIALSIZEMAP: bool
        ZHI: float
        ZLO: float
        ...
    class Ripple(Modifier):
        AMPLITUDE1: float
        AMPLITUDE2: float
        DECAY: float
        PHASE: float
        WAVELENGTH: float
        ...
    class Ripplebinding(SpacewarpModifier):
        ...
    class RmModel(GeometryClass):
        ...
    class RmModelGeometry(GeometryClass):
        ...
    class RolloutClass(Value):
        ...
    class RolloutControl(Value):
        ...
    class RootNodeClass(Node):
        ...
    class Rotate(NodeGeneric):
        ...
    class RotateX(MappedGeneric):
        ...
    class RotateXMatrix(Primitive):
        ...
    class RotateY(MappedGeneric):
        ...
    class RotateYMatrix(Primitive):
        ...
    class RotateYPRMatrix(Primitive):
        ...
    class RotateZ(MappedGeneric):
        ...
    class RotateZMatrix(Primitive):
        ...
    class RotationLayer(RotationController):
        ...
    class RotationList(RotationController):
        AVERAGE: bool
        WEIGHT: MXSWrapperBase
        ...
    class RotationReactor(RotationController):
        ...
    class Rotation_Layer(RotationController):
        ...
    class Rotation_Mixer_Controller(RotationController):
        ...
    class Rotation_Motion_Capture(RotationController):
        ...
    class Rotation_Reactor(RotationController):
        ...
    class Rotation_Wire(RotationController):
        ...
    class RvtComponentPacket(ReferenceMaker):
        ...
    class RvtElementtPacket(ReferenceMaker):
        ...
    class RvtObjTranslator(ReferenceMaker):
        ...
    class SATExport(ExporterPlugin):
        ...
    class SATImport(ImporterPlugin):
        ...
    class SDeflectMod(SpacewarpModifier):
        ...
    class SDeflector(SpacewarpObject):
        BOUNCE: float
        BOUNCEVAR: float
        CHAOS: float
        FRICTION: float
        INHERITVELOCITY: float
        RADIUS: float
        ...
    class SLAP(RenderEffect):
        ...
    class SME(Interface):
        ...
    class SMEGUP(GlobalUtilityPlugin):
        ...
    class SOmniFlect(SpacewarpObject):
        AFFECTS: float
        BOUNCE: float
        BOUNCEVAR: float
        CHAOS: float
        DECELERATION: float
        DECELVAR: float
        DIFFUSION: float
        DIFFUSIONVAR: float
        FRICTION: float
        INHERITVELOCITY: float
        PASSVELOCITY: float
        PASSVELOCITYVAR: float
        RADIUS: float
        REFRACTION: float
        REFRACTIONVAR: float
        REFRACTS: float
        SPAWN: float
        TIMEOFF: MXSWrapperBase
        TIMEON: MXSWrapperBase
        ...
    class SOmniFlectMod(SpacewarpModifier):
        ...
    class STL_Check(Modifier):
        CHANGE_MATID: int
        CHECK_NOW: int
        MATERIAL_ID: int
        SELECTION_TYPE: int
        SELECT_FACES: int
        ...
    class STL_Export(ExporterPlugin):
        ...
    class STL_Import(ImporterPlugin):
        ...
    class SafeArrayWrapper(Value):
        ...
    class SamplerClass(MAXWrapper):
        ...
    class SaveQuadClr(MAXScriptFunction):
        ...
    class Save_Verification(GlobalUtilityPlugin):
        ...
    class Scalar(ReferenceTarget):
        ANGLE_VALUE: float
        ANGLE_VARIATION: float
        BOOLEAN_VALUE: int
        FILTER: None
        FLOAT_VALUE: float
        FLOAT_VARIATION: float
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INTEGER_VALUE: int
        INTEGER_VARIATION: int
        OUTPUT_TYPE: int
        PERCENT_VALUE: float
        PERCENT_VARIATION: float
        RANDOM_SEED: int
        SYNC_TYPE: int
        TIME_VALUE: int
        TIME_VARIATION: int
        UNITS_PER_TYPE: int
        USE_AS_ACCELERATION: bool
        USE_AS_SPEED_OR_SPIN_RATE: bool
        USE_E1: bool
        USE_E2: bool
        USE_E3: bool
        USE_E4: bool
        USE_FOR_TIME_RELATED_ADDITION: bool
        USE_FOR_TIME_RELATED_MULTIPLICATION: bool
        WORLD_VALUE: float
        WORLD_VARIATION: float
        ...
    class ScaleLayer(ScaleController):
        ...
    class ScaleList(ScaleController):
        AVERAGE: bool
        WEIGHT: MXSWrapperBase
        ...
    class ScaleMatrix(Primitive):
        ...
    class ScaleParticles(Helper):
        BIAS: int
        CONSTRAIN_SCALE: bool
        CONSTRAIN_SCALE_VARIATION: bool
        RANDOM_SEED: int
        SYNC_TYPE: int
        TYPE: int
        X_SCALE_FACTOR: float
        X_SCALE_VARIATION: float
        Y_SCALE_FACTOR: float
        Y_SCALE_VARIATION: float
        Z_SCALE_FACTOR: float
        Z_SCALE_VARIATION: float
        ...
    class ScaleReactor(ScaleController):
        ...
    class ScaleXYZ(ScaleController):
        ...
    class Scale_Expression(ScaleController):
        ...
    class Scale_Layer(ScaleController):
        ...
    class Scale_Mixer_Controller(ScaleController):
        ...
    class Scale_Motion_Capture(ScaleController):
        ...
    class Scale_Reactor(ScaleController):
        ...
    class Scale_Test(Helper):
        AXIS_TYPE: int
        CONDITION_TYPE: int
        RANDOM_SEED: int
        SCALE_VALUE: float
        SCALE_VARIATION: float
        SIZE_VALUE: float
        SIZE_VARIATION: float
        SYNC_TYPE: int
        TEST_TYPE: int
        ...
    class Scale_Wire(ScaleController):
        ...
    class Scatter(GeometryClass):
        ...
    class ScatterReferenceTarget(ReferenceTarget):
        CENTERX: float
        CENTERY: float
        CENTERZ: float
        CHILDBBOX: bool
        CLONECONTROLLERS: bool
        CLONEHIERARCHY: bool
        CLONEOBJECT: None
        CLONETYPE: int
        COMPUTECLONES: bool
        COMPUTEPOSITIONS: bool
        COMPUTEROTATIONS: bool
        COMPUTESCALES: bool
        FORWARDAXIS: int
        FORWARDAXISSIGN: bool
        INCPOSITIONSEED: bool
        INCPOSSEED: bool
        INCROTATIONSEED: bool
        INCROTSEED: bool
        INCSCALESEED: bool
        INCSCLSEED: bool
        LOOKATTARGET: None
        LOOKFROM: int
        LOOKFROMOBJECT: None
        LOOKTOWARDS: int
        MATCHXTOYSCALE: bool
        MATCHXTOZSCALE: bool
        MATCHYTOXSCALE: bool
        MATCHYTOZSCALE: bool
        MATCHZTOXSCALE: bool
        MATCHZTOYSCALE: bool
        NUMCLONES: int
        OBJECTSTOSCATTER: MXSWrapperBase
        POSITIONOBJECT: None
        POSITIONSEED: int
        POSITIONSPACE: int
        RADIUS: float
        ROTATIONSEED: int
        SCALESEED: int
        SIDEDEVIATION: float
        SPACING: float
        SURFACEOFFSET: float
        UPAXIS: int
        UPAXISSIGN: bool
        UPDOWNDEVIATION: float
        XSCALE: float
        XSCALEDEVIATION: float
        XYPLANE: bool
        YSCALE: float
        YSCALEDEVIATION: float
        ZSCALE: float
        ZSCALEDEVIATION: float
        ...
    class Scene(ReferenceTarget):
        ...
    class SceneAppDataLatch(CtrlUserDataTypeClass):
        ...
    class SceneAppData_Latch(CtrlUserDataTypeClass):
        ...
    class SceneConverter(Interface):
        ...
    class SceneEffectLoader(Interface):
        ...
    class SceneExplorerManager(Interface):
        ...
    class SceneExposureControl(Interface):
        ...
    class SceneMissingPlugIns(Interface):
        ...
    class SceneRadiosity(Interface):
        ...
    class Scene_Converter(GlobalUtilityPlugin):
        ...
    class Scene_Effect_Loader(FloatController):
        ...
    class Scene_Effect_LoaderUtilityPlugin(UtilityPlugin):
        ...
    class Scene_State(ReferenceTarget):
        ...
    class Scene_State_Manager(UtilityPlugin):
        ...
    class Scene_State_ManagerCtrlUserDataTypeClass(CtrlUserDataTypeClass):
        ...
    class SchematicViewUtility(MAXWrapperNonRefTarg):
        ...
    class ScriptSecurityManager(Interface):
        ...
    class Script_Operator(Helper):
        PROCEED_SCRIPT: str
        RANDOM_SEED: int
        ...
    class Script_Test(Helper):
        PROCEED_SCRIPT: str
        RANDOM_SEED: int
        ...
    class ScriptedBehavior(ReferenceTarget):
        NAME: str
        SCRIPT: None
        SCRIPTCONTEXTNAME: str
        TYPE: int
        ...
    class Scripted_Behavior(ReferenceTarget):
        NAME: str
        SCRIPT: None
        SCRIPTCONTEXTNAME: str
        TYPE: int
        ...
    class Seat(GeometryClass):
        GENDER: int
        HEIGHT: float
        ID: int
        MOTIONSEED: int
        SINGLE: bool
        ...
    class SecurityTools(Interface):
        ...
    class SecurityToolsUtility(GlobalUtilityPlugin):
        ...
    class SeekBehavior(ReferenceTarget):
        DISPLAYFORCE: bool
        FALLOFF: float
        FORCECOLOR: MXSWrapperBase
        INNERRADIUS: float
        NAME: str
        OUTERRADIUS: float
        SEEKMETHOD: int
        SHOWRADII: bool
        TARGETCOMP: int
        TARGETS: MXSWrapperBase
        USERADII: bool
        ...
    class Seek_Behavior(ReferenceTarget):
        DISPLAYFORCE: bool
        FALLOFF: float
        FORCECOLOR: MXSWrapperBase
        INNERRADIUS: float
        NAME: str
        OUTERRADIUS: float
        SEEKMETHOD: int
        SHOWRADII: bool
        TARGETCOMP: int
        TARGETS: MXSWrapperBase
        USERADII: bool
        ...
    class SegTrans(Matrix3Controller):
        ...
    class SelectByChannel(Modifier):
        MAPID: int
        MAPSUBID: int
        SELECTIONTYPE: int
        ...
    class SelectSaveBitMap(Primitive):
        ...
    class Select_By_Channel(Modifier):
        MAPID: int
        MAPSUBID: int
        SELECTIONTYPE: int
        ...
    class Select_Keys_By_Time(TrackViewUtility):
        ...
    class Select_Object(ReferenceTarget):
        FILTER: None
        INDEPENDENT_PFLOW_SYSTEM: bool
        OBJECT: None
        OBJECTS: MXSWrapperBase
        SINGLE_OR_MULTIPLE: int
        TYPE: int
        ...
    class Select_The_Biped_For_Use_As_A_Retargeting_Reference(ReferenceTarget):
        ...
    class SelectionFragment(GraphicsFragmentPlugin):
        ...
    class SelectionHasCATParent(MAXScriptFunction):
        ...
    class SelectionPreviewFragment(GraphicsFragmentPlugin):
        ...
    class SelectionSet(Value):
        ...
    class SelectionSetArray(Value):
        ...
    class Self_Illumination(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class Send_Out(Helper):
        CONDITION_TYPE: int
        ...
    class SetActiveController(MAXScriptFunction):
        ...
    class SetBackGround(Primitive):
        ...
    class SetBackGroundController(Primitive):
        ...
    class SetBkgFrameRange(Primitive):
        ...
    class SetBkgImageAnimate(Primitive):
        ...
    class SetBkgImageAspect(Primitive):
        ...
    class SetBkgORType(Primitive):
        ...
    class SetBkgStartTime(Primitive):
        ...
    class SetBkgSyncFrame(Primitive):
        ...
    class SetCVertMode(Primitive):
        ...
    class SetCommandPanelTaskMode(Primitive):
        ...
    class SetControllerValue(Primitive):
        ...
    class SetCoordCenter(Primitive):
        ...
    class SetCurNamedSelSet(Primitive):
        ...
    class SetDialogBitmap(Primitive):
        ...
    class SetDialogPos(Primitive):
        ...
    class SetDialogSize(Primitive):
        ...
    class SetDictValue(Primitive):
        ...
    class SetDir(Primitive):
        ...
    class SetDisplayFilter(Primitive):
        ...
    class SetGridMajorLines(Primitive):
        ...
    class SetGridSpacing(Primitive):
        ...
    class SetImageBlurMultController(Primitive):
        ...
    class SetImageBlurMultiplier(Primitive):
        ...
    class SetInheritVisibility(Primitive):
        ...
    class SetKeyCtrl(FloatController):
        KEYINDEX: int
        ...
    class SetKeyStepsPos(Primitive):
        ...
    class SetKeyStepsRot(Primitive):
        ...
    class SetKeyStepsScale(Primitive):
        ...
    class SetKeyStepsSelOnly(Primitive):
        ...
    class SetKeyStepsUseTrans(Primitive):
        ...
    class SetMaxAssertDisplay(Primitive):
        ...
    class SetMaxAssertLogFileName(Primitive):
        ...
    class SetMotBlur(Primitive):
        ...
    class SetNodes(BipedGeneric):
        ...
    class SetPatchSteps(Primitive):
        ...
    class SetPosTaskWeight(Primitive):
        ...
    class SetQuietMode(Primitive):
        ...
    class SetRefCoordSys(Primitive):
        ...
    class SetRendApertureWidth(Primitive):
        ...
    class SetRenderID(Primitive):
        ...
    class SetRenderType(Primitive):
        ...
    class SetRenderable(Primitive):
        ...
    class SetRotTaskWeight(Primitive):
        ...
    class SetSelectFilter(Primitive):
        ...
    class SetShadeCVerts(Primitive):
        ...
    class SetSilentMode(Primitive):
        ...
    class SetStatusXYZ(Primitive):
        ...
    class SetSysCur(Primitive):
        ...
    class SetTaskAxisState(Primitive):
        ...
    class SetToolBtnState(Primitive):
        ...
    class SetTrajectoryON(Primitive):
        ...
    class SetTwOrgTime(BipedGeneric):
        ...
    class SetTwWarpTime(BipedGeneric):
        ...
    class SetUIColor(Primitive):
        ...
    class SetUseEnvironmentMap(Primitive):
        ...
    class SetVPortBGColor(Primitive):
        ...
    class SetWeight(BipedGeneric):
        ...
    class SetWeightAtTime(BipedGeneric):
        ...
    class SetWeightTime(BipedGeneric):
        ...
    class Set_Key_Crtl(FloatController):
        KEYINDEX: int
        ...
    class Setting(ReferenceTarget):
        ACTIVE: bool
        AVERAGESPEED1: float
        AVERAGESPEED2: float
        BANKFACTOR1: float
        BANKFACTOR2: float
        DECLINEDECEL1: float
        DECLINEDECEL2: float
        DECLINEDECELANGLE1: float
        DECLINEDECELANGLE2: float
        DELEGATES: MXSWrapperBase
        INCLINEDECEL1: float
        INCLINEDECEL2: float
        INCLINEDECELANGLE1: float
        INCLINEDECELANGLE2: float
        MAXACCEL1: float
        MAXACCEL2: float
        MAXBANK1: float
        MAXBANK2: float
        MAXBANKACCEL1: float
        MAXBANKACCEL2: float
        MAXDECLINE1: float
        MAXDECLINE2: float
        MAXINCLINE1: float
        MAXINCLINE2: float
        MAXTURN1: float
        MAXTURN2: float
        MAXTURNACCEL1: float
        MAXTURNACCEL2: float
        NAME: None
        PRIORITY1: int
        PRIORITY2: int
        RAND10: bool
        RAND11: bool
        RAND12: bool
        RAND13: bool
        RAND14: bool
        RAND15: bool
        RAND16: bool
        RAND17: bool
        RAND18: bool
        RAND1: bool
        RAND2: bool
        RAND3: bool
        RAND4: bool
        RAND5: bool
        RAND6: bool
        RAND7: bool
        RAND8: bool
        RAND9: bool
        SET10: bool
        SET11: bool
        SET12: bool
        SET13: bool
        SET14: bool
        SET15: bool
        SET16: bool
        SET17: bool
        SET18: bool
        SET19: bool
        SET1: bool
        SET20: bool
        SET21: bool
        SET22: bool
        SET23: bool
        SET24: bool
        SET25: bool
        SET26: bool
        SET2: bool
        SET3: bool
        SET4: bool
        SET5: bool
        SET6: bool
        SET7: bool
        SET8: bool
        SET9: bool
        SHOWCOGSTATES: bool
        SHOWFORCES: bool
        SHOWVELOCITY: bool
        STARTCLIP: int
        STARTFRAME1: int
        STARTFRAME2: int
        TURNDECEL1: float
        TURNDECEL2: float
        TURNDECELANGLE1: float
        TURNDECELANGLE2: float
        USEBIPED: bool
        USEHIERBBOX: bool
        VELOCITYCOLOR: MXSWrapperBase
        XYCONSTRAIN: bool
        ...
    class Shader(MAXWrapper):
        ...
    class Shadow(MAXWrapper):
        ...
    class ShadowClass(Value):
        ...
    class ShadowRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class ShadowsMap(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        TARGETMAPSLOTNAME: str
        ...
    class ShapeBooleanObject(Shape):
        ...
    class ShapeControl(ReferenceTarget):
        ACQUIRE_MAPPING: bool
        ANIMATED_SHAPE: bool
        DISCRETE_OPTIMIZATION: bool
        EXECUTION_ORDER: int
        FILTER: None
        HISTORY_DEPENDENT: bool
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        INPUT_7: None
        INPUT_8: None
        INPUT_TIME: None
        PARTICLE_GEOMETRY_OBJECT: None
        PRIORITY_ORDER: int
        PROCEED_TYPE: int
        ...
    class ShapeFilterFn(MAXScriptFunction):
        ...
    class ShapeLibrary(Helper):
        DIMENSION_TYPE: int
        FIT_MAPPING: bool
        GENERATE_MAPPING_COORDS: bool
        RANDOM_MULTI_SHAPE_ORDER: bool
        RANDOM_SEED: int
        SCALE_VALUE: float
        SCALE_VARIATION: float
        SIZE: float
        TYPE_2D: int
        TYPE_3D: int
        USE_SCALE: bool
        ...
    class ShapeMap(TextureMap):
        ALPHASOURCE: int
        APPLYCROP: bool
        BGCOLOR: MXSWrapperBase
        BOUNDSOBJECT: None
        BOUNDSTYPE: int
        COORDS: MXSWrapperBase
        CROPORPLACE: int
        CROP_H: float
        CROP_U: float
        CROP_V: float
        CROP_W: float
        ENDTYPE: int
        FILLBG: bool
        FILLCOLOR: MXSWrapperBase
        FILLEDCLOSED: bool
        FILTER: bool
        FINITERESOLUTION: int
        HWBITMAPSIZE: int
        JITTER: bool
        JITTERAMT: float
        MANUALHEIGHT: float
        MANUALWIDTH: float
        MERGESHAPES: bool
        MIPMAP: bool
        MONOOUTPUT: int
        OUTLINECOLOR: MXSWrapperBase
        OUTLINEDCLOSED: bool
        OUTLINEWIDTH: float
        OUTPUT: MXSWrapperBase
        RENDERCHILDREN: bool
        RENDEROPEN: bool
        RENDERROOT: bool
        RESTYPE: int
        RGBOUTPUT: int
        SHAPEOBJECT: None
        STRICTHIERARCHY: bool
        USEFILLCOLOR: bool
        ...
    class ShapeMerge(GeometryClass):
        OPERATION_TYPE: int
        OUTPUT_SUB_MESH_SELECTION: int
        REMOVE_INTERIOR_EXTERIOR: int
        ...
    class ShapeStandard(Helper):
        SCALE_VALUE: float
        SHAPE: int
        SIZE: float
        USE_SCALE: bool
        ...
    class Shape_Check(UtilityPlugin):
        ...
    class Shape_Facing(Helper):
        INHERITED_SCALE: float
        LOOK_AT_OBJECT: None
        ORIENTATION: int
        PARALLEL: bool
        PIVOT_AT: int
        PROPORTION: float
        RANDOM_SEED: int
        SIZE_SPACE: int
        UNITS: float
        VARIATION: float
        WH_RATIO: float
        ...
    class Shape_Instance(Helper):
        ACQUIRE_MAPPING: bool
        ACQUIRE_MATERIAL: bool
        ACQUIRE_SHAPE: bool
        ADD_RANDOM_OFFSET: bool
        ANIMATED_SHAPE: bool
        FAST_SHAPE_EVALUATION: bool
        GROUP_MEMBERS: bool
        HANDLES_TO_REPORT: MXSWrapperBase
        OBJECT_AND_CHILDREN: bool
        OBJECT_ELEMENTS: bool
        RANDOM_OFFSET: int
        RANDOM_SEED: int
        RANDOM_SHAPE: bool
        REPORT_NODE_HANDLES: int
        SCALE_VALUE: float
        SET_SCALE: bool
        SHAPE_OBJECT: None
        SUBMTL_ID_OFFSET: int
        SYNC_TYPE: int
        VARIATION: float
        ...
    class Shape_Mark(Helper):
        ALIGN_TO: int
        ANGLE_DISTORTION: bool
        CONTACT_OBJECT: None
        CONTINUOUS_UPDATE: bool
        DIVERGENCE: float
        GENERATE_MAPPING_COORDS: bool
        HEIGHT: float
        INHERITED_SCALE: float
        LENGTH: float
        MARK_TYPE: int
        MAX_DISTORTION: float
        MULTI_ELEMENTS: bool
        PIVOT_OFFSET: float
        RANDOM_SEED: int
        SIZE_SPACE: int
        SURFACE_ANIMATION: bool
        SURFACE_OFFSET: float
        SURFACE_OFFSET_VARIATION: float
        VARIATION: float
        VERTEX_NOISE: float
        WIDTH: float
        ...
    class SharedMoflow(ReferenceTarget):
        BIPEDS: MXSWrapperBase
        FIGFILELOADED: bool
        NAME: str
        ...
    class SharedMoflowList(ReferenceTarget):
        EDITEDSHAREDMOFLOW: None
        SHAREDMOFLOWS: MXSWrapperBase
        ...
    class SharedMotionFlow(ReferenceTarget):
        BIPEDS: MXSWrapperBase
        FIGFILELOADED: bool
        NAME: str
        ...
    class SharedMotionFlows(ReferenceTarget):
        EDITEDSHAREDMOFLOW: None
        SHAREDMOFLOWS: MXSWrapperBase
        ...
    class SharedMotionFlowsFloatController(FloatController):
        ...
    class SharedViews(UtilityPlugin):
        ...
    class Sharp_Quadratic(Filter):
        ...
    class ShaveStylinIcon(Helper):
        ...
    class Shell(Modifier):
        AUTOSMOOTH: bool
        AUTOSMOOTHANGLE: float
        BEVEL: bool
        BEVELSHAPE: None
        EDGEMAPPING: int
        INNERAMOUNT: float
        MATID: int
        MATINNERID: int
        MATOUTERID: int
        OUTERAMOUNT: float
        OVERRIDEINNERMATID: bool
        OVERRIDEMATID: bool
        OVERRIDEOUTERMATID: bool
        OVERRIDESMOOTHINGGROUP: bool
        SEGMENTS: int
        SELECTEDGEFACES: bool
        SELECTINNERFACES: bool
        SELECTOUTERFACES: bool
        SMOOTHGROUP: int
        STRAIGHTENCORNERS: bool
        TVOFFSET: float
        ...
    class ShellLaunch(Primitive):
        ...
    class Shell_Material(Material):
        BAKEDMATERIAL: MXSWrapperBase
        ORIGINALMATERIAL: MXSWrapperBase
        RENDERMTLINDEX: int
        VIEWPORTMTLINDEX: int
        ...
    class Shellac(Material):
        SHELLACCOLORBLEND: float
        SHELLACMTL1: MXSWrapperBase
        SHELLACMTL2: MXSWrapperBase
        ...
    class ShineExp(UtilityPlugin):
        ...
    class ShowAllActiveXControls(Primitive):
        ...
    class ShowDialog(Primitive):
        ...
    class SilentMode(Primitive):
        ...
    class SimpleFaceData(CustAttrib):
        ...
    class SimpleOSMToWSMMod(SpacewarpModifier):
        ...
    class SimpleOSMToWSMMod2(SpacewarpModifier):
        ...
    class Simple_Shape(Shape):
        ...
    class Simple_Spline(Shape):
        ...
    class SingleWeakRefMakerClass(MAXWrapperNonRefTarg):
        ...
    class Skeleton(Helper):
        ...
    class Skew(Modifier):
        AMOUNT: float
        AXIS: int
        DIRECTION: float
        LIMIT: bool
        LOWERLIMIT: float
        UPPERLIMIT: float
        ...
    class Skin(Modifier):
        ALWAYS_DEFORM: bool
        ANIMATABLEENVELOPES: bool
        BACKFACECULL: bool
        BACKTRANSFORM: bool
        BONE_LIMIT: int
        CLEARZEROLIMIT: float
        COLORALLWEIGHTS: bool
        CROSSSECTIONSALWAYSONTOP: bool
        CROSS_RADIUS: float
        DEBUGMODE: bool
        DRAW_ALL_ENVELOPES: bool
        DRAW_ALL_GIZMOS: bool
        DRAW_ALL_VERTICES: bool
        DRAW_VERTICES: bool
        EFFECT: float
        ENABLEDQ: bool
        ENVELOPESALWAYSONTOP: bool
        FASTGIZMOS: bool
        FASTSUBANIMS: bool
        FASTTMCACHE: bool
        FASTVERTEXWEIGHTING: bool
        FAST_UPDATE: bool
        FILTER_CROSS_SECTIONS: bool
        FILTER_ENVELOPES: bool
        FILTER_VERTICES: bool
        GIZMOS: MXSWrapperBase
        IGNOREBONESCALE: bool
        INITIALENVELOPEINNER: float
        INITIALENVELOPEOUTER: float
        INITIALINNERENVELOPEPERCENT: float
        INITIALOUTERENVELOPEPERCENT: float
        INITIALSQUASH: MXSWrapperBase
        INITIALSTATICENVELOPE: bool
        LOCALSQUASH: MXSWrapperBase
        MANUALUPDATE: bool
        MIRRORENABLED: bool
        MIRRORFAST: bool
        MIRROROFFSET: float
        MIRRORPLANE: int
        MIRRORPROJECTION: int
        MIRRORTHRESHOLD: float
        MIRRORUSEINITIALTM: bool
        NO_UPDATE: bool
        PAINTBLENDMODE: bool
        PAINT_FEATHER: float
        PAINT_RADIUS: float
        PAINT_STR: float
        REF_FRAME: int
        RIGHTJUSTIFYBONETEXT: bool
        RIGID_HANDLES: bool
        RIGID_VERTICES: bool
        SELECTELEMENT: bool
        SHADEWEIGHTS: bool
        SHORTENBONENAMES: bool
        SHOWHIDDENVERTICES: bool
        SHOWNOENVELOPES: bool
        UPDATEONMOUSEUP: bool
        WEIGHTALLVERTICES: bool
        WEIGHTCOLORS: MXSWrapperBase
        WEIGHTTOOL_SCALE: float
        WEIGHTTOOL_TOLERANCE: float
        WEIGHTTOOL_WEIGHT: float
        WT_ACTIVEVERTEXSET: int
        WT_AFFECTSELECTED: bool
        WT_ATTRIBLABELHEIGHT: int
        WT_DRAGLEFTRIGHTMODE: bool
        WT_FLIPUI: bool
        WT_FONTSIZE: int
        WT_MARKERCOLOR: MXSWrapperBase
        WT_MARKERTYPE: int
        WT_PRECISION: float
        WT_SHORTENLABELS: bool
        WT_SHOWAFFECTEDBONES: bool
        WT_SHOWATTRIBUTES: bool
        WT_SHOWCOPYPASTEUI: bool
        WT_SHOWEXCLUSIONS: bool
        WT_SHOWGLOBAL: bool
        WT_SHOWLOCKS: bool
        WT_SHOWMARKER: bool
        WT_SHOWMENU: bool
        WT_SHOWOPTIONSUI: bool
        WT_SHOWSETUI: bool
        WT_TABLEY: int
        WT_UPDATEONMOUSEUP: bool
        WT_WINHEIGHT: int
        WT_WINWIDTH: int
        WT_WINXPOS: int
        WT_WINYPOS: int
        ...
    class SkinTools(UtilityPlugin):
        ...
    class SkinUtilities(UtilityPlugin):
        ...
    class SkinUtils(Interface):
        ...
    class SkinWrapPatch(Modifier):
        PATCH: None
        SAMPLERATE: int
        ...
    class Skin_Morph(Modifier):
        BONES: MXSWrapperBase
        BONESIZE: float
        EDGELIMIT: int
        ENABLED: bool
        FALLOFF: int
        FALLOFFGRAPHS: MXSWrapperBase
        INFLUENCEANGLE: float
        JOINTTYPE: int
        MATRIXSIZE: float
        MIRROROFFSET: float
        MIRRORPLANE: int
        MIRRORTHRESHOLD: float
        MORPHNAME: None
        PREVIEWBONE: bool
        PREVIEWVERTS: bool
        RELOADSELECTED: bool
        SAFEMODE: bool
        SELECTIONRADIUS: float
        SHOWCURRENTANGLE: bool
        SHOWDELTAS: bool
        SHOWDRIVERBONE: bool
        SHOWEDGES: bool
        SHOWLIMITANGLE: bool
        SHOWMIRRORPLANE: bool
        SHOWMORPHBONE: bool
        SHOWX: bool
        SHOWY: bool
        SHOWZ: bool
        SOFTSELECTIONGRAPH: MXSWrapperBase
        TARGETNODES: MXSWrapperBase
        USEEDGELIMIT: bool
        USESOFTSELECTION: bool
        ...
    class Skin_Wrap(Modifier):
        BLEND: bool
        BLENDDISTANCE: float
        DISTANCE: float
        ENGINE: int
        FACELIMIT: int
        FALLOFF: float
        MESH: None
        MESHLIST: MXSWrapperBase
        MIRROROFFSET: float
        MIRRORPLANE: int
        MIRRORTHRESHOLD: float
        SHOWAXIS: bool
        SHOWFACELIMIT: bool
        SHOWLOOPS: bool
        SHOWMIRRORDATA: bool
        SHOWUNASSIGNEDVERTS: bool
        SHOWVERTS: bool
        THRESHOLD: float
        WEIGHTALLVERTS: bool
        ...
    class Skin_Wrap_Patch(Modifier):
        PATCH: None
        SAMPLERATE: int
        ...
    class Skylight(Light):
        CASTSHADOWS: bool
        COLOR: MXSWrapperBase
        MULTIPLIER: float
        ON: bool
        RAYS_PER_SAMPLE: int
        RAY_BIAS: float
        SKY_COLOR_MAP: None
        SKY_COLOR_MAP_AMT: float
        SKY_COLOR_MAP_ON: bool
        SKY_MODE: int
        ...
    class SlateDragDropBridge(Interface):
        ...
    class SlaveFloat(FloatController):
        ...
    class SlaveMatrix3(Matrix3Controller):
        ...
    class SlavePoint3(Point3Controller):
        ...
    class SlavePoint4(Point4Controller):
        ...
    class SlavePos(PositionController):
        ...
    class SlaveRotation(RotationController):
        ...
    class SlaveScale(ScaleController):
        ...
    class Slave_Control(Matrix3Controller):
        ...
    class Slave_Point3(Point3Controller):
        ...
    class Slerp(Generic):
        ...
    class SliceModifier(Modifier):
        FACES___POLYGONS_TOGGLE: int
        SLICE_TYPE: int
        ...
    class SliderControl(RolloutControl):
        ...
    class SliderManip(Helper):
        ...
    class Slider_Manip(Helper):
        ...
    class SlidingDoor(GeometryClass):
        BEVEL_ANGLE: float
        BOTTOM_RAIL: float
        CREATE_FRAME: bool
        DEPTH: float
        DOOR_OFFSET: float
        DOUBLE_DOORS: int
        FLIP_HINGE: bool
        FLIP_SWING: bool
        FRAME_DEPTH: float
        FRAME_WIDTH: float
        GENERATE_MAPPING_COORDS: bool
        GLASS_THICKNESS: float
        HEIGHT: float
        LEAF_THICKNESS: float
        MUNTIN: float
        NUMBER_OF_PANELS_HORIZONTALLY: int
        NUMBER_OF_PANELS_VERTICALLY: int
        OPEN: float
        PANEL_MIDDLE_THICKNESS: float
        PANEL_THICKNESS_1: float
        PANEL_THICKNESS_2: float
        PANEL_TYPE: int
        PANEL_WIDTH_1: float
        PANEL_WIDTH_2: float
        STILES_TOP_RAIL: float
        WIDTH: float
        ...
    class SlidingWindow(GeometryClass):
        CHAMFERED_PROFILE: bool
        DEPTH: float
        FRAME_THICKNESS: float
        GENERATE_MAPPING_COORDS: bool
        GLAZING_THICKNESS: float
        HEIGHT: float
        HORIZONTAL_FRAME_WIDTH: float
        HUNG: bool
        NUMBER_OF_PANELS_HORIZONTALLY: int
        NUMBER_OF_PANELS_VERTICALLY: int
        PERCENT_OPEN: int
        RAIL_WIDTH: float
        VERTICAL_FRAME_WIDTH: float
        WIDTH: float
        ...
    class Smoke(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COORDS: MXSWrapperBase
        EXPONENT: float
        ITERATIONS: int
        MAP1: None
        MAP1ON: bool
        MAP2: None
        MAP2ON: bool
        PHASE: float
        SIZE: float
        ...
    class SmoothModifier(Modifier):
        AUTOSMOOTH: bool
        PREVENTINDIRECT: bool
        SMOOTHINGBITS: int
        THRESHOLD: float
        ...
    class Snow(GeometryClass):
        BIRTHRATE: float
        CONSTANT: bool
        DISPLAY: int
        EMITTERHEIGHT: float
        EMITTERWIDTH: float
        FLAKESIZE: float
        HIDEEMITTER: bool
        LIFE: MXSWrapperBase
        LIFETIME: MXSWrapperBase
        RENDER: int
        RENDERCOUNT: int
        SPEED: float
        START: MXSWrapperBase
        STARTTIME: MXSWrapperBase
        TUMBLE: float
        TUMBLESCALE: float
        VARIATION: float
        VIEWPORTCOUNT: int
        ...
    class SoftSelectTool(UserDataTypeClass):
        ...
    class SoftSelectionManager(TrackViewUtility):
        ...
    class Soft_Selection_Tool(UserDataTypeClass):
        ...
    class Soften(Filter):
        ...
    class SortKey(ReferenceTarget):
        ...
    class Sound(Helper):
        ...
    class SoundClass(MAXWrapper):
        ...
    class SpaceBend(SpacewarpObject):
        ...
    class SpaceCameraMap(SpacewarpModifier):
        CAMERA: None
        ...
    class SpaceConform(SpacewarpModifier):
        ...
    class SpaceFFDBox(SpacewarpObject):
        CONTINUITY: float
        DEFORMTYPE: int
        DISPLATTICE: bool
        DISPSOURCE: bool
        FALLOFF: float
        HEIGHT: float
        LENGTH: float
        TENSION: float
        WIDTH: float
        ...
    class SpaceFFDCyl(SpacewarpObject):
        CONTINUITY: float
        DEFORMTYPE: int
        DISPLATTICE: bool
        DISPSOURCE: bool
        FALLOFF: float
        HEIGHT: float
        RADIUS: float
        TENSION: float
        ...
    class SpaceNoise(SpacewarpObject):
        ...
    class SpacePatchDeform(SpacewarpModifier):
        FLIP_DEFORMATION_AXIS: int
        PLANE_TO_PATCH_DEFORM: int
        ROTATION: float
        U_PERCENT: float
        U_STRETCH: float
        V_PERCENT: float
        V_STRETCH: float
        ...
    class SpacePathDeform(SpacewarpModifier):
        AXIS: int
        FLIP_DEFORMATION_AXIS: int
        PATH: None
        PERCENT_ALONG_PATH: float
        ROTATION: float
        STRETCH: float
        TWIST: float
        ...
    class SpaceSkew(SpacewarpObject):
        DECAY: float
        HEIGHT: float
        LENGTH: float
        WIDTH: float
        ...
    class SpaceStretch(SpacewarpObject):
        DECAY: float
        HEIGHT: float
        LENGTH: float
        WIDTH: float
        ...
    class SpaceSurfDeform(SpacewarpModifier):
        FLIP_DEFORMATION_AXIS: int
        PLANE_TO_PATCH_DEFORM: int
        ROTATION: float
        SURFACE: None
        U_PERCENT: float
        U_STRETCH: float
        V_PERCENT: float
        V_STRETCH: float
        ...
    class SpaceTaper(SpacewarpObject):
        DECAY: float
        HEIGHT: float
        LENGTH: float
        WIDTH: float
        ...
    class SpaceTwist(SpacewarpObject):
        DECAY: float
        HEIGHT: float
        LENGTH: float
        WIDTH: float
        ...
    class Space_Warp_Behavior(ReferenceTarget):
        DISPLAYFORCE: bool
        FORCECOLOR: MXSWrapperBase
        NAME: str
        SPACEWARP: None
        ...
    class Spacedisplace(SpacewarpObject):
        APPLYMAP: bool
        AXIS: int
        BITMAP: None
        BLUR: float
        CAP: bool
        DECAY: float
        HEIGHT: float
        LENGTH: float
        LUMCENTER: float
        LUMCENTERENABLE: bool
        MAP: None
        MAPTYPE: int
        STRENGTH: float
        USEMAP: bool
        U_FLIP: bool
        U_TILE: float
        V_FLIP: bool
        V_TILE: float
        WIDTH: float
        W_FLIP: bool
        W_TILE: float
        ...
    class Spaceripple(SpacewarpObject):
        AMPLITUDE1: float
        AMPLITUDE2: float
        CIRCLES: int
        DECAY: float
        DIVISIONS: int
        PHASE: float
        SEGMENTS: int
        WAVELENGTH: float
        ...
    class SpacewarpModifier(MAXWrapper):
        ...
    class SpacewarpObject(Node):
        ...
    class Spacewave(SpacewarpObject):
        AMPLITUDE1: float
        AMPLITUDE2: float
        CIRCLES: int
        DECAY: float
        DIVISIONS: int
        PHASE: float
        SEGMENTS: int
        WAVELENGTH: float
        ...
    class Spawn(Helper):
        DELETE_PARENT: bool
        DIVERGENCE: float
        NUMBER_OF_OFFSPRINGS: int
        OFFSPRINGS_VARIATION: float
        RANDOM_SEED: int
        RESTART_PARTICLE_AGE: bool
        SCALE_FACTOR: float
        SCALE_VARIATION: float
        SPAWN_ABLE: float
        SPAWN_RATE: float
        SPAWN_STEP_SIZE: float
        SPAWN_TYPE: int
        SPEED: float
        SPEED_INHERITED: float
        SPEED_TYPE: int
        SPEED_VARIATION: float
        SYNC_TYPE: int
        ...
    class Speckle(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COORDS: MXSWrapperBase
        MAP1: None
        MAP1ON: bool
        MAP2: None
        MAP2ON: bool
        SIZE: float
        ...
    class Specular(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class SpeedByIcon(Helper):
        ACCEL_LIMIT: float
        COLOR_TYPE: bool
        DISTANCE: float
        ICON_SIZE: float
        INFLUENCE: float
        RANDOM_SEED: int
        SPEED_MAXIMUM: float
        SPEED_MINIMUM: float
        STEER_TOWARDS_TRAJECTORY: bool
        SYNC_TYPE_ICON_ANIMATION: int
        SYNC_TYPE_PARAM_ANIMATION: int
        USE_ICON_ORIENTATION: bool
        USE_SPEED_VARIATION: bool
        ...
    class SpeedVaryBehavior(ReferenceTarget):
        ACCELDEVIATION: float
        ACCELPERIOD: float
        CENTERSPEED: float
        NAME: str
        PERIOD: int
        PERIODDEVIATION: float
        SEED: int
        SPEEDDEVIATION: float
        ...
    class Speed_By_Surface(Helper):
        ACCELERATION_LIMIT: float
        ANIMATED_SHAPE: bool
        DIRECTION_TYPE: int
        DIVERGENCE: float
        FALLOFF: float
        MATERIAL_ID: int
        MATERIAL_TYPE: int
        RANDOM_SEED: int
        RANGE: float
        SET_SPEED_BY_SURFACE_MATERIAL: bool
        SET_SPEED_MAGNITUDE: bool
        SPEED_TYPE: int
        SPEED_VALUE: float
        SPEED_VARIATION: float
        SUBFRAME_SAMPLING: bool
        SURFACE_OBJECTS: MXSWrapperBase
        SYNC_TYPE: int
        UNLIMITED_RANGE: bool
        USE_SUB_MATERIAL: bool
        ...
    class Speed_Test(Helper):
        ANGLE_VALUE: float
        ANGLE_VARIATION: float
        CONDITION_TYPE: int
        RANDOM_SEED: int
        SYNC_TYPE: int
        TEST_TYPE: int
        UNIT_VALUE: float
        UNIT_VARIATION: float
        ...
    class Speed_Vary_Behavior(ReferenceTarget):
        ACCELDEVIATION: float
        ACCELPERIOD: float
        CENTERSPEED: float
        NAME: str
        PERIOD: int
        PERIODDEVIATION: float
        SEED: int
        SPEEDDEVIATION: float
        ...
    class Sphere(GeometryClass):
        CHOP: int
        HEMISPHERE: float
        MAPCOORDS: bool
        RADIUS: float
        RECENTER: bool
        SEGS: int
        SLICE: bool
        SLICEFROM: float
        SLICEON: bool
        SLICETO: float
        SMOOTH: bool
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS: float
        ...
    class SphereGizmo(Helper):
        HEMISPHERE: bool
        RADIUS: float
        SEED: int
        ...
    class SphericalCollision(ReferenceMaker):
        ...
    class Spherify(Modifier):
        PERCENT: float
        ...
    class SpinLimit(Helper):
        ...
    class Spindle(GeometryClass):
        BLEND: float
        CAP_HEIGHT: float
        CAP_SEGMENTS: int
        HEIGHT: float
        HEIGHT_SEGMENTS: int
        MAPCOORDS: int
        RADIUS: float
        SIDES: int
        SLICE_FROM: float
        SLICE_ON: int
        SLICE_TO: float
        SMOOTH_ON: int
        ...
    class SpineData2(ReferenceTarget):
        ...
    class SpineTrans2(Matrix3Controller):
        ...
    class SpinnerControl(RolloutControl):
        ...
    class Spiral_Stair(GeometryClass):
        CARRIAGECONTEXT: int
        CARRIAGECOUNT: int
        CARRIAGEEXTOFFS: float
        CARRIAGEHEIGHT: float
        CARRIAGEINTOFFS: float
        CARRIAGESPACE: float
        CARRIAGESPACINGTYPE: int
        CARRIAGESPRINGFLOOR: bool
        CARRIAGEWIDTH: float
        CENTERPOLEHEIGHT: float
        CENTERPOLEHEIGHT_X: bool
        CENTERPOLERADIUS: float
        CENTERPOLESEGMENTS: int
        DIRECTION: int
        GENERATECARRIAGE: bool
        GENERATECENTERPOLE: bool
        GENERATEINSIDERAILING: bool
        GENERATEMAPPING: bool
        GENERATEOUTSIDERAILING: bool
        GENERATESTRINGERS: bool
        RADIUS: float
        RAILINGHEIGHT: float
        RAILINGOFFS: float
        RAILINGRADIUS: float
        RAILINGSEGMENTS: int
        REVOLUTIONS: float
        STEPCOUNT: int
        STEPDEPTH: float
        STEPDEPTH_X: bool
        STEPHEIGHT: float
        STEPSEGMENTS: int
        STEPSEGMENTS_X: bool
        STEPTHICKNESS: float
        STEPTYPE: int
        STEPWIDTH: float
        STRINGERDEPTH: float
        STRINGEROFFSET: float
        STRINGERSPRINGFLOOR: bool
        STRINGERWIDTH: float
        ...
    class Splat(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COORDS: MXSWrapperBase
        ITERATIONS: int
        MAP1: None
        MAP1ON: bool
        MAP2: None
        MAP2ON: bool
        SIZE: float
        THRESHOLD: float
        ...
    class SplineIKChain(Matrix3Controller):
        ...
    class SplineIKSolver(IKSolver):
        ...
    class SplineInfluence(Modifier):
        BIAS: float
        BIASSELECTED: bool
        CONVERTSELECTIONS: bool
        ENABLEBIAS: bool
        EXISTINGSELECTION: int
        FALLOFFKNOTS: int
        FALLOFFMETHOD: int
        FALLOFFPERCENT: float
        FALLOFFTYPE: int
        FARINFLUENCE: float
        INFLUENCENODES: MXSWrapperBase
        INVERT: bool
        NEARINFLUENCE: float
        SELECTIONFALLOFFTYPE: int
        SHOWKNOTS: bool
        ...
    class SplineMirror(Modifier):
        AXIS: int
        FLIP: bool
        SHOWKNOTS: bool
        SLICE: bool
        TANGENTS: bool
        THRESHOLD: float
        WELD: bool
        ...
    class SplineMorph(Modifier):
        AMOUNT: float
        INVERT: bool
        MORPHMETHOD: int
        SHOWKNOTS: bool
        TARGET10: None
        TARGET1: None
        TARGET2: None
        TARGET3: None
        TARGET4: None
        TARGET5: None
        TARGET6: None
        TARGET7: None
        TARGET8: None
        TARGET9: None
        TARGETON10: bool
        TARGETON1: bool
        TARGETON2: bool
        TARGETON3: bool
        TARGETON4: bool
        TARGETON5: bool
        TARGETON6: bool
        TARGETON7: bool
        TARGETON8: bool
        TARGETON9: bool
        TARGETWEIGHT10: float
        TARGETWEIGHT1: float
        TARGETWEIGHT2: float
        TARGETWEIGHT3: float
        TARGETWEIGHT4: float
        TARGETWEIGHT5: float
        TARGETWEIGHT6: float
        TARGETWEIGHT7: float
        TARGETWEIGHT8: float
        TARGETWEIGHT9: float
        USE_SOFTSELECTION: bool
        ...
    class SplineOverlap(Modifier):
        DRAPE: float
        SHOWKNOTS: bool
        THICKNESS: float
        USENORMALS: bool
        USESELECTION: bool
        ...
    class SplineRelax(Modifier):
        AMOUNT: float
        ITERATIONS: int
        KNOTS: bool
        SHOWKNOTS: bool
        TANGENTS: bool
        USESELECTION: bool
        ...
    class SplineSelect(Modifier):
        ...
    class SplineShape(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        MAPCOORDS: bool
        OPTIMIZE: bool
        QUAD_CAP: bool
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        ...
    class Spline_Chamfer(Modifier):
        AMOUNT: float
        BIAS: float
        CORNERKNOTSONLY: bool
        DEPTH: float
        LIMITEFFECT: bool
        MINANGLE: float
        SHOWKNOTS: bool
        USEMINANGLE: bool
        USESELECTION: bool
        ...
    class Spline_IK_Control(Modifier):
        BOX: bool
        CONSTANTSCREENSIZE: bool
        DRAWONTOP: bool
        HELPER_AXISTRIPOD: bool
        HELPER_CENTERMARKER: bool
        HELPER_CROSS: bool
        HELPER_LIST: MXSWrapperBase
        HELPER_SIZE: float
        LINKTYPES: int
        ...
    class Split_Amount(Helper):
        EVERY_NTH: int
        FIRST_N: int
        PER_EMISSION_SOURCE: bool
        RANDOM_SEED: int
        RATIO: float
        TEST_TYPE: int
        ...
    class Split_Group(Helper):
        CONDITION_TYPE: int
        GROUP_SELECTION_OPERATOR: None
        GROUP_SELECTION_OPERATORS: MXSWrapperBase
        INDEX_OFFSET: int
        MULTIPLIER: float
        PROXY_PARTICLE_SYSTEM: None
        USE_PROXY_PARTICLES: bool
        ...
    class Split_Selected(Helper):
        CONDITION_TYPE: int
        ...
    class Split_Source(Helper):
        CONDITION_TYPE: int
        SELECTED_SOURCES: MXSWrapperBase
        ...
    class Spray(GeometryClass):
        BIRTHRATE: float
        CONSTANT: bool
        DISPLAY: int
        DROPSIZE: float
        EMITTERHEIGHT: float
        EMITTERWIDTH: float
        HIDEEMITTER: bool
        LIFE: MXSWrapperBase
        LIFETIME: MXSWrapperBase
        RENDER: int
        RENDERCOUNT: int
        SPEED: float
        START: MXSWrapperBase
        STARTTIME: MXSWrapperBase
        VARIATION: float
        VIEWPORTCOUNT: int
        ...
    class SprayBirth(Helper):
        ACQUIRE_SELECTION: bool
        DURATION: int
        EMIT_START: int
        EMIT_STOP: int
        EMIT_TYPE: int
        LOCK_POSITION: bool
        LOCK_ROTATION: bool
        PARTICLE_PAINT_HELPER: None
        SELECTION_TYPE: int
        SUBFRAME_SAMPLING: bool
        ...
    class SprayCursor(GeometryClass):
        ...
    class SprayMaster(Helper):
        ACQUIRE_SUB_MATERIAL_INDEX: bool
        ADJUST_GLOBAL_TIMING: bool
        ASSIGN_TO_MAPPING_CHANNELS: MXSWrapperBase
        AUTOADJUST_CURRENT_FRAME: bool
        AUTO_SYNC_TIMING_BY_SELECTED_STROKE: bool
        DENSITY_CENTER: float
        DENSITY_SIDES: float
        DISPLAY_SIZE: float
        DISPLAY_TYPE: int
        DISTANCE: float
        DISTANCE_VARIATION: float
        DIVERGENCE_FOR_X_AXIS: float
        DIVERGENCE_FOR_Z_AXIS: float
        EDITING_ADJUST_GLOBAL_TIMING: bool
        EDITING_DURATION: int
        EDITING_START_AT: int
        EDITING_STOP_AT: int
        EDITING_STOP_TYPE: int
        GENERATE_MAPPING: bool
        GENERATE_ROTATION: bool
        ICON_SIZE: float
        INCLUDE_MASK_CHILDREN: bool
        INCLUDE_MASK_GROUP_MEMBERS: bool
        INCLUDE_SPRAY_CHILDREN: bool
        INCLUDE_SPRAY_GROUP_MEMBERS: bool
        JET_DURATION: int
        JET_START_TIME: int
        JET_START_TYPE: int
        JET_STOP_TIME: int
        JET_STOP_TYPE: int
        LATE_COLOR: MXSWrapperBase
        LOCATION_TYPE: int
        MAPPING_END_VALUE: float
        MAPPING_OFFSET_VALUE_PER_DROP: float
        MAPPING_OFFSET_VALUE_PER_SECOND: float
        MAPPING_START_VALUE: float
        MAPPING_TYPE: int
        MASKS: MXSWrapperBase
        MAXIMUM_NUMBER_OF_ATTEMPTS: int
        OBJECTS_ANIMATED_SURFACE: bool
        ORIENTATION_TYPE_FOR_X_AXIS: int
        ORIENTATION_TYPE_FOR_Z_AXIS: int
        PER_JET_LIMIT: int
        PRIORITY_AXIS: int
        RANDOM_SEED: int
        RATE_DROPS_PER_JET: int
        RATE_DROPS_PER_LENGTH_UNIT: float
        RATE_DROPS_PER_SECOND: float
        RATE_TYPE: int
        REVERSE_X_AXIS: bool
        REVERSE_Z_AXIS: bool
        SELECTED_STROKES: MXSWrapperBase
        SELECTION_FILTER_TYPE: int
        SEPARATION_DISTANCE: float
        SHOW_PARTICLE_TIMING: bool
        SPRAY_AT_OBJECTS: MXSWrapperBase
        SPRAY_AT_TYPE: int
        SPRAY_RADIUS: float
        SPRAY_RADIUS_GRAPH: None
        SPRAY_RADIUS_RATE: None
        STACK_UP_FOR_SEPARATION: bool
        TIME_SCALE: float
        USE_MASK_OBJECTS: bool
        USE_RADIUS_GRAPH: bool
        USE_RATE_GRAPH: bool
        USE_SEPARATION: bool
        ...
    class SprayPlacement(Helper):
        ACQUIRE_PAINT_MAPPING: bool
        ACQUIRE_PAINT_MATERIALID: bool
        ACQUIRE_PAINT_POSITION: bool
        ACQUIRE_PAINT_ROTATION: bool
        ACQUIRE_PAINT_SELECTION: bool
        BLENDIN_ROTATION: bool
        FAR_DISTANCE: float
        NEAR_DISTANCE: float
        OBEY_QUANTITY_MULTIPLIER: bool
        ORDER_TYPE: int
        PARTICLE_PAINT_HELPER: None
        POSITION_TYPE: int
        RANDOM_SEED: int
        SELECTION_TYPE: int
        SEPARATE_STREAMS_INDEXING: bool
        SNAP_DISTANCE: float
        SNAP_IF_CLOSE: bool
        STOP_IF_COUNT_OVERFLOW: bool
        UPDATE_TYPE: int
        ...
    class Spring(GeometryClass):
        DIAMETER: float
        DYNAMICS_K_CONSTANT_UNITS: int
        DYNAMICS_K_CONSTANT_VALUE: float
        DYNAMICS_SPRING_DIRECTION: int
        DYNAMICS_SPRING_RELAXED_HEIGHT: float
        D_SECTION_ROUND_SIDES: int
        D_SECTION_WIRE_DEPTH: float
        D_SECTION_WIRE_FILLET_SIDES: int
        D_SECTION_WIRE_FILLET_SIZE: float
        D_SECTION_WIRE_ROTATION_ANGLE: float
        D_SECTION_WIRE_WIDTH: float
        ENABLE_NONLINEARITY: int
        END_PLACEMENT_METHOD: int
        FREE_SPRING_HEIGHT: float
        GENERATE_MAPPING_COORDINATES: int
        NUMBER_OF_TURNS: float
        RECTANGULAR_FILLET_SIDES: int
        RECTANGULAR_WIRE_DEPTH: float
        RECTANGULAR_WIRE_FILLET_SIZE: float
        RECTANGULAR_WIRE_ROTATION_ANGLE: float
        RECTANGULAR_WIRE_WIDTH: float
        RENDERABLE_SPRING: int
        ROUND_WIRE_DIAMETER: float
        ROUND_WIRE_SIDE_COUNT: int
        SEGMENTATION_METHOD: int
        SEGMENTS_ALONG_TURN: int
        SEGMENTS_PER_TURN: int
        SMOOTH_SPRING: int
        TURN_DIRECTION: int
        WIRE: int
        ...
    class SpringPoint3Controller(Point3Controller):
        EFFECTHOW: int
        FORCENODE: MXSWrapperBase
        START: int
        STEPS: int
        X_EFFECT: float
        Y_EFFECT: float
        Z_EFFECT: float
        ...
    class SpringPositionController(PositionController):
        EFFECTHOW: int
        FORCENODE: MXSWrapperBase
        START: int
        STEPS: int
        X_EFFECT: float
        Y_EFFECT: float
        Z_EFFECT: float
        ...
    class Squad(Generic):
        ...
    class Squeeze(Modifier):
        BIAS: float
        BULGE_AMOUNT: float
        BULGE_CURVITURE: float
        LIMIT_SQUEEZE_EFFECTS: int
        SQUEEZE_AMOUNT: float
        SQUEEZE_CURVATURE: float
        SQUEEZE_LOWER_LIMIT: float
        SQUEEZE_UPPER_LIMIT: float
        VOLUME: float
        ...
    class StPathClass(Shape):
        ...
    class StackPerformance(Interface):
        ...
    class StandardMaterialClass(Value):
        ...
    class StandardTextureOutput(TexOutputClass):
        ALPHAFROMRGB: bool
        BUMP_AMOUNT: float
        CLAMP: bool
        INVERT: bool
        OUTPUT_AMOUNT: float
        RGB_LEVEL: float
        RGB_OFFSET: float
        ...
    class StandardUVGen(UVGenClass):
        BLUR: float
        BLUR_OFFSET: float
        MAPCHANNEL: int
        MAPPING: int
        MAPPINGTYPE: int
        NOISE_AMOUNT: float
        NOISE_ANIMATE: bool
        NOISE_LEVELS: int
        NOISE_ON: bool
        NOISE_SIZE: float
        PHASE: float
        REALWORLDHEIGHT: float
        REALWORLDSCALE: bool
        REALWORLDWIDTH: float
        SHOWMAPONBACK: bool
        UVTRANSFORM: MXSWrapperBase
        UVW_TYPE: int
        U_ANGLE: float
        U_MIRROR: bool
        U_OFFSET: float
        U_TILE: bool
        U_TILING: float
        V_ANGLE: float
        V_MIRROR: bool
        V_OFFSET: float
        V_TILE: bool
        V_TILING: float
        W_ANGLE: float
        ...
    class StandardXYZGen(XYZGenClass):
        ANGLE: MXSWrapperBase
        BLUR: float
        BLUR_OFFSET: float
        COORDTYPE: int
        MAPCHANNEL: int
        OFFSET: MXSWrapperBase
        TILING: MXSWrapperBase
        ...
    class Standard_16_Bit(BitmapStorageClass):
        ...
    class Standard_16_Bit_Grayscale(BitmapStorageClass):
        ...
    class Standard_1_Bit(BitmapStorageClass):
        ...
    class Standard_24_Bit_LogLUV_Storage(BitmapStorageClass):
        ...
    class Standard_24_Bit_LogLUV_Storage_With_Alpha(BitmapStorageClass):
        ...
    class Standard_32_Bit(BitmapStorageClass):
        ...
    class Standard_32_Bit_Floating_Point_Storage(BitmapStorageClass):
        ...
    class Standard_32_Bit_Floating_Point_Storage_Grayscale(BitmapStorageClass):
        ...
    class Standard_32_Bit_LogLUV_Storage(BitmapStorageClass):
        ...
    class Standard_32_Bit_RealPixel_Storage(BitmapStorageClass):
        ...
    class Standard_64_Bit_Storage(BitmapStorageClass):
        ...
    class Standard_8_Bit_Grayscale(BitmapStorageClass):
        ...
    class Standard_8_Bit_Paletted(BitmapStorageClass):
        ...
    class Standard_Flow(ReferenceTarget):
        ...
    class Standardmaterial(Material):
        ADTEXTURELOCK: bool
        APPLYREFLECTIONDIMMING: bool
        DIMLEVEL: float
        FACEMAP: bool
        FACETED: bool
        FILTERCOLOR: MXSWrapperBase
        FILTERMAP: None
        IOR: float
        MAPAMOUNTS: MXSWrapperBase
        MAPENABLES: MXSWrapperBase
        MAPS: MXSWrapperBase
        OPACITY: float
        OPACITYFALLOFF: float
        OPACITYFALLOFFTYPE: int
        OPACITYTYPE: int
        REFLECTIONLEVEL: float
        SAMPLER: int
        SAMPLERADAPTON: bool
        SAMPLERADAPTTHRESHOLD: float
        SAMPLERADVANCEDOPTIONS: bool
        SAMPLERBYNAME: str
        SAMPLERENABLE: bool
        SAMPLERQUALITY: float
        SAMPLERUSEGLOBAL: bool
        SHADERBYNAME: str
        SHADERTYPE: int
        SUBSAMPLETEXTUREON: bool
        TWOSIDED: bool
        USERPARAM0: float
        USERPARAM1: float
        WIRE: bool
        WIRESIZE: float
        WIREUNITS: int
        ...
    class Standin_For_Missing_MultiPass_Camera_Effect_Plugin(MPassCamEffect):
        ...
    class Star(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        DISTORT: float
        FILLET1: float
        FILLET2: float
        MAPCOORDS: bool
        NUMPOINTS: int
        OPTIMIZE: bool
        POINTS: int
        QUAD_CAP: bool
        RADIUS1: float
        RADIUS2: float
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        ...
    class Star_Element(ReferenceTarget):
        ALPHA: int
        ANGLE: float
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        APPLYLIGHTS: bool
        APPLYNOISE: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        CENTERCOLOR: MXSWrapperBase
        CENTERSECTIONCOLOR: MXSWrapperBase
        CIRCULARCOLORMIX: float
        CIRCULARMAP: None
        CIRCULARMTL: None
        COLORSOURCE: float
        EDGECOLOR: MXSWrapperBase
        EFFECTSID: int
        ELEMENTNAME: str
        FILTERALL: bool
        FILTERBRIGHTNESS: bool
        FILTEREDGE: bool
        FILTERHUE: bool
        FILTERPERIMETER: bool
        FILTERPERIMETERALPHA: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        INTENSITY: float
        LEFTSECTIONCOLOR: MXSWrapperBase
        NOISEMAP: None
        OBJECTID: int
        OBJECTSHIDE: bool
        OCCLUSION: float
        ON: bool
        QUANTITY: int
        RADIALDENSITY: None
        RADIALMAP: None
        RADIALMTL: None
        RADIALSIZEMAP: None
        RIGHTSECTIONCOLOR: MXSWrapperBase
        SHARP: float
        SIZE: float
        SOURCEALPHA: bool
        SOURCEEFFECTSID: bool
        SOURCEOBJECTID: bool
        SOURCESURFACENORMAL: bool
        SOURCEUNCLAMPEDCOLOR: bool
        SOURCEWHOLE: bool
        SOURCEZBUFFER: bool
        SQUEEZE: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        TAPER: float
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        USECIRCULARMAP: bool
        USECIRCULARMTL: bool
        USERADIALDENSITY: bool
        USERADIALMAP: bool
        USERADIALMTL: bool
        USERADIALSIZEMAP: bool
        WIDTH: float
        ZHI: float
        ZLO: float
        ...
    class Stars(VideoPostFilter):
        ...
    class StartupTemplateManager(Interface):
        ...
    class StateCreator(ReferenceTarget):
        ...
    class StaticMethodInterface(Value):
        ...
    class StdDualVS(ReferenceMaker):
        ...
    class StdShadowGen(Shadow):
        AA_THRESHOLD: MXSWrapperBase
        BLUR: float
        COPLANAR_THRESHOLD: float
        JITTER_AMT: float
        NOAREASHADOWS: bool
        PASS1: int
        PASS2: int
        RAY_BIAS: float
        SHADOW_MODE: int
        SHADOW_TRANSPARENT: bool
        SKIP_COPLANAR: bool
        SUPPRESS_MAT_AA: bool
        SUPPRESS_REFLT_AA: bool
        TWOSIDEDSHADOWS: bool
        ...
    class SteeringWheelsOps(Interface):
        ...
    class StepShape(FloatController):
        ...
    class StereoFragment(GraphicsFragmentPlugin):
        ...
    class StopCreating(Primitive):
        ...
    class Stop_Gradually(Helper):
        POSITION: MXSWrapperBase
        RANDOM_SEED: int
        ROTATION: MXSWrapperBase
        SLOW_DOWN_START_TIME: int
        START_TIME_VARIATION: int
        STOP_TIME: int
        STOP_TIME_VARIATION: int
        STOP_TYPE: int
        TIMING_START_TYPE: int
        USE_DIFFERENT_TYPES: bool
        ...
    class Straight_Stair(GeometryClass):
        CARRIAGECONTEXT: int
        CARRIAGECOUNT: int
        CARRIAGEEXTOFFS: float
        CARRIAGEHEIGHT: float
        CARRIAGEINTOFFS: float
        CARRIAGESPACE: float
        CARRIAGESPACINGTYPE: int
        CARRIAGESPRINGFLOOR: bool
        CARRIAGEWIDTH: float
        GENERATECARRIAGE: bool
        GENERATEINSIDERAILING: bool
        GENERATEMAPPING: bool
        GENERATEOUTSIDERAILING: bool
        GENERATESTRINGERS: bool
        LENGTH: float
        RAILINGHEIGHT: float
        RAILINGOFFS: float
        RAILINGRADIUS: float
        RAILINGSEGMENTS: int
        STEPCOUNT: int
        STEPDEPTH: float
        STEPDEPTH_X: bool
        STEPHEIGHT: float
        STEPTHICKNESS: float
        STEPTYPE: int
        STEPWIDTH: float
        STRINGERDEPTH: float
        STRINGEROFFSET: float
        STRINGERSPRINGFLOOR: bool
        STRINGERWIDTH: float
        ...
    class Strauss(Shader):
        ...
    class Streak_Element(ReferenceTarget):
        ALPHA: int
        ANGLE: float
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        APPLYLIGHTS: bool
        APPLYNOISE: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        CENTERCOLOR: MXSWrapperBase
        CIRCULARCOLORMIX: float
        CIRCULARMAP: None
        CIRCULARMTL: None
        COLORSOURCE: float
        EDGECOLOR: MXSWrapperBase
        EFFECTSID: int
        ELEMENTNAME: str
        FILTERALL: bool
        FILTERBRIGHTNESS: bool
        FILTEREDGE: bool
        FILTERHUE: bool
        FILTERPERIMETER: bool
        FILTERPERIMETERALPHA: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        INTENSITY: float
        NOISEMAP: None
        OBJECTID: int
        OBJECTSHIDE: bool
        OCCLUSION: float
        ON: bool
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        RADIALDENSITY: None
        RADIALMAP: None
        RADIALMTL: None
        RADIALSIZEMAP: None
        SHARP: float
        SIZE: float
        SOURCEALPHA: bool
        SOURCEEFFECTSID: bool
        SOURCEOBJECTID: bool
        SOURCESURFACENORMAL: bool
        SOURCEUNCLAMPEDCOLOR: bool
        SOURCEWHOLE: bool
        SOURCEZBUFFER: bool
        SQUEEZE: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        TAPER: float
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        USECIRCULARMAP: bool
        USECIRCULARMTL: bool
        USERADIALDENSITY: bool
        USERADIALMAP: bool
        USERADIALMTL: bool
        USERADIALSIZEMAP: bool
        WIDTH: float
        ZHI: float
        ZLO: float
        ...
    class Stretch(Modifier):
        AMPLIFY: float
        AXIS: int
        FROM: float
        LIMIT: int
        STRETCH: float
        TO: float
        ...
    class StringPacket(ReferenceMaker):
        ...
    class StringStream(Value):
        ...
    class Strokes(UtilityPlugin):
        ...
    class StructDef(Value):
        ...
    class Stucco(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COORDS: MXSWrapperBase
        MAP1: None
        MAP1ON: bool
        MAP2: None
        MAP2ON: bool
        SIZE: float
        THICKNESS: float
        THRESHOLD: float
        ...
    class SubstManager(Interface):
        ...
    class Substance(TextureMap):
        COORDS: MXSWrapperBase
        GLOBALMODESCALE: int
        GLOBALTEXTUREHEIGHT: int
        GLOBALTEXTUREWIDTH: int
        LOCALABSOLUTETEXTUREHEIGHT: int
        LOCALABSOLUTETEXTUREWIDTH: int
        LOCALMODE: int
        LOCALRELATIVETEXTUREHEIGHT: int
        LOCALRELATIVETEXTUREWIDTH: int
        LOCKASPECTRATIO: int
        ROLLOUTSTATES: int
        SUBSTANCEFILENAME: str
        ...
    class Substance2(TextureMap):
        EXPORTPRESETFILEPATH: str
        IMPORTPRESETFILEPATH: str
        SUBSTANCEFILEPATH: str
        ...
    class Substance2MenuManager(GlobalUtilityPlugin):
        ...
    class Substance2Output(TextureMap):
        ...
    class SubstanceOutput(TextureMap):
        ...
    class SubstancePBWrapper(ReferenceTarget):
        ...
    class SubstanceTexWrapper(ReferenceTarget):
        ...
    class SubstanceTexture(TextureMap):
        COORDS: MXSWrapperBase
        GLOBALMODESCALE: int
        GLOBALTEXTUREHEIGHT: int
        GLOBALTEXTUREWIDTH: int
        LOCALABSOLUTETEXTUREHEIGHT: int
        LOCALABSOLUTETEXTUREWIDTH: int
        LOCALMODE: int
        LOCALRELATIVETEXTUREHEIGHT: int
        LOCALRELATIVETEXTUREWIDTH: int
        LOCKASPECTRATIO: int
        ROLLOUTSTATES: int
        SUBSTANCEFILENAME: str
        ...
    class Substance_Output(TextureMap):
        ...
    class Substituion_Offset_Transform(Matrix3Controller):
        ...
    class Substitute(Modifier):
        DISPLAYINRENDER: bool
        DISPLAYINVIEWPORT: bool
        MOVECOPYINSTANCE: int
        OBJECTNAME: str
        OBJECTREFERENCE: None
        RETAINLOCALROTATION: bool
        RETAINLOCALSCALE: bool
        RETAINPOSITION: bool
        SUBSTITUTETYPE: str
        ...
    class SubstituteMod(Modifier):
        DISPLAYINRENDER: bool
        DISPLAYINVIEWPORT: bool
        MOVECOPYINSTANCE: int
        OBJECTNAME: str
        OBJECTREFERENCE: None
        RETAINLOCALROTATION: bool
        RETAINLOCALSCALE: bool
        RETAINPOSITION: bool
        SUBSTITUTETYPE: str
        ...
    class SubstituteObject(Helper):
        ...
    class Substitute_Manager(UtilityPlugin):
        ...
    class Substitute_Object(Helper):
        ...
    class Summed_Area(BitmapFilterClass):
        ...
    class SunPositioner(Light):
        ALTITUDE_DEG: float
        AZIMUTH_DEG: float
        COMPASS_RADIUS: float
        DAY: int
        DST: bool
        DST_END_DAY: int
        DST_END_MONTH: int
        DST_START_DAY: int
        DST_START_MONTH: int
        DST_USE_DATE_RANGE: bool
        HOURS: int
        JULIAN_DAY: int
        LATITUDE_DEG: float
        LOCATION: str
        LONGITUDE_DEG: float
        MANUAL_SUN_POSITION: MXSWrapperBase
        MINUTES: int
        MODE: int
        MONTH: int
        NORTH_DIRECTION_DEG: float
        SHOW_COMPASS: bool
        SUN_DISTANCE: float
        TIME_IN_SECONDS: int
        TIME_ZONE: float
        WEATHER_FILE: str
        YEAR: int
        ...
    class Sun_Positioner(Light):
        ALTITUDE_DEG: float
        AZIMUTH_DEG: float
        COMPASS_RADIUS: float
        DAY: int
        DST: bool
        DST_END_DAY: int
        DST_END_MONTH: int
        DST_START_DAY: int
        DST_START_MONTH: int
        DST_USE_DATE_RANGE: bool
        HOURS: int
        JULIAN_DAY: int
        LATITUDE_DEG: float
        LOCATION: str
        LONGITUDE_DEG: float
        MANUAL_SUN_POSITION: MXSWrapperBase
        MINUTES: int
        MODE: int
        MONTH: int
        NORTH_DIRECTION_DEG: float
        SHOW_COMPASS: bool
        SUN_DISTANCE: float
        TIME_IN_SECONDS: int
        TIME_ZONE: float
        WEATHER_FILE: str
        YEAR: int
        ...
    class Sunlight(System):
        ...
    class Sunlight_Daylight_Slave_Controller(Matrix3Controller):
        ...
    class Sunlight_Daylight_Slave_ControllerMatrix3Controller(Matrix3Controller):
        ...
    class Sunlight_Daylight_Slave_Intensity_Controller(FloatController):
        ...
    class Sunlight_Daylight_Slave_Intensity_ControllerFloatController(FloatController):
        ...
    class Sunlight_Slave_Controller(Matrix3Controller):
        ...
    class Sunlight_Slave_Intensity_Controller(FloatController):
        ...
    class SuperSpray(GeometryClass):
        AXIS_SPREAD: float
        BIRTH_RATE: int
        BLUR_STRETCH: int
        BUBBLE_AMPLITUDE: float
        BUBBLE_AMPLITUDE_VARIATION: float
        BUBBLE_PERIOD: MXSWrapperBase
        BUBBLE_PERIOD_VARIATION: float
        BUBBLE_PHASE: float
        BUBBLE_PHASE_VARIATION: float
        DIE__X_FRAMES_AFTER_COLLISION: MXSWrapperBase
        DIE__X_FRAMES_AFTER_COLLISION_VARIATION: float
        DISPLAY_UNTIL: MXSWrapperBase
        EMITTER_START: MXSWrapperBase
        EMITTER_STOP: MXSWrapperBase
        FADE_TIME: MXSWrapperBase
        GROWTH_TIME: MXSWrapperBase
        ICONHIDDEN: bool
        ICONSIZE: float
        INSTANCEFRAMEOFFSET: int
        INSTANCEKEYOFFSETTYPE: int
        INSTANCESUBTREE: bool
        INSTANCINGOBJECT: None
        INTERPARTICLE_COLLISIONS_ON: int
        INTERPARTICLE_COLLISION_BOUNCE: float
        INTERPARTICLE_COLLISION_BOUNCE_VARIATION: float
        INTERPARTICLE_COLLISION_STEPS: int
        LIFE: MXSWrapperBase
        LIFESPANVALUEQUEUE: MXSWrapperBase
        LIFE_VARIATION: MXSWrapperBase
        MAPPINGTYPE: int
        MAPPING_DISTANCE_BASE: float
        MAPPING_TIME_BASE: MXSWrapperBase
        METABALLAUTOCOARSNESS: bool
        METABALLRENDERCOARSNESS: float
        METABALLVIEWCOARSNESS: float
        METAPARTICLE_TENSION: float
        METAPARTICLE_TENSION_VARIATION: float
        MOTIONINFLUENCE: float
        MOTIONMULTIPLIER: float
        MOTIONVARIATION: float
        OBJECTMUTATIONQUEUE: MXSWrapperBase
        OFF_AXIS: float
        OFF_PLANE: float
        PARTICLETYPE: int
        PLANE_SPREAD: float
        QUANTITYMETHOD: int
        SEED: int
        SIZE: float
        SIZE_VARIATION: float
        SPAWNINHERITVELOCITY: bool
        SPAWNSCALEFIXED: bool
        SPAWNSCALETYPE: int
        SPAWNSPEEDFIXED: bool
        SPAWNSPEEDTYPE: int
        SPAWNTYPE: int
        SPAWN_AFFECTS: int
        SPAWN_DIRECTION_CHAOS: float
        SPAWN_MULTIPLIER_VARIATION: float
        SPAWN_SCALE_CHAOS: float
        SPAWN_SPEED_CHAOS: float
        SPEED: float
        SPEED_VARIATION: float
        SPINAXISTYPE: int
        SPIN_AXIS_VARIATION: float
        SPIN_PHASE: float
        SPIN_PHASE_VARIATION: float
        SPIN_TIME: MXSWrapperBase
        SPIN_TIME_VARIATION: float
        STANDARDPARTICLE: int
        SUBSAMPLECREATIONTIME: bool
        SUBSAMPLEEMITTERROTATION: bool
        SUBSAMPLEEMITTERTRANSLATION: bool
        TOTAL_NUMBER: int
        VIEWPERCENT: float
        VIEWTYPE: int
        X_SPIN_VECTOR: float
        Y_SPIN_VECTOR: float
        Z_SPIN_VECTOR: float
        ...
    class SurfDeform(Modifier):
        FLIP_DEFORMATION_AXIS: int
        PLANE_TO_PATCH_DEFORM: int
        ROTATION: float
        SURFACE: None
        U_PERCENT: float
        U_STRETCH: float
        V_PERCENT: float
        V_STRETCH: float
        ...
    class SurfaceArriveBehavior(ReferenceTarget):
        DESCENTSTART: float
        DESCENTSTARTDEVIATION: float
        DISABLEAFTERARRIVING: bool
        DISPLAYOFFSET: bool
        DISPLAYTARGET: bool
        DISTANCE: float
        DISTANCEDEVIATION: float
        EVERYFRAME: bool
        FACING: bool
        HEIGHT: float
        HEIGHTDEVIATION: float
        NAME: str
        OFFSET: float
        RANDOM_CLOSEST: int
        RATE: float
        RATEDEVIATION: float
        SEED: int
        SPEED: float
        SPEEDDEVIATION: float
        SURFACES: MXSWrapperBase
        TARGETCOLOR: MXSWrapperBase
        TARGETSCALE: float
        USENORMAL: bool
        XNORMAL: float
        YNORMAL: float
        ZNORMAL: float
        ...
    class SurfaceFilterFn(MAXScriptFunction):
        ...
    class SurfaceFollowBehavior(ReferenceTarget):
        DISPLAYOFFSET: bool
        DISPLAYTARGET: bool
        NAME: str
        OFFSET: float
        SURFACES: MXSWrapperBase
        TARGETCOLOR: MXSWrapperBase
        TARGETSCALE: float
        USEPROJECTION: bool
        XVECTOR: float
        YVECTOR: float
        ZVECTOR: float
        ...
    class Surface_Approximation(UtilityPlugin):
        ...
    class Surface_Arrive_Behavior(ReferenceTarget):
        DESCENTSTART: float
        DESCENTSTARTDEVIATION: float
        DISABLEAFTERARRIVING: bool
        DISPLAYOFFSET: bool
        DISPLAYTARGET: bool
        DISTANCE: float
        DISTANCEDEVIATION: float
        EVERYFRAME: bool
        FACING: bool
        HEIGHT: float
        HEIGHTDEVIATION: float
        NAME: str
        OFFSET: float
        RANDOM_CLOSEST: int
        RATE: float
        RATEDEVIATION: float
        SEED: int
        SPEED: float
        SPEEDDEVIATION: float
        SURFACES: MXSWrapperBase
        TARGETCOLOR: MXSWrapperBase
        TARGETSCALE: float
        USENORMAL: bool
        XNORMAL: float
        YNORMAL: float
        ZNORMAL: float
        ...
    class Surface_Follow_Behavior(ReferenceTarget):
        DISPLAYOFFSET: bool
        DISPLAYTARGET: bool
        NAME: str
        OFFSET: float
        SURFACES: MXSWrapperBase
        TARGETCOLOR: MXSWrapperBase
        TARGETSCALE: float
        USEPROJECTION: bool
        XVECTOR: float
        YVECTOR: float
        ZVECTOR: float
        ...
    class Surface_Mapper(SpacewarpModifier):
        ...
    class Surface_Position(PositionController):
        ALIGN: int
        FLIP: bool
        SURFACE: None
        ...
    class SuspendEditing(Primitive):
        ...
    class SvfExporter(ExporterPlugin):
        ...
    class Switch(ReferenceTarget):
        ACTIVE_INPUT: int
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        INPUT_7: None
        INPUT_8: None
        RENDER_VIEWPORT_SWITCH: bool
        TYPE: int
        ...
    class System(Node):
        ...
    class TIF(BitmapIO):
        ...
    class TVDummyControl(Matrix3Controller):
        ...
    class TVNode(ReferenceTarget):
        ...
    class TailData2(ReferenceTarget):
        ...
    class TailTrans(Matrix3Controller):
        ...
    class Tape(Helper):
        LENGTH: float
        ...
    class Taper(Modifier):
        AMOUNT: float
        CURVE: float
        EFFECTAXIS: int
        LIMIT: bool
        LOWERLIMIT: float
        PRIMARYAXIS: int
        SYMMETRY: bool
        UPPERLIMIT: float
        ...
    class Targa(BitmapIO):
        ...
    class TargetDirectionallight(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ASPECT: float
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        ATTENDECAY: int
        CASTSHADOWS: bool
        COLOR: MXSWrapperBase
        CONESHAPE: int
        CONTRAST: float
        DECAYRADIUS: float
        ENABLED: bool
        EXCLUDELIST: MXSWrapperBase
        FALLOFF: float
        FARATTENEND: float
        FARATTENSTART: float
        HOTSPOT: float
        HSV: MXSWrapperBase
        HUE: int
        INCLEXCLTYPE: int
        INCLUDELIST: None
        LIGHTAFFECTSSHADOW: bool
        LIGHTSHAPE: int
        MULTIPLIER: float
        NEARATTENEND: float
        NEARATTENSTART: float
        ON: bool
        OVERSHOOT: bool
        PROJECTOR: bool
        PROJECTORMAP: None
        RAYTRACEDSHADOWS: bool
        RGB: MXSWrapperBase
        SATURATION: int
        SHADOWCOLOR: MXSWrapperBase
        SHADOWGENERATOR: MXSWrapperBase
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHOWCONE: bool
        SHOWFARATTEN: bool
        SHOWNEARATTEN: bool
        SOFTENDIFFUSEEDGE: float
        TYPE: MXSWrapperBase
        USEFARATTEN: bool
        USEGLOBALSHADOWSETTINGS: bool
        USENEARATTEN: bool
        USESHADOWPROJECTORMAP: bool
        VALUE: int
        ...
    class Target_Area(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Target_Cylinder(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Target_Disc(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Target_Light(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Target_Linear(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Target_Point(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Target_Rectangle(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Target_Sphere(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        DISPLAYFARATTENUATIONGIZMO: bool
        ENDFARATTENUATION: float
        FALLOFF: float
        FLUX: float
        HOTSPOT: float
        INTENSITY: float
        INTENSITYAT: float
        INTENSITYTYPE: int
        KELVIN: float
        LIGHTAFFECTSSHADOW: bool
        LIGHT_LENGTH: float
        LIGHT_RADIUS: float
        LIGHT_WIDTH: float
        MULTIPLIER: float
        ON: bool
        ORIGINALFLUX: float
        ORIGINALINTENSITY: float
        PROJECTOR: bool
        PROJECTORMAP: None
        RGBFILTER: MXSWrapperBase
        SHADOWCOLOR: MXSWrapperBase
        SHADOWCOLORMAPENABLE: bool
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHIFTCOLORWHENDIMMING: bool
        SHOWCONE: bool
        SOFTENDIFFUSEEDGE: float
        STARTFARATTENUATION: float
        TARGETDISTANCE: None
        USEFARATTENUATION: bool
        USEGLOBALSHADOWSETTINGS: bool
        USEKELVIN: bool
        USEMULTIPLIER: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Targetcamera(Camera):
        CLIPMANUALLY: bool
        CURFOV: float
        FARCLIP: float
        FARRANGE: float
        FAR_CLIP: float
        FOV: float
        FOVTYPE: int
        MPASSEFFECT: MXSWrapperBase
        MPASSENABLED: bool
        MPASSRENDERPERPASS: bool
        NEARCLIP: float
        NEARRANGE: float
        NEAR_CLIP: float
        ORTHOPROJECTION: bool
        SHOWCONE: bool
        SHOWHORIZON: bool
        SHOWRANGES: bool
        TYPE: MXSWrapperBase
        ...
    class Targetobject(GeometryClass):
        ...
    class Teapot(GeometryClass):
        BODY: bool
        HANDLE: bool
        LID: bool
        MAPCOORDS: bool
        RADIUS: float
        SEGS: int
        SMOOTH: bool
        SPOUT: bool
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS: float
        ...
    class Tee(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        MAPCOORDS: bool
        OPTIMIZE: bool
        QUAD_CAP: bool
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        TEE_LENGTH: float
        TEE_RADIUS: float
        TEE_THICKNESS: float
        TEE_WIDTH: float
        THICKNESS: float
        TWIST_CORRECTION: bool
        TYPEIN_CREATIONMETHOD: bool
        TYPEIN_LENGTH: float
        TYPEIN_RADIUS: float
        TYPEIN_THICKNESS: float
        TYPEIN_WIDTH: float
        TYPEIN_X: float
        TYPEIN_Y: float
        TYPEIN_Z: float
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        ...
    class TempObjectClass(TemporaryMergeNodeObjectClass):
        ...
    class TemporaryMergeNodeObjectClass(MAXWrapper):
        ...
    class Terrain(GeometryClass):
        DISPLAY: int
        FORM: int
        HORIZSIMPLIFICATION: int
        NUMOPS: int
        RETRIANGULATE: bool
        STITCHBORDER: bool
        UPDATE: int
        VERTSIMPLIFICATION: int
        ...
    class Test_Icon(Helper):
        ACTIVITY_TYPE: int
        ANIMATABLE_ACTIVE: bool
        AUTO_UPDATE: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        COLOR_COORDINATED: bool
        DEFAULT_HEIGHT: int
        DEFAULT_OFFSET: int
        DEFAULT_RANGE_MAX: float
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_TYPE: int
        DEFAULT_WIDTH: int
        ENABLE_BY_SWITCH: bool
        GROUPS: MXSWrapperBase
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        ICON_TYPE: int
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_DIVIDER: int
        PDVIEW_HEIGHT: int
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_SHOW_PARAMETERS: bool
        PDVIEW_WIDTH: int
        REPEATS: int
        SELECTED_SUBOPERATORS: MXSWrapperBase
        SUBOPERATORS: MXSWrapperBase
        TIME_OFF: int
        TIME_ON: int
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        VISIBLE_ICON: bool
        ...
    class TexOutputClass(Material):
        ...
    class TexSkyLight(Light):
        CASTSHADOWS: bool
        COLOR: MXSWrapperBase
        MULTIPLIER: float
        ON: bool
        RAYS_PER_SAMPLE: int
        RAY_BIAS: float
        SKY_COLOR_MAP: None
        SKY_COLOR_MAP_AMT: float
        SKY_COLOR_MAP_ON: bool
        SKY_MODE: int
        ...
    class Texmaps_RaytraceMtl(ReferenceMaker):
        ...
    class TextBaselineManipulator(Helper):
        ...
    class TextBevelProfileCurve(ReferenceMaker):
        ...
    class TextDisplayOnlyManipulator(Helper):
        ...
    class TextKerningManipulator(Helper):
        ...
    class TextMap(TextureMap):
        ALPHASOURCE: int
        APPLYCROP: bool
        BGCOLOR: MXSWrapperBase
        BOUNDSOBJECT: None
        BOUNDSTYPE: int
        COORDS: MXSWrapperBase
        CROPORPLACE: int
        CROP_H: float
        CROP_U: float
        CROP_V: float
        CROP_W: float
        FILLBG: bool
        FILLCOLOR: MXSWrapperBase
        FILLEDCHARACTERS: bool
        FILTER: bool
        FINITERESOLUTION: int
        GLYPHOPTION: int
        HWBITMAPSIZE: int
        JITTER: bool
        JITTERAMT: float
        MANUALHEIGHT: float
        MANUALWIDTH: float
        MERGESHAPES: bool
        MIPMAP: bool
        MONOOUTPUT: int
        OUTLINECOLOR: MXSWrapperBase
        OUTLINEDCHARACTERS: bool
        OUTLINEWIDTH: float
        OUTPUT: MXSWrapperBase
        RENDERCHILDREN: bool
        RENDERROOT: bool
        RESTYPE: int
        RGBOUTPUT: int
        STRICTHIERARCHY: bool
        TEXTOBJECT: None
        USEFILLCOLOR: bool
        ...
    class TextObject2(GeometryClass):
        ADAPTIVE: int
        ALIGNMENT: int
        APPLYBEVEL: bool
        AXISFLIP: bool
        BEVELDEPTH: float
        BEVELOFFSET: float
        BEVELOPTIMIZE: bool
        BEVELPUSH: float
        BEVELSTEPS: int
        BEVELWIDTH: float
        CAPEND: int
        CAPENDCONSTRAIN: bool
        CAPSTART: int
        CAPSTARTCONSTRAIN: bool
        CAPTYPE: int
        CHARBASELINEOFFSET: MXSWrapperBase
        CHARKERNINGOFFSET: MXSWrapperBase
        CHARXSCALE: MXSWrapperBase
        CHARYSCALE: MXSWrapperBase
        ELEMENTTYPE: int
        ENDBEVELMATERIAL: int
        ENDCAPMATERIAL: int
        EXTRUDEAMOUNT: float
        EXTRUDESEGMENTS: int
        GENERATEGEOMETRY: int
        HSCALE: float
        INTERPOLATIONSTEPS: int
        LAYOUTTYPE: int
        LEADING: float
        LENGTH: float
        MACRONAME: MXSWrapperBase
        MACROVALUE: MXSWrapperBase
        NODEELEMENTS: MXSWrapperBase
        NODEELEMENTSCENTERS: MXSWrapperBase
        OPTIMIZE: int
        PLANE: int
        SIDEMATERIAL: int
        SIZE: float
        STARTBEVELMATERIAL: int
        STARTCAPMATERIAL: int
        TRACKING: float
        UPAXIS: int
        USEBEVELWIDTH: bool
        VSCALE: float
        WIDTH: float
        ...
    class TextPlus(GeometryClass):
        ADAPTIVE: int
        ALIGNMENT: int
        APPLYBEVEL: bool
        AXISFLIP: bool
        BEVELDEPTH: float
        BEVELOFFSET: float
        BEVELOPTIMIZE: bool
        BEVELPUSH: float
        BEVELSTEPS: int
        BEVELWIDTH: float
        CAPEND: int
        CAPENDCONSTRAIN: bool
        CAPSTART: int
        CAPSTARTCONSTRAIN: bool
        CAPTYPE: int
        CHARBASELINEOFFSET: MXSWrapperBase
        CHARKERNINGOFFSET: MXSWrapperBase
        CHARXSCALE: MXSWrapperBase
        CHARYSCALE: MXSWrapperBase
        ELEMENTTYPE: int
        ENDBEVELMATERIAL: int
        ENDCAPMATERIAL: int
        EXTRUDEAMOUNT: float
        EXTRUDESEGMENTS: int
        GENERATEGEOMETRY: int
        HSCALE: float
        INTERPOLATIONSTEPS: int
        LAYOUTTYPE: int
        LEADING: float
        LENGTH: float
        MACRONAME: MXSWrapperBase
        MACROVALUE: MXSWrapperBase
        NODEELEMENTS: MXSWrapperBase
        NODEELEMENTSCENTERS: MXSWrapperBase
        OPTIMIZE: int
        PLANE: int
        SIDEMATERIAL: int
        SIZE: float
        STARTBEVELMATERIAL: int
        STARTCAPMATERIAL: int
        TRACKING: float
        UPAXIS: int
        USEBEVELWIDTH: bool
        VSCALE: float
        WIDTH: float
        ...
    class TextTrackingManipulator(Helper):
        ...
    class TextUniformScaleManipulator(Helper):
        ...
    class TextXScaleManipulator(Helper):
        ...
    class TextYScaleManipulator(Helper):
        ...
    class Text_Baseline_Manipulator(Helper):
        ...
    class Text_Display_Only_Manipulator(Helper):
        ...
    class Text_Kerning_Manipulator(Helper):
        ...
    class Text_Tracking_Manipulator(Helper):
        ...
    class Text_Uniform_Scale_Manipulator(Helper):
        ...
    class Text_X_Scale_Manipulator(Helper):
        ...
    class Text_Y_Scale_Manipulator(Helper):
        ...
    class TextureClass(Value):
        ...
    class TextureObjMask(TextureMap):
        COLOR0: MXSWrapperBase
        COLOR1: MXSWrapperBase
        COORDS: MXSWrapperBase
        DISPLACEAMOUNT: float
        DISPLACEENABLED: bool
        DISPLACETEX: None
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        OBJECT: None
        SUBTEX0: None
        SUBTEX1: None
        TRANSITIONBIAS: float
        TRANSITIONRANGE: float
        ...
    class Texture_Sky(Light):
        CASTSHADOWS: bool
        COLOR: MXSWrapperBase
        MULTIPLIER: float
        ON: bool
        RAYS_PER_SAMPLE: int
        RAY_BIAS: float
        SKY_COLOR_MAP: None
        SKY_COLOR_MAP_AMT: float
        SKY_COLOR_MAP_ON: bool
        SKY_MODE: int
        ...
    class Thin_Wall_Refraction(TextureMap):
        APPLYBLUR: bool
        BLUR: float
        BUMPMAPEFFECT: float
        FRAME: int
        NTHFRAME: int
        THICKNESSOFFSET: float
        USEENVIROMENT: bool
        ...
    class This_Data(ReferenceTarget):
        ...
    class TimeSensor(Helper):
        ...
    class Timer(RolloutControl):
        ...
    class TipSystem(Interface):
        ...
    class ToneMappingFragment(GraphicsFragmentPlugin):
        ...
    class ToneOperator(MAXWrapper):
        ...
    class TooltipFragment(GraphicsFragmentPlugin):
        ...
    class TopBottom(Material):
        BLEND: float
        BOTTOMMATERIAL: MXSWrapperBase
        COORDINATES: int
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        POSITION: float
        TOPMATERIAL: MXSWrapperBase
        ...
    class Torus(GeometryClass):
        MAPCOORDS: bool
        RADIUS1: float
        RADIUS2: float
        SEGS: int
        SIDES: int
        SLICE: bool
        SLICEFROM: float
        SLICEON: bool
        SLICETO: float
        SMOOTH: int
        TUBEROTATION: float
        TUBETWIST: float
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS1: float
        TYPEINRADIUS2: float
        ...
    class Torus_Knot(GeometryClass):
        BASE_CURVE: int
        ECCENTRICITY: float
        GEN_UV: int
        LUMPS: float
        LUMP_HEIGHT: float
        LUMP_OFFSET: float
        P: float
        Q: float
        RADIUS2: float
        RADIUS: float
        SEGMENTS: int
        SIDES: int
        SMOOTH: int
        TWIST: float
        U_OFFSET: float
        U_TILE: float
        V_OFFSET: float
        V_TILE: float
        WARP_COUNT: float
        WARP_HEIGHT: float
        ...
    class TouchSensor(Helper):
        ...
    class TrackBarClass(MAXWrapper):
        ...
    class TrackSet(ReferenceMaker):
        ...
    class TrackSetList(ReferenceMaker):
        ...
    class TrackViewPick(Value):
        ...
    class TransMatrix(Primitive):
        ...
    class Transition(ReferenceTarget):
        DURATION: int
        EASEIN: float
        EASEOUT: float
        FROM: None
        FUNCTIONNAME: str
        PRIORITY: int
        SCRIPT: None
        TO: None
        ...
    class Translate(MappedGeneric):
        ...
    class Translucent(Shader):
        ...
    class Translucent_Shader(Shader):
        ...
    class TreeViewUtil(UtilityPlugin):
        ...
    class TriMesh(Value):
        ...
    class TriMeshGeometry(GeometryClass):
        ...
    class Trim_Extend(Modifier):
        ...
    class TrueType(BezierFontLoaderClass):
        ...
    class Tube(GeometryClass):
        CAPSEGS: int
        HEIGHT: float
        HEIGHTSEGS: int
        MAPCOORDS: bool
        RADIUS1: float
        RADIUS2: float
        SIDES: int
        SLICE: bool
        SLICEFROM: float
        SLICEON: bool
        SLICETO: float
        SMOOTH: bool
        TYPEINCREATIONMETHOD: int
        TYPEINHEIGHT: float
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS1: float
        TYPEINRADIUS2: float
        ...
    class TurboSmooth(Modifier):
        EXPLICITNORMALS: bool
        ISOLINEDISPLAY: bool
        ITERATIONS: int
        RENDERITERATIONS: int
        SEPBYMATS: bool
        SEPBYSMGROUPS: bool
        SMOOTHRESULT: bool
        UPDATE: int
        USERENDERITERATIONS: bool
        ...
    class TurnOffMCGProfiling(MAXScriptFunction):
        ...
    class TurnOnMCGProfiling(MAXScriptFunction):
        ...
    class TurnOnMacroRecorderContext(MAXScriptFunction):
        ...
    class TurnToSeq(MAXScriptFunction):
        ...
    class Turn_To_Mesh(Modifier):
        SELECTIONCONVERSION: int
        SELECTIONLEVEL: int
        USEINVISIBLEEDGES: bool
        USESOFTSELECTION: bool
        ...
    class Turn_To_Patch(Modifier):
        QUADSTOQUADS: bool
        SELECTIONCONVERSION: int
        SELECTIONLEVEL: int
        USESOFTSELECTION: int
        ...
    class Turn_To_Poly(Modifier):
        KEEPCONVEX: bool
        LIMITPOLYSIZE: bool
        MAXPOLYSIZE: int
        PLANARTHRESH: float
        REMOVEMIDEDGEVERTICES: bool
        REQUIREPLANAR: bool
        SELECTIONCONVERSION: int
        SELECTIONLEVEL: int
        USESOFTSELECTION: bool
        ...
    class Twist(Modifier):
        ANGLE: float
        AXIS: int
        BIAS: float
        LIMIT: bool
        LOWERLIMIT: float
        UPPERLIMIT: float
        ...
    class UConstraint(Helper):
        BODY0: None
        BODY1: None
        BREAKABLE: bool
        CHILDATTACHPOINT: MXSWrapperBase
        CHILDINITIALTWIST: float
        COLLISION: bool
        GEARING: bool
        GEARRATIO: float
        HELPERSIZE: float
        LINEARDAMPING: float
        LINEARMODEX: int
        LINEARMODEY: int
        LINEARMODEZ: int
        LINEARPOSITION: float
        LINEARRESTITUTION: float
        LINEARSPRING: float
        MAXFORCE: float
        MAXTORQUE: float
        POSDAMPING: float
        POSSPRING: float
        PROJECTIONANGLE: float
        PROJECTIONDIST: float
        PROJECTIONMODE: int
        SHOWVISUALIZER: bool
        SWING1ANGLE: float
        SWING1DAMPING: float
        SWING1MODE: int
        SWING1RESTITUTION: float
        SWING1SPRING: float
        SWING2ANGLE: float
        SWING2DAMPING: float
        SWING2MODE: int
        SWING2RESTITUTION: float
        SWING2SPRING: float
        SWINGDAMPING: float
        SWINGSPRING: float
        TWISTANGLEHIGH: float
        TWISTANGLELOW: float
        TWISTDAMPING: float
        TWISTDAMPINGHIGH: float
        TWISTDAMPINGLOW: float
        TWISTMODE: int
        TWISTRESTITUTIONHIGH: float
        TWISTRESTITUTIONLOW: float
        TWISTSPRING: float
        TWISTSPRINGHIGH: float
        TWISTSPRINGLOW: float
        USEACCELERATION: bool
        USEHARDLIMITS: bool
        USEPROJECTION: bool
        ...
    class UDeflector(SpacewarpObject):
        BOUNCE: float
        BOUNCEVAR: float
        CHAOS: float
        FRICTION: float
        INHERITVELOCITY: float
        RADIUS: float
        ...
    class UDeflectorMod(SpacewarpModifier):
        ...
    class UIAccessor(Interface):
        ...
    class UOmniFlect(SpacewarpObject):
        AFFECTS: float
        BOUNCE: float
        BOUNCEVAR: float
        CHAOS: float
        DECELERATION: float
        DECELVAR: float
        DIFFUSION: float
        DIFFUSIONVAR: float
        FRICTION: float
        INHERITVELOCITY: float
        PASSVELOCITY: float
        PASSVELOCITYVAR: float
        RADIUS: float
        REFRACTION: float
        REFRACTIONVAR: float
        REFRACTS: float
        SPAWN: float
        TIMEOFF: MXSWrapperBase
        TIMEON: MXSWrapperBase
        ...
    class UOmniFlectMod(SpacewarpModifier):
        ...
    class USetup(Primitive):
        ...
    class UTypeStair(GeometryClass):
        CARRIAGECONTEXT: int
        CARRIAGECOUNT: int
        CARRIAGEEXTOFFS: float
        CARRIAGEHEIGHT: float
        CARRIAGEINTOFFS: float
        CARRIAGESPACE: float
        CARRIAGESPACINGTYPE: int
        CARRIAGESPRINGFLOOR: bool
        CARRIAGEWIDTH: float
        DIRECTION: int
        GENERATECARRIAGE: bool
        GENERATEINSIDERAILING: bool
        GENERATEMAPPING: bool
        GENERATEOUTSIDERAILING: bool
        GENERATESTRINGERS: bool
        LENGTH2: float
        LENGTH: float
        RAILINGHEIGHT: float
        RAILINGOFFS: float
        RAILINGRADIUS: float
        RAILINGSEGMENTS: int
        STEPCOUNT: int
        STEPDEPTH: float
        STEPDEPTH_X: bool
        STEPHEIGHT: float
        STEPTHICKNESS: float
        STEPTYPE: int
        STEPWIDTH: float
        STRINGERDEPTH: float
        STRINGEROFFSET: float
        STRINGERSPRINGFLOOR: bool
        STRINGERWIDTH: float
        UPPEROFFSET: float
        ...
    class UVGenClass(Material):
        ...
    class UVWUnwrap(Modifier):
        AUTOPIN: bool
        BASEMATERIAL: None
        BASEMATERIAL_LIST: MXSWrapperBase
        BUTTONPANEL_HEIGHT1: int
        BUTTONPANEL_HEIGHT2: int
        BUTTONPANEL_VISIBLE: bool
        BUTTONPANEL_WIDTH: int
        CHECKERMATERIAL: MXSWrapperBase
        EDGESNAP: bool
        FILTERPIN: bool
        GRIDSNAP: bool
        GROUPDENSITY: MXSWrapperBase
        GROUPDISPLAY: bool
        GROUPNAME: MXSWrapperBase
        LOCALDISTORTION: bool
        PEELAUTOEDIT: bool
        QUICK_MAP_ALIGN: int
        QUICK_MAP_PREVIEW: bool
        RENDERUV_EDGEALPHA: float
        RENDERUV_EDGECOLOR: MXSWrapperBase
        RENDERUV_FILLALPHA: float
        RENDERUV_FILLCOLOR: MXSWrapperBase
        RENDERUV_FILLMODE: int
        RENDERUV_FORCE2SIDED: bool
        RENDERUV_HEIGHT: int
        RENDERUV_INVISIBLEEDGES: bool
        RENDERUV_OVERLAPCOLOR: MXSWrapperBase
        RENDERUV_SEAMCOLOR: MXSWrapperBase
        RENDERUV_SEAMEDGES: bool
        RENDERUV_SHOWFRAMEBUFFER: bool
        RENDERUV_SHOWOVERLAP: bool
        RENDERUV_VISIBLEEDGES: bool
        RENDERUV_WIDTH: int
        SHOWIMAGEALPHA: bool
        SPLINEMAP_ADVANCEMETHOD: int
        SPLINEMAP_DISPLAY: bool
        SPLINEMAP_ITERATIONS: int
        SPLINEMAP_MANUALSEAMS: bool
        SPLINEMAP_NODE: None
        SPLINEMAP_PROJECTIONTYPE: int
        SPLINEMAP_RESAMPLECOUNT: int
        SPLINEMAP_UOFFSET: float
        SPLINEMAP_USCALE: float
        SPLINEMAP_VOFFSET: float
        SPLINEMAP_VSCALE: float
        TEXMAPIDLIST: MXSWrapperBase
        TEXMAPLIST: MXSWrapperBase
        TEXTURECHECKERMATERIAL: None
        TOOLBARVISIBLE: bool
        VERTEXSNAP: bool
        WELDONLYSHARED: bool
        ...
    class UVW_Mapping_Add(Modifier):
        ...
    class UVW_Mapping_Clear(Modifier):
        MAPID: int
        ...
    class UVW_Mapping_Paste(Modifier):
        ...
    class UVW_Remove(UtilityPlugin):
        ...
    class UVW_Xform(Modifier):
        MAP_CHANNEL: int
        MAP_OR_VERTEX_COLOR: int
        ROTATION_ANGLE: float
        ROTATION_CENTER: int
        U_FLIP: int
        U_OFFSET: float
        U_TILE: float
        V_FLIP: int
        V_OFFSET: float
        V_TILE: float
        W_FLIP: int
        W_OFFSET: float
        W_TILE: float
        ...
    class U_Type_Stair(GeometryClass):
        CARRIAGECONTEXT: int
        CARRIAGECOUNT: int
        CARRIAGEEXTOFFS: float
        CARRIAGEHEIGHT: float
        CARRIAGEINTOFFS: float
        CARRIAGESPACE: float
        CARRIAGESPACINGTYPE: int
        CARRIAGESPRINGFLOOR: bool
        CARRIAGEWIDTH: float
        DIRECTION: int
        GENERATECARRIAGE: bool
        GENERATEINSIDERAILING: bool
        GENERATEMAPPING: bool
        GENERATEOUTSIDERAILING: bool
        GENERATESTRINGERS: bool
        LENGTH2: float
        LENGTH: float
        RAILINGHEIGHT: float
        RAILINGOFFS: float
        RAILINGRADIUS: float
        RAILINGSEGMENTS: int
        STEPCOUNT: int
        STEPDEPTH: float
        STEPDEPTH_X: bool
        STEPHEIGHT: float
        STEPTHICKNESS: float
        STEPTYPE: int
        STEPWIDTH: float
        STRINGERDEPTH: float
        STRINGEROFFSET: float
        STRINGERSPRINGFLOOR: bool
        STRINGERWIDTH: float
        UPPEROFFSET: float
        ...
    class UiCustomization(Interface):
        ...
    class UndefinedClass(Value):
        ...
    class UnsuppliedClass(Value):
        ...
    class Unwrap_UVW(Modifier):
        AUTOPIN: bool
        BASEMATERIAL: None
        BASEMATERIAL_LIST: MXSWrapperBase
        BUTTONPANEL_HEIGHT1: int
        BUTTONPANEL_HEIGHT2: int
        BUTTONPANEL_VISIBLE: bool
        BUTTONPANEL_WIDTH: int
        CHECKERMATERIAL: MXSWrapperBase
        EDGESNAP: bool
        FILTERPIN: bool
        GRIDSNAP: bool
        GROUPDENSITY: MXSWrapperBase
        GROUPDISPLAY: bool
        GROUPNAME: MXSWrapperBase
        LOCALDISTORTION: bool
        PEELAUTOEDIT: bool
        QUICK_MAP_ALIGN: int
        QUICK_MAP_PREVIEW: bool
        RENDERUV_EDGEALPHA: float
        RENDERUV_EDGECOLOR: MXSWrapperBase
        RENDERUV_FILLALPHA: float
        RENDERUV_FILLCOLOR: MXSWrapperBase
        RENDERUV_FILLMODE: int
        RENDERUV_FORCE2SIDED: bool
        RENDERUV_HEIGHT: int
        RENDERUV_INVISIBLEEDGES: bool
        RENDERUV_OVERLAPCOLOR: MXSWrapperBase
        RENDERUV_SEAMCOLOR: MXSWrapperBase
        RENDERUV_SEAMEDGES: bool
        RENDERUV_SHOWFRAMEBUFFER: bool
        RENDERUV_SHOWOVERLAP: bool
        RENDERUV_VISIBLEEDGES: bool
        RENDERUV_WIDTH: int
        SHOWIMAGEALPHA: bool
        SPLINEMAP_ADVANCEMETHOD: int
        SPLINEMAP_DISPLAY: bool
        SPLINEMAP_ITERATIONS: int
        SPLINEMAP_MANUALSEAMS: bool
        SPLINEMAP_NODE: None
        SPLINEMAP_PROJECTIONTYPE: int
        SPLINEMAP_RESAMPLECOUNT: int
        SPLINEMAP_UOFFSET: float
        SPLINEMAP_USCALE: float
        SPLINEMAP_VOFFSET: float
        SPLINEMAP_VSCALE: float
        TEXMAPIDLIST: MXSWrapperBase
        TEXMAPLIST: MXSWrapperBase
        TEXTURECHECKERMATERIAL: None
        TOOLBARVISIBLE: bool
        VERTEXSNAP: bool
        WELDONLYSHARED: bool
        ...
    class UpdatePerViewWorldGenFragment(GraphicsFragmentPlugin):
        ...
    class UpdatePointCloudMaterial(MAXScriptFunction):
        ...
    class UpdateSceneMaterialLib(Primitive):
        ...
    class UserDataTypeClass(MAXWrapperNonRefTarg):
        ...
    class UserGeneric(Value):
        ...
    class UtilityPanel(Interface):
        ...
    class UtilityPlugin(MAXWrapperNonRefTarg):
        ...
    class Uvwmap(Modifier):
        AXIS: int
        CAP: bool
        CHANNEL: int
        HEIGHT: float
        LENGTH: float
        MAPCHANNEL: int
        MAPTYPE: int
        UFLIP: bool
        UTILE: float
        VFLIP: bool
        VTILE: float
        WFLIP: bool
        WIDTH: float
        WTILE: float
        ...
    class VCAddMask(Primitive):
        ...
    class VCAdjustLevels(Primitive):
        ...
    class VCApplyImage(Primitive):
        ...
    class VCBlurLayer(Primitive):
        ...
    class VCColorBalance(Primitive):
        ...
    class VCCreateDisplayBitmap(Primitive):
        ...
    class VCDeleteLayer(Primitive):
        ...
    class VCDeleteMask(Primitive):
        ...
    class VCDuplicateLayer(Primitive):
        ...
    class VCEndTrack(Primitive):
        ...
    class VCFillInBitmap(Primitive):
        ...
    class VCFindEdges(Primitive):
        ...
    class VCFlattenLayers(Primitive):
        ...
    class VCFlattenLayersNoUndo(Primitive):
        ...
    class VCFlipLayer(Primitive):
        ...
    class VCGet2DViewMenuHeight(Primitive):
        ...
    class VCGet2DViewSize(Primitive):
        ...
    class VCGetLayerSetting(Primitive):
        ...
    class VCGetSetting(Primitive):
        ...
    class VCHighPass(Primitive):
        ...
    class VCInvertLayer(Primitive):
        ...
    class VCIsLeftButtonDown(Primitive):
        ...
    class VCJitter(Primitive):
        ...
    class VCLayerAdjust(Primitive):
        ...
    class VCLayerAdjustApply(Primitive):
        ...
    class VCLayerSettingChangeStart(Primitive):
        ...
    class VCLoadBitmapIntoLayer(Primitive):
        ...
    class VCMedian(Primitive):
        ...
    class VCMergeDownLayer(Primitive):
        ...
    class VCMoveLayer(Primitive):
        ...
    class VCNewLayer(Primitive):
        ...
    class VCNormalize(Primitive):
        ...
    class VCPasteFromClipboard(Primitive):
        ...
    class VCSavePSD(Primitive):
        ...
    class VCSetCurrentLayer(Primitive):
        ...
    class VCSetLayerBitmap(Primitive):
        ...
    class VCSetLayerSetting(Primitive):
        ...
    class VCSetSetting(Primitive):
        ...
    class VCSetUsingNewTexture(Primitive):
        ...
    class VCSharpenLayer(Primitive):
        ...
    class VCStartTrack(Primitive):
        ...
    class VCThreshold(Primitive):
        ...
    class VCview2DFitTextureToView(Primitive):
        ...
    class VCview2DFullSize(Primitive):
        ...
    class VCview2DWireToggle(Primitive):
        ...
    class VDM(TextureMap):
        METHOD: int
        MULT_SPIN: float
        VECTOR_MAP: None
        VECTOR_MAP_ENABLED: bool
        VECTOR_MAP_IS_HDR: bool
        ...
    class VFB_Rollout_Bottom(RolloutClass):
        ...
    class VFB_Rollout_TopLeft(RolloutClass):
        ...
    class VFB_Rollout_TopRight(RolloutClass):
        ...
    class VIZ_Radiosity(RadiosityEffect):
        CONTRASTTHRESHOLD: float
        ELAPSEDTIME: int
        INCLUDEAREALIGHTS: bool
        INCLUDELINEARLIGHTS: bool
        INCLUDEPOINTLIGHTS: bool
        INCLUDESELFEMITTINGLIGHTS: bool
        INCLUDESKYLIGHT: bool
        INITIALMESHSIZE: float
        LIGHTPAINTINGINTENSITY: float
        LIGHTPAINTINGPRESSURE: float
        LIGHTUNITSUSED: int
        MESHINGENABLED: bool
        MESHINGSIZE: float
        MINIMUMMESHSIZE: float
        MINIMUMSELFEMITTINGSIZE: float
        RADDIRECTFILTERING: int
        RADDISPLAYINVIEWPORT: bool
        RADFILTERING: int
        RADGLOBALREFINESTEPS: int
        RADINITIALQUALITY: float
        RADPROCESSINRENDERONLY: bool
        RADPROCESSOBJECTREFINESTEPS: bool
        RADSELECTIONREFINESTEPS: int
        RMADAPTIVEENABLED: bool
        RMCLAMPENABLED: bool
        RMCLAMPVALUE: float
        RMFILTERRADIUS: float
        RMMINSAMPLESPACING: int
        RMRAYSPERSAMPLE: int
        RMREGATHER: bool
        RMREUSEDIRECTILLUMINATION: bool
        RMSAMPLESPACING: int
        RMSHOWSAMPLES: bool
        RMSUBDIVISIONCONTRAST: float
        SHOOTDIRECTLIGHTS: bool
        STATMESHSIZE: float
        STATNUMFACES: int
        STATNUMGEOMOBJECTS: int
        STATNUMLIGHTOBJECTS: int
        STATREFINEITERATIONS: int
        STATSOLUTIONQUALITY: float
        USEADAPTIVEMESHING: bool
        ...
    class VRBL_Export(ExporterPlugin):
        ...
    class VUE_File_Renderer(RendererClass):
        ...
    class ValidateExposureControlForLight(MAXScriptFunction):
        ...
    class ValidateGetRenderMeshNeedDelArg(Primitive):
        ...
    class ValidateReferenceMakerRefs(Primitive):
        ...
    class ValidateSingleRefMaker(Primitive):
        ...
    class ValueConverter(Interface):
        ...
    class ValueRef(Value):
        ...
    class Vector(ReferenceTarget):
        ANGLE_VARIATION: float
        ANGLE_X: float
        ANGLE_Y: float
        ANGLE_Z: float
        AXIAL_RADIUS: float
        BEARING: float
        COORD_X: float
        COORD_Y: float
        COORD_Z: float
        DIVERGENCE: float
        FILTER: None
        FLOAT_VARIATION: float
        FLOAT_X: float
        FLOAT_Y: float
        FLOAT_Z: float
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        INPUT_7: None
        LATITUDE: float
        LENGTH_VARIATION: float
        PERCENT_VARIATION: float
        PERCENT_X: float
        PERCENT_Y: float
        PERCENT_Z: float
        RADIUS: float
        RANDOM_SEED: int
        SYNC_TYPE: int
        TYPE: int
        UNITS_PER_TYPE: int
        USE_AS_ACCELERATION: bool
        USE_AS_SPEED_VALUE: bool
        USE_DIVERGENCE: bool
        USE_E1: bool
        USE_E2: bool
        USE_E3: bool
        USE_E4: bool
        USE_E5: bool
        USE_E6: bool
        USE_E7: bool
        USE_LENGTH_VARIATION: bool
        ...
    class VectorField(SpacewarpObject):
        BLENDFALLOFF: float
        BLENDHGTSEGS: int
        BLENDLENSEGS: int
        BLENDSTART: float
        BLENDWIDSEGS: int
        DIRECTION: int
        FALLOFF: float
        FLIPFACES: bool
        HEIGHT: float
        HGTSEGS: int
        ICONSIZE: float
        LENGTH: float
        LENSEGS: int
        OBJECT: None
        PULL: float
        RANGE: float
        RESOLUTION: int
        SHOWLATTICE: bool
        SHOWRANGE: bool
        SHOWSURFSAMPS: bool
        SHOWVECTORS: bool
        STRENGTH: float
        VECSCALE: float
        WIDSEGS: int
        WIDTH: float
        ...
    class VectorMap(TextureMap):
        ALPHASOURCE: int
        APPLYCROP: bool
        BACKCOLOR: MXSWrapperBase
        CONTINOUS: bool
        COORDS: MXSWrapperBase
        CROPORPLACE: int
        CROP_H: float
        CROP_U: float
        CROP_V: float
        CROP_W: float
        FILTER: bool
        FINITERESOLUTION: int
        HWBITMAPSIZE: int
        JITTER: bool
        JITTERAMT: float
        LINECAP: int
        LINECOLOR: MXSWrapperBase
        LINEWIDTH: float
        MEMLIMIT: int
        MIPMAP: bool
        MONOOUTPUT: int
        OUTPUT: MXSWrapperBase
        PAGECOLOR: MXSWrapperBase
        PATTERNNAME: int
        PATTERNREPEAT: float
        PDF_PAGE: float
        PREVIEW: bool
        RESTYPE: int
        RGBOUTPUT: int
        TRANSITIONDIR: int
        TRANSITION_MODE: int
        TRANSPARENT: bool
        VECTORFILE: str
        ...
    class Vector_Displacement(TextureMap):
        METHOD: int
        MULT_SPIN: float
        VECTOR_MAP: None
        VECTOR_MAP_ENABLED: bool
        VECTOR_MAP_IS_HDR: bool
        ...
    class Vector_Field(SpacewarpObject):
        BLENDFALLOFF: float
        BLENDHGTSEGS: int
        BLENDLENSEGS: int
        BLENDSTART: float
        BLENDWIDSEGS: int
        DIRECTION: int
        FALLOFF: float
        FLIPFACES: bool
        HEIGHT: float
        HGTSEGS: int
        ICONSIZE: float
        LENGTH: float
        LENSEGS: int
        OBJECT: None
        PULL: float
        RANGE: float
        RESOLUTION: int
        SHOWLATTICE: bool
        SHOWRANGE: bool
        SHOWSURFSAMPS: bool
        SHOWVECTORS: bool
        STRENGTH: float
        VECSCALE: float
        WIDSEGS: int
        WIDTH: float
        ...
    class Vector_Field_Modifier(SpacewarpModifier):
        ...
    class Vector_Map(TextureMap):
        ALPHASOURCE: int
        APPLYCROP: bool
        BACKCOLOR: MXSWrapperBase
        CONTINOUS: bool
        COORDS: MXSWrapperBase
        CROPORPLACE: int
        CROP_H: float
        CROP_U: float
        CROP_V: float
        CROP_W: float
        FILTER: bool
        FINITERESOLUTION: int
        HWBITMAPSIZE: int
        JITTER: bool
        JITTERAMT: float
        LINECAP: int
        LINECOLOR: MXSWrapperBase
        LINEWIDTH: float
        MEMLIMIT: int
        MIPMAP: bool
        MONOOUTPUT: int
        OUTPUT: MXSWrapperBase
        PAGECOLOR: MXSWrapperBase
        PATTERNNAME: int
        PATTERNREPEAT: float
        PDF_PAGE: float
        PREVIEW: bool
        RESTYPE: int
        RGBOUTPUT: int
        TRANSITIONDIR: int
        TRANSITION_MODE: int
        TRANSPARENT: bool
        VECTORFILE: str
        ...
    class VertexColor(TextureMap):
        MAP: int
        SUBID: int
        ...
    class VertexPaint(Modifier):
        CASTSHADOWS: bool
        COLORBY: int
        HIDEUNSELSUBOBJS: bool
        IGNOREBACKFACING: bool
        LAYERISOLATED: bool
        LAYERMODE: str
        LAYEROPACITY: float
        LIGHTINGMODEL: int
        MAPCHANNEL: int
        RADIOSITYONLY: bool
        RADIOSITYOPTION: int
        SURVIVECONDENSE: bool
        USEMAPS: bool
        USERADIOSITY: bool
        ...
    class VertexPaintTool(Primitive):
        ...
    class VertexSelection(Value):
        ...
    class VertexWeld(Modifier):
        THRESHOLD: float
        ...
    class Vertex_Color(TextureMap):
        MAP: int
        SUBID: int
        ...
    class Vertex_Colors(Modifier):
        ...
    class Vertex_Paint_Floater(UserDataTypeClass):
        ...
    class Vertex_Paint_Startup_GUP(GlobalUtilityPlugin):
        ...
    class Vertex_Weld(Modifier):
        THRESHOLD: float
        ...
    class Vertical_Horizontal_Turn(MAXWrapper):
        ...
    class Video(Filter):
        ...
    class VideoPostFilter(MAXWrapperNonRefTarg):
        ...
    class View2DControl(RolloutControl):
        ...
    class ViewCubeOps(Interface):
        ...
    class ViewPanelManager(Interface):
        ...
    class ViewportButtonMgr(Interface):
        ...
    class ViewportCanvasColorPicker(Primitive):
        ...
    class ViewportCanvasEnd(Primitive):
        ...
    class ViewportCanvasSetup(Primitive):
        ...
    class ViewportCanvasSwitchBrush(Primitive):
        ...
    class ViewportCanvasUnitTest(Primitive):
        ...
    class ViewportManager(GlobalUtilityPlugin):
        ...
    class ViewportManagerControl(GlobalUtilityPlugin):
        ...
    class ViewportManagerCustAttrib(CustAttrib):
        DXSTDMAT: bool
        EFFECT: int
        ENABLED: bool
        SAVEFXFILE: None
        ...
    class ViewportSSB(Interface):
        ...
    class VisualMSUtil(UtilityPlugin):
        ...
    class Visual_MAXScript(UtilityPlugin):
        ...
    class Vol__Select(Modifier):
        AUTOFIT: bool
        BUBBLE: float
        FALLOFF: float
        INVERT: bool
        LEVEL: int
        MAP: int
        MAPCHANNEL: int
        MATID: int
        METHOD: int
        NODE: None
        PINCH: float
        SMGROUP: int
        TEXTURE: None
        TYPE: int
        USEAFFECTREGION: bool
        VOLUME: int
        ...
    class VolumeHelper(Helper):
        COLOR: MXSWrapperBase
        MESHNODE: None
        SECTIONRADIUS: float
        SIZE: float
        VOLUMETYPE: int
        ...
    class VolumeSelect(Modifier):
        AUTOFIT: bool
        BUBBLE: float
        FALLOFF: float
        INVERT: bool
        LEVEL: int
        MAP: int
        MAPCHANNEL: int
        MATID: int
        METHOD: int
        NODE: None
        PINCH: float
        SMGROUP: int
        TEXTURE: None
        TYPE: int
        USEAFFECTREGION: bool
        VOLUME: int
        ...
    class Volume_Fog(Atmospheric):
        DENSITY: float
        EXPONENTIAL: int
        FOG_BACKGROUND: int
        FOG_COLOR: MXSWrapperBase
        HIGH_THRESHOLD: float
        INVERT: int
        LEVELS: float
        LOW_THRESHOLD: float
        MAX_STEPS: int
        NOISE_TYPE: int
        PHASE: float
        SIZE: float
        SOFTEN_GIZMO_EDGES: float
        STEP_SIZE: float
        UNIFORMITY: float
        WIND_DIRECTION: int
        WIND_STRENGTH: float
        ...
    class Volume_Light(Atmospheric):
        ATTENUATION_COLOR: MXSWrapperBase
        ATTENUATION_COLOR_MULTIPLIER: float
        ATTEN__END: float
        ATTEN__START: float
        AUTO_SAMPLE: int
        DENSITY: float
        EXPONENTIAL: int
        FILTER_SHADOWS: int
        FOG_COLOR: MXSWrapperBase
        HIGH_THRESHOLD: float
        INVERT: int
        LEVELS: float
        LINK_TO_LIGHT: int
        LOW_THRESHOLD: float
        MAX_LIGHT: float
        MIN_LIGHT: float
        NOISE_AMOUNT: float
        NOISE_ON: int
        NOISE_TYPE: int
        PHASE: float
        SAMPLES: int
        SIZE: float
        UNIFORMITY: float
        USE_ATTENUATION_COLOR: int
        WIND_DIRECTION: int
        WIND_STRENGTH: float
        ...
    class Vortex(SpacewarpObject):
        AXIALDAMPING: float
        AXIALFALLOFF: float
        AXIALRANGE: float
        AXIALSTRENGTH: float
        DIRECTION: int
        ICONSIZE: float
        RADIALDAMPING: float
        RADIALFALLOFF: float
        RADIALRANGE: float
        RADIALSTRENGTH: float
        RANGELESS: bool
        ROTATIONDAMPING: float
        ROTATIONFALLOFF: float
        ROTATIONRANGE: float
        ROTATIONSTRENGTH: float
        TAPERSHAPE: float
        TAPERSTRENGTH: float
        TIMEOFF: MXSWrapperBase
        TIMEON: MXSWrapperBase
        ...
    class VortexMod(SpacewarpModifier):
        ...
    class VrmlImp(ImporterPlugin):
        ...
    class Vsp_Gantry(GeometryClass):
        DIA: float
        FLIPSIGNALS: bool
        HEIGHT: float
        LENGTH: float
        LSTYLE: bool
        MATID: int
        NUMBEROFSIGNALS: int
        RADIUS: float
        SIGNALGAP: float
        SIGNALOFFSET: float
        SIGNALS: bool
        XFALL: float
        ...
    class Vsp_GantryNZ(GeometryClass):
        DIA: float
        FLIPSIGNALS: bool
        HEIGHT: float
        LENGTH: float
        LSTYLE: bool
        MATID: int
        NUMBEROFSIGNALS: int
        RADIUS: float
        SIGNALGAP: float
        SIGNALOFFSET: float
        SIGNALS: bool
        XFALL: float
        ...
    class Vsp_GantrySA(GeometryClass):
        DIA: float
        FLIPSIGNALS: bool
        HEIGHT: float
        LENGTH: float
        LSTYLE: bool
        MATID: int
        NUMBEROFSIGNALS: int
        RADIUS: float
        SIGNALGAP: float
        SIGNALOFFSET: float
        SIGNALS: bool
        XFALL: float
        ...
    class Vsp_Lamp(GeometryClass):
        ANGLE: float
        ARMLEN: float
        DEPTH: float
        DIA1: float
        DIA2: float
        HEADSCALEX: float
        HEADSCALEY: float
        HEIGHT: float
        KINK1: float
        KINK2: float
        LEFTARM: bool
        MATID: int
        ONOFF: bool
        RADIUS: float
        RIGHTARM: bool
        ...
    class Vsp_Sign(GeometryClass):
        DEPTH: float
        EDGEOFF: float
        HEIGHT: float
        PHEIGHT: float
        POSTS: int
        TYPE: int
        WIDTH: float
        ...
    class Vsp_Signal(GeometryClass):
        CURPHASE: int
        DEPTH: float
        EDGEOFF: float
        HEIGHT: float
        NUMPHASES: int
        PHEIGHT: float
        POSTS: int
        TYPE: int
        WIDTH: float
        ...
    class Vsp_Symb(GeometryClass):
        HEIGHT: float
        TYPE: int
        WIDTH: float
        ...
    class Vsp_Tree(GeometryClass):
        HEIGHT: float
        MATID: int
        NFACES: int
        WIDTH: float
        ...
    class VzMaterialTable(ReferenceTarget):
        ...
    class VzObjectTable(ReferenceMaker):
        ...
    class VzObjectTableRecord(ReferenceMaker):
        ...
    class WM3_AddProgressiveMorphNode(Primitive):
        ...
    class WM3_CreateMarker(Primitive):
        ...
    class WM3_DeleteMarker(Primitive):
        ...
    class WM3_DeleteProgressiveMorphNode(Primitive):
        ...
    class WM3_GetCurrentMarker(Primitive):
        ...
    class WM3_GetMarkerIndex(Primitive):
        ...
    class WM3_GetMarkerName(Primitive):
        ...
    class WM3_GetProgressiveMorphNode(Primitive):
        ...
    class WM3_GetProgressiveMorphTension(Primitive):
        ...
    class WM3_GetProgressiveMorphWeight(Primitive):
        ...
    class WM3_MC_BuildFromNode(Primitive):
        ...
    class WM3_MC_Delete(Primitive):
        ...
    class WM3_MC_GetLimitMAX(Primitive):
        ...
    class WM3_MC_GetLimitMIN(Primitive):
        ...
    class WM3_MC_GetMemUse(Primitive):
        ...
    class WM3_MC_GetMorphPoint(Primitive):
        ...
    class WM3_MC_GetMorphWeight(Primitive):
        ...
    class WM3_MC_GetName(Primitive):
        ...
    class WM3_MC_GetTarget(Primitive):
        ...
    class WM3_MC_GetUseLimits(Primitive):
        ...
    class WM3_MC_GetUseVertexSel(Primitive):
        ...
    class WM3_MC_GetValue(Primitive):
        ...
    class WM3_MC_HasData(Primitive):
        ...
    class WM3_MC_HasTarget(Primitive):
        ...
    class WM3_MC_IsActive(Primitive):
        ...
    class WM3_MC_IsValid(Primitive):
        ...
    class WM3_MC_NumMPts(Primitive):
        ...
    class WM3_MC_NumPts(Primitive):
        ...
    class WM3_MC_Rebuild(Primitive):
        ...
    class WM3_MC_SetActive(Primitive):
        ...
    class WM3_MC_SetLimitMAX(Primitive):
        ...
    class WM3_MC_SetLimitMIN(Primitive):
        ...
    class WM3_MC_SetName(Primitive):
        ...
    class WM3_MC_SetTarget(Primitive):
        ...
    class WM3_MC_SetUseLimits(Primitive):
        ...
    class WM3_MC_SetUseVertexSel(Primitive):
        ...
    class WM3_MC_SetValue(Primitive):
        ...
    class WM3_MoveMorph(Primitive):
        ...
    class WM3_NumberOfChannels(Primitive):
        ...
    class WM3_NumberOfMarkers(Primitive):
        ...
    class WM3_NumberOfProgressiveMorphs(Primitive):
        ...
    class WM3_RebuildInternalCache(Primitive):
        ...
    class WM3_RefreshChannelListUI(Primitive):
        ...
    class WM3_RefreshChannelParamsUI(Primitive):
        ...
    class WM3_SetChannelPos(Primitive):
        ...
    class WM3_SetChannelSel(Primitive):
        ...
    class WM3_SetCurrentMarker(Primitive):
        ...
    class WM3_SetMarkerData(Primitive):
        ...
    class WM3_SetProgressiveMorphTension(Primitive):
        ...
    class WM3_SetProgressiveMorphWeight(Primitive):
        ...
    class WM3_SwapMorph(Primitive):
        ...
    class WSMApplyFC(Primitive):
        ...
    class WSMSupportsCollision(Primitive):
        ...
    class WSMSupportsForce(Primitive):
        ...
    class WalkThroughGUP(GlobalUtilityPlugin):
        ...
    class Wall(GeometryClass):
        GENERATE_MAPPING_COORDS: int
        HEIGHT: float
        JUSTIFICATION: int
        WIDTH: float
        ...
    class WallRepelBehavior(ReferenceTarget):
        DISPLAYFORCE: bool
        FALLOFF: float
        FORCECOLOR: MXSWrapperBase
        GRIDEND: bool
        GRIDSPACING: int
        INNERDISTANCE: float
        NAME: str
        OUTERDISTANCE: float
        REPELDIRECTION: int
        REPELGRIDS: MXSWrapperBase
        REPELMETHOD: int
        SHOWDISTANCE: bool
        USEDISTANCE: bool
        ...
    class WallSeekBehavior(ReferenceTarget):
        DISPLAYFORCE: bool
        FALLOFF: float
        FORCECOLOR: MXSWrapperBase
        GRIDEND: bool
        GRIDSPACING: int
        INNERDISTANCE: float
        NAME: str
        OUTERDISTANCE: float
        SEEKDIRECTION: int
        SEEKGRID: None
        SEEKMETHOD: int
        SHOWDISTANCE: bool
        USEDISTANCE: bool
        ...
    class Wall_Repel_Behavior(ReferenceTarget):
        DISPLAYFORCE: bool
        FALLOFF: float
        FORCECOLOR: MXSWrapperBase
        GRIDEND: bool
        GRIDSPACING: int
        INNERDISTANCE: float
        NAME: str
        OUTERDISTANCE: float
        REPELDIRECTION: int
        REPELGRIDS: MXSWrapperBase
        REPELMETHOD: int
        SHOWDISTANCE: bool
        USEDISTANCE: bool
        ...
    class Wall_Seek_Behavior(ReferenceTarget):
        DISPLAYFORCE: bool
        FALLOFF: float
        FORCECOLOR: MXSWrapperBase
        GRIDEND: bool
        GRIDSPACING: int
        INNERDISTANCE: float
        NAME: str
        OUTERDISTANCE: float
        SEEKDIRECTION: int
        SEEKGRID: None
        SEEKMETHOD: int
        SHOWDISTANCE: bool
        USEDISTANCE: bool
        ...
    class WalledRectangle(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        MAPCOORDS: bool
        OPTIMIZE: bool
        QUAD_CAP: bool
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        TWIST_CORRECTION: bool
        TYPEIN_CREATIONMETHOD: bool
        TYPEIN_LENGTH: float
        TYPEIN_RADIUS2: float
        TYPEIN_RADIUS: float
        TYPEIN_THICKNESS: float
        TYPEIN_WIDTH: float
        TYPEIN_X: float
        TYPEIN_Y: float
        TYPEIN_Z: float
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        WRECT_LENGTH: float
        WRECT_RADIUS2: float
        WRECT_RADIUS: float
        WRECT_SYNCCORNERFILLETS: bool
        WRECT_THICKNESS: float
        WRECT_WIDTH: float
        ...
    class WanderBehavior(ReferenceTarget):
        DISPLAYFORCE: bool
        FORCECOLOR: MXSWrapperBase
        NAME: str
        PERIOD: int
        PERIODDEVIATION: float
        SEED: int
        TURNANGLE: float
        TURNPERIOD: float
        TURNPERIODDEVIATION: float
        ...
    class Wander_Behavior(ReferenceTarget):
        DISPLAYFORCE: bool
        FORCECOLOR: MXSWrapperBase
        NAME: str
        PERIOD: int
        PERIODDEVIATION: float
        SEED: int
        TURNANGLE: float
        TURNPERIOD: float
        TURNPERIODDEVIATION: float
        ...
    class Water(TextureMap):
        AMPLITUDE: float
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COORDS: MXSWrapperBase
        DISTRIBUTION: int
        MAP1: None
        MAP1ON: bool
        MAP2: None
        MAP2ON: bool
        NUMWAVESETS: int
        PHASE: float
        RANDOMSEED: int
        WAVELENMAX: float
        WAVELENMIN: float
        WAVERADIUS: float
        ...
    class Wave(Modifier):
        AMPLITUDE1: float
        AMPLITUDE2: float
        DECAY: float
        PHASE: float
        WAVELENGTH: float
        ...
    class WaveMaster(SoundClass):
        ...
    class WaveObject(SoundClass):
        ...
    class Wavebinding(SpacewarpModifier):
        ...
    class Waveform_Float(FloatController):
        ...
    class WeightShift(FloatController):
        ...
    class WeightedNormalsMod(Modifier):
        BLENDINGCOEFF: float
        BOUNDARYCOEFF: float
        DISPLAYNORMALS: bool
        HARDEDGEANGLE: float
        NORMALLENGTH: float
        RELAXATIONCOEFF: float
        SMOOTHINGCOEFF: float
        SMOOTHINGITERLIMIT: int
        SNAPTOLARGESTFACE: bool
        USEANGLEWEIGHT: bool
        USEAREAWEIGHT: bool
        USECONVEXANGLE: bool
        USEHARDEDGEANGLE: bool
        USESMOOTHINGGROUPS: bool
        USETOTALCOPLANARAREA: bool
        USEUVSEAMS: bool
        UVCHANNELINDEX: int
        ...
    class Weighted_Normals(Modifier):
        BLENDINGCOEFF: float
        BOUNDARYCOEFF: float
        DISPLAYNORMALS: bool
        HARDEDGEANGLE: float
        NORMALLENGTH: float
        RELAXATIONCOEFF: float
        SMOOTHINGCOEFF: float
        SMOOTHINGITERLIMIT: int
        SNAPTOLARGESTFACE: bool
        USEANGLEWEIGHT: bool
        USEAREAWEIGHT: bool
        USECONVEXANGLE: bool
        USEHARDEDGEANGLE: bool
        USESMOOTHINGGROUPS: bool
        USETOTALCOPLANARAREA: bool
        USEUVSEAMS: bool
        UVCHANNELINDEX: int
        ...
    class WelcomeScreenLaunchCount(Primitive):
        ...
    class WelcomeScreenShowAtStartup(Primitive):
        ...
    class Welder(Modifier):
        DONTWELDSELECTEDEDGES: bool
        THRESHOLD: float
        WELDMETHOD: int
        ...
    class WideFlange(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        MAPCOORDS: bool
        OPTIMIZE: bool
        QUAD_CAP: bool
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        TWIST_CORRECTION: bool
        TYPEIN_CREATIONMETHOD: bool
        TYPEIN_LENGTH: float
        TYPEIN_RADIUS: float
        TYPEIN_THICKNESS: float
        TYPEIN_WIDTH: float
        TYPEIN_X: float
        TYPEIN_Y: float
        TYPEIN_Z: float
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        WIDE_FLANGE_LENGTH: float
        WIDE_FLANGE_RADIUS: float
        WIDE_FLANGE_THICKNESS: float
        WIDE_FLANGE_WIDTH: float
        ...
    class Wind(SpacewarpObject):
        DECAY: float
        FREQUENCY: float
        HOOPSON: bool
        ICONSIZE: float
        SCALE: MXSWrapperBase
        STRENGTH: float
        TURBULENCE: float
        WINDTYPE: int
        ...
    class Windbinding(SpacewarpModifier):
        ...
    class WindowStream(Value):
        ...
    class Wipe(VideoPostFilter):
        ...
    class WireFloat(FloatController):
        ...
    class WirePoint3(Point3Controller):
        ...
    class WirePoint4(Point4Controller):
        ...
    class WirePosition(PositionController):
        ...
    class WireRotation(RotationController):
        ...
    class WireScale(ScaleController):
        ...
    class WireframeFragment(GraphicsFragmentPlugin):
        ...
    class Wood(TextureMap):
        ...
    class WorkingPivot(Interface):
        ...
    class WorkspaceManager(Interface):
        ...
    class WorldAlignObject(MappedPrimitive):
        ...
    class WorldAlignPivot(MappedPrimitive):
        ...
    class WorldSpaceSubdivideMod(SpacewarpModifier):
        ADAPTIVEEDGELENGTH: float
        ADAPTIVEREGULARITY: float
        ADAPTIVETHRESHOLD: float
        DELAUNAYRELAXATIONCOEFF: float
        DELAUNAYRELAXATIONITERATIONS: int
        DELAUNAYSIZE: float
        MANUALUPDATE: int
        PRESERVEDMAPINDEX: int
        PRESERVEDSHARPEDGEANGLE: float
        PRESERVEMESHDATA: bool
        PRESERVESHARPEDGESBYANGLE: bool
        REMESHTYPE: int
        SHOWALLTRIANGLES: bool
        SIZE: float
        SUBDIVIDEDIAGONALRATIO: float
        SUBDIVIDEDOENFORCEQUALITY: bool
        SUBDIVIDEDOFORMQUADS: bool
        SUBDIVIDEDOSUBDIVIDETRIANGLES: bool
        SUBDIVIDEMAXSTEINERPOINTS: int
        SUBDIVIDENUMBUCKETS: int
        SUBDIVIDEQUADAREARATIO: float
        SUBDIVIDEREFINEMENTTYPE: int
        VARIABLECURVATUREEDGELENGTH: float
        VARIABLECURVATUREITERATIONS: int
        VARIABLECURVATUREREGULARITY: float
        VARIABLECURVATURETHRESHOLD: float
        VARIABLECURVATURETRANSITION: float
        VARIABLECURVATUREVARIABLEDENSITY: float
        ...
    class WriteByte(Primitive):
        ...
    class WriteDouble(Primitive):
        ...
    class WriteFloat(Primitive):
        ...
    class WriteFloatAsDouble(Primitive):
        ...
    class WriteLong(Primitive):
        ...
    class WriteLongLong(Primitive):
        ...
    class WriteShort(Primitive):
        ...
    class WriteString(Primitive):
        ...
    class WsmBehavior(ReferenceTarget):
        DISPLAYFORCE: bool
        FORCECOLOR: MXSWrapperBase
        NAME: str
        SPACEWARP: None
        ...
    class XForm(Modifier):
        PRESERVENORMALS: bool
        ...
    class XFormMat(Generic):
        ...
    class XMLImp2(ImporterPlugin):
        ...
    class XORRenderFragment(GraphicsFragmentPlugin):
        ...
    class XRefAtmosWrapper(Atmospheric):
        ...
    class XRefObject(System):
        ...
    class XRefScene(Value):
        ...
    class XRef_Controller(Matrix3Controller):
        ...
    class XRef_Material(Material):
        ENABLEOVERRIDE: bool
        OVERRIDEMATERIAL: MXSWrapperBase
        ...
    class XRefmaterial(Material):
        ENABLEOVERRIDE: bool
        OVERRIDEMATERIAL: MXSWrapperBase
        ...
    class XYZGenClass(Material):
        ...
    class YUV(BitmapIO):
        ...
    class ZRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ZMAX: float
        ZMIN: float
        ZUPDATE: bool
        ...
    class Z_Depth(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ZMAX: float
        ZMIN: float
        ZUPDATE: bool
        ...
    class Zero(MappedGeneric):
        ...
    class Zoom(Generic):
        ...
    class Abs(Generic):
        ...
    class Acos(Generic):
        ...
    class ActionMan(Interface):
        ...
    class Add(VideoPostFilter):
        ...
    class AddAndWeld(NodeGeneric):
        ...
    class AddAtmospheric(Primitive):
        ...
    class AddEaseCurve(MappedGeneric):
        ...
    class AddEffect(Primitive):
        ...
    class AddKnot(NodeGeneric):
        ...
    class AddModifier(NodeGeneric):
        ...
    class AddModifierWithLocalData(Primitive):
        ...
    class AddMorphTarget(Primitive):
        ...
    class AddMultiplierCurve(Generic):
        ...
    class AddNURBSSet(Primitive):
        ...
    class AddNewKey(MappedGeneric):
        ...
    class AddNewNoteKey(Generic):
        ...
    class AddNewSpline(NodeGeneric):
        ...
    class AddNoteTrack(Primitive):
        ...
    class AddPluginRollouts(Generic):
        ...
    class AddRollout(Primitive):
        ...
    class AddScript(BipedGeneric):
        ...
    class AddSnippet(BipedGeneric):
        ...
    class AddTrackViewController(Primitive):
        ...
    class AddTranInfo(BipedGeneric):
        ...
    class AddTransition(BipedGeneric):
        ...
    class AffectRegionVal(Primitive):
        ...
    class AiPBParameter(ReferenceTarget):
        ...
    class AiPBParameterClassDescCreator(Interface):
        ...
    class Ai_Max_Adapter(TextureMap):
        ...
    class Ai_Max_UVGenerator(TextureMap):
        ...
    class Ai_Abs(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Add(TextureMap):
        INPUT1: MXSWrapperBase
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        INPUT2: MXSWrapperBase
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        ...
    class Ai_Ambient_Occlusion(TextureMap):
        BLACK: MXSWrapperBase
        BLACK_CONNECTED: bool
        BLACK_SHADER: None
        FALLOFF: float
        FALLOFF_CONNECTED: bool
        FALLOFF_SHADER: None
        FAR_CLIP: float
        FAR_CLIP_CONNECTED: bool
        FAR_CLIP_SHADER: None
        INCLUSIVE: bool
        INVERT_NORMALS: bool
        NEAR_CLIP: float
        NEAR_CLIP_CONNECTED: bool
        NEAR_CLIP_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        SAMPLES: int
        SELF_ONLY: bool
        SPREAD: float
        SPREAD_CONNECTED: bool
        SPREAD_SHADER: None
        TRACE_SET: str
        WHITE: MXSWrapperBase
        WHITE_CONNECTED: bool
        WHITE_SHADER: None
        ...
    class Ai_Aov_Read_Float(TextureMap):
        AOV_NAME: str
        ...
    class Ai_Aov_Read_Int(TextureMap):
        AOV_NAME: str
        ...
    class Ai_Aov_Read_Rgb(TextureMap):
        AOV_NAME: str
        ...
    class Ai_Aov_Read_Rgba(TextureMap):
        AOV_NAME: str
        ...
    class Ai_Aov_Write_Float(Material):
        AOV_INPUT: float
        AOV_INPUT_CONNECTED: bool
        AOV_INPUT_SHADER: None
        AOV_NAME: str
        BLEND_OPACITY: bool
        PASSTHROUGH: None
        ...
    class Ai_Aov_Write_Int(Material):
        AOV_INPUT: int
        AOV_INPUT_CONNECTED: bool
        AOV_INPUT_SHADER: None
        AOV_NAME: str
        PASSTHROUGH: None
        ...
    class Ai_Aov_Write_Rgb(Material):
        AOV_INPUT: MXSWrapperBase
        AOV_INPUT_CONNECTED: bool
        AOV_INPUT_SHADER: None
        AOV_NAME: str
        BLEND_OPACITY: bool
        PASSTHROUGH: None
        ...
    class Ai_Aov_Write_Rgba(Material):
        AOV_INPUT: MXSWrapperBase
        AOV_INPUT_CONNECTED: bool
        AOV_INPUT_SHADER: None
        AOV_NAME: str
        BLEND_OPACITY: bool
        PASSTHROUGH: None
        ...
    class Ai_Aov_Write_Vector(Material):
        AOV_INPUT: MXSWrapperBase
        AOV_INPUT_CONNECTED: bool
        AOV_INPUT_SHADER: None
        AOV_NAME: str
        BLEND_OPACITY: bool
        PASSTHROUGH: None
        ...
    class Ai_Atan(TextureMap):
        UNITS: int
        X: MXSWrapperBase
        X_CONNECTED: bool
        X_SHADER: None
        Y: MXSWrapperBase
        Y_CONNECTED: bool
        Y_SHADER: None
        ...
    class Ai_Atmosphere_Volume(Material):
        AFFECT_CAMERA: float
        AFFECT_CAMERA_CONNECTED: bool
        AFFECT_CAMERA_SHADER: None
        AFFECT_DIFFUSE: float
        AFFECT_DIFFUSE_CONNECTED: bool
        AFFECT_DIFFUSE_SHADER: None
        AFFECT_SPECULAR: float
        AFFECT_SPECULAR_CONNECTED: bool
        AFFECT_SPECULAR_SHADER: None
        ATTENUATION: float
        ATTENUATION_CONNECTED: bool
        ATTENUATION_SHADER: None
        DENSITY: float
        DENSITY_CONNECTED: bool
        DENSITY_SHADER: None
        ECCENTRICITY: float
        ECCENTRICITY_CONNECTED: bool
        ECCENTRICITY_SHADER: None
        RGB_ATTENUATION: MXSWrapperBase
        RGB_ATTENUATION_CONNECTED: bool
        RGB_ATTENUATION_SHADER: None
        RGB_DENSITY: MXSWrapperBase
        RGB_DENSITY_CONNECTED: bool
        RGB_DENSITY_SHADER: None
        SAMPLES: int
        ...
    class Ai_Barndoor(TextureMap):
        ...
    class Ai_Blackbody(TextureMap):
        INTENSITY: float
        INTENSITY_CONNECTED: bool
        INTENSITY_SHADER: None
        NORMALIZE: bool
        TEMPERATURE: float
        TEMPERATURE_CONNECTED: bool
        TEMPERATURE_SHADER: None
        ...
    class Ai_Blackman_Harris_Filter(TextureMap):
        ...
    class Ai_Box_Filter(TextureMap):
        ...
    class Ai_Bump2D(TextureMap):
        BUMP_HEIGHT: float
        BUMP_HEIGHT_CONNECTED: bool
        BUMP_HEIGHT_SHADER: None
        BUMP_MAP: float
        BUMP_MAP_CONNECTED: bool
        BUMP_MAP_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        ...
    class Ai_Bump3D(TextureMap):
        BUMP_HEIGHT: float
        BUMP_HEIGHT_CONNECTED: bool
        BUMP_HEIGHT_SHADER: None
        BUMP_MAP: float
        BUMP_MAP_CONNECTED: bool
        BUMP_MAP_SHADER: None
        EPSILON: float
        EPSILON_CONNECTED: bool
        EPSILON_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        ...
    class Ai_Cache(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Camera_Projection(TextureMap):
        ASPECT_RATIO: float
        BACK_FACING: bool
        CAMERA: None
        CAMERA_CONNECTED: bool
        CAMERA_SHADER: None
        COORD_SPACE: int
        FRONT_FACING: bool
        MASK: float
        MASK_CONNECTED: bool
        MASK_SHADER: None
        OFFSCREEN_COLOR: MXSWrapperBase
        OFFSCREEN_COLOR_CONNECTED: bool
        OFFSCREEN_COLOR_SHADER: None
        P: MXSWrapperBase
        PREF_NAME: str
        PROJECTION_COLOR: MXSWrapperBase
        PROJECTION_COLOR_CONNECTED: bool
        PROJECTION_COLOR_SHADER: None
        P_CONNECTED: bool
        P_SHADER: None
        USE_SHADING_NORMAL: bool
        ...
    class Ai_Car_Paint(Material):
        BASE: float
        BASE_COLOR: MXSWrapperBase
        BASE_COLOR_CONNECTED: bool
        BASE_COLOR_SHADER: None
        BASE_CONNECTED: bool
        BASE_ROUGHNESS: float
        BASE_ROUGHNESS_CONNECTED: bool
        BASE_ROUGHNESS_SHADER: None
        BASE_SHADER: None
        COAT: float
        COAT_COLOR: MXSWrapperBase
        COAT_COLOR_CONNECTED: bool
        COAT_COLOR_SHADER: None
        COAT_CONNECTED: bool
        COAT_IOR: float
        COAT_IOR_CONNECTED: bool
        COAT_IOR_SHADER: None
        COAT_NORMAL: MXSWrapperBase
        COAT_NORMAL_CONNECTED: bool
        COAT_NORMAL_SHADER: None
        COAT_ROUGHNESS: float
        COAT_ROUGHNESS_CONNECTED: bool
        COAT_ROUGHNESS_SHADER: None
        COAT_SHADER: None
        FLAKE_COLOR: MXSWrapperBase
        FLAKE_COLOR_CONNECTED: bool
        FLAKE_COLOR_SHADER: None
        FLAKE_COORD_SPACE: int
        FLAKE_DENSITY: float
        FLAKE_DENSITY_CONNECTED: bool
        FLAKE_DENSITY_SHADER: None
        FLAKE_FALLOFF: float
        FLAKE_FALLOFF_CONNECTED: bool
        FLAKE_FALLOFF_SHADER: None
        FLAKE_FLIP_FLOP: MXSWrapperBase
        FLAKE_FLIP_FLOP_CONNECTED: bool
        FLAKE_FLIP_FLOP_SHADER: None
        FLAKE_IOR: float
        FLAKE_IOR_CONNECTED: bool
        FLAKE_IOR_SHADER: None
        FLAKE_LAYERS: int
        FLAKE_LAYERS_CONNECTED: bool
        FLAKE_LAYERS_SHADER: None
        FLAKE_LIGHT_FACING: MXSWrapperBase
        FLAKE_LIGHT_FACING_CONNECTED: bool
        FLAKE_LIGHT_FACING_SHADER: None
        FLAKE_NORMAL_RANDOMIZE: float
        FLAKE_NORMAL_RANDOMIZE_CONNECTED: bool
        FLAKE_NORMAL_RANDOMIZE_SHADER: None
        FLAKE_ROUGHNESS: float
        FLAKE_ROUGHNESS_CONNECTED: bool
        FLAKE_ROUGHNESS_SHADER: None
        FLAKE_SCALE: float
        FLAKE_SCALE_CONNECTED: bool
        FLAKE_SCALE_SHADER: None
        PREF_NAME: str
        SPECULAR: float
        SPECULAR_COLOR: MXSWrapperBase
        SPECULAR_COLOR_CONNECTED: bool
        SPECULAR_COLOR_SHADER: None
        SPECULAR_CONNECTED: bool
        SPECULAR_FALLOFF: float
        SPECULAR_FALLOFF_CONNECTED: bool
        SPECULAR_FALLOFF_SHADER: None
        SPECULAR_FLIP_FLOP: MXSWrapperBase
        SPECULAR_FLIP_FLOP_CONNECTED: bool
        SPECULAR_FLIP_FLOP_SHADER: None
        SPECULAR_IOR: float
        SPECULAR_IOR_CONNECTED: bool
        SPECULAR_IOR_SHADER: None
        SPECULAR_LIGHT_FACING: MXSWrapperBase
        SPECULAR_LIGHT_FACING_CONNECTED: bool
        SPECULAR_LIGHT_FACING_SHADER: None
        SPECULAR_ROUGHNESS: float
        SPECULAR_ROUGHNESS_CONNECTED: bool
        SPECULAR_ROUGHNESS_SHADER: None
        SPECULAR_SHADER: None
        TRANSMISSION_COLOR: MXSWrapperBase
        TRANSMISSION_COLOR_CONNECTED: bool
        TRANSMISSION_COLOR_SHADER: None
        ...
    class Ai_Catrom_Filter(TextureMap):
        ...
    class Ai_Cell_Noise(TextureMap):
        ADDITIVE: bool
        AMPLITUDE: float
        AMPLITUDE_CONNECTED: bool
        AMPLITUDE_SHADER: None
        COLOR: MXSWrapperBase
        COLOR_CONNECTED: bool
        COLOR_SHADER: None
        COORD_SPACE: int
        DENSITY: float
        DENSITY_CONNECTED: bool
        DENSITY_SHADER: None
        LACUNARITY: float
        LACUNARITY_CONNECTED: bool
        LACUNARITY_SHADER: None
        OCTAVES: int
        OFFSET: MXSWrapperBase
        OFFSET_CONNECTED: bool
        OFFSET_SHADER: None
        P: MXSWrapperBase
        PALETTE: MXSWrapperBase
        PALETTE_CONNECTED: bool
        PALETTE_SHADER: None
        PATTERN: int
        PREF_NAME: str
        P_CONNECTED: bool
        P_SHADER: None
        RANDOMNESS: float
        RANDOMNESS_CONNECTED: bool
        RANDOMNESS_SHADER: None
        SCALE: MXSWrapperBase
        SCALE_CONNECTED: bool
        SCALE_SHADER: None
        TIME: float
        TIME_CONNECTED: bool
        TIME_SHADER: None
        ...
    class Ai_Checkerboard(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR1_CONNECTED: bool
        COLOR1_SHADER: None
        COLOR2: MXSWrapperBase
        COLOR2_CONNECTED: bool
        COLOR2_SHADER: None
        CONTRAST: float
        CONTRAST_CONNECTED: bool
        CONTRAST_SHADER: None
        FILTER_OFFSET: float
        FILTER_OFFSET_CONNECTED: bool
        FILTER_OFFSET_SHADER: None
        FILTER_STRENGTH: float
        FILTER_STRENGTH_CONNECTED: bool
        FILTER_STRENGTH_SHADER: None
        UVSET: str
        U_FREQUENCY: float
        U_FREQUENCY_CONNECTED: bool
        U_FREQUENCY_SHADER: None
        U_OFFSET: float
        U_OFFSET_CONNECTED: bool
        U_OFFSET_SHADER: None
        V_FREQUENCY: float
        V_FREQUENCY_CONNECTED: bool
        V_FREQUENCY_SHADER: None
        V_OFFSET: float
        V_OFFSET_CONNECTED: bool
        V_OFFSET_SHADER: None
        ...
    class Ai_Clamp(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        MAX: float
        MAX_COLOR: MXSWrapperBase
        MAX_COLOR_CONNECTED: bool
        MAX_COLOR_SHADER: None
        MAX_CONNECTED: bool
        MAX_SHADER: None
        MIN: float
        MIN_COLOR: MXSWrapperBase
        MIN_COLOR_CONNECTED: bool
        MIN_COLOR_SHADER: None
        MIN_CONNECTED: bool
        MIN_SHADER: None
        MODE: int
        MODE_CONNECTED: bool
        MODE_SHADER: None
        ...
    class Ai_Clip_Geo(Material):
        INCLUSIVE: bool
        INTERSECTION: None
        TRACE_SET: str
        ...
    class Ai_Closest_Filter(TextureMap):
        ...
    class Ai_Collection(TextureMap):
        ...
    class Ai_Color_Convert(TextureMap):
        FROM: int
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        TO: int
        ...
    class Ai_Color_Correct(TextureMap):
        ADD: MXSWrapperBase
        ADD_CONNECTED: bool
        ADD_SHADER: None
        ALPHA_ADD: float
        ALPHA_ADD_CONNECTED: bool
        ALPHA_ADD_SHADER: None
        ALPHA_IS_LUMINANCE: bool
        ALPHA_MULTIPLY: float
        ALPHA_MULTIPLY_CONNECTED: bool
        ALPHA_MULTIPLY_SHADER: None
        CONTRAST: float
        CONTRAST_CONNECTED: bool
        CONTRAST_PIVOT: float
        CONTRAST_PIVOT_CONNECTED: bool
        CONTRAST_PIVOT_SHADER: None
        CONTRAST_SHADER: None
        EXPOSURE: float
        EXPOSURE_CONNECTED: bool
        EXPOSURE_SHADER: None
        GAMMA: float
        GAMMA_CONNECTED: bool
        GAMMA_SHADER: None
        HUE_SHIFT: float
        HUE_SHIFT_CONNECTED: bool
        HUE_SHIFT_SHADER: None
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        INVERT: bool
        INVERT_ALPHA: bool
        MASK: float
        MASK_CONNECTED: bool
        MASK_SHADER: None
        MULTIPLY: MXSWrapperBase
        MULTIPLY_CONNECTED: bool
        MULTIPLY_SHADER: None
        SATURATION: float
        SATURATION_CONNECTED: bool
        SATURATION_SHADER: None
        ...
    class Ai_Color_Jitter(TextureMap):
        DATA_GAIN_MAX: float
        DATA_GAIN_MAX_CONNECTED: bool
        DATA_GAIN_MAX_SHADER: None
        DATA_GAIN_MIN: float
        DATA_GAIN_MIN_CONNECTED: bool
        DATA_GAIN_MIN_SHADER: None
        DATA_HUE_MAX: float
        DATA_HUE_MAX_CONNECTED: bool
        DATA_HUE_MAX_SHADER: None
        DATA_HUE_MIN: float
        DATA_HUE_MIN_CONNECTED: bool
        DATA_HUE_MIN_SHADER: None
        DATA_INPUT: int
        DATA_INPUT_CONNECTED: bool
        DATA_INPUT_SHADER: None
        DATA_SATURATION_MAX: float
        DATA_SATURATION_MAX_CONNECTED: bool
        DATA_SATURATION_MAX_SHADER: None
        DATA_SATURATION_MIN: float
        DATA_SATURATION_MIN_CONNECTED: bool
        DATA_SATURATION_MIN_SHADER: None
        DATA_SEED: int
        DATA_SEED_CONNECTED: bool
        DATA_SEED_SHADER: None
        FACE_GAIN_MAX: float
        FACE_GAIN_MAX_CONNECTED: bool
        FACE_GAIN_MAX_SHADER: None
        FACE_GAIN_MIN: float
        FACE_GAIN_MIN_CONNECTED: bool
        FACE_GAIN_MIN_SHADER: None
        FACE_HUE_MAX: float
        FACE_HUE_MAX_CONNECTED: bool
        FACE_HUE_MAX_SHADER: None
        FACE_HUE_MIN: float
        FACE_HUE_MIN_CONNECTED: bool
        FACE_HUE_MIN_SHADER: None
        FACE_MODE: int
        FACE_SATURATION_MAX: float
        FACE_SATURATION_MAX_CONNECTED: bool
        FACE_SATURATION_MAX_SHADER: None
        FACE_SATURATION_MIN: float
        FACE_SATURATION_MIN_CONNECTED: bool
        FACE_SATURATION_MIN_SHADER: None
        FACE_SEED: int
        FACE_SEED_CONNECTED: bool
        FACE_SEED_SHADER: None
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        OBJ_GAIN_MAX: float
        OBJ_GAIN_MAX_CONNECTED: bool
        OBJ_GAIN_MAX_SHADER: None
        OBJ_GAIN_MIN: float
        OBJ_GAIN_MIN_CONNECTED: bool
        OBJ_GAIN_MIN_SHADER: None
        OBJ_HUE_MAX: float
        OBJ_HUE_MAX_CONNECTED: bool
        OBJ_HUE_MAX_SHADER: None
        OBJ_HUE_MIN: float
        OBJ_HUE_MIN_CONNECTED: bool
        OBJ_HUE_MIN_SHADER: None
        OBJ_SATURATION_MAX: float
        OBJ_SATURATION_MAX_CONNECTED: bool
        OBJ_SATURATION_MAX_SHADER: None
        OBJ_SATURATION_MIN: float
        OBJ_SATURATION_MIN_CONNECTED: bool
        OBJ_SATURATION_MIN_SHADER: None
        OBJ_SEED: int
        OBJ_SEED_CONNECTED: bool
        OBJ_SEED_SHADER: None
        PROC_GAIN_MAX: float
        PROC_GAIN_MAX_CONNECTED: bool
        PROC_GAIN_MAX_SHADER: None
        PROC_GAIN_MIN: float
        PROC_GAIN_MIN_CONNECTED: bool
        PROC_GAIN_MIN_SHADER: None
        PROC_HUE_MAX: float
        PROC_HUE_MAX_CONNECTED: bool
        PROC_HUE_MAX_SHADER: None
        PROC_HUE_MIN: float
        PROC_HUE_MIN_CONNECTED: bool
        PROC_HUE_MIN_SHADER: None
        PROC_SATURATION_MAX: float
        PROC_SATURATION_MAX_CONNECTED: bool
        PROC_SATURATION_MAX_SHADER: None
        PROC_SATURATION_MIN: float
        PROC_SATURATION_MIN_CONNECTED: bool
        PROC_SATURATION_MIN_SHADER: None
        PROC_SEED: int
        PROC_SEED_CONNECTED: bool
        PROC_SEED_SHADER: None
        ...
    class Ai_Compare(TextureMap):
        INPUT1: float
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        INPUT2: float
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        TEST: int
        ...
    class Ai_Complement(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Complex_Ior(TextureMap):
        ...
    class Ai_Composite(TextureMap):
        ...
    class Ai_Contour_Filter(TextureMap):
        ...
    class Ai_Cross(TextureMap):
        INPUT1: MXSWrapperBase
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        INPUT2: MXSWrapperBase
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        ...
    class Ai_Cryptomatte(TextureMap):
        AOV_CRYPTO_ASSET: str
        AOV_CRYPTO_ASSET_CONNECTED: bool
        AOV_CRYPTO_ASSET_SHADER: None
        AOV_CRYPTO_MATERIAL: str
        AOV_CRYPTO_MATERIAL_CONNECTED: bool
        AOV_CRYPTO_MATERIAL_SHADER: None
        AOV_CRYPTO_OBJECT: str
        AOV_CRYPTO_OBJECT_CONNECTED: bool
        AOV_CRYPTO_OBJECT_SHADER: None
        CRYPTOMATTE_DEPTH: int
        CRYPTOMATTE_DEPTH_CONNECTED: bool
        CRYPTOMATTE_DEPTH_SHADER: None
        PREVIEW_IN_EXR: bool
        PREVIEW_IN_EXR_CONNECTED: bool
        PREVIEW_IN_EXR_SHADER: None
        PROCESS_LEGACY: bool
        PROCESS_LEGACY_CONNECTED: bool
        PROCESS_LEGACY_SHADER: None
        PROCESS_MAT_PATH_PIPES: bool
        PROCESS_MAT_PATH_PIPES_CONNECTED: bool
        PROCESS_MAT_PATH_PIPES_SHADER: None
        PROCESS_MAYA: bool
        PROCESS_MAYA_CONNECTED: bool
        PROCESS_MAYA_SHADER: None
        PROCESS_OBJ_PATH_PIPES: bool
        PROCESS_OBJ_PATH_PIPES_CONNECTED: bool
        PROCESS_OBJ_PATH_PIPES_SHADER: None
        PROCESS_PATHS: bool
        PROCESS_PATHS_CONNECTED: bool
        PROCESS_PATHS_SHADER: None
        SIDECAR_MANIFESTS: bool
        SIDECAR_MANIFESTS_CONNECTED: bool
        SIDECAR_MANIFESTS_SHADER: None
        STRIP_MAT_NAMESPACES: bool
        STRIP_MAT_NAMESPACES_CONNECTED: bool
        STRIP_MAT_NAMESPACES_SHADER: None
        STRIP_OBJ_NAMESPACES: bool
        STRIP_OBJ_NAMESPACES_CONNECTED: bool
        STRIP_OBJ_NAMESPACES_SHADER: None
        USER_CRYPTO_AOV_0: str
        USER_CRYPTO_AOV_0_CONNECTED: bool
        USER_CRYPTO_AOV_0_SHADER: None
        USER_CRYPTO_AOV_1: str
        USER_CRYPTO_AOV_1_CONNECTED: bool
        USER_CRYPTO_AOV_1_SHADER: None
        USER_CRYPTO_AOV_2: str
        USER_CRYPTO_AOV_2_CONNECTED: bool
        USER_CRYPTO_AOV_2_SHADER: None
        USER_CRYPTO_AOV_3: str
        USER_CRYPTO_AOV_3_CONNECTED: bool
        USER_CRYPTO_AOV_3_SHADER: None
        USER_CRYPTO_SRC_0: str
        USER_CRYPTO_SRC_0_CONNECTED: bool
        USER_CRYPTO_SRC_0_SHADER: None
        USER_CRYPTO_SRC_1: str
        USER_CRYPTO_SRC_1_CONNECTED: bool
        USER_CRYPTO_SRC_1_SHADER: None
        USER_CRYPTO_SRC_2: str
        USER_CRYPTO_SRC_2_CONNECTED: bool
        USER_CRYPTO_SRC_2_SHADER: None
        USER_CRYPTO_SRC_3: str
        USER_CRYPTO_SRC_3_CONNECTED: bool
        USER_CRYPTO_SRC_3_SHADER: None
        ...
    class Ai_Cryptomatte_Filter(TextureMap):
        ...
    class Ai_Curvature(TextureMap):
        BIAS: float
        BIAS_CONNECTED: bool
        BIAS_SHADER: None
        INCLUSIVE: bool
        MULTIPLY: float
        MULTIPLY_CONNECTED: bool
        MULTIPLY_SHADER: None
        OUTPUT: int
        RADIUS: float
        RADIUS_CONNECTED: bool
        RADIUS_SHADER: None
        SAMPLES: int
        SELF_ONLY: bool
        SPREAD: float
        SPREAD_CONNECTED: bool
        SPREAD_SHADER: None
        THRESHOLD: float
        THRESHOLD_CONNECTED: bool
        THRESHOLD_SHADER: None
        TRACE_SET: str
        ...
    class Ai_Denoise_Optix_Filter(TextureMap):
        ...
    class Ai_Diff_Filter(TextureMap):
        ...
    class Ai_Disable(TextureMap):
        ...
    class Ai_Divide(TextureMap):
        INPUT1: MXSWrapperBase
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        INPUT2: MXSWrapperBase
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        ...
    class Ai_Dot(TextureMap):
        INPUT1: MXSWrapperBase
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        INPUT2: MXSWrapperBase
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        ...
    class Ai_Exp(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Facing_Ratio(TextureMap):
        BIAS: float
        GAIN: float
        INVERT: bool
        LINEAR: bool
        ...
    class Ai_Farthest_Filter(TextureMap):
        ...
    class Ai_Flakes(TextureMap):
        COORD_SPACE: int
        DENSITY: float
        DENSITY_CONNECTED: bool
        DENSITY_SHADER: None
        DEPTH: float
        DEPTH_CONNECTED: bool
        DEPTH_SHADER: None
        IOR: float
        IOR_CONNECTED: bool
        IOR_SHADER: None
        NORMAL_RANDOMIZE: float
        NORMAL_RANDOMIZE_CONNECTED: bool
        NORMAL_RANDOMIZE_SHADER: None
        OUTPUT_SPACE: int
        PREF_NAME: str
        SCALE: float
        SCALE_CONNECTED: bool
        SCALE_SHADER: None
        STEP: float
        STEP_CONNECTED: bool
        STEP_SHADER: None
        ...
    class Ai_Flat(TextureMap):
        COLOR: MXSWrapperBase
        COLOR_CONNECTED: bool
        COLOR_SHADER: None
        ...
    class Ai_Float_To_Int(TextureMap):
        INPUT: float
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        MODE: int
        MODE_CONNECTED: bool
        MODE_SHADER: None
        ...
    class Ai_Float_To_Matrix(TextureMap):
        INPUT_00: float
        INPUT_00_CONNECTED: bool
        INPUT_00_SHADER: None
        INPUT_01: float
        INPUT_01_CONNECTED: bool
        INPUT_01_SHADER: None
        INPUT_02: float
        INPUT_02_CONNECTED: bool
        INPUT_02_SHADER: None
        INPUT_03: float
        INPUT_03_CONNECTED: bool
        INPUT_03_SHADER: None
        INPUT_10: float
        INPUT_10_CONNECTED: bool
        INPUT_10_SHADER: None
        INPUT_11: float
        INPUT_11_CONNECTED: bool
        INPUT_11_SHADER: None
        INPUT_12: float
        INPUT_12_CONNECTED: bool
        INPUT_12_SHADER: None
        INPUT_13: float
        INPUT_13_CONNECTED: bool
        INPUT_13_SHADER: None
        INPUT_20: float
        INPUT_20_CONNECTED: bool
        INPUT_20_SHADER: None
        INPUT_21: float
        INPUT_21_CONNECTED: bool
        INPUT_21_SHADER: None
        INPUT_22: float
        INPUT_22_CONNECTED: bool
        INPUT_22_SHADER: None
        INPUT_23: float
        INPUT_23_CONNECTED: bool
        INPUT_23_SHADER: None
        INPUT_30: float
        INPUT_30_CONNECTED: bool
        INPUT_30_SHADER: None
        INPUT_31: float
        INPUT_31_CONNECTED: bool
        INPUT_31_SHADER: None
        INPUT_32: float
        INPUT_32_CONNECTED: bool
        INPUT_32_SHADER: None
        INPUT_33: float
        INPUT_33_CONNECTED: bool
        INPUT_33_SHADER: None
        ...
    class Ai_Float_To_Rgb(TextureMap):
        B: float
        B_CONNECTED: bool
        B_SHADER: None
        G: float
        G_CONNECTED: bool
        G_SHADER: None
        R: float
        R_CONNECTED: bool
        R_SHADER: None
        ...
    class Ai_Float_To_Rgba(TextureMap):
        A: float
        A_CONNECTED: bool
        A_SHADER: None
        B: float
        B_CONNECTED: bool
        B_SHADER: None
        G: float
        G_CONNECTED: bool
        G_SHADER: None
        R: float
        R_CONNECTED: bool
        R_SHADER: None
        ...
    class Ai_Fog(Material):
        COLOR: MXSWrapperBase
        COLOR_CONNECTED: bool
        COLOR_SHADER: None
        DISTANCE: float
        DISTANCE_CONNECTED: bool
        DISTANCE_SHADER: None
        GROUND_NORMAL: MXSWrapperBase
        GROUND_NORMAL_CONNECTED: bool
        GROUND_NORMAL_SHADER: None
        GROUND_POINT: MXSWrapperBase
        GROUND_POINT_CONNECTED: bool
        GROUND_POINT_SHADER: None
        HEIGHT: float
        HEIGHT_CONNECTED: bool
        HEIGHT_SHADER: None
        ...
    class Ai_Fraction(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Gaussian_Filter(TextureMap):
        ...
    class Ai_Gobo(TextureMap):
        ...
    class Ai_Hair(Material):
        ...
    class Ai_Heatmap_Filter(TextureMap):
        ...
    class Ai_Image(TextureMap):
        COLOR_SPACE: int
        FILENAME: str
        FILTER: int
        IGNORE_MISSING_TEXTURES: bool
        IMAGE_FRAME_NUMBER: int
        MIPMAP_BIAS: int
        MISSING_TEXTURE_COLOR: MXSWrapperBase
        MISSING_TEXTURE_COLOR_CONNECTED: bool
        MISSING_TEXTURE_COLOR_SHADER: None
        MULTIPLY: MXSWrapperBase
        MULTIPLY_CONNECTED: bool
        MULTIPLY_SHADER: None
        OFFSET: MXSWrapperBase
        OFFSET_CONNECTED: bool
        OFFSET_SHADER: None
        SFLIP: bool
        SINGLE_CHANNEL: bool
        SOFFSET: float
        SSCALE: float
        START_CHANNEL: int
        SWAP_ST: bool
        SWRAP: int
        TFLIP: bool
        TOFFSET: float
        TSCALE: float
        TWRAP: int
        UVCOORDS: MXSWrapperBase
        UVCOORDS_CONNECTED: bool
        UVCOORDS_SHADER: None
        UVSET: int
        ...
    class Ai_Imager_Color_Correct(TextureMap):
        ENABLE: bool
        HIGHLIGHTS_CONTRAST: float
        HIGHLIGHTS_GAIN: MXSWrapperBase
        HIGHLIGHTS_GAMMA: float
        HIGHLIGHTS_OFFSET: MXSWrapperBase
        HIGHLIGHTS_SATURATION: float
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        LAYER_SELECTION: str
        MAIN_CONTRAST: float
        MAIN_GAIN: MXSWrapperBase
        MAIN_GAMMA: float
        MAIN_OFFSET: MXSWrapperBase
        MAIN_SATURATION: float
        MIDTONES_CONTRAST: float
        MIDTONES_GAIN: MXSWrapperBase
        MIDTONES_GAMMA: float
        MIDTONES_OFFSET: MXSWrapperBase
        MIDTONES_SATURATION: float
        SHADOWS_CONTRAST: float
        SHADOWS_GAIN: MXSWrapperBase
        SHADOWS_GAMMA: float
        SHADOWS_OFFSET: MXSWrapperBase
        SHADOWS_SATURATION: float
        ...
    class Ai_Imager_Exposure(TextureMap):
        ENABLE: bool
        EXPOSURE: float
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        LAYER_SELECTION: str
        ...
    class Ai_Imager_Lens_Effects(TextureMap):
        ENABLE: bool
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        LAYER_SELECTION: str
        VIGNETTING: float
        ...
    class Ai_Imager_Tonemap(TextureMap):
        ENABLE: bool
        FILMIC_SHOULDER_ANGLE: float
        FILMIC_SHOULDER_LENGTH: float
        FILMIC_SHOULDER_STRENGTH: float
        FILMIC_TOE_LENGTH: float
        FILMIC_TOE_STRENGTH: float
        GAMMA: float
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        LAYER_SELECTION: str
        MODE: int
        PRESERVE_SATURATION: bool
        REINHARD_HIGHLIGHTS: float
        REINHARD_SHADOWS: float
        ...
    class Ai_Imager_White_Balance(TextureMap):
        CUSTOM: MXSWrapperBase
        ENABLE: bool
        ILLUMINANT: int
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        LAYER_SELECTION: str
        MODE: int
        TEMPERATURE: float
        ...
    class Ai_Include_Graph(TextureMap):
        ...
    class Ai_Is_Finite(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Lambert(Material):
        KD: float
        KD_COLOR: MXSWrapperBase
        KD_COLOR_CONNECTED: bool
        KD_COLOR_SHADER: None
        KD_CONNECTED: bool
        KD_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        OPACITY: MXSWrapperBase
        OPACITY_CONNECTED: bool
        OPACITY_SHADER: None
        ...
    class Ai_Layer_Float(TextureMap):
        ENABLE1: bool
        ENABLE2: bool
        ENABLE3: bool
        ENABLE4: bool
        ENABLE5: bool
        ENABLE6: bool
        ENABLE7: bool
        ENABLE8: bool
        INPUT1: float
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        INPUT2: float
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        INPUT3: float
        INPUT3_CONNECTED: bool
        INPUT3_SHADER: None
        INPUT4: float
        INPUT4_CONNECTED: bool
        INPUT4_SHADER: None
        INPUT5: float
        INPUT5_CONNECTED: bool
        INPUT5_SHADER: None
        INPUT6: float
        INPUT6_CONNECTED: bool
        INPUT6_SHADER: None
        INPUT7: float
        INPUT7_CONNECTED: bool
        INPUT7_SHADER: None
        INPUT8: float
        INPUT8_CONNECTED: bool
        INPUT8_SHADER: None
        MIX1: float
        MIX1_CONNECTED: bool
        MIX1_SHADER: None
        MIX2: float
        MIX2_CONNECTED: bool
        MIX2_SHADER: None
        MIX3: float
        MIX3_CONNECTED: bool
        MIX3_SHADER: None
        MIX4: float
        MIX4_CONNECTED: bool
        MIX4_SHADER: None
        MIX5: float
        MIX5_CONNECTED: bool
        MIX5_SHADER: None
        MIX6: float
        MIX6_CONNECTED: bool
        MIX6_SHADER: None
        MIX7: float
        MIX7_CONNECTED: bool
        MIX7_SHADER: None
        MIX8: float
        MIX8_CONNECTED: bool
        MIX8_SHADER: None
        NAME1: str
        NAME2: str
        NAME3: str
        NAME4: str
        NAME5: str
        NAME6: str
        NAME7: str
        NAME8: str
        ...
    class Ai_Layer_Rgba(TextureMap):
        ALPHA_OPERATION1: int
        ALPHA_OPERATION2: int
        ALPHA_OPERATION3: int
        ALPHA_OPERATION4: int
        ALPHA_OPERATION5: int
        ALPHA_OPERATION6: int
        ALPHA_OPERATION7: int
        ALPHA_OPERATION8: int
        CLAMP: bool
        ENABLE1: bool
        ENABLE2: bool
        ENABLE3: bool
        ENABLE4: bool
        ENABLE5: bool
        ENABLE6: bool
        ENABLE7: bool
        ENABLE8: bool
        INPUT1: MXSWrapperBase
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        INPUT2: MXSWrapperBase
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        INPUT3: MXSWrapperBase
        INPUT3_CONNECTED: bool
        INPUT3_SHADER: None
        INPUT4: MXSWrapperBase
        INPUT4_CONNECTED: bool
        INPUT4_SHADER: None
        INPUT5: MXSWrapperBase
        INPUT5_CONNECTED: bool
        INPUT5_SHADER: None
        INPUT6: MXSWrapperBase
        INPUT6_CONNECTED: bool
        INPUT6_SHADER: None
        INPUT7: MXSWrapperBase
        INPUT7_CONNECTED: bool
        INPUT7_SHADER: None
        INPUT8: MXSWrapperBase
        INPUT8_CONNECTED: bool
        INPUT8_SHADER: None
        MIX1: float
        MIX1_CONNECTED: bool
        MIX1_SHADER: None
        MIX2: float
        MIX2_CONNECTED: bool
        MIX2_SHADER: None
        MIX3: float
        MIX3_CONNECTED: bool
        MIX3_SHADER: None
        MIX4: float
        MIX4_CONNECTED: bool
        MIX4_SHADER: None
        MIX5: float
        MIX5_CONNECTED: bool
        MIX5_SHADER: None
        MIX6: float
        MIX6_CONNECTED: bool
        MIX6_SHADER: None
        MIX7: float
        MIX7_CONNECTED: bool
        MIX7_SHADER: None
        MIX8: float
        MIX8_CONNECTED: bool
        MIX8_SHADER: None
        NAME1: str
        NAME2: str
        NAME3: str
        NAME4: str
        NAME5: str
        NAME6: str
        NAME7: str
        NAME8: str
        OPERATION1: int
        OPERATION2: int
        OPERATION3: int
        OPERATION4: int
        OPERATION5: int
        OPERATION6: int
        OPERATION7: int
        OPERATION8: int
        ...
    class Ai_Layer_Shader(Material):
        ENABLE1: bool
        ENABLE2: bool
        ENABLE3: bool
        ENABLE4: bool
        ENABLE5: bool
        ENABLE6: bool
        ENABLE7: bool
        ENABLE8: bool
        INPUT1: None
        INPUT2: None
        INPUT3: None
        INPUT4: None
        INPUT5: None
        INPUT6: None
        INPUT7: None
        INPUT8: None
        MIX1: float
        MIX1_CONNECTED: bool
        MIX1_SHADER: None
        MIX2: float
        MIX2_CONNECTED: bool
        MIX2_SHADER: None
        MIX3: float
        MIX3_CONNECTED: bool
        MIX3_SHADER: None
        MIX4: float
        MIX4_CONNECTED: bool
        MIX4_SHADER: None
        MIX5: float
        MIX5_CONNECTED: bool
        MIX5_SHADER: None
        MIX6: float
        MIX6_CONNECTED: bool
        MIX6_SHADER: None
        MIX7: float
        MIX7_CONNECTED: bool
        MIX7_SHADER: None
        MIX8: float
        MIX8_CONNECTED: bool
        MIX8_SHADER: None
        NAME1: str
        NAME2: str
        NAME3: str
        NAME4: str
        NAME5: str
        NAME6: str
        NAME7: str
        NAME8: str
        ...
    class Ai_Length(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        MODE: int
        ...
    class Ai_Light_Blocker(TextureMap):
        ...
    class Ai_Light_Decay(TextureMap):
        ...
    class Ai_Log(TextureMap):
        BASE: MXSWrapperBase
        BASE_CONNECTED: bool
        BASE_SHADER: None
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Materialx(TextureMap):
        ...
    class Ai_Matrix_Interpolate(TextureMap):
        ...
    class Ai_Matrix_Multiply_Vector(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        MATRIX: MXSWrapperBase
        MATRIX_CONNECTED: bool
        MATRIX_SHADER: None
        TYPE: int
        ...
    class Ai_Matrix_Transform(TextureMap):
        ANGLE: float
        ANGLE_CONNECTED: bool
        ANGLE_SHADER: None
        AXIS: MXSWrapperBase
        AXIS_CONNECTED: bool
        AXIS_SHADER: None
        PIVOT: MXSWrapperBase
        PIVOT_CONNECTED: bool
        PIVOT_SHADER: None
        ROTATION: MXSWrapperBase
        ROTATION_CONNECTED: bool
        ROTATION_ORDER: int
        ROTATION_SHADER: None
        ROTATION_TYPE: int
        SCALE: MXSWrapperBase
        SCALE_CONNECTED: bool
        SCALE_SHADER: None
        TRANSFORM_ORDER: int
        TRANSLATE: MXSWrapperBase
        TRANSLATE_CONNECTED: bool
        TRANSLATE_SHADER: None
        UNITS: int
        ...
    class Ai_Matte(Material):
        COLOR: MXSWrapperBase
        COLOR_CONNECTED: bool
        COLOR_SHADER: None
        OPACITY: MXSWrapperBase
        OPACITY_CONNECTED: bool
        OPACITY_SHADER: None
        PASSTHROUGH: None
        ...
    class Ai_Max(TextureMap):
        INPUT1: MXSWrapperBase
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        INPUT2: MXSWrapperBase
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        ...
    class Ai_Merge(TextureMap):
        ...
    class Ai_Min(TextureMap):
        INPUT1: MXSWrapperBase
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        INPUT2: MXSWrapperBase
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        ...
    class Ai_Mitnet_Filter(TextureMap):
        ...
    class Ai_Mix_Rgba(TextureMap):
        INPUT1: MXSWrapperBase
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        INPUT2: MXSWrapperBase
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        MIX: float
        MIX_CONNECTED: bool
        MIX_SHADER: None
        ...
    class Ai_Mix_Shader(Material):
        ADD_TRANSPARENCY: bool
        MIX: float
        MIX_CONNECTED: bool
        MIX_SHADER: None
        MODE: int
        SHADER1: None
        SHADER2: None
        ...
    class Ai_Modulo(TextureMap):
        DIVISOR: MXSWrapperBase
        DIVISOR_CONNECTED: bool
        DIVISOR_SHADER: None
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Motion_Vector(TextureMap):
        MAX_DISPLACE: float
        RAW: bool
        TIME0: float
        TIME1: float
        ...
    class Ai_Multiply(TextureMap):
        INPUT1: MXSWrapperBase
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        INPUT2: MXSWrapperBase
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        ...
    class Ai_Negate(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Noise(TextureMap):
        AMPLITUDE: float
        AMPLITUDE_CONNECTED: bool
        AMPLITUDE_SHADER: None
        COLOR1: MXSWrapperBase
        COLOR1_CONNECTED: bool
        COLOR1_SHADER: None
        COLOR2: MXSWrapperBase
        COLOR2_CONNECTED: bool
        COLOR2_SHADER: None
        COORD_SPACE: int
        DISTORTION: float
        DISTORTION_CONNECTED: bool
        DISTORTION_SHADER: None
        LACUNARITY: float
        LACUNARITY_CONNECTED: bool
        LACUNARITY_SHADER: None
        MODE: int
        OCTAVES: int
        OFFSET: MXSWrapperBase
        OFFSET_CONNECTED: bool
        OFFSET_SHADER: None
        P: MXSWrapperBase
        PREF_NAME: str
        P_CONNECTED: bool
        P_SHADER: None
        SCALE: MXSWrapperBase
        SCALE_CONNECTED: bool
        SCALE_SHADER: None
        TIME: float
        TIME_CONNECTED: bool
        TIME_SHADER: None
        ...
    class Ai_Normal_Map(TextureMap):
        COLOR_TO_SIGNED: bool
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        INVERT_X: bool
        INVERT_Y: bool
        INVERT_Z: bool
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        ORDER: int
        STRENGTH: float
        STRENGTH_CONNECTED: bool
        STRENGTH_SHADER: None
        TANGENT: MXSWrapperBase
        TANGENT_CONNECTED: bool
        TANGENT_SHADER: None
        TANGENT_SPACE: bool
        ...
    class Ai_Normalize(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Osl(TextureMap):
        ...
    class Ai_Passthrough(Material):
        EVAL10: None
        EVAL11: None
        EVAL12: None
        EVAL13: None
        EVAL14: None
        EVAL15: None
        EVAL16: None
        EVAL17: None
        EVAL18: None
        EVAL19: None
        EVAL1: None
        EVAL20: None
        EVAL2: None
        EVAL3: None
        EVAL4: None
        EVAL5: None
        EVAL6: None
        EVAL7: None
        EVAL8: None
        EVAL9: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        PASSTHROUGH: None
        ...
    class Ai_Physical_Sky(TextureMap):
        AZIMUTH: float
        ELEVATION: float
        ENABLE_SUN: bool
        GROUND_ALBEDO: MXSWrapperBase
        INTENSITY: float
        SKY_TINT: MXSWrapperBase
        SUN_DIRECTION: MXSWrapperBase
        SUN_SIZE: float
        SUN_TINT: MXSWrapperBase
        TURBIDITY: float
        USE_DEGREES: bool
        X: MXSWrapperBase
        Y: MXSWrapperBase
        Z: MXSWrapperBase
        ...
    class Ai_Pow(TextureMap):
        BASE: MXSWrapperBase
        BASE_CONNECTED: bool
        BASE_SHADER: None
        EXPONENT: MXSWrapperBase
        EXPONENT_CONNECTED: bool
        EXPONENT_SHADER: None
        ...
    class Ai_Procedural_Operator(TextureMap):
        ...
    class Ai_Ramp_Float(TextureMap):
        INPUT: float
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        INTERPOLATION: MXSWrapperBase
        POSITION: MXSWrapperBase
        TYPE: int
        USE_IMPLICIT_UVS: int
        UVSET: str
        VALUE: MXSWrapperBase
        WRAP_UVS: bool
        ...
    class Ai_Ramp_Rgb(TextureMap):
        COLOR: MXSWrapperBase
        INPUT: float
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        INTERPOLATION: MXSWrapperBase
        POSITION: MXSWrapperBase
        TYPE: int
        USE_IMPLICIT_UVS: int
        UVSET: str
        WRAP_UVS: bool
        ...
    class Ai_Random(TextureMap):
        GRAYSCALE: bool
        INPUT_COLOR: MXSWrapperBase
        INPUT_COLOR_CONNECTED: bool
        INPUT_COLOR_SHADER: None
        INPUT_FLOAT: float
        INPUT_FLOAT_CONNECTED: bool
        INPUT_FLOAT_SHADER: None
        INPUT_INT: int
        INPUT_INT_CONNECTED: bool
        INPUT_INT_SHADER: None
        INPUT_TYPE: int
        SEED: int
        SEED_CONNECTED: bool
        SEED_SHADER: None
        ...
    class Ai_Range(TextureMap):
        BIAS: float
        BIAS_CONNECTED: bool
        BIAS_SHADER: None
        CONTRAST: float
        CONTRAST_CONNECTED: bool
        CONTRAST_PIVOT: float
        CONTRAST_PIVOT_CONNECTED: bool
        CONTRAST_PIVOT_SHADER: None
        CONTRAST_SHADER: None
        GAIN: float
        GAIN_CONNECTED: bool
        GAIN_SHADER: None
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_MAX: float
        INPUT_MAX_CONNECTED: bool
        INPUT_MAX_SHADER: None
        INPUT_MIN: float
        INPUT_MIN_CONNECTED: bool
        INPUT_MIN_SHADER: None
        INPUT_SHADER: None
        OUTPUT_MAX: float
        OUTPUT_MAX_CONNECTED: bool
        OUTPUT_MAX_SHADER: None
        OUTPUT_MIN: float
        OUTPUT_MIN_CONNECTED: bool
        OUTPUT_MIN_SHADER: None
        SMOOTHSTEP: bool
        ...
    class Ai_Ray_Switch_Rgba(TextureMap):
        CAMERA: MXSWrapperBase
        CAMERA_CONNECTED: bool
        CAMERA_SHADER: None
        DIFFUSE_REFLECTION: MXSWrapperBase
        DIFFUSE_REFLECTION_CONNECTED: bool
        DIFFUSE_REFLECTION_SHADER: None
        DIFFUSE_TRANSMISSION: MXSWrapperBase
        DIFFUSE_TRANSMISSION_CONNECTED: bool
        DIFFUSE_TRANSMISSION_SHADER: None
        SHADOW: MXSWrapperBase
        SHADOW_CONNECTED: bool
        SHADOW_SHADER: None
        SPECULAR_REFLECTION: MXSWrapperBase
        SPECULAR_REFLECTION_CONNECTED: bool
        SPECULAR_REFLECTION_SHADER: None
        SPECULAR_TRANSMISSION: MXSWrapperBase
        SPECULAR_TRANSMISSION_CONNECTED: bool
        SPECULAR_TRANSMISSION_SHADER: None
        VOLUME: MXSWrapperBase
        VOLUME_CONNECTED: bool
        VOLUME_SHADER: None
        ...
    class Ai_Ray_Switch_Shader(Material):
        CAMERA: None
        DIFFUSE_REFLECTION: None
        DIFFUSE_TRANSMISSION: None
        SHADOW: None
        SPECULAR_REFLECTION: None
        SPECULAR_TRANSMISSION: None
        VOLUME: None
        ...
    class Ai_Reciprocal(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Rgb_To_Float(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        MODE: int
        MODE_CONNECTED: bool
        MODE_SHADER: None
        ...
    class Ai_Rgb_To_Vector(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        MODE: int
        MODE_CONNECTED: bool
        MODE_SHADER: None
        ...
    class Ai_Rgba_To_Float(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        MODE: int
        MODE_CONNECTED: bool
        MODE_SHADER: None
        ...
    class Ai_Round_Corners(TextureMap):
        INCLUSIVE: bool
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        OBJECT_SPACE: bool
        RADIUS: float
        RADIUS_CONNECTED: bool
        RADIUS_SHADER: None
        SAMPLES: int
        SELF_ONLY: bool
        TRACE_SET: str
        ...
    class Ai_Set_Parameter(TextureMap):
        ...
    class Ai_Set_Transform(TextureMap):
        ...
    class Ai_Shadow_Matte(TextureMap):
        ALPHA_MASK: bool
        ALPHA_MASK_CONNECTED: bool
        ALPHA_MASK_SHADER: None
        AOV_GROUP: str
        AOV_SHADOW: str
        AOV_SHADOW_DIFF: str
        AOV_SHADOW_MASK: str
        BACKGROUND: int
        BACKGROUND_COLOR: MXSWrapperBase
        BACKGROUND_COLOR_CONNECTED: bool
        BACKGROUND_COLOR_SHADER: None
        BACKGROUND_CONNECTED: bool
        BACKGROUND_SHADER: None
        BACKLIGHTING: float
        BACKLIGHTING_CONNECTED: bool
        BACKLIGHTING_SHADER: None
        DIFFUSE_COLOR: MXSWrapperBase
        DIFFUSE_COLOR_CONNECTED: bool
        DIFFUSE_COLOR_SHADER: None
        DIFFUSE_INTENSITY: float
        DIFFUSE_INTENSITY_CONNECTED: bool
        DIFFUSE_INTENSITY_SHADER: None
        DIFFUSE_USE_BACKGROUND: bool
        INDIRECT_DIFFUSE_ENABLE: bool
        INDIRECT_SPECULAR_ENABLE: bool
        SHADOW_COLOR: MXSWrapperBase
        SHADOW_COLOR_CONNECTED: bool
        SHADOW_COLOR_SHADER: None
        SHADOW_OPACITY: float
        SHADOW_OPACITY_CONNECTED: bool
        SHADOW_OPACITY_SHADER: None
        SPECULAR_COLOR: MXSWrapperBase
        SPECULAR_COLOR_CONNECTED: bool
        SPECULAR_COLOR_SHADER: None
        SPECULAR_INTENSITY: float
        SPECULAR_INTENSITY_CONNECTED: bool
        SPECULAR_INTENSITY_SHADER: None
        SPECULAR_IOR: float
        SPECULAR_IOR_CONNECTED: bool
        SPECULAR_IOR_SHADER: None
        SPECULAR_ROUGHNESS: float
        SPECULAR_ROUGHNESS_CONNECTED: bool
        SPECULAR_ROUGHNESS_SHADER: None
        ...
    class Ai_Shuffle(TextureMap):
        ALPHA: float
        ALPHA_CONNECTED: bool
        ALPHA_SHADER: None
        CHANNEL_A: int
        CHANNEL_B: int
        CHANNEL_G: int
        CHANNEL_R: int
        COLOR: MXSWrapperBase
        COLOR_CONNECTED: bool
        COLOR_SHADER: None
        NEGATE_A: bool
        NEGATE_B: bool
        NEGATE_G: bool
        NEGATE_R: bool
        ...
    class Ai_Sign(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Sinc_Filter(TextureMap):
        ...
    class Ai_Skin(Material):
        ...
    class Ai_Sky(Material):
        ...
    class Ai_Space_Transform(TextureMap):
        FROM: int
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        NORMAL: MXSWrapperBase
        NORMALIZE: bool
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        SCALE: float
        SCALE_CONNECTED: bool
        SCALE_SHADER: None
        TANGENT: MXSWrapperBase
        TANGENT_CONNECTED: bool
        TANGENT_SHADER: None
        TO: int
        TYPE: int
        ...
    class Ai_Sqrt(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Standard(Material):
        ...
    class Ai_Standard_Hair(Material):
        AOV_ID1: str
        AOV_ID2: str
        AOV_ID3: str
        AOV_ID4: str
        AOV_ID5: str
        AOV_ID6: str
        AOV_ID7: str
        AOV_ID8: str
        BASE: float
        BASE_COLOR: MXSWrapperBase
        BASE_COLOR_CONNECTED: bool
        BASE_COLOR_SHADER: None
        BASE_CONNECTED: bool
        BASE_SHADER: None
        DIFFUSE: float
        DIFFUSE_COLOR: MXSWrapperBase
        DIFFUSE_COLOR_CONNECTED: bool
        DIFFUSE_COLOR_SHADER: None
        DIFFUSE_CONNECTED: bool
        DIFFUSE_SHADER: None
        EMISSION: float
        EMISSION_COLOR: MXSWrapperBase
        EMISSION_COLOR_CONNECTED: bool
        EMISSION_COLOR_SHADER: None
        EMISSION_CONNECTED: bool
        EMISSION_SHADER: None
        EXTRA_DEPTH: int
        EXTRA_SAMPLES: int
        ID1: MXSWrapperBase
        ID1_CONNECTED: bool
        ID1_SHADER: None
        ID2: MXSWrapperBase
        ID2_CONNECTED: bool
        ID2_SHADER: None
        ID3: MXSWrapperBase
        ID3_CONNECTED: bool
        ID3_SHADER: None
        ID4: MXSWrapperBase
        ID4_CONNECTED: bool
        ID4_SHADER: None
        ID5: MXSWrapperBase
        ID5_CONNECTED: bool
        ID5_SHADER: None
        ID6: MXSWrapperBase
        ID6_CONNECTED: bool
        ID6_SHADER: None
        ID7: MXSWrapperBase
        ID7_CONNECTED: bool
        ID7_SHADER: None
        ID8: MXSWrapperBase
        ID8_CONNECTED: bool
        ID8_SHADER: None
        INDIRECT_DIFFUSE: float
        INDIRECT_SPECULAR: float
        IOR: float
        IOR_CONNECTED: bool
        IOR_SHADER: None
        MELANIN: float
        MELANIN_CONNECTED: bool
        MELANIN_RANDOMIZE: float
        MELANIN_RANDOMIZE_CONNECTED: bool
        MELANIN_RANDOMIZE_SHADER: None
        MELANIN_REDNESS: float
        MELANIN_REDNESS_CONNECTED: bool
        MELANIN_REDNESS_SHADER: None
        MELANIN_SHADER: None
        OPACITY: MXSWrapperBase
        OPACITY_CONNECTED: bool
        OPACITY_SHADER: None
        ROUGHNESS: float
        ROUGHNESS_ANISOTROPIC: bool
        ROUGHNESS_AZIMUTHAL: float
        ROUGHNESS_AZIMUTHAL_CONNECTED: bool
        ROUGHNESS_AZIMUTHAL_SHADER: None
        ROUGHNESS_CONNECTED: bool
        ROUGHNESS_SHADER: None
        SHIFT: float
        SHIFT_CONNECTED: bool
        SHIFT_SHADER: None
        SPECULAR2_TINT: MXSWrapperBase
        SPECULAR2_TINT_CONNECTED: bool
        SPECULAR2_TINT_SHADER: None
        SPECULAR_TINT: MXSWrapperBase
        SPECULAR_TINT_CONNECTED: bool
        SPECULAR_TINT_SHADER: None
        TRANSMISSION_TINT: MXSWrapperBase
        TRANSMISSION_TINT_CONNECTED: bool
        TRANSMISSION_TINT_SHADER: None
        ...
    class Ai_Standard_Surface(Material):
        AOV_ID1: str
        AOV_ID2: str
        AOV_ID3: str
        AOV_ID4: str
        AOV_ID5: str
        AOV_ID6: str
        AOV_ID7: str
        AOV_ID8: str
        BASE: float
        BASE_COLOR: MXSWrapperBase
        BASE_COLOR_CONNECTED: bool
        BASE_COLOR_SHADER: None
        BASE_CONNECTED: bool
        BASE_SHADER: None
        CAUSTICS: bool
        COAT: float
        COAT_AFFECT_COLOR: float
        COAT_AFFECT_COLOR_CONNECTED: bool
        COAT_AFFECT_COLOR_SHADER: None
        COAT_AFFECT_ROUGHNESS: float
        COAT_AFFECT_ROUGHNESS_CONNECTED: bool
        COAT_AFFECT_ROUGHNESS_SHADER: None
        COAT_ANISOTROPY: float
        COAT_ANISOTROPY_CONNECTED: bool
        COAT_ANISOTROPY_SHADER: None
        COAT_COLOR: MXSWrapperBase
        COAT_COLOR_CONNECTED: bool
        COAT_COLOR_SHADER: None
        COAT_CONNECTED: bool
        COAT_IOR: float
        COAT_IOR_CONNECTED: bool
        COAT_IOR_SHADER: None
        COAT_NORMAL: MXSWrapperBase
        COAT_NORMAL_CONNECTED: bool
        COAT_NORMAL_SHADER: None
        COAT_ROTATION: float
        COAT_ROTATION_CONNECTED: bool
        COAT_ROTATION_SHADER: None
        COAT_ROUGHNESS: float
        COAT_ROUGHNESS_CONNECTED: bool
        COAT_ROUGHNESS_SHADER: None
        COAT_SHADER: None
        DIELECTRIC_PRIORITY: int
        DIFFUSE_ROUGHNESS: float
        DIFFUSE_ROUGHNESS_CONNECTED: bool
        DIFFUSE_ROUGHNESS_SHADER: None
        EMISSION: float
        EMISSION_COLOR: MXSWrapperBase
        EMISSION_COLOR_CONNECTED: bool
        EMISSION_COLOR_SHADER: None
        EMISSION_CONNECTED: bool
        EMISSION_SHADER: None
        EXIT_TO_BACKGROUND: bool
        ID1: MXSWrapperBase
        ID1_CONNECTED: bool
        ID1_SHADER: None
        ID2: MXSWrapperBase
        ID2_CONNECTED: bool
        ID2_SHADER: None
        ID3: MXSWrapperBase
        ID3_CONNECTED: bool
        ID3_SHADER: None
        ID4: MXSWrapperBase
        ID4_CONNECTED: bool
        ID4_SHADER: None
        ID5: MXSWrapperBase
        ID5_CONNECTED: bool
        ID5_SHADER: None
        ID6: MXSWrapperBase
        ID6_CONNECTED: bool
        ID6_SHADER: None
        ID7: MXSWrapperBase
        ID7_CONNECTED: bool
        ID7_SHADER: None
        ID8: MXSWrapperBase
        ID8_CONNECTED: bool
        ID8_SHADER: None
        INDIRECT_DIFFUSE: float
        INDIRECT_SPECULAR: float
        INTERNAL_REFLECTIONS: bool
        METALNESS: float
        METALNESS_CONNECTED: bool
        METALNESS_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        OPACITY: MXSWrapperBase
        OPACITY_CONNECTED: bool
        OPACITY_SHADER: None
        SHEEN: float
        SHEEN_COLOR: MXSWrapperBase
        SHEEN_COLOR_CONNECTED: bool
        SHEEN_COLOR_SHADER: None
        SHEEN_CONNECTED: bool
        SHEEN_ROUGHNESS: float
        SHEEN_ROUGHNESS_CONNECTED: bool
        SHEEN_ROUGHNESS_SHADER: None
        SHEEN_SHADER: None
        SPECULAR: float
        SPECULAR_ANISOTROPY: float
        SPECULAR_ANISOTROPY_CONNECTED: bool
        SPECULAR_ANISOTROPY_SHADER: None
        SPECULAR_COLOR: MXSWrapperBase
        SPECULAR_COLOR_CONNECTED: bool
        SPECULAR_COLOR_SHADER: None
        SPECULAR_CONNECTED: bool
        SPECULAR_IOR: float
        SPECULAR_IOR_CONNECTED: bool
        SPECULAR_IOR_SHADER: None
        SPECULAR_ROTATION: float
        SPECULAR_ROTATION_CONNECTED: bool
        SPECULAR_ROTATION_SHADER: None
        SPECULAR_ROUGHNESS: float
        SPECULAR_ROUGHNESS_CONNECTED: bool
        SPECULAR_ROUGHNESS_SHADER: None
        SPECULAR_SHADER: None
        SUBSURFACE: float
        SUBSURFACE_ANISOTROPY: float
        SUBSURFACE_ANISOTROPY_CONNECTED: bool
        SUBSURFACE_ANISOTROPY_SHADER: None
        SUBSURFACE_COLOR: MXSWrapperBase
        SUBSURFACE_COLOR_CONNECTED: bool
        SUBSURFACE_COLOR_SHADER: None
        SUBSURFACE_CONNECTED: bool
        SUBSURFACE_RADIUS: MXSWrapperBase
        SUBSURFACE_RADIUS_CONNECTED: bool
        SUBSURFACE_RADIUS_SHADER: None
        SUBSURFACE_SCALE: float
        SUBSURFACE_SCALE_CONNECTED: bool
        SUBSURFACE_SCALE_SHADER: None
        SUBSURFACE_SHADER: None
        SUBSURFACE_TYPE: int
        TANGENT: MXSWrapperBase
        TANGENT_CONNECTED: bool
        TANGENT_SHADER: None
        THIN_FILM_IOR: float
        THIN_FILM_IOR_CONNECTED: bool
        THIN_FILM_IOR_SHADER: None
        THIN_FILM_THICKNESS: float
        THIN_FILM_THICKNESS_CONNECTED: bool
        THIN_FILM_THICKNESS_SHADER: None
        THIN_WALLED: bool
        TRANSMISSION: float
        TRANSMISSION_COLOR: MXSWrapperBase
        TRANSMISSION_COLOR_CONNECTED: bool
        TRANSMISSION_COLOR_SHADER: None
        TRANSMISSION_CONNECTED: bool
        TRANSMISSION_DEPTH: float
        TRANSMISSION_DEPTH_CONNECTED: bool
        TRANSMISSION_DEPTH_SHADER: None
        TRANSMISSION_DISPERSION: float
        TRANSMISSION_DISPERSION_CONNECTED: bool
        TRANSMISSION_DISPERSION_SHADER: None
        TRANSMISSION_EXTRA_ROUGHNESS: float
        TRANSMISSION_EXTRA_ROUGHNESS_CONNECTED: bool
        TRANSMISSION_EXTRA_ROUGHNESS_SHADER: None
        TRANSMISSION_SCATTER: MXSWrapperBase
        TRANSMISSION_SCATTER_ANISOTROPY: float
        TRANSMISSION_SCATTER_ANISOTROPY_CONNECTED: bool
        TRANSMISSION_SCATTER_ANISOTROPY_SHADER: None
        TRANSMISSION_SCATTER_CONNECTED: bool
        TRANSMISSION_SCATTER_SHADER: None
        TRANSMISSION_SHADER: None
        TRANSMIT_AOVS: bool
        ...
    class Ai_Standard_Volume(Material):
        BLACKBODY_INTENSITY: float
        BLACKBODY_INTENSITY_CONNECTED: bool
        BLACKBODY_INTENSITY_SHADER: None
        BLACKBODY_KELVIN: float
        BLACKBODY_KELVIN_CONNECTED: bool
        BLACKBODY_KELVIN_SHADER: None
        DENSITY: float
        DENSITY_CHANNEL: str
        DENSITY_CONNECTED: bool
        DENSITY_SHADER: None
        DISPLACEMENT: MXSWrapperBase
        DISPLACEMENT_CONNECTED: bool
        DISPLACEMENT_SHADER: None
        EMISSION: float
        EMISSION_CHANNEL: str
        EMISSION_COLOR: MXSWrapperBase
        EMISSION_COLOR_CONNECTED: bool
        EMISSION_COLOR_SHADER: None
        EMISSION_CONNECTED: bool
        EMISSION_MODE: int
        EMISSION_SHADER: None
        INTERPOLATION: int
        SCATTER: float
        SCATTER_ANISOTROPY: float
        SCATTER_ANISOTROPY_CONNECTED: bool
        SCATTER_ANISOTROPY_SHADER: None
        SCATTER_COLOR: MXSWrapperBase
        SCATTER_COLOR_CHANNEL: str
        SCATTER_COLOR_CONNECTED: bool
        SCATTER_COLOR_SHADER: None
        SCATTER_CONNECTED: bool
        SCATTER_SHADER: None
        TEMPERATURE: float
        TEMPERATURE_CHANNEL: str
        TEMPERATURE_CONNECTED: bool
        TEMPERATURE_SHADER: None
        TRANSPARENT: MXSWrapperBase
        TRANSPARENT_CHANNEL: str
        TRANSPARENT_CONNECTED: bool
        TRANSPARENT_DEPTH: float
        TRANSPARENT_SHADER: None
        ...
    class Ai_State_Float(TextureMap):
        VARIABLE: int
        ...
    class Ai_State_Int(TextureMap):
        VARIABLE: int
        ...
    class Ai_State_Vector(TextureMap):
        VARIABLE: int
        ...
    class Ai_String_Replace(TextureMap):
        ...
    class Ai_Subtract(TextureMap):
        INPUT1: MXSWrapperBase
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        INPUT2: MXSWrapperBase
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        ...
    class Ai_Switch_Operator(TextureMap):
        ...
    class Ai_Switch_Rgba(TextureMap):
        INDEX: int
        INDEX_CONNECTED: bool
        INDEX_SHADER: None
        INPUT0: MXSWrapperBase
        INPUT0_CONNECTED: bool
        INPUT0_SHADER: None
        INPUT10: MXSWrapperBase
        INPUT10_CONNECTED: bool
        INPUT10_SHADER: None
        INPUT11: MXSWrapperBase
        INPUT11_CONNECTED: bool
        INPUT11_SHADER: None
        INPUT12: MXSWrapperBase
        INPUT12_CONNECTED: bool
        INPUT12_SHADER: None
        INPUT13: MXSWrapperBase
        INPUT13_CONNECTED: bool
        INPUT13_SHADER: None
        INPUT14: MXSWrapperBase
        INPUT14_CONNECTED: bool
        INPUT14_SHADER: None
        INPUT15: MXSWrapperBase
        INPUT15_CONNECTED: bool
        INPUT15_SHADER: None
        INPUT16: MXSWrapperBase
        INPUT16_CONNECTED: bool
        INPUT16_SHADER: None
        INPUT17: MXSWrapperBase
        INPUT17_CONNECTED: bool
        INPUT17_SHADER: None
        INPUT18: MXSWrapperBase
        INPUT18_CONNECTED: bool
        INPUT18_SHADER: None
        INPUT19: MXSWrapperBase
        INPUT19_CONNECTED: bool
        INPUT19_SHADER: None
        INPUT1: MXSWrapperBase
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        INPUT2: MXSWrapperBase
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        INPUT3: MXSWrapperBase
        INPUT3_CONNECTED: bool
        INPUT3_SHADER: None
        INPUT4: MXSWrapperBase
        INPUT4_CONNECTED: bool
        INPUT4_SHADER: None
        INPUT5: MXSWrapperBase
        INPUT5_CONNECTED: bool
        INPUT5_SHADER: None
        INPUT6: MXSWrapperBase
        INPUT6_CONNECTED: bool
        INPUT6_SHADER: None
        INPUT7: MXSWrapperBase
        INPUT7_CONNECTED: bool
        INPUT7_SHADER: None
        INPUT8: MXSWrapperBase
        INPUT8_CONNECTED: bool
        INPUT8_SHADER: None
        INPUT9: MXSWrapperBase
        INPUT9_CONNECTED: bool
        INPUT9_SHADER: None
        ...
    class Ai_Switch_Shader(Material):
        INDEX: int
        INDEX_CONNECTED: bool
        INDEX_SHADER: None
        INPUT0: None
        INPUT10: None
        INPUT11: None
        INPUT12: None
        INPUT13: None
        INPUT14: None
        INPUT15: None
        INPUT16: None
        INPUT17: None
        INPUT18: None
        INPUT19: None
        INPUT1: None
        INPUT2: None
        INPUT3: None
        INPUT4: None
        INPUT5: None
        INPUT6: None
        INPUT7: None
        INPUT8: None
        INPUT9: None
        ...
    class Ai_Thin_Film(TextureMap):
        ...
    class Ai_Toon(TextureMap):
        ANGLE_THRESHOLD: float
        ANGLE_THRESHOLD_CONNECTED: bool
        ANGLE_THRESHOLD_SHADER: None
        AOV_HIGHLIGHT: str
        AOV_PREFIX: str
        AOV_RIM_LIGHT: str
        BASE: float
        BASE_COLOR: MXSWrapperBase
        BASE_COLOR_CONNECTED: bool
        BASE_COLOR_SHADER: None
        BASE_CONNECTED: bool
        BASE_SHADER: None
        BASE_TONEMAP: MXSWrapperBase
        BASE_TONEMAP_CONNECTED: bool
        BASE_TONEMAP_SHADER: None
        BUMP_MODE: int
        EDGE_COLOR: MXSWrapperBase
        EDGE_COLOR_CONNECTED: bool
        EDGE_COLOR_SHADER: None
        EDGE_OPACITY: float
        EDGE_OPACITY_CONNECTED: bool
        EDGE_OPACITY_SHADER: None
        EDGE_TONEMAP: MXSWrapperBase
        EDGE_TONEMAP_CONNECTED: bool
        EDGE_TONEMAP_SHADER: None
        EDGE_WIDTH_SCALE: float
        EDGE_WIDTH_SCALE_CONNECTED: bool
        EDGE_WIDTH_SCALE_SHADER: None
        EMISSION: float
        EMISSION_COLOR: MXSWrapperBase
        EMISSION_COLOR_CONNECTED: bool
        EMISSION_COLOR_SHADER: None
        EMISSION_CONNECTED: bool
        EMISSION_SHADER: None
        ENABLE: bool
        ENABLE_SILHOUETTE: bool
        ENERGY_CONSERVING: bool
        HIGHLIGHT_COLOR: MXSWrapperBase
        HIGHLIGHT_COLOR_CONNECTED: bool
        HIGHLIGHT_COLOR_SHADER: None
        HIGHLIGHT_SIZE: float
        HIGHLIGHT_SIZE_CONNECTED: bool
        HIGHLIGHT_SIZE_SHADER: None
        ID_DIFFERENCE: bool
        IGNORE_THROUGHPUT: bool
        INDIRECT_DIFFUSE: float
        INDIRECT_SPECULAR: float
        IOR: float
        IOR_CONNECTED: bool
        IOR_SHADER: None
        LIGHTS: str
        MASK_COLOR: MXSWrapperBase
        MASK_COLOR_CONNECTED: bool
        MASK_COLOR_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        NORMAL_TYPE: int
        PRIORITY: int
        RIM_LIGHT: str
        RIM_LIGHT_COLOR: MXSWrapperBase
        RIM_LIGHT_COLOR_CONNECTED: bool
        RIM_LIGHT_COLOR_SHADER: None
        RIM_LIGHT_TINT: float
        RIM_LIGHT_TINT_CONNECTED: bool
        RIM_LIGHT_TINT_SHADER: None
        RIM_LIGHT_WIDTH: float
        RIM_LIGHT_WIDTH_CONNECTED: bool
        RIM_LIGHT_WIDTH_SHADER: None
        SHADER_DIFFERENCE: bool
        SHEEN: float
        SHEEN_COLOR: MXSWrapperBase
        SHEEN_COLOR_CONNECTED: bool
        SHEEN_COLOR_SHADER: None
        SHEEN_CONNECTED: bool
        SHEEN_ROUGHNESS: float
        SHEEN_ROUGHNESS_CONNECTED: bool
        SHEEN_ROUGHNESS_SHADER: None
        SHEEN_SHADER: None
        SILHOUETTE_COLOR: MXSWrapperBase
        SILHOUETTE_COLOR_CONNECTED: bool
        SILHOUETTE_COLOR_SHADER: None
        SILHOUETTE_OPACITY: float
        SILHOUETTE_OPACITY_CONNECTED: bool
        SILHOUETTE_OPACITY_SHADER: None
        SILHOUETTE_TONEMAP: MXSWrapperBase
        SILHOUETTE_TONEMAP_CONNECTED: bool
        SILHOUETTE_TONEMAP_SHADER: None
        SILHOUETTE_WIDTH_SCALE: float
        SILHOUETTE_WIDTH_SCALE_CONNECTED: bool
        SILHOUETTE_WIDTH_SCALE_SHADER: None
        SPECULAR: float
        SPECULAR_ANISOTROPY: float
        SPECULAR_ANISOTROPY_CONNECTED: bool
        SPECULAR_ANISOTROPY_SHADER: None
        SPECULAR_COLOR: MXSWrapperBase
        SPECULAR_COLOR_CONNECTED: bool
        SPECULAR_COLOR_SHADER: None
        SPECULAR_CONNECTED: bool
        SPECULAR_ROTATION: float
        SPECULAR_ROTATION_CONNECTED: bool
        SPECULAR_ROTATION_SHADER: None
        SPECULAR_ROUGHNESS: float
        SPECULAR_ROUGHNESS_CONNECTED: bool
        SPECULAR_ROUGHNESS_SHADER: None
        SPECULAR_SHADER: None
        SPECULAR_TONEMAP: MXSWrapperBase
        SPECULAR_TONEMAP_CONNECTED: bool
        SPECULAR_TONEMAP_SHADER: None
        TANGENT: MXSWrapperBase
        TANGENT_CONNECTED: bool
        TANGENT_SHADER: None
        TRANSMISSION: float
        TRANSMISSION_ANISOTROPY: float
        TRANSMISSION_ANISOTROPY_CONNECTED: bool
        TRANSMISSION_ANISOTROPY_SHADER: None
        TRANSMISSION_COLOR: MXSWrapperBase
        TRANSMISSION_COLOR_CONNECTED: bool
        TRANSMISSION_COLOR_SHADER: None
        TRANSMISSION_CONNECTED: bool
        TRANSMISSION_ROTATION: float
        TRANSMISSION_ROTATION_CONNECTED: bool
        TRANSMISSION_ROTATION_SHADER: None
        TRANSMISSION_ROUGHNESS: float
        TRANSMISSION_ROUGHNESS_CONNECTED: bool
        TRANSMISSION_ROUGHNESS_SHADER: None
        TRANSMISSION_SHADER: None
        USER_ID: bool
        UV_THRESHOLD: float
        UV_THRESHOLD_CONNECTED: bool
        UV_THRESHOLD_SHADER: None
        ...
    class Ai_Trace_Set(Material):
        INCLUSIVE: bool
        PASSTHROUGH: None
        TRACE_SET: str
        ...
    class Ai_Triangle_Filter(TextureMap):
        ...
    class Ai_Trigo(TextureMap):
        FREQUENCY: float
        FREQUENCY_CONNECTED: bool
        FREQUENCY_SHADER: None
        FUNCTION: int
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        PHASE: float
        PHASE_CONNECTED: bool
        PHASE_SHADER: None
        UNITS: int
        ...
    class Ai_Triplanar(TextureMap):
        BLEND: float
        BLEND_CONNECTED: bool
        BLEND_SHADER: None
        CELL: bool
        CELL_BLEND: float
        CELL_BLEND_CONNECTED: bool
        CELL_BLEND_SHADER: None
        CELL_CONNECTED: bool
        CELL_ROTATE: float
        CELL_ROTATE_CONNECTED: bool
        CELL_ROTATE_SHADER: None
        CELL_SHADER: None
        COORD_SPACE: int
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        OFFSET: MXSWrapperBase
        OFFSET_CONNECTED: bool
        OFFSET_SHADER: None
        PREF_NAME: str
        ROTATE: MXSWrapperBase
        ROTATE_CONNECTED: bool
        ROTATE_SHADER: None
        SCALE: MXSWrapperBase
        SCALE_CONNECTED: bool
        SCALE_SHADER: None
        ...
    class Ai_Two_Sided(Material):
        BACK: None
        FRONT: None
        ...
    class Ai_User_Data_Float(TextureMap):
        ATTRIBUTE: str
        DEFAULT: float
        DEFAULT_CONNECTED: bool
        DEFAULT_SHADER: None
        ...
    class Ai_User_Data_Int(TextureMap):
        ATTRIBUTE: str
        DEFAULT: int
        DEFAULT_CONNECTED: bool
        DEFAULT_SHADER: None
        ...
    class Ai_User_Data_Rgb(TextureMap):
        ATTRIBUTE: str
        DEFAULT: MXSWrapperBase
        DEFAULT_CONNECTED: bool
        DEFAULT_SHADER: None
        ...
    class Ai_User_Data_Rgba(TextureMap):
        ATTRIBUTE: str
        DEFAULT: MXSWrapperBase
        DEFAULT_CONNECTED: bool
        DEFAULT_SHADER: None
        ...
    class Ai_User_Data_String(TextureMap):
        ATTRIBUTE: str
        DEFAULT: str
        DEFAULT_CONNECTED: bool
        DEFAULT_SHADER: None
        ...
    class Ai_Utility(TextureMap):
        AO_DISTANCE: float
        AO_DISTANCE_CONNECTED: bool
        AO_DISTANCE_SHADER: None
        COLOR: MXSWrapperBase
        COLOR_CONNECTED: bool
        COLOR_MODE: int
        COLOR_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        OVERLAY_MODE: int
        ROUGHNESS: float
        ROUGHNESS_CONNECTED: bool
        ROUGHNESS_SHADER: None
        SHADE_MODE: int
        ...
    class Ai_Uv_Projection(TextureMap):
        CLAMP: bool
        COORD_SPACE: int
        DEFAULT_COLOR: MXSWrapperBase
        DEFAULT_COLOR_CONNECTED: bool
        DEFAULT_COLOR_SHADER: None
        MATRIX: MXSWrapperBase
        MATRIX_CONNECTED: bool
        MATRIX_SHADER: None
        P: MXSWrapperBase
        PREF_NAME: str
        PROJECTION_COLOR: MXSWrapperBase
        PROJECTION_COLOR_CONNECTED: bool
        PROJECTION_COLOR_SHADER: None
        PROJECTION_TYPE: int
        P_CONNECTED: bool
        P_SHADER: None
        U_ANGLE: float
        U_ANGLE_CONNECTED: bool
        U_ANGLE_SHADER: None
        V_ANGLE: float
        V_ANGLE_CONNECTED: bool
        V_ANGLE_SHADER: None
        ...
    class Ai_Uv_Transform(TextureMap):
        COVERAGE: MXSWrapperBase
        COVERAGE_CONNECTED: bool
        COVERAGE_SHADER: None
        FLIP_U: bool
        FLIP_V: bool
        MIRROR_U: bool
        MIRROR_V: bool
        NOISE: MXSWrapperBase
        NOISE_CONNECTED: bool
        NOISE_SHADER: None
        OFFSET: MXSWrapperBase
        OFFSET_CONNECTED: bool
        OFFSET_SHADER: None
        PASSTHROUGH: MXSWrapperBase
        PASSTHROUGH_CONNECTED: bool
        PASSTHROUGH_SHADER: None
        PIVOT: MXSWrapperBase
        PIVOT_CONNECTED: bool
        PIVOT_FRAME: MXSWrapperBase
        PIVOT_FRAME_CONNECTED: bool
        PIVOT_FRAME_SHADER: None
        PIVOT_SHADER: None
        REPEAT: MXSWrapperBase
        REPEAT_CONNECTED: bool
        REPEAT_SHADER: None
        ROTATE: float
        ROTATE_CONNECTED: bool
        ROTATE_FRAME: float
        ROTATE_FRAME_CONNECTED: bool
        ROTATE_FRAME_SHADER: None
        ROTATE_SHADER: None
        SCALE_FRAME: MXSWrapperBase
        SCALE_FRAME_CONNECTED: bool
        SCALE_FRAME_SHADER: None
        STAGGER: bool
        SWAP_UV: bool
        TRANSLATE_FRAME: MXSWrapperBase
        TRANSLATE_FRAME_CONNECTED: bool
        TRANSLATE_FRAME_SHADER: None
        UNIT: int
        UVSET: str
        WRAP_FRAME_COLOR: MXSWrapperBase
        WRAP_FRAME_COLOR_CONNECTED: bool
        WRAP_FRAME_COLOR_SHADER: None
        WRAP_FRAME_U: int
        WRAP_FRAME_V: int
        ...
    class Ai_Variance_Filter(TextureMap):
        ...
    class Ai_Vector_Map(TextureMap):
        COLOR_TO_SIGNED: bool
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        INVERT_X: bool
        INVERT_Y: bool
        INVERT_Z: bool
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        ORDER: int
        SCALE: float
        SCALE_CONNECTED: bool
        SCALE_SHADER: None
        TANGENT: MXSWrapperBase
        TANGENT_CONNECTED: bool
        TANGENT_SHADER: None
        TANGENT_SPACE: bool
        ...
    class Ai_Vector_To_Rgb(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        MODE: int
        MODE_CONNECTED: bool
        MODE_SHADER: None
        ...
    class Ai_Visible_Light(TextureMap):
        ...
    class Ai_Volume_Collector(Material):
        ...
    class Ai_Volume_Sample_Float(TextureMap):
        BIAS: float
        CHANNEL: str
        CLAMP_MAX: bool
        CLAMP_MIN: bool
        CONTRAST: float
        CONTRAST_PIVOT: float
        GAIN: float
        INPUT_MAX: float
        INPUT_MIN: float
        INTERPOLATION: int
        OUTPUT_MAX: float
        OUTPUT_MIN: float
        POSITION_OFFSET: MXSWrapperBase
        POSITION_OFFSET_CONNECTED: bool
        POSITION_OFFSET_SHADER: None
        SDF_BLEND: float
        SDF_BLEND_CONNECTED: bool
        SDF_BLEND_SHADER: None
        SDF_INVERT: bool
        SDF_OFFSET: float
        SDF_OFFSET_CONNECTED: bool
        SDF_OFFSET_SHADER: None
        VOLUME_TYPE: int
        ...
    class Ai_Volume_Sample_Rgb(TextureMap):
        ADD: float
        CHANNEL: str
        CONTRAST: float
        CONTRAST_PIVOT: float
        EXPOSURE: float
        GAMMA: float
        HUE_SHIFT: float
        INTERPOLATION: int
        MULTIPLY: float
        POSITION_OFFSET: MXSWrapperBase
        POSITION_OFFSET_CONNECTED: bool
        POSITION_OFFSET_SHADER: None
        SATURATION: float
        ...
    class Ai_Wireframe(TextureMap):
        EDGE_TYPE: int
        EDGE_TYPE_CONNECTED: bool
        EDGE_TYPE_SHADER: None
        FILL_COLOR: MXSWrapperBase
        FILL_COLOR_CONNECTED: bool
        FILL_COLOR_SHADER: None
        LINE_COLOR: MXSWrapperBase
        LINE_COLOR_CONNECTED: bool
        LINE_COLOR_SHADER: None
        LINE_WIDTH: float
        LINE_WIDTH_CONNECTED: bool
        LINE_WIDTH_SHADER: None
        RASTER_SPACE: bool
        RASTER_SPACE_CONNECTED: bool
        RASTER_SPACE_SHADER: None
        ...
    class Alpha(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class AlphaRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class Amax(Primitive):
        ...
    class AmbientColor(Color):
        ...
    class AmbientColorController(Bezier_Color):
        ...
    class Amin(Primitive):
        ...
    class Angle(Shape):
        ADAPTIVE: bool
        ANGLE: float
        ANGLE_EDGEFILLET: float
        ANGLE_LENGTH: float
        ANGLE_RADIUS2: float
        ANGLE_RADIUS: float
        ANGLE_SYNCCORNERFILLETS: bool
        ANGLE_THICKNESS: float
        ANGLE_WIDTH: float
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        MAPCOORDS: bool
        OPTIMIZE: bool
        QUAD_CAP: bool
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        TWIST_CORRECTION: bool
        TYPEIN_CREATIONMETHOD: bool
        TYPEIN_EDGEFILLET: float
        TYPEIN_LENGTH: float
        TYPEIN_RADIUS2: float
        TYPEIN_RADIUS: float
        TYPEIN_THICKNESS: float
        TYPEIN_WIDTH: float
        TYPEIN_X: float
        TYPEIN_Y: float
        TYPEIN_Z: float
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        ...
    class AnimateAll(Primitive):
        ...
    class AnimateVertex(Primitive):
        ...
    class AnimationRange(Interval):
        ...
    class ApolloParamContainer(GeometryClass):
        ...
    class Append(Generic):
        ...
    class AppendClip(BipedGeneric):
        ...
    class AppendCurve(NURBSGenericMethodsWrapper):
        ...
    class AppendCurveByID(NURBSGenericMethodsWrapper):
        ...
    class AppendGizmo(Generic):
        ...
    class AppendIfUnique(Primitive):
        ...
    class AppendKey(Primitive):
        ...
    class AppendMaxClip(BipedGeneric):
        ...
    class AppendObject(NURBSGenericMethodsWrapper):
        ...
    class AppendTrack(BipedGeneric):
        ...
    class AppendTrackgroup(BipedGeneric):
        ...
    class AppendUCurve(NURBSGenericMethodsWrapper):
        ...
    class AppendUCurveByID(NURBSGenericMethodsWrapper):
        ...
    class AppendVCurve(NURBSGenericMethodsWrapper):
        ...
    class AppendVCurveByID(NURBSGenericMethodsWrapper):
        ...
    class ApplyEaseCurve(Generic):
        ...
    class ApplyOffset(Primitive):
        ...
    class ApplymaxIKCA(AttributeDef):
        ...
    class Apropos(Primitive):
        ...
    class ArchiveMaxFile(Primitive):
        ...
    class AreMtlAndRendererCompatible(Primitive):
        ...
    class AreNodesInstances(Primitive):
        ...
    class Arnold_Cyl_Camera(Camera):
        ARNOLD_NODE: str
        ARNOLD_NODE_HORIZONTAL_FOV: float
        ARNOLD_NODE_PROJECTIVE: bool
        ARNOLD_NODE_VERTICAL_FOV: float
        ...
    class Arnold_Fisheye_Camera(Camera):
        ARNOLD_NODE: str
        ARNOLD_NODE_AUTOCROP: bool
        ARNOLD_NODE_FOV: float
        ...
    class Arnold_Spherical_Camera(Camera):
        ARNOLD_NODE: str
        ...
    class Arnold_Vr_Camera(Camera):
        ARNOLD_NODE: str
        ARNOLD_NODE_BOTTOM_MERGE_ANGLE: float
        ARNOLD_NODE_BOTTOM_MERGE_MODE: int
        ARNOLD_NODE_EYE_SEPARATION: float
        ARNOLD_NODE_EYE_TO_NECK: float
        ARNOLD_NODE_MODE: int
        ARNOLD_NODE_PROJECTION: int
        ARNOLD_NODE_TOP_MERGE_ANGLE: float
        ARNOLD_NODE_TOP_MERGE_MODE: int
        ...
    class Arnoldlight_Cylindermanip(Helper):
        ...
    class Arnoldlight_Quadmanip(Helper):
        ...
    class Arnoldlight_Radiusmanip(Helper):
        ...
    class Arnoldlight_Spotmanip(Helper):
        ...
    class Asin(Generic):
        ...
    class AssemblyMgr(Interface):
        ...
    class Assert_Array_Equal(Primitive):
        ...
    class Assert_Bitarray_Equal(Primitive):
        ...
    class Assert_Defined(Primitive):
        ...
    class Assert_Equal(Primitive):
        ...
    class Assert_False(Primitive):
        ...
    class Assert_Float(Primitive):
        ...
    class Assert_Float_Equal(Primitive):
        ...
    class Assert_Matchpattern(Primitive):
        ...
    class Assert_Matrix_Equal(Primitive):
        ...
    class Assert_Not_Equal(Primitive):
        ...
    class Assert_Point2_Equal(Primitive):
        ...
    class Assert_Point3_Equal(Primitive):
        ...
    class Assert_Point4_Equal(Primitive):
        ...
    class Assert_String_Equal(Primitive):
        ...
    class Assert_True(Primitive):
        ...
    class Assert_Undefined(Primitive):
        ...
    class AssetUser(Name):
        ...
    class AssignKey(Primitive):
        ...
    class Atan(Generic):
        ...
    class Atan2(Generic):
        ...
    class AtmosphereRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class Atmospheric(MAXWrapper):
        ...
    class Attach(Generic):
        ...
    class AttachNodesToGroup(Primitive):
        ...
    class AutoProjectSwitcherOnFilePreOpen(MAXScriptFunction):
        ...
    class Autosave(Interface):
        ...
    class BackgroundColor(Color):
        ...
    class BackgroundColorController(Bezier_Color):
        ...
    class BakeSetupController_AbsoluteMode(MAXScriptFunction):
        ...
    class BakeSetupController_AdditiveMode(MAXScriptFunction):
        ...
    class BakeShell(Material):
        BAKEDMATERIAL: MXSWrapperBase
        ORIGINALMATERIAL: MXSWrapperBase
        RENDERMTLINDEX: int
        VIEWPORTMTLINDEX: int
        ...
    class BakeUnsetupController_DontRevert(MAXScriptFunction):
        ...
    class BakeUnsetupController_Revert(MAXScriptFunction):
        ...
    class BatchRenderMgr(Interface):
        ...
    class BeautyRenderElement(RenderElement):
        ...
    class Bezier_Color(Point3Controller):
        ...
    class Bezier_Float(FloatController):
        ...
    class Bezier_Point3(Point3Controller):
        ...
    class Bezier_Point4(Point4Controller):
        ...
    class Bezier_Position(PositionController):
        ...
    class Bezier_Rgba(Point4Controller):
        ...
    class Bezier_Rotation(RotationController):
        ...
    class Bezier_Scale(ScaleController):
        ...
    class Beziershape(MAXBezierShapeClass):
        ...
    class BgndRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class BindKnot(NodeGeneric):
        ...
    class BindSpaceWarp(NodeGeneric):
        ...
    class BipedSystem(System):
        ...
    class Bitmap(Value):
        ...
    class BitmapTex(TextureMap):
        ALPHASOURCE: int
        APPLY: bool
        BITMAP: None
        CLIPH: float
        CLIPU: float
        CLIPV: float
        CLIPW: float
        COORDS: MXSWrapperBase
        CROPPLACE: int
        ENDCONDITION: int
        FILENAME: str
        FILTERING: int
        JITTER: float
        MONOOUTPUT: int
        OUTPUT: MXSWrapperBase
        PLAYBACKRATE: float
        PREMULTALPHA: bool
        RGBOUTPUT: int
        STARTTIME: MXSWrapperBase
        TIETIMETOMATIDS: bool
        USEJITTER: bool
        ...
    class Black(Color):
        ...
    class BlockMgr(Interface):
        ...
    class Blue(Color):
        ...
    class Blur(RenderEffect):
        BDIRALPHA: bool
        BDIRROTATION: int
        BDIRUPIXRAD: float
        BDIRUTRAIL: float
        BDIRVPIXRAD: float
        BDIRVTRAIL: float
        BLUR_TYPE: int
        BRADIALALPHA: bool
        BRADIALNODE: None
        BRADIALPIXRAD: float
        BRADIALTRAIL: float
        BRADIALUSENODE: bool
        BRADIALXORIG: int
        BRADIALYORIG: int
        BUNIFALPHA: bool
        BUNIFPIXRAD: float
        SELGENBRIGHTTYPE: int
        SELIBACKACTIVE: bool
        SELIBACKBLEND: float
        SELIBACKBRIGHTEN: float
        SELIBACKFRADIUS: float
        SELIMAGEACTIVE: bool
        SELIMAGEBLEND: float
        SELIMAGEBRIGHTEN: float
        SELLUMACTIVE: bool
        SELLUMBLEND: float
        SELLUMBRIGHTEN: float
        SELLUMFRADIUS: float
        SELLUMMAX: float
        SELLUMMIN: float
        SELMASKACTIVE: bool
        SELMASKBLEND: float
        SELMASKBRIGHTEN: float
        SELMASKCHANNEL: int
        SELMASKFRADIUS: float
        SELMASKMAP: None
        SELMASKMAX: float
        SELMASKMIN: float
        SELMATIDSACTIVE: bool
        SELMATIDSBLEND: float
        SELMATIDSBRIGHTEN: float
        SELMATIDSFRADIUS: float
        SELMATIDSIDS: MXSWrapperBase
        SELMATIDSLUMMAX: float
        SELMATIDSLUMMIN: float
        SELOBJIDSACTIVE: bool
        SELOBJIDSBLEND: float
        SELOBJIDSBRIGHTEN: float
        SELOBJIDSFRADIUS: float
        SELOBJIDSIDS: MXSWrapperBase
        SELOBJIDSLUMMAX: float
        SELOBJIDSLUMMIN: float
        ...
    class Bmpio(BitmapIO):
        ...
    class Boolcntrl(FloatController):
        ...
    class Boolean_Float(FloatController):
        ...
    class BreakCurve(Primitive):
        ...
    class BreakSurface(Primitive):
        ...
    class BriteCon(RenderEffect):
        BRIGHTNESS: float
        CONTRAST: float
        IGNOREBACK: bool
        ...
    class Brown(Color):
        ...
    class Bsearch(Primitive):
        ...
    class BuildTVFaces(Generic):
        ...
    class BuildVCFaces(Generic):
        ...
    class Camera(Node):
        ...
    class Cameras(ObjectSet):
        ...
    class CanConvertTo(Generic):
        ...
    class CancelTryContinueBox(Primitive):
        ...
    class CavityMap(Primitive):
        ...
    class CcCurve(Value):
        ...
    class CcPoint(Value):
        ...
    class Ceil(Generic):
        ...
    class CellularTex(TextureMap):
        ADAPTIVE: bool
        CELLCOLOR: MXSWrapperBase
        CELLMAP: None
        COORDS: MXSWrapperBase
        DIVCOLOR1: MXSWrapperBase
        DIVCOLOR2: MXSWrapperBase
        DIVMAP1: None
        DIVMAP2: None
        FRACTAL: bool
        HIGHTHRESH: float
        ITERATION: float
        LOWTHRESH: float
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        MAP3ENABLED: bool
        MIDTHRESH: float
        OUTPUT: MXSWrapperBase
        ROUGHNESS: float
        SIZE: float
        SMOOTH: float
        SPREAD: float
        TYPE: int
        VARIATION: float
        ...
    class Channel(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        CHANNEL_LENGTH: float
        CHANNEL_RADIUS2: float
        CHANNEL_RADIUS: float
        CHANNEL_SYNCCORNERFILLETS: bool
        CHANNEL_THICKNESS: float
        CHANNEL_WIDTH: float
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        MAPCOORDS: bool
        OPTIMIZE: bool
        QUAD_CAP: bool
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        TWIST_CORRECTION: bool
        TYPEIN_CREATIONMETHOD: bool
        TYPEIN_LENGTH: float
        TYPEIN_RADIUS2: float
        TYPEIN_RADIUS: float
        TYPEIN_THICKNESS: float
        TYPEIN_WIDTH: float
        TYPEIN_X: float
        TYPEIN_Y: float
        TYPEIN_Z: float
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        ...
    class CheckBakedPositionName(MAXScriptFunction):
        ...
    class CheckBakedRotationName(MAXScriptFunction):
        ...
    class ClassOf(Generic):
        ...
    class Clear(Generic):
        ...
    class ClearAllAppData(Generic):
        ...
    class ClearCacheEntry(Generic):
        ...
    class ClearControllerNewFlag(Primitive):
        ...
    class ClearListener(Primitive):
        ...
    class ClearMixer(BipedGeneric):
        ...
    class ClearProdTess(NURBSGenericMethodsWrapper):
        ...
    class ClearSelection(Primitive):
        ...
    class ClearTrack(BipedGeneric):
        ...
    class ClearTrackgroup(BipedGeneric):
        ...
    class ClearUndoBuffer(Primitive):
        ...
    class ClearViewTess(NURBSGenericMethodsWrapper):
        ...
    class Close(Generic):
        ...
    class CloseCameraTracker(Primitive):
        ...
    class CloseRolloutFloater(Primitive):
        ...
    class CloseU(NURBSGenericMethodsWrapper):
        ...
    class CloseUtility(Primitive):
        ...
    class CloseV(NURBSGenericMethodsWrapper):
        ...
    class Close_Enough(Primitive):
        ...
    class Closelog(Primitive):
        ...
    class Clothfx(Modifier):
        ADVANCEDPINCHING: bool
        CHECKINTERSECTIONS: bool
        CLOTHCLOTHMETHOD: int
        ENABLEENDFRAME: bool
        ENDFRAME: int
        GRAVITY: float
        IGNOREBACKFACING: bool
        RELATIVEVELOCITY: float
        SCALE: float
        SELFCOLLISION: bool
        SHOWCURRENTSTATE: bool
        SHOWENABLEDCLOTHCOLLISION: bool
        SHOWENABLEDSOLIDCOLLISION: bool
        SHOWSEWINGSPRINGS: bool
        SHOWTARGETSTATE: bool
        SHOWTENSION: bool
        SIMONMOUSEDOWN: bool
        SIMONRENDER: bool
        SIMPRIORITY: int
        SOLIDCOLLISION: bool
        STARTFRAME: int
        SUBSAMPLE: int
        TENSIONSCALE: float
        TIMESCALE: float
        TIMESTEP: float
        USEGRAVITY: bool
        USESEWINGSPRINGS: bool
        WELDMETHOD: int
        ...
    class CmdPanel(Interface):
        ...
    class Collapse(UtilityPlugin):
        ...
    class CollapseStack(NodeGeneric):
        ...
    class Collapseface(Generic):
        ...
    class Color(Value):
        ...
    class ColorBalance(RenderEffect):
        BLUE: int
        GREEN: int
        IGNOREBACK: bool
        PRESERVELUM: bool
        RED: int
        ...
    class ColorMan(Interface):
        ...
    class ColorPicker(MAXWrapperNonRefTarg):
        ...
    class ColorPickerDlg(Primitive):
        ...
    class ColorReferenceTarget(ReferenceTarget):
        BLUE: int
        BLUE_VARIATION: int
        COLOR: MXSWrapperBase
        FILTER: None
        GREEN: int
        GREEN_VARIATION: int
        HUE: int
        HUE_VARIATION: int
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        INPUT_7: None
        INPUT_8: None
        RANDOM_SEED: int
        RED: int
        RED_VARIATION: int
        SATURATION: int
        SATURATION_VARIATION: int
        SYNC_TYPE: int
        TYPE: int
        USE_BLUE_VARIATION: bool
        USE_E7: bool
        USE_E8: bool
        USE_GREEN_VARIATION: bool
        USE_HSV_E1: bool
        USE_HSV_E2: bool
        USE_HSV_E3: bool
        USE_HSV_E4: bool
        USE_HSV_E5: bool
        USE_HSV_E6: bool
        USE_HSV_I1: bool
        USE_HSV_I2: bool
        USE_HSV_I3: bool
        USE_HSV_I4: bool
        USE_HSV_I5: bool
        USE_HSV_I6: bool
        USE_HUE_VARIATION: bool
        USE_RED_VARIATION: bool
        USE_RGB_E1: bool
        USE_RGB_E2: bool
        USE_RGB_E3: bool
        USE_RGB_E4: bool
        USE_RGB_E5: bool
        USE_RGB_E6: bool
        USE_RGB_I1: bool
        USE_RGB_I2: bool
        USE_RGB_I3: bool
        USE_RGB_I4: bool
        USE_RGB_I5: bool
        USE_RGB_I6: bool
        USE_SATURATION_VARIATION: bool
        USE_VALUE_VARIATION: bool
        VALUE: int
        VALUE_VARIATION: int
        VARIATION_TYPE: int
        ...
    class CompareBitmaps(Primitive):
        ...
    class Composite(Generic):
        ...
    class CompositeTexture(TextureMap):
        BLENDMODE: MXSWrapperBase
        DLGOPENED: MXSWrapperBase
        LAYERNAME: MXSWrapperBase
        MAPENABLED: MXSWrapperBase
        MAPLIST: MXSWrapperBase
        MASK: MXSWrapperBase
        MASKENABLED: MXSWrapperBase
        OPACITY: MXSWrapperBase
        ...
    class Compositematerial(Material):
        AMOUNT: MXSWrapperBase
        MAPENABLES: MXSWrapperBase
        MATERIALLIST: MXSWrapperBase
        MIXTYPE: MXSWrapperBase
        ...
    class ComputeAnimation(BipedGeneric):
        ...
    class ConformToShape(Primitive):
        ...
    class Contains(Generic):
        ...
    class Contrast(VideoPostFilter):
        ...
    class ConvertTo(NodeGeneric):
        ...
    class ConvertToMesh(NodeGeneric):
        ...
    class ConvertToNURBSCurve(Primitive):
        ...
    class ConvertToNURBSSurface(Primitive):
        ...
    class ConvertToPoly(NodeGeneric):
        ...
    class ConvertToSplineShape(NodeGeneric):
        ...
    class Copy(NodeGeneric):
        ...
    class CopyFile(Primitive):
        ...
    class CopyMixdownToBiped(BipedGeneric):
        ...
    class CopyPasteKeys(Primitive):
        ...
    class Cos(Generic):
        ...
    class Cosh(Generic):
        ...
    class Cpptests(Interface):
        ...
    class CreateFloatControllerWithRandomValues(Primitive):
        ...
    class CreateInstance(Generic):
        ...
    class CreateMorphObject(Primitive):
        ...
    class CreateNumberedFilename(Primitive):
        ...
    class CreateOLEObject(Primitive):
        ...
    class CreatePointCloudMaterial(MAXScriptFunction):
        ...
    class CreateReaction(Primitive):
        ...
    class Createfile(Primitive):
        ...
    class Crop(Generic):
        ...
    class Cross(Generic):
        ...
    class Cubic(Filter):
        ...
    class CurrentMaterialLibrary(MaterialLibrary):
        ...
    class CurrentTime(Time):
        ...
    class CurveLength(NodeGeneric):
        ...
    class CustAttribCollapseManager(Interface):
        ...
    class CwsWarn(MAXScriptFunction):
        ...
    class Cws_Ops_Array(Array):
        ...
    class DSightRender(RenderEffect):
        ALPHABLEND: bool
        DIMBG: bool
        EDITTEXTBC: str
        EDITTEXTBL: str
        EDITTEXTBR: str
        EDITTEXTTC: str
        EDITTEXTTL: str
        EDITTEXTTR: str
        FONTSCALE: int
        FRAMEPAD: int
        IMAGEFNAME: str
        IMAGE_X: int
        IMAGE_Y: int
        IMGOPACITY: int
        REQDDISTANCE: int
        TRANSFER_MODE: int
        TYPETEXTBC: int
        TYPETEXTBL: int
        TYPETEXTBR: int
        TYPETEXTTC: int
        TYPETEXTTL: int
        TYPETEXTTR: int
        USEIMAGE: bool
        ...
    class DebugVisualizerApexClothingAutoUI(MAXScriptFunction):
        ...
    class DebugVisualizerAutoUI(MAXScriptFunction):
        ...
    class DebugVisualizerClothingAutoUI(MAXScriptFunction):
        ...
    class DeepCopy(Primitive):
        ...
    class DefaultActions(Interface):
        ...
    class DefaultVCFaces(Generic):
        ...
    class DelINISetting(Primitive):
        ...
    class Delete(Primitive):
        ...
    class DeleteAllChangeHandlers(Primitive):
        ...
    class DeleteAllCopies(BipedGeneric):
        ...
    class DeleteAppData(Generic):
        ...
    class DeleteAtmospheric(Primitive):
        ...
    class DeleteChangeHandler(Primitive):
        ...
    class DeleteCopy(BipedGeneric):
        ...
    class DeleteEaseCurve(MappedGeneric):
        ...
    class DeleteEffect(Primitive):
        ...
    class DeleteFile(Primitive):
        ...
    class DeleteGizmo(Generic):
        ...
    class DeleteItem(Generic):
        ...
    class DeleteKey(Generic):
        ...
    class DeleteKeys(MappedGeneric):
        ...
    class DeleteKnot(NodeGeneric):
        ...
    class DeleteModifier(NodeGeneric):
        ...
    class DeleteMorphTarget(Primitive):
        ...
    class DeleteMultiplierCurve(Generic):
        ...
    class DeleteNoteKey(Generic):
        ...
    class DeleteNoteKeys(Generic):
        ...
    class DeleteNoteTrack(Primitive):
        ...
    class DeleteObjects(NURBSGenericMethodsWrapper):
        ...
    class DeletePoint(CurveCtlGeneric):
        ...
    class DeleteReaction(Primitive):
        ...
    class DeleteScript(BipedGeneric):
        ...
    class DeleteSnippet(BipedGeneric):
        ...
    class DeleteSpline(NodeGeneric):
        ...
    class DeleteTime(MappedGeneric):
        ...
    class DeleteTrack(BipedGeneric):
        ...
    class DeleteTrackViewController(Primitive):
        ...
    class DeleteTrackViewNode(Primitive):
        ...
    class DeleteTracker(Generic):
        ...
    class DeleteTrackgroup(BipedGeneric):
        ...
    class DeleteTranInfo(BipedGeneric):
        ...
    class DeleteTransition(BipedGeneric):
        ...
    class DeleteTransitionsTo(BipedGeneric):
        ...
    class DeleteUserProp(Primitive):
        ...
    class Deleteface(Generic):
        ...
    class Deletevert(Generic):
        ...
    class DensityMap(Primitive):
        ...
    class Dents(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COORDS: MXSWrapperBase
        ITERATIONS: int
        MAP1: None
        MAP1ENABLED: bool
        MAP2: None
        MAP2ENABLED: bool
        SIZE: float
        STRENGTH: float
        ...
    class DependsOn(Primitive):
        ...
    class Deselect(NodeGeneric):
        ...
    class DeselectKey(Generic):
        ...
    class DeselectKeys(MappedGeneric):
        ...
    class DetachFaces(Generic):
        ...
    class DetachNodesFromGroup(Primitive):
        ...
    class DetachVerts(Generic):
        ...
    class DiffuseMap(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        LIGHTINGON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        SHADOWSON: bool
        TARGETMAPSLOTNAME: str
        ...
    class DiffuseRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        LIGHTINGON: bool
        ...
    class DisableDisplayFilterCallbacks(Primitive):
        ...
    class DisableRedrawViewsCallbacks(Primitive):
        ...
    class DisableRefMsgs(Primitive):
        ...
    class DisableSelectFilterCallbacks(Primitive):
        ...
    class DisableTimeCallbacks(Primitive):
        ...
    class Disconnect(NURBSGenericMethodsWrapper):
        ...
    class DisplacementToPreset(Generic):
        ...
    class Display(Generic):
        ...
    class DisplayControlDialog(Primitive):
        ...
    class DisplayFilterCallbacksEnabled(Primitive):
        ...
    class Distance(Generic):
        ...
    class DoesDirectoryExist(Primitive):
        ...
    class DoesFileExist(Primitive):
        ...
    class DoesUserPropExist(Primitive):
        ...
    class DontCollect(UndefinedClass):
        ...
    class Dot(Generic):
        ...
    class DotNetClass(Value):
        ...
    class DotNetControl(RolloutControl):
        ...
    class DotNetMXSValue(Value):
        ...
    class DotNetMethod(Value):
        ...
    class DotNetObject(Value):
        ...
    class DoubleSidedMat(Material):
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        MATERIAL1: MXSWrapperBase
        MATERIAL2: MXSWrapperBase
        TRANSLUCENCY: float
        ...
    class DragAndDrop(Interface):
        ...
    class DumpMAXStrings(Primitive):
        ...
    class DustMap(Primitive):
        ...
    class Dxshadermanager(Interface):
        ...
    class Edit(Primitive):
        ...
    class EditAtmospheric(Primitive):
        ...
    class EditEffect(Primitive):
        ...
    class EmissionRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class Empty(Generic):
        ...
    class EmptyVal(EmptyClass):
        ...
    class EnableDisplayFilterCallbacks(Primitive):
        ...
    class EnableHardwareMaterial(Primitive):
        ...
    class EnableORTs(MappedGeneric):
        ...
    class EnableRedrawViewsCallbacks(Primitive):
        ...
    class EnableRefMsgs(Primitive):
        ...
    class EnableSelectFilterCallbacks(Primitive):
        ...
    class EnableTimeCallbacks(Primitive):
        ...
    class EnableUndo(Primitive):
        ...
    class EncryptFile(Primitive):
        ...
    class EncryptScript(Primitive):
        ...
    class EnlargeBy(UserGeneric):
        ...
    class EnumerateFiles(Primitive):
        ...
    class Eof(Generic):
        ...
    class EulerToQuat(Primitive):
        ...
    class EvalPos(NURBSGenericMethodsWrapper):
        ...
    class EvalTangent(NURBSGenericMethodsWrapper):
        ...
    class EvalUTangent(NURBSGenericMethodsWrapper):
        ...
    class EvalVTangent(NURBSGenericMethodsWrapper):
        ...
    class Execute(Generic):
        ...
    class ExecuteScriptFile(Primitive):
        ...
    class Exp(Generic):
        ...
    class ExpandToInclude(UserGeneric):
        ...
    class ExplodeGroup(Primitive):
        ...
    class ExportFile(Primitive):
        ...
    class ExprForMAXObject(Generic):
        ...
    class Extrudeface(Generic):
        ...
    class Falloff(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        DIRECTION: int
        EXTRAPOLATEON: bool
        FARDISTANCE: float
        IOR: float
        MAP1: None
        MAP1AMOUNT: float
        MAP1ON: bool
        MAP2: None
        MAP2AMOUNT: float
        MAP2ON: bool
        MTLIOROVERRIDE: bool
        NEARDISTANCE: float
        NODE: None
        TYPE: int
        ...
    class FallofftextureMap(TextureMap):
        ...
    class Fclose(Primitive):
        ...
    class FetchMaxFile(Primitive):
        ...
    class Fflush(Primitive):
        ...
    class FileOut(RenderEffect):
        ACTIVE: bool
        AFFECTSOURCE: bool
        CAMERANODE: None
        CHANNELTYPE: int
        FARZ: float
        FITSCENE: bool
        NEARZ: float
        ...
    class Filein(Primitive):
        ...
    class FilenameFromPath(Primitive):
        ...
    class Filepos(Generic):
        ...
    class Filter(MAXWrapper):
        ...
    class FindItem(Generic):
        ...
    class FindPattern(Generic):
        ...
    class FindProjectFolderFromFileName(MAXScriptFunction):
        ...
    class FindString(Generic):
        ...
    class Findobject(MAXScriptFunction):
        ...
    class FlagChanged(Generic):
        ...
    class FlagForeground(NodeGeneric):
        ...
    class FlagSendPropertiesToEditor(Primitive):
        ...
    class FlatMirror(TextureMap):
        APPLYBLUR: bool
        APPLYTOFACEID: bool
        BLURAMOUNT: float
        DISTORTIONAMOUNT: float
        DISTORTIONTYPE: int
        FACEID: int
        FRAME: int
        LEVEL: float
        NOISETYPE: int
        NTHFRAME: int
        PHASE: float
        SIZE: float
        USEENVIROMENT: bool
        ...
    class Flightstudioimage(BitmapIO):
        ...
    class Float(Value):
        ...
    class FloatController(MAXWrapper):
        ...
    class Float_ListDummyEntry(FloatController):
        ...
    class Float_Limit(FloatController):
        ENABLE: bool
        LOWER_LIMIT: float
        LOWER_LIMIT_ENABLED: bool
        LOWER_SMOOTHING: float
        STATIC_VALUE: float
        UPPER_LIMIT: float
        UPPER_LIMIT_ENABLED: bool
        UPPER_SMOOTHING: float
        ...
    class Float_List(FloatController):
        AVERAGE: bool
        WEIGHT: MXSWrapperBase
        ...
    class Float_Script(FloatController):
        SCRIPT: str
        ...
    class Floor(Generic):
        ...
    class Flush(Generic):
        ...
    class Flushlog(Primitive):
        ...
    class Fopen(Primitive):
        ...
    class Fopenexr(BitmapIO):
        ...
    class ForceReloadBitmapFile(Primitive):
        ...
    class Format(Primitive):
        ...
    class FormattedPrint(Primitive):
        ...
    class FractalNoise(Primitive):
        ...
    class Free(Generic):
        ...
    class FreeIesSun(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        CASTSHADOWS: bool
        CONTRAST: float
        HASTARGET: bool
        MULTIPLIER: float
        ON: bool
        RGB: MXSWrapperBase
        SHADOWMULTIPLIER: float
        SOFTENDIFFUSEEDGE: float
        TARGETDISTANCE: None
        USEGLOBALSHADOWSETTINGS: bool
        ...
    class FreeSceneBitmaps(Primitive):
        ...
    class FreeSpot(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ASPECT: float
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        ATTENDECAY: int
        CASTSHADOWS: bool
        COLOR: MXSWrapperBase
        CONESHAPE: int
        CONTRAST: float
        DECAYRADIUS: float
        ENABLED: bool
        EXCLUDELIST: MXSWrapperBase
        FALLOFF: float
        FARATTENEND: float
        FARATTENSTART: float
        HOTSPOT: float
        HSV: MXSWrapperBase
        HUE: int
        INCLEXCLTYPE: int
        INCLUDELIST: None
        LIGHTAFFECTSSHADOW: bool
        LIGHTSHAPE: int
        MULTIPLIER: float
        NEARATTENEND: float
        NEARATTENSTART: float
        ON: bool
        OVERSHOOT: bool
        PROJECTOR: bool
        PROJECTORMAP: None
        RAYTRACEDSHADOWS: bool
        RGB: MXSWrapperBase
        SATURATION: int
        SHADOWCOLOR: MXSWrapperBase
        SHADOWGENERATOR: MXSWrapperBase
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHOWCONE: bool
        SHOWFARATTEN: bool
        SHOWNEARATTEN: bool
        SOFTENDIFFUSEEDGE: float
        TYPE: MXSWrapperBase
        USEFARATTEN: bool
        USEGLOBALSHADOWSETTINGS: bool
        USENEARATTEN: bool
        USESHADOWPROJECTORMAP: bool
        VALUE: int
        ...
    class Freeze(NodeGeneric):
        ...
    class FreezeSelection(Primitive):
        ...
    class Fseek(Primitive):
        ...
    class Ftell(Primitive):
        ...
    class GPxRBKeys(Array):
        ...
    class GSimClock(DotNetObject):
        ...
    class Gc(Primitive):
        ...
    class GenClassID(Primitive):
        ...
    class GenGUID(Primitive):
        ...
    class GenerateAPIList(Primitive):
        ...
    class Geometry(ObjectSet):
        ...
    class GeometryReferenceTarget(ReferenceTarget):
        ANIMATED_SURFACE: bool
        FILTER: None
        GEOMETRY_SAFE_MODE: bool
        GRADIENT_DELTA: float
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        INPUT_7: None
        MAP_CHANNEL_INDEX: int
        RANDOM_SEED: int
        SEPARATE_CHILDREN: bool
        SEPARATE_GROUP_MEMBERS: bool
        STATIC_OBJECTS: bool
        SUBFRAME_GEOMETRY: bool
        SUBFRAME_PLACEMENT: bool
        SUB_MATERIAL_INDEX: int
        TYPE: int
        USE_E7: bool
        USE_I3: bool
        USE_R6: bool
        USE_SUB_MATERIAL: bool
        USE_T2: bool
        USE_V4: bool
        USE_V5: bool
        ...
    class GetActiveCamera(Primitive):
        ...
    class GetAfterORT(Generic):
        ...
    class GetAnimByHandle(Primitive):
        ...
    class GetAnimByPointer(Primitive):
        ...
    class GetAnimPointer(Primitive):
        ...
    class GetAppData(Generic):
        ...
    class GetAtmospheric(Primitive):
        ...
    class GetAvailableSubstanceGraphsAndOutputsFromPackage(Primitive):
        ...
    class GetBeforeORT(Generic):
        ...
    class GetBitmapInfo(Primitive):
        ...
    class GetBitmapOpenFileName(Primitive):
        ...
    class GetBitmapSaveFileName(Primitive):
        ...
    class GetCINCfg(MAXScriptFunction):
        ...
    class GetCPTM(Primitive):
        ...
    class GetCV(NURBSGenericMethodsWrapper):
        ...
    class GetChannel(Generic):
        ...
    class GetChannelAsMask(Generic):
        ...
    class GetClassCounts(Primitive):
        ...
    class GetClassInstances(Primitive):
        ...
    class GetClassName(Primitive):
        ...
    class GetClip(BipedGeneric):
        ...
    class GetCopy(BipedGeneric):
        ...
    class GetCoreInterfaces(Primitive):
        ...
    class GetCurNameSelSet(Primitive):
        ...
    class GetCurrentException(Primitive):
        ...
    class GetCurrentExceptionCallStack(Primitive):
        ...
    class GetCurrentExceptionStackTrace(Primitive):
        ...
    class GetCurrentSelection(Primitive):
        ...
    class GetCursorPos(Primitive):
        ...
    class GetCurve(NURBSGenericMethodsWrapper):
        ...
    class GetCurveID(NURBSGenericMethodsWrapper):
        ...
    class GetCurveStartPoint(NURBSGenericMethodsWrapper):
        ...
    class GetD3DMeshAllocated(Primitive):
        ...
    class GetD3DMeshAllocatedFaces(Primitive):
        ...
    class GetD3DTimer(Primitive):
        ...
    class GetDimensions(Primitive):
        ...
    class GetDirectories(Primitive):
        ...
    class GetDisplacementMapping(Generic):
        ...
    class GetEaseCurve(Primitive):
        ...
    class GetEdge(NURBSGenericMethodsWrapper):
        ...
    class GetEdgeSelection(NodeGeneric):
        ...
    class GetEdgeVis(Generic):
        ...
    class GetEffect(Primitive):
        ...
    class GetErrorSourceFileLine(Primitive):
        ...
    class GetErrorSourceFileName(Primitive):
        ...
    class GetErrorSourceFileOffset(Primitive):
        ...
    class GetFace(Generic):
        ...
    class GetFaceMatID(Generic):
        ...
    class GetFaceNormal(Generic):
        ...
    class GetFaceSelection(NodeGeneric):
        ...
    class GetFaceSmoothGroup(Generic):
        ...
    class GetFileAttribute(Primitive):
        ...
    class GetFileCreateDate(Primitive):
        ...
    class GetFileModDate(Primitive):
        ...
    class GetFileSecurityInfo(Primitive):
        ...
    class GetFileSize(Primitive):
        ...
    class GetFileVersion(Primitive):
        ...
    class GetFilenameFile(Primitive):
        ...
    class GetFilenamePath(Primitive):
        ...
    class GetFilenameType(Primitive):
        ...
    class GetFiles(Primitive):
        ...
    class GetFilter(BipedGeneric):
        ...
    class GetFlip(NURBSGenericMethodsWrapper):
        ...
    class GetFlipTrim(NURBSGenericMethodsWrapper):
        ...
    class GetGenerateUVs(NURBSGenericMethodsWrapper):
        ...
    class GetGizmo(Generic):
        ...
    class GetHandleByAnim(Primitive):
        ...
    class GetHashValue(Primitive):
        ...
    class GetINISetting(Primitive):
        ...
    class GetIconAsBitmap(Primitive):
        ...
    class GetIconSizes(Primitive):
        ...
    class GetInVec(NodeGeneric):
        ...
    class GetIndexedPixels(Generic):
        ...
    class GetIndexedProperty(Primitive):
        ...
    class GetInheritanceFlags(Primitive):
        ...
    class GetInterface(Generic):
        ...
    class GetInterfaces(Generic):
        ...
    class GetKBChar(Primitive):
        ...
    class GetKBLine(Primitive):
        ...
    class GetKBPoint(Primitive):
        ...
    class GetKBValue(Primitive):
        ...
    class GetKey(Generic):
        ...
    class GetKeyIndex(Generic):
        ...
    class GetKeyTime(Generic):
        ...
    class GetKnot(NURBSGenericMethodsWrapper):
        ...
    class GetKnotPoint(NodeGeneric):
        ...
    class GetKnotSelection(Primitive):
        ...
    class GetKnotType(NodeGeneric):
        ...
    class GetLastMergedNodes(Primitive):
        ...
    class GetLastRenderedImage(Primitive):
        ...
    class GetListenerSel(Primitive):
        ...
    class GetListenerSelText(Primitive):
        ...
    class GetLocalTime(Primitive):
        ...
    class GetLog(Primitive):
        ...
    class GetMAXClass(Primitive):
        ...
    class GetMAXFileAssetMetadata(Primitive):
        ...
    class GetMAXFileObjectNames(Primitive):
        ...
    class GetMAXOpenFileName(Primitive):
        ...
    class GetMAXSaveFileName(Primitive):
        ...
    class GetMAXWindowPos(Primitive):
        ...
    class GetMAXWindowSize(Primitive):
        ...
    class GetMKKey(Primitive):
        ...
    class GetMKKeyIndex(Primitive):
        ...
    class GetMKTargetNames(Primitive):
        ...
    class GetMKTargetWeights(Primitive):
        ...
    class GetMKTime(Primitive):
        ...
    class GetMKWeight(Primitive):
        ...
    class GetMTLMEditFlags(Primitive):
        ...
    class GetMTLMeditObjType(Primitive):
        ...
    class GetMTLMeditTiling(Primitive):
        ...
    class GetMaterialID(Primitive):
        ...
    class GetMaxExtensionVersion(Primitive):
        ...
    class GetMaxFileVersionData(Primitive):
        ...
    class GetMaxscriptStartupState(Primitive):
        ...
    class GetMeditMaterial(Primitive):
        ...
    class GetModContextBBox(Primitive):
        ...
    class GetModContextBBoxMax(Generic):
        ...
    class GetModContextBBoxMin(Generic):
        ...
    class GetModContextTM(Generic):
        ...
    class GetMultiplierCurve(Primitive):
        ...
    class GetMultiplierValue(Generic):
        ...
    class GetNURBSSelection(Primitive):
        ...
    class GetNURBSSet(Primitive):
        ...
    class GetNodeBBox(Primitive):
        ...
    class GetNodeByName(Primitive):
        ...
    class GetNodeEventCallbacks(Primitive):
        ...
    class GetNodeTM(Primitive):
        ...
    class GetNoteKeyIndex(Generic):
        ...
    class GetNoteKeyTime(Generic):
        ...
    class GetNoteTrack(Primitive):
        ...
    class GetNumCPVVerts(Generic):
        ...
    class GetNumFaces(Generic):
        ...
    class GetNumSubMtls(Primitive):
        ...
    class GetNumSubTexmaps(Primitive):
        ...
    class GetNumTVerts(Generic):
        ...
    class GetNumVerts(Generic):
        ...
    class GetObject(NURBSGenericMethodsWrapper):
        ...
    class GetObjectName(Primitive):
        ...
    class GetOpenFileName(Primitive):
        ...
    class GetOutVec(NodeGeneric):
        ...
    class GetParent(NURBSGenericMethodsWrapper):
        ...
    class GetParentID(NURBSGenericMethodsWrapper):
        ...
    class GetPixels(Generic):
        ...
    class GetPoint(NURBSGenericMethodsWrapper):
        ...
    class GetPointController(Primitive):
        ...
    class GetPointControllers(Primitive):
        ...
    class GetPointPos(Primitive):
        ...
    class GetProdTess(NURBSGenericMethodsWrapper):
        ...
    class GetProgressCancel(Primitive):
        ...
    class GetPropNames(Generic):
        ...
    class GetProperty(Primitive):
        ...
    class GetPropertyController(Primitive):
        ...
    class GetQtTextExtent(Primitive):
        ...
    class GetRadius(NURBSGenericMethodsWrapper):
        ...
    class GetReactionCount(Primitive):
        ...
    class GetReactionFalloff(Primitive):
        ...
    class GetReactionInfluence(Primitive):
        ...
    class GetReactionName(Primitive):
        ...
    class GetReactionState(Primitive):
        ...
    class GetReactionStrength(Primitive):
        ...
    class GetReactionValue(Primitive):
        ...
    class GetSaveFileName(Primitive):
        ...
    class GetSavePath(Primitive):
        ...
    class GetSaveRequired(Primitive):
        ...
    class GetScriptIndex(BipedGeneric):
        ...
    class GetSeed(NURBSGenericMethodsWrapper):
        ...
    class GetSegLengths(Primitive):
        ...
    class GetSegSelection(Primitive):
        ...
    class GetSegmentType(NodeGeneric):
        ...
    class GetSelectedPts(CurveCtlGeneric):
        ...
    class GetSelectedReactionNum(Primitive):
        ...
    class GetSelectionLevel(Primitive):
        ...
    class GetSimilarNodes(Primitive):
        ...
    class GetSnippetIndex(BipedGeneric):
        ...
    class GetSourceFileLine(Primitive):
        ...
    class GetSourceFileName(Primitive):
        ...
    class GetSourceFileOffSet(Primitive):
        ...
    class GetSplineSelection(Primitive):
        ...
    class GetSplitMesh(Generic):
        ...
    class GetSubAnim(Generic):
        ...
    class GetSubAnimName(Generic):
        ...
    class GetSubAnimNames(Generic):
        ...
    class GetSubMtl(Primitive):
        ...
    class GetSubMtlSlotName(Primitive):
        ...
    class GetSubTexmap(Primitive):
        ...
    class GetSubTexmapSlotName(Primitive):
        ...
    class GetSubdivisionDisplacement(Generic):
        ...
    class GetTVFace(Generic):
        ...
    class GetTextExtent(Primitive):
        ...
    class GetTextureSurface(NURBSGenericMethodsWrapper):
        ...
    class GetTextureUVs(NURBSGenericMethodsWrapper):
        ...
    class GetThisScriptFilename(Primitive):
        ...
    class GetTiling(NURBSGenericMethodsWrapper):
        ...
    class GetTilingOffset(NURBSGenericMethodsWrapper):
        ...
    class GetTimeRange(Generic):
        ...
    class GetTrack(BipedGeneric):
        ...
    class GetTracker(Generic):
        ...
    class GetTrackgroup(BipedGeneric):
        ...
    class GetTransformAxis(Primitive):
        ...
    class GetTransformLockFlags(Primitive):
        ...
    class GetTrimSurface(NURBSGenericMethodsWrapper):
        ...
    class GetUCurve(NURBSGenericMethodsWrapper):
        ...
    class GetUCurveID(NURBSGenericMethodsWrapper):
        ...
    class GetUKnot(NURBSGenericMethodsWrapper):
        ...
    class GetUniversalTime(Primitive):
        ...
    class GetUserProp(NodeGeneric):
        ...
    class GetUserPropBuffer(NodeGeneric):
        ...
    class GetUserPropVal(Primitive):
        ...
    class GetVCFace(Generic):
        ...
    class GetVCurve(NURBSGenericMethodsWrapper):
        ...
    class GetVCurveID(NURBSGenericMethodsWrapper):
        ...
    class GetVKnot(NURBSGenericMethodsWrapper):
        ...
    class GetValue(CurveCtlGeneric):
        ...
    class GetVert(Generic):
        ...
    class GetVertSelection(NodeGeneric):
        ...
    class GetVertexPaintAmounts(Primitive):
        ...
    class GetVertexPaintColors(Primitive):
        ...
    class GetViewFOV(Primitive):
        ...
    class GetViewSize(Primitive):
        ...
    class GetViewTM(Primitive):
        ...
    class GetViewTess(NURBSGenericMethodsWrapper):
        ...
    class GetXYZControllers(Primitive):
        ...
    class GetclipboardBitmap(Primitive):
        ...
    class GetclipboardText(Primitive):
        ...
    class Getnormal(Generic):
        ...
    class Gettvert(Generic):
        ...
    class Getvertcolor(Generic):
        ...
    class GizmoBulge(ReferenceTarget):
        ...
    class GizmoJoint(ReferenceTarget):
        ...
    class GizmoJointMorph(ReferenceTarget):
        ...
    class GlobalDXDisplayManager(Interface):
        ...
    class GlobalInpoint(BipedGeneric):
        ...
    class GlobalOutpoint(BipedGeneric):
        ...
    class GlobalToLocal(BipedGeneric):
        ...
    class GlobalToScaledLocal(BipedGeneric):
        ...
    class GlobalTracks(MAXTVNode):
        ...
    class Go(Primitive):
        ...
    class GotoFrame(Generic):
        ...
    class Gravity(SpacewarpObject):
        DECAY: float
        GRAVITYTYPE: int
        HOOPSON: bool
        ICONSIZE: float
        STRENGTH: float
        ...
    class Gray(Color):
        ...
    class Green(Color):
        ...
    class Grid(Helper):
        ACTIVECOLOR: int
        DISPLAYPLANE: int
        GRID: float
        LENGTH: float
        WIDTH: float
        ...
    class GridPrefs(Interface):
        ...
    class Group(Primitive):
        ...
    class HasCurrentExceptionCallStack(Primitive):
        ...
    class HasCurrentExceptionStackTrace(Primitive):
        ...
    class HasINISetting(Primitive):
        ...
    class HasMacroRecorderContext(MAXScriptFunction):
        ...
    class HasNoteTracks(Primitive):
        ...
    class HasProperty(Primitive):
        ...
    class HeapCheck(Primitive):
        ...
    class HeightManager(Interface):
        ...
    class Help(MAXScriptFunction):
        ...
    class Helper(Node):
        ...
    class Helpers(ObjectSet):
        ...
    class Hide(NodeGeneric):
        ...
    class HideSelectedSegments(NodeGeneric):
        ...
    class HideSelectedSplines(NodeGeneric):
        ...
    class HideSelectedVerts(NodeGeneric):
        ...
    class HoldMaxFile(Primitive):
        ...
    class IDisplayGamma(Interface):
        ...
    class IParserLoader(Interface):
        ...
    class Icon(ReferenceTarget):
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        RANDOM_SEED: int
        STATIC_ICON: bool
        SUBFRAME_GEOMETRY: bool
        SUBFRAME_PLACEMENT: bool
        TYPE: int
        USE_E4: bool
        USE_T1: bool
        USE_V3: bool
        USE_V4: bool
        ...
    class IllumRenderElement(RenderElement):
        ...
    class ImageMotionBlur(RenderEffect):
        DURATION: float
        TRANSPARENCY: bool
        ...
    class Imerge(Interface):
        ...
    class ImportFile(Primitive):
        ...
    class Include(Primitive):
        ...
    class InitGroupMembers(MAXScriptFunction):
        ...
    class InputTextColor(Color):
        ...
    class InsertItem(Primitive):
        ...
    class InsertPoint(CurveCtlGeneric):
        ...
    class InsertSnippet(BipedGeneric):
        ...
    class InsertTime(MappedGeneric):
        ...
    class InsertTrack(BipedGeneric):
        ...
    class InsertTrackgroup(BipedGeneric):
        ...
    class Instance(NodeGeneric):
        ...
    class InstanceReplace(NodeGeneric):
        ...
    class Int(Primitive):
        ...
    class Integer(Value):
        ...
    class InterpBezier3D(Primitive):
        ...
    class InterpCurve3D(Primitive):
        ...
    class IntersectRay(NodeGeneric):
        ...
    class IntersectRayScene(Primitive):
        ...
    class Intersects(NodeGeneric):
        ...
    class InvalTrack(Generic):
        ...
    class InvalidateTM(MappedPrimitive):
        ...
    class InvalidateTreeTM(MappedPrimitive):
        ...
    class InvalidateWS(MappedPrimitive):
        ...
    class Invert(Generic):
        ...
    class Is64BitApplication(Primitive):
        ...
    class IsActive(Primitive):
        ...
    class IsAnimPlaying(Primitive):
        ...
    class IsAnimated(CurveCtlGeneric):
        ...
    class IsClosed(NodeGeneric):
        ...
    class IsCompatible(Generic):
        ...
    class IsController(Primitive):
        ...
    class IsCreatingObject(Primitive):
        ...
    class IsDeformable(Primitive):
        ...
    class IsDeleted(Generic):
        ...
    class IsDirectoryWriteable(Primitive):
        ...
    class IsEmpty(Generic):
        ...
    class IsGroupHead(Primitive):
        ...
    class IsGroupMember(Primitive):
        ...
    class IsIdentity(Generic):
        ...
    class IsKeySelected(Generic):
        ...
    class IsKindOf(Generic):
        ...
    class IsMSCustAttrib(Primitive):
        ...
    class IsMSCustAttribClass(Primitive):
        ...
    class IsMSPlugin(Primitive):
        ...
    class IsMSPluginClass(Primitive):
        ...
    class IsMaxFile(Primitive):
        ...
    class IsMtlUsedInSceneMtl(Primitive):
        ...
    class IsOpenGroupHead(Primitive):
        ...
    class IsOpenGroupMember(Primitive):
        ...
    class IsParticleSystem(Primitive):
        ...
    class IsProperty(Primitive):
        ...
    class IsPropertyAnimatable(Primitive):
        ...
    class IsReadOnly(Primitive):
        ...
    class IsSceneXRefNode(Primitive):
        ...
    class IsSelectionFrozen(Primitive):
        ...
    class IsSpace(Primitive):
        ...
    class IsStruct(Primitive):
        ...
    class IsStructDef(Primitive):
        ...
    class IsUsedInScene(Primitive):
        ...
    class IsValidNode(Primitive):
        ...
    class IsValidObj(Primitive):
        ...
    class IsValidValue(Primitive):
        ...
    class IsWorldSpaceObject(Primitive):
        ...
    class Join(Generic):
        ...
    class JoinCurves(Primitive):
        ...
    class JoinSurfaces(Primitive):
        ...
    class Jpegio(BitmapIO):
        ...
    class Length(Generic):
        ...
    class LengthInterp(NodeGeneric):
        ...
    class LengthTangent(NodeGeneric):
        ...
    class LengthToPathParam(NodeGeneric):
        ...
    class Light(Node):
        ...
    class LightLevelController(Bezier_Float):
        ...
    class LightTintColor(Color):
        ...
    class LightTintColorController(Bezier_Color):
        ...
    class LightingAnalysisDataRenderElement(RenderElement):
        ...
    class Lights(ObjectSet):
        ...
    class Line(Shape):
        ADAPTIVE: bool
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        MAPCOORDS: bool
        OPTIMIZE: bool
        QUAD_CAP: bool
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        STEPS: int
        THICKNESS: float
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        ...
    class Linear_Float(FloatController):
        ...
    class Linear_Position(PositionController):
        ...
    class Linear_Rotation(RotationController):
        ...
    class Linear_Scale(ScaleController):
        ...
    class Listener(WindowStream):
        ...
    class ListenerBackgroundColor(Color):
        ...
    class LoadCUIScheme(MAXScriptFunction):
        ...
    class LoadCurrentPathConfigFile(MAXScriptFunction):
        ...
    class LoadDllsFromDir(Primitive):
        ...
    class LoadFrames(Generic):
        ...
    class LoadMaterialLibrary(Primitive):
        ...
    class LoadMaxAnimationFile(BipedGeneric):
        ...
    class LoadMaxFile(Primitive):
        ...
    class LoadMixFile(BipedGeneric):
        ...
    class LoadMoFlowFile(BipedGeneric):
        ...
    class LoadPicture(Primitive):
        ...
    class LoadSnippetFiles(BipedGeneric):
        ...
    class LoadTempMaterialLibrary(Primitive):
        ...
    class Loadfile(BipedGeneric):
        ...
    class LocalToGlobal(BipedGeneric):
        ...
    class LocalToScaledLocal(BipedGeneric):
        ...
    class Locals(Primitive):
        ...
    class Log(Generic):
        ...
    class Log10(Generic):
        ...
    class Lookat(Matrix3Controller):
        ...
    class LumRenderElement(RenderElement):
        ...
    class MCloth(Modifier):
        ATTACHMENT_RESPONSE_COEFFICIENT: float
        ATTACHMENT_TEAR_FACTOR: float
        ATTACHTOCOLLIDE: bool
        BEHAVIOR: int
        BENDINESS: float
        COLLISION_RESPONSE_COEFFICIENT: float
        COMPRESSIONS_LIMIT: float
        COMPRESSIONS_STIFFNESS: float
        COM_DAMPING: bool
        DAMPING: float
        DAMPING_COEFFICIENT: float
        DENSITY: float
        DISABLE_DYNAMIC_CCD: bool
        DO_ADHERE: bool
        DO_BENDING: bool
        DO_BENDING_ORTHO: bool
        DO_FLUID_COLLISION: bool
        DO_GRAVITY: bool
        DO_HARD_STRETCH_LIMITATION: bool
        DO_INTER_COLLISION: bool
        DO_PRESSURE: bool
        DO_UNTANGLING: bool
        ENABLELIVEDRAG: bool
        ENABLE_COLLISION: bool
        FORCELIST: MXSWrapperBase
        FRICTION: float
        FROM_FLUID_RESPONSE_COEFFICIENT: float
        GRAVITY: float
        HARDWARE: bool
        HARD_STRETCH_LIMITATION: float
        HIERARCHICAL_LEVELS: int
        IGNOREBACKFACING: bool
        INHERIT_VELOCITY: bool
        IS_STATIC: bool
        KINEMATIC_UNTIL_FRAME: int
        MAP: int
        MAPCHANNEL: int
        MIN_ADHERE_VELOCITY: float
        PRESSURE: float
        SELF_COLLISION: bool
        SELF_THICKNESS: float
        SHOWTARGETSTATE: bool
        SHOWTENSION: bool
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELBUBBLE: float
        SOFTSELEDGEDIST: int
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELUSEEDGEDISTANCE: bool
        SOLVER_ITERATIONS: int
        STRETCHINESS: float
        TEARABLE: bool
        TEAR_FACTOR: float
        TENSIONSCALE: float
        TEXTURE: None
        THICKNESS: float
        TO_FLUID_RESPONSE_COEFFICIENT: float
        TWO_WAY_COLLISION: bool
        UNTILFRAMEENABLE: bool
        USESOFTSELECTION: bool
        USETEXTUREMAP: bool
        VALIDBOUNDS: bool
        VISUALIZATION: bool
        WELDMETHOD: int
        ...
    class MP_Buoyancy(Helper):
        ANGULAR_DRAG: float
        COLOR_COORDINATED: bool
        DENSITY: float
        GRID_GEOMETRY: None
        ICON_HEIGHT: float
        ICON_LENGTH: float
        ICON_SHAPE: int
        ICON_WIDTH: float
        LEVEL_HEIGHT: float
        LEVEL_TYPE: int
        LIMIT_BUOYANCY_BY_ICON: bool
        LINEAR_DRAG: float
        QUADRATIC_DRAG: float
        SURFACE_UNIT: float
        USE_ANGULAR_DRAG: bool
        USE_LINEAR_DRAG: bool
        USE_QUADRATIC_DRAG: bool
        ...
    class MP_Collision(Helper):
        ADDITIVE_COUNT: bool
        COLLISION_COUNT: int
        COLLISION_GROUP: int
        DEFLECTORS: MXSWrapperBase
        MAX_SPEED: float
        MIN_SPEED: float
        REPORT_TO_DATA_OPERATOR: bool
        TEST_TRUE: bool
        TEST_TYPE: int
        ...
    class MP_Drag(Helper):
        ANGULAR_DAMPING: float
        ANGULAR_DAMPING_DATA_CREATOR: None
        ANGULAR_DAMPING_FROM_DATA: bool
        APPLY_ANGULAR_DAMPING: bool
        APPLY_LINEAR_DAMPING: bool
        LINEAR_DAMPING: float
        LINEAR_DAMPING_DATA_CREATOR: None
        LINEAR_DAMPING_FROM_DATA: bool
        SPEED_MULTIPLIER: bool
        SPEED_UNIT: float
        SPIN_UNIT: float
        SYNC: int
        TIMING_TYPE: int
        USE_DATA_WIRING: bool
        ...
    class MP_Force(Helper):
        EXPONENT: int
        FORCE_OVERLAPPING: int
        FORCE_SPACE_WARPS: MXSWrapperBase
        FORCE_TYPE: int
        FORCE_VARIATION_THRESHOLD: bool
        IMPULSE_ON_EVENT_ENTRY: bool
        INFLUENCE: float
        SHAPE_SIZE: float
        SYNC: int
        TIME_WARP: int
        USE_SCRIPT_FLOAT: int
        ...
    class MP_Glue(Helper):
        ADJUST_BY_PARTICLE_MASS: bool
        ALIGN_MARGIN: float
        ALLOW_BINDING_PENETRATION: bool
        AVERAGE_BINDING_LENGTH_DATA_CREATOR: None
        AVERAGE_BINDING_LENGTH_TO_DATA: bool
        AVERAGE_BREAKING_IMPULSE_DATA_CREATOR: None
        AVERAGE_BREAKING_IMPULSE_TO_DATA: bool
        BINDING_GROUPS_DATA_CREATOR: None
        BINDING_GROUPS_FROM_DATA: bool
        BIND_CENTER_ALIGNED_ONLY: bool
        BIND_DISTANCE: float
        BIND_DISTANCE_DATA_CREATOR: None
        BIND_DISTANCE_FROM_DATA: bool
        BIND_GAP: float
        BIND_GAP_DATA_CREATOR: None
        BIND_GAP_FROM_DATA: bool
        BIND_IN_CURRENT_EVENT: bool
        BIND_WITH_DEFLECTORS: bool
        BIND_WITH_GROUND: bool
        BIND_WITH_OTHER_EVENTS: bool
        BREAKABILITY_MAX_FORCE_DATA_CREATOR: None
        BREAKABILITY_MAX_FORCE_FROM_DATA: bool
        BREAKABILITY_MAX_TORQUE_DATA_CREATOR: None
        BREAKABILITY_MAX_TORQUE_FROM_DATA: bool
        BREAKABLE_BY_FORCE: bool
        BREAKABLE_BY_OVERSTRETCH: bool
        BURY_BINDING_ANCHORS: bool
        COLOR: MXSWrapperBase
        CONTINUOUS_ADJUSTMENT: bool
        DAMPER_COEF: float
        DEFLECTORS_TO_BIND_WITH: MXSWrapperBase
        DEPTH: float
        DISTANCE_UNIT: float
        ENABLE_SPRING_FORCE: bool
        EVENTS_TO_BIND_WITH: MXSWrapperBase
        MAXIMUM_ABSOLUTE_DISTANCE: float
        MAXIMUM_BINDING_LENGTH_DATA_CREATOR: None
        MAXIMUM_BINDING_LENGTH_TO_DATA: bool
        MAXIMUM_BREAKING_IMPULSE_DATA_CREATOR: None
        MAXIMUM_BREAKING_IMPULSE_TO_DATA: bool
        MAXIMUM_DISTANCE_LIMIT_DATA_CREATOR: None
        MAXIMUM_DISTANCE_LIMIT_FROM_DATA: bool
        MAXIMUM_DISTANCE_TYPE: int
        MAXIMUM_RELATIVE_DISTANCE: float
        MAX_BINDS_PER_PARTICLE: int
        MAX_BINDS_PER_PARTICLE_DATA_CREATOR: None
        MAX_BINDS_PER_PARTICLE_FROM_DATA: bool
        MAX_BY_BIND_DISTANCE: bool
        MAX_FORCE: float
        MAX_TORQUE: float
        MINIMUM_ABSOLUTE_DISTANCE: float
        MINIMUM_BINDING_LENGTH_DATA_CREATOR: None
        MINIMUM_BINDING_LENGTH_TO_DATA: bool
        MINIMUM_DISTANCE_LIMIT_DATA_CREATOR: None
        MINIMUM_DISTANCE_LIMIT_FROM_DATA: bool
        MINIMUM_DISTANCE_TYPE: int
        MINIMUM_RELATIVE_DISTANCE: float
        NUM_ACTIVE_BINDINGS_DATA_CREATOR: None
        NUM_ACTIVE_BINDINGS_TO_DATA: bool
        NUM_BROKEN_BINDINGS_DATA_CREATOR: None
        NUM_BROKEN_BINDINGS_TO_DATA: bool
        NUM_BROKEN_BY_FORCE_DATA_CREATOR: None
        NUM_BROKEN_BY_FORCE_TO_DATA: bool
        OVERSTRETCH_ABSOLUTE_LIMIT: float
        OVERSTRETCH_DISTANCE_LIMIT_DATA_CREATOR: None
        OVERSTRETCH_DISTANCE_LIMIT_FROM_DATA: bool
        OVERSTRETCH_RELATIVE_LIMIT: float
        OVERSTRETCH_TYPE: int
        RIGID_BINDING_ANCHOR_TYPE: int
        SIMPLIFIED_BINDING_ANCHOR_TYPE: int
        SOLVER_FACTOR: float
        SPRING_COEF: float
        SPRING_DAMPER_COEF_DATA_CREATOR: None
        SPRING_DAMPER_COEF_FROM_DATA: bool
        SPRING_FORCE_COEF_DATA_CREATOR: None
        SPRING_FORCE_COEF_FROM_DATA: bool
        SYNC: int
        TEST_TRUE: bool
        TEST_TYPE: int
        TIMING_TYPE: int
        TYPE: int
        USE_BIND_GAP_CONDITION: bool
        USE_MAXIMUM_DISTANCE_LIMIT: bool
        USE_MINIMUM_DISTANCE_LIMIT: bool
        VISUALIZE_BINDING: bool
        ...
    class MP_InterCollision(Helper):
        ADDITIVE_COUNT: bool
        COLLISION_COUNT: int
        MAX_SPEED: float
        MIN_SPEED: float
        REPORT_TO_DATA_OPERATOR: bool
        SCOPE_TYPE: int
        SELECTED_EVENTS: MXSWrapperBase
        TEST_TYPE: int
        ...
    class MP_Shape(Helper):
        COLLIDE_TYPE: int
        COLLISION_GROUP: int
        COLOR: MXSWrapperBase
        CONFORM_TO_PARTICLE_SHAPE: bool
        DENSITY: float
        DISPLAY_TYPE: int
        DYNAMIC_FRICTION: float
        GENERATE_TOLERANCE_CHANNEL: bool
        INFLATE_WIDTH: float
        INTERPENETRATION_TOLERANCE: float
        MASS: float
        MASS_TYPE: int
        RESTITUTION: float
        SCALE: MXSWrapperBase
        SCALE_MARGIN: float
        SCALE_TYPE: int
        SHAPE_HEIGHT: float
        SHAPE_LENGTH: float
        SHAPE_WIDTH: float
        STATIC_FRICTION: float
        WELD_THRESHOLD: float
        ...
    class MP_Solvent(Helper):
        COLOR_COORDINATED: bool
        DATA_CHANNEL: None
        GLUE_TESTS: MXSWrapperBase
        ICON_SHAPE: int
        ICON_SIZE: float
        LIMIT_SOLVENT_BY_DATA: bool
        LIMIT_SOLVENT_BY_ICON: bool
        LIMIT_SOLVENT_BY_LIST: bool
        LIMIT_SOLVENT_BY_TIME: bool
        MODE: int
        PARTICLES_TO_DEFLECTORS: bool
        PARTICLES_TO_GROUND: bool
        PARTICLES_TO_PARTICLES: bool
        START: int
        STOP: int
        ...
    class MP_Switch(Helper):
        ANTIGRAVITY_ACTIVE: bool
        ANTIGRAVITY_START: int
        ANTIGRAVITY_STOP: int
        ANTIGRAVITY_TYPE: int
        ANTI_GRAVITY_SYNC_TYPE: int
        APPLY_ANTI_GRAVITY: bool
        MATCH_POSITION: bool
        MATCH_ROTATION: bool
        MATCH_SPEED: bool
        MATCH_SPIN: bool
        POSITION_SPEED_ACTIVE: bool
        POSITION_SPEED_MATCH_TYPE: int
        POSITION_SPEED_START: int
        POSITION_SPEED_STOP: int
        POSITION_SPEED_SYNC_TYPE: int
        ROTATION_SPIN_ACTIVE: bool
        ROTATION_SPIN_MATCH_TYPE: int
        ROTATION_SPIN_START: int
        ROTATION_SPIN_STOP: int
        ROTATION_SPIN_SYNC_TYPE: int
        SPEED_LIMIT: float
        SPIN_LIMIT: float
        TURN_OFF_ACTIVE: bool
        TURN_OFF_SIMULATION: bool
        TURN_OFF_SIMULATION_TYPE: int
        TURN_OFF_START: int
        TURN_OFF_STOP: int
        TURN_OFF_SYNC_TYPE: int
        USE_SPEED_LIMIT: bool
        USE_SPIN_LIMIT: bool
        ...
    class MP_World(Helper):
        PHYSX_DRIVER_TYPE: int
        PHYSX_WORLD_DRIVER: None
        SUPPRESS_EXPRESS_SAVE: bool
        ...
    class MP_Worldhelper(Helper):
        APPLY_GRAVITY: bool
        BOUNCE_THRESHOLD: float
        CALCULATION_LIMIT: int
        COLLISION_GROUP: int
        DEFAULT_DYNAMIC_FRICTION: float
        DEFAULT_RESTITUTION: float
        DEFAULT_STATIC_FRICTION: float
        ENABLE_MULTI_THREADING: bool
        ENERGY_THRESHOLD: float
        GRAVITY_ACCELERATION: float
        GROUND_COLLISION_PLANE: bool
        HIDE_ICON: bool
        HIDE_PARTICLE_BINDINGS: bool
        ICON_HEIGHT: float
        ICON_LENGTH: float
        ICON_WIDTH: float
        RANGE_FINISH: int
        RANGE_START: int
        RANGE_TYPE: int
        RESTRICTED_BROADPHASE: bool
        RUN_BAKED_SIMULATION: bool
        SAFE_MODE_SIMULATION: bool
        SET_WORLD_LIMITS: bool
        SHOW_BAKE_DIALOG: int
        SLEEP_THRESHOLD_TYPE: int
        SPEED_THRESHOLD: float
        SPIN_RATE_THRESHOLD: float
        SUBFRAME_FACTOR: int
        SUBFRAME_TYPE: int
        THREAD_COUNT: int
        TIME_SCALE: float
        UPDATE_VIEWPORTS: bool
        USE_HARDWARE_PPU: bool
        USE_TIME_SCALE: bool
        ...
    class MParticles_Flow(ReferenceTarget):
        ...
    class MacroRecorder(WindowStream):
        ...
    class MacroRecorderBackgroundColor(Color):
        ...
    class MacroRecorderTextColor(Color):
        ...
    class MakeCube(UserGeneric):
        ...
    class MakeDir(Primitive):
        ...
    class MakeIndependent(Primitive):
        ...
    class MakeUniqueArray(Primitive):
        ...
    class MakeValidName(Primitive):
        ...
    class Manip(Interface):
        ...
    class MapKeys(MappedGeneric):
        ...
    class MapPoint(Primitive):
        ...
    class MapScreenToCP(Primitive):
        ...
    class MapScreenToView(Primitive):
        ...
    class MapScreenToWorldRay(Primitive):
        ...
    class Mapping(Helper):
        CHANNEL_TYPE: int
        MAP_CHANNEL: int
        SHOW_IN_VIEWPORT: bool
        SYNC_TYPE: int
        U_MAP: float
        V_MAP: float
        W_MAP: float
        ...
    class MappinglayerData(AttributeDef):
        ...
    class MaskTex(TextureMap):
        MAP: None
        MAPENABLED: bool
        MASK: None
        MASKENABLED: bool
        MASKINVERTED: bool
        ...
    class Material(MAXWrapper):
        ...
    class MaterialID(NodeGeneric):
        ...
    class MaterialIDRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class Materialhelper(Helper):
        ...
    class MaxOps(Interface):
        ...
    class MaxVersion(Primitive):
        ...
    class Maz(Primitive):
        ...
    class MeasureOffset(Primitive):
        ...
    class Medit(Interface):
        ...
    class MeditMaterials(Material_Editor):
        ...
    class MemStreamMgr(Interface):
        ...
    class Mental_Ray__Area_Light_Custom_Attribute(CustAttrib):
        MR_ENABLELIGHTSHAPERENDERING: bool
        MR_NUMAREASAMPLES: int
        ...
    class MentalraySun(Light):
        ...
    class MenuMan(Interface):
        ...
    class Menuitem(Value):
        ...
    class Merge(Generic):
        ...
    class MergeMaxFile(Primitive):
        ...
    class Mesh(MAXMeshClass):
        ...
    class MeshGrid(GeometryClass):
        DENSITY: float
        LENGTH: float
        LENGTHSEGS: int
        MAPCOORDS: bool
        RENDERSCALE: float
        TYPEINCREATIONMETHOD: int
        TYPEINLENGTH: float
        TYPEINPOS: MXSWrapperBase
        TYPEINWIDTH: float
        WIDTH: float
        WIDTHSEGS: int
        ...
    class Mesh_Weld_Overlapping_Vertices(Primitive):
        ...
    class Meshsmooth(Modifier):
        AFFECTBACKFACING: bool
        BUBBLE: float
        CAGECOLOR: MXSWrapperBase
        CONTROLLEVEL: int
        DISPLAYCAGE: bool
        EDGEDIST: int
        FACETYPE: int
        FALLOFF: float
        IGNOREBACKFACING: bool
        IGNORESEL: bool
        ISOLINEDISPLAY: bool
        ITERATIONS: int
        KEEPCONVEX: bool
        LIMITSURFACE: bool
        OLDMAPPING: bool
        PINCH: float
        RELAX: float
        RENDERITERATIONS: int
        RENDERSMOOTHNESS: float
        RESET: int
        SELECTEDCAGECOLOR: MXSWrapperBase
        SEPBYMATS: bool
        SEPBYSMGROUPS: bool
        SMOOTHNESS: float
        SMOOTHRESULT: bool
        STRENGTH: float
        SUBDIVMETHOD: int
        UPDATE: int
        USEEDGEDIST: bool
        USERENDERITERATIONS: bool
        USERENDERSMOOTHNESS: bool
        USESOFTSEL: bool
        ...
    class MessageBox(Primitive):
        ...
    class MessageTextColor(Color):
        ...
    class Mirror(Modifier):
        COPY: bool
        MIRROR_AXIS: int
        OFFSET: float
        ...
    class MissingPathCache(Interface):
        ...
    class MixTexture(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        LOWER: float
        MAP1: None
        MAP1ENABLED: bool
        MAP2: None
        MAP2ENABLED: bool
        MASK: None
        MASKENABLED: bool
        MIXAMOUNT: float
        OUTPUT: MXSWrapperBase
        UPPER: float
        USECURVE: bool
        ...
    class Mixdown(BipedGeneric):
        ...
    class Mod(Generic):
        ...
    class Modifier(MAXWrapper):
        ...
    class MouseTrack(Primitive):
        ...
    class Move(NodeGeneric):
        ...
    class MoveClip(BipedGeneric):
        ...
    class MoveKey(Generic):
        ...
    class MoveKeys(MappedGeneric):
        ...
    class MrAreaLightCustAttrib(CustAttrib):
        MR_ENABLELIGHTSHAPERENDERING: bool
        MR_NUMAREASAMPLES: int
        ...
    class MrPBParameter(ReferenceTarget):
        ...
    class MrPBParameterClassDescCreator(Interface):
        ...
    class MrPhysSkyLight(Light):
        ...
    class Mr_Sky(Light):
        ...
    class Mr_Sun(Light):
        ...
    class MsZip(Interface):
        ...
    class MultiPassDOF(MPassCamEffect):
        DISABLEANTIALIASING: bool
        DISABLEFILTERING: bool
        DISPLAYPASSES: bool
        DITHERSTRENGTH: float
        FOCALDEPTH: float
        NORMALIZEWEIGHTS: bool
        SAMPLEBIAS: float
        SAMPLERADIUS: float
        TILESIZE: int
        TOTALPASSES: int
        USEORIGINALLOCATION: bool
        USETARGETDISTANCE: bool
        ...
    class MultiPassMotionBlur(MPassCamEffect):
        BIAS: float
        DISABLEANTIALIASING: bool
        DISABLEFILTERING: bool
        DISPLAYPASSES: bool
        DITHERSTRENGTH: float
        DURATION: float
        NORMALIZEWEIGHTS: bool
        TILESIZE: int
        TOTALPASSES: int
        ...
    class MultiSubMaterial(Material):
        MAPENABLED: MXSWrapperBase
        MATERIALIDLIST: MXSWrapperBase
        MATERIALLIST: MXSWrapperBase
        NAMES: MXSWrapperBase
        ...
    class MultiSubMaterial_Empty(Material):
        ...
    class Name(Value):
        ...
    class NearestPathParam(NodeGeneric):
        ...
    class Negative(VideoPostFilter):
        ...
    class Netrender(Interface):
        ...
    class NewRolloutFloater(Primitive):
        ...
    class NewScript(Primitive):
        ...
    class NewSnippet(BipedGeneric):
        ...
    class NewTrackViewNode(Primitive):
        ...
    class Node(MAXWrapper):
        ...
    class NodeGetBoundingBox(Primitive):
        ...
    class NodeLocalBoundingBox(Primitive):
        ...
    class NodeSelectionSet(Interface):
        ...
    class Noise3(Primitive):
        ...
    class Noise4(Primitive):
        ...
    class Normalize(Generic):
        ...
    class Normtime(Primitive):
        ...
    class NotifyDependents(Primitive):
        ...
    class NumCopies(BipedGeneric):
        ...
    class NumEaseCurves(Generic):
        ...
    class NumKeys(Generic):
        ...
    class NumKnots(NodeGeneric):
        ...
    class NumMultiplierCurves(Generic):
        ...
    class NumNoteTracks(Primitive):
        ...
    class NumPoints(Primitive):
        ...
    class NumSegments(NodeGeneric):
        ...
    class NumSelKeys(Generic):
        ...
    class NumSplines(NodeGeneric):
        ...
    class NvBox(GeometryClass):
        HEIGHT: float
        HEIGHTSEGS: int
        LENGTH: float
        LENGTHSEGS: int
        WIDTH: float
        WIDTHSEGS: int
        ...
    class NvCapsule(GeometryClass):
        HEIGHT: float
        HEIGHTTYPE: int
        RADIUS: float
        ...
    class NvConstraint(Helper):
        BODY0: None
        BODY1: None
        BREAKABLE: bool
        CHILDATTACHPOINT: MXSWrapperBase
        CHILDINITIALTWIST: float
        COLLISION: bool
        GEARING: bool
        GEARRATIO: float
        HELPERSIZE: float
        LINEARDAMPING: float
        LINEARMODEX: int
        LINEARMODEY: int
        LINEARMODEZ: int
        LINEARPOSITION: float
        LINEARRESTITUTION: float
        LINEARSPRING: float
        MAXFORCE: float
        MAXTORQUE: float
        POSDAMPING: float
        POSSPRING: float
        PROJECTIONANGLE: float
        PROJECTIONDIST: float
        PROJECTIONMODE: int
        SHOWVISUALIZER: bool
        SWING1ANGLE: float
        SWING1DAMPING: float
        SWING1MODE: int
        SWING1RESTITUTION: float
        SWING1SPRING: float
        SWING2ANGLE: float
        SWING2DAMPING: float
        SWING2MODE: int
        SWING2RESTITUTION: float
        SWING2SPRING: float
        SWINGDAMPING: float
        SWINGSPRING: float
        TWISTANGLEHIGH: float
        TWISTANGLELOW: float
        TWISTDAMPING: float
        TWISTDAMPINGHIGH: float
        TWISTDAMPINGLOW: float
        TWISTMODE: int
        TWISTRESTITUTIONHIGH: float
        TWISTRESTITUTIONLOW: float
        TWISTSPRING: float
        TWISTSPRINGHIGH: float
        TWISTSPRINGLOW: float
        USEACCELERATION: bool
        USEHARDLIMITS: bool
        USEPROJECTION: bool
        ...
    class NvRagdoll(Helper):
        BONEGROUPS: None
        HELPERSIZE: float
        INFLATION: float
        JOINTS: None
        MESHTYPE: int
        RAGDOLLNODE: None
        RBTYPE: int
        ROOTBONE: None
        WEIGHT: float
        ...
    class NvSphere(GeometryClass):
        RADIUS: float
        SEGS: int
        ...
    class Nvpx(Interface):
        ...
    class NvpxConsts(Interface):
        ...
    class ObjXRefMgr(Interface):
        ...
    class ObjXRefs(Interface):
        ...
    class Object(Value):
        ...
    class ObjectIDRenderElement(RenderElement):
        BITMAP: None
        COLORMODE: int
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class ObjectReferenceTarget(ReferenceTarget):
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        SEPARATE_CHILDREN: bool
        SEPARATE_GROUP_MEMBERS: bool
        STATIC_OBJECTS: bool
        SUBFRAME_PLACEMENT: bool
        TYPE: int
        USE_I3: bool
        USE_T2: bool
        USE_V4: bool
        ...
    class Objects(ObjectSet):
        ...
    class OcclusionMap(Primitive):
        ...
    class OffsetTimer(FloatController):
        ...
    class OkCancelBox(Primitive):
        ...
    class OkToCreate(Primitive):
        ...
    class Open(NodeGeneric):
        ...
    class OpenBitMap(Primitive):
        ...
    class OpenCTBitMap(Primitive):
        ...
    class OpenEdges(Interface):
        ...
    class OpenEncryptedFile(Primitive):
        ...
    class OpenUtility(Primitive):
        ...
    class Openfile(Primitive):
        ...
    class Openlog(Primitive):
        ...
    class Optimize(Modifier):
        AUTOEDGE: bool
        BIAS1: float
        BIAS2: float
        EDGETHRESHOLD1: float
        EDGETHRESHOLD2: float
        FACETHRESHOLD1: float
        FACETHRESHOLD2: float
        MANUALUPDATE: bool
        MAXEDGELENGTH1: float
        MAXEDGELENGTH2: float
        PRESERVEMAT1: bool
        PRESERVEMAT2: bool
        PRESERVESMOOTH1: bool
        PRESERVESMOOTH2: bool
        RENDERLOD: int
        VIEWLOD: int
        ...
    class OptimizeClipTransition(BipedGeneric):
        ...
    class OptimizeTransitions(BipedGeneric):
        ...
    class Orange(Color):
        ...
    class Osl_Blackbody(TextureMap):
        ...
    class Osl_CameraProjector(TextureMap):
        ...
    class Osl_Candy(TextureMap):
        ...
    class Osl_Checker(TextureMap):
        ...
    class Osl_ColorAdd(TextureMap):
        ...
    class Osl_ColorClamp(TextureMap):
        ...
    class Osl_ColorComp(TextureMap):
        ...
    class Osl_ColorCurveGrad(TextureMap):
        ...
    class Osl_ColorCurves(TextureMap):
        ...
    class Osl_ColorDiv(TextureMap):
        ...
    class Osl_ColorJuggler(TextureMap):
        ...
    class Osl_ColorKey(TextureMap):
        ...
    class Osl_ColorMax(TextureMap):
        ...
    class Osl_ColorMin(TextureMap):
        ...
    class Osl_ColorMul(TextureMap):
        ...
    class Osl_ColorScale(TextureMap):
        ...
    class Osl_ColorSpace(TextureMap):
        ...
    class Osl_ColorSub(TextureMap):
        ...
    class Osl_ColorTweak(TextureMap):
        ...
    class Osl_Compare(TextureMap):
        ...
    class Osl_Composite(TextureMap):
        ...
    class Osl_DegToRad(TextureMap):
        ...
    class Osl_Digits(TextureMap):
        ...
    class Osl_EnvironmentBackground(TextureMap):
        ...
    class Osl_Falloff(TextureMap):
        ...
    class Osl_Float1OfN(TextureMap):
        ...
    class Osl_Float1OfNtextureMap(TextureMap):
        ...
    class Osl_Float2Int(TextureMap):
        ...
    class Osl_FloatACos(TextureMap):
        ...
    class Osl_FloatASin(TextureMap):
        ...
    class Osl_FloatATan(TextureMap):
        ...
    class Osl_FloatAbs(TextureMap):
        ...
    class Osl_FloatAdd(TextureMap):
        ...
    class Osl_FloatAngle(TextureMap):
        ...
    class Osl_FloatClamp(TextureMap):
        ...
    class Osl_FloatComp(TextureMap):
        ...
    class Osl_FloatCos(TextureMap):
        ...
    class Osl_FloatCurves(TextureMap):
        ...
    class Osl_FloatDiv(TextureMap):
        ...
    class Osl_FloatExp(TextureMap):
        ...
    class Osl_FloatInterpolate(TextureMap):
        ...
    class Osl_FloatLog(TextureMap):
        ...
    class Osl_FloatLogX(TextureMap):
        ...
    class Osl_FloatMax(TextureMap):
        ...
    class Osl_FloatMin(TextureMap):
        ...
    class Osl_FloatMod(TextureMap):
        ...
    class Osl_FloatMul(TextureMap):
        ...
    class Osl_FloatNegate(TextureMap):
        ...
    class Osl_FloatPow(TextureMap):
        ...
    class Osl_FloatRange(TextureMap):
        ...
    class Osl_FloatRecip(TextureMap):
        ...
    class Osl_FloatSin(TextureMap):
        ...
    class Osl_FloatSmoothStep(TextureMap):
        ...
    class Osl_FloatSqrt(TextureMap):
        ...
    class Osl_FloatSub(TextureMap):
        ...
    class Osl_FloatTan(TextureMap):
        ...
    class Osl_FourPointGradient(TextureMap):
        ...
    class Osl_GaborNoise(TextureMap):
        ...
    class Osl_GetAttribute(TextureMap):
        ...
    class Osl_GetCoordSpace(TextureMap):
        ...
    class Osl_GetFrame(TextureMap):
        ...
    class Osl_GetMtlID(TextureMap):
        ...
    class Osl_GetNodeID(TextureMap):
        ...
    class Osl_GetNodeName(TextureMap):
        ...
    class Osl_GetObjSpace(TextureMap):
        ...
    class Osl_GetObjectID(TextureMap):
        ...
    class Osl_GetParticleAge(TextureMap):
        ...
    class Osl_GetTime(TextureMap):
        ...
    class Osl_GetUVW(TextureMap):
        ...
    class Osl_GetWireColor(TextureMap):
        ...
    class Osl_Gradient2(TextureMap):
        ...
    class Osl_GreaterThan(TextureMap):
        ...
    class Osl_HDRILights(TextureMap):
        ...
    class Osl_HDRIenv(TextureMap):
        ...
    class Osl_HalftoneDots(TextureMap):
        ...
    class Osl_IdxRndCol(TextureMap):
        ...
    class Osl_IdxRndFlt(TextureMap):
        ...
    class Osl_IdxRndVec(TextureMap):
        ...
    class Osl_Interpolate(TextureMap):
        ...
    class Osl_LiftGammaGain(TextureMap):
        ...
    class Osl_Mandelbrot(TextureMap):
        ...
    class Osl_MatCapUV(TextureMap):
        ...
    class Osl_MixColor(TextureMap):
        ...
    class Osl_MixVector(TextureMap):
        ...
    class Osl_MultiMixColor(TextureMap):
        ...
    class Osl_Noise(TextureMap):
        ...
    class Osl_Noise3D(TextureMap):
        ...
    class Osl_Normal(TextureMap):
        ...
    class Osl_OSLBitmap2(TextureMap):
        ...
    class Osl_ObjectProjector(TextureMap):
        ...
    class Osl_PBRMixer(TextureMap):
        ...
    class Osl_RadToDeg(TextureMap):
        ...
    class Osl_RandomBitmaps2(TextureMap):
        ...
    class Osl_RandomIndex(TextureMap):
        ...
    class Osl_RandomTilingBitmap(TextureMap):
        ...
    class Osl_Rivets(TextureMap):
        ...
    class Osl_SetColor(TextureMap):
        ...
    class Osl_SetFile(TextureMap):
        ...
    class Osl_SetFloat(TextureMap):
        ...
    class Osl_SetInt(TextureMap):
        ...
    class Osl_SetNumFile(TextureMap):
        ...
    class Osl_SetString(TextureMap):
        ...
    class Osl_SetVector(TextureMap):
        ...
    class Osl_SimpleTiles(TextureMap):
        ...
    class Osl_SmoothStepC(TextureMap):
        ...
    class Osl_SpecGlosToPhysical(TextureMap):
        ...
    class Osl_SphericalProjector(TextureMap):
        ...
    class Osl_Threads(TextureMap):
        ...
    class Osl_ToonWidth(TextureMap):
        ...
    class Osl_TriTone(TextureMap):
        ...
    class Osl_UVWEnviron(TextureMap):
        ...
    class Osl_UVWRowOffset(TextureMap):
        ...
    class Osl_UVWTransform(TextureMap):
        ...
    class Osl_UberBitmap2(TextureMap):
        ...
    class Osl_UberColorCorrect(TextureMap):
        ...
    class Osl_UberNoise(TextureMap):
        ...
    class Osl_VectorAdd(TextureMap):
        ...
    class Osl_VectorCross(TextureMap):
        ...
    class Osl_VectorDist(TextureMap):
        ...
    class Osl_VectorDiv(TextureMap):
        ...
    class Osl_VectorDot(TextureMap):
        ...
    class Osl_VectorInv(TextureMap):
        ...
    class Osl_VectorJuggler(TextureMap):
        ...
    class Osl_VectorLength(TextureMap):
        ...
    class Osl_VectorMax(TextureMap):
        ...
    class Osl_VectorMin(TextureMap):
        ...
    class Osl_VectorMul(TextureMap):
        ...
    class Osl_VectorNorm(TextureMap):
        ...
    class Osl_VectorScale(TextureMap):
        ...
    class Osl_VectorSub(TextureMap):
        ...
    class Osl_WaveLength(TextureMap):
        ...
    class Osl_Waveform(TextureMap):
        ...
    class Osl_Weave(TextureMap):
        ...
    class Osl_WireFrame(TextureMap):
        ...
    class Output(TextureMap):
        MAP1: None
        MAP1ENABLED: bool
        OUTPUT: MXSWrapperBase
        ...
    class OutputTextColor(Color):
        ...
    class ParamPublishMgr(Interface):
        ...
    class ParamTypeToTypeName(Primitive):
        ...
    class ParamWire(Interface):
        ...
    class Parameter(ReferenceTarget):
        ANGLE_OFFSET: float
        ANGLE_VALUE: float
        FILTER: None
        FLOAT_OFFSET: float
        FLOAT_VALUE: float
        INPUT_1: None
        INTEGER_FACTOR: int
        INTEGER_OFFSET: int
        INTEGER_VALUE: int
        MODIFIER_TYPE: int
        PERCENT_OFFSET: float
        PERCENT_VALUE: float
        RANDOM_SEED: int
        REAL_FACTOR: float
        SYNC_TYPE: int
        TIME_OFFSET: int
        TIME_VALUE: int
        TYPE: int
        USE_AS_MODIFIER: bool
        WORLD_UNIT_OFFSET: float
        WORLD_VALUE: float
        ...
    class ParticleAge(NodeGeneric):
        ...
    class ParticleBlur(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        SHARP: float
        ...
    class ParticleCenter(Primitive):
        ...
    class ParticleCount(NodeGeneric):
        ...
    class ParticleFlow(Interface):
        ...
    class ParticleFlowUtility(Interface):
        ...
    class ParticleLife(Primitive):
        ...
    class ParticleMesher(GeometryClass):
        BOUNDSMAX: MXSWrapperBase
        BOUNDSMIN: MXSWrapperBase
        PFEVENTLIST: MXSWrapperBase
        PICK: None
        RADIUS: float
        RENDERTIMEONLY: bool
        TIME: float
        USEALLPFEVENTS: bool
        USECUSTOMBOUNDS: bool
        ...
    class ParticlePos(NodeGeneric):
        ...
    class ParticleSize(NodeGeneric):
        ...
    class ParticleSize2(Primitive):
        ...
    class ParticleVelocity(NodeGeneric):
        ...
    class PasteBitmap(Primitive):
        ...
    class Path(PositionController):
        ALLOWUPSIDEDOWN: bool
        AXIS: int
        AXISFLIP: bool
        BANK: bool
        BANKAMOUNT: float
        CONSTANTVEL: bool
        FOLLOW: bool
        LOOP: bool
        PATH: None
        PERCENT: float
        RELATIVE: bool
        SMOOTHNESS: float
        WEIGHT: MXSWrapperBase
        ...
    class PathInterp(NodeGeneric):
        ...
    class PathIsNetworkPath(Primitive):
        ...
    class PathTangent(NodeGeneric):
        ...
    class PathToLengthParam(NodeGeneric):
        ...
    class PeekToken(Primitive):
        ...
    class PerlinMarble(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COORDS: MXSWrapperBase
        LEVEL: float
        MAP1: None
        MAP1ENABLED: bool
        MAP2: None
        MAP2ENABLED: bool
        SATURATION1: float
        SATURATION2: float
        SIZE: float
        ...
    class PerspectiveMatch(Generic):
        ...
    class PftParticleView(Interface):
        ...
    class PhysXpaneldata(PhysXPanel):
        ...
    class PickAnimatable(Primitive):
        ...
    class PickObject(Primitive):
        ...
    class PickOffsetDistance(Primitive):
        ...
    class PickPoint(Primitive):
        ...
    class Pivot(GeometryClass):
        BEVEL_ANGLE: float
        BOTTOM_RAIL: float
        CREATE_FRAME: bool
        DEPTH: float
        DOOR_OFFSET: float
        DOUBLE_DOORS: int
        FLIP_HINGE: bool
        FLIP_SWING: bool
        FRAME_DEPTH: float
        FRAME_WIDTH: float
        GENERATE_MAPPING_COORDS: bool
        GLASS_THICKNESS: float
        HEIGHT: float
        LEAF_THICKNESS: float
        MUNTIN: float
        NUMBER_OF_PANELS_HORIZONTALLY: int
        NUMBER_OF_PANELS_VERTICALLY: int
        OPEN__DEGREES: float
        PANEL_MIDDLE_THICKNESS: float
        PANEL_THICKNESS_1: float
        PANEL_THICKNESS_2: float
        PANEL_TYPE: int
        PANEL_WIDTH_1: float
        PANEL_WIDTH_2: float
        STILES_TOP_RAIL: float
        WIDTH: float
        ...
    class PlayAnimation(Primitive):
        ...
    class PluginManager(Interface):
        ...
    class Pngio(BitmapIO):
        ...
    class Point3(Value):
        ...
    class Point3Controller(MAXWrapper):
        ...
    class Point3_ListDummyEntry(Point3Controller):
        ...
    class Point3_List(Point3Controller):
        AVERAGE: bool
        WEIGHT: MXSWrapperBase
        ...
    class Point3_Script(Point3Controller):
        SCRIPT: str
        ...
    class Point4Controller(MAXWrapper):
        ...
    class Point4_ListDummyEntry(Point4Controller):
        ...
    class Point4_List(Point4Controller):
        AVERAGE: bool
        WEIGHT: MXSWrapperBase
        ...
    class Point4_Script(Point4Controller):
        SCRIPT: str
        ...
    class Pop(Interface):
        ...
    class PopSkinCharSelected(MAXScriptFunction):
        ...
    class PositionController(MAXWrapper):
        ...
    class Position_ListDummyEntry(PositionController):
        ...
    class Position_List(PositionController):
        AVERAGE: bool
        WEIGHT: MXSWrapperBase
        ...
    class Position_Script(PositionController):
        SCRIPT: str
        ...
    class Pow(Generic):
        ...
    class Print(MappedGeneric):
        ...
    class Printstack(NodeGeneric):
        ...
    class ProductAppID(Name):
        ...
    class ProgressBar(RolloutControl):
        ...
    class ProgressEnd(Primitive):
        ...
    class ProgressStart(Primitive):
        ...
    class ProgressUpdate(Primitive):
        ...
    class ProjectChangedRollout(RolloutClass):
        ...
    class Projected(GeometryClass):
        BOTTOM_HEIGHT: float
        DEPTH: float
        FRAME_THICKNESS: float
        GENERATE_MAPPING_COORDS: bool
        GLAZING_THICKNESS: float
        HEIGHT: float
        HORIZONTAL_FRAME_WIDTH: float
        MIDDLE_HEIGHT: float
        PERCENT_OPEN: int
        RAIL_WIDTH: float
        VERTICAL_FRAME_WIDTH: float
        WIDTH: float
        ...
    class Prs(Matrix3Controller):
        ...
    class PseudoColorExposureControl(ToneOperator):
        ACTIVE: bool
        AUTOMATIC: bool
        DISPLAY: int
        MAXIMUM: float
        MINIMUM: float
        PHYSICALSCALE: float
        PROCESSBG: bool
        QUANTITY: int
        SCALEFUNCTION: int
        UNITSYSTEMUSED: int
        ...
    class PxBake(MAXScriptFunction):
        ...
    class PxBakeAll(MAXScriptFunction):
        ...
    class PxBakeClothing(MAXScriptFunction):
        ...
    class PxBakeNodes(MAXScriptFunction):
        ...
    class PxBakeNodesUndoOn(MAXScriptFunction):
        ...
    class PxBakeSelection(MAXScriptFunction):
        ...
    class PxBakeSelectionUndoOn(MAXScriptFunction):
        ...
    class PxDebugVisualizerUndo(MAXScriptFunction):
        ...
    class PxGroupNodes(Array):
        ...
    class PxJoint(Helper):
        APTYPE: int
        BODY0: None
        BODY1: None
        BREAKABLE: bool
        COLLISION: bool
        GEARING: bool
        GEARRATIO: float
        HELPERSIZE: float
        MAXFORCE: float
        MAXTORQUE: float
        PROJECTIONANGLE: float
        PROJECTIONDIST: float
        PROJECTIONMODE: int
        SWING1_ANGLE: float
        SWING1_DAMP: float
        SWING1_LIMITED: bool
        SWING1_LOCKED: bool
        SWING1_REST: float
        SWING1_SPRING: float
        SWING2_ANGLE: float
        SWING2_DAMP: float
        SWING2_LIMITED: bool
        SWING2_LOCKED: bool
        SWING2_REST: float
        SWING2_SPRING: float
        TWISTHIGH: float
        TWISTLOW: float
        TWIST_DAMP: float
        TWIST_ENBL: bool
        TWIST_LMT: bool
        TWIST_REST: float
        TWIST_SPRING: float
        XLATE_RAD: float
        X_STATE: int
        Y_STATE: int
        Z_STATE: int
        ...
    class PxRemoveInstances(MAXScriptFunction):
        ...
    class PxRestoreBake(MAXScriptFunction):
        ...
    class PxSelectedConstraints(Array):
        ...
    class PxSelectedDummyHelpers(Array):
        ...
    class PxSelectedHelpers(Array):
        ...
    class PxSelectedNodes(Array):
        ...
    class PxSelectedRigidBodyMods(Array):
        ...
    class PxSelectedRigidBodyObjs(Array):
        ...
    class PxSelectedShapes(Array):
        ...
    class PxShapeHandles(Array):
        ...
    class PxSingleNodes(Array):
        ...
    class PxUnbake(MAXScriptFunction):
        ...
    class Px_UpdateSelectedRigidBodyLists(MAXScriptFunction):
        ...
    class Px_Add_Rigidbody(MAXScriptFunction):
        ...
    class Px_D6Panel_Advanced(RolloutClass):
        ...
    class Px_D6Panel_Connection(RolloutClass):
        ...
    class Px_D6Panel_Spring(RolloutClass):
        ...
    class Px_D6Panel_Swingtwist(RolloutClass):
        ...
    class Px_D6Panel_Translation(RolloutClass):
        ...
    class Px_Exporter_Clothing(RolloutClass):
        ...
    class Px_Exporter_Destruction(RolloutClass):
        ...
    class Px_Exporter_General(RolloutClass):
        ...
    class Px_Exporter_Options(RolloutClass):
        ...
    class Px_Exporter_Scene_Settings(RolloutClass):
        ...
    class Px_FilePostOpen(MAXScriptFunction):
        ...
    class Px_FilePreOpen(MAXScriptFunction):
        ...
    class Px_FilePreSave(MAXScriptFunction):
        ...
    class Px_Panel_AdvancedSettings(RolloutClass):
        ...
    class Px_Panel_DebugVisualizer(RolloutClass):
        ...
    class Px_Panel_DebugVisualizerApexClothing(RolloutClass):
        ...
    class Px_Panel_DebugVisualizerClothing(RolloutClass):
        ...
    class Px_Panel_Engine(RolloutClass):
        ...
    class Px_Panel_GlobalParameters(RolloutClass):
        ...
    class Px_Panel_Multiedit_Advanced(RolloutClass):
        ...
    class Px_Panel_Multiedit_BoxParams(RolloutClass):
        ...
    class Px_Panel_Multiedit_CapsuleParams(RolloutClass):
        ...
    class Px_Panel_Multiedit_CompositeParams(RolloutClass):
        ...
    class Px_Panel_Multiedit_Constraints_Advanced(RolloutClass):
        ...
    class Px_Panel_Multiedit_Constraints_General(RolloutClass):
        ...
    class Px_Panel_Multiedit_Constraints_Spring(RolloutClass):
        ...
    class Px_Panel_Multiedit_Constraints_SwingTwistLimits(RolloutClass):
        ...
    class Px_Panel_Multiedit_Constraints_TranslationLimits(RolloutClass):
        ...
    class Px_Panel_Multiedit_ConvexParams(RolloutClass):
        ...
    class Px_Panel_Multiedit_CustomParams(RolloutClass):
        ...
    class Px_Panel_Multiedit_Forces(RolloutClass):
        ...
    class Px_Panel_Multiedit_Material(RolloutClass):
        ...
    class Px_Panel_Multiedit_MaterialList(RolloutClass):
        ...
    class Px_Panel_Multiedit_Mesh(RolloutClass):
        ...
    class Px_Panel_Multiedit_OriginalParams(RolloutClass):
        ...
    class Px_Panel_Multiedit_Properties(RolloutClass):
        ...
    class Px_Panel_Multiedit_Selection(RolloutClass):
        ...
    class Px_Panel_Multiedit_SphereParams(RolloutClass):
        ...
    class Px_Panel_RigidBodyDisplay(RolloutClass):
        ...
    class Px_Panel_Simulation(RolloutClass):
        ...
    class Px_Panel_Tools_Destruction(RolloutClass):
        ...
    class Px_Panel_Tools_Simulation(RolloutClass):
        ...
    class Px_Panel_Tools_Utilities(RolloutClass):
        ...
    class Px_PhysXPanel(RolloutClass):
        ...
    class Px_SelectionChanged(MAXScriptFunction):
        ...
    class Px_SelectionChangedDirty(MAXScriptFunction):
        ...
    class Px_StopSimulationForEditing(MAXScriptFunction):
        ...
    class Px_SyncRagdollList(MAXScriptFunction):
        ...
    class Px_SystemPostNew(MAXScriptFunction):
        ...
    class Px_SystemPostReset(MAXScriptFunction):
        ...
    class Px_SystemPreNew(MAXScriptFunction):
        ...
    class Px_SystemPreReset(MAXScriptFunction):
        ...
    class Px_SystemPreShutdown(MAXScriptFunction):
        ...
    class Python(Interface):
        ...
    class PythonPromptColor(Color):
        ...
    class Qorthog(Generic):
        ...
    class Qsort(Primitive):
        ...
    class QuadMenuSettings(Interface):
        ...
    class QuadPatch(GeometryClass):
        LENGTH: float
        LENGTHSEGS: int
        MAPCOORDS: bool
        WIDTH: float
        WIDTHSEGS: int
        ...
    class QuatArrayToEulerArray(Primitive):
        ...
    class QuatToEuler(Primitive):
        ...
    class QuatToEuler2(Primitive):
        ...
    class QueryBox(Primitive):
        ...
    class QuitMax(Primitive):
        ...
    class RApplyIKChain(RolloutClass):
        ...
    class RCATRigMapping(RolloutClass):
        ...
    class RCaptureAnim(RolloutClass):
        ...
    class RCollapseLayers(RolloutClass):
        ...
    class RGizmos(RolloutClass):
        ...
    class RImportBIP(RolloutClass):
        ...
    class RImportBVH(RolloutClass):
        ...
    class RImportHTR(RolloutClass):
        ...
    class RLMR(RolloutClass):
        ...
    class RLoadFile(RolloutClass):
        ...
    class RMergeAnim(RolloutClass):
        ...
    class RObjectMapping(RolloutClass):
        ...
    class RPoseMixer(RolloutClass):
        ...
    class RSaveFile(RolloutClass):
        ...
    class RadToDeg(Primitive):
        ...
    class RadianceMap(ReferenceTarget):
        ...
    class RadiosityMeshOps(Interface):
        ...
    class RadiusManip(Helper):
        ...
    class Random(Generic):
        ...
    class RandomReferenceTarget(ReferenceTarget):
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        INPUT_7: None
        INTEGER_DISTRIBUTION_TYPE: int
        INTEGER_PARAMETER_1: int
        INTEGER_PARAMETER_2: int
        INTEGER_PARAMETER_3: int
        ITERATIONS: float
        OUTPUT_TYPE: int
        PARAMETER_1: float
        PARAMETER_2: float
        PARAMETER_3: float
        POSITIVE_PARAMETER_1: float
        POSITIVE_PARAMETER_2: float
        POSITIVE_PARAMETER_3: float
        RANDOM_SEED: int
        REAL_DISTRIBUTION_TYPE: int
        SYNC_TYPE: int
        USE_E3: bool
        USE_E4: bool
        USE_E5: bool
        USE_E6: bool
        USE_E7: bool
        VECTOR_DISTRIBUTION_TYPE: int
        ...
    class RaytraceShadow(Shadow):
        MAXDEPTH: int
        RAYTRACEBIAS: float
        TWOSIDEDSHADOWS: bool
        ...
    class ReactTo(Primitive):
        ...
    class ReactionMgr(Interface):
        ...
    class ReadChar(Generic):
        ...
    class ReadChars(Generic):
        ...
    class ReadDelimitedString(Generic):
        ...
    class ReadExpr(Generic):
        ...
    class ReadLine(Generic):
        ...
    class ReadToken(Primitive):
        ...
    class ReadValue(Generic):
        ...
    class Rectify(Generic):
        ...
    class Red(Color):
        ...
    class RedrawViews(Primitive):
        ...
    class RedrawViewsCallbacksEnabled(Primitive):
        ...
    class ReduceKeys(MappedGeneric):
        ...
    class Reference(NodeGeneric):
        ...
    class ReferenceReplace(NodeGeneric):
        ...
    class Refhierarchy(Interface):
        ...
    class Refine(NURBSGenericMethodsWrapper):
        ...
    class RefineSegment(NodeGeneric):
        ...
    class RefineU(NURBSGenericMethodsWrapper):
        ...
    class RefineV(NURBSGenericMethodsWrapper):
        ...
    class ReflectRefract(TextureMap):
        APPLY: bool
        BITMAPNAME: MXSWrapperBase
        BLUR: float
        BLUROFFSET: float
        FAR: float
        FRAMETYPE: int
        NEAR: float
        NTHFRAME: int
        OUTPUTNAME: None
        SIZE: int
        SOURCE: int
        USEATMOSPHERICMAP: bool
        ...
    class ReflectionRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class RefractionRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class RegisterDisplayFilterCallback(Primitive):
        ...
    class RegisterFileChangedFunction(Primitive):
        ...
    class RegisterOLEInterface(Primitive):
        ...
    class RegisterRedrawViewsCallback(Primitive):
        ...
    class RegisterRightClickMenu(Primitive):
        ...
    class RegisterSelectFilterCallback(Primitive):
        ...
    class RegisterTimeCallback(Primitive):
        ...
    class RegisterViewWindow(Primitive):
        ...
    class ReleaseAllOLEObjects(Primitive):
        ...
    class ReleaseOLEObject(Primitive):
        ...
    class RemoveDir(Primitive):
        ...
    class RemoveObject(NURBSGenericMethodsWrapper):
        ...
    class RemoveRollout(Primitive):
        ...
    class RenameFile(Primitive):
        ...
    class RendEnd(Time):
        ...
    class RendStart(Time):
        ...
    class Render(Primitive):
        ...
    class RenderEffect(MAXWrapper):
        ...
    class RenderMap(Generic):
        ...
    class RenderMessageManager(Interface):
        ...
    class RenderPresetMRUList(Array):
        ...
    class RenderPresets(Interface):
        ...
    class Renderer(Name):
        ...
    class Reparameterize(NURBSGenericMethodsWrapper):
        ...
    class Replace(Generic):
        ...
    class ReplaceInstances(Primitive):
        ...
    class Replace_CRLF_With_LF(Primitive):
        ...
    class Replace_LF_With_CRLF(Primitive):
        ...
    class Resample(Generic):
        ...
    class Reset(Generic):
        ...
    class ResetLattice(Primitive):
        ...
    class ResetLengthInterp(Primitive):
        ...
    class ResetMaxFile(Primitive):
        ...
    class ResetShape(NodeGeneric):
        ...
    class ResetZoom(Generic):
        ...
    class RetryCancelBox(Primitive):
        ...
    class RetryIgnoreAbortBox(Primitive):
        ...
    class Reverse(NodeGeneric):
        ...
    class ReverseTime(MappedGeneric):
        ...
    class Rgb(BitmapIO):
        ...
    class RgbMult(TextureMap):
        ALPHAFROM: int
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1: None
        MAP1ENABLED: bool
        MAP2: None
        MAP2ENABLED: bool
        ...
    class RgbTint(TextureMap):
        BLUE: MXSWrapperBase
        GREEN: MXSWrapperBase
        MAP1: None
        MAP1ENABLED: bool
        RED: MXSWrapperBase
        ...
    class RolloutFloater(Value):
        ...
    class Rollup(Interface):
        ...
    class RootNode(MAXRootNode):
        ...
    class RootScene(Scene):
        ...
    class Rotation(Helper):
        DIRECTION: int
        DIVERGENCE: float
        DIVERGENCE_AXIS_X: float
        DIVERGENCE_AXIS_Y: float
        DIVERGENCE_AXIS_Z: float
        EULER_X: float
        EULER_Y: float
        EULER_Z: float
        RANDOM_SEED: int
        RESTRICT_DIVERGENCE_TO_AXIS: bool
        ...
    class RotationController(MAXWrapper):
        ...
    class Rotation_ListDummyEntry(RotationController):
        ...
    class Rotation_List(RotationController):
        AVERAGE: bool
        WEIGHT: MXSWrapperBase
        ...
    class Rotation_Script(RotationController):
        SCRIPT: str
        ...
    class Save(Generic):
        ...
    class SaveCurrentPathConfigFile(MAXScriptFunction):
        ...
    class SaveMaterialLibrary(Primitive):
        ...
    class SaveMaxFile(Primitive):
        ...
    class SaveMixFile(BipedGeneric):
        ...
    class SaveMoFlowFile(BipedGeneric):
        ...
    class SaveNodes(Primitive):
        ...
    class SaveTempMaterialLibrary(Primitive):
        ...
    class Scale(NodeGeneric):
        ...
    class ScaleClip(BipedGeneric):
        ...
    class ScaleController(MAXWrapper):
        ...
    class ScaleTime(MappedGeneric):
        ...
    class Scale_ListDummyEntry(ScaleController):
        ...
    class Scale_List(ScaleController):
        AVERAGE: bool
        WEIGHT: MXSWrapperBase
        ...
    class Scale_Script(ScaleController):
        SCRIPT: str
        ...
    class ScaledLocalToGlobal(BipedGeneric):
        ...
    class ScaledLocalToLocal(BipedGeneric):
        ...
    class ScanForNewPlugins(Primitive):
        ...
    class SceneMaterials(MaterialLibrary):
        ...
    class SceneStateMgr(Interface):
        ...
    class Schematicviews(Interface):
        ...
    class Section(Shape):
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        LENGTH: float
        MAPCOORDS: bool
        QUAD_CAP: bool
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SPHERE_CAP: float
        THICKNESS: float
        TWIST_CORRECTION: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        WIDTH: float
        ...
    class Seed(Primitive):
        ...
    class Seek(Generic):
        ...
    class Select(NodeGeneric):
        ...
    class SelectBitMap(Primitive):
        ...
    class SelectByName(Primitive):
        ...
    class SelectCTBitMap(Primitive):
        ...
    class SelectFilterCallbacksEnabled(Primitive):
        ...
    class SelectKey(Generic):
        ...
    class SelectKeys(MappedGeneric):
        ...
    class SelectReaction(Primitive):
        ...
    class Selection(ObjectSet):
        ...
    class SelectionChangeFn(MAXScriptFunction):
        ...
    class SelectionSets(SelectionSetArray):
        ...
    class SelectionToBitmap(Primitive):
        ...
    class Selectmore(NodeGeneric):
        ...
    class Set(Value):
        ...
    class SetActive(Primitive):
        ...
    class SetAfterORT(MappedGeneric):
        ...
    class SetAppData(Generic):
        ...
    class SetArrowCursor(Primitive):
        ...
    class SetAsBackground(Generic):
        ...
    class SetAtmospheric(Primitive):
        ...
    class SetBeforeORT(MappedGeneric):
        ...
    class SetCV(NURBSGenericMethodsWrapper):
        ...
    class SetCacheEntry(Generic):
        ...
    class SetCurve(NURBSGenericMethodsWrapper):
        ...
    class SetCurveByID(NURBSGenericMethodsWrapper):
        ...
    class SetCurveStartPoint(NURBSGenericMethodsWrapper):
        ...
    class SetD3DMeshCacheSize(Primitive):
        ...
    class SetDimensions(Primitive):
        ...
    class SetDisplacementMapping(Generic):
        ...
    class SetEdge(NURBSGenericMethodsWrapper):
        ...
    class SetEdgeSelection(NodeGeneric):
        ...
    class SetEdgeVis(Generic):
        ...
    class SetEffect(Primitive):
        ...
    class SetFaceMatID(Generic):
        ...
    class SetFaceSelection(NodeGeneric):
        ...
    class SetFaceSmoothGroup(Generic):
        ...
    class SetFade(Generic):
        ...
    class SetFileAttribute(Primitive):
        ...
    class SetFilter(BipedGeneric):
        ...
    class SetFirstKnot(NodeGeneric):
        ...
    class SetFirstSpline(NodeGeneric):
        ...
    class SetFlip(NURBSGenericMethodsWrapper):
        ...
    class SetFlipTrim(NURBSGenericMethodsWrapper):
        ...
    class SetFocus(Primitive):
        ...
    class SetForegroundWindow(Primitive):
        ...
    class SetGenerateUVs(NURBSGenericMethodsWrapper):
        ...
    class SetGroupHead(Primitive):
        ...
    class SetGroupMember(Primitive):
        ...
    class SetGroupOpen(Primitive):
        ...
    class SetINISetting(Primitive):
        ...
    class SetInVec(NodeGeneric):
        ...
    class SetIndexedPixels(Generic):
        ...
    class SetIndexedProperty(Primitive):
        ...
    class SetInheritanceFlags(MappedPrimitive):
        ...
    class SetIniForceUTF16Default(Primitive):
        ...
    class SetKnot(NURBSGenericMethodsWrapper):
        ...
    class SetKnotPoint(NodeGeneric):
        ...
    class SetKnotSelection(Primitive):
        ...
    class SetKnotType(NodeGeneric):
        ...
    class SetListenerSel(Primitive):
        ...
    class SetListenerSelText(Primitive):
        ...
    class SetMAXFileAssetMetadata(Primitive):
        ...
    class SetMKTime(Primitive):
        ...
    class SetMKWeight(Primitive):
        ...
    class SetMTLMEditFlags(Primitive):
        ...
    class SetMTLMeditObjType(Primitive):
        ...
    class SetMTLMeditTiling(Primitive):
        ...
    class SetMaterialID(Primitive):
        ...
    class SetMeditMaterial(Primitive):
        ...
    class SetMesh(Generic):
        ...
    class SetModContextBBox(Primitive):
        ...
    class SetModContextTM(Primitive):
        ...
    class SetMorphTarget(Primitive):
        ...
    class SetMorphTargetName(Primitive):
        ...
    class SetNeedsRedraw(Primitive):
        ...
    class SetNumCPVVerts(Generic):
        ...
    class SetNumFaces(Generic):
        ...
    class SetNumTVerts(Generic):
        ...
    class SetNumVerts(Generic):
        ...
    class SetNumberThreads(Primitive):
        ...
    class SetObject(NURBSGenericMethodsWrapper):
        ...
    class SetOpenSceneScript(Primitive):
        ...
    class SetOutVec(NodeGeneric):
        ...
    class SetParent(NURBSGenericMethodsWrapper):
        ...
    class SetParentID(NURBSGenericMethodsWrapper):
        ...
    class SetPixels(Generic):
        ...
    class SetPoint(NURBSGenericMethodsWrapper):
        ...
    class SetProdTess(NURBSGenericMethodsWrapper):
        ...
    class SetProgressCancel(Primitive):
        ...
    class SetProperty(Primitive):
        ...
    class SetPropertyController(Primitive):
        ...
    class SetRadius(NURBSGenericMethodsWrapper):
        ...
    class SetReactionFalloff(Primitive):
        ...
    class SetReactionInfluence(Primitive):
        ...
    class SetReactionName(Primitive):
        ...
    class SetReactionState(Primitive):
        ...
    class SetReactionStrength(Primitive):
        ...
    class SetReactionValue(Primitive):
        ...
    class SetRenderApproximation(Primitive):
        ...
    class SetSaveRequired(Primitive):
        ...
    class SetSaveSceneScript(Primitive):
        ...
    class SetSeed(NURBSGenericMethodsWrapper):
        ...
    class SetSegSelection(Primitive):
        ...
    class SetSegmentType(NodeGeneric):
        ...
    class SetSelectedPts(CurveCtlGeneric):
        ...
    class SetSelectionLevel(Primitive):
        ...
    class SetSize(Generic):
        ...
    class SetSplineSelection(Primitive):
        ...
    class SetSplitMesh(Generic):
        ...
    class SetStruct(Generic):
        ...
    class SetSubMtl(Primitive):
        ...
    class SetSubTexmap(Primitive):
        ...
    class SetSubdivisionDisplacement(Generic):
        ...
    class SetSurfaceDisplay(Primitive):
        ...
    class SetTVFace(Generic):
        ...
    class SetTextureSurface(NURBSGenericMethodsWrapper):
        ...
    class SetTextureUVs(NURBSGenericMethodsWrapper):
        ...
    class SetTiling(NURBSGenericMethodsWrapper):
        ...
    class SetTilingOffset(NURBSGenericMethodsWrapper):
        ...
    class SetTimeRange(MappedGeneric):
        ...
    class SetTransformLockFlags(MappedPrimitive):
        ...
    class SetTrimSurface(NURBSGenericMethodsWrapper):
        ...
    class SetUCurve(NURBSGenericMethodsWrapper):
        ...
    class SetUCurveByID(NURBSGenericMethodsWrapper):
        ...
    class SetUKnot(NURBSGenericMethodsWrapper):
        ...
    class SetUseOldD3DCache(Primitive):
        ...
    class SetUserProp(NodeGeneric):
        ...
    class SetUserPropBuffer(NodeGeneric):
        ...
    class SetUserPropVal(Primitive):
        ...
    class SetVCFace(Generic):
        ...
    class SetVCurve(NURBSGenericMethodsWrapper):
        ...
    class SetVCurveByID(NURBSGenericMethodsWrapper):
        ...
    class SetVKnot(NURBSGenericMethodsWrapper):
        ...
    class SetVert(Generic):
        ...
    class SetVertColor(Generic):
        ...
    class SetVertSelection(NodeGeneric):
        ...
    class SetVertexPaintAmounts(Primitive):
        ...
    class SetVertexPaintColors(Primitive):
        ...
    class SetViewApproximation(Primitive):
        ...
    class SetViewTess(NURBSGenericMethodsWrapper):
        ...
    class SetWaitCursor(Primitive):
        ...
    class SetclipboardBitmap(Primitive):
        ...
    class SetclipboardText(Primitive):
        ...
    class Setface(Generic):
        ...
    class Setfacenormal(Generic):
        ...
    class Setnormal(Generic):
        ...
    class Settvert(Generic):
        ...
    class SetupEvents(Primitive):
        ...
    class Sgi(BitmapIO):
        ...
    class ShadowMap(Shadow):
        ABSOLUTEMAPBIAS: bool
        MAPBIAS: float
        MAPSIZE: int
        SAMPLERANGE: float
        TWOSIDEDSHADOWS: bool
        ...
    class Shape(Node):
        ...
    class Shapes(ObjectSet):
        ...
    class Show(MAXScriptFunction):
        ...
    class ShowClass(Primitive):
        ...
    class ShowEvents(Generic):
        ...
    class ShowHWTextureMap(Primitive):
        ...
    class ShowInterface(Generic):
        ...
    class ShowInterfaces(Generic):
        ...
    class ShowMethods(Generic):
        ...
    class ShowNodeEventCallbacks(Primitive):
        ...
    class ShowProjectSwitchDialog(MAXScriptFunction):
        ...
    class ShowProperties(Generic):
        ...
    class ShowSource(Primitive):
        ...
    class ShowTextureMap(Primitive):
        ...
    class ShowTrack(Generic):
        ...
    class ShowregisteredDisplayFilterCallbacks(Primitive):
        ...
    class ShowregisteredRedrawViewsCallbacks(Primitive):
        ...
    class ShowregisteredSelectFilterCallbacks(Primitive):
        ...
    class ShowregisteredTimeCallbacks(Primitive):
        ...
    class SilentValue(NoValueClass):
        ...
    class SimpleFaceManager(Interface):
        ...
    class Sin(Generic):
        ...
    class Sinh(Generic):
        ...
    class SketchUp(ImporterPlugin):
        ...
    class SkipSpace(Primitive):
        ...
    class SkipToNextLine(Generic):
        ...
    class SkipToString(Generic):
        ...
    class Sleep(Primitive):
        ...
    class SliderManipulator(Helper):
        HIDE: bool
        MAXVAL: float
        MINVAL: float
        SLDNAME: str
        SNAPTOGGLE: bool
        SNAPVAL: float
        VALUE: float
        WIDTH: float
        XPOS: float
        YPOS: float
        ...
    class SliderTime(Time):
        ...
    class Smooth(Modifier):
        AUTOSMOOTH: bool
        PREVENTINDIRECT: bool
        SMOOTHINGBITS: int
        THRESHOLD: float
        ...
    class SmoothReferenceTarget(ReferenceTarget):
        FILTER: bool
        FILTERDELEGATES: bool
        FROM: int
        FUTUREKEYS: int
        N: int
        OBJECTS: MXSWrapperBase
        PASTKEYS: int
        POSITIONS: bool
        REDUCE: bool
        ROTATIONS: bool
        SMOOTHNESS: int
        TO: int
        WHOLEANIM: int
        ...
    class Snapshot(NodeGeneric):
        ...
    class SnapshotAsMesh(Primitive):
        ...
    class Sort(Generic):
        ...
    class SortKeys(MappedGeneric):
        ...
    class SortNoteKeys(Generic):
        ...
    class Spacewarps(ObjectSet):
        ...
    class SpecularMap(BakeElement):
        AUTOSZON: bool
        BACKGROUNDCOLOR: MXSWrapperBase
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        FILTERON: bool
        LIGHTINGON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        SHADOWSON: bool
        TARGETMAPSLOTNAME: str
        ...
    class SpecularRenderElement(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        ...
    class Speed(Helper):
        DIRECTION: int
        DIVERGENCE: float
        RANDOM_SEED: int
        REVERSE: bool
        SPEED: float
        VARIATION: float
        ...
    class Spin(Helper):
        DIRECTION: int
        DIVERGENCE: float
        RANDOM_SEED: int
        SPINRATE: float
        SPIN_X_AXIS: float
        SPIN_Y_AXIS: float
        SPIN_Z_AXIS: float
        VARIATION: float
        ...
    class Sqrt(Generic):
        ...
    class Squadrev(Primitive):
        ...
    class Srr_Exports(Interface):
        ...
    class Stack(Primitive):
        ...
    class Standard(Material):
        ADTEXTURELOCK: bool
        APPLYREFLECTIONDIMMING: bool
        DIMLEVEL: float
        FACEMAP: bool
        FACETED: bool
        FILTERCOLOR: MXSWrapperBase
        FILTERMAP: None
        IOR: float
        MAPAMOUNTS: MXSWrapperBase
        MAPENABLES: MXSWrapperBase
        MAPS: MXSWrapperBase
        OPACITY: float
        OPACITYFALLOFF: float
        OPACITYFALLOFFTYPE: int
        OPACITYTYPE: int
        REFLECTIONLEVEL: float
        SAMPLER: int
        SAMPLERADAPTON: bool
        SAMPLERADAPTTHRESHOLD: float
        SAMPLERADVANCEDOPTIONS: bool
        SAMPLERBYNAME: str
        SAMPLERENABLE: bool
        SAMPLERQUALITY: float
        SAMPLERUSEGLOBAL: bool
        SHADERBYNAME: str
        SHADERTYPE: int
        SUBSAMPLETEXTUREON: bool
        TWOSIDED: bool
        USERPARAM0: float
        USERPARAM1: float
        WIRE: bool
        WIRESIZE: float
        WIREUNITS: int
        ...
    class StartObjectCreation(Primitive):
        ...
    class StartTool(Primitive):
        ...
    class StatusPanel(Interface):
        ...
    class Stop(Helper):
        POSITION: MXSWrapperBase
        ROTATION: MXSWrapperBase
        ...
    class StopAnimation(Primitive):
        ...
    class StopTool(Primitive):
        ...
    class StrRagdollHelperMesh(StringStream):
        ...
    class Stricmp(Primitive):
        ...
    class String(Value):
        ...
    class StyleMgr(Interface):
        ...
    class SubAnim(Value):
        ...
    class SubRollout(RolloutControl):
        ...
    class SubSurfaceMap(Primitive):
        ...
    class Subdivide(Modifier):
        ADAPTIVEEDGELENGTH: float
        ADAPTIVEREGULARITY: float
        ADAPTIVETHRESHOLD: float
        DELAUNAYRELAXATIONCOEFF: float
        DELAUNAYRELAXATIONITERATIONS: int
        DELAUNAYSIZE: float
        MANUALUPDATE: int
        PRESERVEDMAPINDEX: int
        PRESERVEDSHARPEDGEANGLE: float
        PRESERVEMESHDATA: bool
        PRESERVESHARPEDGESBYANGLE: bool
        REMESHTYPE: int
        SHOWALLTRIANGLES: bool
        SIZE: float
        SUBDIVIDEDIAGONALRATIO: float
        SUBDIVIDEDOENFORCEQUALITY: bool
        SUBDIVIDEDOFORMQUADS: bool
        SUBDIVIDEDOSUBDIVIDETRIANGLES: bool
        SUBDIVIDEMAXSTEINERPOINTS: int
        SUBDIVIDENUMBUCKETS: int
        SUBDIVIDEQUADAREARATIO: float
        SUBDIVIDEREFINEMENTTYPE: int
        VARIABLECURVATUREEDGELENGTH: float
        VARIABLECURVATUREITERATIONS: int
        VARIABLECURVATUREREGULARITY: float
        VARIABLECURVATURETHRESHOLD: float
        VARIABLECURVATURETRANSITION: float
        VARIABLECURVATUREVARIABLEDENSITY: float
        ...
    class SubdivideSegment(Primitive):
        ...
    class SubdivideSpacewarpModifier(SpacewarpModifier):
        ADAPTIVEEDGELENGTH: float
        ADAPTIVEREGULARITY: float
        ADAPTIVETHRESHOLD: float
        DELAUNAYRELAXATIONCOEFF: float
        DELAUNAYRELAXATIONITERATIONS: int
        DELAUNAYSIZE: float
        MANUALUPDATE: int
        PRESERVEDMAPINDEX: int
        PRESERVEDSHARPEDGEANGLE: float
        PRESERVEMESHDATA: bool
        PRESERVESHARPEDGESBYANGLE: bool
        REMESHTYPE: int
        SHOWALLTRIANGLES: bool
        SIZE: float
        SUBDIVIDEDIAGONALRATIO: float
        SUBDIVIDEDOENFORCEQUALITY: bool
        SUBDIVIDEDOFORMQUADS: bool
        SUBDIVIDEDOSUBDIVIDETRIANGLES: bool
        SUBDIVIDEMAXSTEINERPOINTS: int
        SUBDIVIDENUMBUCKETS: int
        SUBDIVIDEQUADAREARATIO: float
        SUBDIVIDEREFINEMENTTYPE: int
        VARIABLECURVATUREEDGELENGTH: float
        VARIABLECURVATUREITERATIONS: int
        VARIABLECURVATUREREGULARITY: float
        VARIABLECURVATURETHRESHOLD: float
        VARIABLECURVATURETRANSITION: float
        VARIABLECURVATUREVARIABLEDENSITY: float
        ...
    class SubstituteString(Primitive):
        ...
    class Substring(Generic):
        ...
    class SuperClassOf(Generic):
        ...
    class Superclasses(Array):
        ...
    class SupportsTimeOperations(Generic):
        ...
    class Surface(Modifier):
        STEPS: int
        THRESHOLD: float
        ...
    class Swap(Primitive):
        ...
    class Sweep(Modifier):
        ANGLE: float
        ASSIGNCSTYPE: int
        BANKING: bool
        CURRENTBUILTINSHAPE: int
        CUSTOMSHAPE: int
        CUSTOMSHAPENAME: None
        GENERATEMAPPINGCOORDS: bool
        GENMATIDS: bool
        MIRRORXYPLANE: bool
        MIRRORXZPLANE: bool
        PIVOTALIGNMENT: int
        REALWORLDMAPSIZE: bool
        SHAPES: MXSWrapperBase
        SMOOTHPATH: bool
        SMOOTHSECTION: bool
        UNIONINTERSECTIONS: bool
        USEPATHIDS: bool
        USESECTIONIDS: bool
        XOFFSET: float
        YOFFSET: float
        ...
    class Swirl(TextureMap):
        BASE: MXSWrapperBase
        BASEMAP: None
        BASEMAPENABLED: bool
        CENTER_POSITION_X: float
        CENTER_POSITION_Y: float
        COLOR_CONTRAST: float
        CONSTANT_DETAIL: int
        COORDS: MXSWrapperBase
        LOCK_BACKGROUND: int
        RANDOM_SEED: float
        SWIRL: MXSWrapperBase
        SWIRLMAP: None
        SWIRLMAPENABLED: bool
        SWIRL_AMOUNT: float
        SWIRL_INTENSITY: float
        TWIST: float
        ...
    class Symmetry(Modifier):
        AXIS: int
        FLIP: bool
        SLICE: int
        THRESHOLD: float
        WELD: int
        ...
    class Systems(ObjectSet):
        ...
    class Tan(Generic):
        ...
    class TangentBezier3D(Primitive):
        ...
    class TangentCurve3D(Primitive):
        ...
    class Tanh(Generic):
        ...
    class TargetSpot(Light):
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        ASPECT: float
        ATMOSCOLORAMT: float
        ATMOSOPACITY: float
        ATMOSSHADOWS: bool
        ATTENDECAY: int
        CASTSHADOWS: bool
        COLOR: MXSWrapperBase
        CONESHAPE: int
        CONTRAST: float
        DECAYRADIUS: float
        ENABLED: bool
        EXCLUDELIST: MXSWrapperBase
        FALLOFF: float
        FARATTENEND: float
        FARATTENSTART: float
        HOTSPOT: float
        HSV: MXSWrapperBase
        HUE: int
        INCLEXCLTYPE: int
        INCLUDELIST: None
        LIGHTAFFECTSSHADOW: bool
        LIGHTSHAPE: int
        MULTIPLIER: float
        NEARATTENEND: float
        NEARATTENSTART: float
        ON: bool
        OVERSHOOT: bool
        PROJECTOR: bool
        PROJECTORMAP: None
        RAYTRACEDSHADOWS: bool
        RGB: MXSWrapperBase
        SATURATION: int
        SHADOWCOLOR: MXSWrapperBase
        SHADOWGENERATOR: MXSWrapperBase
        SHADOWMULTIPLIER: float
        SHADOWPROJECTORMAP: None
        SHOWCONE: bool
        SHOWFARATTEN: bool
        SHOWNEARATTEN: bool
        SOFTENDIFFUSEEDGE: float
        TYPE: MXSWrapperBase
        USEFARATTEN: bool
        USEGLOBALSHADOWSETTINGS: bool
        USENEARATTEN: bool
        USESHADOWPROJECTORMAP: bool
        VALUE: int
        ...
    class Tcb_Float(FloatController):
        ...
    class Tcb_Point3(Point3Controller):
        ...
    class Tcb_Point4(Point4Controller):
        ...
    class Tcb_Position(PositionController):
        ...
    class Tcb_Rotation(RotationController):
        ...
    class Tcb_Scale(ScaleController):
        ...
    class Tessellate(Modifier):
        FACETYPE: int
        ITERATIONS: int
        TENSION: float
        TYPE: int
        UPDATEWHEN: int
        ...
    class Test_Safearray(Primitive):
        ...
    class Text(Shape):
        ADAPTIVE: bool
        ALIGNMENT: int
        ANGLE: float
        CAP: bool
        CAP_SEGMENTS: int
        DISPLAYRENDERMESH: bool
        DISPLAYRENDERSETTINGS: bool
        FONT: str
        ITALIC: bool
        KERNING: float
        LEADING: float
        MAPCOORDS: bool
        OPTIMIZE: bool
        QUAD_CAP: bool
        REALWORLDMAPSIZE: bool
        RENDERABLE: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        RENDER_MAPCOORDS: bool
        RENDER_RECTANGULAR: bool
        RENDER_RENDERABLE: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_VIEWPORT_ANGLE: float
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_WIDTH: float
        SIDES: int
        SIZE: float
        SPHERE_CAP: float
        STEPS: int
        TEXT: str
        THICKNESS: float
        TWIST_CORRECTION: bool
        UNDERLINE: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORT_ANGLE: float
        VIEWPORT_SIDES: int
        VIEWPORT_THICKNESS: float
        ...
    class TextureMap(Material):
        ...
    class TextureWrap(Primitive):
        ...
    class Tgaio(BitmapIO):
        ...
    class ThawSelection(Primitive):
        ...
    class ThePainterInterface(ReferenceTarget):
        ADDITIVEMODE: bool
        BUILDVNORMALS: bool
        DRAWNORMAL: bool
        DRAWRING: bool
        DRAWTRACE: bool
        FALLOFFGRAPH: MXSWrapperBase
        LAGRATE: int
        MARKER: float
        MARKERENABLE: bool
        MAXSIZE: float
        MAXSTR: float
        MINSIZE: float
        MINSTR: float
        MIRRORAXIS: int
        MIRRORENABLE: bool
        MIRRORGIZMOSIZE: float
        MIRROROFFSET: float
        NODES: MXSWrapperBase
        NORMALSCALE: float
        OFFMESHHITPOS: MXSWrapperBase
        OFFMESHHITTYPE: bool
        OFFMESHHITZDEPTH: float
        POINTGATHERENABLE: bool
        PREDEFINEDSIZEENABLE: bool
        PREDEFINEDSIZEGRAPH: MXSWrapperBase
        PREDEFINEDSTRENABLE: bool
        PREDEFINEDSTRGRAPH: MXSWrapperBase
        PRESSUREAFFECTS: int
        PRESSUREENABLE: bool
        QUADDEPTH: int
        SPLINECONSTRAINTNODE: None
        STRDRAGLIMITMAX: float
        STRDRAGLIMITMIN: float
        UPDATEONMOUSEUP: bool
        ...
    class ThinWallRefraction(TextureMap):
        APPLYBLUR: bool
        BLUR: float
        BUMPMAPEFFECT: float
        FRAME: int
        NTHFRAME: int
        THICKNESSOFFSET: float
        USEENVIROMENT: bool
        ...
    class Threads(Primitive):
        ...
    class Tifio(BitmapIO):
        ...
    class Tiles(TextureMap):
        BRICKS: None
        BRICKS_MAP: None
        BRICK_COLOR: MXSWrapperBase
        CHANGE_COLUMN: float
        CHANGE_ROW: float
        COLOR_VARIANCE: float
        EDGE_ROUGHNESS: float
        FADE_VARIANCE: float
        HOLES: int
        HORIZONTAL_COUNT: float
        HORIZONTAL_GAP: float
        LINE_SHIFT: float
        LOCK_GAP_SYMMETRY: int
        MORTAR: None
        MORTAR_COLOR: MXSWrapperBase
        MORTAR_MAP: None
        PER_COLUMN: int
        PER_ROW: int
        RANDOM_SEED: int
        RANDOM_SHIFT: float
        SHOW_TEXTURE_SWATCHES: int
        TILE_TYPE: int
        USE_COLUMN_EDIT: int
        USE_ROW_EDIT: int
        VERTICAL_COUNT: float
        VERTICAL_GAP: float
        ...
    class Time(Value):
        ...
    class TimeCallbacksEnabled(Primitive):
        ...
    class TimeDisplayMode(Name):
        ...
    class TimeGetTime(Primitive):
        ...
    class TimeSlider(Interface):
        ...
    class TimeStamp(Primitive):
        ...
    class TmGizmos(Interface):
        ...
    class ToLower(Generic):
        ...
    class ToUpper(Generic):
        ...
    class TopBottomMat(Material):
        BLEND: float
        BOTTOMMATERIAL: MXSWrapperBase
        COORDINATES: int
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        POSITION: float
        TOPMATERIAL: MXSWrapperBase
        ...
    class Tprofiler(GlobalUtilityPlugin):
        ...
    class TrackSelectionSets(Interface):
        ...
    class TrackViewNodes(MAXTVNode):
        ...
    class TrackViewUtility(MAXWrapperNonRefTarg):
        ...
    class Trackviews(Interface):
        ...
    class Transform(Primitive):
        ...
    class Transform_Script(Matrix3Controller):
        SCRIPT: str
        ...
    class Transpose(Generic):
        ...
    class TriPatch(GeometryClass):
        LENGTH: float
        MAPCOORDS: bool
        WIDTH: float
        ...
    class TriggerNodeEventCallback(Primitive):
        ...
    class TrimExtend(Primitive):
        ...
    class TrimLeft(Primitive):
        ...
    class TrimRight(Primitive):
        ...
    class Turbulence(Primitive):
        ...
    class Tverts(Interface):
        ...
    class TypeNameToParamType(Primitive):
        ...
    class UnDisplay(Generic):
        ...
    class UnRegisterViewWindow(Primitive):
        ...
    class UnbindKnot(NodeGeneric):
        ...
    class Unfreeze(NodeGeneric):
        ...
    class Ungroup(Primitive):
        ...
    class Unhide(NodeGeneric):
        ...
    class UnhideSegments(NodeGeneric):
        ...
    class UniqueName(Primitive):
        ...
    class Unmaz(Primitive):
        ...
    class UnregisterAllRightClickMenus(Primitive):
        ...
    class UnregisterDisplayFilterCallback(Primitive):
        ...
    class UnregisterRedrawViewsCallback(Primitive):
        ...
    class UnregisterRightClickMenu(Primitive):
        ...
    class UnregisterSelectFilterCallback(Primitive):
        ...
    class UnregisterTimeCallback(Primitive):
        ...
    class UnwrapUIdialog(RolloutClass):
        ...
    class Update(Generic):
        ...
    class UpdateBindList(NodeGeneric):
        ...
    class UpdateMTLInMedit(Primitive):
        ...
    class UpdateRolloutLayout(Primitive):
        ...
    class UpdateShape(NodeGeneric):
        ...
    class UpdateSurfaceMapper(Primitive):
        ...
    class UpdateToolbarButtons(Primitive):
        ...
    class UpdateWindow(Primitive):
        ...
    class UpdateXRef(Generic):
        ...
    class UsedMaps(Primitive):
        ...
    class Uvchecker_Mtl(Standardmaterial):
        ...
    class UvwMappingHeightManip(Helper):
        ...
    class UvwMappingLengthManip(Helper):
        ...
    class UvwMappingPositionManip(Helper):
        ...
    class UvwMappingWidthManip(Helper):
        ...
    class ValidModifier(Primitive):
        ...
    class ValidateId(Primitive):
        ...
    class ValidateValueLinkages(Primitive):
        ...
    class Value():
        ...
    class Velocity(RenderElement):
        BITMAP: None
        ELEMENTNAME: str
        ENABLED: bool
        FILTERON: bool
        VELOCITYMAX: float
        VELOCITYON: bool
        ...
    class VideoPostTracks(MAXTVNode):
        ...
    class VisualMS(Interface):
        ...
    class VisualMSCA(Interface):
        ...
    class VptSetting(IObject):
        ...
    class WalkThroughOps(Interface):
        ...
    class Waves(TextureMap):
        AMPLITUDE: float
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COORDS: MXSWrapperBase
        DISTRIBUTION: int
        MAP1: None
        MAP1ON: bool
        MAP2: None
        MAP2ON: bool
        NUMWAVESETS: int
        PHASE: float
        RANDOMSEED: int
        WAVELENMAX: float
        WAVELENMIN: float
        WAVERADIUS: float
        ...
    class WeldSpline(Primitive):
        ...
    class White(Color):
        ...
    class Write_Cws_Channel(MAXScriptFunction):
        ...
    class Write_Cws_CineonConverter(MAXScriptFunction):
        ...
    class Write_Cws_Composite(MAXScriptFunction):
        ...
    class Write_Cws_Composite_Settings(MAXScriptFunction):
        ...
    class Write_Cws_Connect(MAXScriptFunction):
        ...
    class Write_Cws_Eof(MAXScriptFunction):
        ...
    class Write_Cws_Footage(MAXScriptFunction):
        ...
    class Write_Cws_Head(MAXScriptFunction):
        ...
    class Write_Cws_Object(MAXScriptFunction):
        ...
    class Write_Cws_Operator(MAXScriptFunction):
        ...
    class Write_Cws_Parenting(MAXScriptFunction):
        ...
    class XView(GlobalUtilityPlugin):
        ...
    class XViewChecker(Interface):
        ...
    class X_Axis(Point3):
        ...
    class Y_Axis(Point3):
        ...
    class Yellow(Color):
        ...
    class YesNoCancelBox(Primitive):
        ...
    class Z_Axis(Point3):
        ...
def undo(onoff, label='MAXScript'): ...
