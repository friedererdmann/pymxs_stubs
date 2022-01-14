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
        FORMAT: str
        QUALITY: str
        EXPOSURE: str
        RENDERTYPE: str
        WIDTH: int
        HEIGHT: int
        NOTIFYBYEMAIL: bool
        ALPHA: bool
        ...
    class A360RendererPresetsHelper(ReferenceTarget):
        ...
    class A360_Cloud_Rendering(RendererClass):
        FORMAT: str
        QUALITY: str
        EXPOSURE: str
        RENDERTYPE: str
        WIDTH: int
        HEIGHT: int
        NOTIFYBYEMAIL: bool
        ALPHA: bool
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
        ENABLE_ITERATIONS: bool
        ITERATIONS: int
        QUALITY_DB: float
        ENABLE_TIME: bool
        TIME_IN_SECONDS: int
        TIME_SPLIT_SECONDS: int
        TIME_SPLIT_MINUTES: int
        TIME_SPLIT_HOURS: int
        MOTION_BLUR_ALL_OBJECTS: bool
        RENDER_METHOD: int
        POINT_LIGHT_DIAMETER: float
        ENABLE_OUTLIER_CLAMP: bool
        ANTI_ALIASING_FILTER_DIAMETER: float
        ENABLE_ANIMATED_NOISE: bool
        ENABLE_NOISE_FILTER: bool
        NOISE_FILTER_STRENGTH: float
        NOISE_FILTER_STRENGTH_PERCENTAGE: float
        TEXTURE_BAKE_RESOLUTION: int
        MAXIMUM_INTERACTIVE_DOWN_RES_FACTOR: int
        ...
    class ART_Renderer_Noise_Filter(RenderElement):
        ELEMENTNAME: str
        ENABLED: bool
        BITMAP: bool
        STRENGTH: float
        STRENGTH_PERCENTAGE: float
        ...
    class ASec_Element(ReferenceTarget):
        ELEMENTNAME: str
        MINSIZE: float
        INTENSITY: float
        MAXSIZE: float
        AXIS: float
        QUANTITY: int
        SIDES: int
        ON: bool
        SQUEEZE: bool
        OCCLUSION: float
        PRESETS: int
        COLORSOURCE: float
        RADIALCOLOR1: MXSWrapperBase
        RADIALCOLOR2: MXSWrapperBase
        RADIALCOLOR3: MXSWrapperBase
        RADIALCOLOR4: MXSWrapperBase
        COLORRADIUS1: float
        COLORRADIUS2: float
        COLORRADIUS3: float
        COLORRADIUS4: float
        RADIALMTL: None
        USERADIALMTL: bool
        RADIALMAP: None
        USERADIALMAP: bool
        CIRCULARCOLORMIX: float
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        QUADRANT4COLOR: MXSWrapperBase
        CIRCULARMTL: None
        USECIRCULARMTL: bool
        CIRCULARMAP: None
        USECIRCULARMAP: bool
        RADIALSIZEMAP: None
        USERADIALSIZEMAP: bool
        APPLYLIGHTS: bool
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        SOURCEOBJECTID: bool
        OBJECTID: int
        SOURCEEFFECTSID: bool
        EFFECTSID: int
        SOURCEUNCLAMPEDCOLOR: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        SOURCESURFACENORMAL: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        SOURCEWHOLE: bool
        SOURCEALPHA: bool
        ALPHA: int
        SOURCEZBUFFER: bool
        ZHI: float
        ZLO: float
        FILTERALL: bool
        FILTEREDGE: bool
        FILTERPERIMETERALPHA: bool
        FILTERPERIMETER: bool
        FILTERBRIGHTNESS: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        FILTERHUE: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        APPLYNOISE: bool
        NOISEMAP: None
        RADIALDENSITY: None
        USERADIALDENSITY: bool
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
        ENABLE: bool
        QUALITY: float
        ENABLE_ADAPTIVE: bool
        ADAPTIVE_THRESHOLD: float
        ...
    class Adaptive_Uniform(SamplerClass):
        ENABLE: bool
        QUALITY: float
        ENABLE_ADAPTIVE: bool
        ADAPTIVE_THRESHOLD: float
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
        SHADOW_MODE: int
        PASS1: int
        PASS2: int
        RAY_BIAS: float
        BLUR: float
        JITTER_AMT: float
        TWOSIDEDSHADOWS: bool
        NOAREASHADOWS: bool
        SHADOW_TRANSPARENT: bool
        AA_THRESHOLD: MXSWrapperBase
        SUPPRESS_MAT_AA: bool
        SUPPRESS_REFLT_AA: bool
        SKIP_COPLANAR: bool
        COPLANAR_THRESHOLD: float
        ...
    class AdvancedWood(TextureMap):
        COORDS: MXSWrapperBase
        PRESET: int
        ROUGHNESS: float
        EARLY_WOOD_COLOR: MXSWrapperBase
        EARLY_WOOD_COLOR_MAP: None
        LATE_WOOD_COLOR_POWER: float
        USE_MANUAL_LATE_WOOD_COLOR: bool
        MANUAL_LATE_WOOD_COLOR: MXSWrapperBase
        MANUAL_LATE_WOOD_COLOR_MAP: None
        RING_THICKNESS: float
        DIFFUSE_LOBE_WEIGHT: float
        USE_PORES: bool
        PORE_TYPE: int
        PORE_CELL_DIM: float
        PORE_RADIUS: float
        PORE_COLOR_POWER: float
        PORE_DEPTH: float
        USE_RAYS: bool
        RAY_COLOR_POWER: float
        RAY_SEG_LENGTH_Z: float
        RAY_NUM_SLICES: int
        RAY_ELLIPSE_SCALE_X: float
        RAY_ELLIPSE_Z2X: float
        LATE_WOOD_RATIO: float
        EARLY_WOOD_SHARPNESS: float
        LATE_WOOD_SHARPNESS: float
        FIBER_PERLIN_SCALE_Z: float
        DIFFUSE_PERLIN_SCALE_Z: float
        USE_LATE_WOOD_BUMP: bool
        LATE_WOOD_BUMP_DEPTH: float
        USE_GROOVE_ROUGHNESS: bool
        GROOVE_ROUGHNESS: float
        USE_FIBER_PERLIN: bool
        USE_FIBER_COSINE: bool
        USE_GROWTH_PERLIN: bool
        USE_EARLY_WOOD_COLOR_PERLIN: bool
        USE_LATE_WOOD_COLOR_PERLIN: bool
        USE_DIFFUSE_PERLIN: bool
        FIBER_PERLIN_PROF: str
        FIBER_COSINE_PROF: str
        GROWTH_PERLIN_PROF: str
        DIFFUSE_PERLIN_PROF: str
        EARLY_WOOD_COLOR_PERLIN_PROF: str
        LATE_WOOD_COLOR_PERLIN_PROF: str
        SCALE: float
        AXIS: int
        UNIT_DEPENDENT: bool
        ...
    class Advanced_Lighting_Override(Material):
        REFLECTANCESCALE: float
        COLORBLEED: float
        TRANSMITTANCESCALE: float
        LUMINANCESCALE: float
        BUMPSCALE: float
        BASEMATERIAL: MXSWrapperBase
        ...
    class Advanced_Ray_Traced(Shadow):
        SHADOW_MODE: int
        PASS1: int
        PASS2: int
        RAY_BIAS: float
        BLUR: float
        JITTER_AMT: float
        TWOSIDEDSHADOWS: bool
        NOAREASHADOWS: bool
        SHADOW_TRANSPARENT: bool
        AA_THRESHOLD: MXSWrapperBase
        SUPPRESS_MAT_AA: bool
        SUPPRESS_REFLT_AA: bool
        SKIP_COPLANAR: bool
        COPLANAR_THRESHOLD: float
        ...
    class Affect_Region(Modifier):
        FALLOFF: float
        IGNOREBACKFACING: int
        PINCH: float
        BUBBLE: float
        ...
    class Age_Test(Helper):
        TEST_TYPE: int
        CONDITION_TYPE: int
        TEST_VALUE: int
        VARIATION: int
        SUBFRAME_SAMPLING: bool
        RANDOM_SEED: int
        ADJUSTABLE_AGE: bool
        ...
    class AlembicCamera(Camera):
        ...
    class AlembicContainer(GeometryClass):
        NODES: MXSWrapperBase
        ICONSCALE: float
        SHOWICON: bool
        ...
    class AlembicDummyObject(Helper):
        ...
    class AlembicExport(ExporterPlugin):
        ...
    class AlembicFloat(FloatController):
        SOURCE: str
        OBJECT: None
        PLAYBACKTYPE: int
        PLAYBACKSTART: float
        PLAYBACKEND: float
        PLAYBACKFRAME: float
        PROPERTYPATH: None
        VISCONTROL: bool
        RANKINDEX: int
        IMPORTVISIBILITY: bool
        PLAYBACKTYPEGEN: int
        PLAYBACKSTARTGEN: int
        PLAYBACKENDGEN: int
        PLAYBACKFRAMEGEN: int
        ...
    class AlembicImport(ImporterPlugin):
        ...
    class AlembicObject(GeometryClass):
        SOURCE: str
        OBJECT: None
        PLAYBACKTYPE: int
        PLAYBACKSTART: float
        PLAYBACKEND: float
        PLAYBACKFRAME: float
        IMPORTUVS: bool
        IMPORTNORMALS: bool
        IMPORTVERTEXCOLORS: bool
        IMPORTEXTRACHANNELS: bool
        IMPORTVELOCITY: bool
        IMPORTMATERIALIDS: bool
        IMPORTCUSTOMATTRIBUTES: bool
        PLAYBACKTYPEGEN: int
        PLAYBACKSTARTGEN: int
        PLAYBACKENDGEN: int
        PLAYBACKFRAMEGEN: int
        GENERATIONID: int
        ...
    class AlembicXform(Matrix3Controller):
        SOURCE: str
        OBJECT: None
        PLAYBACKTYPE: int
        PLAYBACKSTART: float
        PLAYBACKEND: float
        PLAYBACKFRAME: float
        MAXCOORDS: bool
        PLAYBACKTYPEGEN: int
        PLAYBACKSTARTGEN: int
        PLAYBACKENDGEN: int
        PLAYBACKFRAMEGEN: int
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
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        ...
    class AlwaysEqualFilter(ReferenceMaker):
        ...
    class AmbientOcclusionBakeElement(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SAMPLES: int
        BRIGHT: MXSWrapperBase
        DARK: MXSWrapperBase
        SPREAD: float
        MAXDISTANCE: float
        FALLOFF: float
        ...
    class Ambient_Occlusion(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SAMPLES: int
        BRIGHT: MXSWrapperBase
        DARK: MXSWrapperBase
        SPREAD: float
        MAXDISTANCE: float
        FALLOFF: float
        ...
    class AmountChange(ReferenceTarget):
        TYPE: int
        SUB_TYPE: int
        RESET_PARTICLE_AGE: bool
        SPAWNS_AS_NEW_IN_EVENT: bool
        PROCEED_TYPE: int
        HISTORY_DEPENDENT: bool
        EXECUTION_ORDER: int
        USE_IS_CURRENT_PARENT: bool
        IS_CURRENT_PARENT_DATA_CHANNEL: None
        USE_IS_CURRENT_SPAWN: bool
        IS_CURRENT_SPAWN_DATA_CHANNEL: None
        USE_PARENT_ID: bool
        PARENT_ID_DATA_CHANNEL: None
        USE_LAST_SPAWN_ID: bool
        LAST_SPAWN_ID_DATA_CHANNEL: None
        USE_FIRST_SPAWN_ID: bool
        FIRST_SPAWN_ID_DATA_CHANNEL: None
        USE_CURRENT_FIRST_SPAWN_ID: bool
        CURRENT_FIRST_SPAWN_ID_DATA_CHANNEL: None
        USE_OLDER_SIBLING_ID: bool
        OLDER_SIBLING_ID_DATA_CHANNEL: None
        USE_CURRENT_SPAWN_COUNT: bool
        CURRENT_SPAWN_COUNT_DATA_CHANNEL: None
        USE_TOTAL_SPAWN_COUNT: bool
        TOTAL_SPAWN_COUNT_DATA_CHANNEL: None
        USE_CURRENT_SPAWN_ORDER: bool
        CURRENT_SPAWN_ORDER_DATA_CHANNEL: None
        FILTER: None
        INPUT_1: None
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
        SEED: int
        SIZE: float
        ANGLE: float
        INTENSITY: float
        SQUEEZE: float
        AFFECTALPHA: bool
        AFFECTZBUFFER: bool
        DISTAFFECTSSIZE: bool
        DISTAFFECTSINTENSITY: bool
        CENTERAFFECTSSIZE: bool
        CENTERAFFECTSINTENSITY: bool
        INNEROCCLUSIONRADIUS: float
        OCCLUSIONAFFECTSSIZE: bool
        OUTEROCCLUSIONRADIUS: float
        OCCLUSIONAFFECTSINTENSITY: bool
        AFFECTBYATMOSPHERE: bool
        LIGHTDIRECTIONAFFECTSSIZE: bool
        LIGHTDIRECTIONAFFECTSINTENSITY: bool
        ...
    class Apollo_Param_Container(GeometryClass):
        ...
    class AppendSubSelSet(Primitive):
        ...
    class ApplyOperation(MAXScriptFunction):
        ...
    class ApplyUVAsColor(Modifier):
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class ApplyUVAsHSLColor(Modifier):
        HUE_MINIMUM: float
        HUE_MAXIMUM: float
        SATURATION_MINIMUM: float
        SATURATION_MAXIMUM: float
        LUMINANCE_MINIMUM: float
        LUMINANCE_MAXIMUM: float
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class ApplyUVAsHSLGradient(Modifier):
        USE_V_FOR_HUE: bool
        COLOR_1: MXSWrapperBase
        COLOR_2: MXSWrapperBase
        COLOR_3: MXSWrapperBase
        USE_V_FOR_SATURATION: bool
        USE_V_FOR_LIGHTNESS: bool
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class ApplyUVAsHSLGradientWithMidpoint(Modifier):
        USE_V_FOR_HUE: bool
        MIDPOINT: float
        COLOR_1: MXSWrapperBase
        COLOR_2: MXSWrapperBase
        EASE_A: float
        COLOR_3: MXSWrapperBase
        EASE_B: float
        USE_V_FOR_SATURATION: bool
        USE_V_FOR_LIGHTNESS: bool
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class ArbAxis(Primitive):
        ...
    class ArbBone(Matrix3Controller):
        ...
    class ArbBoneTrans(Matrix3Controller):
        ...
    class Arc(Shape):
        FROM: float
        STEPS: int
        TO: float
        RADIUS: float
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        REVERSE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        PIE: bool
        ...
    class Architectural(Material):
        TEMPLATE: str
        DIFFUSE: MXSWrapperBase
        IOR: float
        TWOSIDED: bool
        EMITLUMINANCE: bool
        COLORBLEED: float
        REFLECTANCESCALE: float
        INDIRECTBUMPAMOUNT: float
        TRANSMITTANCESCALE: float
        USETEXTURESIZE: bool
        TEXTUREWIDTH: float
        TEXTUREHEIGHT: float
        TEXTUREUOFFSET: float
        TEXTUREVOFFSET: float
        RAWDIFFUSETEXTURE: bool
        SAMPLER: int
        SAMPLERQUALITY: float
        SAMPLERENABLE: bool
        SAMPLERADAPTTHRESHOLD: float
        SAMPLERADAPTON: bool
        SUBSAMPLETEXTUREON: bool
        SAMPLERADVANCEDOPTIONS: bool
        SAMPLERBYNAME: str
        USERPARAM0: float
        USERPARAM1: float
        SAMPLERUSEGLOBAL: bool
        DIFFUSEMAP: None
        FILTERMAP: None
        SHININESSMAP: None
        LUMINANCEMAP: None
        BUMPMAP: None
        DISPLACEMENTMAP: None
        TRANSLUCENCYMAP: None
        CUTOUTMAP: None
        INTENSITYMAP: None
        DIFFUSEMAPAMOUNT: float
        SHININESS: float
        TRANSPARENCY: float
        LUMINANCE: float
        BUMPMAPAMOUNT: float
        DISPLACEMENTMAPAMOUNT: float
        TRANSLUCENCY: float
        CUTOUTMAPAMOUNT: float
        INTENSITYMAPAMOUNT: float
        DIFFUSEMAPENABLE: bool
        SHININESSMAPENABLE: bool
        TRANSPARENCYMAPENABLE: bool
        LUMINANCEMAPENABLE: bool
        BUMPMAPENABLE: bool
        DISPLACEMENTMAPENABLE: bool
        TRANSLUCENCYENABLE: bool
        CUTOUTMAPENABLE: bool
        INTENSITYMAPENABLE: bool
        MAPS: MXSWrapperBase
        MAPAMOUNTS: MXSWrapperBase
        MAPSENABLES: MXSWrapperBase
        ...
    class ArchitecturalMaterial(Material):
        TEMPLATE: str
        DIFFUSE: MXSWrapperBase
        IOR: float
        TWOSIDED: bool
        EMITLUMINANCE: bool
        COLORBLEED: float
        REFLECTANCESCALE: float
        INDIRECTBUMPAMOUNT: float
        TRANSMITTANCESCALE: float
        USETEXTURESIZE: bool
        TEXTUREWIDTH: float
        TEXTUREHEIGHT: float
        TEXTUREUOFFSET: float
        TEXTUREVOFFSET: float
        RAWDIFFUSETEXTURE: bool
        SAMPLER: int
        SAMPLERQUALITY: float
        SAMPLERENABLE: bool
        SAMPLERADAPTTHRESHOLD: float
        SAMPLERADAPTON: bool
        SUBSAMPLETEXTUREON: bool
        SAMPLERADVANCEDOPTIONS: bool
        SAMPLERBYNAME: str
        USERPARAM0: float
        USERPARAM1: float
        SAMPLERUSEGLOBAL: bool
        DIFFUSEMAP: None
        FILTERMAP: None
        SHININESSMAP: None
        LUMINANCEMAP: None
        BUMPMAP: None
        DISPLACEMENTMAP: None
        TRANSLUCENCYMAP: None
        CUTOUTMAP: None
        INTENSITYMAP: None
        DIFFUSEMAPAMOUNT: float
        SHININESS: float
        TRANSPARENCY: float
        LUMINANCE: float
        BUMPMAPAMOUNT: float
        DISPLACEMENTMAPAMOUNT: float
        TRANSLUCENCY: float
        CUTOUTMAPAMOUNT: float
        INTENSITYMAPAMOUNT: float
        DIFFUSEMAPENABLE: bool
        SHININESSMAPENABLE: bool
        TRANSPARENCYMAPENABLE: bool
        LUMINANCEMAPENABLE: bool
        BUMPMAPENABLE: bool
        DISPLACEMENTMAPENABLE: bool
        TRANSLUCENCYENABLE: bool
        CUTOUTMAPENABLE: bool
        INTENSITYMAPENABLE: bool
        MAPS: MXSWrapperBase
        MAPAMOUNTS: MXSWrapperBase
        MAPSENABLES: MXSWrapperBase
        ...
    class Area(Filter):
        ...
    class Area_Shadows(Shadow):
        SHADOW_MODE: int
        PASS1: int
        PASS2: int
        RAY_BIAS: float
        BLUR: float
        SHADOW_WIDTH: float
        SHADOW_LENGTH: float
        SHADOW_HEIGHT: float
        JITTER_AMT: float
        TWOSIDEDSHADOWS: bool
        SHADOW_TRANSPARENT: bool
        AA_THRESHOLD: MXSWrapperBase
        SUPPRESS_MAT_AA: bool
        SUPPRESS_REFLT_AA: bool
        SKIP_COPLANAR: bool
        COPLANAR_THRESHOLD: float
        ...
    class Arnold(RendererClass):
        PREPASS_ENABLED: bool
        PREPASS_SAMPLES: int
        AA_SAMPLES: int
        GI_DIFFUSE_SAMPLES: int
        GI_DIFFUSE_DEPTH: int
        GI_SPECULAR_SAMPLES: int
        GI_SPECULAR_DEPTH: int
        GI_TRANSMISSION_SAMPLES: int
        GI_TRANSMISSION_DEPTH: int
        GI_SSS_SAMPLES: int
        GI_VOLUME_SAMPLES: int
        GI_VOLUME_DEPTH: int
        ENABLE_ADAPTIVE_SAMPLING: bool
        AA_SAMPLES_MAX: int
        ADAPTIVE_THRESHOLD: float
        PROGRESSIVE_RENDER: bool
        GI_TOTAL_DEPTH: int
        AUTO_TRANSPARENCY_DEPTH: int
        LOW_LIGHT_THRESHOLD: float
        LOCK_SAMPLING_PATTERN: bool
        SSS_USE_AUTOBUMP: bool
        INDIRECT_SPECULAR_BLUR: float
        FILTER: int
        FILTER_WIDTH: float
        AA_SAMPLE_CLAMP_ENABLED: bool
        AA_SAMPLE_CLAMP_AFFECTS_AOVS: bool
        AA_SAMPLE_CLAMP: float
        INDIRECT_SAMPLE_CLAMP: float
        PHYSICAL_MATERIAL_SSS_TYPE: int
        DIELECTRIC_PRIORITIES: bool
        ENV_MODE: int
        ENV_IBL_SAMPLES: int
        ENV_PHYS_BGND_MODE: int
        ENV_PHYS_BGND_COLOR: MXSWrapperBase
        ENV_PHYS_BGND_MAP: None
        ENV_IBL_ENABLE: bool
        ENV_ADV_IBL_MULTIPLIER: float
        ENV_ADV_IBL_VOLUME_SAMPLES: int
        ENV_ADV_IBL_PORTAL_MODE: int
        ENV_ADV_IBL_MAX_BOUNCES: int
        ENV_ADV_IBL_RESOLUTION_ENABLE: bool
        ENV_ADV_IBL_RESOLUTION: int
        ENV_ADV_IBL_EMIT_CAMERA: bool
        ENV_ADV_IBL_EMIT_DIFFUSE: bool
        ENV_ADV_IBL_EMIT_SPECULAR: bool
        ENV_ADV_IBL_EMIT_TRANSMISSION: bool
        ENV_ADV_IBL_AFFECT_SSS: bool
        ENV_ADV_IBL_AFFECT_INDIRECT: bool
        ENV_ADV_IBL_AFFECT_VOLUME: bool
        ENV_ADV_IBL_CAMERA_MULT: float
        ENV_ADV_IBL_DIFFUSE_MULT: float
        ENV_ADV_IBL_SPECULAR_MULT: float
        ENV_ADV_IBL_TRANSMISSION_MULT: float
        ENV_ADV_IBL_SSS_MULT: float
        ENV_ADV_IBL_INDIRECT_MULT: float
        ENV_ADV_IBL_VOLUME_MULT: float
        ENV_ADV_IBL_CAST_SHADOWS: bool
        ENV_ADV_IBL_SHADOW_COLOR: MXSWrapperBase
        ENV_ADV_IBL_SHADOW_DENSITY: float
        ENV_ADV_BGND_MODE: int
        ENV_ADV_BGND_VISIBLE_TO_CAMERA: bool
        ENV_ADV_BGND_VISIBLE_TO_DIFFUSE_REFLECTIONS: bool
        ENV_ADV_BGND_VISIBLE_TO_SPECULAR_REFLECTIONS: bool
        ENV_ADV_BGND_VISIBLE_TO_DIFFUSE_TRANSMISSION: bool
        ENV_ADV_BGND_VISIBLE_TO_SPECULAR_TRANSMISSION: bool
        ENV_ADV_BGND_VISIBLE_TO_VOLUME_SCATTERING: bool
        ENV_ADV_BGND_CUSTOM_COLOR: MXSWrapperBase
        ENV_ADV_BGND_CUSTOM_MAP: None
        ENV_ADV_BGND_CUSTOM_SHADER: None
        ATMOSPHERE: None
        RESPECT_PHYSICAL_CAMERA_MOTION_BLUR: bool
        ENABLE_TRANSFORM_KEYS: bool
        TRANSFORM_KEYS: int
        ENABLE_DEFORM_KEYS: bool
        DEFORM_KEYS: int
        SHUTTER_LENGTH: float
        SHUTTER_POSITION: int
        AUTO_SHUTTER: bool
        SHUTTER_OPEN: float
        SHUTTER_CLOSE: float
        SHUTTER_TYPE: int
        IGNORE_MOTION_BLUR: bool
        MAX_SUBDIVISIONS: int
        GEOMETRY_DICING_CAMERA: None
        SUBDIV_FRUSTUM_CULLING: bool
        SUBDIV_FRUSTUM_PADDING: float
        DISPLACEMENT_DEFAULT_SUBDIV_TYPE: int
        DISPLACEMENT_DEFAULT_SUBDIV_ITERATIONS: int
        DISPLACEMENT_DEFAULT_SUBDIV_ADAPTIVE_ERROR: float
        CURVES_DEFAULT_BASIS: int
        CURVES_DEFAULT_MODE: int
        CURVES_DEFAULT_MIN_PIXEL_WIDTH: float
        TEXTURE_AUTOMIP: bool
        TEXTURE_ACCEPT_UNMIPPED: bool
        TEXTURE_ENABLE_AUTOTILE: bool
        TEXTURE_AUTOTILE: int
        TEXTURE_ACCEPT_UNTILED: bool
        USE_EXISTING_TX: bool
        TEXTURE_MAX_MEMORY_MB: int
        TEXTURE_MAX_OPEN_FILES: int
        GPU_MAX_TEXTURE_RESOLUTION: int
        BUCKET_SCANNING: int
        BUCKET_SIZE: int
        SHOW_BUCKET_CORNERS_PROD: bool
        SHOW_BUCKET_CORNERS_AS: bool
        ABORT_ON_LICENSE_FAIL: bool
        SKIP_LICENSE_CHECK: bool
        LEGACY_3DS_MAX_MAP_SUPPORT: bool
        AUTODETECT_THREADS: bool
        THREADS: int
        GPU_SELECTION: MXSWrapperBase
        GPU_RENDERING: bool
        RENDER_DEVICE: int
        RENDER_DEVICE_FALLBACK: int
        DEFAULT_GPU_NAMES: str
        DEFAULT_GPU_MIN_MEMORY_MB: int
        GPU_AUTO_SELECTION: bool
        USE_OPTIX_ON_BEAUTY: bool
        NOICE_INPUT: str
        NOICE_OUTPUT: str
        NOICE_ANIM_RANGE: int
        NOICE_START_FRAME: int
        NOICE_END_FRAME: int
        NOICE_ADDITIONAL_FRAMES: int
        NOICE_VARIANCE: float
        NOICE_SEARCH_RADIUS: int
        NOICE_PATCH_RADIUS: int
        NOICE_LIGHT_AOV_NAMES: str
        OUTPUT_DENOISING_AOVS: bool
        PROCEDURAL_SEARCHPATH: None
        PLUGIN_SEARCHPATH: None
        TEXTURE_SEARCHPATH: None
        VERBOSITY_LEVEL: int
        LOG_TO_CONSOLE: bool
        LOG_TO_FILE: bool
        LOG_FILE: None
        MAX_WARNINGS: int
        TEXTURE_PER_FILE_STATS: bool
        LOG_RENDER_STATS: bool
        RENDER_STATS_FILE: None
        RENDER_STATS_MODE: int
        LOG_RENDER_PROFILE: bool
        RENDER_PROFILE_FILE: None
        ABORT_ON_ERROR: bool
        ABORT_ON_ERROR_ACTIVESHADE: bool
        ERROR_COLOR_BAD_TEXTURE: MXSWrapperBase
        ERROR_COLOR_BAD_SHADER: MXSWrapperBase
        ERROR_COLOR_BAD_PIXEL: MXSWrapperBase
        IGNORE_TEXTURES: bool
        IGNORE_SHADERS: bool
        IGNORE_ATMOSPHERE: bool
        IGNORE_LIGHTS: bool
        IGNORE_SHADOWS: bool
        IGNORE_SUBDIVISION: bool
        IGNORE_DISPLACEMENT: bool
        IGNORE_BUMP: bool
        IGNORE_SMOOTHING: bool
        IGNORE_MOTION: bool
        IGNORE_DOF: bool
        IGNORE_SSS: bool
        IGNORE_OPERATORS: bool
        SHADER_OVERRIDE_ENABLED: bool
        SHADER_OVERRIDE: None
        ENABLE_USER_OPTIONS: bool
        USER_OPTIONS: None
        EXPORT_TO_ASS: bool
        ASS_FILE_PATH: None
        EXPORT_OPTION: bool
        EXPORT_CAMERAS: bool
        EXPORT_DRIVERSFILTERS: bool
        EXPORT_LIGHTS: bool
        EXPORT_GEOMETRY: bool
        EXPORT_SHADERS: bool
        EXPORT_OPERATORS: bool
        EXPORT_BINARY: bool
        EXPAND_PROCEDURALS: bool
        EXPORT_TO_MTLX: bool
        MTLX_FILE_PATH: None
        MTLX_LOOK: str
        MTLX_PROPERTIES: None
        MTLX_RELATIVE: bool
        MTLX_USE_CURRENT_SELECTION: bool
        OPERATOR_ROOT: None
        OPERATOR_EXPORT_LIST: MXSWrapperBase
        OPERATOR_EXPORT_TREE: bool
        MATERIAL_EXPORT_LIST: MXSWrapperBase
        RETRANSLATE_ALL_FRAMES: bool
        USE_QUADS: int
        EXPORT_TO_ASS_ORIGIN: int
        USE_RENDER_VIEW: bool
        RENDER_VIEW_SETTINGS: str
        IMAGER_0: None
        AOV_MANAGER: None
        DRIVER_TYPE: None
        AOV_SHADERS_MAT_0: None
        AOV_SHADERS_MAT_1: None
        AOV_SHADERS_MAT_2: None
        AOV_SHADERS_MAP_0: None
        AOV_SHADERS_MAP_1: None
        AOV_SHADERS_MAP_2: None
        ...
    class ArnoldAOV(ReferenceTarget):
        ACTIVE: bool
        DENOISED: bool
        DATA: str
        NAME: None
        FILTER: str
        FILTERWIDTH: float
        LIGHTGROUP: str
        LAYERTOLERANCE: float
        LAYERENABLEFILTERING: bool
        LAYERHALFPRECISION: bool
        ...
    class ArnoldAOVsManager(ReferenceTarget):
        ...
    class ArnoldAOVsManagerClassDescCreator(Interface):
        ...
    class ArnoldDEEPEXRDriver(ReferenceTarget):
        ACTIVE: bool
        FILENAMESUFFIX: None
        NAME: None
        USEAOVNAME: bool
        TILED: bool
        APPEND: bool
        SUBPIXELMERGE: bool
        USERGBOPACITY: bool
        ALPHATOLERANCE: float
        DEPTHTOLERANCE: float
        ALPHAHALFPRECISION: bool
        DEPTHHALFPRECISION: bool
        CUSTOMATTRIBUTES: None
        AOVLIST: MXSWrapperBase
        LIGHTGROUP: str
        ...
    class ArnoldEXRDriver(ReferenceTarget):
        ACTIVE: bool
        FILENAMESUFFIX: None
        NAME: None
        USEAOVNAME: bool
        COMPRESSION: str
        HALFPRECISION: bool
        TILED: bool
        PRESERVELAYERNAME: bool
        AUTOCROP: bool
        APPEND: bool
        CUSTOMATTRIBUTES: None
        AOVLIST: MXSWrapperBase
        LIGHTGROUP: str
        ...
    class ArnoldFluidUtility(Interface):
        ...
    class ArnoldGeometryPropertiesModifier(Modifier):
        ENABLE_VISIBILITY_OPTIONS: bool
        PRIMARY_VISIBILITY: bool
        VISIBLE_TO_DIFFUSE_REFLECTIONS: bool
        VISIBLE_TO_SPECULAR_REFLECTIONS: bool
        VISIBLE_TO_DIFFUSE_TRANSMISSION: bool
        VISIBLE_TO_SPECULAR_TRANSMISSION: bool
        VISIBLE_TO_VOLUME_SCATTERING: bool
        ENABLE_SHADOW_OPTIONS: bool
        CASTS_SHADOWS: bool
        RECEIVE_SHADOWS: bool
        SELF_SHADOWS: bool
        ENABLE_GENERAL_OPTIONS: bool
        DOUBLE_SIDED: bool
        INVERT_NORMALS: bool
        OPAQUE: bool
        MATTE: bool
        ENABLE_MIKKT: bool
        MIKKT_UV_CHANNEL: int
        ENABLE_DISPLACEMENT_OPTIONS: bool
        DISPLACEMENT_HEIGHT: float
        DISPLACEMENT_ZERO: float
        DISPLACEMENT_BOUNDS_PADDING: float
        DISPLACEMENT_ENABLE_AUTOBUMP: bool
        AUTOBUMP_CAMERA: bool
        AUTOBUMP_DIFFUSE_REFLECTIONS: bool
        AUTOBUMP_SPECULAR_REFLECTIONS: bool
        AUTOBUMP_DIFFUSE_TRANSMISSION: bool
        AUTOBUMP_SPECULAR_TRANSMISSION: bool
        AUTOBUMP_VOLUME_SCATTERING: bool
        DISPLACEMENT_MAP_ON: bool
        DISPLACEMENT_MAP: None
        ENABLE_SUBDIVISION_OPTIONS: bool
        SUBDIVISION_TYPE: int
        SUBDIVISION_ITERATIONS: int
        SUBDIVISION_METRIC: int
        SUBDIVISION_ADAPTIVE_ERROR: float
        SUBDIVISION_SPACE: int
        SUBDIVISION_UV_TYPE: int
        SUBDIVISION_SMOOTH_TANGENTS: bool
        SUBDIV_FRUSTUM_IGNORE: bool
        MOTION_BLUR_USE_TRANSFORM: bool
        MOTION_BLUR_TRANSFORM_KEYS: int
        MOTION_BLUR_USE_DEFORMATION: bool
        MOTION_BLUR_DEFORMATION_KEYS: int
        ENABLE_SSS_OPTIONS: bool
        SSS_SET_NAME: None
        ENABLE_TOON_OPTIONS: bool
        TOON_ID: None
        ENABLE_VOLUME: bool
        STEP_SIZE: float
        VOLUME_PADDING: float
        ENABLE_POINTS: bool
        MIN_PIXEL_WIDTH: float
        MODE: int
        PARTICLE_SYS_AS_POINTS: bool
        ENABLE_USER_OPTIONS: bool
        USER_OPTIONS: None
        TRACE_SETS: None
        ENABLE_LIGHT_GROUP: bool
        LIGHT_GROUP: MXSWrapperBase
        ENABLE_SHADOW_GROUP: bool
        SHADOW_GROUP: MXSWrapperBase
        ENABLE_CAMERA: bool
        RADIAL_DISTORTION: float
        ENABLE_FILTERMAP: bool
        FILTERMAP: None
        ENABLE_UV_REMAP: bool
        UV_REMAP: None
        RADIAL_DISTORTION_TYPE: int
        ...
    class ArnoldJPEGDriver(ReferenceTarget):
        ACTIVE: bool
        FILENAMESUFFIX: None
        NAME: None
        USEAOVNAME: bool
        OUTPUTPADDED: bool
        COLOR_SPACE: int
        DITHER: bool
        QUALITY: int
        AOVLIST: MXSWrapperBase
        LIGHTGROUP: str
        ...
    class ArnoldLightBlockerFilterModifier(Modifier):
        GEOMETRY_TYPE: int
        DENSITY: float
        ROUNDNESS: float
        WIDTH_EDGE: float
        HEIGHT_EDGE: float
        RAMP: float
        AXIS: int
        POSITIONX: float
        POSITIONY: float
        POSITIONZ: float
        ROTATIONX: float
        ROTATIONY: float
        ROTATIONZ: float
        SCALEX: float
        SCALEY: float
        SCALEZ: float
        OBJECT: None
        USESHADER: bool
        SHADER: None
        ...
    class ArnoldLightFilterModifier(Modifier):
        LIGHTFILTER: None
        VIEWPORTSHAPE: None
        VIEWPORTDATA: None
        ...
    class ArnoldMapToMtl(Material):
        SURFACESHADER: None
        SURFACESHADERENABLED: bool
        OPAQUEENABLED: bool
        ...
    class ArnoldPNGDriver(ReferenceTarget):
        ACTIVE: bool
        FILENAMESUFFIX: None
        NAME: None
        USEAOVNAME: bool
        FORMAT: None
        OUTPUTPADDED: bool
        COLOR_SPACE: int
        DITHER: bool
        AOVLIST: MXSWrapperBase
        LIGHTGROUP: str
        ...
    class ArnoldSceneSourceExport(ExporterPlugin):
        ...
    class ArnoldShadersLoader(GlobalUtilityPlugin):
        ...
    class ArnoldTIFFDriver(ReferenceTarget):
        ACTIVE: bool
        FILENAMESUFFIX: None
        NAME: None
        USEAOVNAME: bool
        COMPRESSION: str
        FORMAT: None
        TILED: bool
        OUTPUTPADDED: bool
        COLOR_SPACE: int
        DITHER: bool
        UNPREMULTALPHA: bool
        SKIPALPHA: bool
        APPEND: bool
        AOVLIST: MXSWrapperBase
        LIGHTGROUP: str
        ...
    class Arnold_A(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Alembic_Object(GeometryClass):
        FILENAME: str
        NAME_SPACE: str
        NAMEPREFIX: str
        OBJECTPATH: str
        FRAME: float
        FPS: float
        EXCLUDE_XFORM: bool
        MAKE_INSTANCE: bool
        SUBDIV_ITERATIONS: int
        FLIP_V: bool
        SCENE_CAMERA: str
        PULL_USER_PARAMS: bool
        VELOCITY_IGNORE: bool
        VELOCITY_SCALE: float
        VISIBILITY_IGNORE: bool
        EXPAND_HIDDEN: bool
        RADIUS_ATTRIBUTE: str
        RADIUS_DEFAULT: float
        RADIUS_SCALE: float
        UPAXIS: int
        BBOXLOW: MXSWrapperBase
        BBOXHI: MXSWrapperBase
        OPERATOR: None
        LAYERS: MXSWrapperBase
        ANIMATED: bool
        ANIMSEQUENCESTART: int
        ANIMSEQUENCEEND: int
        ANIMANIMSTART: int
        ANIMANIMEND: int
        ANIMSPEED: float
        ANIMPINGPONG: bool
        ANIMLOOP: bool
        ANIMEXTEND: bool
        VIEWPORT_MODE: int
        BBOX_THRESHOLD: float
        USE_BBOX_THRESHOLD: bool
        ANIMATION_CACHE: int
        USE_ANIMATION_CACHE: bool
        USE_VP_ANIMATION: bool
        ...
    class Arnold_Barndoor(Modifier):
        ARNOLD_NODE: str
        ARNOLD_NODE_BARNDOOR_TOP_LEFT: float
        ARNOLD_NODE_BARNDOOR_TOP_RIGHT: float
        ARNOLD_NODE_BARNDOOR_TOP_EDGE: float
        ARNOLD_NODE_BARNDOOR_RIGHT_TOP: float
        ARNOLD_NODE_BARNDOOR_RIGHT_BOTTOM: float
        ARNOLD_NODE_BARNDOOR_RIGHT_EDGE: float
        ARNOLD_NODE_BARNDOOR_BOTTOM_LEFT: float
        ARNOLD_NODE_BARNDOOR_BOTTOM_RIGHT: float
        ARNOLD_NODE_BARNDOOR_BOTTOM_EDGE: float
        ARNOLD_NODE_BARNDOOR_LEFT_TOP: float
        ARNOLD_NODE_BARNDOOR_LEFT_BOTTOM: float
        ARNOLD_NODE_BARNDOOR_LEFT_EDGE: float
        ...
    class Arnold_Light(Light):
        ON: bool
        TARGETED: bool
        TARGDIST: float
        USECOLOR: bool
        COLOR: MXSWrapperBase
        USEPRESET: bool
        PRESET: int
        USEKELVIN: bool
        KELVIN: float
        FILTER: MXSWrapperBase
        INTENSITY: float
        EXPOSURE: float
        NORMALIZE: bool
        SAMPLES: int
        VOLUME_SAMPLES: int
        SHAPETYPE: int
        LIGHTRADIUS: float
        LIGHTSHAPEVISIBLE: bool
        CAST_SHADOWS: bool
        CAST_VOLUMETRIC_SHADOWS: bool
        SHADOW_COLOR: MXSWrapperBase
        SHADOW_DENSITY: float
        CAMERA: float
        DIFFUSE: float
        SPECULAR: float
        TRANSMISSION: float
        SSS: float
        INDIRECT: float
        MAX_BOUNCES: int
        AFFECTVIEWPORT: bool
        SPREAD: float
        QUADX: float
        QUADY: float
        HEIGHT: float
        ANGLE: float
        LENS_RADIUS: float
        PENUMBRA_ANGLE: float
        ASPECT_RATIO: float
        SPOTROUNDNESS: float
        QUADROUNDNESS: float
        SOFT_EDGE: float
        USEROPTIONS: None
        FILENAME: str
        RESOLUTION: int
        FORMAT: int
        USETEXMAP: bool
        TEXMAP: None
        LIGHTMESH: None
        ALWAYSVISIBLEINVIEWPORT: bool
        VOLUME: float
        AOV: str
        CONE_ANGLE: float
        PHOTOMETRICRADIUS: float
        PORTAL: bool
        PORTAL_MODE: int
        AOV_INDIRECT: bool
        ...
    class Arnold_Light_Decay(Modifier):
        ARNOLD_NODE: str
        ARNOLD_NODE_USE_NEAR_ATTEN: bool
        SHOW_NEAR_ATTEN: bool
        ARNOLD_NODE_NEAR_START: float
        ARNOLD_NODE_NEAR_END: float
        ARNOLD_NODE_USE_FAR_ATTEN: bool
        SHOW_FAR_ATTEN: bool
        ARNOLD_NODE_FAR_START: float
        ARNOLD_NODE_FAR_END: float
        ...
    class Arnold_Light_Gobo(Modifier):
        ARNOLD_NODE: str
        ARNOLD_NODE_DENSITY: float
        ARNOLD_NODE_FILTER_MODE: int
        ARNOLD_NODE_SLIDEMAP: MXSWrapperBase
        ARNOLD_LINK_SLIDEMAP: None
        ARNOLD_NODE_OFFSET: MXSWrapperBase
        ARNOLD_NODE_SSCALE: float
        ARNOLD_NODE_TSCALE: float
        ARNOLD_NODE_SWRAP: int
        ARNOLD_NODE_TWRAP: int
        ...
    class Arnold_N(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_P(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Procedural_Object(GeometryClass):
        PROCEDURAL: str
        UPAXIS: int
        BBOXLOW: MXSWrapperBase
        BBOXHI: MXSWrapperBase
        AUTO_INSTANCING: bool
        ANIMATED: bool
        ANIMFRAMES: int
        ANIMSEQUENCEEND: int
        ANIMSPEED: float
        ANIMOFFSET: int
        ANIMSEQUENCESTART: int
        ANIMANIMSTART: int
        ANIMANIMEND: int
        ANIMPINGPONG: bool
        ANIMLOOP: bool
        ANIMEXTEND: bool
        NAME_SPACE: str
        OPERATOR: None
        VIEWPORT_MODE: int
        BBOX_THRESHOLD: float
        USE_BBOX_THRESHOLD: bool
        ANIMATION_CACHE: int
        USE_ANIMATION_CACHE: bool
        ...
    class Arnold_RGBA(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_RGBA_Denoise(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Shape(Helper):
        SHAPE_OBJECT: None
        GROUP_MEMBERS: bool
        OBJECT_AND_CHILDREN: bool
        OBJECT_ELEMENTS: bool
        SCALE_VALUE: float
        VARIATION: float
        ACQUIRE_MAPPING: bool
        ACQUIRE_MATERIAL: bool
        SUBMTL_ID_OFFSET: int
        RANDOM_SHAPE: bool
        ANIMATED_SHAPE: bool
        ACQUIRE_SHAPE: bool
        FAST_SHAPE_EVALUATION: bool
        SYNC_TYPE: int
        ADD_RANDOM_OFFSET: bool
        RANDOM_OFFSET: int
        RANDOM_SEED: int
        SET_SCALE: bool
        REPORT_NODE_HANDLES: int
        HANDLES_TO_REPORT: MXSWrapperBase
        ...
    class Arnold_USD_Object(GeometryClass):
        FILENAME: str
        NAME_SPACE: str
        OBJECTPATH: str
        DEBUG: bool
        FRAME: float
        UPAXIS: int
        BBOXLOW: MXSWrapperBase
        BBOXHI: MXSWrapperBase
        OPERATOR: None
        VIEWPORT_MODE: int
        BBOX_THRESHOLD: float
        USE_BBOX_THRESHOLD: bool
        ANIMATION_CACHE: int
        USE_ANIMATION_CACHE: bool
        USE_VP_ANIMATION: bool
        ...
    class Arnold_Volume_Object(GeometryClass):
        VDBFILE: str
        UPAXIS: int
        BBOXAUTO: bool
        BBOXLOW: MXSWrapperBase
        BBOXHI: MXSWrapperBase
        BBOXPADDING: float
        SHADER: None
        GRIDS: str
        VELGRIDS: str
        VELOCITYSCALE: float
        STEPMODE: int
        STEPSCALE: float
        STEPSIZE: float
        VELOCITYOUTLIERTHRESHOLD: float
        ANIMATED: bool
        ANIMFRAMES: int
        ANIMSEQUENCEEND: int
        ANIMSPEED: float
        ANIMOFFSET: int
        ANIMSEQUENCESTART: int
        ANIMANIMSTART: int
        ANIMANIMEND: int
        ANIMPINGPONG: bool
        ANIMLOOP: bool
        ANIMEXTEND: bool
        ...
    class Arnold_Advanced_Map(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Albedo(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Coat(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Coat_Albedo(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Coat_Direct(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Coat_Indirect(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Denoise_Albedo(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Diffuse(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Diffuse_Albedo(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Diffuse_Direct(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Diffuse_Indirect(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Direct(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Emission(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Indirect(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Map_Override(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Metalness(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Roughness(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Shadow_Matte(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Sheen(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Sheen_Albedo(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Sheen_Direct(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Sheen_Indirect(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Specular(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Sss(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Sss_Albedo(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Sss_Direct(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Sss_Indirect(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Arnold_Volume_Z(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        SHADERS: str
        PARAMETER: str
        MAP: None
        ...
    class Array(Value):
        ...
    class ArrayParameter(Value):
        ...
    class ArrowHelper(Helper):
        ICONSIZE: float
        COLOR: MXSWrapperBase
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
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ...
    class AtmosphericClass(Value):
        ...
    class AttachObjects(Primitive):
        ...
    class Attachment(PositionController):
        ALIGN: bool
        NODE: None
        MANUPDATE: bool
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
        ELEMENTNAME: str
        MINSIZE: float
        INTENSITY: float
        MAXSIZE: float
        AXIS: float
        QUANTITY: int
        SIDES: int
        ON: bool
        SQUEEZE: bool
        OCCLUSION: float
        PRESETS: int
        COLORSOURCE: float
        RADIALCOLOR1: MXSWrapperBase
        RADIALCOLOR2: MXSWrapperBase
        RADIALCOLOR3: MXSWrapperBase
        RADIALCOLOR4: MXSWrapperBase
        COLORRADIUS1: float
        COLORRADIUS2: float
        COLORRADIUS3: float
        COLORRADIUS4: float
        RADIALMTL: None
        USERADIALMTL: bool
        RADIALMAP: None
        USERADIALMAP: bool
        CIRCULARCOLORMIX: float
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        QUADRANT4COLOR: MXSWrapperBase
        CIRCULARMTL: None
        USECIRCULARMTL: bool
        CIRCULARMAP: None
        USECIRCULARMAP: bool
        RADIALSIZEMAP: None
        USERADIALSIZEMAP: bool
        APPLYLIGHTS: bool
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        SOURCEOBJECTID: bool
        OBJECTID: int
        SOURCEEFFECTSID: bool
        EFFECTSID: int
        SOURCEUNCLAMPEDCOLOR: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        SOURCESURFACENORMAL: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        SOURCEWHOLE: bool
        SOURCEALPHA: bool
        ALPHA: int
        SOURCEZBUFFER: bool
        ZHI: float
        ZLO: float
        FILTERALL: bool
        FILTEREDGE: bool
        FILTERPERIMETERALPHA: bool
        FILTERPERIMETER: bool
        FILTERBRIGHTNESS: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        FILTERHUE: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        APPLYNOISE: bool
        NOISEMAP: None
        RADIALDENSITY: None
        USERADIALDENSITY: bool
        ...
    class Autodesk360(Interface):
        ...
    class AutodeskMap(TextureMap):
        ...
    class AutodeskMaterial(Material):
        ...
    class AutodeskMaterialManager(Interface):
        ...
    class Autodesk_Map(TextureMap):
        ...
    class Autodesk_Material(Material):
        ...
    class AutomaticAdaptiveExposureControl(ToneOperator):
        PHYSICALSCALE: float
        CHROMATICADAPTATION: bool
        COLORDIFFERENTIATION: bool
        WHITECOLOR: MXSWrapperBase
        ACTIVE: bool
        PROCESSBG: bool
        EXPOSUREVALUE: float
        CONTRAST: float
        BRIGHTESS: float
        ...
    class AutomaticLinearExposureControl(ToneOperator):
        PHYSICALSCALE: float
        CHROMATICADAPTATION: bool
        COLORDIFFERENTIATION: bool
        WHITECOLOR: MXSWrapperBase
        ACTIVE: bool
        PROCESSBG: bool
        EXPOSUREVALUE: float
        CONTRAST: float
        BRIGHTESS: float
        ...
    class Automatic_Exposure_Control(ToneOperator):
        PHYSICALSCALE: float
        CHROMATICADAPTATION: bool
        COLORDIFFERENTIATION: bool
        WHITECOLOR: MXSWrapperBase
        ACTIVE: bool
        PROCESSBG: bool
        EXPOSUREVALUE: float
        CONTRAST: float
        BRIGHTESS: float
        ...
    class AverageSelVertCenter(Primitive):
        ...
    class AverageSelVertNormal(Primitive):
        ...
    class AvoidBehavior(ReferenceTarget):
        NAME: str
        OBSTACLES: MXSWrapperBase
        LOOKAHEAD: int
        HARDRADIUS: float
        SHOWHARDRADIUS: bool
        DETOURANGLE: float
        BRAKEPRESSURE: float
        REPELSTRENGTH: float
        REPELRADIUS: float
        REPELFALLOFF: float
        SHOWREPELRADIUS: bool
        VFIELDSTRENGTH: float
        VFIELDFALLOFF: float
        SHOWPOTENTIALCOLS: bool
        SHOWREPELACTIVITY: bool
        SHOWLOOKAHEAD: bool
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
        ...
    class Avoid_Behavior(ReferenceTarget):
        NAME: str
        OBSTACLES: MXSWrapperBase
        LOOKAHEAD: int
        HARDRADIUS: float
        SHOWHARDRADIUS: bool
        DETOURANGLE: float
        BRAKEPRESSURE: float
        REPELSTRENGTH: float
        REPELRADIUS: float
        REPELFALLOFF: float
        SHOWREPELRADIUS: bool
        VFIELDSTRENGTH: float
        VFIELDFALLOFF: float
        SHOWPOTENTIALCOLS: bool
        SHOWREPELACTIVITY: bool
        SHOWLOOKAHEAD: bool
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
        ...
    class Awning(GeometryClass):
        HEIGHT: float
        WIDTH: float
        DEPTH: float
        HORIZONTAL_FRAME_WIDTH: float
        VERTICAL_FRAME_WIDTH: float
        FRAME_THICKNESS: float
        GLAZING_THICKNESS: float
        RAIL_WIDTH: float
        NUMBER_OF_PANELS: int
        PERCENT_OPEN: int
        GENERATE_MAPPING_COORDS: bool
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
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
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
        BENDDIR: float
        BENDAXIS: int
        FROMTO: bool
        BENDFROM: float
        BENDTO: float
        ...
    class BendMod(Modifier):
        BENDANGLE: float
        BENDDIR: float
        BENDAXIS: int
        FROMTO: bool
        BENDFROM: float
        BENDTO: float
        ...
    class BendModWSM(SpacewarpObject):
        ...
    class Bevel(Modifier):
        SEGMENTS: int
        CAP_BOTTOM: int
        CAP_TOP: int
        CAP_TYPE: int
        SIDE_TYPE: int
        SMOOTH_LEVELS: int
        PRODUCE_MAPPING_COORDS: int
        KEEP_LINES_FROM_CROSSING: int
        SEPARATION_BETWEEN_LINES: float
        STARTING_OUTLINE: float
        LEVEL_1_HEIGHT: float
        LEVEL_1_OUTLINE: float
        USE_LEVEL_2: int
        LEVEL_2_HEIGHT: float
        LEVEL_2_OUTLINE: float
        USE_LEVEL_3: int
        LEVEL_3_HEIGHT: float
        LEVEL_3_OUTLINE: float
        ...
    class BevelProfileMod(Modifier):
        PRODUCE_MAPPING_COORDS: bool
        CAP_BOTTOM: bool
        CAP_TOP: bool
        CAP_TYPE: int
        KEEP_LINES_FROM_CROSSING: bool
        SEPARATION_BETWEEN_LINES: float
        CLASSICORIMPROVED: int
        EXTRUDEAMOUNT: float
        EXTRUDESEGMENTS: int
        BEVELDEPTH: float
        USEBEVELWIDTH: bool
        BEVELWIDTH: float
        BEVELSTEPS: int
        BEVELPUSH: float
        BEVELOPTIMIZE: bool
        BEVELOFFSET: float
        CAPSTART: int
        CAPSTARTCONSTRAIN: bool
        CAPEND: int
        CAPENDCONSTRAIN: bool
        CAPTYPE: int
        STARTCAPMATERIAL: int
        STARTBEVELMATERIAL: int
        SIDEMATERIAL: int
        ENDBEVELMATERIAL: int
        ENDCAPMATERIAL: int
        ...
    class BevelProfileUtilityInterface(UtilityPlugin):
        ...
    class Bevel_Profile(Modifier):
        PRODUCE_MAPPING_COORDS: bool
        CAP_BOTTOM: bool
        CAP_TOP: bool
        CAP_TYPE: int
        KEEP_LINES_FROM_CROSSING: bool
        SEPARATION_BETWEEN_LINES: float
        CLASSICORIMPROVED: int
        EXTRUDEAMOUNT: float
        EXTRUDESEGMENTS: int
        BEVELDEPTH: float
        USEBEVELWIDTH: bool
        BEVELWIDTH: float
        BEVELSTEPS: int
        BEVELPUSH: float
        BEVELOPTIMIZE: bool
        BEVELOFFSET: float
        CAPSTART: int
        CAPSTARTCONSTRAIN: bool
        CAPEND: int
        CAPENDCONSTRAIN: bool
        CAPTYPE: int
        STARTCAPMATERIAL: int
        STARTBEVELMATERIAL: int
        SIDEMATERIAL: int
        ENDBEVELMATERIAL: int
        ENDCAPMATERIAL: int
        ...
    class BezierFontLoaderClass(MAXWrapperNonRefTarg):
        ...
    class BezierShapeValue(Value):
        ...
    class Bezier_Point2(Point2Controller):
        ...
    class BiFold(GeometryClass):
        HEIGHT: float
        OPEN: float
        WIDTH: float
        DEPTH: float
        DOUBLE_DOORS: int
        FLIP_SWING: bool
        FLIP_HINGE: bool
        CREATE_FRAME: bool
        FRAME_WIDTH: float
        FRAME_DEPTH: float
        DOOR_OFFSET: float
        LEAF_THICKNESS: float
        STILES_TOP_RAIL: float
        BOTTOM_RAIL: float
        NUMBER_OF_PANELS_HORIZONTALLY: int
        NUMBER_OF_PANELS_VERTICALLY: int
        MUNTIN: float
        PANEL_TYPE: int
        GLASS_THICKNESS: float
        BEVEL_ANGLE: float
        PANEL_THICKNESS_1: float
        PANEL_THICKNESS_2: float
        PANEL_MIDDLE_THICKNESS: float
        PANEL_WIDTH_1: float
        PANEL_WIDTH_2: float
        GENERATE_MAPPING_COORDS: bool
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
        POSACTIVE: bool
        ROTACTIVE: bool
        SCALEACTIVE: bool
        KEEP: bool
        PERFRAME: bool
        ...
    class Birth(Helper):
        EMIT_START: int
        EMIT_STOP: int
        TYPE: int
        AMOUNT: int
        SUBFRAME_SAMPLING: bool
        RATE: float
        ...
    class BirthGrid(Helper):
        EMIT_TIME: int
        GRID_BASE_TYPE: int
        GRID_SIZE: float
        USE_NON_UNIFORM_GRID: bool
        GRID_WIDTH: float
        GRID_LENGTH: float
        GRID_HEIGHT: float
        USE_ALTERNATING_LATERAL_OFFSET: bool
        COMPACT_VERTICAL_SIZE: bool
        USE_RANDOM_VERTICAL_OFFSET: bool
        GRID_OFFSET: float
        RANDOM_SEED: int
        RESTRICT_BY_MESH_VOLUME: bool
        DELETE_INTERNAL_PARTICLES: bool
        REFERENCE_GEOMETRY: None
        ICON_WIDTH: float
        ICON_LENGTH: float
        ICON_HEIGHT: float
        COLOR_TYPE: bool
        UPPER_LIMIT: int
        SAVE_GRID_DATA_WITH_FILE: bool
        EXTERNAL_LAYERS: int
        INTERACTIVE_UPDATE: bool
        ...
    class BirthGroup(Helper):
        EMIT_TIME: int
        PARTICLE_OBJECTS: MXSWrapperBase
        SPLIT_BY_GROUP_MEMBERS: bool
        SPLIT_BY_CHILDREN: bool
        SPLIT_BY_ELEMENTS: bool
        ACQUIRE_SHAPES: bool
        ACQUIRE_MAPPING: bool
        ACQUIRE_MATERIAL: bool
        SUBMTL_ID_OFFSET: int
        REPORT_NODE_HANDLES: int
        HANDLES_TO_REPORT: MXSWrapperBase
        ...
    class BirthStream(Helper):
        EMIT_START: int
        EMIT_STOP: int
        RATE: float
        SEPARATION: float
        DELAY_BIRTH_IF_OVERLAP: bool
        SPEED: float
        INHERIT_ICON_MOVEMENT: bool
        MULTIPLIER: float
        RANDOM_SEED: int
        ICON_TYPE: int
        ICON_WIDTH: float
        ICON_LENGTH: float
        COLOR_TYPE: bool
        MAX_ATTEMPTS: int
        ...
    class BirthTexture(Helper):
        EMIT_START: int
        EMIT_STOP: int
        LOCK_ON_EMITTER: bool
        DATA_START: int
        DATA_STOP: int
        DELAY_VARIATION: int
        USE_LATENCY: bool
        LATENCY: int
        PRECISION: int
        EMISSION_TYPE: int
        MAXIMUM_AMOUNT: int
        MAXIMUM_RATE: float
        SEPARATE_DISTANCE: float
        ADJUST_SEPARATION_BY_SCALE_FACTOR: bool
        FAST_APPROXIMATE_SEPARATION: bool
        USE_SUBDIVISION: bool
        SUBDIVISION_LENGTH: float
        AMOUNT_LIMIT: int
        ANIMATED_SHAPE: bool
        EMISSION_BY: int
        EMISSION_RGB_CHANNELS: MXSWrapperBase
        EMISSION_TEXTURE_SUBMATERIAL_ID: int
        WHITENESS: float
        SURFACE_NORMAL_OFFSET: bool
        SURFACE_OFFSET_MINIMUM: float
        SURFACE_OFFSET_MAXIMUM: float
        SCALE_TYPE: int
        SCALE_FACTOR_SUBMTL_ID: int
        BLACK_SCALE: float
        WHITE_SCALE: float
        SHOW_PARTICLES: bool
        DISPLAY_TYPE: int
        SHOW_ONLY_WHEN_SELECTED: bool
        ICON_SIZE: float
        COLOR_COORDINATED: bool
        RANDOM_SEED: int
        EMITTER_OBJECTS: MXSWrapperBase
        ...
    class Birth_File(Helper):
        PARTICLE_FILE: str
        PARTICLE_FILE_VALID: bool
        FILE_NB_FRAMES: int
        FILE_START: int
        FILE_END: int
        FILE_RATE: float
        FILE_CHANNEL_MASK: int
        FILETIME: int
        DATAFILE_THISFRAME: None
        NB_PARTICLES_THISFRAME: int
        RANGE_TYPE: int
        RANGE_START: int
        RANGE_END: int
        EMIT_START: int
        SPEED_FACTOR: float
        EXTRAPOLATION_TYPE: int
        USE_POSITION_CHANNEL: bool
        USE_ORIENTATION_CHANNEL: bool
        ORIENTATION_UP_VECTOR: int
        USE_SCALE_CHANNEL: bool
        USE_SPEED_CHANNEL: bool
        USE_COLOR_CHANNEL: bool
        COLOR_MAP_CHANNEL: int
        USE_OPACITY_CHANNEL: bool
        OPACITY_MAP_CHANNEL: int
        ...
    class Birth_Group(Helper):
        EMIT_TIME: int
        PARTICLE_OBJECTS: MXSWrapperBase
        SPLIT_BY_GROUP_MEMBERS: bool
        SPLIT_BY_CHILDREN: bool
        SPLIT_BY_ELEMENTS: bool
        ACQUIRE_SHAPES: bool
        ACQUIRE_MAPPING: bool
        ACQUIRE_MATERIAL: bool
        SUBMTL_ID_OFFSET: int
        REPORT_NODE_HANDLES: int
        HANDLES_TO_REPORT: MXSWrapperBase
        ...
    class Birth_Paint(Helper):
        PARTICLE_PAINT_HELPER: None
        EMIT_START: int
        EMIT_TYPE: int
        EMIT_STOP: int
        DURATION: int
        SUBFRAME_SAMPLING: bool
        LOCK_POSITION: bool
        LOCK_ROTATION: bool
        ACQUIRE_SELECTION: bool
        SELECTION_TYPE: int
        ...
    class Birth_Script(Helper):
        RANDOM_SEED: int
        PROCEED_SCRIPT: str
        EMIT_START: int
        ...
    class Birth_Texture(Helper):
        EMIT_START: int
        EMIT_STOP: int
        LOCK_ON_EMITTER: bool
        DATA_START: int
        DATA_STOP: int
        DELAY_VARIATION: int
        USE_LATENCY: bool
        LATENCY: int
        PRECISION: int
        EMISSION_TYPE: int
        MAXIMUM_AMOUNT: int
        MAXIMUM_RATE: float
        SEPARATE_DISTANCE: float
        ADJUST_SEPARATION_BY_SCALE_FACTOR: bool
        FAST_APPROXIMATE_SEPARATION: bool
        USE_SUBDIVISION: bool
        SUBDIVISION_LENGTH: float
        AMOUNT_LIMIT: int
        ANIMATED_SHAPE: bool
        EMISSION_BY: int
        EMISSION_RGB_CHANNELS: MXSWrapperBase
        EMISSION_TEXTURE_SUBMATERIAL_ID: int
        WHITENESS: float
        SURFACE_NORMAL_OFFSET: bool
        SURFACE_OFFSET_MINIMUM: float
        SURFACE_OFFSET_MAXIMUM: float
        SCALE_TYPE: int
        SCALE_FACTOR_SUBMTL_ID: int
        BLACK_SCALE: float
        WHITE_SCALE: float
        SHOW_PARTICLES: bool
        DISPLAY_TYPE: int
        SHOW_ONLY_WHEN_SELECTED: bool
        ICON_SIZE: float
        COLOR_COORDINATED: bool
        RANDOM_SEED: int
        EMITTER_OBJECTS: MXSWrapperBase
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
        CLIPU: float
        CLIPV: float
        CLIPW: float
        CLIPH: float
        JITTER: float
        USEJITTER: bool
        APPLY: bool
        CROPPLACE: int
        FILTERING: int
        MONOOUTPUT: int
        RGBOUTPUT: int
        ALPHASOURCE: int
        PREMULTALPHA: bool
        BITMAP: None
        COORDS: MXSWrapperBase
        OUTPUT: MXSWrapperBase
        FILENAME: str
        STARTTIME: MXSWrapperBase
        PLAYBACKRATE: float
        ENDCONDITION: int
        TIETIMETOMATIDS: bool
        ...
    class Blackman(Filter):
        ...
    class Blend(Material):
        MIXAMOUNT: float
        LOWER: float
        UPPER: float
        USECURVE: bool
        INTERACTIVE: int
        MAP1: MXSWrapperBase
        MAP2: MXSWrapperBase
        MASK: None
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        MASKENABLED: bool
        ...
    class BlendFragment(GraphicsFragmentPlugin):
        ...
    class BlendMap(BakeElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        BACKGROUNDCOLOR: MXSWrapperBase
        LIGHTINGON: bool
        SHADOWSON: bool
        DIFFUSEON: bool
        AMBIENTON: bool
        SPECULARON: bool
        EMISSIONON: bool
        REFLECTIONON: bool
        REFRACTIONON: bool
        TARGETMAPSLOTNAME: str
        ...
    class BlendRenderElement(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ATMOSPHEREON: bool
        SHADOWON: bool
        DIFFUSEON: bool
        AMBIENTON: bool
        SPECULARON: bool
        EMISSIONON: bool
        REFLECTIONON: bool
        REFRACTIONON: bool
        INKON: bool
        PAINTON: bool
        ...
    class BlendedBoxMap(TextureMap):
        COORDS: MXSWrapperBase
        MODE: int
        COLORS: MXSWrapperBase
        TEX: MXSWrapperBase
        MAPENABLED: MXSWrapperBase
        MAPSCALE: float
        BLEND: float
        TEXTURESPACE: int
        NODE: None
        POSU: float
        POSV: float
        POSU2: float
        POSV2: float
        POSLOCK: bool
        ROTA: float
        ROTB: float
        ROTC: float
        ROTA2: float
        ROTB2: float
        ROTC2: float
        ROTLOCK: bool
        SCALEU: float
        SCALEV: float
        SCALEU2: float
        SCALEV2: float
        SCALELOCK: bool
        USERANDOM: bool
        SEED: int
        RENDERRESOLUTION: int
        FORSEED: int
        RANDX: bool
        RANDY: bool
        RANDZ: bool
        CUBE: bool
        CUBEMODE: int
        LOCKTOFRAME: bool
        LOCKFRAME: int
        BLENDMAPSTRENGTH: float
        CUBESIZE: float
        CUBENODE: None
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
        SIZE: float
        SEED: int
        SPEED: float
        MAPPINGTYPE: int
        VIEWTYPE: int
        VIEWPERCENT: float
        EMITTERHIDDEN: bool
        QUANTITYMETHOD: int
        PARTICLETYPE: int
        STANDARDPARTICLE: int
        METABALLRENDERCOARSNESS: float
        METABALLVIEWCOARSNESS: float
        METABALLAUTOCOARSNESS: bool
        INSTANCESUBTREE: bool
        INSTANCEKEYOFFSETTYPE: int
        INSTANCEFRAMEOFFSET: int
        MATERIALSOURCE: int
        SPINAXISTYPE: int
        SPAWNTYPE: int
        SPAWNSPEEDTYPE: int
        SPAWNINHERITVELOCITY: bool
        SPAWNSPEEDFIXED: bool
        SPAWNSCALETYPE: int
        SPAWNSCALEFIXED: bool
        MOTIONINFLUENCE: float
        MOTIONMULTIPLIER: float
        MOTIONVARIATION: float
        INSTANCINGOBJECT: None
        LIFESPANVALUEQUEUE: MXSWrapperBase
        OBJECTMUTATIONQUEUE: MXSWrapperBase
        SUBSAMPLEEMITTERTRANSLATION: bool
        SUBSAMPLEEMITTERROTATION: bool
        SUBSAMPLECREATIONTIME: bool
        LIFE: MXSWrapperBase
        TUMBLE: float
        TUMBLE_RATE: float
        EMITTER_LENGTH: float
        SPEED_VARIATION: float
        BIRTH_RATE: int
        TOTAL_NUMBER: int
        EMITTER_START: MXSWrapperBase
        EMITTER_STOP: MXSWrapperBase
        DISPLAY_UNTIL: MXSWrapperBase
        LIFE_VARIATION: MXSWrapperBase
        SIZE_VARIATION: float
        GROWTH_TIME: MXSWrapperBase
        FADE_TIME: MXSWrapperBase
        EMITTER_WIDTH: float
        METAPARTICLE_TENSION: float
        METAPARTICLE_TENSION_VARIATION: float
        MAPPING_TIME_BASE: MXSWrapperBase
        MAPPING_DISTANCE_BASE: float
        SPIN_TIME: MXSWrapperBase
        SPIN_TIME_VARIATION: float
        SPIN_PHASE: float
        SPIN_PHASE_VARIATION: float
        X_SPIN_VECTOR: float
        Y_SPIN_VECTOR: float
        Z_SPIN_VECTOR: float
        SPIN_AXIS_VARIATION: float
        SPAWN_DIRECTION_CHAOS: float
        SPAWN_SPEED_CHAOS: float
        SPAWN_SCALE_CHAOS: float
        SPAWN_AFFECTS: int
        SPAWN_MULTIPLIER_VARIATION: float
        BUBBLE_PHASE_VARIATION: int
        DIE__X_FRAMES_AFTER_COLLISION: MXSWrapperBase
        DIE__X_FRAMES_AFTER_COLLISION_VARIATION: float
        INTERPARTICLE_COLLISIONS_ON: int
        INTERPARTICLE_COLLISION_STEPS: int
        INTERPARTICLE_COLLISION_BOUNCE: float
        INTERPARTICLE_COLLISION_BOUNCE_VARIATION: float
        ...
    class BlobMesh(GeometryClass):
        SIZE: float
        TENSION: float
        RENDERCOARSENESS: float
        VIEWPORTCOARSENESS: float
        RELATIVECOARSENESS: bool
        NODELIST: MXSWrapperBase
        USESOFTSELECTION: bool
        MINSIZE: float
        LARGEDATASETOPTIMIZATION: bool
        USEALLPFEVENTS: bool
        PFEVENTLIST: MXSWrapperBase
        OFFINVIEW: bool
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
        GROUPRESULTS: bool
        STOCKOUTSIDE: bool
        STOCKINSIDE: bool
        CUTTEROUTSIDE: bool
        ...
    class Body_Join(GeometryClass):
        BREPOPERATION: int
        MAKEINTOSOLID: bool
        TOBREPOBJECTHELP: bool
        ...
    class Body_Object(GeometryClass):
        ...
    class Body_Utility(GeometryClass):
        SHOWRESULTOP: bool
        SHOWALLOPERANDSOP: bool
        OP_NOT_USED1: int
        OP_NOT_USED2: bool
        TWOSIDEDMESHESOP: bool
        OP_NOT_USED3: bool
        OP_NOT_USED4: bool
        SAVEBREPSOP: bool
        SHOWSELECTEDOPERANDSOP: bool
        FASTEDITOP: bool
        RENDERRADIORA: int
        FACEAPPROXANGLERA: float
        EDGEAPPROXANGLERA: float
        FACECHORDRA: float
        EDGECHORDRA: float
        MAXEDGERA: float
        LOWQUALITYRA: bool
        MEDIUMQUALITYRA: bool
        HIGHQUALITYRA: bool
        WELDANDSMOOTHRA: bool
        SAVERENDERMESHRA: bool
        RENDERVIEWPORTMESHRA: bool
        FILLETALLEDGESFAO: bool
        FIRSTORENDEDGESFAO: bool
        SECONDORSIDEEDGESFAO: bool
        THIRDORSTARTEDGESFAO: bool
        FAO_NOT_USED1: bool
        FAO_NOT_USED2: bool
        FAO_NOT_USED3: bool
        FILLETRADIUSFAO: float
        APPROXIMATEARCFAO: bool
        CONSTANTDISTANCEFAO: bool
        LINEARCROSSSECTIONFAO: bool
        SHELLSTARTFACEFAO: bool
        SHELLENDFACEFAO: bool
        SHELLRADIOFAO: int
        OFFSETRADIUSFAO: float
        FAO_NOT_USED4: bool
        CORNEREXTENSIONFAO: bool
        SECTIONTYPEFAO: int
        BLENDSTRENGTHFAO: float
        DISPLAYRADIOVDS: int
        VDS_NOT_USED1: bool
        ULINESVDS: float
        VLINESVDS: float
        ISOANGLEDS: float
        ISOCHORDHEIGHTVDS: float
        FACEAPPROXANGLEVDS: float
        EDGEAPPROXANGLEVDS: float
        FACECHORDHEIGHTVDS: float
        EDGECHORDHEIGHTVDS: float
        MAXEDGELENGTHPCTVDS: float
        CLEANMESHVDS: bool
        SUBDMESHVDS: bool
        LOWQUALITYVDS: bool
        MEDIUMQUALITYVDS: bool
        HIGHQUALITYVDS: bool
        DISPLAYSURFACEKNOTSVDS: bool
        SMOOTHINGPASSESVDS: float
        DISPLAYCONTROLPOINTSSA: bool
        DISPLAYCONTROLMESHSA: bool
        DISPLAYCURVECURVATURESA: bool
        CURVECURVATURETYPESA: int
        CURVATURESCALESA: float
        CURVATUREDENSITYSA: float
        DISPLAYSURFACECURVATURESA: bool
        SURFACECURVATURETYPESA: int
        STDDEVMULTIPLESSA: float
        USEMINMAXRANGESA: bool
        STDDEVMINRANGESA: float
        STDDEVMAXRANGESA: float
        SURFANALYSISQUICKHELPSA: bool
        NQ_NOT_USED1: bool
        NQ_NOT_USED2: bool
        EXTRTOBREPNQ: bool
        EXTRTONURBSNQ: bool
        EXTRTOCURVENQ: bool
        NQ_NOT_USED3: bool
        NQ_NOT_USED4: bool
        NQ_NOT_USED5: bool
        ...
    class Bomb(SpacewarpObject):
        SEED: int
        SPIN: float
        GRAVITY: float
        FALLOFF: float
        STRENGTH: float
        CHAOS: float
        DETONATION: MXSWrapperBase
        FALLOFFENABLE: bool
        MINFRAGMENTSIZE: int
        MAXFRAGMENTSIZE: int
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
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINLENGTH: float
        TYPEINWIDTH: float
        TYPEINHEIGHT: float
        LENGTH: float
        WIDTH: float
        HEIGHT: float
        WIDTHSEGS: int
        LENGTHSEGS: int
        HEIGHTSEGS: int
        MAPCOORDS: bool
        ...
    class Box2(Value):
        ...
    class Box3(Value):
        ...
    class BoxGizmo(Helper):
        HEIGHT: float
        LENGTH: float
        WIDTH: float
        SEED: int
        ...
    class BoxPickNode(Primitive):
        ...
    class Box_2_Global_Utility(GlobalUtilityPlugin):
        ...
    class Bricks(TextureMap):
        BRICKS: None
        MORTAR_MAP: None
        BRICKS_MAP: None
        MORTAR: None
        RANDOM_SEED: int
        MORTAR_COLOR: MXSWrapperBase
        BRICK_COLOR: MXSWrapperBase
        HORIZONTAL_COUNT: float
        VERTICAL_COUNT: float
        COLOR_VARIANCE: float
        VERTICAL_GAP: float
        HORIZONTAL_GAP: float
        LINE_SHIFT: float
        RANDOM_SHIFT: float
        HOLES: int
        LOCK_GAP_SYMMETRY: int
        FADE_VARIANCE: float
        EDGE_ROUGHNESS: float
        SHOW_TEXTURE_SWATCHES: int
        USE_ROW_EDIT: int
        USE_COLUMN_EDIT: int
        CHANGE_ROW: float
        CHANGE_COLUMN: float
        PER_COLUMN: int
        PER_ROW: int
        TILE_TYPE: int
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
        X_COL: int
        Y_COL: int
        Z_COL: int
        NUM_SAMPLES: int
        RED_AMOUNT: float
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class CFDImportData(GeometryClass):
        WELD_DST: float
        FORCE_RELOAD_SIGNAL: bool
        NBHEADERLINES: int
        NBBOTTOMLINES: int
        CSV_FILE: str
        SEPARATOR: str
        DEFAULT_VALUE: float
        X_POS__CHN: int
        Y_POS__CHN: int
        Z_POS__CHN: int
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class CFDInterpOnSpline(GeometryClass):
        SPLINES: None
        AMOUNT: float
        RED_AMOUNT: float
        CLONE: None
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class CFDKeepNVertices(Modifier):
        N: int
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class CFDSplineNode(Shape):
        BAKESPLINE_SIGNAL: bool
        CFD_POINTS: None
        SPLINE_ORIGIN_HELPER: None
        SPLINE_VERTICES: int
        REFRESH_DATA_SIGNAL: bool
        FIELD_INTERPOLATION: int
        SMOOTHING: float
        FIELD_SAMPLING: float
        MATERIAL_ID_COUNT: int
        MATERIAL_ANIMATION: int
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class CFDSplinePaths(Shape):
        PROFILE: None
        DISABLE: bool
        NUM_STEPS: int
        CFDIMPORT_OBJECT: None
        X_COL: int
        Y_COL: int
        Z_COL: int
        NUM_SAMPLES: int
        STEP_SIZE: float
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class CFDVelocityField(GeometryClass):
        CFDIMPORT_OBJECT: None
        X_COL: int
        Y_COL: int
        Z_COL: int
        ARROW_SCALE: float
        NORMALIZED_LENGTHS: bool
        MIN_LENGTH: float
        MAX_LENGTH: float
        RED_AMOUNT: float
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class CFDVertexPaintChannel(Modifier):
        UPDATE_CACHES: bool
        CFDPOINTS: None
        NBCLOSEST: int
        SMOOTH_FACTOR: float
        CHANNELID: int
        LOCAL_NORM: bool
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class CFDVertexPaintVelocity(Modifier):
        UPDATE_CACHES: bool
        CFDPOINTS: None
        NBCLOSEST: int
        SMOOTH_FACTOR: float
        VX_CHN: int
        VY_CHN: int
        VZ_CHN: int
        LOCAL_NORM: bool
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
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
        RENDER_THICKNESS: float
        RENDER_SIDES: int
        RENDER_ANGLE: float
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        RENDER_WIDTH: float
        RENDER_LENGTH: float
        RENDER_ANGLE2: float
        RENDER_THRESHOLD: float
        ...
    class CV_Curveshape(Shape):
        ...
    class CV_Surf(GeometryClass):
        ...
    class C_Ext(GeometryClass):
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINBACKLENGTH: float
        TYPEINSIDELENGTH: float
        TYPEINFRONTLENGTH: float
        TYPEINBACKWIDTH: float
        TYPEINSIDEWIDTH: float
        TYPEINFRONTWIDTH: float
        TYPEINHEIGHT: float
        BACK_LENGTH: float
        SIDE_LENGTH: float
        FRONT_LENGTH: float
        BACK_WIDTH: float
        SIDE_WIDTH: float
        FRONT_WIDTH: float
        HEIGHT: float
        BACK_SEGMENTS: int
        SIDE_SEGMENTS: int
        FRONT_SEGMENTS: int
        WIDTH_SEGMENTS: int
        HEIGHT_SEGMENTS: int
        MAPCOORDS: bool
        CENTERCREATE: bool
        ...
    class Cache(Helper):
        USE_AT: int
        UPDATE_TYPE: int
        CACHE_TEST_RESULTS: bool
        RANGE_TYPE: int
        START_TIME: MXSWrapperBase
        END_TIME: MXSWrapperBase
        SAMPLING_TYPE: int
        EVERY_NTH_FRAME: int
        CACHE_WITH_FILE: bool
        CACHE_WITH_HOLD: bool
        CLEAR_RANGE_TYPE: int
        CLEAR_START_TIME: MXSWrapperBase
        CLEAR_END_TIME: MXSWrapperBase
        UPDATE_VIEWPORTS: bool
        MEMORY_LIMIT: int
        MEMORY_TOTAL: int
        MEMORY_FOR_CURRENT_FRAME: int
        ...
    class CacheDisk(Helper):
        USE_AT: int
        RANGE_TYPE: int
        START_TIME: MXSWrapperBase
        END_TIME: MXSWrapperBase
        SAMPLING_TYPE: int
        EVERY_NTH_FRAME: int
        CACHE_TEST_RESULTS: bool
        WRITE_TO_FILE: None
        UPDATE_CLEAR_RANGE_TYPE: int
        UPDATE_CLEAR_START_TIME: MXSWrapperBase
        UPDATE_CLEAR_END_TIME: MXSWrapperBase
        UPDATE_VIEWPORTS: bool
        EXCLUDE_SHAPE: bool
        EXCLUDE_SCALE: bool
        EXCLUDE_MAPPING: bool
        EXCLUDE_SCRIPT_DATA: bool
        EXCLUDE_MATERIAL_ID: bool
        EXCLUDE_ROTATION: bool
        USE_POST_CACHE_OPERATORS: bool
        POST_CACHE_OPERATORS: MXSWrapperBase
        MEMORY_LIMIT: int
        ...
    class CacheFile(ReferenceTarget):
        ...
    class CacheSelective(Helper):
        USE_AT: int
        RANGE_TYPE: int
        START_TIME: MXSWrapperBase
        END_TIME: MXSWrapperBase
        SAMPLING_TYPE: int
        EVERY_NTH_FRAME: int
        CACHE_TEST_RESULTS: bool
        SAVE_CACHE_WITH_FILE: bool
        SAVE_CACHE_WITH_HOLD: bool
        UPDATE_CLEAR_RANGE_TYPE: int
        UPDATE_CLEAR_START_TIME: MXSWrapperBase
        UPDATE_CLEAR_END_TIME: MXSWrapperBase
        UPDATE_VIEWPORTS: bool
        EXCLUDE_SHAPE: bool
        EXCLUDE_SCALE: bool
        EXCLUDE_MAPPING: bool
        EXCLUDE_SCRIPT_DATA: bool
        EXCLUDE_MATERIAL_ID: bool
        EXCLUDE_ROTATION: bool
        USE_POST_CACHE_OPERATORS: bool
        POST_CACHE_OPERATORS: MXSWrapperBase
        MEMORY_LIMIT: int
        ...
    class CacheSubGraphOutputFragment(GraphicsFragmentPlugin):
        ...
    class Cache_Disk(Helper):
        USE_AT: int
        RANGE_TYPE: int
        START_TIME: MXSWrapperBase
        END_TIME: MXSWrapperBase
        SAMPLING_TYPE: int
        EVERY_NTH_FRAME: int
        CACHE_TEST_RESULTS: bool
        WRITE_TO_FILE: None
        UPDATE_CLEAR_RANGE_TYPE: int
        UPDATE_CLEAR_START_TIME: MXSWrapperBase
        UPDATE_CLEAR_END_TIME: MXSWrapperBase
        UPDATE_VIEWPORTS: bool
        EXCLUDE_SHAPE: bool
        EXCLUDE_SCALE: bool
        EXCLUDE_MAPPING: bool
        EXCLUDE_SCRIPT_DATA: bool
        EXCLUDE_MATERIAL_ID: bool
        EXCLUDE_ROTATION: bool
        USE_POST_CACHE_OPERATORS: bool
        POST_CACHE_OPERATORS: MXSWrapperBase
        MEMORY_LIMIT: int
        ...
    class Cache_Selective(Helper):
        USE_AT: int
        RANGE_TYPE: int
        START_TIME: MXSWrapperBase
        END_TIME: MXSWrapperBase
        SAMPLING_TYPE: int
        EVERY_NTH_FRAME: int
        CACHE_TEST_RESULTS: bool
        SAVE_CACHE_WITH_FILE: bool
        SAVE_CACHE_WITH_HOLD: bool
        UPDATE_CLEAR_RANGE_TYPE: int
        UPDATE_CLEAR_START_TIME: MXSWrapperBase
        UPDATE_CLEAR_END_TIME: MXSWrapperBase
        UPDATE_VIEWPORTS: bool
        EXCLUDE_SHAPE: bool
        EXCLUDE_SCALE: bool
        EXCLUDE_MAPPING: bool
        EXCLUDE_SCRIPT_DATA: bool
        EXCLUDE_MATERIAL_ID: bool
        EXCLUDE_ROTATION: bool
        USE_POST_CACHE_OPERATORS: bool
        POST_CACHE_OPERATORS: MXSWrapperBase
        MEMORY_LIMIT: int
        ...
    class Caddy(GlobalUtilityPlugin):
        ...
    class CallbackFn1(MAXScriptFunction):
        ...
    class CamMatchDataCustAttrib(CustAttrib):
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
        VIEWPORT_SIZE_X: int
        VIEWPORT_SIZE_Y: int
        AXIS_MODE: int
        ...
    class CamPerspCorrect(Modifier):
        PARAMPERSPECTCORRECTAMOUNT: float
        PARAMPERSPECTCORRECTDIR: float
        ...
    class CamPoint(Helper):
        SHOWAXIS: bool
        AXISLENGTH: float
        ...
    class CameraCulling(Helper):
        USE_ACTIVE_CAMERA: bool
        CAMERA: None
        USE_CAMERA_CLIPPING_PLANES: bool
        USE_NEAR_CLIP: bool
        NEAR_CLIP_DISTANCE: float
        USE_FAR_CLIP: bool
        FAR_CLIP_DISTANCE: float
        CULLING_TYPE: int
        RENDER_CULLING: bool
        VIEWPORT_CULLING: bool
        USE_FOR_GROUP_SELECTION: bool
        SELECTION_TYPE: int
        SUBFRAME_PRECISION: bool
        ...
    class CameraMBlur(Helper):
        USE_ACTIVE_CAMERA: bool
        CAMERA: None
        USE_EVENT_MULTIPLIER: bool
        MULTIPLIER: float
        ...
    class CameraMap(Modifier):
        ...
    class CameraMapSpaceWarp(SpacewarpObject):
        ...
    class CameraMapTexture(TextureMap):
        CAMERA: None
        MAPCHANNEL: int
        TEXTURE: None
        BACKFACE: bool
        USEZBUFFER: bool
        ZBUFFER: None
        ZFUDGE: float
        ANGLETHRESHOLD: float
        MASK: None
        USEMASK: bool
        MASKUSESPROJECTION: bool
        AFFECTBEHINDCAM: bool
        ASPECTMODE: int
        HASPECT: float
        VASPECT: float
        ...
    class Camera_Culling(Helper):
        USE_ACTIVE_CAMERA: bool
        CAMERA: None
        USE_CAMERA_CLIPPING_PLANES: bool
        USE_NEAR_CLIP: bool
        NEAR_CLIP_DISTANCE: float
        USE_FAR_CLIP: bool
        FAR_CLIP_DISTANCE: float
        CULLING_TYPE: int
        RENDER_CULLING: bool
        VIEWPORT_CULLING: bool
        USE_FOR_GROUP_SELECTION: bool
        SELECTION_TYPE: int
        SUBFRAME_PRECISION: bool
        ...
    class Camera_IMBlur(Helper):
        USE_ACTIVE_CAMERA: bool
        CAMERA: None
        USE_EVENT_MULTIPLIER: bool
        MULTIPLIER: float
        ...
    class Camera_Map_Per_Pixel(TextureMap):
        CAMERA: None
        MAPCHANNEL: int
        TEXTURE: None
        BACKFACE: bool
        USEZBUFFER: bool
        ZBUFFER: None
        ZFUDGE: float
        ANGLETHRESHOLD: float
        MASK: None
        USEMASK: bool
        MASKUSESPROJECTION: bool
        AFFECTBEHINDCAM: bool
        ASPECTMODE: int
        HASPECT: float
        VASPECT: float
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
        SMOOTH: bool
        RADIUS: float
        SIDES: int
        MAPCOORDS: bool
        SLICEON: bool
        HEIGHTTYPE: int
        HEIGHTSEGS: int
        SLICEFROM: float
        SLICETO: float
        ...
    class CaptureAnimation(MAXScriptFunction):
        ...
    class CaptureCallStack(Primitive):
        ...
    class Captured_Object_State(ReferenceTarget):
        ...
    class Casement(GeometryClass):
        HEIGHT: float
        WIDTH: float
        DEPTH: float
        PANEL_WIDTH: float
        NUMBER_OF_CASEMENTS: int
        OPENS_TO_INSIDE: bool
        HORIZONTAL_FRAME_WIDTH: float
        VERTICAL_FRAME_WIDTH: float
        FRAME_THICKNESS: float
        GLAZING_THICKNESS: float
        PERCENT_OPEN: int
        GENERATE_MAPPING_COORDS: bool
        ...
    class Catmull_Rom(Filter):
        ...
    class Cellular(TextureMap):
        CELLCOLOR: MXSWrapperBase
        DIVCOLOR1: MXSWrapperBase
        DIVCOLOR2: MXSWrapperBase
        CELLMAP: None
        DIVMAP1: None
        DIVMAP2: None
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        MAP3ENABLED: bool
        VARIATION: float
        SIZE: float
        SPREAD: float
        LOWTHRESH: float
        MIDTHRESH: float
        HIGHTHRESH: float
        TYPE: int
        FRACTAL: bool
        ITERATION: float
        ROUGHNESS: float
        SMOOTH: float
        ADAPTIVE: bool
        COORDS: MXSWrapperBase
        OUTPUT: MXSWrapperBase
        ...
    class CenterObject(MappedPrimitive):
        ...
    class CenterPivot(MappedPrimitive):
        ...
    class Chair(GeometryClass):
        GENDER: int
        MOTIONSEED: int
        ID: int
        SINGLE: bool
        HEIGHT: float
        ...
    class Chamfer(Modifier):
        AMOUNT: float
        SEGMENTS: int
        TENSION: float
        OPENCHAMFER: bool
        INVERT: bool
        SELECTIONOPTION: int
        SMOOTHINGOPTION: int
        MATERIALOPTION: int
        SETMATERIAL: bool
        MATERIALID: int
        SMOOTH: bool
        SMOOTHTYPE: int
        SMOOTHTHRESHOLD: float
        CHAMFERTYPE: int
        LIMITEFFECT: bool
        USEMINANGLE: bool
        MINANGLE: float
        USEMAXANGLE: bool
        MAXANGLE: float
        SMOOTHTOADJACENT: bool
        QUADINTERSECTIONMODE: bool
        MITERINGTYPE: int
        AMOUNTTYPE: int
        MINAMOUNT: float
        MAXAMOUNT: float
        ADDINSET: bool
        INSETAMOUNT: float
        INSETSEGMENTS: int
        INSETOFFSET: float
        FORCEPOSITIVEOFFSET: bool
        MITERENDBIAS: float
        USECONSTANTOFFSET: bool
        DEPTH: float
        PRESETOPTIONSCOMBOBOX: int
        RADIUSBIAS: float
        BIASENDPOINTS: bool
        SCALE: float
        DEPTHTYPE: int
        INSETTYPE: int
        ANGLEFACTORVERTEX: float
        ...
    class ChamferBox(GeometryClass):
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINLENGTH: float
        TYPEINWIDTH: float
        TYPEINHEIGHT: float
        TYPEINFILLET: float
        LENGTH: float
        WIDTH: float
        HEIGHT: float
        FILLET: float
        LENGTH_SEGMENTS: int
        WIDTH_SEGMENTS: int
        HEIGHT_SEGMENTS: int
        FILLET_SEGMENTS: int
        MAPCOORDS: bool
        SMOOTH: bool
        ...
    class ChamferCyl(GeometryClass):
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS: float
        TYPEINHEIGHT: float
        TYPEINFILLET: float
        RADIUS: float
        HEIGHT: float
        FILLET: float
        HEIGHT_SEGMENTS: int
        FILLET_SEGMENTS: int
        SIDES: int
        CAP_SEGMENTS: int
        SMOOTH_ON: bool
        SLICE_ON: bool
        SLICE_FROM: float
        SLICE_TO: float
        MAPCOORDS: bool
        ...
    class ChamferMod(Modifier):
        AMOUNT: float
        SEGMENTS: int
        TENSION: float
        OPENCHAMFER: bool
        INVERT: bool
        SELECTIONOPTION: int
        SMOOTHINGOPTION: int
        MATERIALOPTION: int
        SETMATERIAL: bool
        MATERIALID: int
        SMOOTH: bool
        SMOOTHTYPE: int
        SMOOTHTHRESHOLD: float
        CHAMFERTYPE: int
        LIMITEFFECT: bool
        USEMINANGLE: bool
        MINANGLE: float
        USEMAXANGLE: bool
        MAXANGLE: float
        SMOOTHTOADJACENT: bool
        QUADINTERSECTIONMODE: bool
        MITERINGTYPE: int
        AMOUNTTYPE: int
        MINAMOUNT: float
        MAXAMOUNT: float
        ADDINSET: bool
        INSETAMOUNT: float
        INSETSEGMENTS: int
        INSETOFFSET: float
        FORCEPOSITIVEOFFSET: bool
        MITERENDBIAS: float
        USECONSTANTOFFSET: bool
        DEPTH: float
        PRESETOPTIONSCOMBOBOX: int
        RADIUSBIAS: float
        BIASENDPOINTS: bool
        SCALE: float
        DEPTHTYPE: int
        INSETTYPE: int
        ANGLEFACTORVERTEX: float
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
        ICONSIZE: int
        DISPLAYRES: int
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
        SOFTEN: float
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1: None
        MAP2: None
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        COORDS: MXSWrapperBase
        ...
    class Circle(Shape):
        STEPS: int
        RADIUS: float
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        ...
    class CirclePickNode(Primitive):
        ...
    class CivilView_Alignment(Shape):
        STARTSTATION: float
        ENDSTATION: float
        CURRENTDATASET: int
        DATASETNAMEARRAY: MXSWrapperBase
        DATASETSIZEARRAY: MXSWrapperBase
        XYZSTATIONARRAY: MXSWrapperBase
        RADBEARGRADEARRAY: MXSWrapperBase
        ALIGNENTTYPEARRAY: MXSWrapperBase
        PROFILEENTTYPEARRAY: MXSWrapperBase
        ISALIGNENTSTARTEND: MXSWrapperBase
        ISPROFILEENTSTARTEND: MXSWrapperBase
        DESIGNSPEEDCOMMENTS: MXSWrapperBase
        DESIGNSPEEDSTATIONS: MXSWrapperBase
        DESIGNSPEEDVALUES: MXSWrapperBase
        ...
    class CivilView_Pipe(Shape):
        DISPLAYNAME: str
        DESCRIPTION: str
        PARTDESCRIPTION: str
        PARTSIZENAME: str
        PARTSUBTYPE: str
        STARTSTRUCTUREHANDLE: str
        ENDSTRUCTUREHANDLE: str
        HORTYPE: int
        PSETYPE: int
        FLOWDIRECTION: int
        FLOWDIRECTIONMETHOD: int
        CROSSSECTIONALSHAPE: int
        BEARING: float
        RADIUS: float
        SLOPE: float
        INNERDIAMETERORWIDTH: float
        INNERHEIGHT: float
        OUTERDIAMETERORWIDTH: float
        OUTERHEIGHT: float
        MINIMUMCOVER: float
        MAXIMUMCOVER: float
        LENGTH2DCENTERTOCENTER: float
        LENGTH3DCENTERTOCENTER: float
        LENGTH2DTOINSIDEEDGE: float
        LENGTH3DTOINSIDEEDGE: float
        ...
    class Civil_Structure(GeometryClass):
        TYPE: int
        FRAME_TYPE: int
        STRUCTURE_WIDTHORDIA: float
        STRUCTURE_LENGTH: float
        STRUCTURE_HEIGHT: float
        FRAME_WIDTHORDIA: float
        FRAME_LENGTH: float
        FRAME_HEIGHT: float
        CONE_WIDTHORDIA: float
        CONE_LENGTH: float
        CONE_HEIGHT: float
        FLOOR_THICKNESS: float
        WALL_THICKNESS: float
        RIM_THICKNESS: float
        CONCENTRIC_OFFSET_X: float
        CONCENTRIC_OFFSET_Y: float
        USE_MATID: bool
        MAPCOORDS: bool
        DISPLAYNAME: None
        NETWORKNAME: None
        NETWORKID: None
        COVER: None
        FRAME: None
        GRATE: None
        MATERIALNAME: None
        PARTDEFID: None
        PARTDESC: None
        PARTSIZENAME: None
        PARTSUBTYPE: None
        CONNECTEDPARTCOUNT: int
        CONNECTEDPIPESCOUNT: int
        PARTTYPE: int
        BARRELPIPECLEARANCE: float
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
        GRAVITY: float
        SELFCOLLISION: bool
        SOLIDCOLLISION: bool
        SCALE: float
        USESEWINGSPRINGS: bool
        STARTFRAME: int
        TIMESTEP: float
        SHOWSEWINGSPRINGS: bool
        SUBSAMPLE: int
        ENDFRAME: int
        ENABLEENDFRAME: bool
        CHECKINTERSECTIONS: bool
        CLOTHCLOTHMETHOD: int
        USEGRAVITY: bool
        SIMONRENDER: bool
        SIMPRIORITY: int
        ADVANCEDPINCHING: bool
        RELATIVEVELOCITY: float
        TIMESCALE: float
        IGNOREBACKFACING: bool
        SIMONMOUSEDOWN: bool
        SHOWCURRENTSTATE: bool
        SHOWTARGETSTATE: bool
        SHOWENABLEDSOLIDCOLLISION: bool
        SHOWENABLEDCLOTHCOLLISION: bool
        SHOWTENSION: bool
        TENSIONSCALE: float
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
        COLLISION_NODES: MXSWrapperBase
        TEST_TYPE: int
        SPEED_OPTION: int
        MIN_SPEED: float
        MAX_SPEED: float
        RANDOM_SEED: int
        WILL_COLLIDE_FRAME: int
        COLLISION_COUNT: int
        COLLISION_COUNT_OPTIONS: int
        ...
    class Collision_Spawn(Helper):
        TRUE_FOR_PARTICLES_COLLIDED: bool
        TRUE_FOR_SPAWN_PARTICLES: bool
        COLLISION_NODES: MXSWrapperBase
        SPAWN_TYPE: int
        DELETE_PARENT: bool
        NUMBER_OF_COLLISIONS: int
        SPAWN_ABLE: float
        NUMBER_OF_OFFSPRINGS: int
        OFFSPRINGS_VARIATION: float
        SYNC_TYPE: int
        RESTART_PARTICLE_AGE: bool
        PARENT_SPEED: int
        OFFSPRING_SPEED: int
        SPEED_TYPE: int
        SPEED: float
        SPEED_INHERITED: float
        SPEED_VARIATION: float
        DIVERGENCE: float
        SCALE_FACTOR: float
        SCALE_VARIATION: float
        RANDOM_SEED: int
        ...
    class ColorCorrection(TextureMap):
        COLOR: MXSWrapperBase
        MAP: None
        REWIREMODE: int
        REWIRER: int
        REWIREG: int
        REWIREB: int
        REWIREA: int
        HUESHIFT: float
        SATURATION: float
        TINT: MXSWrapperBase
        TINTSTRENGTH: float
        LIGHTNESSMODE: int
        CONTRAST: float
        BRIGHTNESS: float
        EXPOSUREMODE: int
        ENABLER: bool
        ENABLEG: bool
        ENABLEB: bool
        GAINRGB: float
        GAINR: float
        GAING: float
        GAINB: float
        GAMMARGB: float
        GAMMAR: float
        GAMMAG: float
        GAMMAB: float
        PIVOTRGB: float
        PIVOTR: float
        PIVOTG: float
        PIVOTB: float
        LIFTRGB: float
        LIFTR: float
        LIFTG: float
        LIFTB: float
        PRINTERLIGHTS: float
        ...
    class ColorMap(TextureMap):
        SOLIDCOLOR: MXSWrapperBase
        MAP: None
        MAPENABLED: bool
        GAMMA: float
        GAIN: float
        REVERSEGAMMA: bool
        ...
    class ColorPickerControl(RolloutControl):
        ...
    class ColorTargetToPresentableTargetFragment(GraphicsFragmentPlugin):
        ...
    class Color_Balance(RenderEffect):
        RED: int
        GREEN: int
        BLUE: int
        PRESERVELUM: bool
        IGNOREBACK: bool
        ...
    class Color_Clipboard(UtilityPlugin):
        ...
    class Color_Correction(TextureMap):
        COLOR: MXSWrapperBase
        MAP: None
        REWIREMODE: int
        REWIRER: int
        REWIREG: int
        REWIREB: int
        REWIREA: int
        HUESHIFT: float
        SATURATION: float
        TINT: MXSWrapperBase
        TINTSTRENGTH: float
        LIGHTNESSMODE: int
        CONTRAST: float
        BRIGHTNESS: float
        EXPOSUREMODE: int
        ENABLER: bool
        ENABLEG: bool
        ENABLEB: bool
        GAINRGB: float
        GAINR: float
        GAING: float
        GAINB: float
        GAMMARGB: float
        GAMMAR: float
        GAMMAG: float
        GAMMAB: float
        PIVOTRGB: float
        PIVOTR: float
        PIVOTG: float
        PIVOTB: float
        LIFTRGB: float
        LIFTR: float
        LIFTG: float
        LIFTB: float
        PRINTERLIGHTS: float
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
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        BACKGROUNDCOLOR: MXSWrapperBase
        SHADOWSON: bool
        TARGETMAPSLOTNAME: str
        ...
    class CompleteRedraw(Primitive):
        ...
    class CompositeMap(TextureMap):
        MAPENABLED: MXSWrapperBase
        MASKENABLED: MXSWrapperBase
        BLENDMODE: MXSWrapperBase
        LAYERNAME: MXSWrapperBase
        DLGOPENED: MXSWrapperBase
        OPACITY: MXSWrapperBase
        MAPLIST: MXSWrapperBase
        MASK: MXSWrapperBase
        ...
    class CompositeTexturemap(TextureMap):
        MAPENABLED: MXSWrapperBase
        MASKENABLED: MXSWrapperBase
        BLENDMODE: MXSWrapperBase
        LAYERNAME: MXSWrapperBase
        DLGOPENED: MXSWrapperBase
        OPACITY: MXSWrapperBase
        MAPLIST: MXSWrapperBase
        MASK: MXSWrapperBase
        ...
    class Condition(ReferenceTarget):
        TYPE: int
        CONDITION_TYPE_REAL: int
        USE_INPUT_AS_A: bool
        INTEGER_A: int
        FLOAT_A: float
        TIME_A: int
        WORLD_A: float
        PERCENT_A: float
        ANGLE_A: float
        USE_SECOND_CONDITION: bool
        USE_INPUT_AS_B: bool
        INTEGER_B: int
        FLOAT_B: float
        TIME_B: int
        WORLD_B: float
        PERCENT_B: float
        ANGLE_B: float
        USE_AS_SPEED_OR_SPIN_RATE: bool
        UNITS_PER_TYPE: int
        ANGLE_AS_ORIENTATION: bool
        SYNC_TYPE: int
        USE_E4: bool
        CONDITION_TYPE_INT: int
        USE_AS_ACCELERATION: bool
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        ...
    class Cone(GeometryClass):
        SLICEON: bool
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS1: float
        TYPEINRADIUS2: float
        TYPEINHEIGHT: float
        RADIUS1: float
        RADIUS2: float
        HEIGHT: float
        HEIGHTSEGS: int
        CAPSEGS: int
        SIDES: int
        SMOOTH: bool
        SLICE: bool
        SLICEFROM: float
        SLICETO: float
        MAPCOORDS: bool
        ...
    class ConeAngleManip(Helper):
        ORIGIN: MXSWrapperBase
        DIRECTION: MXSWrapperBase
        ANGLE: float
        DISTANCE: float
        USESQUARE: bool
        ASPECT: float
        ...
    class Cone_Angle(Helper):
        ORIGIN: MXSWrapperBase
        DIRECTION: MXSWrapperBase
        ANGLE: float
        DISTANCE: float
        USESQUARE: bool
        ASPECT: float
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
        LOCALDEFINITIONFILENAME: str
        UNLOADED: bool
        ACCESSCONTENT: bool
        ALLOWINPLACEEDITING: bool
        ACCESSPUBLISHEDCONTENT: bool
        SOURCEDEFINITIONFILENAME: str
        CONTENTBOUNDINGBOX: bool
        DISPLAYLABEL: bool
        OVERRIDENODEPROPERTIES: bool
        SIZE: float
        AUTOUPDATECLOSED: bool
        DISPLAYSTATUS: bool
        EDITINGUSER: str
        UPDATENEEDED: bool
        ALTERNATEDEFINITIONFILENAME: MXSWrapperBase
        CURRENTALTERNATEDEFINITION: int
        DUPLICATEMATCHINGLAYERS: bool
        ...
    class ContainerHelper(Helper):
        LOCALDEFINITIONFILENAME: str
        UNLOADED: bool
        ACCESSCONTENT: bool
        ALLOWINPLACEEDITING: bool
        ACCESSPUBLISHEDCONTENT: bool
        SOURCEDEFINITIONFILENAME: str
        CONTENTBOUNDINGBOX: bool
        DISPLAYLABEL: bool
        OVERRIDENODEPROPERTIES: bool
        SIZE: float
        AUTOUPDATECLOSED: bool
        DISPLAYSTATUS: bool
        EDITINGUSER: str
        UPDATENEEDED: bool
        ALTERNATEDEFINITIONFILENAME: MXSWrapperBase
        CURRENTALTERNATEDEFINITION: int
        DUPLICATEMATCHINGLAYERS: bool
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
        TYPE: int
        BOOLEAN_CONVERSION: int
        INTEGER_TIME_CONVERSION: int
        MATRIX_VECTOR_CONVERSION: int
        QUATERNION_REAL_CONVERSION: int
        QUATERNION_VECTOR_CONVERSION: int
        REAL_INTEGER_CONVERSION: int
        REAL_TIME_CONVERSION: int
        REAL_VECTOR_CONVERSION: int
        VECTOR_QUATERNION_CONVERSION: int
        VECTOR_REAL_CONVERSION: int
        PAIR_INTEGER_CONVERSION: int
        VECTOR_PAIR_CONVERSION: int
        NEGATIVE_UP_TOWARD_ZERO: bool
        USE_I3_AS_OBJECT_INDEX: bool
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
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
        USESOFTSELECTION: int
        SELECTIONLEVEL: int
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
        SELECTIONOPTION: int
        CREASECOLOR: MXSWrapperBase
        DISPLAYCOLOR: bool
        ...
    class CreaseExplorerManager(Interface):
        ...
    class CreaseMod(Modifier):
        CREASE: float
        SELECTIONOPTION: int
        CREASECOLOR: MXSWrapperBase
        DISPLAYCOLOR: bool
        ...
    class CreaseSet(Modifier):
        CREASESETTYPE: MXSWrapperBase
        CREASESETSELECT: MXSWrapperBase
        CREASESETCOLOR: MXSWrapperBase
        CREASESETNAME: MXSWrapperBase
        CREASESETCREASE: MXSWrapperBase
        IGNOREBACKFACING: bool
        ANGLESELECTTYPE: int
        ANGLEA: float
        ANGLEB: float
        AUTOSELECTNODES: bool
        TOLERANCE: float
        KEEPEXISTINGSETS: bool
        DISPLAYSETCOLORS: bool
        ...
    class CreaseSetManager(Interface):
        ...
    class CreaseSetMod(Modifier):
        CREASESETTYPE: MXSWrapperBase
        CREASESETSELECT: MXSWrapperBase
        CREASESETCOLOR: MXSWrapperBase
        CREASESETNAME: MXSWrapperBase
        CREASESETCREASE: MXSWrapperBase
        IGNOREBACKFACING: bool
        ANGLESELECTTYPE: int
        ANGLEA: float
        ANGLEB: float
        AUTOSELECTNODES: bool
        TOLERANCE: float
        KEEPEXISTINGSETS: bool
        DISPLAYSETCOLORS: bool
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
        SIMSTART: int
        SOLVESTART: int
        SOLVEEND: int
        DELETEKEYS: bool
        SAVENTHPOS: int
        SAVENTHROT: int
        UPDATE: bool
        UPDATEFREQUENCY: int
        VECTORSCALE: float
        USESCRIPT: bool
        FUNCTIONNAME: str
        SCRIPT: None
        SOLVEFORBIPEDS: bool
        BACKTRACKING: bool
        USEPRIORITIES: bool
        FLASHING: bool
        BEHAVIORS: MXSWrapperBase
        TEAMS: MXSWrapperBase
        ASSIGNMENTS: MXSWrapperBase
        COGCONTROLS: MXSWrapperBase
        SCATTER: MXSWrapperBase
        OBJASSOC: MXSWrapperBase
        SMOOTH: MXSWrapperBase
        PRIORITY: MXSWrapperBase
        ICONSIZE: float
        SHOWCOLLISIONS: bool
        WHENTOSHOWCOLLISIONS: int
        COLLISIONCOLOR: MXSWrapperBase
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
        TEAM: None
        DELEGATE: None
        BEHAVIOR: None
        COGCONTROL: None
        WEIGHT: float
        ACTIVE: bool
        ...
    class CrowdDelegate(Helper):
        WIDTH: float
        DEPTH: float
        HEIGHT: float
        VELOCITYCOLOR: MXSWrapperBase
        ACTIVE: bool
        SHOWFORCES: bool
        SHOWVELOCITY: bool
        SHOWCOGSTATES: bool
        XYCONSTRAIN: bool
        USEHIERBBOX: bool
        AVERAGESPEED: float
        MAXACCEL: float
        TURNDECEL: float
        TURNDECELANGLE: float
        INCLINEDECEL: float
        INCLINEDECELANGLE: float
        DECLINEACCEL: float
        DECLINEACCELANGLE: float
        MAXTURNVEL: float
        MAXTURNACCEL: float
        MAXINCLINE: float
        MAXDECLINE: float
        MAXBANK: float
        MAXBANKVEL: float
        BANKPERTURN: float
        USEBIPED: bool
        BIPED: None
        STARTFRAME: int
        PRIORITY: int
        STARTCLIP: int
        BEHAVIORS: MXSWrapperBase
        WEIGHTS: MXSWrapperBase
        DURATION: int
        INDEX: int
        RANDID: int
        SIMPOS: MXSWrapperBase
        ...
    class CrowdDoRestartPathTool(Primitive):
        ...
    class CrowdGroup(ReferenceTarget):
        NAME: str
        MEMBERS: MXSWrapperBase
        ...
    class CrowdPathDrawing(Primitive):
        ...
    class CrowdPathExtend(Primitive):
        ...
    class CrowdPathSetDefaultWidth(Primitive):
        ...
    class CrowdState(ReferenceTarget):
        NAME: str
        BEHAVIORS: MXSWrapperBase
        WEIGHTS: MXSWrapperBase
        TRANSITIONS: MXSWrapperBase
        ...
    class CrowdTeam(ReferenceTarget):
        NAME: str
        MEMBERS: MXSWrapperBase
        ...
    class CrowdTransition(ReferenceTarget):
        PRIORITY: int
        DURATION: int
        EASEIN: float
        EASEOUT: float
        FUNCTIONNAME: str
        SCRIPT: None
        FROM: None
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
        SLICEON: bool
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS: float
        TYPEINHEIGHT: float
        RADIUS: float
        HEIGHT: float
        HEIGHTSEGS: int
        CAPSEGS: int
        SIDES: int
        SMOOTH: bool
        SLICE: bool
        SLICEFROM: float
        SLICETO: float
        MAPCOORDS: bool
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
        FOCALPOINT: int
        FOCALTYPE: int
        HORIZFOCALLOSS: float
        VERTFOCALLOSS: float
        FOCALRANGE: float
        FOCALLIMIT: float
        CAMNODEINDEX: int
        FOCALNODEINDEX: int
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
        FORCE: float
        DRAG: float
        END_PLACEMENT_METHOD: int
        FREE_DAMPER_HEIGHT: float
        RENDERABLE_SPRING: int
        BASE_STUD_DIAMETER: float
        BASE_STUD_HEIGHT: float
        CYLINDER_DIAMETER: float
        CYLINDER_HEIGHT: float
        CYLINDER_SIDES: int
        CYLINDER_FILLET_1: float
        CYLINDER_FILLET_1_SEGMENTS: int
        CYLINDER_FILLET_2: float
        CYLINDER_FILLET_2_SEGMENTS: int
        INSIDE_DIAMETER: float
        SMOOTH_CYLINDER: int
        PISTON_DIAMETER: float
        PISTON_HEIGHT: float
        PISTON_SIDES: int
        SMOOTH_PISTON: int
        ENABLE_BOOT: int
        BOOT_SMALL_DIAMETER: float
        BOOT_LARGE_DIAMETER: float
        BOOT_SIDES: int
        BOOT_FOLDS: int
        BOOT_FOLD_RESOLUTION: int
        BOOT_STOP_DIAMETER: float
        BOOT_STOP_HEIGHT: float
        BOOT_STOP_SETBACK: float
        BOOT_STOP_FILLET: float
        BOOT_STOP_FILLET_SEGEMENTS: int
        SMOOTH_BOOT: int
        DYNAMICS_OBJECT_TYPE: int
        DRAG_UNITS: int
        DAMPER_DIRECTION: int
        FORCE_UNITS: int
        GENERATE_MAPPING_COORDINATES: int
        ...
    class DataChannelModifier(Modifier):
        OPERATORS: MXSWrapperBase
        OPERATOR_ENABLED: MXSWrapperBase
        OPERATOR_OPS: MXSWrapperBase
        OPERATOR_ORDER: MXSWrapperBase
        DISPLAY: bool
        OPERATOR_FROZEN: MXSWrapperBase
        DEBUGINFO: bool
        FLOATDISPLAY: int
        POINT3DISPLAY: int
        TICKSIZE: int
        NORMALIZEDISPLAY: bool
        SHOWNUMERICDATA: bool
        MINCOLOR: MXSWrapperBase
        MIDCOLOR: MXSWrapperBase
        MAXCOLOR: MXSWrapperBase
        NUMERIC_MAX: int
        NUMERIC_DRAWDIST: int
        ...
    class DataOpDeleteCatcher(ReferenceTarget):
        ...
    class DataOperIcon(Helper):
        VISIBLE_ICON: bool
        ICON_TYPE: int
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        COLOR_COORDINATED: bool
        AUTO_UPDATE: bool
        SUBOPERATORS: MXSWrapperBase
        SELECTED_SUBOPERATORS: MXSWrapperBase
        GROUPS: MXSWrapperBase
        ENABLE_BY_SWITCH: bool
        DEFAULT_WIDTH: int
        DEFAULT_OFFSET: int
        DEFAULT_HEIGHT: int
        DEFAULT_RANGE_TYPE: int
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_MAX: float
        ACTIVITY_TYPE: int
        TIME_ON: int
        TIME_OFF: int
        ANIMATABLE_ACTIVE: bool
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_WIDTH: int
        PDVIEW_HEIGHT: int
        PDVIEW_DIVIDER: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_SHOW_PARAMETERS: bool
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        REPEATS: int
        ...
    class DataOperator(Helper):
        VISIBLE_ICON: bool
        ICON_TYPE: int
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        COLOR_COORDINATED: bool
        AUTO_UPDATE: bool
        SUBOPERATORS: MXSWrapperBase
        SELECTED_SUBOPERATORS: MXSWrapperBase
        GROUPS: MXSWrapperBase
        ENABLE_BY_SWITCH: bool
        DEFAULT_WIDTH: int
        DEFAULT_OFFSET: int
        DEFAULT_HEIGHT: int
        DEFAULT_RANGE_TYPE: int
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_MAX: float
        ACTIVITY_TYPE: int
        TIME_ON: int
        TIME_OFF: int
        ANIMATABLE_ACTIVE: bool
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_WIDTH: int
        PDVIEW_HEIGHT: int
        PDVIEW_DIVIDER: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_SHOW_PARAMETERS: bool
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        REPEATS: int
        ...
    class DataPair(Value):
        ...
    class DataTest(Helper):
        VISIBLE_ICON: bool
        ICON_TYPE: int
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        COLOR_COORDINATED: bool
        AUTO_UPDATE: bool
        SUBOPERATORS: MXSWrapperBase
        SELECTED_SUBOPERATORS: MXSWrapperBase
        GROUPS: MXSWrapperBase
        ENABLE_BY_SWITCH: bool
        DEFAULT_WIDTH: int
        DEFAULT_OFFSET: int
        DEFAULT_HEIGHT: int
        DEFAULT_RANGE_TYPE: int
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_MAX: float
        ACTIVITY_TYPE: int
        TIME_ON: int
        TIME_OFF: int
        ANIMATABLE_ACTIVE: bool
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_WIDTH: int
        PDVIEW_HEIGHT: int
        PDVIEW_DIVIDER: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_SHOW_PARAMETERS: bool
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        REPEATS: int
        ...
    class DataTestIcon(Helper):
        VISIBLE_ICON: bool
        ICON_TYPE: int
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        COLOR_COORDINATED: bool
        AUTO_UPDATE: bool
        SUBOPERATORS: MXSWrapperBase
        SELECTED_SUBOPERATORS: MXSWrapperBase
        GROUPS: MXSWrapperBase
        ENABLE_BY_SWITCH: bool
        DEFAULT_WIDTH: int
        DEFAULT_OFFSET: int
        DEFAULT_HEIGHT: int
        DEFAULT_RANGE_TYPE: int
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_MAX: float
        ACTIVITY_TYPE: int
        TIME_ON: int
        TIME_OFF: int
        ANIMATABLE_ACTIVE: bool
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_WIDTH: int
        PDVIEW_HEIGHT: int
        PDVIEW_DIVIDER: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_SHOW_PARAMETERS: bool
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        REPEATS: int
        ...
    class DataViewGroup(ReferenceTarget):
        ...
    class Data_Icon(Helper):
        VISIBLE_ICON: bool
        ICON_TYPE: int
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        COLOR_COORDINATED: bool
        AUTO_UPDATE: bool
        SUBOPERATORS: MXSWrapperBase
        SELECTED_SUBOPERATORS: MXSWrapperBase
        GROUPS: MXSWrapperBase
        ENABLE_BY_SWITCH: bool
        DEFAULT_WIDTH: int
        DEFAULT_OFFSET: int
        DEFAULT_HEIGHT: int
        DEFAULT_RANGE_TYPE: int
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_MAX: float
        ACTIVITY_TYPE: int
        TIME_ON: int
        TIME_OFF: int
        ANIMATABLE_ACTIVE: bool
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_WIDTH: int
        PDVIEW_HEIGHT: int
        PDVIEW_DIVIDER: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_SHOW_PARAMETERS: bool
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        REPEATS: int
        ...
    class Data_Operator(Helper):
        VISIBLE_ICON: bool
        ICON_TYPE: int
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        COLOR_COORDINATED: bool
        AUTO_UPDATE: bool
        SUBOPERATORS: MXSWrapperBase
        SELECTED_SUBOPERATORS: MXSWrapperBase
        GROUPS: MXSWrapperBase
        ENABLE_BY_SWITCH: bool
        DEFAULT_WIDTH: int
        DEFAULT_OFFSET: int
        DEFAULT_HEIGHT: int
        DEFAULT_RANGE_TYPE: int
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_MAX: float
        ACTIVITY_TYPE: int
        TIME_ON: int
        TIME_OFF: int
        ANIMATABLE_ACTIVE: bool
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_WIDTH: int
        PDVIEW_HEIGHT: int
        PDVIEW_DIVIDER: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_SHOW_PARAMETERS: bool
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        REPEATS: int
        ...
    class Data_Test(Helper):
        VISIBLE_ICON: bool
        ICON_TYPE: int
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        COLOR_COORDINATED: bool
        AUTO_UPDATE: bool
        SUBOPERATORS: MXSWrapperBase
        SELECTED_SUBOPERATORS: MXSWrapperBase
        GROUPS: MXSWrapperBase
        ENABLE_BY_SWITCH: bool
        DEFAULT_WIDTH: int
        DEFAULT_OFFSET: int
        DEFAULT_HEIGHT: int
        DEFAULT_RANGE_TYPE: int
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_MAX: float
        ACTIVITY_TYPE: int
        TIME_ON: int
        TIME_OFF: int
        ANIMATABLE_ACTIVE: bool
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_WIDTH: int
        PDVIEW_HEIGHT: int
        PDVIEW_DIVIDER: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_SHOW_PARAMETERS: bool
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        REPEATS: int
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
        WIDTH: float
        LENGTH: float
        VARIATION: float
        CHAOS: float
        FRICTION: float
        INHERITVELOCITY: float
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
        WIDTH: float
        DEPTH: float
        HEIGHT: float
        VELOCITYCOLOR: MXSWrapperBase
        ACTIVE: bool
        SHOWFORCES: bool
        SHOWVELOCITY: bool
        SHOWCOGSTATES: bool
        XYCONSTRAIN: bool
        USEHIERBBOX: bool
        AVERAGESPEED: float
        MAXACCEL: float
        TURNDECEL: float
        TURNDECELANGLE: float
        INCLINEDECEL: float
        INCLINEDECELANGLE: float
        DECLINEACCEL: float
        DECLINEACCELANGLE: float
        MAXTURNVEL: float
        MAXTURNACCEL: float
        MAXINCLINE: float
        MAXDECLINE: float
        MAXBANK: float
        MAXBANKVEL: float
        BANKPERTURN: float
        USEBIPED: bool
        BIPED: None
        STARTFRAME: int
        PRIORITY: int
        STARTCLIP: int
        BEHAVIORS: MXSWrapperBase
        WEIGHTS: MXSWrapperBase
        DURATION: int
        INDEX: int
        RANDID: int
        SIMPOS: MXSWrapperBase
        ...
    class DeleteMesh(Modifier):
        ...
    class DeleteParticles(Helper):
        TYPE: int
        LIFE_SPAN: int
        VARIATION: int
        RANDOM_SEED: int
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
        MAP1: None
        MAP2: None
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        SIZE: float
        STRENGTH: float
        ITERATIONS: int
        COORDS: MXSWrapperBase
        ...
    class DepthFragment(GraphicsFragmentPlugin):
        ...
    class Depth_Of_Field(RenderEffect):
        AFFECTALPHA: bool
        FOCALPOINT: int
        FOCALTYPE: int
        HORIZFOCALLOSS: float
        VERTFOCALLOSS: float
        FOCALRANGE: float
        FOCALLIMIT: float
        CAMNODEINDEX: int
        FOCALNODEINDEX: int
        ...
    class Depth_Of_FieldMPassCamEffect(MPassCamEffect):
        USETARGETDISTANCE: bool
        FOCALDEPTH: float
        DISPLAYPASSES: bool
        USEORIGINALLOCATION: bool
        TOTALPASSES: int
        SAMPLERADIUS: float
        SAMPLEBIAS: float
        NORMALIZEWEIGHTS: bool
        DITHERSTRENGTH: float
        TILESIZE: int
        DISABLEFILTERING: bool
        DISABLEANTIALIASING: bool
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
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
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
        USESHADERFX: int
        SHADERFXGRAPH: None
        TECHNIQUE: int
        RENDERENABLED: bool
        RENDERMATERIAL: MXSWrapperBase
        ENGINERESOURCE: None
        PRESETMATERIAL: int
        PARENTMATERIAL: None
        ...
    class DirectX_9_ShaderReferenceTarget(ReferenceTarget):
        ...
    class Directionallight(Light):
        ASPECT: float
        RGB: MXSWrapperBase
        COLOR: MXSWrapperBase
        CONTRAST: float
        ENABLED: bool
        ON: bool
        TYPE: MXSWrapperBase
        VALUE: int
        FALLOFF: float
        EXCLUDELIST: MXSWrapperBase
        INCLUDELIST: None
        SHOWCONE: bool
        MULTIPLIER: float
        SOFTENDIFFUSEEDGE: float
        HOTSPOT: float
        FARATTENSTART: float
        FARATTENEND: float
        NEARATTENSTART: float
        NEARATTENEND: float
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        DECAYRADIUS: float
        SHADOWCOLOR: MXSWrapperBase
        SHADOWMULTIPLIER: float
        HSV: MXSWrapperBase
        HUE: int
        SATURATION: int
        INCLEXCLTYPE: int
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        USENEARATTEN: bool
        SHOWNEARATTEN: bool
        USEFARATTEN: bool
        SHOWFARATTEN: bool
        ATTENDECAY: int
        PROJECTOR: bool
        PROJECTORMAP: None
        CASTSHADOWS: bool
        USEGLOBALSHADOWSETTINGS: bool
        RAYTRACEDSHADOWS: bool
        OVERSHOOT: bool
        CONESHAPE: int
        LIGHTSHAPE: int
        ATMOSSHADOWS: bool
        LIGHTAFFECTSSHADOW: bool
        SHADOWPROJECTORMAP: None
        USESHADOWPROJECTORMAP: bool
        AMBIENTONLY: bool
        SHADOWGENERATOR: MXSWrapperBase
        ...
    class DisableSceneRedraw(Primitive):
        ...
    class DisableStatusXYZ(Primitive):
        ...
    class DiscreetRadiosityMaterial(Material):
        REFLECTANCESCALE: float
        COLORBLEED: float
        TRANSMITTANCESCALE: float
        LUMINANCESCALE: float
        BUMPSCALE: float
        BASEMATERIAL: MXSWrapperBase
        ...
    class Discreet_Radiosity(RadiosityEffect):
        RADINITIALQUALITY: float
        RADGLOBALREFINESTEPS: int
        RADSELECTIONREFINESTEPS: int
        RADFILTERING: int
        RADPROCESSOBJECTREFINESTEPS: bool
        RADDISPLAYINVIEWPORT: bool
        RADPROCESSINRENDERONLY: bool
        RADDIRECTFILTERING: int
        MESHINGENABLED: bool
        MESHINGSIZE: float
        USEADAPTIVEMESHING: bool
        MINIMUMMESHSIZE: float
        INITIALMESHSIZE: float
        CONTRASTTHRESHOLD: float
        INCLUDEPOINTLIGHTS: bool
        INCLUDELINEARLIGHTS: bool
        INCLUDEAREALIGHTS: bool
        INCLUDESELFEMITTINGLIGHTS: bool
        SHOOTDIRECTLIGHTS: bool
        INCLUDESKYLIGHT: bool
        MINIMUMSELFEMITTINGSIZE: float
        LIGHTPAINTINGINTENSITY: float
        LIGHTPAINTINGPRESSURE: float
        LIGHTUNITSUSED: int
        RMREGATHER: bool
        RMREUSEDIRECTILLUMINATION: bool
        RMRAYSPERSAMPLE: int
        RMFILTERRADIUS: float
        RMCLAMPENABLED: bool
        RMCLAMPVALUE: float
        RMADAPTIVEENABLED: bool
        RMSAMPLESPACING: int
        RMMINSAMPLESPACING: int
        RMSUBDIVISIONCONTRAST: float
        RMSHOWSAMPLES: bool
        STATNUMFACES: int
        STATREFINEITERATIONS: int
        STATSOLUTIONQUALITY: float
        STATNUMGEOMOBJECTS: int
        STATNUMLIGHTOBJECTS: int
        STATMESHSIZE: float
        ELAPSEDTIME: int
        ...
    class Discretizator(ReferenceTarget):
        TYPE: int
        BASE_INTEGER: int
        BASE_FLOAT: float
        BASE_TIME: int
        BASE_WORLD: float
        BASE_PERCENT: float
        BASE_ANGLE: float
        STEP_INTEGER: int
        STEP_FLOAT: float
        STEP_TIME: int
        STEP_WORLD: float
        STEP_PERCENT: float
        STEP_ANGLE: float
        USE_AS_SPEED_OR_SPIN_RATE: bool
        UNITS_PER_TYPE: int
        FILTER: None
        INPUT: None
        ...
    class Disp_Approx(Modifier):
        ...
    class Displace(Modifier):
        AXIS: int
        BITMAP: None
        BLUR: float
        HEIGHT: float
        LENGTH: float
        MAP: None
        WIDTH: float
        CAP: bool
        U_TILE: float
        V_TILE: float
        DECAY: float
        MAPTYPE: int
        LUMCENTER: float
        LUMCENTERENABLE: bool
        USEMAP: bool
        APPLYMAP: bool
        U_FLIP: bool
        V_FLIP: bool
        W_FLIP: bool
        STRENGTH: float
        W_TILE: float
        MAP_OR_VERTEX_COLOR: int
        MAP_CHANNEL: int
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
        COLOR: MXSWrapperBase
        SHOW_NUMBERING: bool
        ADD_PREFIX: bool
        PREFIX_TEXT: str
        DATA_CHANNEL: None
        DATA_HANDLE: int
        REAL_SHOW_AS: int
        VECTOR_SHOW_AS: int
        QUATERNION_SHOW_AS: int
        MATRIX_SHOW_AS: int
        COMPLEX_SHOW_AS: int
        PAIR_SHOW_AS: int
        RATE_VALUE: bool
        UNITS_PER_TYPE: int
        OFFSET_LEFTRIGHT: int
        OFFSET_UPDOWN: int
        OFFSET_INOUT: int
        PRECISION: int
        FILTER_TYPE: int
        GROUP_SELECTION: None
        EXECUTION_ORDER: int
        ...
    class DisplayManager(Interface):
        ...
    class DisplayParticles(Helper):
        TYPE: int
        VISIBLE: float
        COLOR: MXSWrapperBase
        SHOW_NUMBERING: bool
        SELECTED_TYPE: int
        ...
    class DisplayScriptParticles(Helper):
        COLOR: MXSWrapperBase
        SHOW_NUMBERING: bool
        ADD_PREFIX: bool
        PREFIX_TEXT: str
        SCRIPT_DATA_TYPE: int
        OFFSET_LEFTRIGHT: int
        OFFSET_UPDOWN: int
        OFFSET_INOUT: int
        PRECISION: int
        FILTER_TYPE: int
        GROUP_SELECTION: None
        EXECUTION_ORDER: int
        ...
    class DisplayTempPrompt(Primitive):
        ...
    class Display_Script(Helper):
        COLOR: MXSWrapperBase
        SHOW_NUMBERING: bool
        ADD_PREFIX: bool
        PREFIX_TEXT: str
        SCRIPT_DATA_TYPE: int
        OFFSET_LEFTRIGHT: int
        OFFSET_UPDOWN: int
        OFFSET_INOUT: int
        PRECISION: int
        FILTER_TYPE: int
        GROUP_SELECTION: None
        EXECUTION_ORDER: int
        ...
    class DoesSelectedContainInterface(MAXScriptFunction):
        ...
    class Donut(Shape):
        STEPS: int
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        RADIUS1: float
        RADIUS2: float
        ...
    class Double(Value):
        ...
    class DoublePacket(ReferenceMaker):
        ...
    class DoubleSided(Material):
        MATERIAL1: MXSWrapperBase
        MATERIAL2: MXSWrapperBase
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        TRANSLUCENCY: float
        ...
    class Drag(SpacewarpObject):
        TIMEON: MXSWrapperBase
        TIMEOFF: MXSWrapperBase
        SYMMETRY: int
        DAMPINGX: float
        RANGEX: float
        FALLOFFX: float
        DAMPINGY: float
        RANGEY: float
        FALLOFFY: float
        DAMPINGZ: float
        RANGEZ: float
        FALLOFFZ: float
        DAMPINGR: float
        RANGER: float
        FALLOFFR: float
        DAMPINGGC: float
        RANGEGC: float
        FALLOFFGC: float
        DAMPINGRC: float
        RANGERC: float
        FALLOFFRC: float
        DAMPINGC: float
        RANGEC: float
        FALLOFFC: float
        DAMPINGAX: float
        RANGEAX: float
        FALLOFFAX: float
        RANGELESS: bool
        ICONSIZE: float
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
        EFFECTFILE: str
        USESHADERFX: int
        SHADERFXGRAPH: None
        TECHNIQUE: int
        RENDERENABLED: bool
        RENDERMATERIAL: MXSWrapperBase
        ENGINERESOURCE: None
        PRESETMATERIAL: int
        PARENTMATERIAL: None
        K_A: MXSWrapperBase
        K_D: MXSWrapperBase
        K_S: MXSWrapperBase
        N: int
        G_ALPHAVERTEX: bool
        G_ADDVERTEXCOLOR: bool
        G_USEPARALLAX: bool
        G_PARALLAXSCALE: float
        G_PARALLAXBIAS: float
        G_AMBIENTOCCENABLE: bool
        G_TOPDIFFUSEENABLE: bool
        G_BOTTOMDIFFUSEENABLE: bool
        G_SPECULARENABLE: bool
        G_NORMALENABLE: bool
        G_FLIPGREEN: bool
        USEMIKKT: bool
        CALCULATEBITANGENTPERPIXEL: bool
        ORTHOGONALIZETANGENTBITANGENTPERPIXEL: bool
        G_BUMPSCALE: float
        G_REFLECTIONENABLE: bool
        G_REFLECTAMOUNT: float
        G_AMBIENTOCCTEXTURE: None
        G_TOPTEXTURE: None
        G_TOPTEXTUREMAPCHANNEL: int
        G_BOTTOMTEXTURE: None
        G_BOTTOMTEXTUREMAPCHANNEL: int
        G_SPECULARTEXTURE: None
        G_NORMALTEXTURE: None
        G_REFLECTIONTEXTURE: None
        LAMP0POS: int
        K_A: MXSWrapperBase
        K_D: MXSWrapperBase
        K_S: MXSWrapperBase
        N: int
        G_ALPHAVERTEX: bool
        G_ADDVERTEXCOLOR: bool
        G_USEPARALLAX: bool
        G_PARALLAXSCALE: float
        G_PARALLAXBIAS: float
        G_AMBIENTOCCENABLE: bool
        G_TOPDIFFUSEENABLE: bool
        G_BOTTOMDIFFUSEENABLE: bool
        G_SPECULARENABLE: bool
        G_NORMALENABLE: bool
        G_FLIPGREEN: bool
        USEMIKKT: bool
        CALCULATEBITANGENTPERPIXEL: bool
        ORTHOGONALIZETANGENTBITANGENTPERPIXEL: bool
        G_BUMPSCALE: float
        G_REFLECTIONENABLE: bool
        G_REFLECTAMOUNT: float
        G_AMBIENTOCCTEXTURE: None
        G_TOPTEXTURE: None
        G_TOPTEXTUREMAPCHANNEL: int
        G_BOTTOMTEXTURE: None
        G_BOTTOMTEXTUREMAPCHANNEL: int
        G_SPECULARTEXTURE: None
        G_NORMALTEXTURE: None
        G_REFLECTIONTEXTURE: None
        LAMP0POS: int
        K_A: MXSWrapperBase
        K_D: MXSWrapperBase
        K_S: MXSWrapperBase
        N: int
        G_ALPHAVERTEX: bool
        G_ADDVERTEXCOLOR: bool
        G_USEPARALLAX: bool
        G_PARALLAXSCALE: float
        G_PARALLAXBIAS: float
        G_AMBIENTOCCENABLE: bool
        G_TOPDIFFUSEENABLE: bool
        G_BOTTOMDIFFUSEENABLE: bool
        G_SPECULARENABLE: bool
        G_NORMALENABLE: bool
        G_FLIPGREEN: bool
        USEMIKKT: bool
        CALCULATEBITANGENTPERPIXEL: bool
        ORTHOGONALIZETANGENTBITANGENTPERPIXEL: bool
        G_BUMPSCALE: float
        G_REFLECTIONENABLE: bool
        G_REFLECTAMOUNT: float
        G_AMBIENTOCCTEXTURE: None
        G_TOPTEXTURE: None
        G_TOPTEXTUREMAPCHANNEL: int
        G_BOTTOMTEXTURE: None
        G_BOTTOMTEXTUREMAPCHANNEL: int
        G_SPECULARTEXTURE: None
        G_NORMALTEXTURE: None
        G_REFLECTIONTEXTURE: None
        LAMP0POS: int
        K_A: MXSWrapperBase
        K_D: MXSWrapperBase
        K_S: MXSWrapperBase
        N: int
        G_ALPHAVERTEX: bool
        G_ADDVERTEXCOLOR: bool
        G_USEPARALLAX: bool
        G_PARALLAXSCALE: float
        G_PARALLAXBIAS: float
        G_AMBIENTOCCENABLE: bool
        G_TOPDIFFUSEENABLE: bool
        G_BOTTOMDIFFUSEENABLE: bool
        G_SPECULARENABLE: bool
        G_NORMALENABLE: bool
        G_FLIPGREEN: bool
        USEMIKKT: bool
        CALCULATEBITANGENTPERPIXEL: bool
        ORTHOGONALIZETANGENTBITANGENTPERPIXEL: bool
        G_BUMPSCALE: float
        G_REFLECTIONENABLE: bool
        G_REFLECTAMOUNT: float
        G_AMBIENTOCCTEXTURE: None
        G_TOPTEXTURE: None
        G_TOPTEXTUREMAPCHANNEL: int
        G_BOTTOMTEXTURE: None
        G_BOTTOMTEXTUREMAPCHANNEL: int
        G_SPECULARTEXTURE: None
        G_NORMALTEXTURE: None
        G_REFLECTIONTEXTURE: None
        LAMP0POS: int
        K_A: MXSWrapperBase
        K_D: MXSWrapperBase
        K_S: MXSWrapperBase
        N: int
        G_ALPHAVERTEX: bool
        G_ADDVERTEXCOLOR: bool
        G_USEPARALLAX: bool
        G_PARALLAXSCALE: float
        G_PARALLAXBIAS: float
        G_AMBIENTOCCENABLE: bool
        G_TOPDIFFUSEENABLE: bool
        G_BOTTOMDIFFUSEENABLE: bool
        G_SPECULARENABLE: bool
        G_NORMALENABLE: bool
        G_FLIPGREEN: bool
        USEMIKKT: bool
        CALCULATEBITANGENTPERPIXEL: bool
        ORTHOGONALIZETANGENTBITANGENTPERPIXEL: bool
        G_BUMPSCALE: float
        G_REFLECTIONENABLE: bool
        G_REFLECTAMOUNT: float
        G_AMBIENTOCCTEXTURE: None
        G_TOPTEXTURE: None
        G_TOPTEXTUREMAPCHANNEL: int
        G_BOTTOMTEXTURE: None
        G_BOTTOMTEXTUREMAPCHANNEL: int
        G_SPECULARTEXTURE: None
        G_NORMALTEXTURE: None
        G_REFLECTIONTEXTURE: None
        LAMP0POS: int
        K_A: MXSWrapperBase
        K_D: MXSWrapperBase
        K_S: MXSWrapperBase
        N: int
        G_ALPHAVERTEX: bool
        G_ADDVERTEXCOLOR: bool
        G_USEPARALLAX: bool
        G_PARALLAXSCALE: float
        G_PARALLAXBIAS: float
        G_AMBIENTOCCENABLE: bool
        G_TOPDIFFUSEENABLE: bool
        G_BOTTOMDIFFUSEENABLE: bool
        G_SPECULARENABLE: bool
        G_NORMALENABLE: bool
        G_FLIPGREEN: bool
        USEMIKKT: bool
        CALCULATEBITANGENTPERPIXEL: bool
        ORTHOGONALIZETANGENTBITANGENTPERPIXEL: bool
        G_BUMPSCALE: float
        G_REFLECTIONENABLE: bool
        G_REFLECTAMOUNT: float
        G_AMBIENTOCCTEXTURE: None
        G_TOPTEXTURE: None
        G_TOPTEXTUREMAPCHANNEL: int
        G_BOTTOMTEXTURE: None
        G_BOTTOMTEXTUREMAPCHANNEL: int
        G_SPECULARTEXTURE: None
        G_NORMALTEXTURE: None
        G_REFLECTIONTEXTURE: None
        LAMP0POS: int
        K_A: MXSWrapperBase
        K_D: MXSWrapperBase
        K_S: MXSWrapperBase
        N: int
        G_ALPHAVERTEX: bool
        G_ADDVERTEXCOLOR: bool
        G_USEPARALLAX: bool
        G_PARALLAXSCALE: float
        G_PARALLAXBIAS: float
        G_AMBIENTOCCENABLE: bool
        G_TOPDIFFUSEENABLE: bool
        G_BOTTOMDIFFUSEENABLE: bool
        G_SPECULARENABLE: bool
        G_NORMALENABLE: bool
        G_FLIPGREEN: bool
        USEMIKKT: bool
        CALCULATEBITANGENTPERPIXEL: bool
        ORTHOGONALIZETANGENTBITANGENTPERPIXEL: bool
        G_BUMPSCALE: float
        G_REFLECTIONENABLE: bool
        G_REFLECTAMOUNT: float
        G_AMBIENTOCCTEXTURE: None
        G_TOPTEXTURE: None
        G_TOPTEXTUREMAPCHANNEL: int
        G_BOTTOMTEXTURE: None
        G_BOTTOMTEXTUREMAPCHANNEL: int
        G_SPECULARTEXTURE: None
        G_NORMALTEXTURE: None
        G_REFLECTIONTEXTURE: None
        LAMP0POS: int
        K_A: MXSWrapperBase
        K_D: MXSWrapperBase
        K_S: MXSWrapperBase
        N: int
        G_ALPHAVERTEX: bool
        G_ADDVERTEXCOLOR: bool
        G_USEPARALLAX: bool
        G_PARALLAXSCALE: float
        G_PARALLAXBIAS: float
        G_AMBIENTOCCENABLE: bool
        G_TOPDIFFUSEENABLE: bool
        G_BOTTOMDIFFUSEENABLE: bool
        G_SPECULARENABLE: bool
        G_NORMALENABLE: bool
        G_FLIPGREEN: bool
        USEMIKKT: bool
        CALCULATEBITANGENTPERPIXEL: bool
        ORTHOGONALIZETANGENTBITANGENTPERPIXEL: bool
        G_BUMPSCALE: float
        G_REFLECTIONENABLE: bool
        G_REFLECTAMOUNT: float
        G_AMBIENTOCCTEXTURE: None
        G_TOPTEXTURE: None
        G_TOPTEXTUREMAPCHANNEL: int
        G_BOTTOMTEXTURE: None
        G_BOTTOMTEXTUREMAPCHANNEL: int
        G_SPECULARTEXTURE: None
        G_NORMALTEXTURE: None
        G_REFLECTIONTEXTURE: None
        LAMP0POS: int
        K_A: MXSWrapperBase
        K_D: MXSWrapperBase
        K_S: MXSWrapperBase
        N: int
        G_ALPHAVERTEX: bool
        G_ADDVERTEXCOLOR: bool
        G_USEPARALLAX: bool
        G_PARALLAXSCALE: float
        G_PARALLAXBIAS: float
        G_AMBIENTOCCENABLE: bool
        G_TOPDIFFUSEENABLE: bool
        G_BOTTOMDIFFUSEENABLE: bool
        G_SPECULARENABLE: bool
        G_NORMALENABLE: bool
        G_FLIPGREEN: bool
        USEMIKKT: bool
        CALCULATEBITANGENTPERPIXEL: bool
        ORTHOGONALIZETANGENTBITANGENTPERPIXEL: bool
        G_BUMPSCALE: float
        G_REFLECTIONENABLE: bool
        G_REFLECTAMOUNT: float
        G_AMBIENTOCCTEXTURE: None
        G_TOPTEXTURE: None
        G_TOPTEXTUREMAPCHANNEL: int
        G_BOTTOMTEXTURE: None
        G_BOTTOMTEXTUREMAPCHANNEL: int
        G_SPECULARTEXTURE: None
        G_NORMALTEXTURE: None
        G_REFLECTIONTEXTURE: None
        LAMP0POS: int
        ...
    class DynBuilding(Modifier):
        XAMOUNT: float
        XSEGS: int
        XCAPSTART: bool
        XCAPEND: bool
        XCAPTYPE: int
        XOUTPUT: int
        XMATIDS: bool
        XUSESHAPEIDS: bool
        XSMOOTH: bool
        XMAPCOORDS: bool
        XREALWORLDMAPSIZE: bool
        XFLOORS: int
        XWALLMATIDS: int
        XMAPWIDTH: float
        XMAPTYPE: int
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
        SELECTBY: int
        IGNOREBACKFACING: bool
        SHOWHANDLES: bool
        DISPLAYLENGTH: float
        ...
    class EditPolyMod(Modifier):
        CURRENTOPERATION: int
        ANIMATIONMODE: int
        SHOWCAGE: bool
        USESTACKSELECTION: bool
        SELECTBYVERTEX: bool
        IGNOREBACKFACING: bool
        SELECTBYANGLE: bool
        SELECTANGLE: float
        USESOFTSEL: bool
        SSUSEEDGEDIST: bool
        SSEDGEDIST: int
        AFFECTBACKFACING: bool
        FALLOFF: float
        PINCH: float
        BUBBLE: float
        LOCKSOFTSEL: bool
        PAINTSELMODE: int
        PAINTSELVALUE: float
        PAINTSELSIZE: float
        PAINTSELSTRENGTH: float
        PAINTDEFORMMODE: int
        PAINTDEFORMVALUE: float
        PAINTDEFORMSIZE: float
        PAINTDEFORMSTRENGTH: float
        PAINTDEFORMAXIS: int
        CONSTRAINTYPE: int
        PRESERVEUVS: bool
        SPLIT: bool
        SMOOTHNESS: float
        SEPARATEBYSMOOTHING: bool
        SEPARATEBYMATERIAL: bool
        DELETEISOLATEDVERTS: bool
        EXTRUDEFACETYPE: int
        EXTRUDEFACEHEIGHT: float
        EXTRUDEVERTEXHEIGHT: float
        EXTRUDEEDGEHEIGHT: float
        EXTRUDEVERTEXWIDTH: float
        EXTRUDEEDGEWIDTH: float
        BEVELTYPE: int
        BEVELHEIGHT: float
        BEVELOUTLINE: float
        OUTLINEAMOUNT: float
        INSETAMOUNT: float
        INSETTYPE: int
        CHAMFERVERTEXAMOUNT: float
        CHAMFERVERTEXOPEN: bool
        CHAMFEREDGEAMOUNT: float
        EDGECHAMFERSEGMENTS: int
        CHAMFEREDGEOPEN: bool
        WELDVERTEXTHRESHOLD: float
        WELDEDGETHRESHOLD: float
        TESSELLATEBYFACE: int
        TESSTENSION: float
        CONNECTEDGESEGMENTS: int
        EXTRUDEALONGSPLINENODE: None
        EXTRUDEALONGSPLINESEGMENTS: int
        EXTRUDEALONGSPLINETAPER: float
        EXTRUDEALONGSPLINETAPERCURVE: float
        EXTRUDEALONGSPLINETWIST: float
        EXTRUDEALONGSPLINEROTATION: float
        EXTRUDEALONGSPLINEALIGN: bool
        WORLDTOOBJECTTRANSFORM: MXSWrapperBase
        HINGEANGLE: float
        HINGEBASE: MXSWrapperBase
        HINGEDIRECTION: MXSWrapperBase
        HINGESEGMENTS: int
        ALIGNTYPE: int
        ALIGNPLANENORMAL: MXSWrapperBase
        ALIGNPLANEOFFSET: float
        AUTOSMOOTHTHRESHOLD: float
        SMOOTHINGGROUPSTOSET: int
        SMOOTHINGGROUPSTOCLEAR: int
        MATERIALIDTOSET: int
        SELECTBYMATERIALID: int
        SELECTBYMATERIALCLEAR: bool
        SELECTBYSMOOTHINGGROUP: int
        SELECTBYSMOOTHINGGROUPCLEAR: bool
        BRIDGESEGMENTS: int
        BRIDGETAPER: float
        BRIDGEBIAS: float
        BRIDGESMOOTHTHRESHOLD: float
        BRIDGESELECTED: int
        BRIDGETWIST1: int
        BRIDGETWIST2: int
        BRIDGETARGET1: int
        BRIDGETARGET2: int
        RELAXAMOUNT: float
        RELAXITERATIONS: int
        RELAXHOLDBOUNDARYPOINTS: bool
        RELAXHOLDOUTERPOINTS: bool
        BRIDGEEDGEADJACENT: float
        BRIDGEREVERSETRIANGLE: int
        CONNECTEDGEPINCH: int
        CONNECTEDGESLIDE: int
        BREAKDISTANCE: float
        REMVEEDGECTRLKEY: bool
        CAGECOLOR: MXSWrapperBase
        SELECTEDCAGECOLOR: MXSWrapperBase
        SELECTMODE: int
        EDGECHAMFERMITERINGTYPE: int
        EDGECHAMFERTENSION: float
        EDGECHAMFERDEPTH: float
        EDGECHAMFERENDBIAS: float
        EDGECHAMFERRADIALBIAS: float
        EDGECHAMFERINVERT: bool
        EDGECHAMFERSMOOTH: bool
        EDGECHAMFERSMOOTHTYPE: int
        EDGECHAMFERSMOOTHTHRESHOLD: float
        DATACHANNEL: int
        DATAVALUE: float
        HARDEDGEDISPLAYCOLOR: MXSWrapperBase
        HARDEDGEDISPLAY: int
        LASTDELTAINDEX: int
        EXTRUDEFACEBIAS: float
        BEVELFACEBIAS: float
        EDGECHAMFERTYPEOBSOLETE: int
        EDGECHAMFERQUADINTERSECTIONSOBSOLETE: bool
        CHAMFERVERTEXSEGMENTS: int
        CHAMFERVERTEXDEPTH: float
        CHAMFERVERTEXSMOOTH: bool
        CHAMFERVERTEXSMOOTHTYPE: int
        CHAMFERVERTEXSMOOTHTHRESHOLD: float
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
        SELECTBY: int
        IGNOREBACKFACING: bool
        SHOWHANDLES: bool
        DISPLAYLENGTH: float
        ...
    class Edit_Patch(Modifier):
        ...
    class Edit_Poly(Modifier):
        CURRENTOPERATION: int
        ANIMATIONMODE: int
        SHOWCAGE: bool
        USESTACKSELECTION: bool
        SELECTBYVERTEX: bool
        IGNOREBACKFACING: bool
        SELECTBYANGLE: bool
        SELECTANGLE: float
        USESOFTSEL: bool
        SSUSEEDGEDIST: bool
        SSEDGEDIST: int
        AFFECTBACKFACING: bool
        FALLOFF: float
        PINCH: float
        BUBBLE: float
        LOCKSOFTSEL: bool
        PAINTSELMODE: int
        PAINTSELVALUE: float
        PAINTSELSIZE: float
        PAINTSELSTRENGTH: float
        PAINTDEFORMMODE: int
        PAINTDEFORMVALUE: float
        PAINTDEFORMSIZE: float
        PAINTDEFORMSTRENGTH: float
        PAINTDEFORMAXIS: int
        CONSTRAINTYPE: int
        PRESERVEUVS: bool
        SPLIT: bool
        SMOOTHNESS: float
        SEPARATEBYSMOOTHING: bool
        SEPARATEBYMATERIAL: bool
        DELETEISOLATEDVERTS: bool
        EXTRUDEFACETYPE: int
        EXTRUDEFACEHEIGHT: float
        EXTRUDEVERTEXHEIGHT: float
        EXTRUDEEDGEHEIGHT: float
        EXTRUDEVERTEXWIDTH: float
        EXTRUDEEDGEWIDTH: float
        BEVELTYPE: int
        BEVELHEIGHT: float
        BEVELOUTLINE: float
        OUTLINEAMOUNT: float
        INSETAMOUNT: float
        INSETTYPE: int
        CHAMFERVERTEXAMOUNT: float
        CHAMFERVERTEXOPEN: bool
        CHAMFEREDGEAMOUNT: float
        EDGECHAMFERSEGMENTS: int
        CHAMFEREDGEOPEN: bool
        WELDVERTEXTHRESHOLD: float
        WELDEDGETHRESHOLD: float
        TESSELLATEBYFACE: int
        TESSTENSION: float
        CONNECTEDGESEGMENTS: int
        EXTRUDEALONGSPLINENODE: None
        EXTRUDEALONGSPLINESEGMENTS: int
        EXTRUDEALONGSPLINETAPER: float
        EXTRUDEALONGSPLINETAPERCURVE: float
        EXTRUDEALONGSPLINETWIST: float
        EXTRUDEALONGSPLINEROTATION: float
        EXTRUDEALONGSPLINEALIGN: bool
        WORLDTOOBJECTTRANSFORM: MXSWrapperBase
        HINGEANGLE: float
        HINGEBASE: MXSWrapperBase
        HINGEDIRECTION: MXSWrapperBase
        HINGESEGMENTS: int
        ALIGNTYPE: int
        ALIGNPLANENORMAL: MXSWrapperBase
        ALIGNPLANEOFFSET: float
        AUTOSMOOTHTHRESHOLD: float
        SMOOTHINGGROUPSTOSET: int
        SMOOTHINGGROUPSTOCLEAR: int
        MATERIALIDTOSET: int
        SELECTBYMATERIALID: int
        SELECTBYMATERIALCLEAR: bool
        SELECTBYSMOOTHINGGROUP: int
        SELECTBYSMOOTHINGGROUPCLEAR: bool
        BRIDGESEGMENTS: int
        BRIDGETAPER: float
        BRIDGEBIAS: float
        BRIDGESMOOTHTHRESHOLD: float
        BRIDGESELECTED: int
        BRIDGETWIST1: int
        BRIDGETWIST2: int
        BRIDGETARGET1: int
        BRIDGETARGET2: int
        RELAXAMOUNT: float
        RELAXITERATIONS: int
        RELAXHOLDBOUNDARYPOINTS: bool
        RELAXHOLDOUTERPOINTS: bool
        BRIDGEEDGEADJACENT: float
        BRIDGEREVERSETRIANGLE: int
        CONNECTEDGEPINCH: int
        CONNECTEDGESLIDE: int
        BREAKDISTANCE: float
        REMVEEDGECTRLKEY: bool
        CAGECOLOR: MXSWrapperBase
        SELECTEDCAGECOLOR: MXSWrapperBase
        SELECTMODE: int
        EDGECHAMFERMITERINGTYPE: int
        EDGECHAMFERTENSION: float
        EDGECHAMFERDEPTH: float
        EDGECHAMFERENDBIAS: float
        EDGECHAMFERRADIALBIAS: float
        EDGECHAMFERINVERT: bool
        EDGECHAMFERSMOOTH: bool
        EDGECHAMFERSMOOTHTYPE: int
        EDGECHAMFERSMOOTHTHRESHOLD: float
        DATACHANNEL: int
        DATAVALUE: float
        HARDEDGEDISPLAYCOLOR: MXSWrapperBase
        HARDEDGEDISPLAY: int
        LASTDELTAINDEX: int
        EXTRUDEFACEBIAS: float
        BEVELFACEBIAS: float
        EDGECHAMFERTYPEOBSOLETE: int
        EDGECHAMFERQUADINTERSECTIONSOBSOLETE: bool
        CHAMFERVERTEXSEGMENTS: int
        CHAMFERVERTEXDEPTH: float
        CHAMFERVERTEXSMOOTH: bool
        CHAMFERVERTEXSMOOTHTYPE: int
        CHAMFERVERTEXSMOOTHTHRESHOLD: float
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
        STEPS: int
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        EGG_OUTLINE: bool
        EGG_THICKNESS: float
        EGG_ANGLE: float
        EGG_LENGTH: float
        EGG_WIDTH: float
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
        STEPS: int
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        LENGTH: float
        WIDTH: float
        ELLIPSE_THICKNESS: float
        ELLIPSE_OUTLINE: bool
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
        LOCALEULER: MXSWrapperBase
        LOCALEULERX: float
        LOCALEULERY: float
        LOCALEULERZ: float
        WORLDEULER: MXSWrapperBase
        WORLDEULERX: float
        WORLDEULERY: float
        WORLDEULERZ: float
        LOCALPOSITION: MXSWrapperBase
        LOCALPOSITIONX: float
        LOCALPOSITIONY: float
        LOCALPOSITIONZ: float
        WORLDPOSITION: MXSWrapperBase
        WORLDPOSITIONX: float
        WORLDPOSITIONY: float
        WORLDPOSITIONZ: float
        DISTANCE: float
        WORLDBOUNDINGBOXSIZE: MXSWrapperBase
        WORLDBOUNDINGBOXWIDTH: float
        WORLDBOUNDINGBOXLENGTH: float
        WORLDBOUNDINGBOXHEIGHT: float
        ANGLE: float
        EXPOSENODE: None
        LOCALREFERENCENODE: None
        USEPARENT: bool
        STRIPNUSCALE: bool
        EULERXORDER: int
        EULERYORDER: int
        EULERZORDER: int
        USETIMEOFFSET: bool
        TIMEOFFSET: MXSWrapperBase
        SIZE: float
        CENTERMARKER: bool
        AXISTRIPOD: bool
        CROSS: bool
        BOX: bool
        CONSTANTSCREENSIZE: bool
        DRAWONTOP: bool
        DISPLAYEXPOSEDVALS: bool
        ...
    class ExposeTransform(Helper):
        LOCALEULER: MXSWrapperBase
        LOCALEULERX: float
        LOCALEULERY: float
        LOCALEULERZ: float
        WORLDEULER: MXSWrapperBase
        WORLDEULERX: float
        WORLDEULERY: float
        WORLDEULERZ: float
        LOCALPOSITION: MXSWrapperBase
        LOCALPOSITIONX: float
        LOCALPOSITIONY: float
        LOCALPOSITIONZ: float
        WORLDPOSITION: MXSWrapperBase
        WORLDPOSITIONX: float
        WORLDPOSITIONY: float
        WORLDPOSITIONZ: float
        DISTANCE: float
        WORLDBOUNDINGBOXSIZE: MXSWrapperBase
        WORLDBOUNDINGBOXWIDTH: float
        WORLDBOUNDINGBOXLENGTH: float
        WORLDBOUNDINGBOXHEIGHT: float
        ANGLE: float
        EXPOSENODE: None
        LOCALREFERENCENODE: None
        USEPARENT: bool
        STRIPNUSCALE: bool
        EULERXORDER: int
        EULERYORDER: int
        EULERZORDER: int
        USETIMEOFFSET: bool
        TIMEOFFSET: MXSWrapperBase
        SIZE: float
        CENTERMARKER: bool
        AXISTRIPOD: bool
        CROSS: bool
        BOX: bool
        CONSTANTSCREENSIZE: bool
        DRAWONTOP: bool
        DISPLAYEXPOSEDVALS: bool
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
        MATIDS: bool
        SMOOTH: bool
        CAPSTART: bool
        CAPEND: bool
        CAPTYPE: int
        SEGS: int
        MAPCOORDS: bool
        OUTPUT: int
        AMOUNT: float
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
        DISPLATTICE: bool
        DISPSOURCE: bool
        DEFORMTYPE: int
        INPOINTS: bool
        OUTPOINTS: bool
        OFFSET: float
        ...
    class FFD3X3X3(Modifier):
        DISPLATTICE: bool
        DISPSOURCE: bool
        DEFORMTYPE: int
        INPOINTS: bool
        OUTPOINTS: bool
        OFFSET: float
        ...
    class FFD4X4X4(Modifier):
        DISPLATTICE: bool
        DISPSOURCE: bool
        DEFORMTYPE: int
        INPOINTS: bool
        OUTPOINTS: bool
        OFFSET: float
        ...
    class FFDBox(Modifier):
        DISPLATTICE: bool
        DISPSOURCE: bool
        DEFORMTYPE: int
        FALLOFF: float
        TENSION: float
        CONTINUITY: float
        INPOINTS: bool
        OUTPOINTS: bool
        OFFSET: float
        ...
    class FFDCyl(Modifier):
        DISPLATTICE: bool
        DISPSOURCE: bool
        DEFORMTYPE: int
        FALLOFF: float
        TENSION: float
        CONTINUITY: float
        INPOINTS: bool
        OUTPOINTS: bool
        OFFSET: float
        ...
    class FFD_2X2X2(Modifier):
        DISPLATTICE: bool
        DISPSOURCE: bool
        DEFORMTYPE: int
        INPOINTS: bool
        OUTPOINTS: bool
        OFFSET: float
        ...
    class FFD_3X3X3(Modifier):
        DISPLATTICE: bool
        DISPSOURCE: bool
        DEFORMTYPE: int
        INPOINTS: bool
        OUTPOINTS: bool
        OFFSET: float
        ...
    class FFD_4X4X4(Modifier):
        DISPLATTICE: bool
        DISPSOURCE: bool
        DEFORMTYPE: int
        INPOINTS: bool
        OUTPOINTS: bool
        OFFSET: float
        ...
    class FFD_Binding(SpacewarpModifier):
        ...
    class FFD_Select(Modifier):
        ...
    class FaceSelection(Value):
        ...
    class Face_Extrude(Modifier):
        SCALE: float
        AMOUNT: float
        EXTRUDEFROMCENTER: bool
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
        CHANNELTYPE: int
        CAMERANODE: None
        NEARZ: float
        FARZ: float
        FITSCENE: bool
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
        FILTER_WIDTH: float
        FILTER_VALUE: float
        FILTER_DEPTH: float
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
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
        SPEED_TYPE: int
        USE_CRUISE_SPEED: bool
        CRUISE_SPEED: float
        CRUISE_SPEED_VARIATION: float
        ACCELERATION_LIMIT: float
        SYNC_TYPE: int
        TEST_DISTANCE: float
        TIMING_TYPE: int
        TIME: int
        TIME_VARIATION: int
        SUBFRAME_SAMPLING: bool
        USE_DOCKING_SPEED: bool
        DOCKING_SPEED: float
        DOCKING_SPEED_VARIATION: float
        TARGET_TYPE: int
        TARGET_OBJECTS: MXSWrapperBase
        ANIMATED_SHAPE: bool
        FOLLOW_TARGET: bool
        LOCK_ON_TARGET: bool
        AIM_POINT_TYPE: int
        ASSIGNMENT_TYPE: int
        DOCKING_TYPE: int
        ICON_SIZE: float
        RANDOM_SEED: int
        TEST_TYPE: int
        EASE_IN: float
        TARGET_SYNC_TYPE: int
        DOCKING_DISTANCE: float
        COLOR_TYPE: bool
        ...
    class Fire_Effect(Atmospheric):
        STRETCH: float
        SMOKE: int
        PHASE: float
        SAMPLES: int
        DENSITY: float
        INNER_COLOR: MXSWrapperBase
        OUTER_COLOR: MXSWrapperBase
        SMOKE_COLOR: MXSWrapperBase
        FLAME_TYPE: int
        REGULARITY: float
        FLAME_SIZE: float
        FLAME_DETAIL: float
        DRIFT: float
        EXPLOSION: int
        FURY: float
        ...
    class FixAmbient(UtilityPlugin):
        ...
    class FixInvalidMaterialsForDaylightSimulation(MAXScriptFunction):
        ...
    class Fix_Ambient(UtilityPlugin):
        ...
    class Fixed(GeometryClass):
        HEIGHT: float
        WIDTH: float
        DEPTH: float
        CHAMFERED_PROFILE: bool
        NUMBER_OF_PANELS_HORIZONTALLY: int
        NUMBER_OF_PANELS_VERTICALLY: int
        HORIZONTAL_FRAME_WIDTH: float
        VERTICAL_FRAME_WIDTH: float
        FRAME_THICKNESS: float
        GLAZING_THICKNESS: float
        RAIL_WIDTH: float
        GENERATE_MAPPING_COORDS: bool
        ...
    class FlashNodes(Primitive):
        ...
    class Flat_Mirror(TextureMap):
        BLURAMOUNT: float
        DISTORTIONAMOUNT: float
        LEVEL: float
        SIZE: float
        PHASE: float
        APPLYBLUR: bool
        NTHFRAME: int
        FRAME: int
        USEENVIROMENT: bool
        APPLYTOFACEID: bool
        FACEID: int
        DISTORTIONTYPE: int
        NOISETYPE: int
        ...
    class Flex(Modifier):
        FLEX: float
        STRENGTH: float
        SWAY: float
        REFERENCEFRAME: int
        PAINTSTRENGTH: float
        PAINTRADIUS: float
        PAINTFEATHER: float
        PAINTBACKFACE: bool
        FORCENODE: MXSWrapperBase
        ABSOLUTE: bool
        SOLVER: int
        SAMPLES: int
        CHASE: bool
        ENABLECENTER: bool
        ENDFRAME: int
        ENABLEENDFRAME: bool
        COLLIDERNODE: MXSWrapperBase
        STRETCHSTRENGTH: float
        STRETCHSWAY: float
        TORQUESTRENGTH: float
        TORQUESWAY: float
        EXTRASTRENGTH: MXSWrapperBase
        EXTRASWAY: MXSWrapperBase
        HOLDRADIUS: float
        ADDMODE: int
        DISPLAYSPRINGS: bool
        HOLDLENGTH: bool
        HOLDLENGTHPERCENT: float
        LAZYEVAL: bool
        STRETCH: float
        STIFFNESS: float
        ENABLEADVANCESPRINGS: bool
        SPRINGCOLORS: MXSWrapperBase
        CUSTOMSPRINGDISPLAY: MXSWrapperBase
        AFFECTALL: bool
        CREATESPRINGDEPTH: int
        CREATESPRINGMULT: float
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
        UPPER_LIMIT: float
        LOWER_LIMIT: float
        UPPER_LIMIT_ENABLED: bool
        LOWER_LIMIT_ENABLED: bool
        STATIC_VALUE: float
        UPPER_SMOOTHING: float
        LOWER_SMOOTHING: float
        ...
    class FloatList(FloatController):
        WEIGHT: MXSWrapperBase
        AVERAGE: bool
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
        WIDTH: float
        LANEWIDTH: float
        DIRECTIONINDEX: int
        POSITIONSAMPLE: int
        GENDERSAMPLE: int
        LINKPORTALS: bool
        DENSITY: float
        SPEED: float
        RUNNING: float
        GENDER: float
        DENSITY2: float
        SPEED2: float
        RUNNING2: float
        GENDER2: float
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
        ICONSIZE: float
        SHOWICON: int
        CACHETAB: MXSWrapperBase
        CACHENAMETAB: MXSWrapperBase
        CACHEFLAGSTAB: MXSWrapperBase
        DISPLAYCACHELIMIT: float
        MATERIALID_TAB: MXSWrapperBase
        PLAYBACKMODE_TAB: MXSWrapperBase
        STARTONLY_TAB: MXSWrapperBase
        STARTFRAME_TAB: MXSWrapperBase
        ENDFRAME_TAB: MXSWrapperBase
        PLAYBACKFRAME_TAB: MXSWrapperBase
        MATERIALIDINDIRECT: int
        PLAYBACKMODEINDIRECT: int
        STARTONLYINDIRECT: int
        STARTFRAMEINDIRECT: int
        ENDFRAMEINDIRECT: int
        PLAYBACKFRAMEINDIRECT: int
        DISPLAYTYPEMODE: int
        VIEWPORTPERCENTACCESSOR: float
        COLORCHANNELMODE: int
        STATICCOLOR: MXSWrapperBase
        COLORCHANNELMIN: MXSWrapperBase
        COLORCHANNELMAX: MXSWrapperBase
        OPACITYCHANNELMODE: float
        STATICOPACITY: float
        OPACITYCHANNELMIN: float
        OPACITYCHANNELMAX: float
        SIZECHANNELMODE: float
        STATICSIZE: float
        SIZECHANNELMIN: float
        SIZECHANNELMAX: float
        CUSTOMNODE: None
        FOAMVIEWPORTPERCENTACCESSOR: float
        FOAMDISPLAYTYPEMODE: int
        FOAMCOLORCHANNELMODE: int
        FOAMSTATICCOLOR: MXSWrapperBase
        FOAMCOLORCHANNELMIN: MXSWrapperBase
        FOAMCOLORCHANNELMAX: MXSWrapperBase
        FOAMOPACITYCHANNELMODE: int
        FOAMSTATICOPACITY: float
        FOAMOPACITYCHANNELMIN: float
        FOAMOPACITYCHANNELMAX: float
        FOAMSIZECHANNELMODE: int
        FOAMSTATICSIZE: float
        FOAMSIZECHANNELMIN: float
        FOAMSIZECHANNELMAX: float
        MESHINGDROPLETREVEALFACTORACCESSOR: float
        MESHINGDROPLETREVEALFACTORTAB: MXSWrapperBase
        MESHINGSURFACERADIUSACCESSOR: float
        MESHINGSURFACERADIUSTAB: MXSWrapperBase
        MESHINGDROPLETRADIUSACCESSOR: float
        MESHINGDROPLETRADIUSTAB: MXSWrapperBase
        MESHINGKERNELFACTORACCESSOR: float
        MESHINGKERNELFACTORTAB: MXSWrapperBase
        MESHINGSMOOTHINGACCESSOR: int
        MESHINGSMOOTHINGTAB: MXSWrapperBase
        MESHINGRESOLUTIONFACTORACCESSOR: float
        MESHINGRESOLUTIONFACTORTAB: MXSWrapperBase
        MESHINGHOLEKILLTHRESHOLDACCESSOR: float
        MESHINGHOLEKILLTHRESHOLDTAB: MXSWrapperBase
        MESHINGFLIPFACENORMALACCESSOR: bool
        MESHINGFLIPFACENORMALTAB: MXSWrapperBase
        ENABLEGPUPOINTS: bool
        LIQUIDRENDERTYPE: int
        LIQUIDRENDERSTATICSIZE: float
        LIQUIDRENDERSIZEMIN: float
        LIQUIDRENDERSIZEMAX: float
        LIQUIDRENDERSIZEMINDOMAIN: float
        LIQUIDRENDERSIZEMAXDOMAIN: float
        FOAMRENDERTYPE: int
        FOAMRENDERSTATICSIZE: float
        FOAMRENDERSIZEMIN: float
        FOAMRENDERSIZEMAX: float
        FOAMRENDERSIZEMINDOMAIN: float
        FOAMRENDERSIZEMAXDOMAIN: float
        LIQUIDCUSTOMRENDERNODE: None
        FOAMCUSTOMRENDERNODE: None
        LIQUIDRENDERSIZECHANNEL: str
        FOAMRENDERSIZECHANNEL: str
        LIQUIDSIZECHANNELTYPE: int
        FOAMSIZECHANNELTYPE: int
        RENDERCHANNELMAPNAME: MXSWrapperBase
        RENDERCHANNELMAPINDEX: MXSWrapperBase
        ARNOLDSURFACETYPE: int
        ARNOLDRENDERCOMPONENTTYPE: int
        ARNOLDDROPLETREVEALFACTOR: float
        ARNOLDSURFACERADIUS: float
        ARNOLDDROPLETRADIUS: float
        ARNOLDRESOLUTIONFACTOR: float
        ARNOLDHOLEKILLTHRESHOLD: float
        ARNOLDFILTERINGDILATE: float
        ARNOLDFILTERINGSMOOTH: float
        ARNOLDFILTERINGSMOOTHMODE: int
        ARNOLDFILTERINGSMOOTHITERATIONS: int
        ARNOLDFILTERINGERODE: float
        ARNOLDUSEOCEANBLENDING: bool
        ARNOLDOCEANMESHPLANE: None
        ARNOLDOCEANBLENDINGBOUNDARYRADIUS: float
        ARNOLDMESHSUBDIVISIONS: int
        ARNOLDMESHSMOOTHING: bool
        ARNOLDIMPLICITSTEPSIZE: float
        ARNOLDIMPLICITSAMPLES: int
        ARNOLDFOAMSURFACETYPE: int
        ARNOLDFOAMDROPLETREVEALFACTOR: float
        ARNOLDFOAMSURFACERADIUS: float
        ARNOLDFOAMDROPLETRADIUS: float
        ARNOLDFOAMRESOLUTIONFACTOR: float
        ARNOLDFOAMHOLEKILLTHRESHOLD: float
        ARNOLDFOAMFILTERINGDILATE: float
        ARNOLDFOAMFILTERINGSMOOTH: float
        ARNOLDFOAMFILTERINGSMOOTHMODE: int
        ARNOLDFOAMFILTERINGSMOOTHITERATIONS: int
        ARNOLDFOAMFILTERINGERODE: float
        ARNOLDFOAMUSEOCEANBLENDING: bool
        ARNOLDFOAMOCEANMESHPLANE: None
        ARNOLDFOAMOCEANBLENDINGBOUNDARYRADIUS: float
        ARNOLDFOAMMESHSUBDIVISIONS: int
        ARNOLDFOAMMESHSMOOTHING: bool
        ARNOLDFOAMIMPLICITSTEPSIZE: float
        ARNOLDFOAMIMPLICITSAMPLES: int
        ARNOLDPOINTRADIUSCHANNEL: int
        ARNOLDPOINTRADIUS: float
        ARNOLDPOINTSTEPSIZE: float
        ARNOLDPOINTCHUNKSIZE: int
        DISPLAYCACHELIMITENABLE: bool
        USELOADEROBJECTTRANSFORM: bool
        ARNOLDSURFACECHANNELNAMETAB: MXSWrapperBase
        ...
    class FluidSimObjectManager(Interface):
        ...
    class Fog(Atmospheric):
        SIZE: float
        ANGLE: float
        FALLOFF: int
        PHASE: float
        DENSITY: float
        BOTTOM: float
        TOP: float
        FOG_COLOR: MXSWrapperBase
        FOG_BACKGROUND: int
        FOG_TYPE: int
        NEAR: float
        FAR: float
        EXPONENTIAL: int
        USE_COLOR_MAP: int
        USE_OPACITY_MAP: int
        HORIZON_NOISE: int
        ...
    class FogHelper(Helper):
        ...
    class Foliage(GeometryClass):
        HEIGHT: float
        SEED: int
        DENSITY: float
        PRUNING: float
        CANOPYMODE: int
        GENUV: bool
        SHOWTRUNK: bool
        SHOWBRANCHES: bool
        SHOWLEAVES: bool
        SHOWFRUIT: bool
        SHOWFLOWERS: bool
        SHOWROOTS: bool
        LEVELOFDETAIL: int
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
        INFLUENCE: float
        SYNC: int
        FORCE_SPACE_WARPS: MXSWrapperBase
        FORCE_OVERLAPPING: int
        USE_SCRIPT_FLOAT: int
        ...
    class ForceCompleteRedraw(Primitive):
        ...
    class FragmentGraph(GraphicsFragmentPlugin):
        ...
    class FrameTagManager(Interface):
        ...
    class Free_Area(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Free_Cylinder(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Free_Disc(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Free_Light(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Free_Linear(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Free_Point(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Free_Rectangle(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Free_Sphere(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Freecamera(Camera):
        TYPE: MXSWrapperBase
        FOV: float
        TARGETDISTANCE: None
        NEARRANGE: float
        FARRANGE: float
        NEARCLIP: float
        NEAR_CLIP: float
        FARCLIP: float
        FAR_CLIP: float
        MPASSENABLED: bool
        MPASSRENDERPERPASS: bool
        CURFOV: float
        FOVTYPE: int
        ORTHOPROJECTION: bool
        SHOWCONE: bool
        SHOWHORIZON: bool
        SHOWRANGES: bool
        CLIPMANUALLY: bool
        MPASSEFFECT: MXSWrapperBase
        ...
    class FreehandSpline(Shape):
        STEPS: int
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        CURVETYPE: int
        SHOWKNOTS: bool
        ENABLECLOSEDCURVE: bool
        CONSTRAINOFFSET: float
        ENABLECONSTRAINSHOWNORMALS: bool
        ENABLECONSTRAIN: bool
        GRANULARITY: int
        ENDCREATEONBUTTONUP: bool
        KNOTS: MXSWrapperBase
        NORMALS: MXSWrapperBase
        SHAPE_KNOTS: MXSWrapperBase
        SAMPLING: int
        THRESHOLD: int
        ...
    class Function(Value):
        ...
    class FunctionReferenceTarget(ReferenceTarget):
        FIRST_OPERAND_TYPE: int
        USE_R_AS_FACTOR_FOR_FIRST_OPERAND: bool
        FACTOR_FOR_FIRST_OPERAND: float
        INTEGER_FACTOR_FOR_FIRST_OPERAND: int
        USE_SECOND_OPERAND: bool
        SECOND_OPERAND_TYPE_FOR_INTEGER_REAL: int
        SECOND_OPERAND_TYPE_FOR_QUATERNION: int
        SECOND_OPERAND_TYPE_FOR_VECTOR: int
        USE_R_AS_FACTOR_FOR_SECOND_OPERAND: bool
        FACTOR_FOR_SECOND_OPERAND: float
        INTEGER_FACTOR_FOR_SECOND_OPERAND: int
        FUNCTION_TYPE_FOR_BOOLEAN_SINGLE: int
        FUNCTION_TYPE_FOR_BOOLEAN_AND_BOOLEAN: int
        FUNCTION_TYPE_FOR_TIME_SINGLE: int
        FUNCTION_TYPE_FOR_TIME_AND_TIME: int
        FUNCTION_TYPE_FOR_MATRIX_SINGLE: int
        FUNCTION_TYPE_FOR_MATRIX_AND_MATRIX: int
        FUNCTION_TYPE_FOR_QUATERNION_SINGLE: int
        FUNCTION_TYPE_FOR_QUATERNION_AND_QUATERNION: int
        FUNCTION_TYPE_FOR_QUATERNION_AND_REAL: int
        FUNCTION_TYPE_FOR_QUATERNION_AND_INTEGER_TIME: int
        FUNCTION_TYPE_FOR_INTEGER_REAL_SINGLE: int
        FUNCTION_TYPE_FOR_INTEGER_AND_REAL: int
        FUNCTION_TYPE_FOR_VECTOR_SINGLE: int
        FUNCTION_TYPE_FOR_VECTOR_AND_QUATERNION: int
        FUNCTION_TYPE_FOR_VECTOR_AND_MATRIX: int
        FUNCTION_TYPE_FOR_VECTOR_AND_REAL: int
        FUNCTION_TYPE_FOR_VECTOR_AND_INTEGER_TIME: int
        FUNCTION_TYPE_FOR_VECTOR_AND_VECTOR: int
        POST_FACTOR: float
        INTEGER_POST_FACTOR: int
        SYNC_TYPE: int
        USE_E5: bool
        OFFSET_FOR_FIRST_OPERAND: float
        INTEGER_OFFSET_FOR_FIRST_OPERAND: int
        RESTRICT_BY_GROUP_ID: bool
        GROUP_ID_DATA_CHANNEL: None
        GROUP_ID_DATA_HANDLE: int
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
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
        DENSITY: float
        AUTOMESH: bool
        PRESERVE: bool
        OUTPUTTYPE: int
        STRETCHMAPPING: bool
        FIGURE: None
        STRIPWIDTH: float
        STRIPTEXTURESCALE: float
        SHOWMESH: bool
        SHOWSEAMS: bool
        RELAX: bool
        ...
    class Garmentize2(Modifier):
        DENSITY: float
        AUTOMESH: bool
        PRESERVE: bool
        OUTPUTTYPE: int
        STRETCHMAPPING: bool
        FIGURE: None
        STRIPWIDTH: float
        STRIPTEXTURESCALE: float
        SHOWMESH: bool
        SHOWSEAMS: bool
        RELAX: bool
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
        HEIGHT: float
        SMOOTH: int
        RADIUS: float
        SIDES: int
        MAPCOORDS: int
        FILLET: float
        FILLET_SEGMENTS: int
        SIDE_SEGMENTS: int
        HEIGHT_SEGMENTS: int
        ...
    class GeoSphere(GeometryClass):
        CREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS: float
        HEMISPHERE: bool
        SEGS: int
        RADIUS: float
        BASETYPE: int
        BASETOPIVOT: bool
        SMOOTH: bool
        MAPCOORDS: bool
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
        ELEMENTNAME: str
        SIZE: float
        INTENSITY: float
        ON: bool
        OBJECTSHIDE: bool
        SQUEEZE: bool
        OCCLUSION: float
        USESOURCECOLOR: float
        CENTERCOLOR: MXSWrapperBase
        EDGECOLOR: MXSWrapperBase
        RADIALMTL: None
        USERADIALMTL: bool
        RADIALMAP: None
        USERADIALMAP: bool
        CIRCULARCOLORMIX: float
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        QUADRANT4COLOR: MXSWrapperBase
        CIRCULARMTL: None
        USECIRCULARMTL: bool
        CIRCULARMAP: None
        USECIRCULARMAP: bool
        RADIALSIZEMAP: None
        USERADIALSIZEMAP: bool
        APPLYLIGHTS: bool
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        SOURCEOBJECTID: bool
        OBJECTID: int
        SOURCEEFFECTSID: bool
        EFFECTSID: int
        SOURCEUNCLAMPEDCOLOR: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        SOURCESURFACENORMAL: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        SOURCEWHOLE: bool
        SOURCEALPHA: bool
        ALPHA: int
        SOURCEZBUFFER: bool
        ZHI: float
        ZLO: float
        FILTERALL: bool
        FILTEREDGE: bool
        FILTERPERIMETERALPHA: bool
        FILTERPERIMETER: bool
        FILTERBRIGHTNESS: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        FILTERHUE: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        APPLYNOISE: bool
        NOISEMAP: None
        RADIALDENSITY: None
        USERADIALDENSITY: bool
        ...
    class Gnormal(TextureMap):
        MULT_SPIN: float
        BUMP_SPIN: float
        NORMAL_MAP: None
        BUMP_MAP: None
        MAP1ON: bool
        MAP2ON: bool
        METHOD: int
        FLIPRED: bool
        FLIPGREEN: bool
        SWAP_RG: bool
        ...
    class Go_To_Rotation(Helper):
        SEND_OUT: bool
        TRANSITION_TYPE: int
        TIME: int
        VARIATION: int
        TARGET_ROTATION: int
        MATCH_INITIAL_SPIN: bool
        SPINRATE: float
        SPIN_RATE_VARIATION: float
        EASE_IN: float
        STOP_SPINNING: bool
        RANDOM_SEED: int
        ...
    class Gradient(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COLOR3: MXSWrapperBase
        MAP1: None
        MAP2: None
        MAP3: None
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        MAP3ENABLED: bool
        COLOR2POS: float
        GRADIENTTYPE: int
        NOISEAMOUNT: float
        NOISETYPE: int
        NOISESIZE: float
        NOISEPHASE: float
        NOISELEVELS: float
        NOISETHRESHOLDLOW: float
        NOISETHRESHOLDHIGH: float
        NOISETHRESHOLDSMOOTH: float
        COORDS: MXSWrapperBase
        OUTPUT: MXSWrapperBase
        ...
    class Gradient_GradCtlData(ReferenceTarget):
        ...
    class Gradient_Ramp(TextureMap):
        SIZE: float
        PHASE: float
        AMOUNT: float
        GRADIENT_TYPE: int
        NOISE_TYPE: int
        LEVELS: float
        LOW_THRESHOLD: float
        HIGH_THRESHOLD: float
        THRESHOLD_SMOOTHING: float
        SOURCE_MAP_ON: int
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
        GROUP_SELECTION: None
        EVENT_WITH_OPERATORS: None
        GROUP_SELECTION_OPERATORS: MXSWrapperBase
        SELECTION_CONDITION: int
        ...
    class GroupSelection(Helper):
        UPDATE_TYPE: int
        REVERSE_SELECTION: bool
        SELECTION_TYPE: int
        SNAPSHOT_TYPE: int
        SNAPSHOT_PARTICLE_SYSTEM: int
        SNAPSHOT_INDICES: MXSWrapperBase
        ICON_TYPE: int
        SUBFRAME_SAMPLING: bool
        INSIDE_OBJECT: None
        ANIMATED_SHAPE: bool
        PROPERTY_TYPE: int
        AGE_FROM: int
        AGE_TO: int
        AGE_VARIATION: int
        SPEED_FROM: float
        SPEED_TO: float
        SPEED_VARIATION: float
        DIVERGENCE: float
        DIVERGENCE_VARIATION: float
        SCALE_FROM: float
        SCALE_TO: float
        SCALE_VARIATION: float
        SIZE_FROM: float
        SIZE_TO: float
        SIZE_VARIATION: float
        INDEX_FROM: int
        INDEX_TO: int
        INDEX_VARIATION: int
        FLOAT_FROM: float
        FLOAT_TO: float
        FLOAT_VARIATION: float
        CHANCE: float
        COMBINE_TYPE: int
        GROUP_A: None
        GROUP_B: None
        ICON_SIZE: float
        LOGO_SIZE: float
        RANDOM_SEED: int
        COLOR_COORDINATED: bool
        ...
    class GroupStartControl(RolloutControl):
        ...
    class Group_Operator(Helper):
        GROUP_SELECTION: None
        EVENT_WITH_OPERATORS: None
        GROUP_SELECTION_OPERATORS: MXSWrapperBase
        SELECTION_CONDITION: int
        ...
    class Group_Select(Helper):
        UPDATE_TYPE: int
        REVERSE_SELECTION: bool
        SELECTION_TYPE: int
        SNAPSHOT_TYPE: int
        SNAPSHOT_PARTICLE_SYSTEM: int
        SNAPSHOT_INDICES: MXSWrapperBase
        ICON_TYPE: int
        SUBFRAME_SAMPLING: bool
        INSIDE_OBJECT: None
        ANIMATED_SHAPE: bool
        PROPERTY_TYPE: int
        AGE_FROM: int
        AGE_TO: int
        AGE_VARIATION: int
        SPEED_FROM: float
        SPEED_TO: float
        SPEED_VARIATION: float
        DIVERGENCE: float
        DIVERGENCE_VARIATION: float
        SCALE_FROM: float
        SCALE_TO: float
        SCALE_VARIATION: float
        SIZE_FROM: float
        SIZE_TO: float
        SIZE_VARIATION: float
        INDEX_FROM: int
        INDEX_TO: int
        INDEX_VARIATION: int
        FLOAT_FROM: float
        FLOAT_TO: float
        FLOAT_VARIATION: float
        CHANCE: float
        COMBINE_TYPE: int
        GROUP_A: None
        GROUP_B: None
        ICON_SIZE: float
        LOGO_SIZE: float
        RANDOM_SEED: int
        COLOR_COORDINATED: bool
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
        LEVELOFDETAIL: int
        DISPLAYLEVEL: int
        IGNOREBACKFACE: bool
        ONLYCURRENTLEVEL: bool
        VERTEXTYPE: int
        CREASE: float
        MATID: int
        FORCEQUADS: bool
        SMOOTHRESULT: bool
        USESOFTSEL: bool
        USEEDGEDIST: bool
        AFFECTBACKFACE: bool
        EDGEDISTANCE: int
        FALLOFF: float
        PINCH: float
        BUBBLE: float
        ...
    class HSDSObject(Modifier):
        LEVELOFDETAIL: int
        DISPLAYLEVEL: int
        IGNOREBACKFACE: bool
        ONLYCURRENTLEVEL: bool
        VERTEXTYPE: int
        CREASE: float
        MATID: int
        FORCEQUADS: bool
        SMOOTHRESULT: bool
        USESOFTSEL: bool
        USEEDGEDIST: bool
        AFFECTBACKFACE: bool
        EDGEDISTANCE: int
        FALLOFF: float
        PINCH: float
        BUBBLE: float
        ...
    class HSDS_Modifier(Modifier):
        LEVELOFDETAIL: int
        DISPLAYLEVEL: int
        IGNOREBACKFACE: bool
        ONLYCURRENTLEVEL: bool
        VERTEXTYPE: int
        CREASE: float
        MATID: int
        FORCEQUADS: bool
        SMOOTHRESULT: bool
        USESOFTSEL: bool
        USEEDGEDIST: bool
        AFFECTBACKFACE: bool
        EDGEDISTANCE: int
        FALLOFF: float
        PINCH: float
        BUBBLE: float
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
        OVERSAMPLING: int
        OCCLUSIONSETTYPE: int
        OCCLUSIONNODES: MXSWrapperBase
        COMPOSITIONMETHOD: int
        MBINTERVALTYPE: int
        HAIRMODE: int
        LIGHTINGMODE: int
        USEALLLIGHTS: bool
        MBDURATION: float
        SHADOWDENSITY: float
        MRVOXELRES: int
        APPLYGI: bool
        GI_MULTIPLIER: float
        RAYTRACE_REFLECTIONS_REFRACTIONS: bool
        TILEMEMORYUSAGE: int
        TRANSPARENCYDEPTH: int
        ...
    class HairGIAtmospheric(Atmospheric):
        ...
    class HairLightAttr(CustAttrib):
        LIGHTHAIR: bool
        SHADOWRESOLUTION: int
        SHADOWFUZZ: float
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
        HAIRCOUNT: int
        HAIRSEGMENTS: int
        HAIRPASSES: int
        HAIRDENSITY: float
        HAIRSCALE: float
        HAIRCUTLENGTH: float
        HAIRRANDSCALE: float
        HAIRROOTTHICKNESS: float
        HAIRTIPTHICKNESS: float
        HAIRDISPLACEMENT: float
        HAIRINTERPOLATEGUIDES: bool
        MATERIALSELFSHADOW: float
        MATERIALGEOMSHADOW: float
        MATERIALSPECULAR: float
        MATERIALSPECTINT: MXSWrapperBase
        MATERIALGLOSSNESS: float
        MATERIALOCCLUDEDAMB: float
        MATERIALTIPCOLOR: MXSWrapperBase
        MATERIALTIPFADE: bool
        MATERIALHUEVARIATION: float
        MATERIALVALUEVARIATION: float
        MATERIALROOTCOLOR: MXSWrapperBase
        MATERIALMUTANTHAIRCOLOR: MXSWrapperBase
        MATERIALPERCENTMUTANTHAIR: float
        MATERIALGEOMMTLID: int
        MATERIALSQUIRREL: bool
        MATERIALSPECTINT2: MXSWrapperBase
        MR_APPLYSHADER: bool
        MR_SHADER: None
        MR_SUBMTLSTOREPLACE: MXSWrapperBase
        FLYAWAYPERC: int
        FLYAWAYSTREN: float
        MESSSTREN: float
        CLUMPS: int
        CLUMPSSTREN: float
        CLUMPSSCRUFF: float
        CLUMPSROT: float
        CLUMPSOFFSET: float
        CLUMPSCOLORS: float
        CLUMPSRAND: float
        CLUMPSFLAT: float
        FRIZZROOT: float
        FRIZZTIP: float
        FRIZZFREQX: float
        FRIZZFREQY: float
        FRIZZFREQZ: float
        FRIZZANIM: float
        FRIZZANIMSPEED: float
        FRIZZANIMDIR: MXSWrapperBase
        KINKROOT: float
        KINKTIP: float
        KINKFREQX: float
        KINKFREQY: float
        KINKFREQZ: float
        MULTISTRANDCOUNT: int
        MULTISTRANDROOTSPLAY: float
        MULTISTRANDTIPSPLAY: float
        MULTIRANDOMIZE: float
        MULTISTRANDTWIST: float
        MULTISTRANDOFFSET: float
        MULTISTRANDASPECT: float
        DYNAMICSMODE: int
        SIMULATIONSTART: int
        SIMULATIONEND: int
        DYNAMICSSTIFFNESS: float
        DYNAMICSROOTHOLD: float
        DYNAMICSDAMPEN: float
        DYNAMICSGRAVITY: float
        COLLISIONNODES: MXSWrapperBase
        AUTOCOLLISION: bool
        COLLISIONMETHOD: int
        DISPLAYSHOWGUIDES: bool
        DISPLAYGUIDECOLOR: MXSWrapperBase
        DISPLAYSHOWHAIRS: bool
        DISPLAYHAIRASGEOMETRY: bool
        DISPLAYOVERRIDEHAIRCOLOR: bool
        DISPLAYHAIRCOLOR: MXSWrapperBase
        DISPLAYHAIRPERCENT: float
        DISPLAYMAXHAIRS: int
        MAPS: MXSWrapperBase
        MAPENABLES: MXSWrapperBase
        FORCEFIELDS: MXSWrapperBase
        MERGEINSTANCEMATERIAL: bool
        BYVERTEX: bool
        IGNOREBACKFACING: bool
        INSTANCEGEOMNAME: str
        TOOLSSPLINELOCKNODE: None
        RANDOMSEED: int
        ...
    class HairRenderElement(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
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
        VERTICES: MXSWrapperBase
        RADIUS: float
        MAPCOORDS: bool
        FAMILY: int
        P: float
        Q: float
        SCALEP: float
        SCALEQ: float
        SCALER: float
        VERTTYPE: int
        ...
    class HeightMap(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        ...
    class Helix(Shape):
        HEIGHT: float
        BIAS: float
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        RADIUS1: float
        RADIUS2: float
        TURNS: float
        DIRECTION: int
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
        HOSE_HEIGHT: float
        SEGMENTS_ALONG_HOSE: int
        SMOOTH_SPRING: int
        RENDERABLE_HOSE: int
        HOSE_CROSS_SECTION_TYPE: int
        ROUND_HOSE_DIAMETER: float
        ROUND_HOSE_SIDES: int
        RECTANGULAR_HOSE_WIDTH: float
        RECTANGULAR_HOSE_DEPTH: float
        RECTANGULAR_HOSE_FILLET_SIZE: float
        RECTANGULAR_HOSE_FILLET_SEGS: int
        RECTANGULAR_HOSE_SECTION_ROTATION: float
        D_SECTION_HOSE_WIDTH: float
        D_SECTION_HOSE_DEPTH: float
        D_SECTION_HOSE_FILLET_SIZE: float
        D_SECTION_HOSE_FILLET_SEGS: int
        D_SECTION_HOSE_ROUND_SEGS: int
        D_SECTION_HOSE_SECTION_ROTATION: float
        FLEX_SECTION_ENABLED: int
        FLEX_SECTION_START: float
        FLEX_SECTION_STOP: float
        FLEX_CYCLE_COUNT: int
        FLEX_SECTION_DIAMETER: float
        TOP_TENSION: float
        BOTTOM_TENSION: float
        END_PLACEMENT_METHOD: int
        GENERATE_MAPPING_COORDINATES: int
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
        MULTIPLIER: float
        COLOR: MXSWrapperBase
        RAYS_PER_SAMPLE: int
        RAY_BIAS: float
        ON: bool
        CASTSHADOWS: bool
        SKY_COVER: float
        ...
    class IES_Sun(Light):
        RGB: MXSWrapperBase
        MULTIPLIER: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        TARGETDISTANCE: None
        USEGLOBALSHADOWSETTINGS: bool
        HASTARGET: bool
        ON: bool
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        CASTSHADOWS: bool
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
        GROUPS: float
        PAIR: float
        GENDER: float
        ORIENT: float
        ORIENTSPREAD: float
        LOOKAT: None
        LOOKATOBJ: None
        RANDSEEDGROUP: int
        RANDSEEDINDIV: int
        RANDSEEDROT: int
        RANDSEEDGEN: int
        RANDSEEDMTN: int
        ID: int
        ...
    class IdleAreaSubtractArea(Primitive):
        ...
    class IesSkyLight(Light):
        MULTIPLIER: float
        COLOR: MXSWrapperBase
        RAYS_PER_SAMPLE: int
        RAY_BIAS: float
        ON: bool
        CASTSHADOWS: bool
        SKY_COVER: float
        ...
    class IlluminanceFragment(GraphicsFragmentPlugin):
        ...
    class IlluminanceRenderElement(RenderElement):
        ENABLEDON: bool
        FILTERON: bool
        ATMOSPHEREON: bool
        SHADOWON: bool
        ELEMENTNAME: str
        BITMAP: None
        SCALEFACTOR: float
        ...
    class Illuminance_HDR_Data(RenderElement):
        ENABLEDON: bool
        FILTERON: bool
        ATMOSPHEREON: bool
        SHADOWON: bool
        ELEMENTNAME: str
        BITMAP: None
        SCALEFACTOR: float
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
        ON: bool
        NEARDIST: float
        FARDIST: float
        FALLOFFTYPE: int
        ENABLEBIAS: bool
        BIASSELECTED: bool
        BIAS: float
        INVERT: bool
        SHOWNEAR: bool
        SHOWFAR: bool
        NEARCOLOR: MXSWrapperBase
        FARCOLOR: MXSWrapperBase
        ...
    class InitialState(Helper):
        EMIT_TIME: int
        MAX_SPREAD: float
        MAGNITUDE_VARIATION: float
        DIVERGENCE: float
        STATE_FROM_TYPE: int
        PARTICLE_SYSTEM: None
        SELECTED_EVENTS: MXSWrapperBase
        USE_AGE: bool
        USE_SPEED: bool
        USE_SCALE: bool
        USE_ROTATION: bool
        USE_SPIN: bool
        USE_MAPPING: bool
        USE_MATERIAL_ID: bool
        USE_SCRIPT_DATA: bool
        USE_SHAPE: bool
        USE_SELECTION: bool
        LOCK_POSITION: bool
        LOCK_SPEED: bool
        ICON_SIZE: float
        RANDOM_SEED: int
        AUTO_SYNC_EMIT_TIME: bool
        COLOR_COORDINATED: bool
        ...
    class Initial_State(Helper):
        EMIT_TIME: int
        MAX_SPREAD: float
        MAGNITUDE_VARIATION: float
        DIVERGENCE: float
        STATE_FROM_TYPE: int
        PARTICLE_SYSTEM: None
        SELECTED_EVENTS: MXSWrapperBase
        USE_AGE: bool
        USE_SPEED: bool
        USE_SCALE: bool
        USE_ROTATION: bool
        USE_SPIN: bool
        USE_MAPPING: bool
        USE_MATERIAL_ID: bool
        USE_SCRIPT_DATA: bool
        USE_SHAPE: bool
        USE_SELECTION: bool
        LOCK_POSITION: bool
        LOCK_SPEED: bool
        ICON_SIZE: float
        RANDOM_SEED: int
        AUTO_SYNC_EMIT_TIME: bool
        COLOR_COORDINATED: bool
        ...
    class InitializeTimeWarp(BipedGeneric):
        ...
    class Ink(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ...
    class InkNPaint(Material):
        FOG_BG: bool
        BUMP_MAP_ON: bool
        DSP_MAP_ON: bool
        FACE_MAP_ON: bool
        TWO_SIDE_ON: bool
        FACETED_ON: bool
        BUMP_MAP_AMT: float
        DSP_MAP_AMT: float
        BUMP_MAP: None
        DSP_MAP: None
        PIXEL_GRID_ON: bool
        OPAQUE_ALPHA_ON: bool
        MAT1: None
        MAT1_ON: bool
        PAINT_COLOR: MXSWrapperBase
        SPEC_COLOR: MXSWrapperBase
        SPEC_GLOSS: float
        PAINT_LEVELS: int
        PAINT_ON: bool
        SPEC_ON: bool
        PAINT_MAP_ON: bool
        SPEC_MAP_ON: bool
        SUB_MTL_AMT: float
        PAINT_MAP_AMT: float
        SPEC_MAP_AMT: float
        PAINT_MAP: None
        SPEC_MAP: None
        SHADE_COLOR: MXSWrapperBase
        SHADE_COLOR_MAP_ON: bool
        SHADE_COLOR_MAP_AMT: float
        SHADE_COLOR_MAP: None
        SHADE_AMT_ON: bool
        SHADE_AMT: float
        COLOR1: MXSWrapperBase
        MIN_INK_WIDTH: float
        INK_QUALITY: int
        EDGE_ANG_THRESH: float
        SMGROUP_EDGE_INK_COLOR: MXSWrapperBase
        MATID_INK_COLOR: MXSWrapperBase
        EDGE_ANG_INK_COLOR: MXSWrapperBase
        MAX_INK_WIDTH: float
        OUT_INK_ON: bool
        SMGROUP_EDGE_INK_ON: bool
        MATID_INK_ON: bool
        EDGE_ANG_INK_ON: bool
        INK_AUTO_VARY_ON: bool
        WIDTH_MAP_ON: bool
        INK_ON: bool
        OUT_INK_MAP_ON: bool
        SMGROUP_EDGE_MAP_ON: bool
        MATID_MAP_ON: bool
        EDGE_ANG_INK_MAP_ON: bool
        WIDTH_MAP_AMT: float
        OUT_INK_MAP_AMT: float
        SMGROUP_EDGE_MAP_AMT: float
        MATID_MAP_AMT: float
        EDGE_ANG_INK_MAP_AMT: float
        WIDTH_MAP: None
        OUT_INK_MAP: None
        SMGROUP_EDGE_MAP: None
        MATID_MAP: None
        EDGE_ANG_INK_MAP: None
        SELF_OVERLAP_INK_ON: bool
        SELF_OVERLAP_INK_MAP_ON: bool
        SELF_OVERLAP_INK_COLOR: MXSWrapperBase
        SELF_OVERLAP_BIAS: float
        SELF_OVERLAP_INK_MAP_AMT: float
        SELF_OVERLAP_INK_MAP: None
        SELF_UNDERLAP_INK_ON: bool
        SELF_UNDERLAP_INK_MAP_ON: bool
        SELF_UNDERLAP_INK_COLOR: MXSWrapperBase
        SELF_UNDERLAP_BIAS: float
        SELF_UNDERLAP_INK_MAP_AMT: float
        SELF_UNDERLAP_INK_MAP: None
        INTERSECT_BIAS: float
        MATID_ADJ_REQ_ON: bool
        MATID_INTERSECT_BIAS: float
        INK_WIDTH_CLAMP_ON: bool
        SAMPLER: int
        SAMPLERQUALITY: float
        SAMPLERENABLE: bool
        SAMPLERADAPTTHRESHOLD: float
        SAMPLERADAPTON: bool
        SUBSAMPLETEXTUREON: bool
        SAMPLERADVANCEDOPTIONS: bool
        SAMPLERBYNAME: str
        USERPARAM0: float
        USERPARAM1: float
        SAMPLERUSEGLOBAL: bool
        INIT_FAIL_ON: bool
        INIT_FAIL_COLOR: MXSWrapperBase
        BACKFACE_ERROR_ON: bool
        BACKFACE_ERROR_COLOR: MXSWrapperBase
        MISSED_RAYS_ERROR_ON: bool
        MISSED_RAYS_ERROR_COLOR: MXSWrapperBase
        ...
    class InkRenderElement(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ...
    class Inline(Helper):
        ...
    class InputCustom(ReferenceTarget):
        DATA_CHANNEL: None
        DATA_HANDLE: int
        USE_PROXY_PARTICLES: bool
        USE_I2: bool
        I3_USAGE: int
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        ...
    class InputPhysX(ReferenceTarget):
        DATA_TYPE: int
        MATCH_TYPE: int
        THRESHOLD_TYPE: int
        COLLISION_TYPE: int
        FILTER: None
        ...
    class InputProxy(ReferenceTarget):
        USE_I2: bool
        I3_USAGE: int
        DATA_TYPE: int
        PARTICLEID_TYPE: int
        TIME_TYPE: int
        POSITION_TYPE: int
        SPEED_TYPE: int
        ROTATION_TYPE: int
        SPIN_TYPE: int
        SCALE_TYPE: int
        SIZE_TYPE: int
        ADJUSTED_BY_SCALE: bool
        SHAPE_TYPE: int
        SCRIPT_TYPE: int
        TM_TYPE: int
        MAPPING_TYPE: int
        MAP_CHANNEL: int
        GROUP_SELECTION_OPERATOR: None
        GROUP_TYPE: int
        USE_E4: bool
        ACCELERATION_TYPE: int
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        ...
    class InputStandard(ReferenceTarget):
        DATA_TYPE: int
        PARTICLEID_TYPE: int
        TIME_TYPE: int
        POSITION_TYPE: int
        SPEED_TYPE: int
        ROTATION_TYPE: int
        SPIN_TYPE: int
        SCALE_TYPE: int
        SIZE_TYPE: int
        ADJUSTED_BY_SCALE: bool
        SHAPE_TYPE: int
        SCRIPT_TYPE: int
        TM_TYPE: int
        MAPPING_TYPE: int
        MAP_CHANNEL: int
        GROUP_SELECTION_OPERATOR: None
        GROUP_TYPE: int
        USE_E1: bool
        ACCELERATION_TYPE: int
        VISIBILITY_TYPE: int
        VIEWPORT_RENDER_OPERATOR: None
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        ...
    class Input_Proxy(ReferenceTarget):
        USE_I2: bool
        I3_USAGE: int
        DATA_TYPE: int
        PARTICLEID_TYPE: int
        TIME_TYPE: int
        POSITION_TYPE: int
        SPEED_TYPE: int
        ROTATION_TYPE: int
        SPIN_TYPE: int
        SCALE_TYPE: int
        SIZE_TYPE: int
        ADJUSTED_BY_SCALE: bool
        SHAPE_TYPE: int
        SCRIPT_TYPE: int
        TM_TYPE: int
        MAPPING_TYPE: int
        MAP_CHANNEL: int
        GROUP_SELECTION_OPERATOR: None
        GROUP_TYPE: int
        USE_E4: bool
        ACCELERATION_TYPE: int
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        ...
    class Input_MParticles(ReferenceTarget):
        DATA_TYPE: int
        MATCH_TYPE: int
        THRESHOLD_TYPE: int
        COLLISION_TYPE: int
        FILTER: None
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
        FORCE: float
        USE_ACCEL_LIMIT: bool
        ACCEL_LIMIT: float
        USE_SPEED_LIMIT: bool
        SPEED_LIMIT: float
        RANGE_TYPE: int
        CORE_SIZE: float
        FALLOFF_SIZE: float
        CORE_PERCENTAGE: float
        FALLOFF_PERCENTAGE: float
        VARIATION: float
        SCOPE_TYPE: int
        SELECTED_EVENTS: MXSWrapperBase
        SELECTED_SYSTEMS: MXSWrapperBase
        RANDOM_SEED: int
        USE_SCRIPT_FLOAT: int
        USE_SCRIPT_VECTOR: int
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
        STEPTYPE: int
        GENERATESTRINGERS: bool
        GENERATECARRIAGE: bool
        GENERATEINSIDERAILING: bool
        GENERATEOUTSIDERAILING: bool
        STEPWIDTH: float
        STEPTHICKNESS: float
        GENERATEMAPPING: bool
        STEPDEPTH_X: bool
        STEPDEPTH: float
        STEPHEIGHT: float
        STEPCOUNT: int
        STRINGERDEPTH: float
        STRINGERWIDTH: float
        STRINGEROFFSET: float
        STRINGERSPRINGFLOOR: bool
        CARRIAGEWIDTH: float
        CARRIAGEINTOFFS: float
        CARRIAGEEXTOFFS: float
        CARRIAGESPACE: float
        CARRIAGECOUNT: int
        CARRIAGECONTEXT: int
        CARRIAGESPACINGTYPE: int
        CARRIAGEHEIGHT: float
        CARRIAGESPRINGFLOOR: bool
        RAILINGHEIGHT: float
        RAILINGOFFS: float
        RAILINGSEGMENTS: int
        RAILINGRADIUS: float
        LENGTH: float
        LENGTH2: float
        ANGLE: float
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
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINSIDELENGTH: float
        TYPEINFRONTLENGTH: float
        TYPEINSIDEWIDTH: float
        TYPEINFRONTWIDTH: float
        TYPEINHEIGHT: float
        SIDE_LENGTH: float
        FRONT_LENGTH: float
        SIDE_WIDTH: float
        FRONT_WIDTH: float
        HEIGHT: float
        SIDE_SEGMENTS: int
        FRONT_SEGMENTS: int
        WIDTH_SEGMENTS: int
        HEIGHT_SEGMENTS: int
        MAPCOORDS: bool
        CENTERCREATE: bool
        ...
    class L_Type_Stair(GeometryClass):
        STEPTYPE: int
        GENERATESTRINGERS: bool
        GENERATECARRIAGE: bool
        GENERATEINSIDERAILING: bool
        GENERATEOUTSIDERAILING: bool
        STEPWIDTH: float
        STEPTHICKNESS: float
        GENERATEMAPPING: bool
        STEPDEPTH_X: bool
        STEPDEPTH: float
        STEPHEIGHT: float
        STEPCOUNT: int
        STRINGERDEPTH: float
        STRINGERWIDTH: float
        STRINGEROFFSET: float
        STRINGERSPRINGFLOOR: bool
        CARRIAGEWIDTH: float
        CARRIAGEINTOFFS: float
        CARRIAGEEXTOFFS: float
        CARRIAGESPACE: float
        CARRIAGECOUNT: int
        CARRIAGECONTEXT: int
        CARRIAGESPACINGTYPE: int
        CARRIAGEHEIGHT: float
        CARRIAGESPRINGFLOOR: bool
        RAILINGHEIGHT: float
        RAILINGOFFS: float
        RAILINGSEGMENTS: int
        RAILINGRADIUS: float
        LENGTH: float
        LENGTH2: float
        ANGLE: float
        UPPEROFFSET: float
        ...
    class LabelControl(RolloutControl):
        ...
    class LandXMLImport(ImporterPlugin):
        ...
    class LandXML___DEM_Model_Import(ImporterPlugin):
        ...
    class Lathe(Modifier):
        MATIDS: bool
        SMOOTH: bool
        CAPSTART: bool
        CAPEND: bool
        CAPTYPE: int
        WELDCORE: bool
        FLIPNORMALS: bool
        SEGS: int
        MAPCOORDS: bool
        OUTPUT: int
        DEGREES: float
        USESHAPEIDS: bool
        ...
    class Lattice(Modifier):
        STRUT_RADIUS: float
        STRUT_SEGMENTS: int
        STRUT_SIDES: int
        JOINT_RADIUS: float
        JOINT_SEGS: int
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
        SEED: int
        SIZE: float
        ANGLE: float
        INTENSITY: float
        SQUEEZE: float
        AFFECTALPHA: bool
        AFFECTZBUFFER: bool
        DISTAFFECTSSIZE: bool
        DISTAFFECTSINTENSITY: bool
        CENTERAFFECTSSIZE: bool
        CENTERAFFECTSINTENSITY: bool
        INNEROCCLUSIONRADIUS: float
        OCCLUSIONAFFECTSSIZE: bool
        OUTEROCCLUSIONRADIUS: float
        OCCLUSIONAFFECTSINTENSITY: bool
        AFFECTBYATMOSPHERE: bool
        LIGHTDIRECTIONAFFECTSSIZE: bool
        LIGHTDIRECTIONAFFECTSINTENSITY: bool
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
        LIGHTMAP_TEXTURE: None
        DIFFUSE_TEXTURE: None
        DIFFUSE_MAPPING: int
        LIGHTMAP_FILENAME: str
        DIFFUSE_FILENAME: str
        LIGHTMAP_ON: bool
        DIFFUSE_ON: bool
        LIGHTMAP_MAPPING: int
        ...
    class LightMeter(Helper):
        ...
    class LightMeterManager(Interface):
        ...
    class LightTrace(RadiosityEffect):
        RAYS: int
        SKY_LIGHTS: float
        BOUNCES: int
        RAY_BIAS: float
        FILTER_SIZE: float
        SKY_LIGHTS_ON: bool
        GLOBAL_MULTIPLIER: float
        OBJECT_MULTIPLIER: float
        COLOR_BLEED: float
        COLOR_FILTER: MXSWrapperBase
        EXTRA_AMBIENT: MXSWrapperBase
        CONE_ANGLE: float
        VOLUMES_ON: bool
        VOLUMES: float
        ADAPTIVE_UNDERSAMPLING_ON: bool
        INITIAL_SAMPLE_SPACING: int
        SUBDIVIDE_DOWN_TO: int
        SUBDIVISION_CONTRAST: float
        SHOW_SAMPLES: bool
        ...
    class Light_RollAngle_Manipulator(Helper):
        ...
    class Light_Tracer(RadiosityEffect):
        RAYS: int
        SKY_LIGHTS: float
        BOUNCES: int
        RAY_BIAS: float
        FILTER_SIZE: float
        SKY_LIGHTS_ON: bool
        GLOBAL_MULTIPLIER: float
        OBJECT_MULTIPLIER: float
        COLOR_BLEED: float
        COLOR_FILTER: MXSWrapperBase
        EXTRA_AMBIENT: MXSWrapperBase
        CONE_ANGLE: float
        VOLUMES_ON: bool
        VOLUMES: float
        ADAPTIVE_UNDERSAMPLING_ON: bool
        INITIAL_SAMPLE_SPACING: int
        SUBDIVIDE_DOWN_TO: int
        SUBDIVISION_CONTRAST: float
        SHOW_SAMPLES: bool
        ...
    class Lighting(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        SHADOWSON: bool
        DIRECTON: bool
        INDIRECTON: bool
        ...
    class LightingAnalysisOverlay(RenderEffect):
        ...
    class LightingAnalysisOverlayFactory(Interface):
        ...
    class LightingMap(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        SHADOWSON: bool
        DIRECTON: bool
        INDIRECTON: bool
        TARGETMAPSLOTNAME: str
        ...
    class LightingRenderElement(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        SHADOWSON: bool
        DIRECTON: bool
        INDIRECTON: bool
        ...
    class LightingUnits(Interface):
        ...
    class Lighting_Analysis_Data(RenderElement):
        ...
    class Lighting_Analysis_Overlay(RenderEffect):
        ...
    class LightscapeExposureControl(ToneOperator):
        PHYSICALSCALE: float
        CHROMATICADAPTATION: bool
        COLORDIFFERENTIATION: bool
        WHITECOLOR: MXSWrapperBase
        ACTIVE: bool
        PROCESSBG: bool
        BRIGHTNESS: float
        CONTRAST: float
        DAYLIGHT: bool
        EXTERIOR: bool
        EXTERIORDAYLIGHT: bool
        MIDTONES: float
        INDIRECTONLY: bool
        USELEGACYALGORITHM: bool
        ...
    class LimbData2(ReferenceTarget):
        ...
    class LinearShape(Shape):
        ...
    class Linear_Exposure_Control(ToneOperator):
        PHYSICALSCALE: float
        CHROMATICADAPTATION: bool
        COLORDIFFERENTIATION: bool
        WHITECOLOR: MXSWrapperBase
        ACTIVE: bool
        PROCESSBG: bool
        EXPOSUREVALUE: float
        CONTRAST: float
        BRIGHTESS: float
        ...
    class Lines(Shape):
        ...
    class Link(Matrix3Controller):
        KEY_MODE: int
        KEY_NODES_MODE: int
        KEY_HIERARCHY_MODE: int
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
        KEY_MODE: int
        KEY_NODES_MODE: int
        KEY_HIERARCHY_MODE: int
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
        LOCK_TYPE: int
        ANIMATED_SURFACE: bool
        SNAP_TO_SURFACE: bool
        RESTRICT_POSITION_TO_SURFACE: bool
        USE_POSITION_OFFSET_LIMIT: bool
        POSITION_OFFSET_LIMIT: float
        USE_SPEED_LIMIT: bool
        SPEED_LIMIT: float
        POSITION_FORCE: float
        POSITION_DAMPENING_TYPE: int
        DAMPENING_FRICTION: float
        DAMPENING_RESISTANCE: float
        SPEED_UNIT: float
        USE_NO_ACCELERATION_ZONE: bool
        USE_NO_DAMPENING_ZONE: bool
        ZONE_RADIUS: float
        USE_BREAK_OFF_TEST: bool
        BREAK_OFF_TYPE: int
        BREAK_OFF_SPEED: float
        BREAK_OFF_ACCELERATION: float
        BREAK_IF_OUTWARDS_ONLY: bool
        USE_ROTATION_OFFSET_LIMIT: bool
        ROTATION_OFFSET_LIMIT: float
        USE_SPIN_LIMIT: bool
        SPIN_LIMIT: float
        ROTATION_FORCE: float
        ROTATION_DAMPENING: float
        SYNC_TYPE: int
        INDUCED_BY_SPEED_CHANGE: bool
        INERTIAL_SIZE: float
        BREAK_OFF_VARIATION: float
        RANDOM_SEED: int
        LOCK_ON_OBJECTS: MXSWrapperBase
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
        PHYSICALSCALE: float
        CHROMATICADAPTATION: bool
        COLORDIFFERENTIATION: bool
        WHITECOLOR: MXSWrapperBase
        ACTIVE: bool
        PROCESSBG: bool
        BRIGHTNESS: float
        CONTRAST: float
        DAYLIGHT: bool
        EXTERIOR: bool
        EXTERIORDAYLIGHT: bool
        MIDTONES: float
        INDIRECTONLY: bool
        USELEGACYALGORITHM: bool
        ...
    class LookAt_Constraint(RotationController):
        WEIGHT: MXSWrapperBase
        RELATIVE: bool
        LOOKAT_VECTOR_LENGTH: float
        SET_ORIENTATION: bool
        TARGET_AXIS: int
        TARGET_AXISFLIP: bool
        UPNODE_AXIS: int
        UPNODE_WORLD: bool
        PICKUPNODE: None
        STOUP_AXIS: int
        STOUP_AXISFLIP: bool
        VIEWLINE_LENGTH_ABS: bool
        UPNODE_CTRL: int
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
        ENABLEDON: bool
        FILTERON: bool
        ATMOSPHEREON: bool
        SHADOWON: bool
        ELEMENTNAME: str
        BITMAP: None
        SCALEFACTOR: float
        ...
    class Luminance_HDR_Data(RenderElement):
        ENABLEDON: bool
        FILTERON: bool
        ATMOSPHEREON: bool
        SHADOWON: bool
        ELEMENTNAME: str
        BITMAP: None
        SCALEFACTOR: float
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
        PREPASS_ENABLED: bool
        PREPASS_SAMPLES: int
        AA_SAMPLES: int
        GI_DIFFUSE_SAMPLES: int
        GI_DIFFUSE_DEPTH: int
        GI_SPECULAR_SAMPLES: int
        GI_SPECULAR_DEPTH: int
        GI_TRANSMISSION_SAMPLES: int
        GI_TRANSMISSION_DEPTH: int
        GI_SSS_SAMPLES: int
        GI_VOLUME_SAMPLES: int
        GI_VOLUME_DEPTH: int
        ENABLE_ADAPTIVE_SAMPLING: bool
        AA_SAMPLES_MAX: int
        ADAPTIVE_THRESHOLD: float
        PROGRESSIVE_RENDER: bool
        GI_TOTAL_DEPTH: int
        AUTO_TRANSPARENCY_DEPTH: int
        LOW_LIGHT_THRESHOLD: float
        LOCK_SAMPLING_PATTERN: bool
        SSS_USE_AUTOBUMP: bool
        INDIRECT_SPECULAR_BLUR: float
        FILTER: int
        FILTER_WIDTH: float
        AA_SAMPLE_CLAMP_ENABLED: bool
        AA_SAMPLE_CLAMP_AFFECTS_AOVS: bool
        AA_SAMPLE_CLAMP: float
        INDIRECT_SAMPLE_CLAMP: float
        PHYSICAL_MATERIAL_SSS_TYPE: int
        DIELECTRIC_PRIORITIES: bool
        ENV_MODE: int
        ENV_IBL_SAMPLES: int
        ENV_PHYS_BGND_MODE: int
        ENV_PHYS_BGND_COLOR: MXSWrapperBase
        ENV_PHYS_BGND_MAP: None
        ENV_IBL_ENABLE: bool
        ENV_ADV_IBL_MULTIPLIER: float
        ENV_ADV_IBL_VOLUME_SAMPLES: int
        ENV_ADV_IBL_PORTAL_MODE: int
        ENV_ADV_IBL_MAX_BOUNCES: int
        ENV_ADV_IBL_RESOLUTION_ENABLE: bool
        ENV_ADV_IBL_RESOLUTION: int
        ENV_ADV_IBL_EMIT_CAMERA: bool
        ENV_ADV_IBL_EMIT_DIFFUSE: bool
        ENV_ADV_IBL_EMIT_SPECULAR: bool
        ENV_ADV_IBL_EMIT_TRANSMISSION: bool
        ENV_ADV_IBL_AFFECT_SSS: bool
        ENV_ADV_IBL_AFFECT_INDIRECT: bool
        ENV_ADV_IBL_AFFECT_VOLUME: bool
        ENV_ADV_IBL_CAMERA_MULT: float
        ENV_ADV_IBL_DIFFUSE_MULT: float
        ENV_ADV_IBL_SPECULAR_MULT: float
        ENV_ADV_IBL_TRANSMISSION_MULT: float
        ENV_ADV_IBL_SSS_MULT: float
        ENV_ADV_IBL_INDIRECT_MULT: float
        ENV_ADV_IBL_VOLUME_MULT: float
        ENV_ADV_IBL_CAST_SHADOWS: bool
        ENV_ADV_IBL_SHADOW_COLOR: MXSWrapperBase
        ENV_ADV_IBL_SHADOW_DENSITY: float
        ENV_ADV_BGND_MODE: int
        ENV_ADV_BGND_VISIBLE_TO_CAMERA: bool
        ENV_ADV_BGND_VISIBLE_TO_DIFFUSE_REFLECTIONS: bool
        ENV_ADV_BGND_VISIBLE_TO_SPECULAR_REFLECTIONS: bool
        ENV_ADV_BGND_VISIBLE_TO_DIFFUSE_TRANSMISSION: bool
        ENV_ADV_BGND_VISIBLE_TO_SPECULAR_TRANSMISSION: bool
        ENV_ADV_BGND_VISIBLE_TO_VOLUME_SCATTERING: bool
        ENV_ADV_BGND_CUSTOM_COLOR: MXSWrapperBase
        ENV_ADV_BGND_CUSTOM_MAP: None
        ENV_ADV_BGND_CUSTOM_SHADER: None
        ATMOSPHERE: None
        RESPECT_PHYSICAL_CAMERA_MOTION_BLUR: bool
        ENABLE_TRANSFORM_KEYS: bool
        TRANSFORM_KEYS: int
        ENABLE_DEFORM_KEYS: bool
        DEFORM_KEYS: int
        SHUTTER_LENGTH: float
        SHUTTER_POSITION: int
        AUTO_SHUTTER: bool
        SHUTTER_OPEN: float
        SHUTTER_CLOSE: float
        SHUTTER_TYPE: int
        IGNORE_MOTION_BLUR: bool
        MAX_SUBDIVISIONS: int
        GEOMETRY_DICING_CAMERA: None
        SUBDIV_FRUSTUM_CULLING: bool
        SUBDIV_FRUSTUM_PADDING: float
        DISPLACEMENT_DEFAULT_SUBDIV_TYPE: int
        DISPLACEMENT_DEFAULT_SUBDIV_ITERATIONS: int
        DISPLACEMENT_DEFAULT_SUBDIV_ADAPTIVE_ERROR: float
        CURVES_DEFAULT_BASIS: int
        CURVES_DEFAULT_MODE: int
        CURVES_DEFAULT_MIN_PIXEL_WIDTH: float
        TEXTURE_AUTOMIP: bool
        TEXTURE_ACCEPT_UNMIPPED: bool
        TEXTURE_ENABLE_AUTOTILE: bool
        TEXTURE_AUTOTILE: int
        TEXTURE_ACCEPT_UNTILED: bool
        USE_EXISTING_TX: bool
        TEXTURE_MAX_MEMORY_MB: int
        TEXTURE_MAX_OPEN_FILES: int
        GPU_MAX_TEXTURE_RESOLUTION: int
        BUCKET_SCANNING: int
        BUCKET_SIZE: int
        SHOW_BUCKET_CORNERS_PROD: bool
        SHOW_BUCKET_CORNERS_AS: bool
        ABORT_ON_LICENSE_FAIL: bool
        SKIP_LICENSE_CHECK: bool
        LEGACY_3DS_MAX_MAP_SUPPORT: bool
        AUTODETECT_THREADS: bool
        THREADS: int
        GPU_SELECTION: MXSWrapperBase
        GPU_RENDERING: bool
        RENDER_DEVICE: int
        RENDER_DEVICE_FALLBACK: int
        DEFAULT_GPU_NAMES: str
        DEFAULT_GPU_MIN_MEMORY_MB: int
        GPU_AUTO_SELECTION: bool
        USE_OPTIX_ON_BEAUTY: bool
        NOICE_INPUT: str
        NOICE_OUTPUT: str
        NOICE_ANIM_RANGE: int
        NOICE_START_FRAME: int
        NOICE_END_FRAME: int
        NOICE_ADDITIONAL_FRAMES: int
        NOICE_VARIANCE: float
        NOICE_SEARCH_RADIUS: int
        NOICE_PATCH_RADIUS: int
        NOICE_LIGHT_AOV_NAMES: str
        OUTPUT_DENOISING_AOVS: bool
        PROCEDURAL_SEARCHPATH: None
        PLUGIN_SEARCHPATH: None
        TEXTURE_SEARCHPATH: None
        VERBOSITY_LEVEL: int
        LOG_TO_CONSOLE: bool
        LOG_TO_FILE: bool
        LOG_FILE: None
        MAX_WARNINGS: int
        TEXTURE_PER_FILE_STATS: bool
        LOG_RENDER_STATS: bool
        RENDER_STATS_FILE: None
        RENDER_STATS_MODE: int
        LOG_RENDER_PROFILE: bool
        RENDER_PROFILE_FILE: None
        ABORT_ON_ERROR: bool
        ABORT_ON_ERROR_ACTIVESHADE: bool
        ERROR_COLOR_BAD_TEXTURE: MXSWrapperBase
        ERROR_COLOR_BAD_SHADER: MXSWrapperBase
        ERROR_COLOR_BAD_PIXEL: MXSWrapperBase
        IGNORE_TEXTURES: bool
        IGNORE_SHADERS: bool
        IGNORE_ATMOSPHERE: bool
        IGNORE_LIGHTS: bool
        IGNORE_SHADOWS: bool
        IGNORE_SUBDIVISION: bool
        IGNORE_DISPLACEMENT: bool
        IGNORE_BUMP: bool
        IGNORE_SMOOTHING: bool
        IGNORE_MOTION: bool
        IGNORE_DOF: bool
        IGNORE_SSS: bool
        IGNORE_OPERATORS: bool
        SHADER_OVERRIDE_ENABLED: bool
        SHADER_OVERRIDE: None
        ENABLE_USER_OPTIONS: bool
        USER_OPTIONS: None
        EXPORT_TO_ASS: bool
        ASS_FILE_PATH: None
        EXPORT_OPTION: bool
        EXPORT_CAMERAS: bool
        EXPORT_DRIVERSFILTERS: bool
        EXPORT_LIGHTS: bool
        EXPORT_GEOMETRY: bool
        EXPORT_SHADERS: bool
        EXPORT_OPERATORS: bool
        EXPORT_BINARY: bool
        EXPAND_PROCEDURALS: bool
        EXPORT_TO_MTLX: bool
        MTLX_FILE_PATH: None
        MTLX_LOOK: str
        MTLX_PROPERTIES: None
        MTLX_RELATIVE: bool
        MTLX_USE_CURRENT_SELECTION: bool
        OPERATOR_ROOT: None
        OPERATOR_EXPORT_LIST: MXSWrapperBase
        OPERATOR_EXPORT_TREE: bool
        MATERIAL_EXPORT_LIST: MXSWrapperBase
        RETRANSLATE_ALL_FRAMES: bool
        USE_QUADS: int
        EXPORT_TO_ASS_ORIGIN: int
        USE_RENDER_VIEW: bool
        RENDER_VIEW_SETTINGS: str
        IMAGER_0: None
        AOV_MANAGER: None
        DRIVER_TYPE: None
        AOV_SHADERS_MAT_0: None
        AOV_SHADERS_MAT_1: None
        AOV_SHADERS_MAT_2: None
        AOV_SHADERS_MAP_0: None
        AOV_SHADERS_MAP_1: None
        AOV_SHADERS_MAP_2: None
        ...
    class MAXtoA_Menu(GlobalUtilityPlugin):
        ...
    class MAXtoA_OperatorCustomAttribute(CustAttrib):
        ...
    class MCG_Donut(Shape):
        RADIUS1: float
        RADIUS2: float
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class MCG_MeshEdgesToSpline(Shape):
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class MCG_SinWave(Shape):
        SEGMENTS: int
        DOMAIN: float
        RANGE: float
        OFFSET: float
        AMPLITUDE: float
        CLOSED: bool
        SMOOTHING_FACTOR: float
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class MCG_LookAt(RotationController):
        BILLBOARD: bool
        TARGETAXISFLIP: bool
        TARGETS_TAB: MXSWrapperBase
        WEIGHTS_TAB: MXSWrapperBase
        TARGETAXIS: int
        UPNODEAXIS: int
        SRCUPNODEAXISFLIP: bool
        UPNODECONTROL: int
        UPNODEALIGNAXIS: int
        UPNODEWORLD: bool
        UPNODE: None
        ROTYOFFSET: float
        ROTXOFFSET: float
        ROTZOFFSET: float
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class MCG_RayToSurfaceOrientation(RotationController):
        SURFACES_TAB: MXSWrapperBase
        RAY_TO_SURFACE_PIVOT: bool
        RAY_ORIGIN: None
        FLIP: bool
        RAY_AXIS: int
        LCLUPAXIS: int
        USE_SURFACE_NORMAL: bool
        LCLFWDAXIS: int
        USE_FORWARD_OBJECT: bool
        FORWARD_OBJECT: None
        WORLD_AXIS: int
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class MCG_RayToSurfacePosition(PositionController):
        SURFACES_TAB: MXSWrapperBase
        RAY_TO_SURFACE_PIVOT: bool
        RAY_ORIGIN: None
        FLIP: bool
        RAY_AXIS: int
        USE_SURFACE_NORMAL: bool
        OFFSET: float
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class MCG_RayToSurfaceTransform(Matrix3Controller):
        SURFACES_TAB: MXSWrapperBase
        RAY_TO_SURFACE_PIVOT: bool
        RAY_ORIGIN: None
        FLIP: bool
        RAY_AXIS: int
        LCLUPAXIS: int
        USE_SURFACE_NORMAL: bool
        LCLFWDAXIS: int
        USE_FORWARD_OBJECT: bool
        FORWARD_OBJECT: None
        WORLD_AXIS: int
        OFFSET: float
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        ...
    class MCG_RotationalSpring1DOFTransform(Matrix3Controller):
        PARENT_OBJECT: None
        GEOMETRY_HULL: None
        MASS: float
        AXIS_XYZ: int
        LOWERLIMIT: float
        UPPERLIMIT: float
        LIMITISREVERSED: bool
        DAMPING: float
        BOUNCE: float
        STIFFNESS: float
        GRAVITY: float
        DEACTIVATE_SPRING: bool
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        STEPSPERFRAME: float
        ...
    class MCG_RotationalSpring3DOFTransform(Matrix3Controller):
        PARENT_OBJECT: None
        GEOMETRY_HULL: None
        MASS: float
        USEAXISLIMITS: bool
        LOWERLIMITX: float
        LOWERLIMITY: float
        LOWERLIMITZ: float
        UPPERLIMITX: float
        UPPERLIMITY: float
        UPPERLIMITZ: float
        DAMPING: float
        BOUNCE: float
        STIFFNESS: float
        GRAVITY: float
        DEACTIVATE_SPRING: bool
        _DUMMY: bool
        PLUGINGRAPH: str
        PLUGINGRAPHDEPENDENCIES: MXSWrapperBase
        STEPSPERFRAME: float
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
        ELEMENTNAME: str
        SIZE: float
        INTENSITY: float
        PLANE: float
        SIDES: int
        ON: bool
        SQUEEZE: bool
        OCCLUSION: float
        PRESETS: int
        COLORSOURCE: float
        RADIALCOLOR1: MXSWrapperBase
        RADIALCOLOR2: MXSWrapperBase
        RADIALCOLOR3: MXSWrapperBase
        RADIALCOLOR4: MXSWrapperBase
        COLORRADIUS1: float
        COLORRADIUS2: float
        COLORRADIUS3: float
        COLORRADIUS4: float
        RADIALMTL: None
        USERADIALMTL: bool
        RADIALMAP: None
        USERADIALMAP: bool
        CIRCULARCOLORMIX: float
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        QUADRANT4COLOR: MXSWrapperBase
        CIRCULARMTL: None
        USECIRCULARMTL: bool
        CIRCULARMAP: None
        USECIRCULARMAP: bool
        RADIALSIZEMAP: None
        USERADIALSIZEMAP: bool
        APPLYLIGHTS: bool
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        SOURCEOBJECTID: bool
        OBJECTID: int
        SOURCEEFFECTSID: bool
        EFFECTSID: int
        SOURCEUNCLAMPEDCOLOR: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        SOURCESURFACENORMAL: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        SOURCEWHOLE: bool
        SOURCEALPHA: bool
        ALPHA: int
        SOURCEZBUFFER: bool
        ZHI: float
        ZLO: float
        FILTERALL: bool
        FILTEREDGE: bool
        FILTERPERIMETERALPHA: bool
        FILTERPERIMETER: bool
        FILTERBRIGHTNESS: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        FILTERHUE: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        APPLYNOISE: bool
        NOISEMAP: None
        RADIALDENSITY: None
        USERADIALDENSITY: bool
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
        ELEMENTNAME: str
        SIZE: float
        INTENSITY: float
        PLANE: float
        SIDES: int
        ON: bool
        SQUEEZE: bool
        OCCLUSION: float
        PRESETS: int
        COLORSOURCE: float
        RADIALCOLOR1: MXSWrapperBase
        RADIALCOLOR2: MXSWrapperBase
        RADIALCOLOR3: MXSWrapperBase
        RADIALCOLOR4: MXSWrapperBase
        COLORRADIUS1: float
        COLORRADIUS2: float
        COLORRADIUS3: float
        COLORRADIUS4: float
        RADIALMTL: None
        USERADIALMTL: bool
        RADIALMAP: None
        USERADIALMAP: bool
        CIRCULARCOLORMIX: float
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        QUADRANT4COLOR: MXSWrapperBase
        CIRCULARMTL: None
        USECIRCULARMTL: bool
        CIRCULARMAP: None
        USECIRCULARMAP: bool
        RADIALSIZEMAP: None
        USERADIALSIZEMAP: bool
        APPLYLIGHTS: bool
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        SOURCEOBJECTID: bool
        OBJECTID: int
        SOURCEEFFECTSID: bool
        EFFECTSID: int
        SOURCEUNCLAMPEDCOLOR: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        SOURCESURFACENORMAL: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        SOURCEWHOLE: bool
        SOURCEALPHA: bool
        ALPHA: int
        SOURCEZBUFFER: bool
        ZHI: float
        ZLO: float
        FILTERALL: bool
        FILTEREDGE: bool
        FILTERPERIMETERALPHA: bool
        FILTERPERIMETER: bool
        FILTERBRIGHTNESS: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        FILTERHUE: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        APPLYNOISE: bool
        NOISEMAP: None
        RADIALDENSITY: None
        USERADIALDENSITY: bool
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
        SCALE: float
        UOFFSET: float
        VOFFSET: float
        WRAP: bool
        CHANNEL: int
        UPDIRECTION: int
        WRAPUSINGSMOOTHINGGROUPS: bool
        ...
    class MapScalerModifier(Modifier):
        SCALE: float
        UOFFSET: float
        VOFFSET: float
        WRAP: bool
        CHANNEL: int
        WRAPUSINGSMOOTHINGGROUPS: bool
        ...
    class MapScalerOSM(Modifier):
        SCALE: float
        UOFFSET: float
        VOFFSET: float
        WRAP: bool
        CHANNEL: int
        WRAPUSINGSMOOTHINGGROUPS: bool
        ...
    class MapScalerSpaceWarp(SpacewarpObject):
        ...
    class MapScalerSpacewarpModifier(SpacewarpModifier):
        SCALE: float
        UOFFSET: float
        VOFFSET: float
        WRAP: bool
        CHANNEL: int
        UPDIRECTION: int
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
        MAPPING_TYPE: int
        ACQUIRE_SUBMATERIAL_INDEX: bool
        UNIFORM_COLOR_PER_PARTICLE: bool
        MAPPING_FROM_OBJECTS: MXSWrapperBase
        STATIC_OBJECTS: bool
        ANIMATED_SURFACE: bool
        ACQUIRE_FROM_MAPPING_CHANNELS: MXSWrapperBase
        USE_VERTEX_COLOR: bool
        U_VARIATION: float
        V_VARIATION: float
        W_VARIATION: float
        EXCLUDE_TILING: bool
        BLEND_MAPPING_BY_TIME: bool
        BLEND_TYPE: int
        BLEND_TIME: int
        BLEND_MAPPING_BY_DISTANCE: bool
        FINISH_DISTANCE: float
        SHOW_MAP_IN_VIEWPORT: bool
        RANDOM_SEED: int
        ...
    class Mapping_Object(Helper):
        MAPPING_TYPE: int
        ACQUIRE_SUBMATERIAL_INDEX: bool
        UNIFORM_COLOR_PER_PARTICLE: bool
        MAPPING_FROM_OBJECTS: MXSWrapperBase
        STATIC_OBJECTS: bool
        ANIMATED_SURFACE: bool
        ACQUIRE_FROM_MAPPING_CHANNELS: MXSWrapperBase
        USE_VERTEX_COLOR: bool
        U_VARIATION: float
        V_VARIATION: float
        W_VARIATION: float
        EXCLUDE_TILING: bool
        BLEND_MAPPING_BY_TIME: bool
        BLEND_TYPE: int
        BLEND_TIME: int
        BLEND_MAPPING_BY_DISTANCE: bool
        FINISH_DISTANCE: float
        SHOW_MAP_IN_VIEWPORT: bool
        RANDOM_SEED: int
        ...
    class Marble(TextureMap):
        MAP1: None
        MAP2: None
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        SIZE: float
        WIDTH: float
        COORDS: MXSWrapperBase
        ...
    class Mask(TextureMap):
        MAP: None
        MASK: None
        MAPENABLED: bool
        MASKENABLED: bool
        MASKINVERTED: bool
        ...
    class MassFX_Loader_Linkage(GlobalUtilityPlugin):
        ...
    class MassFX_RBody(Modifier):
        TYPE: int
        SWITCHTYPE: bool
        SWITCHTYPEATFRAME: int
        ENABLEGRAVITY: bool
        CONTINUOUSCOLLISIONDETECTION: bool
        SLEEPATSTART: bool
        COLLIDEWITHRIGIDBODIES: bool
        EXTRASHAPES: None
        MANUALSETUP: bool
        MATERIALID: int
        DENSITY: float
        VOLUME: float
        MASS: float
        STATICFRICTION: float
        DYNAMICFRICTION: float
        BOUNCINESS: float
        ENABLEADVANCEDSETTINGS: int
        CONTACTSHELLOVERRIDEGLOBALS: bool
        CONTACTSHELLCONTACTDISTANCE: float
        CONTACTSHELLRESTDEPTH: float
        SOLVERITER: bool
        SOLVERITERVALUE: int
        INITIALMOTIONSTYLE: int
        INITIALVELOCITYX: float
        INITIALVELOCITYY: float
        INITIALVELOCITYZ: float
        VELOCITYSPEED: float
        INITIALSPINX: float
        INITIALSPINY: float
        INITIALSPINZ: float
        SPINSPEED: float
        MASSCENTERX: float
        MASSCENTERY: float
        MASSCENTERZ: float
        LINEARDAMPING: float
        ANGULARDAMPING: float
        BAKED: int
        MESHTYPE: int
        MESHCUSTOMMESH: None
        MESHVERTICESLIMIT: int
        MESHINFLATION: float
        MESHCONVEXSTYLE: int
        MESHRADIUS: float
        MESHLENGTH: float
        MESHWIDTH: float
        MESHHEIGHT: float
        MESHOVERRIDEMATERIAL: bool
        COMPOSITEMAXVERTICES: int
        COMPOSITEMAXCONCAVITY: float
        SMALLCLUSTERTHRESHOLD: float
        ENABLESOLIDMESHES: bool
        COMPOSITEHIGHQUALITY: bool
        MASSCENTERMODE: int
        ENABLEBACKFACECOLLISION: bool
        FORCESLIST: MXSWrapperBase
        SHOWPHYSICALMESH: bool
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
        RANDOM_SEED: int
        METHOD: int
        MATERIAL_ID__1: float
        MATERIAL_ID__2: float
        MATERIAL_ID__3: float
        MATERIAL_ID__4: float
        MATERIAL_ID__5: float
        MATERIAL_ID__6: float
        MATERIAL_ID__7: float
        MATERIAL_ID__8: float
        MATERIAL_ID_COUNT: int
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
        ASSIGN_MATERIAL: bool
        ASSIGNED_MATERIAL: None
        ASSIGN_MATERIAL_ID: bool
        SHOW_IN_VIEWPORT: bool
        SUBMTL_ID_OFFSET: int
        TYPE: int
        RESET_PARTICLE_AGE: bool
        RANDOMIZE_AGE: bool
        MAX_AGE_OFFSET: MXSWrapperBase
        MATERIAL_ID: int
        NUMBER_OF_SUB_MATERIALS: int
        SUB_MATERIALS_RATE: float
        LOOP: bool
        SYNC_TYPE: int
        ADD_RANDOM_OFFSET: bool
        RANDOM_OFFSET: int
        RANDOM_SEED: int
        ...
    class Material_Editor(Value):
        ...
    class Material_EditorReferenceMaker(ReferenceMaker):
        ...
    class Material_Frequency(Helper):
        ASSIGN_MATERIAL: bool
        ASSIGNED_MATERIAL: None
        ASSIGN_MATERIAL_ID: bool
        SHOW_IN_VIEWPORT: bool
        SUBMTL_ID_OFFSET: int
        MTL_ID_1: float
        MTL_ID_2: float
        MTL_ID_3: float
        MTL_ID_4: float
        MTL_ID_5: float
        MTL_ID_6: float
        MTL_ID_7: float
        MTL_ID_8: float
        MTL_ID_9: float
        MTL_ID_10: float
        RANDOM_SEED: int
        ...
    class Material_ID(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ...
    class Material_Static(Helper):
        ASSIGN_MATERIAL: bool
        ASSIGNED_MATERIAL: None
        ASSIGN_MATERIAL_ID: bool
        SHOW_IN_VIEWPORT: bool
        SUBMTL_ID_OFFSET: int
        TYPE: int
        MATERIAL_ID: int
        NUMBER_OF_SUB_MATERIALS: int
        RATE_TYPE: int
        RATE_PER_SECOND: float
        RATE_PER_PARTICLE: float
        LOOP: bool
        RANDOM_SEED: int
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
        OPAQUEALPHA: bool
        APPLYATMOSPHERE: bool
        ATMOSPHEREDEPTH: int
        RECEIVESHADOWS: bool
        AFFECTALPHA: bool
        SHADOWBRIGHTNESS: float
        COLOR: MXSWrapperBase
        AMOUNT: float
        MAP: None
        USEREFLMAP: bool
        ADDITIVEREFLECTION: int
        ...
    class MatteRenderElement(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        MTLIDON: bool
        GBUFIDON: bool
        GBUFID: int
        MTLID: int
        INCLUDEON: bool
        ...
    class MatteShadow(Material):
        OPAQUEALPHA: bool
        APPLYATMOSPHERE: bool
        ATMOSPHEREDEPTH: int
        RECEIVESHADOWS: bool
        AFFECTALPHA: bool
        SHADOWBRIGHTNESS: float
        COLOR: MXSWrapperBase
        AMOUNT: float
        MAP: None
        USEREFLMAP: bool
        ADDITIVEREFLECTION: int
        ...
    class MaxFluidSolverClass(MAXWrapper):
        ...
    class MaxLiquid(GeometryClass):
        ICONSIZE: float
        SOLVERS: MXSWrapperBase
        EMITTERTYPE: int
        EMITTERLENGTH: float
        EMITTERWIDTH: float
        EMITTERHEIGHT: float
        EMITTER_MESHES: MXSWrapperBase
        COLLIDER_MESHES: MXSWrapperBase
        FOAMMASK_MESHES: MXSWrapperBase
        GUIDE_MESHES: MXSWrapperBase
        FIELD_MESHES: MXSWrapperBase
        KILLPLANES: MXSWrapperBase
        ACCELERATOR_MESHES: MXSWrapperBase
        KILLVOLUMENODE: None
        SCRATCHCACHE: str
        MAXSCRATCHCACHERAM: float
        USEPROJECTFOLDERS: bool
        ROOTSIMDIRECTORY: str
        CACHEOUTPUTFILEPATTERN: str
        EXPORTPRTFILES: bool
        LASTSELECTEDSOLVERINDEX: int
        RENDERSOLVEINDEX: int
        RENDERSOLVELOCK: bool
        SHOWVOXELGRID: bool
        GUIDEEMITTER_MESHES: MXSWrapperBase
        SHOWICON: bool
        DISPLAYCACHELIMITENABLE: bool
        DISPLAYCACHELIMIT: float
        ENABLEGPUPOINTS: bool
        CHANNELFIELD_MESHES: MXSWrapperBase
        ...
    class MaxLiquidSolver(MaxFluidSolverClass):
        ...
    class MaxMotionClipImp(MasterBlockController):
        GLOBALCLIPASSOCIATIONS: MXSWrapperBase
        CLIPASSOCIATIONS: MXSWrapperBase
        ...
    class MaxMotionClipMaster(CtrlUserDataTypeClass):
        ...
    class MaxMotionField(SpacewarpObject):
        MAGNITUDEUI: float
        MAGNITUDE: float
        EVALUATIONTYPE: int
        ENABLE: bool
        ENABLETURBULENCE: bool
        ENABLEVELOCITYSPEED: bool
        ENABLEGEOMETRY: bool
        ENABLEBOUNDARY: bool
        ENABLEDIRECTION: bool
        ENABLEDRAG: bool
        VELOCITYGRID: bool
        VELOCITYGRIDRESOLUTION: int
        VELOCITYDRAWSCALE: float
        BOUNDARYSHAPE: int
        WIDTH: float
        LENGTH: float
        FIELDMAXDEPTH: float
        SECTIONRADIUS: float
        HEIGHT: float
        ENABLEMAXDEPTH: bool
        BOUNDARYFALLOFF: float
        RADIUS: float
        INVERTFALLOFF: bool
        DIRECTIONMAGNITUDE: float
        ENABLECONCENTRIC: bool
        CONCENTRICMAGNITUDE: float
        ENABLEALONGAXIS: bool
        ALONGAXISMAGNITUDE: float
        ENABLEAROUNDAXIS: bool
        AROUNDAXISMAGNITUDE: float
        ENABLEAWAYFROMAXIS: bool
        AWAYFROMAXISMAGNITUDE: float
        DRAG: float
        NORMALDRAG: float
        TURBULENCEMAGNITUDE: float
        TURBULENCEFREQUENCY: float
        TURBULENCESPEED: float
        TURBULENCESCALEX: float
        TURBULENCESCALEY: float
        TURBULENCESCALEZ: float
        TURBULENCEOFFSETX: float
        TURBULENCEOFFSETY: float
        TURBULENCEOFFSETZ: float
        TURBULENCETYPE: int
        WORLDSPACETURBULENCE: bool
        ENABLENOISE: bool
        NOISEMAGNITUDE: float
        TURBULENCETIME: float
        TURBULENCESCALE: MXSWrapperBase
        TURBULENCEOFFSET: MXSWrapperBase
        ENABLEGEOMETRYFALLOFF: bool
        GEOMETRYMINDISTANCE: float
        GEOMETRYMAXDISTANCE: float
        GEOMETRYALONGNORMAL: float
        GEOMETRYFRICTION: float
        INHERITVELOCITY: float
        MOTIONFIELDS_MESHES: None
        MOTIONFIELDS_PROXYOBJECTNAME: str
        MOTIONFIELDS_VOXELSCALE: float
        MOTIONFIELDS_ENABLEBOUNDARY: bool
        MOTIONFIELDS_BOUNDARYSHAPE: int
        MOTIONFIELDS_TRANSFORM: MXSWrapperBase
        MOTIONFIELDS_INVERT: bool
        ENABLEVELOCITYSCALE: bool
        VELOCITYSCALEX: float
        VELOCITYSCALEY: float
        VELOCITYSCALEZ: float
        CLAMPSPEED: bool
        MINSPEED: float
        MAXSPEED: float
        VELOCITYSCALE: MXSWrapperBase
        DIRECTION: MXSWrapperBase
        DIRECTIONZ: float
        DIRECTIONY: float
        DIRECTIONX: float
        TRANSFORM: MXSWrapperBase
        SCALEAFFECTSSPEED: bool
        DRAWTIMESPAN: int
        ICONSIZE: float
        DRAWVELOCITYARROWS: bool
        DRAWADDITIVEVELOCITY: bool
        COLOROPTIONS: int
        STARTCOLOR: MXSWrapperBase
        ENDCOLOR: MXSWrapperBase
        SAMPLEOPTIONS: int
        TEMPSPEEDFIX: int
        ENABLEDISPLAY: bool
        ENABLEDIRECTIONROLLUP: bool
        ENABLEVELOCITYROLLUP: bool
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
        GLOBALCLIPASSOCIATIONS: MXSWrapperBase
        CLIPASSOCIATIONS: MXSWrapperBase
        ...
    class MaxscriptParticleContainer(ReferenceTarget):
        ...
    class Mb_Select(GlobalUtilityPlugin):
        ...
    class Measure(UtilityPlugin):
        ...
    class Melt(Modifier):
        AXIS: int
        SPREAD: float
        CONFINE_TO_GIZMO: int
        CUT_OFF__OBSOLETE: float
        SOLIDITY_PRESET: int
        SOLIDITY_CUSTOM_VALUE: float
        NEGATIVE_AXIS: int
        MELT_AMOUNT: float
        ...
    class MemoryTargetToOGSTargetFragment(GraphicsFragmentPlugin):
        ...
    class MeshCollision(ReferenceMaker):
        ...
    class MeshDeformPW(Modifier):
        MESH: None
        THRESHOLD: float
        ENGINE: int
        FALLOFF: float
        DISTANCE: float
        FACELIMIT: int
        SHOWLOOPS: bool
        SHOWAXIS: bool
        SHOWFACELIMIT: bool
        SHOWMIRRORDATA: bool
        MIRRORPLANE: int
        MIRROROFFSET: float
        MESHLIST: MXSWrapperBase
        SHOWUNASSIGNEDVERTS: bool
        SHOWVERTS: bool
        WEIGHTALLVERTS: bool
        MIRRORTHRESHOLD: float
        BLEND: bool
        BLENDDISTANCE: float
        ...
    class MeshINI(Interface):
        ...
    class MeshInspector(Interface):
        ...
    class MeshProjIntersect(ReferenceTarget):
        ...
    class MeshSelect(Modifier):
        USESOFTSELECTION: bool
        SOFTSELUSEEDGEDISTANCE: bool
        SOFTSELEDGEDIST: int
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELBUBBLE: float
        BYVERTEX: bool
        IGNOREBACKFACING: bool
        MATERIALID: int
        IGNOREVISIBLEEDGES: bool
        PLANARTHRESHOLD: float
        ...
    class Mesh_Select(Modifier):
        USESOFTSELECTION: bool
        SOFTSELUSEEDGEDISTANCE: bool
        SOFTSELEDGEDIST: int
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELBUBBLE: float
        BYVERTEX: bool
        IGNOREBACKFACING: bool
        MATERIALID: int
        IGNOREVISIBLEEDGES: bool
        PLANARTHRESHOLD: float
        ...
    class Mesher(GeometryClass):
        PICK: None
        RENDERTIMEONLY: bool
        TIME: float
        RADIUS: float
        USECUSTOMBOUNDS: bool
        BOUNDSMIN: MXSWrapperBase
        BOUNDSMAX: MXSWrapperBase
        USEALLPFEVENTS: bool
        PFEVENTLIST: MXSWrapperBase
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
        DIFFUSE: None
        NORMAL: None
        DETAIL: None
        MASK: None
        REFLECTION: None
        BUMP: None
        DIFFUSE_ON: bool
        NORMAL_ON: bool
        SPECULAR_ON: bool
        DETAIL_ON: bool
        MASK_ON: bool
        REFLECTION_ON: bool
        BUMP_ON: bool
        SPIN_BUMPSCALE: int
        SPIN_TEXSCALE: int
        SPIN_ALPHA: float
        COLOR_AMBIENT: MXSWrapperBase
        COLOR_DIFFUSE: MXSWrapperBase
        COLOR_SPECULAR: MXSWrapperBase
        MAP_DIFFUSE1: int
        MAP_DIFFUSE2: int
        MAP_SPECULAR: int
        MAP_BUMP: int
        SYNC: bool
        SPIN_REFLECTSCALE: int
        ALPHA_ON: bool
        ...
    class Metal_Bump9(ReferenceTarget):
        DIFFUSE: None
        NORMAL: None
        DETAIL: None
        MASK: None
        REFLECTION: None
        BUMP: None
        DIFFUSE_ON: bool
        NORMAL_ON: bool
        SPECULAR_ON: bool
        DETAIL_ON: bool
        MASK_ON: bool
        REFLECTION_ON: bool
        BUMP_ON: bool
        SPIN_BUMPSCALE: int
        SPIN_TEXSCALE: int
        SPIN_ALPHA: float
        COLOR_AMBIENT: MXSWrapperBase
        COLOR_DIFFUSE: MXSWrapperBase
        COLOR_SPECULAR: MXSWrapperBase
        MAP_DIFFUSE1: int
        MAP_DIFFUSE2: int
        MAP_SPECULAR: int
        MAP_BUMP: int
        SYNC: bool
        SPIN_REFLECTSCALE: int
        ALPHA_ON: bool
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
        MIXAMOUNT: float
        LOWER: float
        UPPER: float
        USECURVE: bool
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1: None
        MAP2: None
        MASK: None
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        MASKENABLED: bool
        OUTPUT: MXSWrapperBase
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
        TYPE: int
        SWITCHTYPE: bool
        SWITCHTYPEATFRAME: int
        ENABLEGRAVITY: bool
        CONTINUOUSCOLLISIONDETECTION: bool
        SLEEPATSTART: bool
        COLLIDEWITHRIGIDBODIES: bool
        EXTRASHAPES: None
        MANUALSETUP: bool
        MATERIALID: int
        DENSITY: float
        VOLUME: float
        MASS: float
        STATICFRICTION: float
        DYNAMICFRICTION: float
        BOUNCINESS: float
        ENABLEADVANCEDSETTINGS: int
        CONTACTSHELLOVERRIDEGLOBALS: bool
        CONTACTSHELLCONTACTDISTANCE: float
        CONTACTSHELLRESTDEPTH: float
        SOLVERITER: bool
        SOLVERITERVALUE: int
        INITIALMOTIONSTYLE: int
        INITIALVELOCITYX: float
        INITIALVELOCITYY: float
        INITIALVELOCITYZ: float
        VELOCITYSPEED: float
        INITIALSPINX: float
        INITIALSPINY: float
        INITIALSPINZ: float
        SPINSPEED: float
        MASSCENTERX: float
        MASSCENTERY: float
        MASSCENTERZ: float
        LINEARDAMPING: float
        ANGULARDAMPING: float
        BAKED: int
        MESHTYPE: int
        MESHCUSTOMMESH: None
        MESHVERTICESLIMIT: int
        MESHINFLATION: float
        MESHCONVEXSTYLE: int
        MESHRADIUS: float
        MESHLENGTH: float
        MESHWIDTH: float
        MESHHEIGHT: float
        MESHOVERRIDEMATERIAL: bool
        COMPOSITEMAXVERTICES: int
        COMPOSITEMAXCONCAVITY: float
        SMALLCLUSTERTHRESHOLD: float
        ENABLESOLIDMESHES: bool
        COMPOSITEHIGHQUALITY: bool
        MASSCENTERMODE: int
        ENABLEBACKFACECOLLISION: bool
        FORCESLIST: MXSWrapperBase
        SHOWPHYSICALMESH: bool
        ...
    class ModifierClass(Value):
        ...
    class MonoGraph(FloatController):
        ...
    class Morph(GeometryClass):
        ...
    class MorphByBone(Modifier):
        BONES: MXSWrapperBase
        MORPHNAME: None
        INFLUENCEANGLE: float
        FALLOFF: int
        SHOWMIRRORPLANE: bool
        MIRRORPLANE: int
        MIRROROFFSET: float
        MIRRORTHRESHOLD: float
        PREVIEWVERTS: bool
        PREVIEWBONE: bool
        JOINTTYPE: int
        TARGETNODES: MXSWrapperBase
        FALLOFFGRAPHS: MXSWrapperBase
        RELOADSELECTED: bool
        SAFEMODE: bool
        SHOWDRIVERBONE: bool
        SHOWMORPHBONE: bool
        SHOWCURRENTANGLE: bool
        SHOWLIMITANGLE: bool
        MATRIXSIZE: float
        SHOWDELTAS: bool
        SHOWX: bool
        SHOWY: bool
        SHOWZ: bool
        BONESIZE: float
        SOFTSELECTIONGRAPH: MXSWrapperBase
        USESOFTSELECTION: bool
        SELECTIONRADIUS: float
        EDGELIMIT: int
        USEEDGELIMIT: bool
        ENABLED: bool
        SHOWEDGES: bool
        ...
    class MorphController(MAXWrapper):
        ...
    class Morph_Angle_Deformer(ReferenceTarget):
        ...
    class Morpher(Modifier):
        USE_LIMITS: int
        SPINNER_MINIMUM: float
        SPINNER_MAXIMUM: float
        VALUE_INCREMENTS: int
        AUTOLOAD_OF_TARGETS: int
        USE_SELECTION: int
        ...
    class MorpherMaterial(Material):
        MAT_1: None
        MAT_2: None
        MAT_3: None
        MAT_4: None
        MAT_5: None
        MAT_6: None
        MAT_7: None
        MAT_8: None
        MAT_9: None
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
        MAT_100: None
        BASE: MXSWrapperBase
        CHANNEL_12: float
        CHANNEL_13: float
        CHANNEL_14: float
        CHANNEL_15: float
        CHANNEL_16: float
        CHANNEL_17: float
        CHANNEL_18: float
        CHANNEL_19: float
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
        CHANNEL_100: int
        CHANNEL_0: float
        CHANNEL_1: float
        CHANNEL_2: float
        CHANNEL_3: float
        CHANNEL_4: float
        CHANNEL_5: float
        CHANNEL_6: float
        CHANNEL_7: float
        CHANNEL_8: float
        CHANNEL_9: float
        CHANNEL_10: float
        CHANNEL_11: float
        ...
    class MotionCaptureDeviceBindingClass(MAXWrapper):
        ...
    class MotionCaptureDeviceClass(MAXWrapperNonRefTarg):
        ...
    class MotionRenderElement(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
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
        DISPLAYPASSES: bool
        TOTALPASSES: int
        DURATION: float
        BIAS: float
        NORMALIZEWEIGHTS: bool
        DITHERSTRENGTH: float
        TILESIZE: int
        DISABLEFILTERING: bool
        DISABLEANTIALIASING: bool
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
        UNITS: int
        ICON_SIZE: float
        ON_TIME: MXSWrapperBase
        OFF_TIME: MXSWrapperBase
        BASIC_TORQUE: float
        FEEDBACK_ON: int
        REVERSIBLE: int
        TARGET_REVS: float
        REVS_UNITS: int
        CONTROL_GAIN: float
        ENABLE_VARIATION: int
        VARIATION_PERIOD_1: MXSWrapperBase
        AMPLITUDE_1: float
        VARIATION_PHASE_1: float
        VARIATION_PERIOD_2: MXSWrapperBase
        AMPLITUDE_2: float
        VARIATION_PHASE_2: float
        RANGE_ENABLE: int
        RANGE_VALUE: float
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
        VERTEXCOUNT: int
        VERTEXPERCENT: float
        MERGEVERTEX: bool
        MERGETHRESHOLD: float
        MERGEWITHINMESH: bool
        BOUNDARYMETRIC: bool
        BASEVERTICES: bool
        MULTIVERTNORM: bool
        CREASEANGLE: float
        REQGENERATE: bool
        RESETPARAMS: bool
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
        AVERAGESPEED1: float
        MAXACCEL1: float
        TURNDECEL1: float
        TURNDECELANGLE1: float
        INCLINEDECEL1: float
        INCLINEDECELANGLE1: float
        DECLINEDECEL1: float
        DECLINEDECELANGLE1: float
        MAXHEADING1: float
        MAXHEADINGRATE1: float
        MAXINCLINE1: float
        MAXDECLINE1: float
        MAXBANK1: float
        MAXBANKRATE1: float
        BANKFACTOR1: float
        STARTFRAME1: int
        PRIORITY1: int
        AVERAGESPEED2: float
        MAXACCEL2: float
        TURNDECEL2: float
        TURNDECELANGLE2: float
        INCLINEDECEL2: float
        INCLINEDECELANGLE2: float
        DECLINEDECEL2: float
        DECLINEDECELANGLE2: float
        MAXHEADING2: float
        MAXHEADINGRATE2: float
        MAXINCLINE2: float
        MAXDECLINE2: float
        MAXBANK2: float
        MAXBANKRATE2: float
        BANKFACTOR2: float
        STARTFRAME2: int
        PRIORITY2: int
        ACTIVE: bool
        SHOWFORCES: bool
        SHOWVELOCITY: bool
        SHOWCOGSTATES: bool
        XYCONSTRAIN: bool
        VELOCITYCOLOR: MXSWrapperBase
        USEHIERBBOX: bool
        USEBIPED: bool
        STARTCLIP: int
        RAND1: bool
        RAND2: bool
        RAND3: bool
        RAND4: bool
        RAND5: bool
        RAND6: bool
        RAND7: bool
        RAND8: bool
        RAND9: bool
        RAND10: bool
        RAND11: bool
        RAND12: bool
        RAND13: bool
        RAND17: bool
        RAND18: bool
        RAND14: bool
        RAND15: bool
        SET1: bool
        SET2: bool
        SET3: bool
        SET4: bool
        SET5: bool
        SET6: bool
        SET7: bool
        SET8: bool
        SET9: bool
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
        SET20: bool
        SET21: bool
        SET22: bool
        SET24: bool
        SET25: bool
        SET26: bool
        DELEGATES: MXSWrapperBase
        SETTINGS: MXSWrapperBase
        EDITSETTING: MXSWrapperBase
        BIPEDASSOCIATIONTYPE: bool
        BIPEDASSOCIATIONUSEBIP: bool
        BIPEDS: MXSWrapperBase
        BIPEDDELEGATES: MXSWrapperBase
        ANIMOBJNODE: None
        ...
    class MultiLayer(Shader):
        ...
    class MultiListBoxControl(RolloutControl):
        ...
    class MultiMaterialClass(Value):
        ...
    class MultiOutputChannelTexmapToTexmap(TextureMap):
        SOURCEMAP: None
        OUTPUTCHANNELINDEX: int
        ...
    class MultiRes(Modifier):
        VERTEXCOUNT: int
        VERTEXPERCENT: float
        MERGEVERTEX: bool
        MERGETHRESHOLD: float
        MERGEWITHINMESH: bool
        BOUNDARYMETRIC: bool
        BASEVERTICES: bool
        MULTIVERTNORM: bool
        CREASEANGLE: float
        REQGENERATE: bool
        RESETPARAMS: bool
        ...
    class MultiTile(TextureMap):
        ...
    class MultiTileMap(TextureMap):
        ...
    class Multi_Layer(Shader):
        ...
    class Multimaterial(Material):
        MATERIALLIST: MXSWrapperBase
        MAPENABLED: MXSWrapperBase
        NAMES: MXSWrapperBase
        MATERIALIDLIST: MXSWrapperBase
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
        AVERAGESPEED1: float
        MAXACCEL1: float
        TURNDECEL1: float
        TURNDECELANGLE1: float
        INCLINEDECEL1: float
        INCLINEDECELANGLE1: float
        DECLINEDECEL1: float
        DECLINEDECELANGLE1: float
        MAXTURN1: float
        MAXTURNACCEL1: float
        MAXINCLINE1: float
        MAXDECLINE1: float
        MAXBANK1: float
        MAXBANKACCEL1: float
        BANKFACTOR1: float
        STARTFRAME1: int
        PRIORITY1: int
        AVERAGESPEED2: float
        MAXACCEL2: float
        TURNDECEL2: float
        TURNDECELANGLE2: float
        INCLINEDECEL2: float
        INCLINEDECELANGLE2: float
        DECLINEDECEL2: float
        DECLINEDECELANGLE2: float
        MAXTURN2: float
        MAXTURNACCEL2: float
        MAXINCLINE2: float
        MAXDECLINE2: float
        MAXBANK2: float
        MAXBANKACCEL2: float
        BANKFACTOR2: float
        STARTFRAME2: int
        PRIORITY2: int
        ACTIVE: bool
        SHOWFORCES: bool
        SHOWVELOCITY: bool
        SHOWCOGSTATES: bool
        XYCONSTRAIN: bool
        VELOCITYCOLOR: MXSWrapperBase
        USEHIERBBOX: bool
        USEBIPED: bool
        STARTCLIP: int
        RAND1: bool
        RAND2: bool
        RAND3: bool
        RAND4: bool
        RAND5: bool
        RAND6: bool
        RAND7: bool
        RAND8: bool
        RAND9: bool
        RAND10: bool
        RAND11: bool
        RAND12: bool
        RAND16: bool
        RAND17: bool
        RAND18: bool
        RAND13: bool
        RAND14: bool
        RAND15: bool
        SET1: bool
        SET2: bool
        SET3: bool
        SET4: bool
        SET5: bool
        SET6: bool
        SET7: bool
        SET8: bool
        SET9: bool
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
        SET20: bool
        SET21: bool
        SET22: bool
        SET23: bool
        SET24: bool
        SET25: bool
        SET26: bool
        DELEGATES: MXSWrapperBase
        NAME: None
        ...
    class Multiple_Delegates(ReferenceTarget):
        AVERAGESPEED1: float
        MAXACCEL1: float
        TURNDECEL1: float
        TURNDECELANGLE1: float
        INCLINEDECEL1: float
        INCLINEDECELANGLE1: float
        DECLINEDECEL1: float
        DECLINEDECELANGLE1: float
        MAXHEADING1: float
        MAXHEADINGRATE1: float
        MAXINCLINE1: float
        MAXDECLINE1: float
        MAXBANK1: float
        MAXBANKRATE1: float
        BANKFACTOR1: float
        STARTFRAME1: int
        PRIORITY1: int
        AVERAGESPEED2: float
        MAXACCEL2: float
        TURNDECEL2: float
        TURNDECELANGLE2: float
        INCLINEDECEL2: float
        INCLINEDECELANGLE2: float
        DECLINEDECEL2: float
        DECLINEDECELANGLE2: float
        MAXHEADING2: float
        MAXHEADINGRATE2: float
        MAXINCLINE2: float
        MAXDECLINE2: float
        MAXBANK2: float
        MAXBANKRATE2: float
        BANKFACTOR2: float
        STARTFRAME2: int
        PRIORITY2: int
        ACTIVE: bool
        SHOWFORCES: bool
        SHOWVELOCITY: bool
        SHOWCOGSTATES: bool
        XYCONSTRAIN: bool
        VELOCITYCOLOR: MXSWrapperBase
        USEHIERBBOX: bool
        USEBIPED: bool
        STARTCLIP: int
        RAND1: bool
        RAND2: bool
        RAND3: bool
        RAND4: bool
        RAND5: bool
        RAND6: bool
        RAND7: bool
        RAND8: bool
        RAND9: bool
        RAND10: bool
        RAND11: bool
        RAND12: bool
        RAND13: bool
        RAND17: bool
        RAND18: bool
        RAND14: bool
        RAND15: bool
        SET1: bool
        SET2: bool
        SET3: bool
        SET4: bool
        SET5: bool
        SET6: bool
        SET7: bool
        SET8: bool
        SET9: bool
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
        SET20: bool
        SET21: bool
        SET22: bool
        SET24: bool
        SET25: bool
        SET26: bool
        DELEGATES: MXSWrapperBase
        SETTINGS: MXSWrapperBase
        EDITSETTING: MXSWrapperBase
        BIPEDASSOCIATIONTYPE: bool
        BIPEDASSOCIATIONUSEBIP: bool
        BIPEDS: MXSWrapperBase
        BIPEDDELEGATES: MXSWrapperBase
        ANIMOBJNODE: None
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
        STEPS: int
        RADIUS: float
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        CORNERRADIUS: float
        NSIDES: int
        CIRCULAR: bool
        SCRIBE: int
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
        MAP1: None
        MAP2: None
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        SIZE: float
        PHASE: float
        LEVELS: float
        THRESHOLDLOW: float
        THRESHOLDHIGH: float
        TYPE: int
        COORDS: MXSWrapperBase
        OUTPUT: MXSWrapperBase
        ...
    class Noise_Float(FloatController):
        POSITIVE: bool
        SEED: int
        FREQUENCY: float
        FRACTAL: bool
        ROUGHNESS: float
        RAMPIN: MXSWrapperBase
        RAMPOUT: MXSWrapperBase
        ...
    class Noise_Point3(Point3Controller):
        SEED: int
        FREQUENCY: float
        FRACTAL: bool
        ROUGHNESS: float
        RAMPIN: MXSWrapperBase
        RAMPOUT: MXSWrapperBase
        X_POSITIVE: bool
        Y_POSITIVE: bool
        Z_POSITIVE: bool
        ...
    class Noise_Position(PositionController):
        SEED: int
        FREQUENCY: float
        FRACTAL: bool
        ROUGHNESS: float
        RAMPIN: MXSWrapperBase
        RAMPOUT: MXSWrapperBase
        X_POSITIVE: bool
        Y_POSITIVE: bool
        Z_POSITIVE: bool
        ...
    class Noise_Rotation(RotationController):
        SEED: int
        FREQUENCY: float
        FRACTAL: bool
        ROUGHNESS: float
        RAMPIN: MXSWrapperBase
        RAMPOUT: MXSWrapperBase
        X_POSITIVE: bool
        Y_POSITIVE: bool
        Z_POSITIVE: bool
        ...
    class Noise_Scale(ScaleController):
        SEED: int
        FREQUENCY: float
        FRACTAL: bool
        ROUGHNESS: float
        RAMPIN: MXSWrapperBase
        RAMPOUT: MXSWrapperBase
        X_POSITIVE: bool
        Y_POSITIVE: bool
        Z_POSITIVE: bool
        ...
    class Noisemodifier(Modifier):
        ANIMATE: bool
        SCALE: float
        SEED: int
        FREQUENCY: float
        FRACTAL: bool
        ROUGHNESS: float
        PHASE: MXSWrapperBase
        STRENGTH: MXSWrapperBase
        ITERATIONS: float
        ...
    class NormalMappingManager(Interface):
        ...
    class Normal_Bump(TextureMap):
        MULT_SPIN: float
        BUMP_SPIN: float
        NORMAL_MAP: None
        BUMP_MAP: None
        MAP1ON: bool
        MAP2ON: bool
        METHOD: int
        FLIPRED: bool
        FLIPGREEN: bool
        SWAP_RG: bool
        ...
    class Normalize_Spl(Modifier):
        ...
    class Normalize_Spline(Modifier):
        ...
    class Normalize_Spline2(Modifier):
        LENGTH: float
        NORMALIZETYPE: int
        NUMKNOTS: int
        INSERTNUM: int
        WEIGHTED: bool
        MAXKNOTS: int
        USEMAXKNOTS: bool
        USESTRAIGHTSEGMENTS: bool
        RETAINKNOTS: bool
        RETAINPERCENT: int
        FOREACHSPLINE: bool
        RETAINTANGENTS: bool
        SHOWKNOTS: bool
        SIMPLEINTERPOLATION: bool
        ...
    class Normalmodifier(Modifier):
        FLIP: bool
        UNIFY: bool
        ...
    class NormalsMap(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        USENORMALBUMP: bool
        USEHEIGHTASALPHA: bool
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
        OSLPATH: str
        OSLCODE: str
        OSLAUTOUPDATE: bool
        OSLSHADERNAME: str
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        INPUT_A: MXSWrapperBase
        INPUT_B: MXSWrapperBase
        MIXER: float
        INPUT_A_MAP: None
        INPUT_B_MAP: None
        MIXER_MAP: None
        A: MXSWrapperBase
        B: MXSWrapperBase
        A: MXSWrapperBase
        B: MXSWrapperBase
        ...
    class OSnap(Primitive):
        ...
    class ObRefModAppClass(MAXWrapper):
        ...
    class ObjAssoc(ReferenceTarget):
        OBJECTS: MXSWrapperBase
        DELEGATES: MXSWrapperBase
        ALIGNSCALE: bool
        ...
    class ObjExp(ExporterPlugin):
        ...
    class ObjImp(ImporterPlugin):
        ...
    class ObjectParameter(ReferenceTarget):
        OBJECT: None
        SUBFRAME_SAMPLING: bool
        USE_AS_SPEED_OR_SPIN_RATE: bool
        UNITS_PER_TYPE: int
        FILTER: None
        INPUT: None
        ...
    class ObjectSet(Set):
        ...
    class ObjectSpaceSubdivideMod(Modifier):
        SIZE: float
        SUBDIVIDEDOENFORCEQUALITY: bool
        SUBDIVIDEDOSUBDIVIDETRIANGLES: bool
        SHOWALLTRIANGLES: bool
        SUBDIVIDEMAXSTEINERPOINTS: int
        SUBDIVIDEQUADAREARATIO: float
        SUBDIVIDEDIAGONALRATIO: float
        SUBDIVIDENUMBUCKETS: int
        SUBDIVIDEDOFORMQUADS: bool
        SUBDIVIDEREFINEMENTTYPE: int
        MANUALUPDATE: int
        REMESHTYPE: int
        PRESERVEMESHDATA: bool
        PRESERVEDMAPINDEX: int
        PRESERVESHARPEDGESBYANGLE: bool
        PRESERVEDSHARPEDGEANGLE: float
        DELAUNAYSIZE: float
        DELAUNAYRELAXATIONCOEFF: float
        DELAUNAYRELAXATIONITERATIONS: int
        ADAPTIVEEDGELENGTH: float
        ADAPTIVEREGULARITY: float
        ADAPTIVETHRESHOLD: float
        VARIABLECURVATUREEDGELENGTH: float
        VARIABLECURVATUREREGULARITY: float
        VARIABLECURVATURETHRESHOLD: float
        VARIABLECURVATUREVARIABLEDENSITY: float
        VARIABLECURVATUREITERATIONS: int
        VARIABLECURVATURETRANSITION: float
        ...
    class Object_Display_Culling(UtilityPlugin):
        ...
    class Object_ID(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        COLORMODE: int
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
        HEIGHT: float
        RADIUS: float
        SIDES: int
        MAPCOORDS: int
        BLEND: float
        CAP_HEIGHT: float
        SMOOTH_ON: int
        SLICE_ON: int
        SLICE_FROM: float
        SLICE_TO: float
        HEIGHT_SEGMENTS: int
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
        RGB: MXSWrapperBase
        COLOR: MXSWrapperBase
        CONTRAST: float
        ENABLED: bool
        ON: bool
        TYPE: MXSWrapperBase
        VALUE: int
        EXCLUDELIST: MXSWrapperBase
        INCLUDELIST: None
        MULTIPLIER: float
        SOFTENDIFFUSEEDGE: float
        FARATTENSTART: float
        FARATTENEND: float
        NEARATTENSTART: float
        NEARATTENEND: float
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        DECAYRADIUS: float
        SHADOWCOLOR: MXSWrapperBase
        SHADOWMULTIPLIER: float
        HSV: MXSWrapperBase
        HUE: int
        SATURATION: int
        INCLEXCLTYPE: int
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        USENEARATTEN: bool
        SHOWNEARATTEN: bool
        USEFARATTEN: bool
        SHOWFARATTEN: bool
        ATTENDECAY: int
        PROJECTOR: bool
        PROJECTORMAP: None
        CASTSHADOWS: bool
        USEGLOBALSHADOWSETTINGS: bool
        RAYTRACEDSHADOWS: bool
        ATMOSSHADOWS: bool
        LIGHTAFFECTSSHADOW: bool
        SHADOWPROJECTORMAP: None
        USESHADOWPROJECTORMAP: bool
        AMBIENTONLY: bool
        SHADOWGENERATOR: MXSWrapperBase
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
        ISOLINEDISPLAY: bool
        ITERATIONS: int
        USERENDERITERATIONS: bool
        RENDERITERATIONS: int
        MODE: int
        VERTBOUNDARY: int
        FVARBOUNDARY: int
        PROPAGATECORNERS: bool
        SMOOTHTRIANGLES: bool
        CREASEMETHOD: int
        UPDATE: int
        SOLVERTYPE: int
        ADAPTIVE: bool
        ADAPTIVEITERATIONS: int
        ...
    class OpenSubdivMod(Modifier):
        ISOLINEDISPLAY: bool
        ITERATIONS: int
        USERENDERITERATIONS: bool
        RENDERITERATIONS: int
        MODE: int
        VERTBOUNDARY: int
        FVARBOUNDARY: int
        PROPAGATECORNERS: bool
        SMOOTHTRIANGLES: bool
        CREASEMETHOD: int
        UPDATE: int
        SOLVERTYPE: int
        ADAPTIVE: bool
        ADAPTIVEITERATIONS: int
        ...
    class Open_Edges(GlobalUtilityPlugin):
        ...
    class OperatorGraph(ReferenceTarget):
        NODES: MXSWrapperBase
        DATA: str
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
        REDUCEDMAXKNOTS: int
        ITERATIONS: int
        ADAPTIVE: bool
        PERCENT: int
        REDUCE_METHOD: int
        SUBSEGMENT: int
        REDUCEDMINKNOTS: int
        SHOWKNOTS: bool
        ...
    class Orbaz_Mix(VideoPostFilter):
        ...
    class OrenNayarBlinn(Shader):
        ...
    class Oren_Nayar_Blinn(Shader):
        ...
    class OrientationBehavior(ReferenceTarget):
        NAME: str
        HEADINGRELATIVE: bool
        MINHEADING: float
        MAXHEADING: float
        MAXHEADINGVEL: float
        HEADINGRESPONSE: float
        PITCHRELATIVE: bool
        MINPITCH: float
        MAXPITCH: float
        MAXPITCHVEL: float
        PITCHRESPONSE: float
        MAXBANK: float
        MAXBANKVEL: float
        BANKPERTURN: float
        ...
    class Orientation_Behavior(ReferenceTarget):
        NAME: str
        HEADINGRELATIVE: bool
        MINHEADING: float
        MAXHEADING: float
        MAXHEADINGVEL: float
        HEADINGRESPONSE: float
        PITCHRELATIVE: bool
        MINPITCH: float
        MAXPITCH: float
        MAXPITCHVEL: float
        PITCHRESPONSE: float
        MAXBANK: float
        MAXBANKVEL: float
        BANKPERTURN: float
        ...
    class Orientation_Constraint(RotationController):
        WEIGHT: MXSWrapperBase
        RELATIVE: bool
        LOCAL_WORLD: int
        ...
    class Orthogonalize(MappedGeneric):
        ...
    class OutputCustom(ReferenceTarget):
        DATA_CHANNEL: None
        DATA_HANDLE: int
        PROCEED_TYPE: int
        HISTORY_DEPENDENT: bool
        EXECUTION_ORDER: int
        PRIORITY_ORDER: int
        FILTER: None
        INPUT_1: None
        ...
    class OutputNew(ReferenceTarget):
        DATA_TYPE: int
        SCOPE_TYPE: int
        DATA_HANDLE: int
        PROCEED_TYPE: int
        HISTORY_DEPENDENT: bool
        EXECUTION_ORDER: int
        PRIORITY_ORDER: int
        FILTER: None
        INPUT_1: None
        ...
    class OutputPhysX(ReferenceTarget):
        DATA_TYPE: int
        MATCH_TYPE: int
        THRESHOLD_TYPE: int
        PROCEED_TYPE: int
        HISTORY_DEPENDENT: bool
        EXECUTION_ORDER: int
        PRIORITY_ORDER: int
        FILTER: None
        INPUT: None
        ...
    class OutputStandard(ReferenceTarget):
        DATA_TYPE: int
        TIME_TYPE: int
        POSITION_TYPE: int
        SPEED_TYPE: int
        ROTATION_TYPE: int
        SPIN_TYPE: int
        SCALE_TYPE: int
        SCRIPT_TYPE: int
        TM_TYPE: int
        MAPPING_TYPE: int
        MAP_CHANNEL: int
        PROCEED_TYPE: int
        HISTORY_DEPENDENT: bool
        EXECUTION_ORDER: int
        PRIORITY_ORDER: int
        USE_T2: bool
        USE_E2: bool
        ACCELERATION_TYPE: int
        VISIBILITY_TYPE: int
        VIEWPORT_RENDER_OPERATOR: None
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        ...
    class OutputTest(ReferenceTarget):
        TYPE: int
        USE_T2: bool
        PROCEED_TYPE: int
        HISTORY_DEPENDENT: bool
        EXECUTION_ORDER: int
        PRIORITY_ORDER: int
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        ...
    class Output_MParticles(ReferenceTarget):
        DATA_TYPE: int
        MATCH_TYPE: int
        THRESHOLD_TYPE: int
        PROCEED_TYPE: int
        HISTORY_DEPENDENT: bool
        EXECUTION_ORDER: int
        PRIORITY_ORDER: int
        FILTER: None
        INPUT: None
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
        SIZE: float
        SEED: int
        ICONSIZE: float
        SPEED: float
        MAPPINGTYPE: int
        FORMATION: int
        VIEWTYPE: int
        VIEWPERCENT: float
        QUANTITYMETHOD: int
        PARTICLETYPE: int
        STANDARDPARTICLE: int
        METABALLRENDERCOARSNESS: float
        METABALLVIEWCOARSNESS: float
        METABALLAUTOCOARSNESS: bool
        INSTANCESUBTREE: bool
        INSTANCEKEYOFFSETTYPE: int
        INSTANCEFRAMEOFFSET: int
        MATERIALSOURCE: int
        SPINAXISTYPE: int
        SPAWNTYPE: int
        SPAWNSPEEDTYPE: int
        SPAWNINHERITVELOCITY: bool
        SPAWNSPEEDFIXED: bool
        SPAWNSCALETYPE: int
        SPAWNSCALEFIXED: bool
        MOTIONINFLUENCE: float
        MOTIONMULTIPLIER: float
        MOTIONVARIATION: float
        EMITTER: None
        INSTANCINGOBJECT: None
        LIFESPANVALUEQUEUE: MXSWrapperBase
        OBJECTMUTATIONQUEUE: MXSWrapperBase
        SUBSAMPLEEMITTERTRANSLATION: bool
        SUBSAMPLEEMITTERROTATION: bool
        SUBSAMPLECREATIONTIME: bool
        ICONHIDDEN: bool
        NUMDISTINCTPOINTS: int
        FRAGMENTMETHOD: int
        FRAGCHUNKMINIMUM: int
        FRAGSMOOTHINGANGLE: float
        FRAGEDGEMATID: int
        FRAGOUTSIDEMATID: int
        FRAGBACKMATID: int
        LIFE: MXSWrapperBase
        DIVERGENCE_ANGLE: float
        FRAGMENT_THICKNESS: float
        BUBBLE_AMPLITUDE: float
        BUBBLE_AMPLITUDE_VARIATION: float
        BUBBLE_PERIOD: MXSWrapperBase
        BUBBLE_PERIOD_VARIATION: float
        BUBBLE_PHASE: float
        BLUR_STRETCH: int
        SPAWN_GENERATIONS: int
        SPAWN_MULTIPLIER: int
        SPAWN_LIFESPAN: int
        USE_SELECTED_SUBOBJECTS: int
        SPEED_VARIATION: float
        BIRTH_RATE: int
        TOTAL_NUMBER: int
        EMITTER_START: MXSWrapperBase
        EMITTER_STOP: MXSWrapperBase
        DISPLAY_UNTIL: MXSWrapperBase
        LIFE_VARIATION: MXSWrapperBase
        SIZE_VARIATION: float
        GROWTH_TIME: MXSWrapperBase
        FADE_TIME: MXSWrapperBase
        METAPARTICLE_TENSION: float
        METAPARTICLE_TENSION_VARIATION: float
        MAPPING_TIME_BASE: MXSWrapperBase
        MAPPING_DISTANCE_BASE: float
        SPIN_TIME: MXSWrapperBase
        SPIN_TIME_VARIATION: float
        SPIN_PHASE: float
        SPIN_PHASE_VARIATION: float
        X_SPIN_VECTOR: float
        Y_SPIN_VECTOR: float
        Z_SPIN_VECTOR: float
        SPIN_AXIS_VARIATION: float
        SPAWN_DIRECTION_CHAOS: float
        SPAWN_SPEED_CHAOS: float
        SPAWN_SCALE_CHAOS: float
        SPAWN_AFFECTS: int
        SPAWN_MULTIPLIER_VARIATION: float
        BUBBLE_PHASE_VARIATION: float
        DIE__X_FRAMES_AFTER_COLLISION: MXSWrapperBase
        DIE__X_FRAMES_AFTER_COLLISION_VARIATION: float
        INTERPARTICLE_COLLISIONS_ON: int
        INTERPARTICLE_COLLISION_STEPS: int
        INTERPARTICLE_COLLISION_BOUNCE: float
        INTERPARTICLE_COLLISION_BOUNCE_VARIATION: float
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
        NORMAL_FLIP_RED: bool
        NORMAL_FLIP_GREEN: bool
        BASECOLOR: MXSWrapperBase
        BASE_COLOR_MAP: None
        METALNESS: float
        METALNESS_MAP: None
        ROUGHNESS: float
        ROUGHNESS_MAP: None
        USEGLOSSINESS: int
        AO_MAP: None
        BUMP_MAP_AMT: float
        NORM_MAP: None
        EMIT_COLOR: MXSWrapperBase
        EMIT_COLOR_MAP: None
        OPACITY_MAP: None
        DISPLACEMENT_AMT: float
        DISPLACEMENT_MAP: None
        ...
    class PBRSpecGloss(Material):
        AO_AFFECTS_DIFFUSE: bool
        AO_AFFECTS_REFLECTION: bool
        NORMAL_FLIP_RED: bool
        NORMAL_FLIP_GREEN: bool
        BASECOLOR: MXSWrapperBase
        BASE_COLOR_MAP: None
        SPECULAR: MXSWrapperBase
        SPECULAR_MAP: None
        GLOSSINESS: float
        GLOSSINESS_MAP: None
        USEGLOSSINESS: int
        AO_MAP: None
        BUMP_MAP_AMT: float
        NORM_MAP: None
        EMIT_COLOR: MXSWrapperBase
        EMIT_COLOR_MAP: None
        OPACITY_MAP: None
        DISPLACEMENT_AMT: float
        DISPLACEMENT_MAP: None
        ...
    class PBStartTrack(Primitive):
        ...
    class PBTrackGetToolActive(Primitive):
        ...
    class PBomb(SpacewarpObject):
        RANGE: float
        SYMMETRY: int
        STRENGTH: float
        CHAOS: float
        ICON_SIZE: float
        LASTS_FOR: MXSWrapperBase
        DECAY_TYPE: int
        START_TIME: MXSWrapperBase
        ...
    class PBombMod(SpacewarpModifier):
        ...
    class PCloud(GeometryClass):
        SIZE: float
        SEED: int
        SPEED: float
        MAPPINGTYPE: int
        FORMATION: int
        VIEWTYPE: int
        VIEWPERCENT: float
        EMITTERHIDDEN: bool
        QUANTITYMETHOD: int
        MOTIONTYPE: int
        DIRECTIONVARIATION: float
        PARTICLETYPE: int
        STANDARDPARTICLE: int
        METABALLRENDERCOARSNESS: float
        METABALLVIEWCOARSNESS: float
        METABALLAUTOCOARSNESS: bool
        INSTANCESUBTREE: bool
        INSTANCEKEYOFFSETTYPE: int
        INSTANCEFRAMEOFFSET: int
        MATERIALSOURCE: int
        SPINAXISTYPE: int
        SPAWNTYPE: int
        SPAWNSPEEDTYPE: int
        SPAWNINHERITVELOCITY: bool
        SPAWNSPEEDFIXED: bool
        SPAWNSCALETYPE: int
        SPAWNSCALEFIXED: bool
        MOTIONINFLUENCE: float
        MOTIONMULTIPLIER: float
        MOTIONVARIATION: float
        EMITTER: None
        MOTIONREFERENCEOBJECT: None
        INSTANCINGOBJECT: None
        LIFESPANVALUEQUEUE: MXSWrapperBase
        OBJECTMUTATIONQUEUE: MXSWrapperBase
        LIFE: MXSWrapperBase
        DIRECTION_VECTOR_X: float
        DIRECTION_VECTOR_Y: float
        DIRECTION_VECTOR_Z: float
        EMITTER_RAD_LEN: float
        EMITTER_HEIGHT: float
        BUBBLE_AMPLITUDE: float
        BUBBLE_AMPLITUDE_VARIATION: float
        BUBBLE_PERIOD: MXSWrapperBase
        BUBBLE_PERIOD_VARIATION: float
        BUBBLE_PHASE: float
        BLUR_STRETCH: int
        SPAWN_GENERATIONS: int
        SPAWN_MULTIPLIER: int
        SPAWN_LIFESPAN: int
        SPEED_VARIATION: float
        BIRTH_RATE: int
        TOTAL_NUMBER: int
        EMITTER_START: MXSWrapperBase
        EMITTER_STOP: MXSWrapperBase
        DISPLAY_UNTIL: MXSWrapperBase
        LIFE_VARIATION: MXSWrapperBase
        SIZE_VARIATION: float
        GROWTH_TIME: MXSWrapperBase
        FADE_TIME: MXSWrapperBase
        EMITTER_WIDTH: float
        METAPARTICLE_TENSION: float
        METAPARTICLE_TENSION_VARIATION: float
        MAPPING_TIME_BASE: MXSWrapperBase
        MAPPING_DISTANCE_BASE: float
        SPIN_TIME: MXSWrapperBase
        SPIN_TIME_VARIATION: float
        SPIN_PHASE: float
        SPIN_PHASE_VARIATION: float
        X_SPIN_VECTOR: float
        Y_SPIN_VECTOR: float
        Z_SPIN_VECTOR: float
        SPIN_AXIS_VARIATION: float
        SPAWN_DIRECTION_CHAOS: float
        SPAWN_SPEED_CHAOS: float
        SPAWN_SCALE_CHAOS: float
        BUBBLE_PHASE_VARIATION: float
        DIE__X_FRAMES_AFTER_COLLISION: MXSWrapperBase
        DIE__X_FRAMES_AFTER_COLLISION_VARIATION: float
        INTERPARTICLE_COLLISIONS_ON: int
        INTERPARTICLE_COLLISION_STEPS: int
        INTERPARTICLE_COLLISION_BOUNCE: float
        INTERPARTICLE_COLLISION_BOUNCE_VARIATION: float
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
        ENABLE_PARTICLES: bool
        LOGO_SIZE: float
        EMITTER_TYPE: int
        EMITTER_LENGTH: float
        EMITTER_WIDTH: float
        EMITTER_HEIGHT: float
        SHOW_LOGO: bool
        SHOW_EMITTER: bool
        QUANTITY_VIEWPORT: float
        QUANTITY_RENDER: float
        SELECT_BY_PARTICLE_ID: int
        CLEAR_SELECTION: bool
        SELECTED_PARTICLES: MXSWrapperBase
        SELECTION_LEVEL: int
        PARTICLE_AMOUNT_LIMIT: int
        INTEGRATION_FOR_VIEWPORT: int
        INTEGRATION_FOR_RENDER: int
        ENABLE_SCRIPT_FOR_EVERY_STEP_UPDATE: bool
        EVERY_STEP_UPDATE_SCRIPT: str
        USE_FILE_FOR_EVERY_STEP_UPDATE: bool
        EVERY_STEP_UPDATE_SCRIPT_FILE: str
        ENABLE_SCRIPT_FOR_FINAL_STEP_UPDATE: bool
        FINAL_STEP_UPDATE_SCRIPT: str
        USE_FILE_FOR_FINAL_STEP_UPDATE: bool
        FINAL_STEP_UPDATE_SCRIPT_FILE: str
        X_COORD: int
        Y_COORD: int
        Z_ORDER: int
        WIDTH: int
        ...
    class PFlow_Collision_Shape(SpacewarpModifier):
        SHAPE: int
        SMOOTH_SURFACE: bool
        RESTITUTION: float
        STATIC_FRICTION: float
        DYNAMIC_FRICTION: float
        VISUALIZE_COLLISION_SHAPE: bool
        THICKNESS: float
        NORMAL_OFFSET: float
        SIDE_OVERLAP: float
        PLACEMENT_VERTICES: bool
        PLACEMENT_EDGES: bool
        PLACEMENT_POLYGONS: bool
        SELECTED_ONLY: bool
        ACTIVE: bool
        PRIMITIVE_SIZE_TYPE: int
        ...
    class PMAlpha(VideoPostFilter):
        ...
    class POmniFlect(SpacewarpObject):
        TIMEON: MXSWrapperBase
        TIMEOFF: MXSWrapperBase
        AFFECTS: float
        BOUNCE: float
        BOUNCEVAR: float
        CHAOS: float
        INHERITVELOCITY: float
        REFRACTS: float
        DECELERATION: float
        DECELVAR: float
        REFRACTION: float
        REFRACTIONVAR: float
        DIFFUSION: float
        DIFFUSIONVAR: float
        WIDTH: float
        HEIGHT: float
        SPAWN: float
        PASSVELOCITY: float
        PASSVELOCITYVAR: float
        FRICTION: float
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
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ...
    class PaintLayerMod(Modifier):
        IGNOREBACKFACING: bool
        MAPCHANNEL: int
        LAYERMODE: str
        LAYEROPACITY: float
        LAYERISOLATED: bool
        SURVIVECONDENSE: bool
        LIGHTINGMODEL: int
        COLORBY: int
        CASTSHADOWS: bool
        USEMAPS: bool
        USERADIOSITY: bool
        RADIOSITYONLY: bool
        HIDEUNSELSUBOBJS: bool
        RADIOSITYOPTION: int
        ...
    class PaintRenderElement(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ...
    class PaintSoftSelPresetContext(Interface):
        ...
    class Paintbox(UserDataTypeClass):
        ...
    class PaintboxStartup(GlobalUtilityPlugin):
        ...
    class PainterInterface(ReferenceTarget):
        NODES: MXSWrapperBase
        DRAWRING: bool
        DRAWNORMAL: bool
        DRAWTRACE: bool
        MINSIZE: float
        MAXSIZE: float
        MINSTR: float
        MAXSTR: float
        ADDITIVEMODE: bool
        FALLOFFGRAPH: MXSWrapperBase
        PRESSUREENABLE: bool
        PRESSUREAFFECTS: int
        UPDATEONMOUSEUP: bool
        QUADDEPTH: int
        PREDEFINEDSTRENABLE: bool
        PREDEFINEDSTRGRAPH: MXSWrapperBase
        PREDEFINEDSIZEENABLE: bool
        PREDEFINEDSIZEGRAPH: MXSWrapperBase
        MIRRORENABLE: bool
        MIRRORAXIS: int
        MIRROROFFSET: float
        MIRRORGIZMOSIZE: float
        POINTGATHERENABLE: bool
        BUILDVNORMALS: bool
        LAGRATE: int
        NORMALSCALE: float
        MARKER: float
        MARKERENABLE: bool
        OFFMESHHITTYPE: bool
        OFFMESHHITZDEPTH: float
        OFFMESHHITPOS: MXSWrapperBase
        STRDRAGLIMITMIN: float
        STRDRAGLIMITMAX: float
        SPLINECONSTRAINTNODE: None
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
        TYPE: int
        BEFORE_HIDE: bool
        AFTER_HIDE: bool
        TIME_ON: int
        TIME_OFF: int
        PARTICLE_FLOW_SYSTEMS: MXSWrapperBase
        ALL_PARTICLE_FLOW_EVENTS: bool
        PARTICLE_FLOW_EVENTS: MXSWrapperBase
        ZONE_SIZE: float
        SCALE_INFLUENCE: float
        ZONE_WEIGHT: float
        MULTIPLY_BY_SCALE: bool
        BLEND_PARTICLES: bool
        SPLIT_PRECISION_TYPE: int
        RELATIVE_PRECISION: float
        ABSOLUTE_PRECISION: float
        SYNC_TYPE: int
        USE_TIME_OFF: bool
        ...
    class ParticleGroup(GeometryClass):
        ...
    class ParticleSkinnerOSM(Modifier):
        BEFORE_HIDE: bool
        AFTER_HIDE: bool
        TIME_ON: int
        TIME_OFF: int
        PARTICLE_FLOW_SYSTEMS: MXSWrapperBase
        ALL_PARTICLE_FLOW_EVENTS: bool
        PARTICLE_FLOW_EVENTS: MXSWrapperBase
        FALLOFF: float
        DISTANCE_INFLUENCE_TYPE: int
        ABSOLUTE_INFLUENCE: float
        SIZE_INFLUENCE: float
        BINDING_INFLUENCE: float
        CONTROLLERS_LIMIT: int
        CONTROL_BY_INSIDE_INCLUSION: bool
        RIP_SURFACE_APART: int
        DISTANCE_TYPE: int
        RELATIVE_DISTANCE: float
        ABSOLUTE_DISTANCE: float
        SPLIT_PRECISION_TYPE: int
        RELATIVE_PRECISION: float
        ABSOLUTE_PRECISION: float
        BINDING_LIST_TYPE: int
        PHYSX_GLUE_TESTS: MXSWrapperBase
        REMOVE_UNCONTROLLED: bool
        SUSTAIN_TOPOLOGY: bool
        INTERVAL_TICKS: int
        USE_VISIBILITY_DATA_CHANNEL: bool
        VISIBILITY_DATA_CREATOR: None
        USE_DATA_CHANNEL: bool
        DATA_CHANNEL_CREATOR: None
        MAP_CHANNEL_TYPE: int
        MAP_CHANNEL: int
        DISPLAY_INFLUENCE: bool
        DISPLAY_UNASSIGNED_POINTS: bool
        DISPLAY_CONTROL_PARTICLES: bool
        USE_TIME_OFF: bool
        ...
    class ParticleView(Helper):
        ...
    class Particle_Age(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COLOR3: MXSWrapperBase
        MAP1: None
        MAP2: None
        MAP3: None
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        MAP3ENABLED: bool
        AGE1: float
        AGE2: float
        AGE3: float
        OUTPUT: MXSWrapperBase
        ...
    class Particle_Bitmap(TextureMap):
        ...
    class Particle_Cache(SpacewarpModifier):
        ...
    class Particle_Face_Creator(Modifier):
        TYPE: int
        BEFORE_HIDE: bool
        AFTER_HIDE: bool
        TIME_ON: int
        TIME_OFF: int
        PARTICLE_FLOW_SYSTEMS: MXSWrapperBase
        ALL_PARTICLE_FLOW_EVENTS: bool
        PARTICLE_FLOW_EVENTS: MXSWrapperBase
        ZONE_SIZE: float
        SCALE_INFLUENCE: float
        ZONE_WEIGHT: float
        MULTIPLY_BY_SCALE: bool
        BLEND_PARTICLES: bool
        SPLIT_PRECISION_TYPE: int
        RELATIVE_PRECISION: float
        ABSOLUTE_PRECISION: float
        SYNC_TYPE: int
        USE_TIME_OFF: bool
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
        SPRAY_RADIUS: float
        DENSITY_CENTER: float
        DENSITY_SIDES: float
        PER_JET_LIMIT: int
        RATE_TYPE: int
        RATE_DROPS_PER_SECOND: float
        RATE_DROPS_PER_LENGTH_UNIT: float
        RATE_DROPS_PER_JET: int
        DISPLAY_TYPE: int
        DISPLAY_SIZE: float
        JET_START_TYPE: int
        JET_START_TIME: int
        JET_STOP_TYPE: int
        TIME_SCALE: float
        JET_STOP_TIME: int
        JET_DURATION: int
        AUTOADJUST_CURRENT_FRAME: bool
        ADJUST_GLOBAL_TIMING: bool
        ICON_SIZE: float
        RANDOM_SEED: int
        USE_RADIUS_GRAPH: bool
        SPRAY_RADIUS_GRAPH: None
        USE_RATE_GRAPH: bool
        SPRAY_RADIUS_RATE: None
        SPRAY_AT_TYPE: int
        SPRAY_AT_OBJECTS: MXSWrapperBase
        OBJECTS_ANIMATED_SURFACE: bool
        INCLUDE_SPRAY_CHILDREN: bool
        INCLUDE_SPRAY_GROUP_MEMBERS: bool
        USE_MASK_OBJECTS: bool
        MASKS: MXSWrapperBase
        INCLUDE_MASK_CHILDREN: bool
        INCLUDE_MASK_GROUP_MEMBERS: bool
        SELECTION_FILTER_TYPE: int
        LOCATION_TYPE: int
        DISTANCE: float
        DISTANCE_VARIATION: float
        USE_SEPARATION: bool
        SEPARATION_DISTANCE: float
        MAXIMUM_NUMBER_OF_ATTEMPTS: int
        STACK_UP_FOR_SEPARATION: bool
        GENERATE_ROTATION: bool
        PRIORITY_AXIS: int
        REVERSE_X_AXIS: bool
        REVERSE_Z_AXIS: bool
        ORIENTATION_TYPE_FOR_X_AXIS: int
        ORIENTATION_TYPE_FOR_Z_AXIS: int
        DIVERGENCE_FOR_X_AXIS: float
        DIVERGENCE_FOR_Z_AXIS: float
        ACQUIRE_SUB_MATERIAL_INDEX: bool
        GENERATE_MAPPING: bool
        ASSIGN_TO_MAPPING_CHANNELS: MXSWrapperBase
        MAPPING_TYPE: int
        MAPPING_START_VALUE: float
        MAPPING_END_VALUE: float
        MAPPING_OFFSET_VALUE_PER_SECOND: float
        MAPPING_OFFSET_VALUE_PER_DROP: float
        SHOW_PARTICLE_TIMING: bool
        LATE_COLOR: MXSWrapperBase
        EDITING_START_AT: int
        EDITING_STOP_TYPE: int
        EDITING_STOP_AT: int
        EDITING_DURATION: int
        EDITING_ADJUST_GLOBAL_TIMING: bool
        SELECTED_STROKES: MXSWrapperBase
        AUTO_SYNC_TIMING_BY_SELECTED_STROKE: bool
        ...
    class Particle_Paint_Cursor(GeometryClass):
        ...
    class Particle_Skinner(Modifier):
        BEFORE_HIDE: bool
        AFTER_HIDE: bool
        TIME_ON: int
        TIME_OFF: int
        PARTICLE_FLOW_SYSTEMS: MXSWrapperBase
        ALL_PARTICLE_FLOW_EVENTS: bool
        PARTICLE_FLOW_EVENTS: MXSWrapperBase
        FALLOFF: float
        DISTANCE_INFLUENCE_TYPE: int
        ABSOLUTE_INFLUENCE: float
        SIZE_INFLUENCE: float
        BINDING_INFLUENCE: float
        CONTROLLERS_LIMIT: int
        CONTROL_BY_INSIDE_INCLUSION: bool
        RIP_SURFACE_APART: int
        DISTANCE_TYPE: int
        RELATIVE_DISTANCE: float
        ABSOLUTE_DISTANCE: float
        SPLIT_PRECISION_TYPE: int
        RELATIVE_PRECISION: float
        ABSOLUTE_PRECISION: float
        BINDING_LIST_TYPE: int
        PHYSX_GLUE_TESTS: MXSWrapperBase
        REMOVE_UNCONTROLLED: bool
        SUSTAIN_TOPOLOGY: bool
        INTERVAL_TICKS: int
        USE_VISIBILITY_DATA_CHANNEL: bool
        VISIBILITY_DATA_CREATOR: None
        USE_DATA_CHANNEL: bool
        DATA_CHANNEL_CREATOR: None
        MAP_CHANNEL_TYPE: int
        MAP_CHANNEL: int
        DISPLAY_INFLUENCE: bool
        DISPLAY_UNASSIGNED_POINTS: bool
        DISPLAY_CONTROL_PARTICLES: bool
        USE_TIME_OFF: bool
        ...
    class Particle_View(Helper):
        ...
    class Particle_View_Global_Actions(GlobalUtilityPlugin):
        ...
    class Particles(ReferenceTarget):
        TYPE: int
        USE_PROXY_FILTER: bool
        FILTER_DATA_CHANNEL: None
        FILTER_DATA_HANDLE: int
        OUTER_RADIUS: float
        USE_CORE_RADIUS: bool
        CORE_RADIUS: float
        FIELD_OF_VISION: float
        APPLY_DOUBLE_FILTERING: bool
        USE_PROXY_PARTICLES: bool
        USE_R2: bool
        USE_R3: bool
        USE_R4: bool
        FOV_DIRECTION_TYPE: int
        USE_V6: bool
        USE_CUSTOM_PARTICLE_WEIGHT: bool
        WEIGHT_DATA_CHANNEL: None
        WEIGHT_DATA_HANDLE: int
        PREVALENT_DATA_CHANNEL: None
        PREVALENT_DATA_HANDLE: int
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        ...
    class PasteSkinWeights(Modifier):
        ...
    class Paste_Skin_Weights(Modifier):
        ...
    class PatchDeform(Modifier):
        ROTATION: float
        U_STRETCH: float
        V_PERCENT: float
        V_STRETCH: float
        PLANE_TO_PATCH_DEFORM: int
        FLIP_DEFORMATION_AXIS: int
        U_PERCENT: float
        ...
    class Patch_Select(Modifier):
        ...
    class PathDeform(Modifier):
        AXIS: int
        ROTATION: float
        TWIST: float
        STRETCH: float
        PATH: None
        FLIP_DEFORMATION_AXIS: int
        PERCENT_ALONG_PATH: float
        ...
    class PathDeformSpaceWarp(SpacewarpObject):
        ...
    class PathFollowBehavior(ReferenceTarget):
        NAME: str
        PATH: None
        RADIUS: float
        AWARENESS: float
        AWAREDEVIATION: float
        START: int
        DIRECTION: int
        ENDACTION: int
        SEED: int
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
        TARGETCOLOR: MXSWrapperBase
        DISPLAYTARGET: bool
        TARGETSCALE: float
        ...
    class PathName(Value):
        ...
    class Path_Constraint(PositionController):
        PERCENT: float
        FOLLOW: bool
        PATH: None
        BANK: bool
        BANKAMOUNT: float
        SMOOTHNESS: float
        ALLOWUPSIDEDOWN: bool
        CONSTANTVEL: bool
        AXIS: int
        AXISFLIP: bool
        WEIGHT: MXSWrapperBase
        LOOP: bool
        RELATIVE: bool
        ...
    class Path_Deform2(Modifier):
        SPLINE: None
        PERCENT_ALONG_PATH: float
        STRETCH: float
        ROTATION: float
        TWIST: float
        AUTO_STRETCH: bool
        AUTO_AMOUNT: float
        FLIP: bool
        AXIS: int
        UNIFORM: bool
        X_OFFSET: float
        Y_OFFSET: float
        Z_OFFSET: float
        ACROSSSHAPES: int
        ADOPTMATID: bool
        ROUNDMATID: int
        LOOPBACK: bool
        APPLY_U: bool
        APPLY_V: bool
        APPLY_W: bool
        CHANNEL: int
        UPVECTOR: int
        MOVEBEFOREROTATION: bool
        USEPIVOTPOINT: bool
        ROTATIONENABLE: bool
        DRIVINGROTSCALE: float
        PRESERVEFORM: bool
        ADAPTIVEUPVECTOR: bool
        LOOKATNODE: None
        ROTATIONCURVE: MXSWrapperBase
        SCALEENABLE: bool
        SCALECURVE: MXSWrapperBase
        DRIVINGSCALESCALE: float
        USE_LEGACY: bool
        BY_ELEMENT: bool
        ...
    class Path_Follow(SpacewarpObject):
        ICON_SIZE: float
        RANGE_LIMITED: int
        SPLINE_FOLLOW_TYPE: int
        TANGENT_CHAOS: float
        TANG_CHAOS_VAR: float
        TANGENT_DIR: int
        SPIRAL_CHAOS: float
        SPIRAL_CHAOS_VAR: float
        SPIRAL_DIR: int
        TRAVEL_TIME: MXSWrapperBase
        TRAVEL_VAR: float
        STOP_TIME: MXSWrapperBase
        CONSTANT_SPEED: int
        RANGE_VALUE: float
        START_TIME: MXSWrapperBase
        ...
    class Path_FollowMod(SpacewarpModifier):
        ...
    class Path_Follow_Behavior(ReferenceTarget):
        NAME: str
        PATH: None
        RADIUS: float
        AWARENESS: float
        AWAREDEVIATION: float
        START: int
        DIRECTION: int
        ENDACTION: int
        SEED: int
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
        TARGETCOLOR: MXSWrapperBase
        DISPLAYTARGET: bool
        TARGETSCALE: float
        ...
    class PerezAllWeather(Interface):
        ...
    class Perlin_Marble(TextureMap):
        MAP1: None
        MAP2: None
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        SATURATION1: float
        SATURATION2: float
        SIZE: float
        LEVEL: float
        COORDS: MXSWrapperBase
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
        DENSITY: float
        LEVEL_TYPE: int
        LEVEL_HEIGHT: float
        GRID_GEOMETRY: None
        USE_QUADRATIC_DRAG: bool
        QUADRATIC_DRAG: float
        USE_LINEAR_DRAG: bool
        LINEAR_DRAG: float
        USE_ANGULAR_DRAG: bool
        ANGULAR_DRAG: float
        SURFACE_UNIT: float
        ICON_SHAPE: int
        ICON_LENGTH: float
        ICON_WIDTH: float
        ICON_HEIGHT: float
        LIMIT_BUOYANCY_BY_ICON: bool
        COLOR_COORDINATED: bool
        ...
    class PhysXCollision(Helper):
        DEFLECTORS: MXSWrapperBase
        TEST_TRUE: bool
        TEST_TYPE: int
        MIN_SPEED: float
        MAX_SPEED: float
        COLLISION_COUNT: int
        REPORT_TO_DATA_OPERATOR: bool
        ADDITIVE_COUNT: bool
        COLLISION_GROUP: int
        ...
    class PhysXDrag(Helper):
        TIMING_TYPE: int
        APPLY_LINEAR_DAMPING: bool
        LINEAR_DAMPING: float
        APPLY_ANGULAR_DAMPING: bool
        ANGULAR_DAMPING: float
        SYNC: int
        SPEED_MULTIPLIER: bool
        SPEED_UNIT: float
        SPIN_UNIT: float
        USE_DATA_WIRING: bool
        LINEAR_DAMPING_FROM_DATA: bool
        LINEAR_DAMPING_DATA_CREATOR: None
        ANGULAR_DAMPING_FROM_DATA: bool
        ANGULAR_DAMPING_DATA_CREATOR: None
        ...
    class PhysXFlow(ReferenceTarget):
        ...
    class PhysXForce(Helper):
        FORCE_TYPE: int
        FORCE_VARIATION_THRESHOLD: bool
        SHAPE_SIZE: float
        INFLUENCE: float
        SYNC: int
        FORCE_SPACE_WARPS: MXSWrapperBase
        FORCE_OVERLAPPING: int
        IMPULSE_ON_EVENT_ENTRY: bool
        TIME_WARP: int
        EXPONENT: int
        USE_SCRIPT_FLOAT: int
        ...
    class PhysXGlue(Helper):
        TIMING_TYPE: int
        BIND_DISTANCE: float
        USE_BIND_GAP_CONDITION: bool
        BIND_GAP: float
        BIND_CENTER_ALIGNED_ONLY: bool
        ALIGN_MARGIN: float
        ALLOW_BINDING_PENETRATION: bool
        TYPE: int
        BREAKABLE_BY_FORCE: bool
        MAX_FORCE: float
        MAX_TORQUE: float
        MAX_BY_BIND_DISTANCE: bool
        DISTANCE_UNIT: float
        CONTINUOUS_ADJUSTMENT: bool
        SYNC: int
        MAX_BINDS_PER_PARTICLE: int
        TEST_TRUE: bool
        TEST_TYPE: int
        BIND_IN_CURRENT_EVENT: bool
        BIND_WITH_OTHER_EVENTS: bool
        EVENTS_TO_BIND_WITH: MXSWrapperBase
        BIND_WITH_DEFLECTORS: bool
        BIND_WITH_GROUND: bool
        DEFLECTORS_TO_BIND_WITH: MXSWrapperBase
        VISUALIZE_BINDING: bool
        COLOR: MXSWrapperBase
        SIMPLIFIED_BINDING_ANCHOR_TYPE: int
        RIGID_BINDING_ANCHOR_TYPE: int
        SOLVER_FACTOR: float
        USE_MINIMUM_DISTANCE_LIMIT: bool
        MINIMUM_DISTANCE_TYPE: int
        MINIMUM_ABSOLUTE_DISTANCE: float
        MINIMUM_RELATIVE_DISTANCE: float
        USE_MAXIMUM_DISTANCE_LIMIT: bool
        MAXIMUM_DISTANCE_TYPE: int
        MAXIMUM_ABSOLUTE_DISTANCE: float
        MAXIMUM_RELATIVE_DISTANCE: float
        ENABLE_SPRING_FORCE: bool
        ADJUST_BY_PARTICLE_MASS: bool
        SPRING_COEF: float
        DAMPER_COEF: float
        BURY_BINDING_ANCHORS: bool
        DEPTH: float
        BREAKABLE_BY_OVERSTRETCH: bool
        OVERSTRETCH_TYPE: int
        OVERSTRETCH_ABSOLUTE_LIMIT: float
        OVERSTRETCH_RELATIVE_LIMIT: float
        BIND_DISTANCE_FROM_DATA: bool
        BIND_DISTANCE_DATA_CREATOR: None
        BIND_GAP_FROM_DATA: bool
        BIND_GAP_DATA_CREATOR: None
        BREAKABILITY_MAX_FORCE_FROM_DATA: bool
        BREAKABILITY_MAX_FORCE_DATA_CREATOR: None
        BREAKABILITY_MAX_TORQUE_FROM_DATA: bool
        BREAKABILITY_MAX_TORQUE_DATA_CREATOR: None
        MAX_BINDS_PER_PARTICLE_FROM_DATA: bool
        MAX_BINDS_PER_PARTICLE_DATA_CREATOR: None
        BINDING_GROUPS_FROM_DATA: bool
        BINDING_GROUPS_DATA_CREATOR: None
        MINIMUM_DISTANCE_LIMIT_FROM_DATA: bool
        MINIMUM_DISTANCE_LIMIT_DATA_CREATOR: None
        MAXIMUM_DISTANCE_LIMIT_FROM_DATA: bool
        MAXIMUM_DISTANCE_LIMIT_DATA_CREATOR: None
        SPRING_FORCE_COEF_FROM_DATA: bool
        SPRING_FORCE_COEF_DATA_CREATOR: None
        SPRING_DAMPER_COEF_FROM_DATA: bool
        SPRING_DAMPER_COEF_DATA_CREATOR: None
        OVERSTRETCH_DISTANCE_LIMIT_FROM_DATA: bool
        OVERSTRETCH_DISTANCE_LIMIT_DATA_CREATOR: None
        NUM_ACTIVE_BINDINGS_TO_DATA: bool
        NUM_ACTIVE_BINDINGS_DATA_CREATOR: None
        NUM_BROKEN_BINDINGS_TO_DATA: bool
        NUM_BROKEN_BINDINGS_DATA_CREATOR: None
        NUM_BROKEN_BY_FORCE_TO_DATA: bool
        NUM_BROKEN_BY_FORCE_DATA_CREATOR: None
        AVERAGE_BINDING_LENGTH_TO_DATA: bool
        AVERAGE_BINDING_LENGTH_DATA_CREATOR: None
        MINIMUM_BINDING_LENGTH_TO_DATA: bool
        MINIMUM_BINDING_LENGTH_DATA_CREATOR: None
        MAXIMUM_BINDING_LENGTH_TO_DATA: bool
        MAXIMUM_BINDING_LENGTH_DATA_CREATOR: None
        AVERAGE_BREAKING_IMPULSE_TO_DATA: bool
        AVERAGE_BREAKING_IMPULSE_DATA_CREATOR: None
        MAXIMUM_BREAKING_IMPULSE_TO_DATA: bool
        MAXIMUM_BREAKING_IMPULSE_DATA_CREATOR: None
        ...
    class PhysXInterCollision(Helper):
        SCOPE_TYPE: int
        SELECTED_EVENTS: MXSWrapperBase
        TEST_TYPE: int
        MIN_SPEED: float
        MAX_SPEED: float
        COLLISION_COUNT: int
        REPORT_TO_DATA_OPERATOR: bool
        ADDITIVE_COUNT: bool
        ...
    class PhysXModRB(Modifier):
        TYPE: int
        SWITCHTYPE: bool
        SWITCHTYPEATFRAME: int
        ENABLEGRAVITY: bool
        CONTINUOUSCOLLISIONDETECTION: bool
        SLEEPATSTART: bool
        COLLIDEWITHRIGIDBODIES: bool
        EXTRASHAPES: None
        MANUALSETUP: bool
        MATERIALID: int
        DENSITY: float
        VOLUME: float
        MASS: float
        STATICFRICTION: float
        DYNAMICFRICTION: float
        BOUNCINESS: float
        ENABLEADVANCEDSETTINGS: int
        CONTACTSHELLOVERRIDEGLOBALS: bool
        CONTACTSHELLCONTACTDISTANCE: float
        CONTACTSHELLRESTDEPTH: float
        SOLVERITER: bool
        SOLVERITERVALUE: int
        INITIALMOTIONSTYLE: int
        INITIALVELOCITYX: float
        INITIALVELOCITYY: float
        INITIALVELOCITYZ: float
        VELOCITYSPEED: float
        INITIALSPINX: float
        INITIALSPINY: float
        INITIALSPINZ: float
        SPINSPEED: float
        MASSCENTERX: float
        MASSCENTERY: float
        MASSCENTERZ: float
        LINEARDAMPING: float
        ANGULARDAMPING: float
        BAKED: int
        MESHTYPE: int
        MESHCUSTOMMESH: None
        MESHVERTICESLIMIT: int
        MESHINFLATION: float
        MESHCONVEXSTYLE: int
        MESHRADIUS: float
        MESHLENGTH: float
        MESHWIDTH: float
        MESHHEIGHT: float
        MESHOVERRIDEMATERIAL: bool
        COMPOSITEMAXVERTICES: int
        COMPOSITEMAXCONCAVITY: float
        SMALLCLUSTERTHRESHOLD: float
        ENABLESOLIDMESHES: bool
        COMPOSITEHIGHQUALITY: bool
        MASSCENTERMODE: int
        ENABLEBACKFACECOLLISION: bool
        FORCESLIST: MXSWrapperBase
        SHOWPHYSICALMESH: bool
        ...
    class PhysXPanel(ReferenceTarget):
        ENABLEGRAVITY: bool
        GRAVITYDIRECTION: int
        GRAVITY: float
        SLEEPSPEED: float
        SLEEPSPIN: float
        SOLVERITERATION: int
        USEGROUNDPLANE: bool
        ONLASTFRAME: int
        LOOPANIMATION: int
        USEFIRST: bool
        PHYSICALMESHES: int
        SUBSTEPS: int
        USEMULTITHREAD: bool
        USEHARDWARESCENE: bool
        ENABLECCD: bool
        SLEEPTHRESHOLDSAUTOMATIC: int
        CCDMINSPEEDAUTOMATIC: int
        BOUNCEMINSPEEDAUTOMATIC: int
        CCDMINSPEEDTHRESHOLD: float
        BOUNCEMINSPEEDTHRESHOLD: float
        VISUALIZERENABLE: bool
        VISUALIZERSCALE: float
        BODYAXIS: bool
        BODYLINEARVEL: bool
        BODYANGULARVEL: bool
        JOINTLOCALAXIS: bool
        JOINTWORLDAXIS: bool
        JOINTLIMITS: bool
        CONTACTPOINTS: bool
        CONTACTNORMAL: bool
        CONTACTFORCE: bool
        COLLISIONSHAPES: bool
        COLLISIONCOMPOUNDS: bool
        COLLISIONSPHERES: bool
        GRAVITYMODE: int
        GRAVITYOBJECT: None
        GROUNDHEIGHT: float
        SHAPEPERELEMENT: bool
        EXPORTERMODE: int
        SLEEPENERGY: float
        PLUGINBUILD: str
        USEADAPTIVEFORCE: bool
        DESTRUCTIONRADIUS: float
        DESTRUCTIONDAMAGE: float
        DESTRUCTIONMOMENTUM: float
        CONTACTSHELLLEGACYMODE: bool
        CONTACTSHELLCONTACTDISTANCE: float
        SKINWIDTH: float
        PLUGINPROPERTYVERSION: int
        UNITTYPE: int
        UNITSCALE: float
        DYNAMICFRICTIONSCALE: float
        STATICFRICTIONSCALE: float
        MAXANGLEVELOCITY: float
        CCDEPSILON: float
        GEOMETRYSCALE: float
        RESTOREORIGINALPOSE: bool
        ...
    class PhysXPanelGUP(GlobalUtilityPlugin):
        ...
    class PhysXPanelGlobalUtilityPlugin(GlobalUtilityPlugin):
        ...
    class PhysXPanelInterface(Interface):
        ...
    class PhysXPanelReferenceTarget(ReferenceTarget):
        ENABLEGRAVITY: bool
        GRAVITYDIRECTION: int
        GRAVITY: float
        SLEEPSPEED: float
        SLEEPSPIN: float
        SOLVERITERATION: int
        USEGROUNDPLANE: bool
        ONLASTFRAME: int
        LOOPANIMATION: int
        USEFIRST: bool
        PHYSICALMESHES: int
        SUBSTEPS: int
        USEMULTITHREAD: bool
        USEHARDWARESCENE: bool
        ENABLECCD: bool
        SLEEPTHRESHOLDSAUTOMATIC: int
        CCDMINSPEEDAUTOMATIC: int
        BOUNCEMINSPEEDAUTOMATIC: int
        CCDMINSPEEDTHRESHOLD: float
        BOUNCEMINSPEEDTHRESHOLD: float
        VISUALIZERENABLE: bool
        VISUALIZERSCALE: float
        BODYAXIS: bool
        BODYLINEARVEL: bool
        BODYANGULARVEL: bool
        JOINTLOCALAXIS: bool
        JOINTWORLDAXIS: bool
        JOINTLIMITS: bool
        CONTACTPOINTS: bool
        CONTACTNORMAL: bool
        CONTACTFORCE: bool
        COLLISIONSHAPES: bool
        COLLISIONCOMPOUNDS: bool
        COLLISIONSPHERES: bool
        GRAVITYMODE: int
        GRAVITYOBJECT: None
        GROUNDHEIGHT: float
        SHAPEPERELEMENT: bool
        EXPORTERMODE: int
        SLEEPENERGY: float
        PLUGINBUILD: str
        USEADAPTIVEFORCE: bool
        DESTRUCTIONRADIUS: float
        DESTRUCTIONDAMAGE: float
        DESTRUCTIONMOMENTUM: float
        CONTACTSHELLLEGACYMODE: bool
        CONTACTSHELLCONTACTDISTANCE: float
        SKINWIDTH: float
        PLUGINPROPERTYVERSION: int
        UNITTYPE: int
        UNITSCALE: float
        DYNAMICFRICTIONSCALE: float
        STATICFRICTIONSCALE: float
        MAXANGLEVELOCITY: float
        CCDEPSILON: float
        GEOMETRYSCALE: float
        RESTOREORIGINALPOSE: bool
        ...
    class PhysXShape(Helper):
        COLLIDE_TYPE: int
        DISPLAY_TYPE: int
        CONFORM_TO_PARTICLE_SHAPE: bool
        SHAPE_LENGTH: float
        SHAPE_WIDTH: float
        SHAPE_HEIGHT: float
        SCALE_TYPE: int
        SCALE: MXSWrapperBase
        COLOR: MXSWrapperBase
        WELD_THRESHOLD: float
        INFLATE_WIDTH: float
        SCALE_MARGIN: float
        RESTITUTION: float
        STATIC_FRICTION: float
        DYNAMIC_FRICTION: float
        MASS_TYPE: int
        MASS: float
        DENSITY: float
        INTERPENETRATION_TOLERANCE: float
        GENERATE_TOLERANCE_CHANNEL: bool
        COLLISION_GROUP: int
        ...
    class PhysXShapeConvex(GeometryClass):
        ...
    class PhysXShapeWSM(SpacewarpModifier):
        SHAPE: int
        SMOOTH_SURFACE: bool
        RESTITUTION: float
        STATIC_FRICTION: float
        DYNAMIC_FRICTION: float
        VISUALIZE_COLLISION_SHAPE: bool
        THICKNESS: float
        NORMAL_OFFSET: float
        SIDE_OVERLAP: float
        PLACEMENT_VERTICES: bool
        PLACEMENT_EDGES: bool
        PLACEMENT_POLYGONS: bool
        SELECTED_ONLY: bool
        ACTIVE: bool
        PRIMITIVE_SIZE_TYPE: int
        ...
    class PhysXSolvent(Helper):
        PARTICLES_TO_PARTICLES: bool
        PARTICLES_TO_DEFLECTORS: bool
        PARTICLES_TO_GROUND: bool
        LIMIT_SOLVENT_BY_LIST: bool
        GLUE_TESTS: MXSWrapperBase
        LIMIT_SOLVENT_BY_TIME: bool
        START: int
        STOP: int
        LIMIT_SOLVENT_BY_DATA: bool
        DATA_CHANNEL: None
        LIMIT_SOLVENT_BY_ICON: bool
        MODE: int
        ICON_SHAPE: int
        ICON_SIZE: float
        COLOR_COORDINATED: bool
        ...
    class PhysXSwitch(Helper):
        MATCH_POSITION: bool
        MATCH_SPEED: bool
        POSITION_SPEED_MATCH_TYPE: int
        POSITION_SPEED_START: int
        POSITION_SPEED_STOP: int
        POSITION_SPEED_ACTIVE: bool
        POSITION_SPEED_SYNC_TYPE: int
        USE_SPEED_LIMIT: bool
        SPEED_LIMIT: float
        MATCH_ROTATION: bool
        MATCH_SPIN: bool
        ROTATION_SPIN_MATCH_TYPE: int
        ROTATION_SPIN_START: int
        ROTATION_SPIN_STOP: int
        ROTATION_SPIN_ACTIVE: bool
        ROTATION_SPIN_SYNC_TYPE: int
        USE_SPIN_LIMIT: bool
        SPIN_LIMIT: float
        APPLY_ANTI_GRAVITY: bool
        ANTIGRAVITY_TYPE: int
        ANTIGRAVITY_START: int
        ANTIGRAVITY_STOP: int
        ANTIGRAVITY_ACTIVE: bool
        ANTI_GRAVITY_SYNC_TYPE: int
        TURN_OFF_SIMULATION: bool
        TURN_OFF_SIMULATION_TYPE: int
        TURN_OFF_START: int
        TURN_OFF_STOP: int
        TURN_OFF_ACTIVE: bool
        TURN_OFF_SYNC_TYPE: int
        ...
    class PhysXWorld(Helper):
        APPLY_GRAVITY: bool
        GRAVITY_ACCELERATION: float
        GROUND_COLLISION_PLANE: bool
        SET_WORLD_LIMITS: bool
        ICON_LENGTH: float
        ICON_WIDTH: float
        ICON_HEIGHT: float
        COLLISION_GROUP: int
        DEFAULT_RESTITUTION: float
        DEFAULT_STATIC_FRICTION: float
        DEFAULT_DYNAMIC_FRICTION: float
        RUN_BAKED_SIMULATION: bool
        RANGE_TYPE: int
        RANGE_START: int
        RANGE_FINISH: int
        UPDATE_VIEWPORTS: bool
        HIDE_ICON: bool
        HIDE_PARTICLE_BINDINGS: bool
        SHOW_BAKE_DIALOG: int
        SUBFRAME_FACTOR: int
        SUBFRAME_TYPE: int
        USE_TIME_SCALE: bool
        TIME_SCALE: float
        ENERGY_THRESHOLD: float
        SPEED_THRESHOLD: float
        SPIN_RATE_THRESHOLD: float
        SLEEP_THRESHOLD_TYPE: int
        BOUNCE_THRESHOLD: float
        ENABLE_MULTI_THREADING: bool
        THREAD_COUNT: int
        USE_HARDWARE_PPU: bool
        RESTRICTED_BROADPHASE: bool
        SAFE_MODE_SIMULATION: bool
        CALCULATION_LIMIT: int
        ...
    class PhysX_Debug_Visualizer(UtilityPlugin):
        ...
    class PhysX_Shape_Convex(GeometryClass):
        ...
    class PhysX_World(Helper):
        PHYSX_WORLD_DRIVER: None
        SUPPRESS_EXPRESS_SAVE: bool
        PHYSX_DRIVER_TYPE: int
        ...
    class PhysX_And_APEX_Exporter(ExporterPlugin):
        ...
    class Physical(Camera):
        TARGETED: bool
        TARGET_DISTANCE: float
        SHOW_CAMERA_CONE: int
        HORIZON_ON: bool
        SHOW_FOCUS_PLANE_IN_CAM_VIEW: bool
        FILM_PRESET: str
        FILM_WIDTH_MM: float
        FOCAL_LENGTH_MM: float
        SPECIFY_FOV: bool
        FOV: float
        ZOOM_FACTOR: float
        F_NUMBER: float
        USE_DOF: bool
        SPECIFY_FOCUS: int
        FOCUS_DISTANCE: float
        LENS_BREATHING_AMOUNT: float
        SHUTTER_UNIT_TYPE: int
        SHUTTER_LENGTH_SECONDS: float
        SHUTTER_OFFSET_SECONDS: float
        SHUTTER_LENGTH_FRAMES: float
        SHUTTER_OFFSET_FRAMES: float
        SHUTTER_OFFSET_ENABLED: bool
        MOTION_BLUR_ENABLED: bool
        EXPOSURE_GAIN_TYPE: int
        ISO: float
        EXPOSURE_VALUE: float
        WHITE_BALANCE_TYPE: int
        WHITE_BALANCE_ILLUMINANT: int
        WHITE_BALANCE_KELVIN: float
        WHITE_BALANCE_CUSTOM: MXSWrapperBase
        VIGNETTING_ENABLED: bool
        VIGNETTING_AMOUNT: float
        BOKEH_SHAPE: int
        BOKEH_BLADES_NUMBER: int
        PB_BOKEH_BLADES_ROTATION_DEGREES: float
        BOKEH_TEXTURE: None
        BOKEH_TEXTURE_AFFECT_EXPOSURE: bool
        BOKEH_OPTICAL_VIGNETTING: float
        BOKEH_CENTER_BIAS: float
        BOKEH_ANISOTROPY: float
        HORIZONTAL_SHIFT: float
        VERTICAL_SHIFT: float
        HORIZONTAL_TILT_CORRECTION: float
        VERTICAL_TILT_CORRECTION: float
        AUTO_VERTICAL_TILT_CORRECTION: bool
        DISTORTION_TYPE: int
        DISTORTION_CUBIC_AMOUNT: float
        DISTORTION_TEXTURE: None
        CLIP_ON: bool
        CLIP_NEAR: float
        CLIP_FAR: float
        ENVIRONMENT_NEAR: float
        ENVIRONMENT_FAR: float
        ...
    class PhysicalMaterial(Material):
        MATERIAL_MODE: int
        BASE_WEIGHT: float
        BASE_COLOR: MXSWrapperBase
        REFLECTIVITY: float
        ROUGHNESS: float
        ROUGHNESS_INV: bool
        METALNESS: float
        REFL_COLOR: MXSWrapperBase
        DIFF_ROUGHNESS: float
        BRDF_MODE: bool
        BRDF_LOW: float
        BRDF_HIGH: float
        BRDF_CURVE: float
        ANISOTROPY: float
        ANISOANGLE: float
        ANISO_MODE: int
        ANISO_CHANNEL: int
        TRANSPARENCY: float
        TRANS_COLOR: MXSWrapperBase
        TRANS_DEPTH: float
        TRANS_ROUGHNESS: float
        TRANS_ROUGHNESS_INV: bool
        TRANS_ROUGHNESS_LOCK: bool
        TRANS_IOR: float
        THIN_WALLED: bool
        SCATTERING: float
        SSS_COLOR: MXSWrapperBase
        SSS_DEPTH: float
        SSS_SCALE: float
        SSS_SCATTER_COLOR: MXSWrapperBase
        EMISSION: float
        EMIT_COLOR: MXSWrapperBase
        EMIT_LUMINANCE: float
        EMIT_KELVIN: float
        COATING: float
        COAT_COLOR: MXSWrapperBase
        COAT_ROUGHNESS: float
        COAT_ROUGHNESS_INV: bool
        COAT_AFFECT_COLOR: float
        COAT_AFFECT_ROUGHNESS: float
        COAT_IOR: float
        BASE_WEIGHT_MAP: None
        BASE_COLOR_MAP: None
        REFLECTIVITY_MAP: None
        REFL_COLOR_MAP: None
        ROUGHNESS_MAP: None
        METALNESS_MAP: None
        DIFF_ROUGH_MAP: None
        ANISOTROPY_MAP: None
        ANISO_ANGLE_MAP: None
        TRANSPARENCY_MAP: None
        TRANS_COLOR_MAP: None
        TRANS_ROUGH_MAP: None
        TRANS_IOR_MAP: None
        SCATTERING_MAP: None
        SSS_COLOR_MAP: None
        SSS_SCALE_MAP: None
        EMISSION_MAP: None
        EMIT_COLOR_MAP: None
        COAT_MAP: None
        COAT_COLOR_MAP: None
        COAT_ROUGH_MAP: None
        BUMP_MAP: None
        COAT_BUMP_MAP: None
        DISPLACEMENT_MAP: None
        CUTOUT_MAP: None
        BASE_WEIGHT_MAP_ON: bool
        BASE_COLOR_MAP_ON: bool
        REFLECTIVITY_MAP_ON: bool
        REFL_COLOR_MAP_ON: bool
        ROUGHNESS_MAP_ON: bool
        METALNESS_MAP_ON: bool
        DIFF_ROUGH_MAP_ON: bool
        ANISOTROPY_MAP_ON: bool
        ANISO_ANGLE_MAP_ON: bool
        TRANSPARENCY_MAP_ON: bool
        TRANS_COLOR_MAP_ON: bool
        TRANS_ROUGH_MAP_ON: bool
        TRANS_IOR_MAP_ON: bool
        SCATTERING_MAP_ON: bool
        SSS_COLOR_MAP_ON: bool
        SSS_SCALE_MAP_ON: bool
        EMISSION_MAP_ON: bool
        EMIT_COLOR_MAP_ON: bool
        COAT_MAP_ON: bool
        COAT_COLOR_MAP_ON: bool
        COAT_ROUGH_MAP_ON: bool
        BUMP_MAP_ON: bool
        COAT_BUMP_MAP_ON: bool
        DISPLACEMENT_MAP_ON: bool
        CUTOUT_MAP_ON: bool
        BUMP_MAP_AMT: float
        CLEARCOAT_BUMP_MAP_AMT: float
        DISPLACEMENT_MAP_AMT: float
        ...
    class PhysicalMaterialManager(GlobalUtilityPlugin):
        ...
    class PhysicalSunSkyEnv(TextureMap):
        SUN_POSITION_OBJECT: None
        GLOBAL_INTENSITY: float
        HAZE: float
        SUN_ENABLED: bool
        SUN_DISC_INTENSITY: float
        SUN_GLOW_INTENSITY: float
        SUN_DISC_SCALE: float
        SUN_DISC_SCALE_PERCENT: float
        SKY_INTENSITY: float
        NIGHT_COLOR: MXSWrapperBase
        NIGHT_INTENSITY: float
        HORIZON_HEIGHT_DEG: float
        HORIZON_BLUR_DEG: float
        GROUND_COLOR: MXSWrapperBase
        SATURATION: float
        TINT: MXSWrapperBase
        ILLUMINANCE_MODEL: int
        PEREZ_DIFFUSE_HORIZONTAL_ILLUMINANCE: float
        PEREZ_DIRECT_NORMAL_ILLUMINANCE: float
        ...
    class Physical_Camera(Camera):
        TARGETED: bool
        TARGET_DISTANCE: float
        SHOW_CAMERA_CONE: int
        HORIZON_ON: bool
        SHOW_FOCUS_PLANE_IN_CAM_VIEW: bool
        FILM_PRESET: str
        FILM_WIDTH_MM: float
        FOCAL_LENGTH_MM: float
        SPECIFY_FOV: bool
        FOV: float
        ZOOM_FACTOR: float
        F_NUMBER: float
        USE_DOF: bool
        SPECIFY_FOCUS: int
        FOCUS_DISTANCE: float
        LENS_BREATHING_AMOUNT: float
        SHUTTER_UNIT_TYPE: int
        SHUTTER_LENGTH_SECONDS: float
        SHUTTER_OFFSET_SECONDS: float
        SHUTTER_LENGTH_FRAMES: float
        SHUTTER_OFFSET_FRAMES: float
        SHUTTER_OFFSET_ENABLED: bool
        MOTION_BLUR_ENABLED: bool
        EXPOSURE_GAIN_TYPE: int
        ISO: float
        EXPOSURE_VALUE: float
        WHITE_BALANCE_TYPE: int
        WHITE_BALANCE_ILLUMINANT: int
        WHITE_BALANCE_KELVIN: float
        WHITE_BALANCE_CUSTOM: MXSWrapperBase
        VIGNETTING_ENABLED: bool
        VIGNETTING_AMOUNT: float
        BOKEH_SHAPE: int
        BOKEH_BLADES_NUMBER: int
        PB_BOKEH_BLADES_ROTATION_DEGREES: float
        BOKEH_TEXTURE: None
        BOKEH_TEXTURE_AFFECT_EXPOSURE: bool
        BOKEH_OPTICAL_VIGNETTING: float
        BOKEH_CENTER_BIAS: float
        BOKEH_ANISOTROPY: float
        HORIZONTAL_SHIFT: float
        VERTICAL_SHIFT: float
        HORIZONTAL_TILT_CORRECTION: float
        VERTICAL_TILT_CORRECTION: float
        AUTO_VERTICAL_TILT_CORRECTION: bool
        DISTORTION_TYPE: int
        DISTORTION_CUBIC_AMOUNT: float
        DISTORTION_TEXTURE: None
        CLIP_ON: bool
        CLIP_NEAR: float
        CLIP_FAR: float
        ENVIRONMENT_NEAR: float
        ENVIRONMENT_FAR: float
        ...
    class Physical_Camera_Exposure_Control(ToneOperator):
        HIGHLIGHTS: float
        MIDTONES: float
        SHADOWS: float
        SATURATION: float
        PHYSICAL_SCALE_MODE: int
        PHYSICAL_SCALE: float
        USE_PHYSICAL_CAMERA_CONTROLS: bool
        USE_GLOBAL_EV: int
        GLOBAL_EV: float
        EV_COMPENSATION: float
        ACTIVE: bool
        PROCESSBG: bool
        WHITE_BALANCE_TYPE: int
        WHITE_BALANCE_ILLUMINANT: int
        WHITE_BALANCE_ILLUMINANT_COLORPREVIEW: MXSWrapperBase
        WHITE_BALANCE_KELVIN: float
        WHITE_BALANCE_KELVIN_COLORPREVIEW: MXSWrapperBase
        WHITE_BALANCE_CUSTOM: MXSWrapperBase
        VIGNETTING_ENABLED: bool
        VIGNETTING_AMOUNT: float
        ...
    class Physical_Material(Material):
        MATERIAL_MODE: int
        BASE_WEIGHT: float
        BASE_COLOR: MXSWrapperBase
        REFLECTIVITY: float
        ROUGHNESS: float
        ROUGHNESS_INV: bool
        METALNESS: float
        REFL_COLOR: MXSWrapperBase
        DIFF_ROUGHNESS: float
        BRDF_MODE: bool
        BRDF_LOW: float
        BRDF_HIGH: float
        BRDF_CURVE: float
        ANISOTROPY: float
        ANISOANGLE: float
        ANISO_MODE: int
        ANISO_CHANNEL: int
        TRANSPARENCY: float
        TRANS_COLOR: MXSWrapperBase
        TRANS_DEPTH: float
        TRANS_ROUGHNESS: float
        TRANS_ROUGHNESS_INV: bool
        TRANS_ROUGHNESS_LOCK: bool
        TRANS_IOR: float
        THIN_WALLED: bool
        SCATTERING: float
        SSS_COLOR: MXSWrapperBase
        SSS_DEPTH: float
        SSS_SCALE: float
        SSS_SCATTER_COLOR: MXSWrapperBase
        EMISSION: float
        EMIT_COLOR: MXSWrapperBase
        EMIT_LUMINANCE: float
        EMIT_KELVIN: float
        COATING: float
        COAT_COLOR: MXSWrapperBase
        COAT_ROUGHNESS: float
        COAT_ROUGHNESS_INV: bool
        COAT_AFFECT_COLOR: float
        COAT_AFFECT_ROUGHNESS: float
        COAT_IOR: float
        BASE_WEIGHT_MAP: None
        BASE_COLOR_MAP: None
        REFLECTIVITY_MAP: None
        REFL_COLOR_MAP: None
        ROUGHNESS_MAP: None
        METALNESS_MAP: None
        DIFF_ROUGH_MAP: None
        ANISOTROPY_MAP: None
        ANISO_ANGLE_MAP: None
        TRANSPARENCY_MAP: None
        TRANS_COLOR_MAP: None
        TRANS_ROUGH_MAP: None
        TRANS_IOR_MAP: None
        SCATTERING_MAP: None
        SSS_COLOR_MAP: None
        SSS_SCALE_MAP: None
        EMISSION_MAP: None
        EMIT_COLOR_MAP: None
        COAT_MAP: None
        COAT_COLOR_MAP: None
        COAT_ROUGH_MAP: None
        BUMP_MAP: None
        COAT_BUMP_MAP: None
        DISPLACEMENT_MAP: None
        CUTOUT_MAP: None
        BASE_WEIGHT_MAP_ON: bool
        BASE_COLOR_MAP_ON: bool
        REFLECTIVITY_MAP_ON: bool
        REFL_COLOR_MAP_ON: bool
        ROUGHNESS_MAP_ON: bool
        METALNESS_MAP_ON: bool
        DIFF_ROUGH_MAP_ON: bool
        ANISOTROPY_MAP_ON: bool
        ANISO_ANGLE_MAP_ON: bool
        TRANSPARENCY_MAP_ON: bool
        TRANS_COLOR_MAP_ON: bool
        TRANS_ROUGH_MAP_ON: bool
        TRANS_IOR_MAP_ON: bool
        SCATTERING_MAP_ON: bool
        SSS_COLOR_MAP_ON: bool
        SSS_SCALE_MAP_ON: bool
        EMISSION_MAP_ON: bool
        EMIT_COLOR_MAP_ON: bool
        COAT_MAP_ON: bool
        COAT_COLOR_MAP_ON: bool
        COAT_ROUGH_MAP_ON: bool
        BUMP_MAP_ON: bool
        COAT_BUMP_MAP_ON: bool
        DISPLACEMENT_MAP_ON: bool
        CUTOUT_MAP_ON: bool
        BUMP_MAP_AMT: float
        CLEARCOAT_BUMP_MAP_AMT: float
        DISPLACEMENT_MAP_AMT: float
        ...
    class Physical_Sun___Sky_Environment(TextureMap):
        SUN_POSITION_OBJECT: None
        GLOBAL_INTENSITY: float
        HAZE: float
        SUN_ENABLED: bool
        SUN_DISC_INTENSITY: float
        SUN_GLOW_INTENSITY: float
        SUN_DISC_SCALE: float
        SUN_DISC_SCALE_PERCENT: float
        SKY_INTENSITY: float
        NIGHT_COLOR: MXSWrapperBase
        NIGHT_INTENSITY: float
        HORIZON_HEIGHT_DEG: float
        HORIZON_BLUR_DEG: float
        GROUND_COLOR: MXSWrapperBase
        SATURATION: float
        TINT: MXSWrapperBase
        ILLUMINANCE_MODEL: int
        PEREZ_DIFFUSE_HORIZONTAL_ILLUMINANCE: float
        PEREZ_DIRECT_NORMAL_ILLUMINANCE: float
        ...
    class Physique(Modifier):
        ...
    class PickerControl(RolloutControl):
        ...
    class Pipe(Shape):
        ...
    class PipeReferenceTarget(ReferenceTarget):
        DATA_TYPE: int
        VALVE_TYPE: int
        VECTOR_VALVE_TYPE: int
        INTEGER_VALVE_TYPE: int
        ANGLE_CONDITIONS: MXSWrapperBase
        FLOAT_CONDITIONS: MXSWrapperBase
        INTEGER_CONDITIONS: MXSWrapperBase
        PERCENT_CONDITIONS: MXSWrapperBase
        TIME_CONDITIONS: MXSWrapperBase
        WORLD_UNIT_CONDITIONS: MXSWrapperBase
        CONDITION_IS_RATE: bool
        UNITS_PER_TYPE: int
        FILTER: None
        INPUT_VALVE: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        INPUT_7: None
        INPUT_8: None
        ...
    class PivotPos(FloatController):
        ...
    class PivotRot(FloatController):
        ...
    class Pivoted(GeometryClass):
        HEIGHT: float
        WIDTH: float
        DEPTH: float
        VERTICAL_ROTATION: bool
        HORIZONTAL_FRAME_WIDTH: float
        VERTICAL_FRAME_WIDTH: float
        FRAME_THICKNESS: float
        GLAZING_THICKNESS: float
        RAIL_WIDTH: float
        PERCENT_OPEN: int
        GENERATE_MAPPING_COORDS: bool
        ...
    class PlacementTool(Interface):
        ...
    class Placement_Paint(Helper):
        PARTICLE_PAINT_HELPER: None
        UPDATE_TYPE: int
        ACQUIRE_PAINT_POSITION: bool
        POSITION_TYPE: int
        SNAP_IF_CLOSE: bool
        SNAP_DISTANCE: float
        ACQUIRE_PAINT_ROTATION: bool
        BLENDIN_ROTATION: bool
        NEAR_DISTANCE: float
        FAR_DISTANCE: float
        ACQUIRE_PAINT_MAPPING: bool
        ACQUIRE_PAINT_MATERIALID: bool
        ACQUIRE_PAINT_SELECTION: bool
        SELECTION_TYPE: int
        ORDER_TYPE: int
        STOP_IF_COUNT_OVERFLOW: bool
        OBEY_QUANTITY_MULTIPLIER: bool
        SEPARATE_STREAMS_INDEXING: bool
        RANDOM_SEED: int
        ...
    class PlanarCollision(ReferenceMaker):
        ...
    class Plane(GeometryClass):
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINLENGTH: float
        TYPEINWIDTH: float
        LENGTH: float
        WIDTH: float
        LENGTHSEGS: int
        WIDTHSEGS: int
        DENSITY: float
        RENDERSCALE: float
        MAPCOORDS: bool
        ...
    class PlaneAngleManip(Helper):
        ORIGIN: MXSWrapperBase
        NORMALVEC: MXSWrapperBase
        UPVEC: MXSWrapperBase
        ANGLE: float
        DISTANCE: float
        SIZE: float
        ...
    class Plane_Angle(Helper):
        ORIGIN: MXSWrapperBase
        NORMALVEC: MXSWrapperBase
        UPVEC: MXSWrapperBase
        ANGLE: float
        DISTANCE: float
        SIZE: float
        ...
    class Planet(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        COLOR3: MXSWrapperBase
        COLOR4: MXSWrapperBase
        COLOR5: MXSWrapperBase
        COLOR6: MXSWrapperBase
        COLOR7: MXSWrapperBase
        COLOR8: MXSWrapperBase
        CONTINENTSIZE: float
        ISLANDFACTOR: float
        OCEANPERCENT: float
        RANDOMSEED: int
        BLENDWATERLAND: bool
        COORDS: MXSWrapperBase
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
        SIZE: float
        CENTERMARKER: bool
        AXISTRIPOD: bool
        CROSS: bool
        BOX: bool
        CONSTANTSCREENSIZE: bool
        DRAWONTOP: bool
        ...
    class Point2(Value):
        ...
    class Point2Controller(MAXWrapper):
        ...
    class Point3Layer(Point3Controller):
        ...
    class Point3List(Point3Controller):
        WEIGHT: MXSWrapperBase
        AVERAGE: bool
        ...
    class Point3Reactor(Point3Controller):
        ...
    class Point3Spring(Point3Controller):
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
        WEIGHT: MXSWrapperBase
        AVERAGE: bool
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
        FILENAME: str
        RECORDSTART: float
        RECORDEND: float
        SAMPLERATE: float
        STRENGTH: float
        RELATIVEOFFSET: bool
        PLAYBACKTYPE: int
        PLAYBACKSTART: float
        PLAYBACKEND: float
        PLAYBACKORTBEFORE: int
        PLAYBACKORTAFTER: int
        PLAYBACKFRAME: float
        INTERPOLATIONTYPE: int
        APPLYMESHTOSPLINE: bool
        PRELOADCACHE: bool
        CLAMPGRAPH: bool
        FORCEUNCPATH: bool
        LOADTYPE: int
        APPLYTOWHOLEOBJECT: bool
        LOADTYPESLAVE: int
        FILECOUNT: int
        ...
    class PointCacheWSM(SpacewarpModifier):
        FILENAME: str
        RECORDSTART: float
        RECORDEND: float
        SAMPLERATE: float
        STRENGTH: float
        RELATIVEOFFSET: bool
        PLAYBACKTYPE: int
        PLAYBACKSTART: float
        PLAYBACKEND: float
        PLAYBACKORTBEFORE: int
        PLAYBACKORTAFTER: int
        PLAYBACKFRAME: float
        INTERPOLATIONTYPE: int
        APPLYMESHTOSPLINE: bool
        PRELOADCACHE: bool
        CLAMPGRAPH: bool
        FORCEUNCPATH: bool
        LOADTYPE: int
        APPLYTOWHOLEOBJECT: bool
        LOADTYPESLAVE: int
        FILECOUNT: int
        ...
    class PointCloud(GeometryClass):
        FILENAME: str
        SCANFILES: MXSWrapperBase
        PTSVISIBLE: MXSWrapperBase
        VOXELSIZE: float
        ASPIXELPOINTSIZE: float
        REALWORLDSCALEPOINTSIZE: float
        POINTSIZETYPE: int
        DISPLAYTECHNIQUE: int
        SINGLECOLOR: MXSWrapperBase
        GRADIENTTEXMAP: MXSWrapperBase
        PERFORMANCEQUALITY: int
        FIXEDLODENABLE: bool
        FIXEDLODLEVEL: int
        ENABLELIMITPLANES: bool
        GLOBALENABLEVOLUMES: bool
        GLOBALINVERTVOLUMES: bool
        VOLUMEOBJECTS: MXSWrapperBase
        SHADER: None
        ...
    class PointHelperObj(Helper):
        SIZE: float
        CENTERMARKER: bool
        AXISTRIPOD: bool
        CROSS: bool
        BOX: bool
        CONSTANTSCREENSIZE: bool
        DRAWONTOP: bool
        ...
    class PointPacket(ReferenceMaker):
        ...
    class PointSelection(Primitive):
        ...
    class Point_Cache(Modifier):
        FILENAME: str
        RECORDSTART: float
        RECORDEND: float
        SAMPLERATE: float
        STRENGTH: float
        RELATIVEOFFSET: bool
        PLAYBACKTYPE: int
        PLAYBACKSTART: float
        PLAYBACKEND: float
        PLAYBACKORTBEFORE: int
        PLAYBACKORTAFTER: int
        PLAYBACKFRAME: float
        INTERPOLATIONTYPE: int
        APPLYMESHTOSPLINE: bool
        PRELOADCACHE: bool
        CLAMPGRAPH: bool
        FORCEUNCPATH: bool
        LOADTYPE: int
        APPLYTOWHOLEOBJECT: bool
        LOADTYPESLAVE: int
        FILECOUNT: int
        ...
    class Point_CacheSpacewarpModifier(SpacewarpModifier):
        FILENAME: str
        RECORDSTART: float
        RECORDEND: float
        SAMPLERATE: float
        STRENGTH: float
        RELATIVEOFFSET: bool
        PLAYBACKTYPE: int
        PLAYBACKSTART: float
        PLAYBACKEND: float
        PLAYBACKORTBEFORE: int
        PLAYBACKORTAFTER: int
        PLAYBACKFRAME: float
        INTERPOLATIONTYPE: int
        APPLYMESHTOSPLINE: bool
        PRELOADCACHE: bool
        CLAMPGRAPH: bool
        FORCEUNCPATH: bool
        LOADTYPE: int
        APPLYTOWHOLEOBJECT: bool
        LOADTYPESLAVE: int
        FILECOUNT: int
        ...
    class Point_Curve(Shape):
        RENDER_THICKNESS: float
        RENDER_SIDES: int
        RENDER_ANGLE: float
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        RENDER_WIDTH: float
        RENDER_LENGTH: float
        RENDER_ANGLE2: float
        RENDER_THRESHOLD: float
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
        USESOFTSELECTION: bool
        SOFTSELUSEEDGEDISTANCE: bool
        SOFTSELEDGEDIST: int
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELBUBBLE: float
        LOCKSOFTSEL: bool
        PAINTSELMODE: int
        PAINTSELVALUE: float
        PAINTSELSIZE: float
        PAINTSELSTRENGTH: float
        BYVERTEX: bool
        IGNOREBACKFACING: bool
        MATERIALID: int
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
        USESOFTSELECTION: bool
        SOFTSELUSEEDGEDISTANCE: bool
        SOFTSELEDGEDIST: int
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELBUBBLE: float
        LOCKSOFTSEL: bool
        PAINTSELMODE: int
        PAINTSELVALUE: float
        PAINTSELSIZE: float
        PAINTSELSTRENGTH: float
        BYVERTEX: bool
        IGNOREBACKFACING: bool
        MATERIALID: int
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
        WEIGHT: MXSWrapperBase
        AVERAGE: bool
        ...
    class PositionManip(Helper):
        ...
    class PositionReactor(PositionController):
        ...
    class PositionSpring(PositionController):
        EFFECTHOW: int
        FORCENODE: MXSWrapperBase
        STEPS: int
        X_EFFECT: float
        Y_EFFECT: float
        Z_EFFECT: float
        START: int
        ...
    class PositionValueManip(Helper):
        ...
    class Position_Constraint(PositionController):
        WEIGHT: MXSWrapperBase
        RELATIVE: bool
        ...
    class Position_Expression(PositionController):
        ...
    class Position_Icon(Helper):
        LOCK_ON_EMITTER: bool
        INHERIT_EMITTER_MOVEMENT: bool
        MULTIPLIER: float
        LOCATION: int
        DISTINCT_POINTS_ONLY: bool
        TOTAL_DISTINCT_POINTS: int
        SUBFRAME_SAMPLING: bool
        RANDOM_SEED: int
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
        LOCK_ON_EMITTER: bool
        INHERIT_EMITTER_MOVEMENT: bool
        MULTIPLIER: float
        VARIATION: float
        EMITTER_OBJECTS: MXSWrapperBase
        ANIMATED_SHAPE: bool
        SUBFRAME_SAMPLING: bool
        LOCATION: int
        USE_SURFACE_OFFSET: bool
        SURFACE_OFFSET_MINIMUM: float
        SURFACE_OFFSET_MAXIMUM: float
        DENSITY_BY_EMITTER_MATERIAL: bool
        DENSITY_TYPE: int
        USE_SUB_MATERIAL: bool
        MATERIAL_ID: int
        APART_PLACEMENT: bool
        APART_DISTANCE: float
        DISTINCT_POINTS_ONLY: bool
        TOTAL_DISTINCT_POINTS: int
        DELETE: bool
        RANDOM_SEED: int
        MAXIMUM_NUMBER_OF_ATTEMPTS: int
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
        ITERATIONS: int
        EDGE_LENGTH_WEIGHT: float
        FACE_ANGLE_WEIGHT: float
        VOLUME_WEIGHT: float
        APPLY_TO_WHOLE_MESH: int
        SELECTED_VERTS_ONLY: int
        INVERT_SELECTION: int
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
        ICON_TYPE: int
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        COLOR_COORDINATED: bool
        AUTO_UPDATE: bool
        SUBOPERATORS: MXSWrapperBase
        SELECTED_SUBOPERATORS: MXSWrapperBase
        GROUPS: MXSWrapperBase
        ENABLE_BY_SWITCH: bool
        DEFAULT_WIDTH: int
        DEFAULT_OFFSET: int
        DEFAULT_HEIGHT: int
        DEFAULT_RANGE_TYPE: int
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_MAX: float
        ACTIVITY_TYPE: int
        TIME_ON: int
        TIME_OFF: int
        ANIMATABLE_ACTIVE: bool
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_WIDTH: int
        PDVIEW_HEIGHT: int
        PDVIEW_DIVIDER: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_SHOW_PARAMETERS: bool
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        REPEATS: int
        ...
    class PresetOperator(Helper):
        ICON_TYPE: int
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        COLOR_COORDINATED: bool
        AUTO_UPDATE: bool
        SUBOPERATORS: MXSWrapperBase
        SELECTED_SUBOPERATORS: MXSWrapperBase
        GROUPS: MXSWrapperBase
        ENABLE_BY_SWITCH: bool
        DEFAULT_WIDTH: int
        DEFAULT_OFFSET: int
        DEFAULT_HEIGHT: int
        DEFAULT_RANGE_TYPE: int
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_MAX: float
        ACTIVITY_TYPE: int
        TIME_ON: int
        TIME_OFF: int
        ANIMATABLE_ACTIVE: bool
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_WIDTH: int
        PDVIEW_HEIGHT: int
        PDVIEW_DIVIDER: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_SHOW_PARAMETERS: bool
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        REPEATS: int
        ...
    class PresetTest(Helper):
        ICON_TYPE: int
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        COLOR_COORDINATED: bool
        AUTO_UPDATE: bool
        SUBOPERATORS: MXSWrapperBase
        SELECTED_SUBOPERATORS: MXSWrapperBase
        GROUPS: MXSWrapperBase
        ENABLE_BY_SWITCH: bool
        DEFAULT_WIDTH: int
        DEFAULT_OFFSET: int
        DEFAULT_HEIGHT: int
        DEFAULT_RANGE_TYPE: int
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_MAX: float
        ACTIVITY_TYPE: int
        TIME_ON: int
        TIME_OFF: int
        ANIMATABLE_ACTIVE: bool
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_WIDTH: int
        PDVIEW_HEIGHT: int
        PDVIEW_DIVIDER: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_SHOW_PARAMETERS: bool
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        REPEATS: int
        ...
    class PresetTestIcon(Helper):
        ICON_TYPE: int
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        COLOR_COORDINATED: bool
        AUTO_UPDATE: bool
        SUBOPERATORS: MXSWrapperBase
        SELECTED_SUBOPERATORS: MXSWrapperBase
        GROUPS: MXSWrapperBase
        ENABLE_BY_SWITCH: bool
        DEFAULT_WIDTH: int
        DEFAULT_OFFSET: int
        DEFAULT_HEIGHT: int
        DEFAULT_RANGE_TYPE: int
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_MAX: float
        ACTIVITY_TYPE: int
        TIME_ON: int
        TIME_OFF: int
        ANIMATABLE_ACTIVE: bool
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_WIDTH: int
        PDVIEW_HEIGHT: int
        PDVIEW_DIVIDER: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_SHOW_PARAMETERS: bool
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        REPEATS: int
        ...
    class Preset_Flow(ReferenceTarget):
        ...
    class Preset_Maker(Modifier):
        ...
    class Primitive(Value):
        ...
    class Priority(ReferenceTarget):
        START: int
        DELEGATES: MXSWrapperBase
        OBJECT: None
        GRID: None
        INCREMENT: int
        SHOWPRIORITIES: bool
        SHOWSTARTFRAMES: bool
        ...
    class Prism(GeometryClass):
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINSIDE1LENGTH: float
        TYPEINSIDE2LENGTH: float
        TYPEINSIDE3LENGTH: float
        TYPEINHEIGHT: float
        SIDE1LENGTH: float
        SIDE2LENGTH: float
        SIDE3LENGTH: float
        HEIGHT: float
        SIDE1SEGS: int
        SIDE2SEGS: int
        SIDE3SEGS: int
        HEIGHTSEGS: int
        MAPCOORDS: bool
        ...
    class ProBoolObj(GeometryClass):
        ...
    class ProBoolean(GeometryClass):
        ...
    class ProCutter(GeometryClass):
        ...
    class ProOptimizer(Modifier):
        VERTEXPERCENT: float
        VERTEXCOUNT: int
        CALCULATE: bool
        OPTIMIZATIONMODE: int
        LOCKMAT: bool
        KEEPUV: bool
        LOCKUV: bool
        TOLERANCEUV: float
        KEEPVC: bool
        LOCKVC: bool
        TOLERANCEVC: int
        KEEPNORMALS: bool
        NORMALMODE: int
        NORMALTHRESHOLD: float
        MERGEPOINTS: bool
        MERGEPOINTSTHRESHOLD: float
        MERGEFACES: bool
        MERGEFACESANGLE: float
        PRESERVESELECTION: bool
        INVERTSELECTION: bool
        SYMMETRYMODE: int
        SYMMETRYTOLERANCE: float
        COMPACTFACES: bool
        PREVENTFLIP: bool
        LOCKPOINTS: bool
        ...
    class ProSound(SoundClass):
        ...
    class Project_Mapping(ReferenceTarget):
        ...
    class Project_Mapping_Holder(Modifier):
        ...
    class Projection(Modifier):
        IGNOREBACKFACING: bool
        MATERIALID: int
        SMOOTHGROUP: int
        MAPCHANNEL: int
        CLEARSELECTION: bool
        USESOFTSELECTION: bool
        SOFTSELUSEEDGEDISTANCE: bool
        SOFTSELEDGEDIST: int
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELBUBBLE: float
        DISPLAYCAGE: bool
        DISPLAYCAGESHADED: bool
        DISPLAYCAGEOFFSET: bool
        PUSHVALUE: float
        PUSHPERCENT: float
        AUTOWRAPTOLERANCE: float
        AUTOWRAPALWAYSUPDATE: bool
        GEOMNAMES: MXSWrapperBase
        SELLEVELS: MXSWrapperBase
        MAPPROPORTIONS: MXSWrapperBase
        IDS: MXSWrapperBase
        GEOMNODES: MXSWrapperBase
        GEOMNODEIDS: MXSWrapperBase
        GEOMNODEVISIBLE: MXSWrapperBase
        DISPLAYTOGGLEENABLE: bool
        DISPLAYTOGGLEMODE: int
        PROJECTIONTYPES: MXSWrapperBase
        SELECTIONCHECKTYPE: int
        SELECTIONCHECKSELFACES: bool
        ...
    class ProjectionHolderUVW(Modifier):
        ...
    class ProjectionIntersectorMgr(Interface):
        ...
    class ProjectionMod(Modifier):
        IGNOREBACKFACING: bool
        MATERIALID: int
        SMOOTHGROUP: int
        MAPCHANNEL: int
        CLEARSELECTION: bool
        USESOFTSELECTION: bool
        SOFTSELUSEEDGEDISTANCE: bool
        SOFTSELEDGEDIST: int
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELBUBBLE: float
        DISPLAYCAGE: bool
        DISPLAYCAGESHADED: bool
        DISPLAYCAGEOFFSET: bool
        PUSHVALUE: float
        PUSHPERCENT: float
        AUTOWRAPTOLERANCE: float
        AUTOWRAPALWAYSUPDATE: bool
        GEOMNAMES: MXSWrapperBase
        SELLEVELS: MXSWrapperBase
        MAPPROPORTIONS: MXSWrapperBase
        IDS: MXSWrapperBase
        GEOMNODES: MXSWrapperBase
        GEOMNODEIDS: MXSWrapperBase
        GEOMNODEVISIBLE: MXSWrapperBase
        DISPLAYTOGGLEENABLE: bool
        DISPLAYTOGGLEMODE: int
        PROJECTIONTYPES: MXSWrapperBase
        SELECTIONCHECKTYPE: int
        SELECTIONCHECKSELFACES: bool
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
        MINIMUM: float
        MAXIMUM: float
        QUANTITY: int
        DISPLAY: int
        PHYSICALSCALE: float
        AUTOMATIC: bool
        SCALEFUNCTION: int
        UNITSYSTEMUSED: int
        ACTIVE: bool
        PROCESSBG: bool
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
        UNITS: int
        ICON_SIZE: float
        BASIC_FORCE: float
        TARGET_SPEED: float
        ON_TIME: MXSWrapperBase
        OFF_TIME: MXSWrapperBase
        FEEDBACK_ON: int
        REVERSIBLE: int
        CONTROL_GAIN: float
        ENABLE_VARIATION: int
        VARIATION_PERIOD_1: MXSWrapperBase
        AMPLITUDE_1: float
        VARIATION_PHASE_1: float
        VARIATION_PERIOD_2: MXSWrapperBase
        AMPLITUDE_2: float
        VARIATION_PHASE_2: float
        RANGE_ENABLE: int
        RANGE_VALUE: float
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
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINWIDTH: float
        TYPEINDEPTH: float
        TYPEINHEIGHT: float
        WIDTH: float
        DEPTH: float
        HEIGHT: float
        WIDTHSEGS: int
        DEPTHSEGS: int
        HEIGHTSEGS: int
        MAPCOORDS: bool
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
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1: None
        MAP2: None
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        ALPHAFROM: int
        ...
    class RGB_Tint(TextureMap):
        RED: MXSWrapperBase
        GREEN: MXSWrapperBase
        BLUE: MXSWrapperBase
        MAP1: None
        MAP1ENABLED: bool
        ...
    class RLA(BitmapIO):
        ...
    class RPF(BitmapIO):
        ...
    class RadioControl(RolloutControl):
        ...
    class Radiosity(RadiosityEffect):
        RADINITIALQUALITY: float
        RADGLOBALREFINESTEPS: int
        RADSELECTIONREFINESTEPS: int
        RADFILTERING: int
        RADPROCESSOBJECTREFINESTEPS: bool
        RADDISPLAYINVIEWPORT: bool
        RADPROCESSINRENDERONLY: bool
        RADDIRECTFILTERING: int
        MESHINGENABLED: bool
        MESHINGSIZE: float
        USEADAPTIVEMESHING: bool
        MINIMUMMESHSIZE: float
        INITIALMESHSIZE: float
        CONTRASTTHRESHOLD: float
        INCLUDEPOINTLIGHTS: bool
        INCLUDELINEARLIGHTS: bool
        INCLUDEAREALIGHTS: bool
        INCLUDESELFEMITTINGLIGHTS: bool
        SHOOTDIRECTLIGHTS: bool
        INCLUDESKYLIGHT: bool
        MINIMUMSELFEMITTINGSIZE: float
        LIGHTPAINTINGINTENSITY: float
        LIGHTPAINTINGPRESSURE: float
        LIGHTUNITSUSED: int
        RMREGATHER: bool
        RMREUSEDIRECTILLUMINATION: bool
        RMRAYSPERSAMPLE: int
        RMFILTERRADIUS: float
        RMCLAMPENABLED: bool
        RMCLAMPVALUE: float
        RMADAPTIVEENABLED: bool
        RMSAMPLESPACING: int
        RMMINSAMPLESPACING: int
        RMSUBDIVISIONCONTRAST: float
        RMSHOWSAMPLES: bool
        STATNUMFACES: int
        STATREFINEITERATIONS: int
        STATSOLUTIONQUALITY: float
        STATNUMGEOMOBJECTS: int
        STATNUMLIGHTOBJECTS: int
        STATMESHSIZE: float
        ELAPSEDTIME: int
        ...
    class RadiosityEffect(MAXWrapper):
        ...
    class RadiosityPreferences(Interface):
        ...
    class Radiosity_Override(Material):
        REFLECTANCESCALE: float
        COLORBLEED: float
        TRANSMITTANCESCALE: float
        LUMINANCESCALE: float
        BUMPSCALE: float
        BASEMATERIAL: MXSWrapperBase
        ...
    class RagdollHelper(Helper):
        ...
    class RagdollVisualizer(Helper):
        ...
    class Railing(GeometryClass):
        TOP_RAIL_DEPTH: float
        TOP_RAIL_WIDTH: float
        TOP_SURFACE_OF_TOP_RAIL_HEIGHT: float
        RAILING_LENGTH: float
        TOP_RAIL_PROFILE: int
        LOWER_RAIL_DEPTH: float
        LOWER_RAIL_WIDTH: float
        LOWEST_RAIL_HEIGHT: float
        LOWER_RAIL_SPACING: float
        NUMBER_OF_LOWER_RAILS: int
        TOP_RAIL_SPACING_TO_NEXT_RAIL: float
        LOWER_RAIL_PROFILE: int
        POST_DEPTH: float
        POST_WIDTH: float
        FIRST_POST_OFFSET: float
        POST_SPACING: float
        NUMBER_OF_POSTS: int
        POSTS_ORIENTED_WITH_CURVED_RAILING: bool
        LAST_POST_OFFSET: float
        POST_EXTENSION_BEYOND_BOTTOM_OF_TOP_RAIL: float
        POST_PROFILE: int
        FENCING_TYPE: int
        PICKET_DEPTH: float
        PICKET_WIDTH: float
        FIRST_PICKET_OFFSET: float
        PICKET_SPACING: float
        NUMBER_OF_PICKETS_BETWEEN_EACH_PAIR_OF_POSTS: int
        PICKETS_ORIENTED_WITH_CURVED_RAILING: bool
        LAST_PICKET_SPACING_TO_POST: float
        PICKET_PROFILE: int
        PICKET_EXTENSION_BEYOND_BOTTOM_OF_TOP_RAIL: float
        PICKET_BOTTOM_OFFSET: float
        FILL_THICKNESS: float
        FILL_TOP_OFFSET: float
        FILL_BOTTOM_OFFSET: float
        FILL_LEFT_OFFSET: float
        FILL_RIGHT_OFFSET: float
        TEXTURE_MAPPED: bool
        NUMBER_OF_SEGMENTS_BETWEEN_EACH_PAIR_OF_POSTS: int
        RESPECT_PATH_CORNERS_IN_RAILS: bool
        ...
    class RandomWalk(Helper):
        ...
    class Randomize_Keys(TrackViewUtility):
        ...
    class RapidRT_Noise_Filter(RenderElement):
        ELEMENTNAME: str
        ENABLED: bool
        BITMAP: bool
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
        ELEMENTNAME: str
        SIZE: float
        INTENSITY: float
        ANGLE: float
        NUMBER: int
        SHARPNESS: float
        ON: bool
        OBJECTSHIDE: bool
        SQUEEZE: bool
        OCCLUSION: float
        COLORSOURCE: float
        CENTERCOLOR: MXSWrapperBase
        EDGECOLOR: MXSWrapperBase
        RADIALMTL: None
        USERADIALMTL: bool
        RADIALMAP: None
        USERADIALMAP: bool
        CIRCULARCOLORMIX: float
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        QUADRANT4COLOR: MXSWrapperBase
        CIRCULARMTL: None
        USECIRCULARMTL: bool
        CIRCULARMAP: None
        USECIRCULARMAP: bool
        RADIALSIZEMAP: None
        USERADIALSIZEMAP: bool
        APPLYLIGHTS: bool
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        SOURCEOBJECTID: bool
        OBJECTID: int
        SOURCEEFFECTSID: bool
        EFFECTSID: int
        SOURCEUNCLAMPEDCOLOR: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        SOURCESURFACENORMAL: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        SOURCEWHOLE: bool
        SOURCEALPHA: bool
        ALPHA: int
        SOURCEZBUFFER: bool
        ZHI: float
        ZLO: float
        FILTERALL: bool
        FILTEREDGE: bool
        FILTERPERIMETERALPHA: bool
        FILTERPERIMETER: bool
        FILTERBRIGHTNESS: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        FILTERHUE: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        APPLYNOISE: bool
        NOISEMAP: None
        RADIALDENSITY: None
        USERADIALDENSITY: bool
        ...
    class Ray_Engine(ReferenceTarget):
        ...
    class Raytrace(TextureMap):
        ...
    class RaytraceGlobalSettings(ReferenceTarget):
        EXCLUDELIST: MXSWrapperBase
        INCLUDELIST: None
        SHOWMESSAGES: bool
        SHOWPROGRESSDLG: bool
        MAX_RAY_DEPTH: int
        MAX_LEVELS_COLOR_MODE: int
        MAX_LEVELS_SPECIFY_COLOR: MXSWrapperBase
        ADAPTIVE_ANTIALIASING_ENABLE_FLAG: bool
        ADAPTIVE_ANTIALIASING_THRESHOLD: float
        ANTIALIASING_MINIMUM_RAYS_TO_FIRE: int
        ANTIALIASING_MAXIMUM_RAYS_TO_FIRE: int
        BLURRING_AMOUNT: float
        BLURRING_ASPECT_RATIO: float
        DEFOCUSING_AMOUNT: float
        DEFOCUSING_ASPECT_RATIO: float
        VOX_MAXDEPTH: int
        VOX_PREVIS: float
        VOX_DIM: int
        VOX_FACE_LIMIT: int
        ENABLE_RAYTRACING: bool
        ENABLE_ANTIALIASING: bool
        ENABLE_SELF_REFLECT_REFRACT: bool
        ENABLE_ATMOSPHERE: bool
        ENABLE_OBJECTS_IN_RAYTRACE_OBJECTS: bool
        ENABLE_ATMOSPHERE_IN_RAYTRACE_OBJECTS: bool
        ENABLE_REFRACT_SPECIAL_EFFECTS: bool
        ENABLE_MATERIAL_ID_RENDERING_SUPPORT: bool
        ADAPTIVE_RAY_DEPTH_THRESHOLD: float
        ...
    class RaytraceMaterial(Material):
        EFFECTSCHANNEL: int
        AMBIENTMAP: None
        DIFFUSEMAP: None
        SPECULARMAP: None
        BUMPMAP: None
        REFLECTIONMAP: None
        DISPLACEMENTMAP: None
        AMBIENTMAPAMOUNT: float
        DIFFUSEMAPAMOUNT: float
        SPECULARMAPAMOUNT: float
        BUMPMAPAMOUNT: float
        REFLECTIONMAPAMOUNT: float
        DISPLACEMENTMAPAMOUNT: float
        AMBIENTMAPENABLE: bool
        DIFFUSEMAPENABLE: bool
        SPECULARMAPENABLE: bool
        BUMPMAPENABLE: bool
        REFLECTIONMAPENABLE: bool
        DISPLACEMENTMAPENABLE: bool
        GLOSSINESSMAP: None
        GLOSSINESSMAPENABLE: bool
        GLOSSINESSMAPAMOUNT: float
        SPECULARLEVELMAP: None
        SPECULARLEVELMAPENABLE: bool
        SPECULARLEVELMAPAMOUNT: float
        LUMINOSITYMAP: None
        LUMINOSITYMAPENABLE: bool
        LUMINOSITYMAPAMOUNT: float
        TRANSPARENCYMAP: None
        TRANSPARENCYMAPENABLE: bool
        TRANSPARENCYMAPAMOUNT: float
        ENVIRONMENTMAP: None
        ENVIRONMENTMAPENABLE: bool
        ENVIRONMENTMAPAMOUNT: float
        TRANSENVMAP: None
        TRANSENVMAPENABLE: bool
        TRANSENVMAPAMOUNT: float
        IORMAP: None
        IORMAPENABLE: bool
        IORMAPAMOUNT: float
        TRANSLUCENCYMAP: None
        TRANSLUCENCYMAPENABLE: bool
        TRANSLUCENCYMAPAMOUNT: float
        EXTRALIGHTINGMAP: None
        EXTRALIGHTINGMAPENABLE: bool
        EXTRALIGHTINGMAPAMOUNT: float
        FLUORESCENCEMAP: None
        FLUORESCENCEMAPENABLE: bool
        FLUORESCENCEMAPAMOUNT: float
        COLORDENSITYMAP: None
        COLORDENSITYMAPENABLE: bool
        COLORDENSITYMAPAMOUNT: float
        FOGCOLORMAP: None
        FOGCOLORMAPENABLE: bool
        FOGCOLORMAPAMOUNT: float
        DIFFUSIONMAP: None
        DIFFUSIONMAPENABLE: bool
        DIFFUSIONMAPAMOUNT: float
        SOFTEN: float
        DIFFUSE: MXSWrapperBase
        SHADERTYPE: int
        SHADERBYNAME: str
        WIRE: bool
        TWOSIDED: bool
        FACEMAP: bool
        SUPERSAMPLE: bool
        WIREUNITS: int
        ANISOTROPY: float
        ORIENTATION: float
        GLOSSINESS: float
        TRANSLUCENCY: MXSWrapperBase
        FOG_COLOR: MXSWrapperBase
        AMBIENT: MXSWrapperBase
        AMBIENT_AMOUNT: float
        AMBIENT_COLOR_ON: bool
        REFLECT: MXSWrapperBase
        REFLECT_AMOUNT: float
        REFLECT_COLOR_ON: int
        LUMINOSITY: MXSWrapperBase
        SELF_ILLUM_AMOUNT: float
        LUMINOSITY_COLOR_ON: bool
        TRANSPARECY: MXSWrapperBase
        TRANSPARENCY_AMOUNT: float
        TRANSPARENCY_COLOR_ON: bool
        INDEX_OF_REFRACTION: float
        SPEC__COLOR: MXSWrapperBase
        SPECULAR_LEVEL: float
        EXTRA_LIGHTING: MXSWrapperBase
        FLUORESCENCE: MXSWrapperBase
        FLUORESCENCE_BIAS: float
        WIRE_SIZE: float
        COLOR_DENSITY_COLOR: MXSWrapperBase
        COLOR_DENSITY_ENABLE: bool
        COLOR_DENSITY_START: float
        COLOR_DENSITY_END: float
        COLOR_DENSITY_AMOUNT: float
        FOG_ENABLE: bool
        FOG_START: float
        FOG_END: float
        FOG_AMOUNT: float
        REFLECTION_TYPE: int
        REFLECTION_GAIN: float
        ENABLE_RAYTRACED_REFLECTIONS: bool
        ENABLE_RAYTRACED_REFRACTIONS: bool
        REFLECTION_FALLOFF_MODE: int
        REFLECTION_FALLOFF_END_DISTANCE: float
        REFRACTION_FALLOFF_MODE: int
        REFRACTION_FALLOFF_END_DISTANCE: float
        ENABLE_REFLECTION_FALLOFF: bool
        REFLECTION_FALLOFF_DISTANCE: float
        ENABLE_REFRACTION_FALLOFF: bool
        REFRACTION_FALLOFF_DISTANCE: float
        BUMP_MAP_EFFECT: float
        OVERRIDE_GLOBAL_ANTIALIASING_SETTINGS: bool
        ADAPTIVE_ANTIALIASING_ON: bool
        LOCAL_MIN__RAYS: int
        LOCAL_MAX__RAYS: int
        LOCAL_THRESHOLD: float
        LOCAL_BLUR_OFFSET: float
        LOCAL_BLUR_ASPECT: float
        LOCAL_DEFOCUS: float
        LOCAL_DEFOCUS_ASPECT: float
        BLUR_MAP: bool
        DEFOCUS_MAP: bool
        OPTIONS___RAYTRACER_ENABLE: bool
        OPTIONS___ANTIALIASING_ENABLE: bool
        OPTIONS___SELF_REFLECT_REFRACT: bool
        OPTIONS___RAYTRACE_ATMOSPHERICS: bool
        OPTIONS___REFLECT_REFRACT_MATERIAL_ID_S: bool
        OPTIONS___RAYTRACE_OBJECTS_IN_GLASS: bool
        OPTIONS___RAYTRACE_ATMOSPHERICS_IN_GLASS: bool
        OPTIONS___COLOR_DENSITY___FOG_ENABLE: bool
        ATTENUATION_START: float
        ATTENUATION_EXPONENT: float
        ATTENUATION_NEAR: float
        ATTENUATION_CONTROL_1: float
        ATTENUATION_CONTROL_2: float
        ATTENUATION_FAR: float
        ATTENUATION_COLOR_MODE: int
        ATTENUATION_COLOR: MXSWrapperBase
        BOUNCE_COEFFICIENT: float
        SLIDING_FRICTION: float
        STATIC_FRICTION: float
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
        LENGTH: float
        STEPS: int
        WIDTH: float
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        CORNERRADIUS: float
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
        SIZE: int
        BLUR: float
        BLUROFFSET: float
        NEAR: float
        FAR: float
        SOURCE: int
        USEATMOSPHERICMAP: bool
        APPLY: bool
        FRAMETYPE: int
        NTHFRAME: int
        BITMAPNAME: MXSWrapperBase
        OUTPUTNAME: None
        ...
    class Reflection(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ...
    class ReflectionFragment(GraphicsFragmentPlugin):
        ...
    class Refraction(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ...
    class Relax(Modifier):
        ITERATIONS: int
        RELAX_VALUE: float
        KEEP_BOUNDARY_PTS_FIXED: int
        ...
    class RemoveDictValue(Primitive):
        ...
    class RemoveSubRollout(Primitive):
        ...
    class RemoveTempPrompt(Primitive):
        ...
    class RendSpline(Modifier):
        THICKNESS: float
        VIEWPORT_THICKNESS: float
        SIDES: int
        VIEWPORT_SIDES: int
        ANGLE: float
        VIEWPORT_ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        DISPLAYRENDERSETTINGS: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORTORRENDER: int
        SYMMETRICALORRECTANGULAR: int
        WIDTH: float
        LENGTH: float
        ANGLE2: float
        LOCKASPECT: bool
        VIEWPORT_SYMMETRICALORRECTANGULAR: int
        VIEWPORT_WIDTH: float
        VIEWPORT_LENGTH: float
        VIEWPORT_ANGLE2: float
        VIEWPORT_LOCKASPECT: bool
        AUTOSMOOTH: bool
        THRESHOLD: float
        TWIST_CORRECTION: bool
        CAP: bool
        QUAD_CAP: bool
        CAP_SEGMENTS: int
        SPHERE_CAP: float
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
        TYPE: int
        VISIBLE: float
        SPLIT_TYPE: int
        MESH_COUNT: int
        PARTICLES_PER_MESH: int
        ...
    class Renderable_Spline(Modifier):
        THICKNESS: float
        VIEWPORT_THICKNESS: float
        SIDES: int
        VIEWPORT_SIDES: int
        ANGLE: float
        VIEWPORT_ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        DISPLAYRENDERSETTINGS: bool
        USEVIEWPORTSETTINGS: bool
        VIEWPORTORRENDER: int
        SYMMETRICALORRECTANGULAR: int
        WIDTH: float
        LENGTH: float
        ANGLE2: float
        LOCKASPECT: bool
        VIEWPORT_SYMMETRICALORRECTANGULAR: int
        VIEWPORT_WIDTH: float
        VIEWPORT_LENGTH: float
        VIEWPORT_ANGLE2: float
        VIEWPORT_LOCKASPECT: bool
        AUTOSMOOTH: bool
        THRESHOLD: float
        TWIST_CORRECTION: bool
        CAP: bool
        QUAD_CAP: bool
        CAP_SEGMENTS: int
        SPHERE_CAP: float
        ...
    class RendererClass(MAXWrapper):
        ...
    class RepelBehavior(ReferenceTarget):
        NAME: str
        REPULSIONSOURCES: MXSWrapperBase
        TARGETCOMP: int
        REPELMETHOD: int
        USERADII: bool
        INNERRADIUS: float
        OUTERRADIUS: float
        FALLOFF: float
        SHOWRADII: bool
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
        ...
    class Repel_Behavior(ReferenceTarget):
        NAME: str
        REPULSIONSOURCES: MXSWrapperBase
        TARGETCOMP: int
        REPELMETHOD: int
        USERADII: bool
        INNERRADIUS: float
        OUTERRADIUS: float
        FALLOFF: float
        SHOWRADII: bool
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
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
        TIME_ON: int
        TIME_GROWING: int
        DISPLAY_UNTIL: int
        REPEATS: int
        MAX_DIAMETER: float
        RING_WIDTH: float
        RING_SEGMENTS: int
        OUTER_EDGE_BREAKUP: bool
        MAJOR_CYCLES_OUTER: int
        MAJOR_CYCLE_FLUX_OUTER: float
        MAJOR_CYCLE_FLUX_PER_OUTER: int
        MINOR_CYCLES_OUTER: int
        MINOR_CYCLE_FLUX_OUTER: float
        MINOR_CYCLE_FLUX_PER_OUTER: int
        INNER_EDGE_BREAKUP: bool
        MAJOR_CYCLES_INNER: int
        MAJOR_CYCLE_FLUX_INNER: float
        MAJOR_CYCLE_FLUX_PER_INNER: int
        MINOR_CYCLES_INNER: int
        MINOR_CYCLE_FLUX_INNER: float
        MINOR_CYCLE_FLUX_PER_INNER: int
        HEIGHT: float
        HEIGHT_SEGS: int
        RADIUS_SEGS: int
        MAPPING_COORDS: bool
        SMOOTHING: bool
        ...
    class Ring_Array(System):
        ...
    class Ring_Element(ReferenceTarget):
        ELEMENTNAME: str
        SIZE: float
        INTENSITY: float
        PLANE: float
        THICKNESS: float
        ON: bool
        OBJECTSHIDE: bool
        SQUEEZE: bool
        OCCLUSION: float
        COLORSOURCE: float
        CENTERCOLOR: MXSWrapperBase
        EDGECOLOR: MXSWrapperBase
        RADIALMTL: None
        USERADIALMTL: bool
        RADIALMAP: None
        USERADIALMAP: bool
        CIRCULARCOLORMIX: float
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        QUADRANT4COLOR: MXSWrapperBase
        CIRCULARMTL: None
        USECIRCULARMTL: bool
        CIRCULARMAP: None
        USECIRCULARMAP: bool
        RADIALSIZEMAP: None
        USERADIALSIZEMAP: bool
        APPLYLIGHTS: bool
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        SOURCEOBJECTID: bool
        OBJECTID: int
        SOURCEEFFECTSID: bool
        EFFECTSID: int
        SOURCEUNCLAMPEDCOLOR: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        SOURCESURFACENORMAL: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        SOURCEWHOLE: bool
        SOURCEALPHA: bool
        ALPHA: int
        SOURCEZBUFFER: bool
        ZHI: float
        ZLO: float
        FILTERALL: bool
        FILTEREDGE: bool
        FILTERPERIMETERALPHA: bool
        FILTERPERIMETER: bool
        FILTERBRIGHTNESS: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        FILTERHUE: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        APPLYNOISE: bool
        NOISEMAP: None
        RADIALDENSITY: None
        USERADIALDENSITY: bool
        ...
    class Ripple(Modifier):
        AMPLITUDE1: float
        AMPLITUDE2: float
        WAVELENGTH: float
        PHASE: float
        DECAY: float
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
        WEIGHT: MXSWrapperBase
        AVERAGE: bool
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
        RADIUS: float
        INHERITVELOCITY: float
        FRICTION: float
        ...
    class SLAP(RenderEffect):
        ...
    class SME(Interface):
        ...
    class SMEGUP(GlobalUtilityPlugin):
        ...
    class SOmniFlect(SpacewarpObject):
        TIMEON: MXSWrapperBase
        TIMEOFF: MXSWrapperBase
        AFFECTS: float
        BOUNCE: float
        BOUNCEVAR: float
        CHAOS: float
        INHERITVELOCITY: float
        REFRACTS: float
        DECELERATION: float
        DECELVAR: float
        REFRACTION: float
        REFRACTIONVAR: float
        DIFFUSION: float
        DIFFUSIONVAR: float
        RADIUS: float
        SPAWN: float
        PASSVELOCITY: float
        PASSVELOCITYVAR: float
        FRICTION: float
        ...
    class SOmniFlectMod(SpacewarpModifier):
        ...
    class STL_Check(Modifier):
        MATERIAL_ID: int
        SELECT_FACES: int
        CHECK_NOW: int
        CHANGE_MATID: int
        SELECTION_TYPE: int
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
        OUTPUT_TYPE: int
        ANGLE_VALUE: float
        ANGLE_VARIATION: float
        BOOLEAN_VALUE: int
        FLOAT_VALUE: float
        FLOAT_VARIATION: float
        INTEGER_VALUE: int
        INTEGER_VARIATION: int
        PERCENT_VALUE: float
        PERCENT_VARIATION: float
        TIME_VALUE: int
        TIME_VARIATION: int
        WORLD_VALUE: float
        WORLD_VARIATION: float
        USE_AS_SPEED_OR_SPIN_RATE: bool
        USE_FOR_TIME_RELATED_ADDITION: bool
        USE_FOR_TIME_RELATED_MULTIPLICATION: bool
        UNITS_PER_TYPE: int
        SYNC_TYPE: int
        RANDOM_SEED: int
        USE_E1: bool
        USE_E2: bool
        USE_E3: bool
        USE_E4: bool
        USE_AS_ACCELERATION: bool
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        ...
    class ScaleLayer(ScaleController):
        ...
    class ScaleList(ScaleController):
        WEIGHT: MXSWrapperBase
        AVERAGE: bool
        ...
    class ScaleMatrix(Primitive):
        ...
    class ScaleParticles(Helper):
        TYPE: int
        X_SCALE_FACTOR: float
        Y_SCALE_FACTOR: float
        Z_SCALE_FACTOR: float
        CONSTRAIN_SCALE: bool
        X_SCALE_VARIATION: float
        Y_SCALE_VARIATION: float
        Z_SCALE_VARIATION: float
        CONSTRAIN_SCALE_VARIATION: bool
        BIAS: int
        SYNC_TYPE: int
        RANDOM_SEED: int
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
        TEST_TYPE: int
        AXIS_TYPE: int
        CONDITION_TYPE: int
        SIZE_VALUE: float
        SIZE_VARIATION: float
        SCALE_VALUE: float
        SCALE_VARIATION: float
        SYNC_TYPE: int
        RANDOM_SEED: int
        ...
    class Scale_Wire(ScaleController):
        ...
    class Scatter(GeometryClass):
        ...
    class ScatterReferenceTarget(ReferenceTarget):
        CLONEOBJECT: None
        NUMCLONES: int
        CLONETYPE: int
        CLONEHIERARCHY: bool
        CLONECONTROLLERS: bool
        POSITIONSPACE: int
        SURFACEOFFSET: float
        POSITIONOBJECT: None
        CENTERX: float
        CENTERY: float
        CENTERZ: float
        RADIUS: float
        XYPLANE: bool
        CHILDBBOX: bool
        SPACING: float
        POSITIONSEED: int
        INCPOSITIONSEED: bool
        FORWARDAXIS: int
        UPAXIS: int
        FORWARDAXISSIGN: bool
        UPAXISSIGN: bool
        LOOKFROM: int
        LOOKFROMOBJECT: None
        LOOKTOWARDS: int
        LOOKATTARGET: None
        SIDEDEVIATION: float
        UPDOWNDEVIATION: float
        ROTATIONSEED: int
        INCROTATIONSEED: bool
        XSCALE: float
        XSCALEDEVIATION: float
        MATCHXTOYSCALE: bool
        MATCHXTOZSCALE: bool
        YSCALE: float
        YSCALEDEVIATION: float
        MATCHYTOXSCALE: bool
        MATCHYTOZSCALE: bool
        ZSCALE: float
        ZSCALEDEVIATION: float
        MATCHZTOXSCALE: bool
        MATCHZTOYSCALE: bool
        SCALESEED: int
        INCSCALESEED: bool
        COMPUTECLONES: bool
        COMPUTEPOSITIONS: bool
        COMPUTEROTATIONS: bool
        COMPUTESCALES: bool
        INCPOSSEED: bool
        INCROTSEED: bool
        INCSCLSEED: bool
        OBJECTSTOSCATTER: MXSWrapperBase
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
        RANDOM_SEED: int
        PROCEED_SCRIPT: str
        ...
    class Script_Test(Helper):
        RANDOM_SEED: int
        PROCEED_SCRIPT: str
        ...
    class ScriptedBehavior(ReferenceTarget):
        NAME: str
        SCRIPTCONTEXTNAME: str
        SCRIPT: None
        TYPE: int
        ...
    class Scripted_Behavior(ReferenceTarget):
        NAME: str
        SCRIPTCONTEXTNAME: str
        SCRIPT: None
        TYPE: int
        ...
    class Seat(GeometryClass):
        GENDER: int
        MOTIONSEED: int
        ID: int
        SINGLE: bool
        HEIGHT: float
        ...
    class SecurityTools(Interface):
        ...
    class SecurityToolsUtility(GlobalUtilityPlugin):
        ...
    class SeekBehavior(ReferenceTarget):
        NAME: str
        TARGETS: MXSWrapperBase
        TARGETCOMP: int
        SEEKMETHOD: int
        USERADII: bool
        INNERRADIUS: float
        OUTERRADIUS: float
        FALLOFF: float
        SHOWRADII: bool
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
        ...
    class Seek_Behavior(ReferenceTarget):
        NAME: str
        TARGETS: MXSWrapperBase
        TARGETCOMP: int
        SEEKMETHOD: int
        USERADII: bool
        INNERRADIUS: float
        OUTERRADIUS: float
        FALLOFF: float
        SHOWRADII: bool
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
        ...
    class SegTrans(Matrix3Controller):
        ...
    class SelectByChannel(Modifier):
        SELECTIONTYPE: int
        MAPID: int
        MAPSUBID: int
        ...
    class SelectSaveBitMap(Primitive):
        ...
    class Select_By_Channel(Modifier):
        SELECTIONTYPE: int
        MAPID: int
        MAPSUBID: int
        ...
    class Select_Keys_By_Time(TrackViewUtility):
        ...
    class Select_Object(ReferenceTarget):
        TYPE: int
        SINGLE_OR_MULTIPLE: int
        OBJECT: None
        OBJECTS: MXSWrapperBase
        INDEPENDENT_PFLOW_SYSTEM: bool
        FILTER: None
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
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
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
        AVERAGESPEED1: float
        MAXACCEL1: float
        TURNDECEL1: float
        TURNDECELANGLE1: float
        INCLINEDECEL1: float
        INCLINEDECELANGLE1: float
        DECLINEDECEL1: float
        DECLINEDECELANGLE1: float
        MAXTURN1: float
        MAXTURNACCEL1: float
        MAXINCLINE1: float
        MAXDECLINE1: float
        MAXBANK1: float
        MAXBANKACCEL1: float
        BANKFACTOR1: float
        STARTFRAME1: int
        PRIORITY1: int
        AVERAGESPEED2: float
        MAXACCEL2: float
        TURNDECEL2: float
        TURNDECELANGLE2: float
        INCLINEDECEL2: float
        INCLINEDECELANGLE2: float
        DECLINEDECEL2: float
        DECLINEDECELANGLE2: float
        MAXTURN2: float
        MAXTURNACCEL2: float
        MAXINCLINE2: float
        MAXDECLINE2: float
        MAXBANK2: float
        MAXBANKACCEL2: float
        BANKFACTOR2: float
        STARTFRAME2: int
        PRIORITY2: int
        ACTIVE: bool
        SHOWFORCES: bool
        SHOWVELOCITY: bool
        SHOWCOGSTATES: bool
        XYCONSTRAIN: bool
        VELOCITYCOLOR: MXSWrapperBase
        USEHIERBBOX: bool
        USEBIPED: bool
        STARTCLIP: int
        RAND1: bool
        RAND2: bool
        RAND3: bool
        RAND4: bool
        RAND5: bool
        RAND6: bool
        RAND7: bool
        RAND8: bool
        RAND9: bool
        RAND10: bool
        RAND11: bool
        RAND12: bool
        RAND16: bool
        RAND17: bool
        RAND18: bool
        RAND13: bool
        RAND14: bool
        RAND15: bool
        SET1: bool
        SET2: bool
        SET3: bool
        SET4: bool
        SET5: bool
        SET6: bool
        SET7: bool
        SET8: bool
        SET9: bool
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
        SET20: bool
        SET21: bool
        SET22: bool
        SET23: bool
        SET24: bool
        SET25: bool
        SET26: bool
        DELEGATES: MXSWrapperBase
        NAME: None
        ...
    class Shader(MAXWrapper):
        ...
    class Shadow(MAXWrapper):
        ...
    class ShadowClass(Value):
        ...
    class ShadowRenderElement(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ...
    class ShadowsMap(BakeElement):
        ENABLED: bool
        FILTERON: bool
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        ELEMENTNAME: str
        BITMAP: None
        BACKGROUNDCOLOR: MXSWrapperBase
        TARGETMAPSLOTNAME: str
        ...
    class ShapeBooleanObject(Shape):
        ...
    class ShapeControl(ReferenceTarget):
        PARTICLE_GEOMETRY_OBJECT: None
        PROCEED_TYPE: int
        HISTORY_DEPENDENT: bool
        EXECUTION_ORDER: int
        PRIORITY_ORDER: int
        ANIMATED_SHAPE: bool
        ACQUIRE_MAPPING: bool
        DISCRETE_OPTIMIZATION: bool
        FILTER: None
        INPUT_TIME: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        INPUT_7: None
        INPUT_8: None
        ...
    class ShapeFilterFn(MAXScriptFunction):
        ...
    class ShapeLibrary(Helper):
        DIMENSION_TYPE: int
        TYPE_2D: int
        TYPE_3D: int
        SIZE: float
        USE_SCALE: bool
        SCALE_VALUE: float
        SCALE_VARIATION: float
        RANDOM_MULTI_SHAPE_ORDER: bool
        RANDOM_SEED: int
        GENERATE_MAPPING_COORDS: bool
        FIT_MAPPING: bool
        ...
    class ShapeMap(TextureMap):
        FILTER: bool
        MIPMAP: bool
        MONOOUTPUT: int
        RGBOUTPUT: int
        APPLYCROP: bool
        CROPORPLACE: int
        CROP_U: float
        CROP_V: float
        CROP_W: float
        CROP_H: float
        JITTER: bool
        JITTERAMT: float
        ALPHASOURCE: int
        COORDS: MXSWrapperBase
        OUTPUT: MXSWrapperBase
        RESTYPE: int
        FINITERESOLUTION: int
        SHAPEOBJECT: None
        OUTLINECOLOR: MXSWrapperBase
        FILLCOLOR: MXSWrapperBase
        BGCOLOR: MXSWrapperBase
        FILLBG: bool
        RENDEROPEN: bool
        ENDTYPE: int
        FILLEDCLOSED: bool
        OUTLINEDCLOSED: bool
        OUTLINEWIDTH: float
        BOUNDSTYPE: int
        MANUALWIDTH: float
        MANUALHEIGHT: float
        STRICTHIERARCHY: bool
        BOUNDSOBJECT: None
        RENDERCHILDREN: bool
        RENDERROOT: bool
        MERGESHAPES: bool
        USEFILLCOLOR: bool
        HWBITMAPSIZE: int
        ...
    class ShapeMerge(GeometryClass):
        OPERATION_TYPE: int
        REMOVE_INTERIOR_EXTERIOR: int
        OUTPUT_SUB_MESH_SELECTION: int
        ...
    class ShapeStandard(Helper):
        SHAPE: int
        SIZE: float
        USE_SCALE: bool
        SCALE_VALUE: float
        ...
    class Shape_Check(UtilityPlugin):
        ...
    class Shape_Facing(Helper):
        LOOK_AT_OBJECT: None
        PARALLEL: bool
        SIZE_SPACE: int
        UNITS: float
        INHERITED_SCALE: float
        PROPORTION: float
        VARIATION: float
        PIVOT_AT: int
        WH_RATIO: float
        RANDOM_SEED: int
        ORIENTATION: int
        ...
    class Shape_Instance(Helper):
        SHAPE_OBJECT: None
        GROUP_MEMBERS: bool
        OBJECT_AND_CHILDREN: bool
        OBJECT_ELEMENTS: bool
        SCALE_VALUE: float
        VARIATION: float
        ACQUIRE_MAPPING: bool
        ACQUIRE_MATERIAL: bool
        SUBMTL_ID_OFFSET: int
        RANDOM_SHAPE: bool
        ANIMATED_SHAPE: bool
        ACQUIRE_SHAPE: bool
        FAST_SHAPE_EVALUATION: bool
        SYNC_TYPE: int
        ADD_RANDOM_OFFSET: bool
        RANDOM_OFFSET: int
        RANDOM_SEED: int
        SET_SCALE: bool
        REPORT_NODE_HANDLES: int
        HANDLES_TO_REPORT: MXSWrapperBase
        ...
    class Shape_Mark(Helper):
        CONTACT_OBJECT: None
        SURFACE_ANIMATION: bool
        ALIGN_TO: int
        DIVERGENCE: float
        SIZE_SPACE: int
        WIDTH: float
        LENGTH: float
        INHERITED_SCALE: float
        VARIATION: float
        ANGLE_DISTORTION: bool
        MAX_DISTORTION: float
        MARK_TYPE: int
        HEIGHT: float
        MULTI_ELEMENTS: bool
        PIVOT_OFFSET: float
        SURFACE_OFFSET: float
        SURFACE_OFFSET_VARIATION: float
        VERTEX_NOISE: float
        CONTINUOUS_UPDATE: bool
        GENERATE_MAPPING_COORDS: bool
        RANDOM_SEED: int
        ...
    class SharedMoflow(ReferenceTarget):
        NAME: str
        FIGFILELOADED: bool
        BIPEDS: MXSWrapperBase
        ...
    class SharedMoflowList(ReferenceTarget):
        SHAREDMOFLOWS: MXSWrapperBase
        EDITEDSHAREDMOFLOW: None
        ...
    class SharedMotionFlow(ReferenceTarget):
        NAME: str
        FIGFILELOADED: bool
        BIPEDS: MXSWrapperBase
        ...
    class SharedMotionFlows(ReferenceTarget):
        SHAREDMOFLOWS: MXSWrapperBase
        EDITEDSHAREDMOFLOW: None
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
        INNERAMOUNT: float
        OUTERAMOUNT: float
        OVERRIDEMATID: bool
        MATID: int
        OVERRIDESMOOTHINGGROUP: bool
        SMOOTHGROUP: int
        EDGEMAPPING: int
        TVOFFSET: float
        OVERRIDEINNERMATID: bool
        MATINNERID: int
        SELECTEDGEFACES: bool
        SELECTINNERFACES: bool
        SEGMENTS: int
        STRAIGHTENCORNERS: bool
        AUTOSMOOTH: bool
        AUTOSMOOTHANGLE: float
        SELECTOUTERFACES: bool
        OVERRIDEOUTERMATID: bool
        MATOUTERID: int
        BEVEL: bool
        BEVELSHAPE: None
        ...
    class ShellLaunch(Primitive):
        ...
    class Shell_Material(Material):
        ORIGINALMATERIAL: MXSWrapperBase
        BAKEDMATERIAL: MXSWrapperBase
        VIEWPORTMTLINDEX: int
        RENDERMTLINDEX: int
        ...
    class Shellac(Material):
        SHELLACMTL1: MXSWrapperBase
        SHELLACMTL2: MXSWrapperBase
        SHELLACCOLORBLEND: float
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
        AXIS: int
        DIRECTION: float
        LIMIT: bool
        UPPERLIMIT: float
        LOWERLIMIT: float
        AMOUNT: float
        ...
    class Skin(Modifier):
        EFFECT: float
        FILTER_VERTICES: bool
        FILTER_ENVELOPES: bool
        FILTER_CROSS_SECTIONS: bool
        DRAW_ALL_ENVELOPES: bool
        DRAW_VERTICES: bool
        REF_FRAME: int
        PAINT_RADIUS: float
        PAINT_FEATHER: float
        CROSS_RADIUS: float
        ALWAYS_DEFORM: bool
        PAINT_STR: float
        LOCALSQUASH: MXSWrapperBase
        INITIALSQUASH: MXSWrapperBase
        INITIALSTATICENVELOPE: bool
        INITIALINNERENVELOPEPERCENT: float
        INITIALOUTERENVELOPEPERCENT: float
        INITIALENVELOPEINNER: float
        INITIALENVELOPEOUTER: float
        PAINTBLENDMODE: bool
        BACKFACECULL: bool
        WEIGHTTOOL_TOLERANCE: float
        WEIGHTTOOL_SCALE: float
        WEIGHTTOOL_WEIGHT: float
        SELECTELEMENT: bool
        MIRRORPLANE: int
        MIRROROFFSET: float
        MIRRORUSEINITIALTM: bool
        MIRRORENABLED: bool
        MIRRORTHRESHOLD: float
        MIRRORPROJECTION: int
        MANUALUPDATE: bool
        MIRRORFAST: bool
        DRAW_ALL_ENVELOPES: bool
        DRAW_VERTICES: bool
        DRAW_ALL_GIZMOS: bool
        DRAW_ALL_VERTICES: bool
        SHADEWEIGHTS: bool
        ENVELOPESALWAYSONTOP: bool
        CROSSSECTIONSALWAYSONTOP: bool
        SHOWNOENVELOPES: bool
        COLORALLWEIGHTS: bool
        WEIGHTCOLORS: MXSWrapperBase
        SHOWHIDDENVERTICES: bool
        REF_FRAME: int
        RIGID_VERTICES: bool
        RIGID_HANDLES: bool
        FAST_UPDATE: bool
        NO_UPDATE: bool
        UPDATEONMOUSEUP: bool
        BONE_LIMIT: int
        BACKTRANSFORM: bool
        SHORTENBONENAMES: bool
        FASTSUBANIMS: bool
        FASTTMCACHE: bool
        FASTVERTEXWEIGHTING: bool
        FASTGIZMOS: bool
        IGNOREBONESCALE: bool
        ANIMATABLEENVELOPES: bool
        WEIGHTALLVERTICES: bool
        CLEARZEROLIMIT: float
        ENABLEDQ: bool
        WT_AFFECTSELECTED: bool
        WT_SHOWAFFECTEDBONES: bool
        WT_UPDATEONMOUSEUP: bool
        WT_FLIPUI: bool
        WT_SHOWATTRIBUTES: bool
        WT_SHOWGLOBAL: bool
        WT_SHORTENLABELS: bool
        WT_SHOWEXCLUSIONS: bool
        WT_SHOWLOCKS: bool
        WT_SHOWOPTIONSUI: bool
        WT_SHOWSETUI: bool
        WT_SHOWCOPYPASTEUI: bool
        WT_SHOWMENU: bool
        WT_TABLEY: int
        WT_PRECISION: float
        WT_FONTSIZE: int
        WT_WINXPOS: int
        WT_WINYPOS: int
        WT_WINWIDTH: int
        WT_WINHEIGHT: int
        WT_DRAGLEFTRIGHTMODE: bool
        WT_ACTIVEVERTEXSET: int
        WT_SHOWMARKER: bool
        WT_MARKERTYPE: int
        WT_MARKERCOLOR: MXSWrapperBase
        DEBUGMODE: bool
        WT_ATTRIBLABELHEIGHT: int
        RIGHTJUSTIFYBONETEXT: bool
        GIZMOS: MXSWrapperBase
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
        MORPHNAME: None
        INFLUENCEANGLE: float
        FALLOFF: int
        SHOWMIRRORPLANE: bool
        MIRRORPLANE: int
        MIRROROFFSET: float
        MIRRORTHRESHOLD: float
        PREVIEWVERTS: bool
        PREVIEWBONE: bool
        JOINTTYPE: int
        TARGETNODES: MXSWrapperBase
        FALLOFFGRAPHS: MXSWrapperBase
        RELOADSELECTED: bool
        SAFEMODE: bool
        SHOWDRIVERBONE: bool
        SHOWMORPHBONE: bool
        SHOWCURRENTANGLE: bool
        SHOWLIMITANGLE: bool
        MATRIXSIZE: float
        SHOWDELTAS: bool
        SHOWX: bool
        SHOWY: bool
        SHOWZ: bool
        BONESIZE: float
        SOFTSELECTIONGRAPH: MXSWrapperBase
        USESOFTSELECTION: bool
        SELECTIONRADIUS: float
        EDGELIMIT: int
        USEEDGELIMIT: bool
        ENABLED: bool
        SHOWEDGES: bool
        ...
    class Skin_Wrap(Modifier):
        MESH: None
        THRESHOLD: float
        ENGINE: int
        FALLOFF: float
        DISTANCE: float
        FACELIMIT: int
        SHOWLOOPS: bool
        SHOWAXIS: bool
        SHOWFACELIMIT: bool
        SHOWMIRRORDATA: bool
        MIRRORPLANE: int
        MIRROROFFSET: float
        MESHLIST: MXSWrapperBase
        SHOWUNASSIGNEDVERTS: bool
        SHOWVERTS: bool
        WEIGHTALLVERTS: bool
        MIRRORTHRESHOLD: float
        BLEND: bool
        BLENDDISTANCE: float
        ...
    class Skin_Wrap_Patch(Modifier):
        PATCH: None
        SAMPLERATE: int
        ...
    class Skylight(Light):
        MULTIPLIER: float
        COLOR: MXSWrapperBase
        RAYS_PER_SAMPLE: int
        RAY_BIAS: float
        ON: bool
        CASTSHADOWS: bool
        SKY_COLOR_MAP: None
        SKY_COLOR_MAP_ON: bool
        SKY_COLOR_MAP_AMT: float
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
        SLICE_TYPE: int
        FACES___POLYGONS_TOGGLE: int
        ...
    class SliderControl(RolloutControl):
        ...
    class SliderManip(Helper):
        ...
    class Slider_Manip(Helper):
        ...
    class SlidingDoor(GeometryClass):
        HEIGHT: float
        OPEN: float
        WIDTH: float
        DEPTH: float
        DOUBLE_DOORS: int
        FLIP_SWING: bool
        FLIP_HINGE: bool
        CREATE_FRAME: bool
        FRAME_WIDTH: float
        FRAME_DEPTH: float
        DOOR_OFFSET: float
        LEAF_THICKNESS: float
        STILES_TOP_RAIL: float
        BOTTOM_RAIL: float
        NUMBER_OF_PANELS_HORIZONTALLY: int
        NUMBER_OF_PANELS_VERTICALLY: int
        MUNTIN: float
        PANEL_TYPE: int
        GLASS_THICKNESS: float
        BEVEL_ANGLE: float
        PANEL_THICKNESS_1: float
        PANEL_THICKNESS_2: float
        PANEL_MIDDLE_THICKNESS: float
        PANEL_WIDTH_1: float
        PANEL_WIDTH_2: float
        GENERATE_MAPPING_COORDS: bool
        ...
    class SlidingWindow(GeometryClass):
        HEIGHT: float
        WIDTH: float
        DEPTH: float
        HUNG: bool
        CHAMFERED_PROFILE: bool
        NUMBER_OF_PANELS_HORIZONTALLY: int
        NUMBER_OF_PANELS_VERTICALLY: int
        HORIZONTAL_FRAME_WIDTH: float
        VERTICAL_FRAME_WIDTH: float
        FRAME_THICKNESS: float
        GLAZING_THICKNESS: float
        RAIL_WIDTH: float
        PERCENT_OPEN: int
        GENERATE_MAPPING_COORDS: bool
        ...
    class Smoke(TextureMap):
        SIZE: float
        ITERATIONS: int
        EXPONENT: float
        PHASE: float
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1: None
        MAP2: None
        MAP1ON: bool
        MAP2ON: bool
        COORDS: MXSWrapperBase
        ...
    class SmoothModifier(Modifier):
        AUTOSMOOTH: bool
        PREVENTINDIRECT: bool
        THRESHOLD: float
        SMOOTHINGBITS: int
        ...
    class Snow(GeometryClass):
        DISPLAY: int
        START: MXSWrapperBase
        CONSTANT: bool
        RENDER: int
        SPEED: float
        VIEWPORTCOUNT: int
        RENDERCOUNT: int
        FLAKESIZE: float
        VARIATION: float
        STARTTIME: MXSWrapperBase
        LIFETIME: MXSWrapperBase
        LIFE: MXSWrapperBase
        BIRTHRATE: float
        EMITTERWIDTH: float
        EMITTERHEIGHT: float
        HIDEEMITTER: bool
        TUMBLE: float
        TUMBLESCALE: float
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
        DISPLATTICE: bool
        DISPSOURCE: bool
        DEFORMTYPE: int
        FALLOFF: float
        TENSION: float
        CONTINUITY: float
        LENGTH: float
        WIDTH: float
        HEIGHT: float
        ...
    class SpaceFFDCyl(SpacewarpObject):
        DISPLATTICE: bool
        DISPSOURCE: bool
        DEFORMTYPE: int
        FALLOFF: float
        TENSION: float
        CONTINUITY: float
        RADIUS: float
        HEIGHT: float
        ...
    class SpaceNoise(SpacewarpObject):
        ...
    class SpacePatchDeform(SpacewarpModifier):
        ROTATION: float
        U_STRETCH: float
        V_PERCENT: float
        V_STRETCH: float
        PLANE_TO_PATCH_DEFORM: int
        FLIP_DEFORMATION_AXIS: int
        U_PERCENT: float
        ...
    class SpacePathDeform(SpacewarpModifier):
        AXIS: int
        ROTATION: float
        TWIST: float
        STRETCH: float
        PATH: None
        FLIP_DEFORMATION_AXIS: int
        PERCENT_ALONG_PATH: float
        ...
    class SpaceSkew(SpacewarpObject):
        HEIGHT: float
        LENGTH: float
        WIDTH: float
        DECAY: float
        ...
    class SpaceStretch(SpacewarpObject):
        HEIGHT: float
        LENGTH: float
        WIDTH: float
        DECAY: float
        ...
    class SpaceSurfDeform(SpacewarpModifier):
        ROTATION: float
        SURFACE: None
        U_STRETCH: float
        V_PERCENT: float
        V_STRETCH: float
        PLANE_TO_PATCH_DEFORM: int
        FLIP_DEFORMATION_AXIS: int
        U_PERCENT: float
        ...
    class SpaceTaper(SpacewarpObject):
        HEIGHT: float
        LENGTH: float
        WIDTH: float
        DECAY: float
        ...
    class SpaceTwist(SpacewarpObject):
        HEIGHT: float
        LENGTH: float
        WIDTH: float
        DECAY: float
        ...
    class Space_Warp_Behavior(ReferenceTarget):
        NAME: str
        SPACEWARP: None
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
        ...
    class Spacedisplace(SpacewarpObject):
        AXIS: int
        BITMAP: None
        BLUR: float
        HEIGHT: float
        LENGTH: float
        MAP: None
        WIDTH: float
        CAP: bool
        U_TILE: float
        V_TILE: float
        DECAY: float
        MAPTYPE: int
        LUMCENTER: float
        LUMCENTERENABLE: bool
        USEMAP: bool
        APPLYMAP: bool
        U_FLIP: bool
        V_FLIP: bool
        W_FLIP: bool
        STRENGTH: float
        W_TILE: float
        ...
    class Spaceripple(SpacewarpObject):
        AMPLITUDE1: float
        AMPLITUDE2: float
        WAVELENGTH: float
        PHASE: float
        DECAY: float
        CIRCLES: int
        SEGMENTS: int
        DIVISIONS: int
        ...
    class SpacewarpModifier(MAXWrapper):
        ...
    class SpacewarpObject(Node):
        ...
    class Spacewave(SpacewarpObject):
        AMPLITUDE1: float
        AMPLITUDE2: float
        WAVELENGTH: float
        PHASE: float
        DECAY: float
        CIRCLES: int
        SEGMENTS: int
        DIVISIONS: int
        ...
    class Spawn(Helper):
        SPAWN_TYPE: int
        DELETE_PARENT: bool
        SPAWN_RATE: float
        SPAWN_STEP_SIZE: float
        SPAWN_ABLE: float
        NUMBER_OF_OFFSPRINGS: int
        OFFSPRINGS_VARIATION: float
        SYNC_TYPE: int
        RESTART_PARTICLE_AGE: bool
        SPEED_TYPE: int
        SPEED: float
        SPEED_INHERITED: float
        SPEED_VARIATION: float
        DIVERGENCE: float
        SCALE_FACTOR: float
        SCALE_VARIATION: float
        RANDOM_SEED: int
        ...
    class Speckle(TextureMap):
        SIZE: float
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1: None
        MAP2: None
        MAP1ON: bool
        MAP2ON: bool
        COORDS: MXSWrapperBase
        ...
    class Specular(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ...
    class SpeedByIcon(Helper):
        ACCEL_LIMIT: float
        INFLUENCE: float
        USE_SPEED_VARIATION: bool
        SPEED_MINIMUM: float
        SPEED_MAXIMUM: float
        USE_ICON_ORIENTATION: bool
        STEER_TOWARDS_TRAJECTORY: bool
        DISTANCE: float
        SYNC_TYPE_PARAM_ANIMATION: int
        SYNC_TYPE_ICON_ANIMATION: int
        ICON_SIZE: float
        COLOR_TYPE: bool
        RANDOM_SEED: int
        ...
    class SpeedVaryBehavior(ReferenceTarget):
        NAME: str
        PERIOD: int
        PERIODDEVIATION: float
        CENTERSPEED: float
        SPEEDDEVIATION: float
        ACCELPERIOD: float
        ACCELDEVIATION: float
        SEED: int
        ...
    class Speed_By_Surface(Helper):
        SPEED_TYPE: int
        SET_SPEED_MAGNITUDE: bool
        SPEED_VALUE: float
        SPEED_VARIATION: float
        SURFACE_OBJECTS: MXSWrapperBase
        ANIMATED_SHAPE: bool
        SUBFRAME_SAMPLING: bool
        SET_SPEED_BY_SURFACE_MATERIAL: bool
        MATERIAL_TYPE: int
        USE_SUB_MATERIAL: bool
        MATERIAL_ID: int
        DIRECTION_TYPE: int
        DIVERGENCE: float
        ACCELERATION_LIMIT: float
        UNLIMITED_RANGE: bool
        RANGE: float
        FALLOFF: float
        SYNC_TYPE: int
        RANDOM_SEED: int
        ...
    class Speed_Test(Helper):
        TEST_TYPE: int
        CONDITION_TYPE: int
        UNIT_VALUE: float
        UNIT_VARIATION: float
        ANGLE_VALUE: float
        ANGLE_VARIATION: float
        SYNC_TYPE: int
        RANDOM_SEED: int
        ...
    class Speed_Vary_Behavior(ReferenceTarget):
        NAME: str
        PERIOD: int
        PERIODDEVIATION: float
        CENTERSPEED: float
        SPEEDDEVIATION: float
        ACCELPERIOD: float
        ACCELDEVIATION: float
        SEED: int
        ...
    class Sphere(GeometryClass):
        SLICEON: bool
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS: float
        RADIUS: float
        SEGS: int
        SMOOTH: bool
        HEMISPHERE: float
        CHOP: int
        RECENTER: bool
        MAPCOORDS: bool
        SLICE: bool
        SLICEFROM: float
        SLICETO: float
        ...
    class SphereGizmo(Helper):
        RADIUS: float
        SEED: int
        HEMISPHERE: bool
        ...
    class SphericalCollision(ReferenceMaker):
        ...
    class Spherify(Modifier):
        PERCENT: float
        ...
    class SpinLimit(Helper):
        ...
    class Spindle(GeometryClass):
        HEIGHT: float
        RADIUS: float
        SIDES: int
        MAPCOORDS: int
        BLEND: float
        CAP_SEGMENTS: int
        CAP_HEIGHT: float
        SMOOTH_ON: int
        SLICE_ON: int
        SLICE_FROM: float
        SLICE_TO: float
        HEIGHT_SEGMENTS: int
        ...
    class SpineData2(ReferenceTarget):
        ...
    class SpineTrans2(Matrix3Controller):
        ...
    class SpinnerControl(RolloutControl):
        ...
    class Spiral_Stair(GeometryClass):
        STEPTYPE: int
        GENERATESTRINGERS: bool
        GENERATECARRIAGE: bool
        GENERATEINSIDERAILING: bool
        GENERATEOUTSIDERAILING: bool
        STEPWIDTH: float
        STEPTHICKNESS: float
        GENERATEMAPPING: bool
        STEPDEPTH_X: bool
        STEPDEPTH: float
        STEPHEIGHT: float
        STEPCOUNT: int
        STRINGERDEPTH: float
        STRINGERWIDTH: float
        STRINGEROFFSET: float
        STRINGERSPRINGFLOOR: bool
        CARRIAGEWIDTH: float
        CARRIAGEINTOFFS: float
        CARRIAGEEXTOFFS: float
        CARRIAGESPACE: float
        CARRIAGECOUNT: int
        CARRIAGECONTEXT: int
        CARRIAGESPACINGTYPE: int
        CARRIAGEHEIGHT: float
        CARRIAGESPRINGFLOOR: bool
        RAILINGHEIGHT: float
        RAILINGOFFS: float
        RAILINGSEGMENTS: int
        RAILINGRADIUS: float
        CENTERPOLERADIUS: float
        CENTERPOLESEGMENTS: int
        CENTERPOLEHEIGHT_X: bool
        CENTERPOLEHEIGHT: float
        GENERATECENTERPOLE: bool
        DIRECTION: int
        RADIUS: float
        REVOLUTIONS: float
        STEPSEGMENTS_X: bool
        STEPSEGMENTS: int
        ...
    class Splat(TextureMap):
        SIZE: float
        ITERATIONS: int
        THRESHOLD: float
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1: None
        MAP2: None
        MAP1ON: bool
        MAP2ON: bool
        COORDS: MXSWrapperBase
        ...
    class SplineIKChain(Matrix3Controller):
        ...
    class SplineIKSolver(IKSolver):
        ...
    class SplineInfluence(Modifier):
        SHOWKNOTS: bool
        NEARINFLUENCE: float
        FARINFLUENCE: float
        INFLUENCENODES: MXSWrapperBase
        FALLOFFTYPE: int
        ENABLEBIAS: bool
        BIASSELECTED: bool
        BIAS: float
        EXISTINGSELECTION: int
        INVERT: bool
        CONVERTSELECTIONS: bool
        FALLOFFMETHOD: int
        SELECTIONFALLOFFTYPE: int
        FALLOFFKNOTS: int
        FALLOFFPERCENT: float
        ...
    class SplineMirror(Modifier):
        AXIS: int
        FLIP: bool
        SLICE: bool
        WELD: bool
        THRESHOLD: float
        SHOWKNOTS: bool
        TANGENTS: bool
        ...
    class SplineMorph(Modifier):
        MORPHMETHOD: int
        AMOUNT: float
        USE_SOFTSELECTION: bool
        INVERT: bool
        SHOWKNOTS: bool
        TARGET1: None
        TARGETON1: bool
        TARGETWEIGHT1: float
        TARGET2: None
        TARGETON2: bool
        TARGETWEIGHT2: float
        TARGET3: None
        TARGETON3: bool
        TARGETWEIGHT3: float
        TARGET4: None
        TARGETON4: bool
        TARGETWEIGHT4: float
        TARGET5: None
        TARGETON5: bool
        TARGETWEIGHT5: float
        TARGET6: None
        TARGETON6: bool
        TARGETWEIGHT6: float
        TARGET7: None
        TARGETON7: bool
        TARGETWEIGHT7: float
        TARGET8: None
        TARGETON8: bool
        TARGETWEIGHT8: float
        TARGET9: None
        TARGETON9: bool
        TARGETWEIGHT9: float
        TARGET10: None
        TARGETON10: bool
        TARGETWEIGHT10: float
        ...
    class SplineOverlap(Modifier):
        THICKNESS: float
        DRAPE: float
        USENORMALS: bool
        USESELECTION: bool
        SHOWKNOTS: bool
        ...
    class SplineRelax(Modifier):
        AMOUNT: float
        ITERATIONS: int
        TANGENTS: bool
        KNOTS: bool
        USESELECTION: bool
        SHOWKNOTS: bool
        ...
    class SplineSelect(Modifier):
        ...
    class SplineShape(Shape):
        STEPS: int
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        ...
    class Spline_Chamfer(Modifier):
        SHOWKNOTS: bool
        AMOUNT: float
        DEPTH: float
        BIAS: float
        LIMITEFFECT: bool
        USESELECTION: bool
        USEMINANGLE: bool
        MINANGLE: float
        CORNERKNOTSONLY: bool
        ...
    class Spline_IK_Control(Modifier):
        HELPER_LIST: MXSWrapperBase
        HELPER_SIZE: float
        HELPER_CENTERMARKER: bool
        HELPER_AXISTRIPOD: bool
        HELPER_CROSS: bool
        BOX: bool
        CONSTANTSCREENSIZE: bool
        DRAWONTOP: bool
        LINKTYPES: int
        ...
    class Split_Amount(Helper):
        TEST_TYPE: int
        RATIO: float
        EVERY_NTH: int
        FIRST_N: int
        PER_EMISSION_SOURCE: bool
        RANDOM_SEED: int
        ...
    class Split_Group(Helper):
        GROUP_SELECTION_OPERATOR: None
        CONDITION_TYPE: int
        USE_PROXY_PARTICLES: bool
        PROXY_PARTICLE_SYSTEM: None
        MULTIPLIER: float
        INDEX_OFFSET: int
        GROUP_SELECTION_OPERATORS: MXSWrapperBase
        ...
    class Split_Selected(Helper):
        CONDITION_TYPE: int
        ...
    class Split_Source(Helper):
        CONDITION_TYPE: int
        SELECTED_SOURCES: MXSWrapperBase
        ...
    class Spray(GeometryClass):
        DISPLAY: int
        START: MXSWrapperBase
        CONSTANT: bool
        RENDER: int
        SPEED: float
        VIEWPORTCOUNT: int
        RENDERCOUNT: int
        VARIATION: float
        STARTTIME: MXSWrapperBase
        LIFETIME: MXSWrapperBase
        LIFE: MXSWrapperBase
        BIRTHRATE: float
        EMITTERWIDTH: float
        EMITTERHEIGHT: float
        HIDEEMITTER: bool
        DROPSIZE: float
        ...
    class SprayBirth(Helper):
        PARTICLE_PAINT_HELPER: None
        EMIT_START: int
        EMIT_TYPE: int
        EMIT_STOP: int
        DURATION: int
        SUBFRAME_SAMPLING: bool
        LOCK_POSITION: bool
        LOCK_ROTATION: bool
        ACQUIRE_SELECTION: bool
        SELECTION_TYPE: int
        ...
    class SprayCursor(GeometryClass):
        ...
    class SprayMaster(Helper):
        SPRAY_RADIUS: float
        DENSITY_CENTER: float
        DENSITY_SIDES: float
        PER_JET_LIMIT: int
        RATE_TYPE: int
        RATE_DROPS_PER_SECOND: float
        RATE_DROPS_PER_LENGTH_UNIT: float
        RATE_DROPS_PER_JET: int
        DISPLAY_TYPE: int
        DISPLAY_SIZE: float
        JET_START_TYPE: int
        JET_START_TIME: int
        JET_STOP_TYPE: int
        TIME_SCALE: float
        JET_STOP_TIME: int
        JET_DURATION: int
        AUTOADJUST_CURRENT_FRAME: bool
        ADJUST_GLOBAL_TIMING: bool
        ICON_SIZE: float
        RANDOM_SEED: int
        USE_RADIUS_GRAPH: bool
        SPRAY_RADIUS_GRAPH: None
        USE_RATE_GRAPH: bool
        SPRAY_RADIUS_RATE: None
        SPRAY_AT_TYPE: int
        SPRAY_AT_OBJECTS: MXSWrapperBase
        OBJECTS_ANIMATED_SURFACE: bool
        INCLUDE_SPRAY_CHILDREN: bool
        INCLUDE_SPRAY_GROUP_MEMBERS: bool
        USE_MASK_OBJECTS: bool
        MASKS: MXSWrapperBase
        INCLUDE_MASK_CHILDREN: bool
        INCLUDE_MASK_GROUP_MEMBERS: bool
        SELECTION_FILTER_TYPE: int
        LOCATION_TYPE: int
        DISTANCE: float
        DISTANCE_VARIATION: float
        USE_SEPARATION: bool
        SEPARATION_DISTANCE: float
        MAXIMUM_NUMBER_OF_ATTEMPTS: int
        STACK_UP_FOR_SEPARATION: bool
        GENERATE_ROTATION: bool
        PRIORITY_AXIS: int
        REVERSE_X_AXIS: bool
        REVERSE_Z_AXIS: bool
        ORIENTATION_TYPE_FOR_X_AXIS: int
        ORIENTATION_TYPE_FOR_Z_AXIS: int
        DIVERGENCE_FOR_X_AXIS: float
        DIVERGENCE_FOR_Z_AXIS: float
        ACQUIRE_SUB_MATERIAL_INDEX: bool
        GENERATE_MAPPING: bool
        ASSIGN_TO_MAPPING_CHANNELS: MXSWrapperBase
        MAPPING_TYPE: int
        MAPPING_START_VALUE: float
        MAPPING_END_VALUE: float
        MAPPING_OFFSET_VALUE_PER_SECOND: float
        MAPPING_OFFSET_VALUE_PER_DROP: float
        SHOW_PARTICLE_TIMING: bool
        LATE_COLOR: MXSWrapperBase
        EDITING_START_AT: int
        EDITING_STOP_TYPE: int
        EDITING_STOP_AT: int
        EDITING_DURATION: int
        EDITING_ADJUST_GLOBAL_TIMING: bool
        SELECTED_STROKES: MXSWrapperBase
        AUTO_SYNC_TIMING_BY_SELECTED_STROKE: bool
        ...
    class SprayPlacement(Helper):
        PARTICLE_PAINT_HELPER: None
        UPDATE_TYPE: int
        ACQUIRE_PAINT_POSITION: bool
        POSITION_TYPE: int
        SNAP_IF_CLOSE: bool
        SNAP_DISTANCE: float
        ACQUIRE_PAINT_ROTATION: bool
        BLENDIN_ROTATION: bool
        NEAR_DISTANCE: float
        FAR_DISTANCE: float
        ACQUIRE_PAINT_MAPPING: bool
        ACQUIRE_PAINT_MATERIALID: bool
        ACQUIRE_PAINT_SELECTION: bool
        SELECTION_TYPE: int
        ORDER_TYPE: int
        STOP_IF_COUNT_OVERFLOW: bool
        OBEY_QUANTITY_MULTIPLIER: bool
        SEPARATE_STREAMS_INDEXING: bool
        RANDOM_SEED: int
        ...
    class Spring(GeometryClass):
        WIRE: int
        DIAMETER: float
        FREE_SPRING_HEIGHT: float
        NUMBER_OF_TURNS: float
        TURN_DIRECTION: int
        SEGMENTATION_METHOD: int
        SEGMENTS_PER_TURN: int
        SEGMENTS_ALONG_TURN: int
        ROUND_WIRE_DIAMETER: float
        ROUND_WIRE_SIDE_COUNT: int
        RECTANGULAR_WIRE_WIDTH: float
        RECTANGULAR_WIRE_DEPTH: float
        RECTANGULAR_WIRE_FILLET_SIZE: float
        RECTANGULAR_FILLET_SIDES: int
        RECTANGULAR_WIRE_ROTATION_ANGLE: float
        D_SECTION_WIRE_WIDTH: float
        D_SECTION_WIRE_DEPTH: float
        D_SECTION_WIRE_FILLET_SIZE: float
        D_SECTION_WIRE_FILLET_SIDES: int
        D_SECTION_ROUND_SIDES: int
        D_SECTION_WIRE_ROTATION_ANGLE: float
        DYNAMICS_SPRING_RELAXED_HEIGHT: float
        DYNAMICS_K_CONSTANT_VALUE: float
        DYNAMICS_K_CONSTANT_UNITS: int
        DYNAMICS_SPRING_DIRECTION: int
        ENABLE_NONLINEARITY: int
        SMOOTH_SPRING: int
        END_PLACEMENT_METHOD: int
        RENDERABLE_SPRING: int
        GENERATE_MAPPING_COORDINATES: int
        ...
    class SpringPoint3Controller(Point3Controller):
        ...
    class SpringPositionController(PositionController):
        EFFECTHOW: int
        FORCENODE: MXSWrapperBase
        STEPS: int
        X_EFFECT: float
        Y_EFFECT: float
        Z_EFFECT: float
        START: int
        ...
    class Squad(Generic):
        ...
    class Squeeze(Modifier):
        BIAS: float
        VOLUME: float
        BULGE_AMOUNT: float
        BULGE_CURVITURE: float
        SQUEEZE_AMOUNT: float
        SQUEEZE_CURVATURE: float
        LIMIT_SQUEEZE_EFFECTS: int
        SQUEEZE_UPPER_LIMIT: float
        SQUEEZE_LOWER_LIMIT: float
        ...
    class StPathClass(Shape):
        ...
    class StackPerformance(Interface):
        ...
    class StandardMaterialClass(Value):
        ...
    class StandardTextureOutput(TexOutputClass):
        INVERT: bool
        CLAMP: bool
        ALPHAFROMRGB: bool
        RGB_LEVEL: float
        RGB_OFFSET: float
        OUTPUT_AMOUNT: float
        BUMP_AMOUNT: float
        ...
    class StandardUVGen(UVGenClass):
        BLUR: float
        MAPPING: int
        MAPCHANNEL: int
        MAPPINGTYPE: int
        UVW_TYPE: int
        U_MIRROR: bool
        V_MIRROR: bool
        U_TILE: bool
        V_TILE: bool
        SHOWMAPONBACK: bool
        NOISE_ON: bool
        NOISE_ANIMATE: bool
        UVTRANSFORM: MXSWrapperBase
        REALWORLDSCALE: bool
        REALWORLDHEIGHT: float
        REALWORLDWIDTH: float
        PHASE: float
        U_OFFSET: float
        V_OFFSET: float
        U_TILING: float
        V_TILING: float
        U_ANGLE: float
        V_ANGLE: float
        W_ANGLE: float
        NOISE_AMOUNT: float
        NOISE_SIZE: float
        NOISE_LEVELS: int
        BLUR_OFFSET: float
        ...
    class StandardXYZGen(XYZGenClass):
        BLUR: float
        OFFSET: MXSWrapperBase
        ANGLE: MXSWrapperBase
        COORDTYPE: int
        MAPCHANNEL: int
        BLUR_OFFSET: float
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
        SHADERTYPE: int
        WIRE: bool
        TWOSIDED: bool
        FACEMAP: bool
        FACETED: bool
        SHADERBYNAME: str
        OPACITYTYPE: int
        OPACITY: float
        FILTERCOLOR: MXSWrapperBase
        FILTERMAP: None
        OPACITYFALLOFFTYPE: int
        OPACITYFALLOFF: float
        IOR: float
        WIRESIZE: float
        WIREUNITS: int
        APPLYREFLECTIONDIMMING: bool
        DIMLEVEL: float
        REFLECTIONLEVEL: float
        SAMPLER: int
        SAMPLERQUALITY: float
        SAMPLERENABLE: bool
        SAMPLERADAPTTHRESHOLD: float
        SAMPLERADAPTON: bool
        SUBSAMPLETEXTUREON: bool
        SAMPLERADVANCEDOPTIONS: bool
        SAMPLERBYNAME: str
        USERPARAM0: float
        USERPARAM1: float
        SAMPLERUSEGLOBAL: bool
        MAPENABLES: MXSWrapperBase
        MAPS: MXSWrapperBase
        MAPAMOUNTS: MXSWrapperBase
        ADTEXTURELOCK: bool
        ...
    class Standin_For_Missing_MultiPass_Camera_Effect_Plugin(MPassCamEffect):
        ...
    class Star(Shape):
        STEPS: int
        NUMPOINTS: int
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        RADIUS1: float
        RADIUS2: float
        POINTS: int
        DISTORT: float
        FILLET1: float
        FILLET2: float
        ...
    class Star_Element(ReferenceTarget):
        ELEMENTNAME: str
        SIZE: float
        INTENSITY: float
        WIDTH: float
        ANGLE: float
        TAPER: float
        SHARP: float
        QUANTITY: int
        ON: bool
        OBJECTSHIDE: bool
        SQUEEZE: bool
        OCCLUSION: float
        COLORSOURCE: float
        CENTERCOLOR: MXSWrapperBase
        EDGECOLOR: MXSWrapperBase
        RADIALMTL: None
        USERADIALMTL: bool
        RADIALMAP: None
        USERADIALMAP: bool
        CIRCULARCOLORMIX: float
        LEFTSECTIONCOLOR: MXSWrapperBase
        CENTERSECTIONCOLOR: MXSWrapperBase
        RIGHTSECTIONCOLOR: MXSWrapperBase
        CIRCULARMTL: None
        USECIRCULARMTL: bool
        CIRCULARMAP: None
        USECIRCULARMAP: bool
        RADIALSIZEMAP: None
        USERADIALSIZEMAP: bool
        APPLYLIGHTS: bool
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        SOURCEOBJECTID: bool
        OBJECTID: int
        SOURCEEFFECTSID: bool
        EFFECTSID: int
        SOURCEUNCLAMPEDCOLOR: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        SOURCESURFACENORMAL: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        SOURCEWHOLE: bool
        SOURCEALPHA: bool
        ALPHA: int
        SOURCEZBUFFER: bool
        ZHI: float
        ZLO: float
        FILTERALL: bool
        FILTEREDGE: bool
        FILTERPERIMETERALPHA: bool
        FILTERPERIMETER: bool
        FILTERBRIGHTNESS: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        FILTERHUE: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        APPLYNOISE: bool
        NOISEMAP: None
        RADIALDENSITY: None
        USERADIALDENSITY: bool
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
        SHADOW_MODE: int
        PASS1: int
        PASS2: int
        RAY_BIAS: float
        BLUR: float
        JITTER_AMT: float
        TWOSIDEDSHADOWS: bool
        NOAREASHADOWS: bool
        SHADOW_TRANSPARENT: bool
        AA_THRESHOLD: MXSWrapperBase
        SUPPRESS_MAT_AA: bool
        SUPPRESS_REFLT_AA: bool
        SKIP_COPLANAR: bool
        COPLANAR_THRESHOLD: float
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
        ROTATION: MXSWrapperBase
        TIMING_START_TYPE: int
        SLOW_DOWN_START_TIME: int
        START_TIME_VARIATION: int
        USE_DIFFERENT_TYPES: bool
        STOP_TYPE: int
        STOP_TIME: int
        STOP_TIME_VARIATION: int
        RANDOM_SEED: int
        ...
    class Straight_Stair(GeometryClass):
        STEPTYPE: int
        GENERATESTRINGERS: bool
        GENERATECARRIAGE: bool
        GENERATEINSIDERAILING: bool
        GENERATEOUTSIDERAILING: bool
        STEPWIDTH: float
        STEPTHICKNESS: float
        GENERATEMAPPING: bool
        STEPDEPTH_X: bool
        STEPDEPTH: float
        STEPHEIGHT: float
        STEPCOUNT: int
        STRINGERDEPTH: float
        STRINGERWIDTH: float
        STRINGEROFFSET: float
        STRINGERSPRINGFLOOR: bool
        CARRIAGEWIDTH: float
        CARRIAGEINTOFFS: float
        CARRIAGEEXTOFFS: float
        CARRIAGESPACE: float
        CARRIAGECOUNT: int
        CARRIAGECONTEXT: int
        CARRIAGESPACINGTYPE: int
        CARRIAGEHEIGHT: float
        CARRIAGESPRINGFLOOR: bool
        RAILINGHEIGHT: float
        RAILINGOFFS: float
        RAILINGSEGMENTS: int
        RAILINGRADIUS: float
        LENGTH: float
        ...
    class Strauss(Shader):
        ...
    class Streak_Element(ReferenceTarget):
        ELEMENTNAME: str
        SIZE: float
        INTENSITY: float
        WIDTH: float
        ANGLE: float
        TAPER: float
        SHARP: float
        ON: bool
        OBJECTSHIDE: bool
        SQUEEZE: bool
        OCCLUSION: float
        COLORSOURCE: float
        CENTERCOLOR: MXSWrapperBase
        EDGECOLOR: MXSWrapperBase
        RADIALMTL: None
        USERADIALMTL: bool
        RADIALMAP: None
        USERADIALMAP: bool
        CIRCULARCOLORMIX: float
        QUADRANT1COLOR: MXSWrapperBase
        QUADRANT2COLOR: MXSWrapperBase
        QUADRANT3COLOR: MXSWrapperBase
        CIRCULARMTL: None
        USECIRCULARMTL: bool
        CIRCULARMAP: None
        USECIRCULARMAP: bool
        RADIALSIZEMAP: None
        USERADIALSIZEMAP: bool
        APPLYLIGHTS: bool
        APPLYIMAGE: bool
        APPLYIMAGECENTERS: bool
        SOURCEOBJECTID: bool
        OBJECTID: int
        SOURCEEFFECTSID: bool
        EFFECTSID: int
        SOURCEUNCLAMPEDCOLOR: bool
        UNCLAMPEDCOLOR: float
        UNCLAMPEDCOLORINVERT: bool
        SOURCESURFACENORMAL: bool
        SURFACENORMAL: float
        SURFACENORMALINVERT: bool
        SOURCEWHOLE: bool
        SOURCEALPHA: bool
        ALPHA: int
        SOURCEZBUFFER: bool
        ZHI: float
        ZLO: float
        FILTERALL: bool
        FILTEREDGE: bool
        FILTERPERIMETERALPHA: bool
        FILTERPERIMETER: bool
        FILTERBRIGHTNESS: bool
        BRIGHTNESS: int
        BRIGHTNESSINVERT: bool
        FILTERHUE: bool
        HUE: MXSWrapperBase
        HUERANGE: int
        APPLYNOISE: bool
        NOISEMAP: None
        RADIALDENSITY: None
        USERADIALDENSITY: bool
        ...
    class Stretch(Modifier):
        AXIS: int
        FROM: float
        TO: float
        STRETCH: float
        LIMIT: int
        AMPLIFY: float
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
        SIZE: float
        THICKNESS: float
        THRESHOLD: float
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1: None
        MAP2: None
        MAP1ON: bool
        MAP2ON: bool
        COORDS: MXSWrapperBase
        ...
    class SubstManager(Interface):
        ...
    class Substance(TextureMap):
        SUBSTANCEFILENAME: str
        COORDS: MXSWrapperBase
        GLOBALTEXTUREWIDTH: int
        GLOBALMODESCALE: int
        LOCALRELATIVETEXTUREWIDTH: int
        LOCALABSOLUTETEXTUREWIDTH: int
        LOCALMODE: int
        GLOBALTEXTUREHEIGHT: int
        LOCALRELATIVETEXTUREHEIGHT: int
        LOCALABSOLUTETEXTUREHEIGHT: int
        LOCKASPECTRATIO: int
        ROLLOUTSTATES: int
        ...
    class Substance2(TextureMap):
        SUBSTANCEFILEPATH: str
        EXPORTPRESETFILEPATH: str
        IMPORTPRESETFILEPATH: str
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
        SUBSTANCEFILENAME: str
        COORDS: MXSWrapperBase
        GLOBALTEXTUREWIDTH: int
        GLOBALMODESCALE: int
        LOCALRELATIVETEXTUREWIDTH: int
        LOCALABSOLUTETEXTUREWIDTH: int
        LOCALMODE: int
        GLOBALTEXTUREHEIGHT: int
        LOCALRELATIVETEXTUREHEIGHT: int
        LOCALABSOLUTETEXTUREHEIGHT: int
        LOCKASPECTRATIO: int
        ROLLOUTSTATES: int
        ...
    class Substance_Output(TextureMap):
        ...
    class Substituion_Offset_Transform(Matrix3Controller):
        ...
    class Substitute(Modifier):
        DISPLAYINVIEWPORT: bool
        DISPLAYINRENDER: bool
        OBJECTREFERENCE: None
        OBJECTNAME: str
        MOVECOPYINSTANCE: int
        SUBSTITUTETYPE: str
        RETAINPOSITION: bool
        RETAINLOCALROTATION: bool
        RETAINLOCALSCALE: bool
        ...
    class SubstituteMod(Modifier):
        DISPLAYINVIEWPORT: bool
        DISPLAYINRENDER: bool
        OBJECTREFERENCE: None
        OBJECTNAME: str
        MOVECOPYINSTANCE: int
        SUBSTITUTETYPE: str
        RETAINPOSITION: bool
        RETAINLOCALROTATION: bool
        RETAINLOCALSCALE: bool
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
        SHOW_COMPASS: bool
        COMPASS_RADIUS: float
        SUN_DISTANCE: float
        MODE: int
        JULIAN_DAY: int
        TIME_IN_SECONDS: int
        HOURS: int
        MINUTES: int
        DAY: int
        MONTH: int
        YEAR: int
        TIME_ZONE: float
        DST: bool
        DST_USE_DATE_RANGE: bool
        DST_START_DAY: int
        DST_START_MONTH: int
        DST_END_DAY: int
        DST_END_MONTH: int
        LOCATION: str
        LATITUDE_DEG: float
        LONGITUDE_DEG: float
        NORTH_DIRECTION_DEG: float
        MANUAL_SUN_POSITION: MXSWrapperBase
        AZIMUTH_DEG: float
        ALTITUDE_DEG: float
        WEATHER_FILE: str
        ...
    class Sun_Positioner(Light):
        SHOW_COMPASS: bool
        COMPASS_RADIUS: float
        SUN_DISTANCE: float
        MODE: int
        JULIAN_DAY: int
        TIME_IN_SECONDS: int
        HOURS: int
        MINUTES: int
        DAY: int
        MONTH: int
        YEAR: int
        TIME_ZONE: float
        DST: bool
        DST_USE_DATE_RANGE: bool
        DST_START_DAY: int
        DST_START_MONTH: int
        DST_END_DAY: int
        DST_END_MONTH: int
        LOCATION: str
        LATITUDE_DEG: float
        LONGITUDE_DEG: float
        NORTH_DIRECTION_DEG: float
        MANUAL_SUN_POSITION: MXSWrapperBase
        AZIMUTH_DEG: float
        ALTITUDE_DEG: float
        WEATHER_FILE: str
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
        SIZE: float
        SEED: int
        ICONSIZE: float
        SPEED: float
        MAPPINGTYPE: int
        VIEWTYPE: int
        VIEWPERCENT: float
        QUANTITYMETHOD: int
        PARTICLETYPE: int
        STANDARDPARTICLE: int
        METABALLRENDERCOARSNESS: float
        METABALLVIEWCOARSNESS: float
        METABALLAUTOCOARSNESS: bool
        INSTANCESUBTREE: bool
        INSTANCEKEYOFFSETTYPE: int
        INSTANCEFRAMEOFFSET: int
        SPINAXISTYPE: int
        SPAWNTYPE: int
        SPAWNSPEEDTYPE: int
        SPAWNINHERITVELOCITY: bool
        SPAWNSPEEDFIXED: bool
        SPAWNSCALETYPE: int
        SPAWNSCALEFIXED: bool
        MOTIONINFLUENCE: float
        MOTIONMULTIPLIER: float
        MOTIONVARIATION: float
        INSTANCINGOBJECT: None
        LIFESPANVALUEQUEUE: MXSWrapperBase
        OBJECTMUTATIONQUEUE: MXSWrapperBase
        SUBSAMPLEEMITTERTRANSLATION: bool
        SUBSAMPLEEMITTERROTATION: bool
        SUBSAMPLECREATIONTIME: bool
        ICONHIDDEN: bool
        LIFE: MXSWrapperBase
        OFF_AXIS: float
        AXIS_SPREAD: float
        OFF_PLANE: float
        PLANE_SPREAD: float
        BUBBLE_AMPLITUDE: float
        BUBBLE_AMPLITUDE_VARIATION: float
        BUBBLE_PERIOD: MXSWrapperBase
        BUBBLE_PERIOD_VARIATION: float
        BUBBLE_PHASE: float
        BLUR_STRETCH: int
        SPEED_VARIATION: float
        BIRTH_RATE: int
        TOTAL_NUMBER: int
        EMITTER_START: MXSWrapperBase
        EMITTER_STOP: MXSWrapperBase
        DISPLAY_UNTIL: MXSWrapperBase
        LIFE_VARIATION: MXSWrapperBase
        SIZE_VARIATION: float
        GROWTH_TIME: MXSWrapperBase
        FADE_TIME: MXSWrapperBase
        METAPARTICLE_TENSION: float
        METAPARTICLE_TENSION_VARIATION: float
        MAPPING_TIME_BASE: MXSWrapperBase
        MAPPING_DISTANCE_BASE: float
        SPIN_TIME: MXSWrapperBase
        SPIN_TIME_VARIATION: float
        SPIN_PHASE: float
        SPIN_PHASE_VARIATION: float
        X_SPIN_VECTOR: float
        Y_SPIN_VECTOR: float
        Z_SPIN_VECTOR: float
        SPIN_AXIS_VARIATION: float
        SPAWN_DIRECTION_CHAOS: float
        SPAWN_SPEED_CHAOS: float
        SPAWN_SCALE_CHAOS: float
        SPAWN_AFFECTS: int
        SPAWN_MULTIPLIER_VARIATION: float
        BUBBLE_PHASE_VARIATION: float
        DIE__X_FRAMES_AFTER_COLLISION: MXSWrapperBase
        DIE__X_FRAMES_AFTER_COLLISION_VARIATION: float
        INTERPARTICLE_COLLISIONS_ON: int
        INTERPARTICLE_COLLISION_STEPS: int
        INTERPARTICLE_COLLISION_BOUNCE: float
        INTERPARTICLE_COLLISION_BOUNCE_VARIATION: float
        ...
    class SurfDeform(Modifier):
        ROTATION: float
        SURFACE: None
        U_STRETCH: float
        V_PERCENT: float
        V_STRETCH: float
        PLANE_TO_PATCH_DEFORM: int
        FLIP_DEFORMATION_AXIS: int
        U_PERCENT: float
        ...
    class SurfaceArriveBehavior(ReferenceTarget):
        NAME: str
        SURFACES: MXSWrapperBase
        DISABLEAFTERARRIVING: bool
        RATE: float
        RATEDEVIATION: float
        SPEED: float
        SPEEDDEVIATION: float
        DISTANCE: float
        DISTANCEDEVIATION: float
        OFFSET: float
        FACING: bool
        RANDOM_CLOSEST: int
        EVERYFRAME: bool
        DISPLAYOFFSET: bool
        HEIGHT: float
        HEIGHTDEVIATION: float
        DESCENTSTART: float
        DESCENTSTARTDEVIATION: float
        USENORMAL: bool
        XNORMAL: float
        YNORMAL: float
        ZNORMAL: float
        SEED: int
        TARGETCOLOR: MXSWrapperBase
        DISPLAYTARGET: bool
        TARGETSCALE: float
        ...
    class SurfaceFilterFn(MAXScriptFunction):
        ...
    class SurfaceFollowBehavior(ReferenceTarget):
        NAME: str
        SURFACES: MXSWrapperBase
        USEPROJECTION: bool
        XVECTOR: float
        YVECTOR: float
        ZVECTOR: float
        OFFSET: float
        DISPLAYOFFSET: bool
        TARGETCOLOR: MXSWrapperBase
        DISPLAYTARGET: bool
        TARGETSCALE: float
        ...
    class Surface_Approximation(UtilityPlugin):
        ...
    class Surface_Arrive_Behavior(ReferenceTarget):
        NAME: str
        SURFACES: MXSWrapperBase
        DISABLEAFTERARRIVING: bool
        RATE: float
        RATEDEVIATION: float
        SPEED: float
        SPEEDDEVIATION: float
        DISTANCE: float
        DISTANCEDEVIATION: float
        OFFSET: float
        FACING: bool
        RANDOM_CLOSEST: int
        EVERYFRAME: bool
        DISPLAYOFFSET: bool
        HEIGHT: float
        HEIGHTDEVIATION: float
        DESCENTSTART: float
        DESCENTSTARTDEVIATION: float
        USENORMAL: bool
        XNORMAL: float
        YNORMAL: float
        ZNORMAL: float
        SEED: int
        TARGETCOLOR: MXSWrapperBase
        DISPLAYTARGET: bool
        TARGETSCALE: float
        ...
    class Surface_Follow_Behavior(ReferenceTarget):
        NAME: str
        SURFACES: MXSWrapperBase
        USEPROJECTION: bool
        XVECTOR: float
        YVECTOR: float
        ZVECTOR: float
        OFFSET: float
        DISPLAYOFFSET: bool
        TARGETCOLOR: MXSWrapperBase
        DISPLAYTARGET: bool
        TARGETSCALE: float
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
        TYPE: int
        ACTIVE_INPUT: int
        RENDER_VIEWPORT_SWITCH: bool
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        INPUT_7: None
        INPUT_8: None
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
        CURVE: float
        SYMMETRY: bool
        LIMIT: bool
        UPPERLIMIT: float
        LOWERLIMIT: float
        AMOUNT: float
        PRIMARYAXIS: int
        EFFECTAXIS: int
        ...
    class Targa(BitmapIO):
        ...
    class TargetDirectionallight(Light):
        ASPECT: float
        RGB: MXSWrapperBase
        COLOR: MXSWrapperBase
        CONTRAST: float
        ENABLED: bool
        ON: bool
        TYPE: MXSWrapperBase
        VALUE: int
        FALLOFF: float
        EXCLUDELIST: MXSWrapperBase
        INCLUDELIST: None
        SHOWCONE: bool
        MULTIPLIER: float
        SOFTENDIFFUSEEDGE: float
        HOTSPOT: float
        FARATTENSTART: float
        FARATTENEND: float
        NEARATTENSTART: float
        NEARATTENEND: float
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        DECAYRADIUS: float
        SHADOWCOLOR: MXSWrapperBase
        SHADOWMULTIPLIER: float
        HSV: MXSWrapperBase
        HUE: int
        SATURATION: int
        INCLEXCLTYPE: int
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        USENEARATTEN: bool
        SHOWNEARATTEN: bool
        USEFARATTEN: bool
        SHOWFARATTEN: bool
        ATTENDECAY: int
        PROJECTOR: bool
        PROJECTORMAP: None
        CASTSHADOWS: bool
        USEGLOBALSHADOWSETTINGS: bool
        RAYTRACEDSHADOWS: bool
        OVERSHOOT: bool
        CONESHAPE: int
        LIGHTSHAPE: int
        ATMOSSHADOWS: bool
        LIGHTAFFECTSSHADOW: bool
        SHADOWPROJECTORMAP: None
        USESHADOWPROJECTORMAP: bool
        AMBIENTONLY: bool
        SHADOWGENERATOR: MXSWrapperBase
        ...
    class Target_Area(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Target_Cylinder(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Target_Disc(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Target_Light(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Target_Linear(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Target_Point(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Target_Rectangle(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Target_Sphere(Light):
        ON: bool
        CASTSHADOWS: bool
        RGBFILTER: MXSWrapperBase
        INTENSITY: float
        KELVIN: float
        USEKELVIN: bool
        INTENSITYAT: float
        INTENSITYTYPE: int
        FLUX: float
        ORIGINALINTENSITY: float
        ORIGINALFLUX: float
        USEMULTIPLIER: bool
        MULTIPLIER: float
        SHIFTCOLORWHENDIMMING: bool
        USEFARATTENUATION: bool
        DISPLAYFARATTENUATIONGIZMO: bool
        STARTFARATTENUATION: float
        ENDFARATTENUATION: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        PROJECTOR: bool
        PROJECTORMAP: None
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        AMBIENTONLY: bool
        TARGETDISTANCE: None
        LIGHT_LENGTH: float
        LIGHT_WIDTH: float
        LIGHT_RADIUS: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        SHADOWCOLORMAPENABLE: bool
        SHADOWCOLOR: MXSWrapperBase
        LIGHTAFFECTSSHADOW: bool
        USEGLOBALSHADOWSETTINGS: bool
        SHADOWPROJECTORMAP: None
        HOTSPOT: float
        FALLOFF: float
        SHOWCONE: bool
        WEBFILE: str
        XROTATION: float
        YROTATION: float
        ZROTATION: float
        ...
    class Targetcamera(Camera):
        TYPE: MXSWrapperBase
        FOV: float
        NEARRANGE: float
        FARRANGE: float
        NEARCLIP: float
        NEAR_CLIP: float
        FARCLIP: float
        FAR_CLIP: float
        MPASSENABLED: bool
        MPASSRENDERPERPASS: bool
        CURFOV: float
        FOVTYPE: int
        ORTHOPROJECTION: bool
        SHOWCONE: bool
        SHOWHORIZON: bool
        SHOWRANGES: bool
        CLIPMANUALLY: bool
        MPASSEFFECT: MXSWrapperBase
        ...
    class Targetobject(GeometryClass):
        ...
    class Teapot(GeometryClass):
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS: float
        RADIUS: float
        SEGS: int
        SMOOTH: bool
        BODY: bool
        HANDLE: bool
        SPOUT: bool
        LID: bool
        MAPCOORDS: bool
        ...
    class Tee(Shape):
        STEPS: int
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        TYPEIN_X: float
        TYPEIN_Y: float
        TYPEIN_Z: float
        TYPEIN_LENGTH: float
        TYPEIN_WIDTH: float
        TYPEIN_THICKNESS: float
        TYPEIN_RADIUS: float
        TYPEIN_CREATIONMETHOD: bool
        TEE_LENGTH: float
        TEE_WIDTH: float
        TEE_THICKNESS: float
        TEE_RADIUS: float
        ...
    class TempObjectClass(TemporaryMergeNodeObjectClass):
        ...
    class TemporaryMergeNodeObjectClass(MAXWrapper):
        ...
    class Terrain(GeometryClass):
        DISPLAY: int
        UPDATE: int
        RETRIANGULATE: bool
        NUMOPS: int
        STITCHBORDER: bool
        HORIZSIMPLIFICATION: int
        VERTSIMPLIFICATION: int
        FORM: int
        ...
    class Test_Icon(Helper):
        VISIBLE_ICON: bool
        ICON_TYPE: int
        ICON_PARAMETER_1: float
        ICON_PARAMETER_2: float
        ICON_PARAMETER_3: float
        COLOR_COORDINATED: bool
        AUTO_UPDATE: bool
        SUBOPERATORS: MXSWrapperBase
        SELECTED_SUBOPERATORS: MXSWrapperBase
        GROUPS: MXSWrapperBase
        ENABLE_BY_SWITCH: bool
        DEFAULT_WIDTH: int
        DEFAULT_OFFSET: int
        DEFAULT_HEIGHT: int
        DEFAULT_RANGE_TYPE: int
        DEFAULT_RANGE_MIN: float
        DEFAULT_RANGE_MAX: float
        ACTIVITY_TYPE: int
        TIME_ON: int
        TIME_OFF: int
        ANIMATABLE_ACTIVE: bool
        PDVIEW_ORIGIN_X: int
        PDVIEW_ORIGIN_Y: int
        PDVIEW_WIDTH: int
        PDVIEW_HEIGHT: int
        PDVIEW_DIVIDER: int
        PDVIEW_SHOW_DEPOT: bool
        PDVIEW_DESCRIPTION_TYPE: int
        PDVIEW_SHOW_PARAMETERS: bool
        USE_DYNAMIC_NAMES_FOR_NEW: bool
        AUTO_UPDATE_ON_DATA_VIEW_CLOSE: bool
        REPEATS: int
        ...
    class TexOutputClass(Material):
        ...
    class TexSkyLight(Light):
        MULTIPLIER: float
        COLOR: MXSWrapperBase
        RAYS_PER_SAMPLE: int
        RAY_BIAS: float
        ON: bool
        CASTSHADOWS: bool
        SKY_COLOR_MAP: None
        SKY_COLOR_MAP_ON: bool
        SKY_COLOR_MAP_AMT: float
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
        FILTER: bool
        MIPMAP: bool
        MONOOUTPUT: int
        RGBOUTPUT: int
        APPLYCROP: bool
        CROPORPLACE: int
        CROP_U: float
        CROP_V: float
        CROP_W: float
        CROP_H: float
        JITTER: bool
        JITTERAMT: float
        ALPHASOURCE: int
        COORDS: MXSWrapperBase
        OUTPUT: MXSWrapperBase
        RESTYPE: int
        FINITERESOLUTION: int
        TEXTOBJECT: None
        OUTLINECOLOR: MXSWrapperBase
        FILLCOLOR: MXSWrapperBase
        BGCOLOR: MXSWrapperBase
        FILLBG: bool
        GLYPHOPTION: int
        FILLEDCHARACTERS: bool
        OUTLINEDCHARACTERS: bool
        OUTLINEWIDTH: float
        BOUNDSTYPE: int
        MANUALWIDTH: float
        MANUALHEIGHT: float
        STRICTHIERARCHY: bool
        BOUNDSOBJECT: None
        RENDERCHILDREN: bool
        RENDERROOT: bool
        MERGESHAPES: bool
        USEFILLCOLOR: bool
        HWBITMAPSIZE: int
        ...
    class TextObject2(GeometryClass):
        INTERPOLATIONSTEPS: int
        OPTIMIZE: int
        ADAPTIVE: int
        LAYOUTTYPE: int
        PLANE: int
        LENGTH: float
        WIDTH: float
        ALIGNMENT: int
        SIZE: float
        TRACKING: float
        LEADING: float
        VSCALE: float
        HSCALE: float
        GENERATEGEOMETRY: int
        ELEMENTTYPE: int
        CHARKERNINGOFFSET: MXSWrapperBase
        CHARBASELINEOFFSET: MXSWrapperBase
        CHARXSCALE: MXSWrapperBase
        CHARYSCALE: MXSWrapperBase
        EXTRUDEAMOUNT: float
        EXTRUDESEGMENTS: int
        APPLYBEVEL: bool
        BEVELDEPTH: float
        USEBEVELWIDTH: bool
        BEVELWIDTH: float
        BEVELSTEPS: int
        BEVELPUSH: float
        BEVELOPTIMIZE: bool
        CAPSTART: int
        CAPSTARTCONSTRAIN: bool
        CAPEND: int
        CAPENDCONSTRAIN: bool
        CAPTYPE: int
        STARTCAPMATERIAL: int
        STARTBEVELMATERIAL: int
        SIDEMATERIAL: int
        ENDBEVELMATERIAL: int
        ENDCAPMATERIAL: int
        BEVELOFFSET: float
        MACRONAME: MXSWrapperBase
        MACROVALUE: MXSWrapperBase
        UPAXIS: int
        AXISFLIP: bool
        NODEELEMENTS: MXSWrapperBase
        NODEELEMENTSCENTERS: MXSWrapperBase
        ...
    class TextPlus(GeometryClass):
        INTERPOLATIONSTEPS: int
        OPTIMIZE: int
        ADAPTIVE: int
        LAYOUTTYPE: int
        PLANE: int
        LENGTH: float
        WIDTH: float
        ALIGNMENT: int
        SIZE: float
        TRACKING: float
        LEADING: float
        VSCALE: float
        HSCALE: float
        GENERATEGEOMETRY: int
        ELEMENTTYPE: int
        CHARKERNINGOFFSET: MXSWrapperBase
        CHARBASELINEOFFSET: MXSWrapperBase
        CHARXSCALE: MXSWrapperBase
        CHARYSCALE: MXSWrapperBase
        EXTRUDEAMOUNT: float
        EXTRUDESEGMENTS: int
        APPLYBEVEL: bool
        BEVELDEPTH: float
        USEBEVELWIDTH: bool
        BEVELWIDTH: float
        BEVELSTEPS: int
        BEVELPUSH: float
        BEVELOPTIMIZE: bool
        CAPSTART: int
        CAPSTARTCONSTRAIN: bool
        CAPEND: int
        CAPENDCONSTRAIN: bool
        CAPTYPE: int
        STARTCAPMATERIAL: int
        STARTBEVELMATERIAL: int
        SIDEMATERIAL: int
        ENDBEVELMATERIAL: int
        ENDCAPMATERIAL: int
        BEVELOFFSET: float
        MACRONAME: MXSWrapperBase
        MACROVALUE: MXSWrapperBase
        UPAXIS: int
        AXISFLIP: bool
        NODEELEMENTS: MXSWrapperBase
        NODEELEMENTSCENTERS: MXSWrapperBase
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
        COORDS: MXSWrapperBase
        OBJECT: None
        COLOR0: MXSWrapperBase
        COLOR1: MXSWrapperBase
        TRANSITIONRANGE: float
        SUBTEX0: None
        SUBTEX1: None
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        DISPLACEAMOUNT: float
        DISPLACETEX: None
        DISPLACEENABLED: bool
        TRANSITIONBIAS: float
        ...
    class Texture_Sky(Light):
        MULTIPLIER: float
        COLOR: MXSWrapperBase
        RAYS_PER_SAMPLE: int
        RAY_BIAS: float
        ON: bool
        CASTSHADOWS: bool
        SKY_COLOR_MAP: None
        SKY_COLOR_MAP_ON: bool
        SKY_COLOR_MAP_AMT: float
        SKY_MODE: int
        ...
    class Thin_Wall_Refraction(TextureMap):
        BLUR: float
        THICKNESSOFFSET: float
        BUMPMAPEFFECT: float
        APPLYBLUR: bool
        NTHFRAME: int
        USEENVIROMENT: bool
        FRAME: int
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
        TOPMATERIAL: MXSWrapperBase
        BOTTOMMATERIAL: MXSWrapperBase
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        BLEND: float
        POSITION: float
        COORDINATES: int
        ...
    class Torus(GeometryClass):
        SLICEON: bool
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS1: float
        TYPEINRADIUS2: float
        RADIUS1: float
        RADIUS2: float
        TUBEROTATION: float
        TUBETWIST: float
        SEGS: int
        SIDES: int
        SMOOTH: int
        SLICE: bool
        SLICETO: float
        SLICEFROM: float
        MAPCOORDS: bool
        ...
    class Torus_Knot(GeometryClass):
        SMOOTH: int
        RADIUS: float
        SIDES: int
        TWIST: float
        U_TILE: float
        V_TILE: float
        SEGMENTS: int
        RADIUS2: float
        P: float
        Q: float
        LUMP_OFFSET: float
        ECCENTRICITY: float
        LUMPS: float
        LUMP_HEIGHT: float
        BASE_CURVE: int
        GEN_UV: int
        WARP_HEIGHT: float
        WARP_COUNT: float
        U_OFFSET: float
        V_OFFSET: float
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
        PRIORITY: int
        DURATION: int
        EASEIN: float
        EASEOUT: float
        FUNCTIONNAME: str
        SCRIPT: None
        FROM: None
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
        SLICEON: bool
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINRADIUS1: float
        TYPEINRADIUS2: float
        TYPEINHEIGHT: float
        RADIUS1: float
        RADIUS2: float
        HEIGHT: float
        SIDES: int
        CAPSEGS: int
        HEIGHTSEGS: int
        SMOOTH: bool
        SLICE: bool
        SLICEFROM: float
        SLICETO: float
        MAPCOORDS: bool
        ...
    class TurboSmooth(Modifier):
        ITERATIONS: int
        USERENDERITERATIONS: bool
        RENDERITERATIONS: int
        ISOLINEDISPLAY: bool
        EXPLICITNORMALS: bool
        SMOOTHRESULT: bool
        SEPBYMATS: bool
        SEPBYSMGROUPS: bool
        UPDATE: int
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
        USEINVISIBLEEDGES: bool
        SELECTIONCONVERSION: int
        USESOFTSELECTION: bool
        SELECTIONLEVEL: int
        ...
    class Turn_To_Patch(Modifier):
        QUADSTOQUADS: bool
        SELECTIONCONVERSION: int
        USESOFTSELECTION: int
        SELECTIONLEVEL: int
        ...
    class Turn_To_Poly(Modifier):
        KEEPCONVEX: bool
        LIMITPOLYSIZE: bool
        MAXPOLYSIZE: int
        REQUIREPLANAR: bool
        PLANARTHRESH: float
        REMOVEMIDEDGEVERTICES: bool
        SELECTIONCONVERSION: int
        USESOFTSELECTION: bool
        SELECTIONLEVEL: int
        ...
    class Twist(Modifier):
        AXIS: int
        BIAS: float
        ANGLE: float
        LIMIT: bool
        UPPERLIMIT: float
        LOWERLIMIT: float
        ...
    class UConstraint(Helper):
        BODY0: None
        BODY1: None
        HELPERSIZE: float
        LINEARMODEX: int
        LINEARMODEY: int
        LINEARMODEZ: int
        LINEARPOSITION: float
        LINEARRESTITUTION: float
        LINEARSPRING: float
        LINEARDAMPING: float
        SWING1MODE: int
        SWING1ANGLE: float
        SWING1RESTITUTION: float
        SWING1SPRING: float
        SWING1DAMPING: float
        SWING2MODE: int
        SWING2ANGLE: float
        SWING2RESTITUTION: float
        SWING2SPRING: float
        SWING2DAMPING: float
        TWISTMODE: int
        TWISTANGLELOW: float
        TWISTANGLEHIGH: float
        TWISTRESTITUTIONLOW: float
        TWISTRESTITUTIONHIGH: float
        TWISTSPRINGLOW: float
        TWISTSPRINGHIGH: float
        TWISTDAMPINGLOW: float
        TWISTDAMPINGHIGH: float
        POSSPRING: float
        POSDAMPING: float
        SWINGSPRING: float
        SWINGDAMPING: float
        TWISTSPRING: float
        TWISTDAMPING: float
        COLLISION: bool
        BREAKABLE: bool
        MAXFORCE: float
        MAXTORQUE: float
        GEARING: bool
        GEARRATIO: float
        USEPROJECTION: bool
        PROJECTIONMODE: int
        PROJECTIONDIST: float
        PROJECTIONANGLE: float
        CHILDATTACHPOINT: MXSWrapperBase
        CHILDINITIALTWIST: float
        SHOWVISUALIZER: bool
        USEACCELERATION: bool
        USEHARDLIMITS: bool
        ...
    class UDeflector(SpacewarpObject):
        BOUNCE: float
        BOUNCEVAR: float
        CHAOS: float
        RADIUS: float
        FRICTION: float
        INHERITVELOCITY: float
        ...
    class UDeflectorMod(SpacewarpModifier):
        ...
    class UIAccessor(Interface):
        ...
    class UOmniFlect(SpacewarpObject):
        TIMEON: MXSWrapperBase
        TIMEOFF: MXSWrapperBase
        AFFECTS: float
        BOUNCE: float
        BOUNCEVAR: float
        CHAOS: float
        FRICTION: float
        INHERITVELOCITY: float
        REFRACTS: float
        DECELERATION: float
        DECELVAR: float
        REFRACTION: float
        REFRACTIONVAR: float
        DIFFUSION: float
        DIFFUSIONVAR: float
        RADIUS: float
        SPAWN: float
        PASSVELOCITY: float
        PASSVELOCITYVAR: float
        ...
    class UOmniFlectMod(SpacewarpModifier):
        ...
    class USetup(Primitive):
        ...
    class UTypeStair(GeometryClass):
        STEPTYPE: int
        GENERATESTRINGERS: bool
        GENERATECARRIAGE: bool
        GENERATEINSIDERAILING: bool
        GENERATEOUTSIDERAILING: bool
        STEPWIDTH: float
        STEPTHICKNESS: float
        GENERATEMAPPING: bool
        STEPDEPTH_X: bool
        STEPDEPTH: float
        STEPHEIGHT: float
        STEPCOUNT: int
        STRINGERDEPTH: float
        STRINGERWIDTH: float
        STRINGEROFFSET: float
        STRINGERSPRINGFLOOR: bool
        CARRIAGEWIDTH: float
        CARRIAGEINTOFFS: float
        CARRIAGEEXTOFFS: float
        CARRIAGESPACE: float
        CARRIAGECOUNT: int
        CARRIAGECONTEXT: int
        CARRIAGESPACINGTYPE: int
        CARRIAGEHEIGHT: float
        CARRIAGESPRINGFLOOR: bool
        RAILINGHEIGHT: float
        RAILINGOFFS: float
        RAILINGSEGMENTS: int
        RAILINGRADIUS: float
        DIRECTION: int
        LENGTH: float
        LENGTH2: float
        UPPEROFFSET: float
        ...
    class UVGenClass(Material):
        ...
    class UVWUnwrap(Modifier):
        TEXMAPLIST: MXSWrapperBase
        CHECKERMATERIAL: MXSWrapperBase
        BASEMATERIAL: None
        TEXMAPIDLIST: MXSWrapperBase
        GRIDSNAP: bool
        VERTEXSNAP: bool
        EDGESNAP: bool
        SHOWIMAGEALPHA: bool
        RENDERUV_WIDTH: int
        RENDERUV_HEIGHT: int
        RENDERUV_EDGECOLOR: MXSWrapperBase
        RENDERUV_EDGEALPHA: float
        RENDERUV_SEAMCOLOR: MXSWrapperBase
        RENDERUV_VISIBLEEDGES: bool
        RENDERUV_INVISIBLEEDGES: bool
        RENDERUV_SEAMEDGES: bool
        RENDERUV_SHOWFRAMEBUFFER: bool
        RENDERUV_FORCE2SIDED: bool
        RENDERUV_FILLMODE: int
        RENDERUV_FILLALPHA: float
        RENDERUV_FILLCOLOR: MXSWrapperBase
        RENDERUV_SHOWOVERLAP: bool
        RENDERUV_OVERLAPCOLOR: MXSWrapperBase
        QUICK_MAP_PREVIEW: bool
        QUICK_MAP_ALIGN: int
        BASEMATERIAL_LIST: MXSWrapperBase
        SPLINEMAP_NODE: None
        SPLINEMAP_MANUALSEAMS: bool
        SPLINEMAP_PROJECTIONTYPE: int
        SPLINEMAP_DISPLAY: bool
        SPLINEMAP_USCALE: float
        SPLINEMAP_VSCALE: float
        SPLINEMAP_UOFFSET: float
        SPLINEMAP_VOFFSET: float
        LOCALDISTORTION: bool
        SPLINEMAP_ITERATIONS: int
        SPLINEMAP_RESAMPLECOUNT: int
        SPLINEMAP_ADVANCEMETHOD: int
        TOOLBARVISIBLE: bool
        BUTTONPANEL_VISIBLE: bool
        BUTTONPANEL_WIDTH: int
        BUTTONPANEL_HEIGHT1: int
        BUTTONPANEL_HEIGHT2: int
        WELDONLYSHARED: bool
        GROUPNAME: MXSWrapperBase
        GROUPDENSITY: MXSWrapperBase
        GROUPDISPLAY: bool
        AUTOPIN: bool
        FILTERPIN: bool
        PEELAUTOEDIT: bool
        TEXTURECHECKERMATERIAL: None
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
        U_TILE: float
        V_TILE: float
        U_FLIP: int
        V_FLIP: int
        W_FLIP: int
        W_OFFSET: float
        ROTATION_ANGLE: float
        ROTATION_CENTER: int
        U_OFFSET: float
        V_OFFSET: float
        W_TILE: float
        MAP_OR_VERTEX_COLOR: int
        MAP_CHANNEL: int
        ...
    class U_Type_Stair(GeometryClass):
        STEPTYPE: int
        GENERATESTRINGERS: bool
        GENERATECARRIAGE: bool
        GENERATEINSIDERAILING: bool
        GENERATEOUTSIDERAILING: bool
        STEPWIDTH: float
        STEPTHICKNESS: float
        GENERATEMAPPING: bool
        STEPDEPTH_X: bool
        STEPDEPTH: float
        STEPHEIGHT: float
        STEPCOUNT: int
        STRINGERDEPTH: float
        STRINGERWIDTH: float
        STRINGEROFFSET: float
        STRINGERSPRINGFLOOR: bool
        CARRIAGEWIDTH: float
        CARRIAGEINTOFFS: float
        CARRIAGEEXTOFFS: float
        CARRIAGESPACE: float
        CARRIAGECOUNT: int
        CARRIAGECONTEXT: int
        CARRIAGESPACINGTYPE: int
        CARRIAGEHEIGHT: float
        CARRIAGESPRINGFLOOR: bool
        RAILINGHEIGHT: float
        RAILINGOFFS: float
        RAILINGSEGMENTS: int
        RAILINGRADIUS: float
        DIRECTION: int
        LENGTH: float
        LENGTH2: float
        UPPEROFFSET: float
        ...
    class UiCustomization(Interface):
        ...
    class UndefinedClass(Value):
        ...
    class UnsuppliedClass(Value):
        ...
    class Unwrap_UVW(Modifier):
        TEXMAPLIST: MXSWrapperBase
        CHECKERMATERIAL: MXSWrapperBase
        BASEMATERIAL: None
        TEXMAPIDLIST: MXSWrapperBase
        GRIDSNAP: bool
        VERTEXSNAP: bool
        EDGESNAP: bool
        SHOWIMAGEALPHA: bool
        RENDERUV_WIDTH: int
        RENDERUV_HEIGHT: int
        RENDERUV_EDGECOLOR: MXSWrapperBase
        RENDERUV_EDGEALPHA: float
        RENDERUV_SEAMCOLOR: MXSWrapperBase
        RENDERUV_VISIBLEEDGES: bool
        RENDERUV_INVISIBLEEDGES: bool
        RENDERUV_SEAMEDGES: bool
        RENDERUV_SHOWFRAMEBUFFER: bool
        RENDERUV_FORCE2SIDED: bool
        RENDERUV_FILLMODE: int
        RENDERUV_FILLALPHA: float
        RENDERUV_FILLCOLOR: MXSWrapperBase
        RENDERUV_SHOWOVERLAP: bool
        RENDERUV_OVERLAPCOLOR: MXSWrapperBase
        QUICK_MAP_PREVIEW: bool
        QUICK_MAP_ALIGN: int
        BASEMATERIAL_LIST: MXSWrapperBase
        SPLINEMAP_NODE: None
        SPLINEMAP_MANUALSEAMS: bool
        SPLINEMAP_PROJECTIONTYPE: int
        SPLINEMAP_DISPLAY: bool
        SPLINEMAP_USCALE: float
        SPLINEMAP_VSCALE: float
        SPLINEMAP_UOFFSET: float
        SPLINEMAP_VOFFSET: float
        LOCALDISTORTION: bool
        SPLINEMAP_ITERATIONS: int
        SPLINEMAP_RESAMPLECOUNT: int
        SPLINEMAP_ADVANCEMETHOD: int
        TOOLBARVISIBLE: bool
        BUTTONPANEL_VISIBLE: bool
        BUTTONPANEL_WIDTH: int
        BUTTONPANEL_HEIGHT1: int
        BUTTONPANEL_HEIGHT2: int
        WELDONLYSHARED: bool
        GROUPNAME: MXSWrapperBase
        GROUPDENSITY: MXSWrapperBase
        GROUPDISPLAY: bool
        AUTOPIN: bool
        FILTERPIN: bool
        PEELAUTOEDIT: bool
        TEXTURECHECKERMATERIAL: None
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
        HEIGHT: float
        LENGTH: float
        WIDTH: float
        CHANNEL: int
        CAP: bool
        MAPCHANNEL: int
        MAPTYPE: int
        UTILE: float
        VTILE: float
        WTILE: float
        UFLIP: bool
        VFLIP: bool
        WFLIP: bool
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
        MULT_SPIN: float
        VECTOR_MAP_ENABLED: bool
        VECTOR_MAP: None
        VECTOR_MAP_IS_HDR: bool
        METHOD: int
        ...
    class VFB_Rollout_Bottom(RolloutClass):
        ...
    class VFB_Rollout_TopLeft(RolloutClass):
        ...
    class VFB_Rollout_TopRight(RolloutClass):
        ...
    class VIZ_Radiosity(RadiosityEffect):
        RADINITIALQUALITY: float
        RADGLOBALREFINESTEPS: int
        RADSELECTIONREFINESTEPS: int
        RADFILTERING: int
        RADPROCESSOBJECTREFINESTEPS: bool
        RADDISPLAYINVIEWPORT: bool
        RADPROCESSINRENDERONLY: bool
        RADDIRECTFILTERING: int
        MESHINGENABLED: bool
        MESHINGSIZE: float
        USEADAPTIVEMESHING: bool
        MINIMUMMESHSIZE: float
        INITIALMESHSIZE: float
        CONTRASTTHRESHOLD: float
        INCLUDEPOINTLIGHTS: bool
        INCLUDELINEARLIGHTS: bool
        INCLUDEAREALIGHTS: bool
        INCLUDESELFEMITTINGLIGHTS: bool
        SHOOTDIRECTLIGHTS: bool
        INCLUDESKYLIGHT: bool
        MINIMUMSELFEMITTINGSIZE: float
        LIGHTPAINTINGINTENSITY: float
        LIGHTPAINTINGPRESSURE: float
        LIGHTUNITSUSED: int
        RMREGATHER: bool
        RMREUSEDIRECTILLUMINATION: bool
        RMRAYSPERSAMPLE: int
        RMFILTERRADIUS: float
        RMCLAMPENABLED: bool
        RMCLAMPVALUE: float
        RMADAPTIVEENABLED: bool
        RMSAMPLESPACING: int
        RMMINSAMPLESPACING: int
        RMSUBDIVISIONCONTRAST: float
        RMSHOWSAMPLES: bool
        STATNUMFACES: int
        STATREFINEITERATIONS: int
        STATSOLUTIONQUALITY: float
        STATNUMGEOMOBJECTS: int
        STATNUMLIGHTOBJECTS: int
        STATMESHSIZE: float
        ELAPSEDTIME: int
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
        TYPE: int
        ANGLE_X: float
        ANGLE_Y: float
        ANGLE_Z: float
        AXIAL_RADIUS: float
        BEARING: float
        COORD_X: float
        COORD_Y: float
        COORD_Z: float
        FLOAT_X: float
        FLOAT_Y: float
        FLOAT_Z: float
        LATITUDE: float
        PERCENT_X: float
        PERCENT_Y: float
        PERCENT_Z: float
        RADIUS: float
        USE_LENGTH_VARIATION: bool
        USE_DIVERGENCE: bool
        ANGLE_VARIATION: float
        FLOAT_VARIATION: float
        LENGTH_VARIATION: float
        PERCENT_VARIATION: float
        DIVERGENCE: float
        USE_AS_SPEED_VALUE: bool
        UNITS_PER_TYPE: int
        SYNC_TYPE: int
        RANDOM_SEED: int
        USE_E1: bool
        USE_E2: bool
        USE_E3: bool
        USE_E4: bool
        USE_E5: bool
        USE_E6: bool
        USE_E7: bool
        USE_AS_ACCELERATION: bool
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        INPUT_7: None
        ...
    class VectorField(SpacewarpObject):
        LENGTH: float
        WIDTH: float
        HEIGHT: float
        LENSEGS: int
        WIDSEGS: int
        HGTSEGS: int
        SHOWLATTICE: bool
        SHOWRANGE: bool
        SHOWVECTORS: bool
        SHOWSURFSAMPS: bool
        VECSCALE: float
        ICONSIZE: float
        STRENGTH: float
        FALLOFF: float
        DIRECTION: int
        PULL: float
        OBJECT: None
        RANGE: float
        RESOLUTION: int
        FLIPFACES: bool
        BLENDSTART: float
        BLENDFALLOFF: float
        BLENDWIDSEGS: int
        BLENDLENSEGS: int
        BLENDHGTSEGS: int
        ...
    class VectorMap(TextureMap):
        VECTORFILE: str
        FILTER: bool
        MIPMAP: bool
        MONOOUTPUT: int
        RGBOUTPUT: int
        APPLYCROP: bool
        CROPORPLACE: int
        CROP_U: float
        CROP_V: float
        CROP_W: float
        CROP_H: float
        JITTER: bool
        JITTERAMT: float
        ALPHASOURCE: int
        COORDS: MXSWrapperBase
        OUTPUT: MXSWrapperBase
        RESTYPE: int
        FINITERESOLUTION: int
        PATTERNNAME: int
        PATTERNREPEAT: float
        LINEWIDTH: float
        LINECOLOR: MXSWrapperBase
        BACKCOLOR: MXSWrapperBase
        LINECAP: int
        PDF_PAGE: float
        CONTINOUS: bool
        TRANSITION_MODE: int
        TRANSPARENT: bool
        PAGECOLOR: MXSWrapperBase
        TRANSITIONDIR: int
        PREVIEW: bool
        MEMLIMIT: int
        HWBITMAPSIZE: int
        ...
    class Vector_Displacement(TextureMap):
        MULT_SPIN: float
        VECTOR_MAP_ENABLED: bool
        VECTOR_MAP: None
        VECTOR_MAP_IS_HDR: bool
        METHOD: int
        ...
    class Vector_Field(SpacewarpObject):
        LENGTH: float
        WIDTH: float
        HEIGHT: float
        LENSEGS: int
        WIDSEGS: int
        HGTSEGS: int
        SHOWLATTICE: bool
        SHOWRANGE: bool
        SHOWVECTORS: bool
        SHOWSURFSAMPS: bool
        VECSCALE: float
        ICONSIZE: float
        STRENGTH: float
        FALLOFF: float
        DIRECTION: int
        PULL: float
        OBJECT: None
        RANGE: float
        RESOLUTION: int
        FLIPFACES: bool
        BLENDSTART: float
        BLENDFALLOFF: float
        BLENDWIDSEGS: int
        BLENDLENSEGS: int
        BLENDHGTSEGS: int
        ...
    class Vector_Field_Modifier(SpacewarpModifier):
        ...
    class Vector_Map(TextureMap):
        VECTORFILE: str
        FILTER: bool
        MIPMAP: bool
        MONOOUTPUT: int
        RGBOUTPUT: int
        APPLYCROP: bool
        CROPORPLACE: int
        CROP_U: float
        CROP_V: float
        CROP_W: float
        CROP_H: float
        JITTER: bool
        JITTERAMT: float
        ALPHASOURCE: int
        COORDS: MXSWrapperBase
        OUTPUT: MXSWrapperBase
        RESTYPE: int
        FINITERESOLUTION: int
        PATTERNNAME: int
        PATTERNREPEAT: float
        LINEWIDTH: float
        LINECOLOR: MXSWrapperBase
        BACKCOLOR: MXSWrapperBase
        LINECAP: int
        PDF_PAGE: float
        CONTINOUS: bool
        TRANSITION_MODE: int
        TRANSPARENT: bool
        PAGECOLOR: MXSWrapperBase
        TRANSITIONDIR: int
        PREVIEW: bool
        MEMLIMIT: int
        HWBITMAPSIZE: int
        ...
    class VertexColor(TextureMap):
        MAP: int
        SUBID: int
        ...
    class VertexPaint(Modifier):
        IGNOREBACKFACING: bool
        MAPCHANNEL: int
        LAYERMODE: str
        LAYEROPACITY: float
        LAYERISOLATED: bool
        SURVIVECONDENSE: bool
        LIGHTINGMODEL: int
        COLORBY: int
        CASTSHADOWS: bool
        USEMAPS: bool
        USERADIOSITY: bool
        RADIOSITYONLY: bool
        HIDEUNSELSUBOBJS: bool
        RADIOSITYOPTION: int
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
        ENABLED: bool
        EFFECT: int
        DXSTDMAT: bool
        SAVEFXFILE: None
        ...
    class ViewportSSB(Interface):
        ...
    class VisualMSUtil(UtilityPlugin):
        ...
    class Visual_MAXScript(UtilityPlugin):
        ...
    class Vol__Select(Modifier):
        LEVEL: int
        METHOD: int
        TYPE: int
        VOLUME: int
        INVERT: bool
        NODE: None
        TEXTURE: None
        MAP: int
        MAPCHANNEL: int
        MATID: int
        SMGROUP: int
        AUTOFIT: bool
        USEAFFECTREGION: bool
        FALLOFF: float
        PINCH: float
        BUBBLE: float
        ...
    class VolumeHelper(Helper):
        VOLUMETYPE: int
        SIZE: float
        SECTIONRADIUS: float
        MESHNODE: None
        COLOR: MXSWrapperBase
        ...
    class VolumeSelect(Modifier):
        LEVEL: int
        METHOD: int
        TYPE: int
        VOLUME: int
        INVERT: bool
        NODE: None
        TEXTURE: None
        MAP: int
        MAPCHANNEL: int
        MATID: int
        SMGROUP: int
        AUTOFIT: bool
        USEAFFECTREGION: bool
        FALLOFF: float
        PINCH: float
        BUBBLE: float
        ...
    class Volume_Fog(Atmospheric):
        INVERT: int
        SIZE: float
        PHASE: float
        DENSITY: float
        FOG_COLOR: MXSWrapperBase
        FOG_BACKGROUND: int
        EXPONENTIAL: int
        UNIFORMITY: float
        MAX_STEPS: int
        WIND_DIRECTION: int
        WIND_STRENGTH: float
        SOFTEN_GIZMO_EDGES: float
        NOISE_TYPE: int
        LEVELS: float
        LOW_THRESHOLD: float
        HIGH_THRESHOLD: float
        STEP_SIZE: float
        ...
    class Volume_Light(Atmospheric):
        INVERT: int
        SIZE: float
        NOISE_ON: int
        PHASE: float
        SAMPLES: int
        DENSITY: float
        FOG_COLOR: MXSWrapperBase
        EXPONENTIAL: int
        MAX_LIGHT: float
        MIN_LIGHT: float
        ATTEN__START: float
        ATTEN__END: float
        FILTER_SHADOWS: int
        AUTO_SAMPLE: int
        LINK_TO_LIGHT: int
        USE_ATTENUATION_COLOR: int
        ATTENUATION_COLOR_MULTIPLIER: float
        UNIFORMITY: float
        WIND_DIRECTION: int
        WIND_STRENGTH: float
        NOISE_AMOUNT: float
        ATTENUATION_COLOR: MXSWrapperBase
        NOISE_TYPE: int
        LEVELS: float
        LOW_THRESHOLD: float
        HIGH_THRESHOLD: float
        ...
    class Vortex(SpacewarpObject):
        TIMEON: MXSWrapperBase
        TIMEOFF: MXSWrapperBase
        AXIALSTRENGTH: float
        AXIALRANGE: float
        AXIALFALLOFF: float
        AXIALDAMPING: float
        ROTATIONSTRENGTH: float
        ROTATIONRANGE: float
        ROTATIONFALLOFF: float
        ROTATIONDAMPING: float
        RADIALSTRENGTH: float
        RADIALRANGE: float
        RADIALFALLOFF: float
        RADIALDAMPING: float
        TAPERSTRENGTH: float
        TAPERSHAPE: float
        DIRECTION: int
        RANGELESS: bool
        ICONSIZE: float
        ...
    class VortexMod(SpacewarpModifier):
        ...
    class VrmlImp(ImporterPlugin):
        ...
    class Vsp_Gantry(GeometryClass):
        LENGTH: float
        HEIGHT: float
        RADIUS: float
        DIA: float
        XFALL: float
        MATID: int
        LSTYLE: bool
        SIGNALS: bool
        NUMBEROFSIGNALS: int
        SIGNALGAP: float
        FLIPSIGNALS: bool
        SIGNALOFFSET: float
        ...
    class Vsp_GantryNZ(GeometryClass):
        LENGTH: float
        HEIGHT: float
        RADIUS: float
        DIA: float
        XFALL: float
        MATID: int
        LSTYLE: bool
        SIGNALS: bool
        NUMBEROFSIGNALS: int
        SIGNALGAP: float
        FLIPSIGNALS: bool
        SIGNALOFFSET: float
        ...
    class Vsp_GantrySA(GeometryClass):
        LENGTH: float
        HEIGHT: float
        RADIUS: float
        DIA: float
        XFALL: float
        MATID: int
        LSTYLE: bool
        SIGNALS: bool
        NUMBEROFSIGNALS: int
        SIGNALGAP: float
        FLIPSIGNALS: bool
        SIGNALOFFSET: float
        ...
    class Vsp_Lamp(GeometryClass):
        HEIGHT: float
        DEPTH: float
        KINK1: float
        KINK2: float
        MATID: int
        ONOFF: bool
        DIA1: float
        DIA2: float
        RADIUS: float
        ARMLEN: float
        ANGLE: float
        HEADSCALEX: float
        HEADSCALEY: float
        LEFTARM: bool
        RIGHTARM: bool
        ...
    class Vsp_Sign(GeometryClass):
        WIDTH: float
        HEIGHT: float
        TYPE: int
        PHEIGHT: float
        DEPTH: float
        POSTS: int
        EDGEOFF: float
        ...
    class Vsp_Signal(GeometryClass):
        WIDTH: float
        HEIGHT: float
        TYPE: int
        PHEIGHT: float
        DEPTH: float
        POSTS: int
        EDGEOFF: float
        NUMPHASES: int
        CURPHASE: int
        ...
    class Vsp_Symb(GeometryClass):
        WIDTH: float
        HEIGHT: float
        TYPE: int
        ...
    class Vsp_Tree(GeometryClass):
        NFACES: int
        HEIGHT: float
        WIDTH: float
        MATID: int
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
        HEIGHT: float
        WIDTH: float
        JUSTIFICATION: int
        GENERATE_MAPPING_COORDS: int
        ...
    class WallRepelBehavior(ReferenceTarget):
        NAME: str
        REPELGRIDS: MXSWrapperBase
        REPELMETHOD: int
        REPELDIRECTION: int
        USEDISTANCE: bool
        INNERDISTANCE: float
        OUTERDISTANCE: float
        FALLOFF: float
        SHOWDISTANCE: bool
        GRIDSPACING: int
        GRIDEND: bool
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
        ...
    class WallSeekBehavior(ReferenceTarget):
        NAME: str
        SEEKGRID: None
        SEEKMETHOD: int
        SEEKDIRECTION: int
        USEDISTANCE: bool
        INNERDISTANCE: float
        OUTERDISTANCE: float
        FALLOFF: float
        SHOWDISTANCE: bool
        GRIDSPACING: int
        GRIDEND: bool
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
        ...
    class Wall_Repel_Behavior(ReferenceTarget):
        NAME: str
        REPELGRIDS: MXSWrapperBase
        REPELMETHOD: int
        REPELDIRECTION: int
        USEDISTANCE: bool
        INNERDISTANCE: float
        OUTERDISTANCE: float
        FALLOFF: float
        SHOWDISTANCE: bool
        GRIDSPACING: int
        GRIDEND: bool
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
        ...
    class Wall_Seek_Behavior(ReferenceTarget):
        NAME: str
        SEEKGRID: None
        SEEKMETHOD: int
        SEEKDIRECTION: int
        USEDISTANCE: bool
        INNERDISTANCE: float
        OUTERDISTANCE: float
        FALLOFF: float
        SHOWDISTANCE: bool
        GRIDSPACING: int
        GRIDEND: bool
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
        ...
    class WalledRectangle(Shape):
        STEPS: int
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        TYPEIN_X: float
        TYPEIN_Y: float
        TYPEIN_Z: float
        TYPEIN_LENGTH: float
        TYPEIN_WIDTH: float
        TYPEIN_THICKNESS: float
        TYPEIN_RADIUS: float
        TYPEIN_RADIUS2: float
        TYPEIN_CREATIONMETHOD: bool
        WRECT_LENGTH: float
        WRECT_WIDTH: float
        WRECT_THICKNESS: float
        WRECT_RADIUS: float
        WRECT_RADIUS2: float
        WRECT_SYNCCORNERFILLETS: bool
        ...
    class WanderBehavior(ReferenceTarget):
        NAME: str
        PERIOD: int
        PERIODDEVIATION: float
        TURNANGLE: float
        TURNPERIOD: float
        TURNPERIODDEVIATION: float
        SEED: int
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
        ...
    class Wander_Behavior(ReferenceTarget):
        NAME: str
        PERIOD: int
        PERIODDEVIATION: float
        TURNANGLE: float
        TURNPERIOD: float
        TURNPERIODDEVIATION: float
        SEED: int
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
        ...
    class Water(TextureMap):
        NUMWAVESETS: int
        WAVERADIUS: float
        WAVELENMIN: float
        WAVELENMAX: float
        AMPLITUDE: float
        PHASE: float
        DISTRIBUTION: int
        RANDOMSEED: int
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1: None
        MAP2: None
        MAP1ON: bool
        MAP2ON: bool
        COORDS: MXSWrapperBase
        ...
    class Wave(Modifier):
        AMPLITUDE1: float
        AMPLITUDE2: float
        WAVELENGTH: float
        PHASE: float
        DECAY: float
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
        USEAREAWEIGHT: bool
        USEANGLEWEIGHT: bool
        USECONVEXANGLE: bool
        BLENDINGCOEFF: float
        SMOOTHINGCOEFF: float
        RELAXATIONCOEFF: float
        BOUNDARYCOEFF: float
        SMOOTHINGITERLIMIT: int
        USESMOOTHINGGROUPS: bool
        USEHARDEDGEANGLE: bool
        HARDEDGEANGLE: float
        DISPLAYNORMALS: bool
        NORMALLENGTH: float
        SNAPTOLARGESTFACE: bool
        USEUVSEAMS: bool
        UVCHANNELINDEX: int
        USETOTALCOPLANARAREA: bool
        ...
    class Weighted_Normals(Modifier):
        USEAREAWEIGHT: bool
        USEANGLEWEIGHT: bool
        USECONVEXANGLE: bool
        BLENDINGCOEFF: float
        SMOOTHINGCOEFF: float
        RELAXATIONCOEFF: float
        BOUNDARYCOEFF: float
        SMOOTHINGITERLIMIT: int
        USESMOOTHINGGROUPS: bool
        USEHARDEDGEANGLE: bool
        HARDEDGEANGLE: float
        DISPLAYNORMALS: bool
        NORMALLENGTH: float
        SNAPTOLARGESTFACE: bool
        USEUVSEAMS: bool
        UVCHANNELINDEX: int
        USETOTALCOPLANARAREA: bool
        ...
    class WelcomeScreenLaunchCount(Primitive):
        ...
    class WelcomeScreenShowAtStartup(Primitive):
        ...
    class Welder(Modifier):
        THRESHOLD: float
        WELDMETHOD: int
        DONTWELDSELECTEDEDGES: bool
        ...
    class WideFlange(Shape):
        STEPS: int
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        TYPEIN_X: float
        TYPEIN_Y: float
        TYPEIN_Z: float
        TYPEIN_LENGTH: float
        TYPEIN_WIDTH: float
        TYPEIN_THICKNESS: float
        TYPEIN_RADIUS: float
        TYPEIN_CREATIONMETHOD: bool
        WIDE_FLANGE_LENGTH: float
        WIDE_FLANGE_WIDTH: float
        WIDE_FLANGE_THICKNESS: float
        WIDE_FLANGE_RADIUS: float
        ...
    class Wind(SpacewarpObject):
        STRENGTH: float
        DECAY: float
        WINDTYPE: int
        TURBULENCE: float
        FREQUENCY: float
        SCALE: MXSWrapperBase
        ICONSIZE: float
        HOOPSON: bool
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
        SIZE: float
        SUBDIVIDEDOENFORCEQUALITY: bool
        SUBDIVIDEDOSUBDIVIDETRIANGLES: bool
        SHOWALLTRIANGLES: bool
        SUBDIVIDEMAXSTEINERPOINTS: int
        SUBDIVIDEQUADAREARATIO: float
        SUBDIVIDEDIAGONALRATIO: float
        SUBDIVIDENUMBUCKETS: int
        SUBDIVIDEDOFORMQUADS: bool
        SUBDIVIDEREFINEMENTTYPE: int
        MANUALUPDATE: int
        REMESHTYPE: int
        PRESERVEMESHDATA: bool
        PRESERVEDMAPINDEX: int
        PRESERVESHARPEDGESBYANGLE: bool
        PRESERVEDSHARPEDGEANGLE: float
        DELAUNAYSIZE: float
        DELAUNAYRELAXATIONCOEFF: float
        DELAUNAYRELAXATIONITERATIONS: int
        ADAPTIVEEDGELENGTH: float
        ADAPTIVEREGULARITY: float
        ADAPTIVETHRESHOLD: float
        VARIABLECURVATUREEDGELENGTH: float
        VARIABLECURVATUREREGULARITY: float
        VARIABLECURVATURETHRESHOLD: float
        VARIABLECURVATUREVARIABLEDENSITY: float
        VARIABLECURVATUREITERATIONS: int
        VARIABLECURVATURETRANSITION: float
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
        NAME: str
        SPACEWARP: None
        FORCECOLOR: MXSWrapperBase
        DISPLAYFORCE: bool
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
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ZMIN: float
        ZMAX: float
        ZUPDATE: bool
        ...
    class Z_Depth(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ZMIN: float
        ZMAX: float
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
        SAMPLES: int
        SPREAD: float
        SPREAD_CONNECTED: bool
        SPREAD_SHADER: None
        NEAR_CLIP: float
        NEAR_CLIP_CONNECTED: bool
        NEAR_CLIP_SHADER: None
        FAR_CLIP: float
        FAR_CLIP_CONNECTED: bool
        FAR_CLIP_SHADER: None
        FALLOFF: float
        FALLOFF_CONNECTED: bool
        FALLOFF_SHADER: None
        BLACK: MXSWrapperBase
        BLACK_CONNECTED: bool
        BLACK_SHADER: None
        WHITE: MXSWrapperBase
        WHITE_CONNECTED: bool
        WHITE_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        INVERT_NORMALS: bool
        TRACE_SET: str
        INCLUSIVE: bool
        SELF_ONLY: bool
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
        PASSTHROUGH: None
        AOV_INPUT: float
        AOV_INPUT_CONNECTED: bool
        AOV_INPUT_SHADER: None
        AOV_NAME: str
        BLEND_OPACITY: bool
        ...
    class Ai_Aov_Write_Int(Material):
        PASSTHROUGH: None
        AOV_INPUT: int
        AOV_INPUT_CONNECTED: bool
        AOV_INPUT_SHADER: None
        AOV_NAME: str
        ...
    class Ai_Aov_Write_Rgb(Material):
        PASSTHROUGH: None
        AOV_INPUT: MXSWrapperBase
        AOV_INPUT_CONNECTED: bool
        AOV_INPUT_SHADER: None
        AOV_NAME: str
        BLEND_OPACITY: bool
        ...
    class Ai_Aov_Write_Rgba(Material):
        PASSTHROUGH: None
        AOV_INPUT: MXSWrapperBase
        AOV_INPUT_CONNECTED: bool
        AOV_INPUT_SHADER: None
        AOV_NAME: str
        BLEND_OPACITY: bool
        ...
    class Ai_Aov_Write_Vector(Material):
        PASSTHROUGH: None
        AOV_INPUT: MXSWrapperBase
        AOV_INPUT_CONNECTED: bool
        AOV_INPUT_SHADER: None
        AOV_NAME: str
        BLEND_OPACITY: bool
        ...
    class Ai_Atan(TextureMap):
        Y: MXSWrapperBase
        Y_CONNECTED: bool
        Y_SHADER: None
        X: MXSWrapperBase
        X_CONNECTED: bool
        X_SHADER: None
        UNITS: int
        ...
    class Ai_Atmosphere_Volume(Material):
        DENSITY: float
        DENSITY_CONNECTED: bool
        DENSITY_SHADER: None
        SAMPLES: int
        ECCENTRICITY: float
        ECCENTRICITY_CONNECTED: bool
        ECCENTRICITY_SHADER: None
        ATTENUATION: float
        ATTENUATION_CONNECTED: bool
        ATTENUATION_SHADER: None
        AFFECT_CAMERA: float
        AFFECT_CAMERA_CONNECTED: bool
        AFFECT_CAMERA_SHADER: None
        AFFECT_DIFFUSE: float
        AFFECT_DIFFUSE_CONNECTED: bool
        AFFECT_DIFFUSE_SHADER: None
        AFFECT_SPECULAR: float
        AFFECT_SPECULAR_CONNECTED: bool
        AFFECT_SPECULAR_SHADER: None
        RGB_DENSITY: MXSWrapperBase
        RGB_DENSITY_CONNECTED: bool
        RGB_DENSITY_SHADER: None
        RGB_ATTENUATION: MXSWrapperBase
        RGB_ATTENUATION_CONNECTED: bool
        RGB_ATTENUATION_SHADER: None
        ...
    class Ai_Barndoor(TextureMap):
        ...
    class Ai_Blackbody(TextureMap):
        TEMPERATURE: float
        TEMPERATURE_CONNECTED: bool
        TEMPERATURE_SHADER: None
        NORMALIZE: bool
        INTENSITY: float
        INTENSITY_CONNECTED: bool
        INTENSITY_SHADER: None
        ...
    class Ai_Blackman_Harris_Filter(TextureMap):
        ...
    class Ai_Box_Filter(TextureMap):
        ...
    class Ai_Bump2D(TextureMap):
        BUMP_MAP: float
        BUMP_MAP_CONNECTED: bool
        BUMP_MAP_SHADER: None
        BUMP_HEIGHT: float
        BUMP_HEIGHT_CONNECTED: bool
        BUMP_HEIGHT_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        ...
    class Ai_Bump3D(TextureMap):
        BUMP_MAP: float
        BUMP_MAP_CONNECTED: bool
        BUMP_MAP_SHADER: None
        BUMP_HEIGHT: float
        BUMP_HEIGHT_CONNECTED: bool
        BUMP_HEIGHT_SHADER: None
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
        PROJECTION_COLOR: MXSWrapperBase
        PROJECTION_COLOR_CONNECTED: bool
        PROJECTION_COLOR_SHADER: None
        OFFSCREEN_COLOR: MXSWrapperBase
        OFFSCREEN_COLOR_CONNECTED: bool
        OFFSCREEN_COLOR_SHADER: None
        MASK: float
        MASK_CONNECTED: bool
        MASK_SHADER: None
        CAMERA: None
        CAMERA_CONNECTED: bool
        CAMERA_SHADER: None
        ASPECT_RATIO: float
        FRONT_FACING: bool
        BACK_FACING: bool
        USE_SHADING_NORMAL: bool
        COORD_SPACE: int
        PREF_NAME: str
        P: MXSWrapperBase
        P_CONNECTED: bool
        P_SHADER: None
        ...
    class Ai_Car_Paint(Material):
        BASE: float
        BASE_CONNECTED: bool
        BASE_SHADER: None
        BASE_COLOR: MXSWrapperBase
        BASE_COLOR_CONNECTED: bool
        BASE_COLOR_SHADER: None
        BASE_ROUGHNESS: float
        BASE_ROUGHNESS_CONNECTED: bool
        BASE_ROUGHNESS_SHADER: None
        SPECULAR: float
        SPECULAR_CONNECTED: bool
        SPECULAR_SHADER: None
        SPECULAR_COLOR: MXSWrapperBase
        SPECULAR_COLOR_CONNECTED: bool
        SPECULAR_COLOR_SHADER: None
        SPECULAR_FLIP_FLOP: MXSWrapperBase
        SPECULAR_FLIP_FLOP_CONNECTED: bool
        SPECULAR_FLIP_FLOP_SHADER: None
        SPECULAR_LIGHT_FACING: MXSWrapperBase
        SPECULAR_LIGHT_FACING_CONNECTED: bool
        SPECULAR_LIGHT_FACING_SHADER: None
        SPECULAR_FALLOFF: float
        SPECULAR_FALLOFF_CONNECTED: bool
        SPECULAR_FALLOFF_SHADER: None
        SPECULAR_ROUGHNESS: float
        SPECULAR_ROUGHNESS_CONNECTED: bool
        SPECULAR_ROUGHNESS_SHADER: None
        SPECULAR_IOR: float
        SPECULAR_IOR_CONNECTED: bool
        SPECULAR_IOR_SHADER: None
        TRANSMISSION_COLOR: MXSWrapperBase
        TRANSMISSION_COLOR_CONNECTED: bool
        TRANSMISSION_COLOR_SHADER: None
        FLAKE_COLOR: MXSWrapperBase
        FLAKE_COLOR_CONNECTED: bool
        FLAKE_COLOR_SHADER: None
        FLAKE_FLIP_FLOP: MXSWrapperBase
        FLAKE_FLIP_FLOP_CONNECTED: bool
        FLAKE_FLIP_FLOP_SHADER: None
        FLAKE_LIGHT_FACING: MXSWrapperBase
        FLAKE_LIGHT_FACING_CONNECTED: bool
        FLAKE_LIGHT_FACING_SHADER: None
        FLAKE_FALLOFF: float
        FLAKE_FALLOFF_CONNECTED: bool
        FLAKE_FALLOFF_SHADER: None
        FLAKE_ROUGHNESS: float
        FLAKE_ROUGHNESS_CONNECTED: bool
        FLAKE_ROUGHNESS_SHADER: None
        FLAKE_IOR: float
        FLAKE_IOR_CONNECTED: bool
        FLAKE_IOR_SHADER: None
        FLAKE_SCALE: float
        FLAKE_SCALE_CONNECTED: bool
        FLAKE_SCALE_SHADER: None
        FLAKE_DENSITY: float
        FLAKE_DENSITY_CONNECTED: bool
        FLAKE_DENSITY_SHADER: None
        FLAKE_LAYERS: int
        FLAKE_LAYERS_CONNECTED: bool
        FLAKE_LAYERS_SHADER: None
        FLAKE_NORMAL_RANDOMIZE: float
        FLAKE_NORMAL_RANDOMIZE_CONNECTED: bool
        FLAKE_NORMAL_RANDOMIZE_SHADER: None
        FLAKE_COORD_SPACE: int
        PREF_NAME: str
        COAT: float
        COAT_CONNECTED: bool
        COAT_SHADER: None
        COAT_COLOR: MXSWrapperBase
        COAT_COLOR_CONNECTED: bool
        COAT_COLOR_SHADER: None
        COAT_ROUGHNESS: float
        COAT_ROUGHNESS_CONNECTED: bool
        COAT_ROUGHNESS_SHADER: None
        COAT_IOR: float
        COAT_IOR_CONNECTED: bool
        COAT_IOR_SHADER: None
        COAT_NORMAL: MXSWrapperBase
        COAT_NORMAL_CONNECTED: bool
        COAT_NORMAL_SHADER: None
        ...
    class Ai_Catrom_Filter(TextureMap):
        ...
    class Ai_Cell_Noise(TextureMap):
        PATTERN: int
        ADDITIVE: bool
        OCTAVES: int
        RANDOMNESS: float
        RANDOMNESS_CONNECTED: bool
        RANDOMNESS_SHADER: None
        LACUNARITY: float
        LACUNARITY_CONNECTED: bool
        LACUNARITY_SHADER: None
        AMPLITUDE: float
        AMPLITUDE_CONNECTED: bool
        AMPLITUDE_SHADER: None
        SCALE: MXSWrapperBase
        SCALE_CONNECTED: bool
        SCALE_SHADER: None
        OFFSET: MXSWrapperBase
        OFFSET_CONNECTED: bool
        OFFSET_SHADER: None
        COORD_SPACE: int
        PREF_NAME: str
        P: MXSWrapperBase
        P_CONNECTED: bool
        P_SHADER: None
        TIME: float
        TIME_CONNECTED: bool
        TIME_SHADER: None
        COLOR: MXSWrapperBase
        COLOR_CONNECTED: bool
        COLOR_SHADER: None
        PALETTE: MXSWrapperBase
        PALETTE_CONNECTED: bool
        PALETTE_SHADER: None
        DENSITY: float
        DENSITY_CONNECTED: bool
        DENSITY_SHADER: None
        ...
    class Ai_Checkerboard(TextureMap):
        COLOR1: MXSWrapperBase
        COLOR1_CONNECTED: bool
        COLOR1_SHADER: None
        COLOR2: MXSWrapperBase
        COLOR2_CONNECTED: bool
        COLOR2_SHADER: None
        U_FREQUENCY: float
        U_FREQUENCY_CONNECTED: bool
        U_FREQUENCY_SHADER: None
        V_FREQUENCY: float
        V_FREQUENCY_CONNECTED: bool
        V_FREQUENCY_SHADER: None
        U_OFFSET: float
        U_OFFSET_CONNECTED: bool
        U_OFFSET_SHADER: None
        V_OFFSET: float
        V_OFFSET_CONNECTED: bool
        V_OFFSET_SHADER: None
        CONTRAST: float
        CONTRAST_CONNECTED: bool
        CONTRAST_SHADER: None
        FILTER_STRENGTH: float
        FILTER_STRENGTH_CONNECTED: bool
        FILTER_STRENGTH_SHADER: None
        FILTER_OFFSET: float
        FILTER_OFFSET_CONNECTED: bool
        FILTER_OFFSET_SHADER: None
        UVSET: str
        ...
    class Ai_Clamp(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        MODE: int
        MODE_CONNECTED: bool
        MODE_SHADER: None
        MIN: float
        MIN_CONNECTED: bool
        MIN_SHADER: None
        MAX: float
        MAX_CONNECTED: bool
        MAX_SHADER: None
        MIN_COLOR: MXSWrapperBase
        MIN_COLOR_CONNECTED: bool
        MIN_COLOR_SHADER: None
        MAX_COLOR: MXSWrapperBase
        MAX_COLOR_CONNECTED: bool
        MAX_COLOR_SHADER: None
        ...
    class Ai_Clip_Geo(Material):
        INTERSECTION: None
        TRACE_SET: str
        INCLUSIVE: bool
        ...
    class Ai_Closest_Filter(TextureMap):
        ...
    class Ai_Collection(TextureMap):
        ...
    class Ai_Color_Convert(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        FROM: int
        TO: int
        ...
    class Ai_Color_Correct(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ALPHA_IS_LUMINANCE: bool
        ALPHA_MULTIPLY: float
        ALPHA_MULTIPLY_CONNECTED: bool
        ALPHA_MULTIPLY_SHADER: None
        ALPHA_ADD: float
        ALPHA_ADD_CONNECTED: bool
        ALPHA_ADD_SHADER: None
        INVERT: bool
        INVERT_ALPHA: bool
        GAMMA: float
        GAMMA_CONNECTED: bool
        GAMMA_SHADER: None
        HUE_SHIFT: float
        HUE_SHIFT_CONNECTED: bool
        HUE_SHIFT_SHADER: None
        SATURATION: float
        SATURATION_CONNECTED: bool
        SATURATION_SHADER: None
        CONTRAST: float
        CONTRAST_CONNECTED: bool
        CONTRAST_SHADER: None
        CONTRAST_PIVOT: float
        CONTRAST_PIVOT_CONNECTED: bool
        CONTRAST_PIVOT_SHADER: None
        EXPOSURE: float
        EXPOSURE_CONNECTED: bool
        EXPOSURE_SHADER: None
        MULTIPLY: MXSWrapperBase
        MULTIPLY_CONNECTED: bool
        MULTIPLY_SHADER: None
        ADD: MXSWrapperBase
        ADD_CONNECTED: bool
        ADD_SHADER: None
        MASK: float
        MASK_CONNECTED: bool
        MASK_SHADER: None
        ...
    class Ai_Color_Jitter(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        DATA_INPUT: int
        DATA_INPUT_CONNECTED: bool
        DATA_INPUT_SHADER: None
        DATA_GAIN_MIN: float
        DATA_GAIN_MIN_CONNECTED: bool
        DATA_GAIN_MIN_SHADER: None
        DATA_GAIN_MAX: float
        DATA_GAIN_MAX_CONNECTED: bool
        DATA_GAIN_MAX_SHADER: None
        DATA_HUE_MIN: float
        DATA_HUE_MIN_CONNECTED: bool
        DATA_HUE_MIN_SHADER: None
        DATA_HUE_MAX: float
        DATA_HUE_MAX_CONNECTED: bool
        DATA_HUE_MAX_SHADER: None
        DATA_SATURATION_MIN: float
        DATA_SATURATION_MIN_CONNECTED: bool
        DATA_SATURATION_MIN_SHADER: None
        DATA_SATURATION_MAX: float
        DATA_SATURATION_MAX_CONNECTED: bool
        DATA_SATURATION_MAX_SHADER: None
        DATA_SEED: int
        DATA_SEED_CONNECTED: bool
        DATA_SEED_SHADER: None
        PROC_GAIN_MIN: float
        PROC_GAIN_MIN_CONNECTED: bool
        PROC_GAIN_MIN_SHADER: None
        PROC_GAIN_MAX: float
        PROC_GAIN_MAX_CONNECTED: bool
        PROC_GAIN_MAX_SHADER: None
        PROC_HUE_MIN: float
        PROC_HUE_MIN_CONNECTED: bool
        PROC_HUE_MIN_SHADER: None
        PROC_HUE_MAX: float
        PROC_HUE_MAX_CONNECTED: bool
        PROC_HUE_MAX_SHADER: None
        PROC_SATURATION_MIN: float
        PROC_SATURATION_MIN_CONNECTED: bool
        PROC_SATURATION_MIN_SHADER: None
        PROC_SATURATION_MAX: float
        PROC_SATURATION_MAX_CONNECTED: bool
        PROC_SATURATION_MAX_SHADER: None
        PROC_SEED: int
        PROC_SEED_CONNECTED: bool
        PROC_SEED_SHADER: None
        OBJ_GAIN_MIN: float
        OBJ_GAIN_MIN_CONNECTED: bool
        OBJ_GAIN_MIN_SHADER: None
        OBJ_GAIN_MAX: float
        OBJ_GAIN_MAX_CONNECTED: bool
        OBJ_GAIN_MAX_SHADER: None
        OBJ_HUE_MIN: float
        OBJ_HUE_MIN_CONNECTED: bool
        OBJ_HUE_MIN_SHADER: None
        OBJ_HUE_MAX: float
        OBJ_HUE_MAX_CONNECTED: bool
        OBJ_HUE_MAX_SHADER: None
        OBJ_SATURATION_MIN: float
        OBJ_SATURATION_MIN_CONNECTED: bool
        OBJ_SATURATION_MIN_SHADER: None
        OBJ_SATURATION_MAX: float
        OBJ_SATURATION_MAX_CONNECTED: bool
        OBJ_SATURATION_MAX_SHADER: None
        OBJ_SEED: int
        OBJ_SEED_CONNECTED: bool
        OBJ_SEED_SHADER: None
        FACE_GAIN_MIN: float
        FACE_GAIN_MIN_CONNECTED: bool
        FACE_GAIN_MIN_SHADER: None
        FACE_GAIN_MAX: float
        FACE_GAIN_MAX_CONNECTED: bool
        FACE_GAIN_MAX_SHADER: None
        FACE_HUE_MIN: float
        FACE_HUE_MIN_CONNECTED: bool
        FACE_HUE_MIN_SHADER: None
        FACE_HUE_MAX: float
        FACE_HUE_MAX_CONNECTED: bool
        FACE_HUE_MAX_SHADER: None
        FACE_SATURATION_MIN: float
        FACE_SATURATION_MIN_CONNECTED: bool
        FACE_SATURATION_MIN_SHADER: None
        FACE_SATURATION_MAX: float
        FACE_SATURATION_MAX_CONNECTED: bool
        FACE_SATURATION_MAX_SHADER: None
        FACE_SEED: int
        FACE_SEED_CONNECTED: bool
        FACE_SEED_SHADER: None
        FACE_MODE: int
        ...
    class Ai_Compare(TextureMap):
        TEST: int
        INPUT1: float
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        INPUT2: float
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
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
        SIDECAR_MANIFESTS: bool
        SIDECAR_MANIFESTS_CONNECTED: bool
        SIDECAR_MANIFESTS_SHADER: None
        CRYPTOMATTE_DEPTH: int
        CRYPTOMATTE_DEPTH_CONNECTED: bool
        CRYPTOMATTE_DEPTH_SHADER: None
        STRIP_OBJ_NAMESPACES: bool
        STRIP_OBJ_NAMESPACES_CONNECTED: bool
        STRIP_OBJ_NAMESPACES_SHADER: None
        STRIP_MAT_NAMESPACES: bool
        STRIP_MAT_NAMESPACES_CONNECTED: bool
        STRIP_MAT_NAMESPACES_SHADER: None
        AOV_CRYPTO_ASSET: str
        AOV_CRYPTO_ASSET_CONNECTED: bool
        AOV_CRYPTO_ASSET_SHADER: None
        AOV_CRYPTO_OBJECT: str
        AOV_CRYPTO_OBJECT_CONNECTED: bool
        AOV_CRYPTO_OBJECT_SHADER: None
        AOV_CRYPTO_MATERIAL: str
        AOV_CRYPTO_MATERIAL_CONNECTED: bool
        AOV_CRYPTO_MATERIAL_SHADER: None
        PREVIEW_IN_EXR: bool
        PREVIEW_IN_EXR_CONNECTED: bool
        PREVIEW_IN_EXR_SHADER: None
        PROCESS_MAYA: bool
        PROCESS_MAYA_CONNECTED: bool
        PROCESS_MAYA_SHADER: None
        PROCESS_PATHS: bool
        PROCESS_PATHS_CONNECTED: bool
        PROCESS_PATHS_SHADER: None
        PROCESS_OBJ_PATH_PIPES: bool
        PROCESS_OBJ_PATH_PIPES_CONNECTED: bool
        PROCESS_OBJ_PATH_PIPES_SHADER: None
        PROCESS_MAT_PATH_PIPES: bool
        PROCESS_MAT_PATH_PIPES_CONNECTED: bool
        PROCESS_MAT_PATH_PIPES_SHADER: None
        PROCESS_LEGACY: bool
        PROCESS_LEGACY_CONNECTED: bool
        PROCESS_LEGACY_SHADER: None
        USER_CRYPTO_AOV_0: str
        USER_CRYPTO_AOV_0_CONNECTED: bool
        USER_CRYPTO_AOV_0_SHADER: None
        USER_CRYPTO_SRC_0: str
        USER_CRYPTO_SRC_0_CONNECTED: bool
        USER_CRYPTO_SRC_0_SHADER: None
        USER_CRYPTO_AOV_1: str
        USER_CRYPTO_AOV_1_CONNECTED: bool
        USER_CRYPTO_AOV_1_SHADER: None
        USER_CRYPTO_SRC_1: str
        USER_CRYPTO_SRC_1_CONNECTED: bool
        USER_CRYPTO_SRC_1_SHADER: None
        USER_CRYPTO_AOV_2: str
        USER_CRYPTO_AOV_2_CONNECTED: bool
        USER_CRYPTO_AOV_2_SHADER: None
        USER_CRYPTO_SRC_2: str
        USER_CRYPTO_SRC_2_CONNECTED: bool
        USER_CRYPTO_SRC_2_SHADER: None
        USER_CRYPTO_AOV_3: str
        USER_CRYPTO_AOV_3_CONNECTED: bool
        USER_CRYPTO_AOV_3_SHADER: None
        USER_CRYPTO_SRC_3: str
        USER_CRYPTO_SRC_3_CONNECTED: bool
        USER_CRYPTO_SRC_3_SHADER: None
        ...
    class Ai_Cryptomatte_Filter(TextureMap):
        ...
    class Ai_Curvature(TextureMap):
        OUTPUT: int
        SAMPLES: int
        RADIUS: float
        RADIUS_CONNECTED: bool
        RADIUS_SHADER: None
        SPREAD: float
        SPREAD_CONNECTED: bool
        SPREAD_SHADER: None
        THRESHOLD: float
        THRESHOLD_CONNECTED: bool
        THRESHOLD_SHADER: None
        BIAS: float
        BIAS_CONNECTED: bool
        BIAS_SHADER: None
        MULTIPLY: float
        MULTIPLY_CONNECTED: bool
        MULTIPLY_SHADER: None
        TRACE_SET: str
        INCLUSIVE: bool
        SELF_ONLY: bool
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
        LINEAR: bool
        INVERT: bool
        ...
    class Ai_Farthest_Filter(TextureMap):
        ...
    class Ai_Flakes(TextureMap):
        SCALE: float
        SCALE_CONNECTED: bool
        SCALE_SHADER: None
        DENSITY: float
        DENSITY_CONNECTED: bool
        DENSITY_SHADER: None
        STEP: float
        STEP_CONNECTED: bool
        STEP_SHADER: None
        DEPTH: float
        DEPTH_CONNECTED: bool
        DEPTH_SHADER: None
        IOR: float
        IOR_CONNECTED: bool
        IOR_SHADER: None
        NORMAL_RANDOMIZE: float
        NORMAL_RANDOMIZE_CONNECTED: bool
        NORMAL_RANDOMIZE_SHADER: None
        COORD_SPACE: int
        PREF_NAME: str
        OUTPUT_SPACE: int
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
        R: float
        R_CONNECTED: bool
        R_SHADER: None
        G: float
        G_CONNECTED: bool
        G_SHADER: None
        B: float
        B_CONNECTED: bool
        B_SHADER: None
        ...
    class Ai_Float_To_Rgba(TextureMap):
        R: float
        R_CONNECTED: bool
        R_SHADER: None
        G: float
        G_CONNECTED: bool
        G_SHADER: None
        B: float
        B_CONNECTED: bool
        B_SHADER: None
        A: float
        A_CONNECTED: bool
        A_SHADER: None
        ...
    class Ai_Fog(Material):
        DISTANCE: float
        DISTANCE_CONNECTED: bool
        DISTANCE_SHADER: None
        HEIGHT: float
        HEIGHT_CONNECTED: bool
        HEIGHT_SHADER: None
        COLOR: MXSWrapperBase
        COLOR_CONNECTED: bool
        COLOR_SHADER: None
        GROUND_POINT: MXSWrapperBase
        GROUND_POINT_CONNECTED: bool
        GROUND_POINT_SHADER: None
        GROUND_NORMAL: MXSWrapperBase
        GROUND_NORMAL_CONNECTED: bool
        GROUND_NORMAL_SHADER: None
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
        FILENAME: str
        IMAGE_FRAME_NUMBER: int
        COLOR_SPACE: int
        FILTER: int
        MIPMAP_BIAS: int
        SINGLE_CHANNEL: bool
        START_CHANNEL: int
        SWRAP: int
        TWRAP: int
        SSCALE: float
        TSCALE: float
        SFLIP: bool
        TFLIP: bool
        SOFFSET: float
        TOFFSET: float
        SWAP_ST: bool
        UVCOORDS: MXSWrapperBase
        UVCOORDS_CONNECTED: bool
        UVCOORDS_SHADER: None
        UVSET: int
        MULTIPLY: MXSWrapperBase
        MULTIPLY_CONNECTED: bool
        MULTIPLY_SHADER: None
        OFFSET: MXSWrapperBase
        OFFSET_CONNECTED: bool
        OFFSET_SHADER: None
        IGNORE_MISSING_TEXTURES: bool
        MISSING_TEXTURE_COLOR: MXSWrapperBase
        MISSING_TEXTURE_COLOR_CONNECTED: bool
        MISSING_TEXTURE_COLOR_SHADER: None
        ...
    class Ai_Imager_Color_Correct(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ENABLE: bool
        LAYER_SELECTION: str
        MAIN_SATURATION: float
        MAIN_CONTRAST: float
        MAIN_GAMMA: float
        MAIN_GAIN: MXSWrapperBase
        MAIN_OFFSET: MXSWrapperBase
        SHADOWS_SATURATION: float
        SHADOWS_CONTRAST: float
        SHADOWS_GAMMA: float
        SHADOWS_GAIN: MXSWrapperBase
        SHADOWS_OFFSET: MXSWrapperBase
        MIDTONES_SATURATION: float
        MIDTONES_CONTRAST: float
        MIDTONES_GAMMA: float
        MIDTONES_GAIN: MXSWrapperBase
        MIDTONES_OFFSET: MXSWrapperBase
        HIGHLIGHTS_SATURATION: float
        HIGHLIGHTS_CONTRAST: float
        HIGHLIGHTS_GAMMA: float
        HIGHLIGHTS_GAIN: MXSWrapperBase
        HIGHLIGHTS_OFFSET: MXSWrapperBase
        ...
    class Ai_Imager_Exposure(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ENABLE: bool
        LAYER_SELECTION: str
        EXPOSURE: float
        ...
    class Ai_Imager_Lens_Effects(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ENABLE: bool
        LAYER_SELECTION: str
        VIGNETTING: float
        ...
    class Ai_Imager_Tonemap(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ENABLE: bool
        LAYER_SELECTION: str
        MODE: int
        FILMIC_TOE_STRENGTH: float
        FILMIC_TOE_LENGTH: float
        FILMIC_SHOULDER_STRENGTH: float
        FILMIC_SHOULDER_LENGTH: float
        FILMIC_SHOULDER_ANGLE: float
        REINHARD_HIGHLIGHTS: float
        REINHARD_SHADOWS: float
        PRESERVE_SATURATION: bool
        GAMMA: float
        ...
    class Ai_Imager_White_Balance(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ENABLE: bool
        LAYER_SELECTION: str
        MODE: int
        TEMPERATURE: float
        ILLUMINANT: int
        CUSTOM: MXSWrapperBase
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
        KD_CONNECTED: bool
        KD_SHADER: None
        KD_COLOR: MXSWrapperBase
        KD_COLOR_CONNECTED: bool
        KD_COLOR_SHADER: None
        OPACITY: MXSWrapperBase
        OPACITY_CONNECTED: bool
        OPACITY_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        ...
    class Ai_Layer_Float(TextureMap):
        ENABLE1: bool
        NAME1: str
        INPUT1: float
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        MIX1: float
        MIX1_CONNECTED: bool
        MIX1_SHADER: None
        ENABLE2: bool
        NAME2: str
        INPUT2: float
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        MIX2: float
        MIX2_CONNECTED: bool
        MIX2_SHADER: None
        ENABLE3: bool
        NAME3: str
        INPUT3: float
        INPUT3_CONNECTED: bool
        INPUT3_SHADER: None
        MIX3: float
        MIX3_CONNECTED: bool
        MIX3_SHADER: None
        ENABLE4: bool
        NAME4: str
        INPUT4: float
        INPUT4_CONNECTED: bool
        INPUT4_SHADER: None
        MIX4: float
        MIX4_CONNECTED: bool
        MIX4_SHADER: None
        ENABLE5: bool
        NAME5: str
        INPUT5: float
        INPUT5_CONNECTED: bool
        INPUT5_SHADER: None
        MIX5: float
        MIX5_CONNECTED: bool
        MIX5_SHADER: None
        ENABLE6: bool
        NAME6: str
        INPUT6: float
        INPUT6_CONNECTED: bool
        INPUT6_SHADER: None
        MIX6: float
        MIX6_CONNECTED: bool
        MIX6_SHADER: None
        ENABLE7: bool
        NAME7: str
        INPUT7: float
        INPUT7_CONNECTED: bool
        INPUT7_SHADER: None
        MIX7: float
        MIX7_CONNECTED: bool
        MIX7_SHADER: None
        ENABLE8: bool
        NAME8: str
        INPUT8: float
        INPUT8_CONNECTED: bool
        INPUT8_SHADER: None
        MIX8: float
        MIX8_CONNECTED: bool
        MIX8_SHADER: None
        ...
    class Ai_Layer_Rgba(TextureMap):
        ENABLE1: bool
        NAME1: str
        INPUT1: MXSWrapperBase
        INPUT1_CONNECTED: bool
        INPUT1_SHADER: None
        MIX1: float
        MIX1_CONNECTED: bool
        MIX1_SHADER: None
        OPERATION1: int
        ALPHA_OPERATION1: int
        ENABLE2: bool
        NAME2: str
        INPUT2: MXSWrapperBase
        INPUT2_CONNECTED: bool
        INPUT2_SHADER: None
        MIX2: float
        MIX2_CONNECTED: bool
        MIX2_SHADER: None
        OPERATION2: int
        ALPHA_OPERATION2: int
        ENABLE3: bool
        NAME3: str
        INPUT3: MXSWrapperBase
        INPUT3_CONNECTED: bool
        INPUT3_SHADER: None
        MIX3: float
        MIX3_CONNECTED: bool
        MIX3_SHADER: None
        OPERATION3: int
        ALPHA_OPERATION3: int
        ENABLE4: bool
        NAME4: str
        INPUT4: MXSWrapperBase
        INPUT4_CONNECTED: bool
        INPUT4_SHADER: None
        MIX4: float
        MIX4_CONNECTED: bool
        MIX4_SHADER: None
        OPERATION4: int
        ALPHA_OPERATION4: int
        ENABLE5: bool
        NAME5: str
        INPUT5: MXSWrapperBase
        INPUT5_CONNECTED: bool
        INPUT5_SHADER: None
        MIX5: float
        MIX5_CONNECTED: bool
        MIX5_SHADER: None
        OPERATION5: int
        ALPHA_OPERATION5: int
        ENABLE6: bool
        NAME6: str
        INPUT6: MXSWrapperBase
        INPUT6_CONNECTED: bool
        INPUT6_SHADER: None
        MIX6: float
        MIX6_CONNECTED: bool
        MIX6_SHADER: None
        OPERATION6: int
        ALPHA_OPERATION6: int
        ENABLE7: bool
        NAME7: str
        INPUT7: MXSWrapperBase
        INPUT7_CONNECTED: bool
        INPUT7_SHADER: None
        MIX7: float
        MIX7_CONNECTED: bool
        MIX7_SHADER: None
        OPERATION7: int
        ALPHA_OPERATION7: int
        ENABLE8: bool
        NAME8: str
        INPUT8: MXSWrapperBase
        INPUT8_CONNECTED: bool
        INPUT8_SHADER: None
        MIX8: float
        MIX8_CONNECTED: bool
        MIX8_SHADER: None
        OPERATION8: int
        ALPHA_OPERATION8: int
        CLAMP: bool
        ...
    class Ai_Layer_Shader(Material):
        ENABLE1: bool
        NAME1: str
        INPUT1: None
        MIX1: float
        MIX1_CONNECTED: bool
        MIX1_SHADER: None
        ENABLE2: bool
        NAME2: str
        INPUT2: None
        MIX2: float
        MIX2_CONNECTED: bool
        MIX2_SHADER: None
        ENABLE3: bool
        NAME3: str
        INPUT3: None
        MIX3: float
        MIX3_CONNECTED: bool
        MIX3_SHADER: None
        ENABLE4: bool
        NAME4: str
        INPUT4: None
        MIX4: float
        MIX4_CONNECTED: bool
        MIX4_SHADER: None
        ENABLE5: bool
        NAME5: str
        INPUT5: None
        MIX5: float
        MIX5_CONNECTED: bool
        MIX5_SHADER: None
        ENABLE6: bool
        NAME6: str
        INPUT6: None
        MIX6: float
        MIX6_CONNECTED: bool
        MIX6_SHADER: None
        ENABLE7: bool
        NAME7: str
        INPUT7: None
        MIX7: float
        MIX7_CONNECTED: bool
        MIX7_SHADER: None
        ENABLE8: bool
        NAME8: str
        INPUT8: None
        MIX8: float
        MIX8_CONNECTED: bool
        MIX8_SHADER: None
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
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        BASE: MXSWrapperBase
        BASE_CONNECTED: bool
        BASE_SHADER: None
        ...
    class Ai_Materialx(TextureMap):
        ...
    class Ai_Matrix_Interpolate(TextureMap):
        ...
    class Ai_Matrix_Multiply_Vector(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        TYPE: int
        MATRIX: MXSWrapperBase
        MATRIX_CONNECTED: bool
        MATRIX_SHADER: None
        ...
    class Ai_Matrix_Transform(TextureMap):
        TRANSFORM_ORDER: int
        ROTATION_TYPE: int
        UNITS: int
        ROTATION_ORDER: int
        ROTATION: MXSWrapperBase
        ROTATION_CONNECTED: bool
        ROTATION_SHADER: None
        AXIS: MXSWrapperBase
        AXIS_CONNECTED: bool
        AXIS_SHADER: None
        ANGLE: float
        ANGLE_CONNECTED: bool
        ANGLE_SHADER: None
        TRANSLATE: MXSWrapperBase
        TRANSLATE_CONNECTED: bool
        TRANSLATE_SHADER: None
        SCALE: MXSWrapperBase
        SCALE_CONNECTED: bool
        SCALE_SHADER: None
        PIVOT: MXSWrapperBase
        PIVOT_CONNECTED: bool
        PIVOT_SHADER: None
        ...
    class Ai_Matte(Material):
        PASSTHROUGH: None
        COLOR: MXSWrapperBase
        COLOR_CONNECTED: bool
        COLOR_SHADER: None
        OPACITY: MXSWrapperBase
        OPACITY_CONNECTED: bool
        OPACITY_SHADER: None
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
        MODE: int
        MIX: float
        MIX_CONNECTED: bool
        MIX_SHADER: None
        ADD_TRANSPARENCY: bool
        SHADER1: None
        SHADER2: None
        ...
    class Ai_Modulo(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        DIVISOR: MXSWrapperBase
        DIVISOR_CONNECTED: bool
        DIVISOR_SHADER: None
        ...
    class Ai_Motion_Vector(TextureMap):
        RAW: bool
        TIME0: float
        TIME1: float
        MAX_DISPLACE: float
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
        OCTAVES: int
        DISTORTION: float
        DISTORTION_CONNECTED: bool
        DISTORTION_SHADER: None
        LACUNARITY: float
        LACUNARITY_CONNECTED: bool
        LACUNARITY_SHADER: None
        AMPLITUDE: float
        AMPLITUDE_CONNECTED: bool
        AMPLITUDE_SHADER: None
        SCALE: MXSWrapperBase
        SCALE_CONNECTED: bool
        SCALE_SHADER: None
        OFFSET: MXSWrapperBase
        OFFSET_CONNECTED: bool
        OFFSET_SHADER: None
        COORD_SPACE: int
        PREF_NAME: str
        P: MXSWrapperBase
        P_CONNECTED: bool
        P_SHADER: None
        TIME: float
        TIME_CONNECTED: bool
        TIME_SHADER: None
        COLOR1: MXSWrapperBase
        COLOR1_CONNECTED: bool
        COLOR1_SHADER: None
        COLOR2: MXSWrapperBase
        COLOR2_CONNECTED: bool
        COLOR2_SHADER: None
        MODE: int
        ...
    class Ai_Normal_Map(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        TANGENT: MXSWrapperBase
        TANGENT_CONNECTED: bool
        TANGENT_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        ORDER: int
        INVERT_X: bool
        INVERT_Y: bool
        INVERT_Z: bool
        COLOR_TO_SIGNED: bool
        TANGENT_SPACE: bool
        STRENGTH: float
        STRENGTH_CONNECTED: bool
        STRENGTH_SHADER: None
        ...
    class Ai_Normalize(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Osl(TextureMap):
        ...
    class Ai_Passthrough(Material):
        PASSTHROUGH: None
        EVAL1: None
        EVAL2: None
        EVAL3: None
        EVAL4: None
        EVAL5: None
        EVAL6: None
        EVAL7: None
        EVAL8: None
        EVAL9: None
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
        EVAL20: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        ...
    class Ai_Physical_Sky(TextureMap):
        TURBIDITY: float
        GROUND_ALBEDO: MXSWrapperBase
        USE_DEGREES: bool
        ELEVATION: float
        AZIMUTH: float
        SUN_DIRECTION: MXSWrapperBase
        ENABLE_SUN: bool
        SUN_SIZE: float
        SUN_TINT: MXSWrapperBase
        SKY_TINT: MXSWrapperBase
        INTENSITY: float
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
        TYPE: int
        INPUT: float
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        POSITION: MXSWrapperBase
        VALUE: MXSWrapperBase
        INTERPOLATION: MXSWrapperBase
        UVSET: str
        USE_IMPLICIT_UVS: int
        WRAP_UVS: bool
        ...
    class Ai_Ramp_Rgb(TextureMap):
        TYPE: int
        INPUT: float
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        POSITION: MXSWrapperBase
        COLOR: MXSWrapperBase
        INTERPOLATION: MXSWrapperBase
        UVSET: str
        USE_IMPLICIT_UVS: int
        WRAP_UVS: bool
        ...
    class Ai_Random(TextureMap):
        INPUT_TYPE: int
        INPUT_INT: int
        INPUT_INT_CONNECTED: bool
        INPUT_INT_SHADER: None
        INPUT_FLOAT: float
        INPUT_FLOAT_CONNECTED: bool
        INPUT_FLOAT_SHADER: None
        INPUT_COLOR: MXSWrapperBase
        INPUT_COLOR_CONNECTED: bool
        INPUT_COLOR_SHADER: None
        SEED: int
        SEED_CONNECTED: bool
        SEED_SHADER: None
        GRAYSCALE: bool
        ...
    class Ai_Range(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        INPUT_MIN: float
        INPUT_MIN_CONNECTED: bool
        INPUT_MIN_SHADER: None
        INPUT_MAX: float
        INPUT_MAX_CONNECTED: bool
        INPUT_MAX_SHADER: None
        OUTPUT_MIN: float
        OUTPUT_MIN_CONNECTED: bool
        OUTPUT_MIN_SHADER: None
        OUTPUT_MAX: float
        OUTPUT_MAX_CONNECTED: bool
        OUTPUT_MAX_SHADER: None
        SMOOTHSTEP: bool
        CONTRAST: float
        CONTRAST_CONNECTED: bool
        CONTRAST_SHADER: None
        CONTRAST_PIVOT: float
        CONTRAST_PIVOT_CONNECTED: bool
        CONTRAST_PIVOT_SHADER: None
        BIAS: float
        BIAS_CONNECTED: bool
        BIAS_SHADER: None
        GAIN: float
        GAIN_CONNECTED: bool
        GAIN_SHADER: None
        ...
    class Ai_Ray_Switch_Rgba(TextureMap):
        CAMERA: MXSWrapperBase
        CAMERA_CONNECTED: bool
        CAMERA_SHADER: None
        SHADOW: MXSWrapperBase
        SHADOW_CONNECTED: bool
        SHADOW_SHADER: None
        DIFFUSE_REFLECTION: MXSWrapperBase
        DIFFUSE_REFLECTION_CONNECTED: bool
        DIFFUSE_REFLECTION_SHADER: None
        DIFFUSE_TRANSMISSION: MXSWrapperBase
        DIFFUSE_TRANSMISSION_CONNECTED: bool
        DIFFUSE_TRANSMISSION_SHADER: None
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
        SHADOW: None
        DIFFUSE_REFLECTION: None
        DIFFUSE_TRANSMISSION: None
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
        SAMPLES: int
        RADIUS: float
        RADIUS_CONNECTED: bool
        RADIUS_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        TRACE_SET: str
        INCLUSIVE: bool
        SELF_ONLY: bool
        OBJECT_SPACE: bool
        ...
    class Ai_Set_Parameter(TextureMap):
        ...
    class Ai_Set_Transform(TextureMap):
        ...
    class Ai_Shadow_Matte(TextureMap):
        BACKGROUND: int
        BACKGROUND_CONNECTED: bool
        BACKGROUND_SHADER: None
        SHADOW_COLOR: MXSWrapperBase
        SHADOW_COLOR_CONNECTED: bool
        SHADOW_COLOR_SHADER: None
        SHADOW_OPACITY: float
        SHADOW_OPACITY_CONNECTED: bool
        SHADOW_OPACITY_SHADER: None
        BACKGROUND_COLOR: MXSWrapperBase
        BACKGROUND_COLOR_CONNECTED: bool
        BACKGROUND_COLOR_SHADER: None
        DIFFUSE_COLOR: MXSWrapperBase
        DIFFUSE_COLOR_CONNECTED: bool
        DIFFUSE_COLOR_SHADER: None
        DIFFUSE_USE_BACKGROUND: bool
        DIFFUSE_INTENSITY: float
        DIFFUSE_INTENSITY_CONNECTED: bool
        DIFFUSE_INTENSITY_SHADER: None
        BACKLIGHTING: float
        BACKLIGHTING_CONNECTED: bool
        BACKLIGHTING_SHADER: None
        INDIRECT_DIFFUSE_ENABLE: bool
        INDIRECT_SPECULAR_ENABLE: bool
        SPECULAR_COLOR: MXSWrapperBase
        SPECULAR_COLOR_CONNECTED: bool
        SPECULAR_COLOR_SHADER: None
        SPECULAR_INTENSITY: float
        SPECULAR_INTENSITY_CONNECTED: bool
        SPECULAR_INTENSITY_SHADER: None
        SPECULAR_ROUGHNESS: float
        SPECULAR_ROUGHNESS_CONNECTED: bool
        SPECULAR_ROUGHNESS_SHADER: None
        SPECULAR_IOR: float
        SPECULAR_IOR_CONNECTED: bool
        SPECULAR_IOR_SHADER: None
        ALPHA_MASK: bool
        ALPHA_MASK_CONNECTED: bool
        ALPHA_MASK_SHADER: None
        AOV_GROUP: str
        AOV_SHADOW: str
        AOV_SHADOW_DIFF: str
        AOV_SHADOW_MASK: str
        ...
    class Ai_Shuffle(TextureMap):
        COLOR: MXSWrapperBase
        COLOR_CONNECTED: bool
        COLOR_SHADER: None
        ALPHA: float
        ALPHA_CONNECTED: bool
        ALPHA_SHADER: None
        CHANNEL_R: int
        CHANNEL_G: int
        CHANNEL_B: int
        CHANNEL_A: int
        NEGATE_R: bool
        NEGATE_G: bool
        NEGATE_B: bool
        NEGATE_A: bool
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
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        TYPE: int
        FROM: int
        TO: int
        TANGENT: MXSWrapperBase
        TANGENT_CONNECTED: bool
        TANGENT_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        NORMALIZE: bool
        SCALE: float
        SCALE_CONNECTED: bool
        SCALE_SHADER: None
        ...
    class Ai_Sqrt(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        ...
    class Ai_Standard(Material):
        ...
    class Ai_Standard_Hair(Material):
        BASE: float
        BASE_CONNECTED: bool
        BASE_SHADER: None
        BASE_COLOR: MXSWrapperBase
        BASE_COLOR_CONNECTED: bool
        BASE_COLOR_SHADER: None
        MELANIN: float
        MELANIN_CONNECTED: bool
        MELANIN_SHADER: None
        MELANIN_REDNESS: float
        MELANIN_REDNESS_CONNECTED: bool
        MELANIN_REDNESS_SHADER: None
        MELANIN_RANDOMIZE: float
        MELANIN_RANDOMIZE_CONNECTED: bool
        MELANIN_RANDOMIZE_SHADER: None
        ROUGHNESS: float
        ROUGHNESS_CONNECTED: bool
        ROUGHNESS_SHADER: None
        ROUGHNESS_AZIMUTHAL: float
        ROUGHNESS_AZIMUTHAL_CONNECTED: bool
        ROUGHNESS_AZIMUTHAL_SHADER: None
        ROUGHNESS_ANISOTROPIC: bool
        IOR: float
        IOR_CONNECTED: bool
        IOR_SHADER: None
        SHIFT: float
        SHIFT_CONNECTED: bool
        SHIFT_SHADER: None
        SPECULAR_TINT: MXSWrapperBase
        SPECULAR_TINT_CONNECTED: bool
        SPECULAR_TINT_SHADER: None
        SPECULAR2_TINT: MXSWrapperBase
        SPECULAR2_TINT_CONNECTED: bool
        SPECULAR2_TINT_SHADER: None
        TRANSMISSION_TINT: MXSWrapperBase
        TRANSMISSION_TINT_CONNECTED: bool
        TRANSMISSION_TINT_SHADER: None
        DIFFUSE: float
        DIFFUSE_CONNECTED: bool
        DIFFUSE_SHADER: None
        DIFFUSE_COLOR: MXSWrapperBase
        DIFFUSE_COLOR_CONNECTED: bool
        DIFFUSE_COLOR_SHADER: None
        EMISSION: float
        EMISSION_CONNECTED: bool
        EMISSION_SHADER: None
        EMISSION_COLOR: MXSWrapperBase
        EMISSION_COLOR_CONNECTED: bool
        EMISSION_COLOR_SHADER: None
        OPACITY: MXSWrapperBase
        OPACITY_CONNECTED: bool
        OPACITY_SHADER: None
        INDIRECT_DIFFUSE: float
        INDIRECT_SPECULAR: float
        EXTRA_DEPTH: int
        EXTRA_SAMPLES: int
        AOV_ID1: str
        ID1: MXSWrapperBase
        ID1_CONNECTED: bool
        ID1_SHADER: None
        AOV_ID2: str
        ID2: MXSWrapperBase
        ID2_CONNECTED: bool
        ID2_SHADER: None
        AOV_ID3: str
        ID3: MXSWrapperBase
        ID3_CONNECTED: bool
        ID3_SHADER: None
        AOV_ID4: str
        ID4: MXSWrapperBase
        ID4_CONNECTED: bool
        ID4_SHADER: None
        AOV_ID5: str
        ID5: MXSWrapperBase
        ID5_CONNECTED: bool
        ID5_SHADER: None
        AOV_ID6: str
        ID6: MXSWrapperBase
        ID6_CONNECTED: bool
        ID6_SHADER: None
        AOV_ID7: str
        ID7: MXSWrapperBase
        ID7_CONNECTED: bool
        ID7_SHADER: None
        AOV_ID8: str
        ID8: MXSWrapperBase
        ID8_CONNECTED: bool
        ID8_SHADER: None
        ...
    class Ai_Standard_Surface(Material):
        BASE: float
        BASE_CONNECTED: bool
        BASE_SHADER: None
        BASE_COLOR: MXSWrapperBase
        BASE_COLOR_CONNECTED: bool
        BASE_COLOR_SHADER: None
        DIFFUSE_ROUGHNESS: float
        DIFFUSE_ROUGHNESS_CONNECTED: bool
        DIFFUSE_ROUGHNESS_SHADER: None
        SPECULAR: float
        SPECULAR_CONNECTED: bool
        SPECULAR_SHADER: None
        SPECULAR_COLOR: MXSWrapperBase
        SPECULAR_COLOR_CONNECTED: bool
        SPECULAR_COLOR_SHADER: None
        SPECULAR_ROUGHNESS: float
        SPECULAR_ROUGHNESS_CONNECTED: bool
        SPECULAR_ROUGHNESS_SHADER: None
        SPECULAR_IOR: float
        SPECULAR_IOR_CONNECTED: bool
        SPECULAR_IOR_SHADER: None
        SPECULAR_ANISOTROPY: float
        SPECULAR_ANISOTROPY_CONNECTED: bool
        SPECULAR_ANISOTROPY_SHADER: None
        SPECULAR_ROTATION: float
        SPECULAR_ROTATION_CONNECTED: bool
        SPECULAR_ROTATION_SHADER: None
        METALNESS: float
        METALNESS_CONNECTED: bool
        METALNESS_SHADER: None
        TRANSMISSION: float
        TRANSMISSION_CONNECTED: bool
        TRANSMISSION_SHADER: None
        TRANSMISSION_COLOR: MXSWrapperBase
        TRANSMISSION_COLOR_CONNECTED: bool
        TRANSMISSION_COLOR_SHADER: None
        TRANSMISSION_DEPTH: float
        TRANSMISSION_DEPTH_CONNECTED: bool
        TRANSMISSION_DEPTH_SHADER: None
        TRANSMISSION_SCATTER: MXSWrapperBase
        TRANSMISSION_SCATTER_CONNECTED: bool
        TRANSMISSION_SCATTER_SHADER: None
        TRANSMISSION_SCATTER_ANISOTROPY: float
        TRANSMISSION_SCATTER_ANISOTROPY_CONNECTED: bool
        TRANSMISSION_SCATTER_ANISOTROPY_SHADER: None
        TRANSMISSION_DISPERSION: float
        TRANSMISSION_DISPERSION_CONNECTED: bool
        TRANSMISSION_DISPERSION_SHADER: None
        TRANSMISSION_EXTRA_ROUGHNESS: float
        TRANSMISSION_EXTRA_ROUGHNESS_CONNECTED: bool
        TRANSMISSION_EXTRA_ROUGHNESS_SHADER: None
        TRANSMIT_AOVS: bool
        SUBSURFACE: float
        SUBSURFACE_CONNECTED: bool
        SUBSURFACE_SHADER: None
        SUBSURFACE_COLOR: MXSWrapperBase
        SUBSURFACE_COLOR_CONNECTED: bool
        SUBSURFACE_COLOR_SHADER: None
        SUBSURFACE_RADIUS: MXSWrapperBase
        SUBSURFACE_RADIUS_CONNECTED: bool
        SUBSURFACE_RADIUS_SHADER: None
        SUBSURFACE_SCALE: float
        SUBSURFACE_SCALE_CONNECTED: bool
        SUBSURFACE_SCALE_SHADER: None
        SUBSURFACE_ANISOTROPY: float
        SUBSURFACE_ANISOTROPY_CONNECTED: bool
        SUBSURFACE_ANISOTROPY_SHADER: None
        SUBSURFACE_TYPE: int
        SHEEN: float
        SHEEN_CONNECTED: bool
        SHEEN_SHADER: None
        SHEEN_COLOR: MXSWrapperBase
        SHEEN_COLOR_CONNECTED: bool
        SHEEN_COLOR_SHADER: None
        SHEEN_ROUGHNESS: float
        SHEEN_ROUGHNESS_CONNECTED: bool
        SHEEN_ROUGHNESS_SHADER: None
        THIN_WALLED: bool
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        TANGENT: MXSWrapperBase
        TANGENT_CONNECTED: bool
        TANGENT_SHADER: None
        COAT: float
        COAT_CONNECTED: bool
        COAT_SHADER: None
        COAT_COLOR: MXSWrapperBase
        COAT_COLOR_CONNECTED: bool
        COAT_COLOR_SHADER: None
        COAT_ROUGHNESS: float
        COAT_ROUGHNESS_CONNECTED: bool
        COAT_ROUGHNESS_SHADER: None
        COAT_IOR: float
        COAT_IOR_CONNECTED: bool
        COAT_IOR_SHADER: None
        COAT_ANISOTROPY: float
        COAT_ANISOTROPY_CONNECTED: bool
        COAT_ANISOTROPY_SHADER: None
        COAT_ROTATION: float
        COAT_ROTATION_CONNECTED: bool
        COAT_ROTATION_SHADER: None
        COAT_NORMAL: MXSWrapperBase
        COAT_NORMAL_CONNECTED: bool
        COAT_NORMAL_SHADER: None
        COAT_AFFECT_COLOR: float
        COAT_AFFECT_COLOR_CONNECTED: bool
        COAT_AFFECT_COLOR_SHADER: None
        COAT_AFFECT_ROUGHNESS: float
        COAT_AFFECT_ROUGHNESS_CONNECTED: bool
        COAT_AFFECT_ROUGHNESS_SHADER: None
        THIN_FILM_THICKNESS: float
        THIN_FILM_THICKNESS_CONNECTED: bool
        THIN_FILM_THICKNESS_SHADER: None
        THIN_FILM_IOR: float
        THIN_FILM_IOR_CONNECTED: bool
        THIN_FILM_IOR_SHADER: None
        EMISSION: float
        EMISSION_CONNECTED: bool
        EMISSION_SHADER: None
        EMISSION_COLOR: MXSWrapperBase
        EMISSION_COLOR_CONNECTED: bool
        EMISSION_COLOR_SHADER: None
        OPACITY: MXSWrapperBase
        OPACITY_CONNECTED: bool
        OPACITY_SHADER: None
        CAUSTICS: bool
        INTERNAL_REFLECTIONS: bool
        EXIT_TO_BACKGROUND: bool
        INDIRECT_DIFFUSE: float
        INDIRECT_SPECULAR: float
        DIELECTRIC_PRIORITY: int
        AOV_ID1: str
        ID1: MXSWrapperBase
        ID1_CONNECTED: bool
        ID1_SHADER: None
        AOV_ID2: str
        ID2: MXSWrapperBase
        ID2_CONNECTED: bool
        ID2_SHADER: None
        AOV_ID3: str
        ID3: MXSWrapperBase
        ID3_CONNECTED: bool
        ID3_SHADER: None
        AOV_ID4: str
        ID4: MXSWrapperBase
        ID4_CONNECTED: bool
        ID4_SHADER: None
        AOV_ID5: str
        ID5: MXSWrapperBase
        ID5_CONNECTED: bool
        ID5_SHADER: None
        AOV_ID6: str
        ID6: MXSWrapperBase
        ID6_CONNECTED: bool
        ID6_SHADER: None
        AOV_ID7: str
        ID7: MXSWrapperBase
        ID7_CONNECTED: bool
        ID7_SHADER: None
        AOV_ID8: str
        ID8: MXSWrapperBase
        ID8_CONNECTED: bool
        ID8_SHADER: None
        ...
    class Ai_Standard_Volume(Material):
        DENSITY: float
        DENSITY_CONNECTED: bool
        DENSITY_SHADER: None
        DENSITY_CHANNEL: str
        SCATTER: float
        SCATTER_CONNECTED: bool
        SCATTER_SHADER: None
        SCATTER_COLOR: MXSWrapperBase
        SCATTER_COLOR_CONNECTED: bool
        SCATTER_COLOR_SHADER: None
        SCATTER_COLOR_CHANNEL: str
        SCATTER_ANISOTROPY: float
        SCATTER_ANISOTROPY_CONNECTED: bool
        SCATTER_ANISOTROPY_SHADER: None
        TRANSPARENT: MXSWrapperBase
        TRANSPARENT_CONNECTED: bool
        TRANSPARENT_SHADER: None
        TRANSPARENT_DEPTH: float
        TRANSPARENT_CHANNEL: str
        EMISSION_MODE: int
        EMISSION: float
        EMISSION_CONNECTED: bool
        EMISSION_SHADER: None
        EMISSION_COLOR: MXSWrapperBase
        EMISSION_COLOR_CONNECTED: bool
        EMISSION_COLOR_SHADER: None
        EMISSION_CHANNEL: str
        TEMPERATURE: float
        TEMPERATURE_CONNECTED: bool
        TEMPERATURE_SHADER: None
        TEMPERATURE_CHANNEL: str
        BLACKBODY_KELVIN: float
        BLACKBODY_KELVIN_CONNECTED: bool
        BLACKBODY_KELVIN_SHADER: None
        BLACKBODY_INTENSITY: float
        BLACKBODY_INTENSITY_CONNECTED: bool
        BLACKBODY_INTENSITY_SHADER: None
        DISPLACEMENT: MXSWrapperBase
        DISPLACEMENT_CONNECTED: bool
        DISPLACEMENT_SHADER: None
        INTERPOLATION: int
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
        ...
    class Ai_Switch_Shader(Material):
        INDEX: int
        INDEX_CONNECTED: bool
        INDEX_SHADER: None
        INPUT0: None
        INPUT1: None
        INPUT2: None
        INPUT3: None
        INPUT4: None
        INPUT5: None
        INPUT6: None
        INPUT7: None
        INPUT8: None
        INPUT9: None
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
        ...
    class Ai_Thin_Film(TextureMap):
        ...
    class Ai_Toon(TextureMap):
        MASK_COLOR: MXSWrapperBase
        MASK_COLOR_CONNECTED: bool
        MASK_COLOR_SHADER: None
        EDGE_COLOR: MXSWrapperBase
        EDGE_COLOR_CONNECTED: bool
        EDGE_COLOR_SHADER: None
        EDGE_TONEMAP: MXSWrapperBase
        EDGE_TONEMAP_CONNECTED: bool
        EDGE_TONEMAP_SHADER: None
        EDGE_OPACITY: float
        EDGE_OPACITY_CONNECTED: bool
        EDGE_OPACITY_SHADER: None
        EDGE_WIDTH_SCALE: float
        EDGE_WIDTH_SCALE_CONNECTED: bool
        EDGE_WIDTH_SCALE_SHADER: None
        SILHOUETTE_COLOR: MXSWrapperBase
        SILHOUETTE_COLOR_CONNECTED: bool
        SILHOUETTE_COLOR_SHADER: None
        SILHOUETTE_TONEMAP: MXSWrapperBase
        SILHOUETTE_TONEMAP_CONNECTED: bool
        SILHOUETTE_TONEMAP_SHADER: None
        SILHOUETTE_OPACITY: float
        SILHOUETTE_OPACITY_CONNECTED: bool
        SILHOUETTE_OPACITY_SHADER: None
        SILHOUETTE_WIDTH_SCALE: float
        SILHOUETTE_WIDTH_SCALE_CONNECTED: bool
        SILHOUETTE_WIDTH_SCALE_SHADER: None
        PRIORITY: int
        ENABLE_SILHOUETTE: bool
        IGNORE_THROUGHPUT: bool
        ENABLE: bool
        ID_DIFFERENCE: bool
        SHADER_DIFFERENCE: bool
        UV_THRESHOLD: float
        UV_THRESHOLD_CONNECTED: bool
        UV_THRESHOLD_SHADER: None
        ANGLE_THRESHOLD: float
        ANGLE_THRESHOLD_CONNECTED: bool
        ANGLE_THRESHOLD_SHADER: None
        NORMAL_TYPE: int
        BASE: float
        BASE_CONNECTED: bool
        BASE_SHADER: None
        BASE_COLOR: MXSWrapperBase
        BASE_COLOR_CONNECTED: bool
        BASE_COLOR_SHADER: None
        BASE_TONEMAP: MXSWrapperBase
        BASE_TONEMAP_CONNECTED: bool
        BASE_TONEMAP_SHADER: None
        SPECULAR: float
        SPECULAR_CONNECTED: bool
        SPECULAR_SHADER: None
        SPECULAR_COLOR: MXSWrapperBase
        SPECULAR_COLOR_CONNECTED: bool
        SPECULAR_COLOR_SHADER: None
        SPECULAR_ROUGHNESS: float
        SPECULAR_ROUGHNESS_CONNECTED: bool
        SPECULAR_ROUGHNESS_SHADER: None
        SPECULAR_ANISOTROPY: float
        SPECULAR_ANISOTROPY_CONNECTED: bool
        SPECULAR_ANISOTROPY_SHADER: None
        SPECULAR_ROTATION: float
        SPECULAR_ROTATION_CONNECTED: bool
        SPECULAR_ROTATION_SHADER: None
        SPECULAR_TONEMAP: MXSWrapperBase
        SPECULAR_TONEMAP_CONNECTED: bool
        SPECULAR_TONEMAP_SHADER: None
        LIGHTS: str
        HIGHLIGHT_COLOR: MXSWrapperBase
        HIGHLIGHT_COLOR_CONNECTED: bool
        HIGHLIGHT_COLOR_SHADER: None
        HIGHLIGHT_SIZE: float
        HIGHLIGHT_SIZE_CONNECTED: bool
        HIGHLIGHT_SIZE_SHADER: None
        AOV_HIGHLIGHT: str
        RIM_LIGHT: str
        RIM_LIGHT_COLOR: MXSWrapperBase
        RIM_LIGHT_COLOR_CONNECTED: bool
        RIM_LIGHT_COLOR_SHADER: None
        RIM_LIGHT_WIDTH: float
        RIM_LIGHT_WIDTH_CONNECTED: bool
        RIM_LIGHT_WIDTH_SHADER: None
        RIM_LIGHT_TINT: float
        RIM_LIGHT_TINT_CONNECTED: bool
        RIM_LIGHT_TINT_SHADER: None
        AOV_RIM_LIGHT: str
        TRANSMISSION: float
        TRANSMISSION_CONNECTED: bool
        TRANSMISSION_SHADER: None
        TRANSMISSION_COLOR: MXSWrapperBase
        TRANSMISSION_COLOR_CONNECTED: bool
        TRANSMISSION_COLOR_SHADER: None
        TRANSMISSION_ROUGHNESS: float
        TRANSMISSION_ROUGHNESS_CONNECTED: bool
        TRANSMISSION_ROUGHNESS_SHADER: None
        TRANSMISSION_ANISOTROPY: float
        TRANSMISSION_ANISOTROPY_CONNECTED: bool
        TRANSMISSION_ANISOTROPY_SHADER: None
        TRANSMISSION_ROTATION: float
        TRANSMISSION_ROTATION_CONNECTED: bool
        TRANSMISSION_ROTATION_SHADER: None
        SHEEN: float
        SHEEN_CONNECTED: bool
        SHEEN_SHADER: None
        SHEEN_COLOR: MXSWrapperBase
        SHEEN_COLOR_CONNECTED: bool
        SHEEN_COLOR_SHADER: None
        SHEEN_ROUGHNESS: float
        SHEEN_ROUGHNESS_CONNECTED: bool
        SHEEN_ROUGHNESS_SHADER: None
        EMISSION: float
        EMISSION_CONNECTED: bool
        EMISSION_SHADER: None
        EMISSION_COLOR: MXSWrapperBase
        EMISSION_COLOR_CONNECTED: bool
        EMISSION_COLOR_SHADER: None
        IOR: float
        IOR_CONNECTED: bool
        IOR_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        TANGENT: MXSWrapperBase
        TANGENT_CONNECTED: bool
        TANGENT_SHADER: None
        INDIRECT_DIFFUSE: float
        INDIRECT_SPECULAR: float
        BUMP_MODE: int
        ENERGY_CONSERVING: bool
        USER_ID: bool
        AOV_PREFIX: str
        ...
    class Ai_Trace_Set(Material):
        PASSTHROUGH: None
        TRACE_SET: str
        INCLUSIVE: bool
        ...
    class Ai_Triangle_Filter(TextureMap):
        ...
    class Ai_Trigo(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        FUNCTION: int
        UNITS: int
        FREQUENCY: float
        FREQUENCY_CONNECTED: bool
        FREQUENCY_SHADER: None
        PHASE: float
        PHASE_CONNECTED: bool
        PHASE_SHADER: None
        ...
    class Ai_Triplanar(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        SCALE: MXSWrapperBase
        SCALE_CONNECTED: bool
        SCALE_SHADER: None
        ROTATE: MXSWrapperBase
        ROTATE_CONNECTED: bool
        ROTATE_SHADER: None
        OFFSET: MXSWrapperBase
        OFFSET_CONNECTED: bool
        OFFSET_SHADER: None
        COORD_SPACE: int
        PREF_NAME: str
        BLEND: float
        BLEND_CONNECTED: bool
        BLEND_SHADER: None
        CELL: bool
        CELL_CONNECTED: bool
        CELL_SHADER: None
        CELL_ROTATE: float
        CELL_ROTATE_CONNECTED: bool
        CELL_ROTATE_SHADER: None
        CELL_BLEND: float
        CELL_BLEND_CONNECTED: bool
        CELL_BLEND_SHADER: None
        ...
    class Ai_Two_Sided(Material):
        FRONT: None
        BACK: None
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
        COLOR_MODE: int
        SHADE_MODE: int
        OVERLAY_MODE: int
        COLOR: MXSWrapperBase
        COLOR_CONNECTED: bool
        COLOR_SHADER: None
        AO_DISTANCE: float
        AO_DISTANCE_CONNECTED: bool
        AO_DISTANCE_SHADER: None
        ROUGHNESS: float
        ROUGHNESS_CONNECTED: bool
        ROUGHNESS_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        ...
    class Ai_Uv_Projection(TextureMap):
        PROJECTION_COLOR: MXSWrapperBase
        PROJECTION_COLOR_CONNECTED: bool
        PROJECTION_COLOR_SHADER: None
        PROJECTION_TYPE: int
        COORD_SPACE: int
        PREF_NAME: str
        P: MXSWrapperBase
        P_CONNECTED: bool
        P_SHADER: None
        U_ANGLE: float
        U_ANGLE_CONNECTED: bool
        U_ANGLE_SHADER: None
        V_ANGLE: float
        V_ANGLE_CONNECTED: bool
        V_ANGLE_SHADER: None
        CLAMP: bool
        DEFAULT_COLOR: MXSWrapperBase
        DEFAULT_COLOR_CONNECTED: bool
        DEFAULT_COLOR_SHADER: None
        MATRIX: MXSWrapperBase
        MATRIX_CONNECTED: bool
        MATRIX_SHADER: None
        ...
    class Ai_Uv_Transform(TextureMap):
        PASSTHROUGH: MXSWrapperBase
        PASSTHROUGH_CONNECTED: bool
        PASSTHROUGH_SHADER: None
        UNIT: int
        UVSET: str
        COVERAGE: MXSWrapperBase
        COVERAGE_CONNECTED: bool
        COVERAGE_SHADER: None
        SCALE_FRAME: MXSWrapperBase
        SCALE_FRAME_CONNECTED: bool
        SCALE_FRAME_SHADER: None
        TRANSLATE_FRAME: MXSWrapperBase
        TRANSLATE_FRAME_CONNECTED: bool
        TRANSLATE_FRAME_SHADER: None
        ROTATE_FRAME: float
        ROTATE_FRAME_CONNECTED: bool
        ROTATE_FRAME_SHADER: None
        PIVOT_FRAME: MXSWrapperBase
        PIVOT_FRAME_CONNECTED: bool
        PIVOT_FRAME_SHADER: None
        WRAP_FRAME_U: int
        WRAP_FRAME_V: int
        WRAP_FRAME_COLOR: MXSWrapperBase
        WRAP_FRAME_COLOR_CONNECTED: bool
        WRAP_FRAME_COLOR_SHADER: None
        REPEAT: MXSWrapperBase
        REPEAT_CONNECTED: bool
        REPEAT_SHADER: None
        OFFSET: MXSWrapperBase
        OFFSET_CONNECTED: bool
        OFFSET_SHADER: None
        ROTATE: float
        ROTATE_CONNECTED: bool
        ROTATE_SHADER: None
        PIVOT: MXSWrapperBase
        PIVOT_CONNECTED: bool
        PIVOT_SHADER: None
        NOISE: MXSWrapperBase
        NOISE_CONNECTED: bool
        NOISE_SHADER: None
        MIRROR_U: bool
        MIRROR_V: bool
        FLIP_U: bool
        FLIP_V: bool
        SWAP_UV: bool
        STAGGER: bool
        ...
    class Ai_Variance_Filter(TextureMap):
        ...
    class Ai_Vector_Map(TextureMap):
        INPUT: MXSWrapperBase
        INPUT_CONNECTED: bool
        INPUT_SHADER: None
        TANGENT: MXSWrapperBase
        TANGENT_CONNECTED: bool
        TANGENT_SHADER: None
        NORMAL: MXSWrapperBase
        NORMAL_CONNECTED: bool
        NORMAL_SHADER: None
        ORDER: int
        INVERT_X: bool
        INVERT_Y: bool
        INVERT_Z: bool
        COLOR_TO_SIGNED: bool
        TANGENT_SPACE: bool
        SCALE: float
        SCALE_CONNECTED: bool
        SCALE_SHADER: None
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
        CHANNEL: str
        POSITION_OFFSET: MXSWrapperBase
        POSITION_OFFSET_CONNECTED: bool
        POSITION_OFFSET_SHADER: None
        INTERPOLATION: int
        VOLUME_TYPE: int
        SDF_OFFSET: float
        SDF_OFFSET_CONNECTED: bool
        SDF_OFFSET_SHADER: None
        SDF_BLEND: float
        SDF_BLEND_CONNECTED: bool
        SDF_BLEND_SHADER: None
        SDF_INVERT: bool
        INPUT_MIN: float
        INPUT_MAX: float
        CONTRAST: float
        CONTRAST_PIVOT: float
        BIAS: float
        GAIN: float
        OUTPUT_MIN: float
        OUTPUT_MAX: float
        CLAMP_MIN: bool
        CLAMP_MAX: bool
        ...
    class Ai_Volume_Sample_Rgb(TextureMap):
        CHANNEL: str
        POSITION_OFFSET: MXSWrapperBase
        POSITION_OFFSET_CONNECTED: bool
        POSITION_OFFSET_SHADER: None
        INTERPOLATION: int
        GAMMA: float
        HUE_SHIFT: float
        SATURATION: float
        CONTRAST: float
        CONTRAST_PIVOT: float
        EXPOSURE: float
        MULTIPLY: float
        ADD: float
        ...
    class Ai_Wireframe(TextureMap):
        LINE_WIDTH: float
        LINE_WIDTH_CONNECTED: bool
        LINE_WIDTH_SHADER: None
        FILL_COLOR: MXSWrapperBase
        FILL_COLOR_CONNECTED: bool
        FILL_COLOR_SHADER: None
        LINE_COLOR: MXSWrapperBase
        LINE_COLOR_CONNECTED: bool
        LINE_COLOR_SHADER: None
        RASTER_SPACE: bool
        RASTER_SPACE_CONNECTED: bool
        RASTER_SPACE_SHADER: None
        EDGE_TYPE: int
        EDGE_TYPE_CONNECTED: bool
        EDGE_TYPE_SHADER: None
        ...
    class Alpha(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ...
    class AlphaRenderElement(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
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
        STEPS: int
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        TYPEIN_X: float
        TYPEIN_Y: float
        TYPEIN_Z: float
        TYPEIN_LENGTH: float
        TYPEIN_WIDTH: float
        TYPEIN_THICKNESS: float
        TYPEIN_RADIUS: float
        TYPEIN_RADIUS2: float
        TYPEIN_CREATIONMETHOD: bool
        TYPEIN_EDGEFILLET: float
        ANGLE_LENGTH: float
        ANGLE_WIDTH: float
        ANGLE_THICKNESS: float
        ANGLE_RADIUS: float
        ANGLE_RADIUS2: float
        ANGLE_SYNCCORNERFILLETS: bool
        ANGLE_EDGEFILLET: float
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
        ARNOLD_NODE_VERTICAL_FOV: float
        ARNOLD_NODE_PROJECTIVE: bool
        ...
    class Arnold_Fisheye_Camera(Camera):
        ARNOLD_NODE: str
        ARNOLD_NODE_FOV: float
        ARNOLD_NODE_AUTOCROP: bool
        ...
    class Arnold_Spherical_Camera(Camera):
        ARNOLD_NODE: str
        ...
    class Arnold_Vr_Camera(Camera):
        ARNOLD_NODE: str
        ARNOLD_NODE_MODE: int
        ARNOLD_NODE_PROJECTION: int
        ARNOLD_NODE_EYE_SEPARATION: float
        ARNOLD_NODE_EYE_TO_NECK: float
        ARNOLD_NODE_TOP_MERGE_MODE: int
        ARNOLD_NODE_TOP_MERGE_ANGLE: float
        ARNOLD_NODE_BOTTOM_MERGE_MODE: int
        ARNOLD_NODE_BOTTOM_MERGE_ANGLE: float
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
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
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
        ORIGINALMATERIAL: MXSWrapperBase
        BAKEDMATERIAL: MXSWrapperBase
        VIEWPORTMTLINDEX: int
        RENDERMTLINDEX: int
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
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
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
        CLIPU: float
        CLIPV: float
        CLIPW: float
        CLIPH: float
        JITTER: float
        USEJITTER: bool
        APPLY: bool
        CROPPLACE: int
        FILTERING: int
        MONOOUTPUT: int
        RGBOUTPUT: int
        ALPHASOURCE: int
        PREMULTALPHA: bool
        BITMAP: None
        COORDS: MXSWrapperBase
        OUTPUT: MXSWrapperBase
        FILENAME: str
        STARTTIME: MXSWrapperBase
        PLAYBACKRATE: float
        ENDCONDITION: int
        TIETIMETOMATIDS: bool
        ...
    class Black(Color):
        ...
    class BlockMgr(Interface):
        ...
    class Blue(Color):
        ...
    class Blur(RenderEffect):
        BLUR_TYPE: int
        BUNIFPIXRAD: float
        BUNIFALPHA: bool
        BDIRUPIXRAD: float
        BDIRVPIXRAD: float
        BDIRUTRAIL: float
        BDIRVTRAIL: float
        BDIRROTATION: int
        BDIRALPHA: bool
        BRADIALPIXRAD: float
        BRADIALTRAIL: float
        BRADIALALPHA: bool
        BRADIALXORIG: int
        BRADIALYORIG: int
        BRADIALUSENODE: bool
        BRADIALNODE: None
        SELIMAGEACTIVE: bool
        SELIMAGEBRIGHTEN: float
        SELIMAGEBLEND: float
        SELIBACKACTIVE: bool
        SELIBACKBRIGHTEN: float
        SELIBACKBLEND: float
        SELIBACKFRADIUS: float
        SELLUMACTIVE: bool
        SELLUMBRIGHTEN: float
        SELLUMBLEND: float
        SELLUMMIN: float
        SELLUMMAX: float
        SELLUMFRADIUS: float
        SELMASKACTIVE: bool
        SELMASKMAP: None
        SELMASKCHANNEL: int
        SELMASKBRIGHTEN: float
        SELMASKBLEND: float
        SELMASKMIN: float
        SELMASKMAX: float
        SELMASKFRADIUS: float
        SELOBJIDSACTIVE: bool
        SELOBJIDSIDS: MXSWrapperBase
        SELOBJIDSBRIGHTEN: float
        SELOBJIDSBLEND: float
        SELOBJIDSFRADIUS: float
        SELOBJIDSLUMMIN: float
        SELOBJIDSLUMMAX: float
        SELMATIDSACTIVE: bool
        SELMATIDSIDS: MXSWrapperBase
        SELMATIDSBRIGHTEN: float
        SELMATIDSBLEND: float
        SELMATIDSFRADIUS: float
        SELMATIDSLUMMIN: float
        SELMATIDSLUMMAX: float
        SELGENBRIGHTTYPE: int
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
        CELLCOLOR: MXSWrapperBase
        DIVCOLOR1: MXSWrapperBase
        DIVCOLOR2: MXSWrapperBase
        CELLMAP: None
        DIVMAP1: None
        DIVMAP2: None
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        MAP3ENABLED: bool
        VARIATION: float
        SIZE: float
        SPREAD: float
        LOWTHRESH: float
        MIDTHRESH: float
        HIGHTHRESH: float
        TYPE: int
        FRACTAL: bool
        ITERATION: float
        ROUGHNESS: float
        SMOOTH: float
        ADAPTIVE: bool
        COORDS: MXSWrapperBase
        OUTPUT: MXSWrapperBase
        ...
    class Channel(Shape):
        STEPS: int
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        TYPEIN_X: float
        TYPEIN_Y: float
        TYPEIN_Z: float
        TYPEIN_LENGTH: float
        TYPEIN_WIDTH: float
        TYPEIN_THICKNESS: float
        TYPEIN_RADIUS: float
        TYPEIN_RADIUS2: float
        TYPEIN_CREATIONMETHOD: bool
        CHANNEL_LENGTH: float
        CHANNEL_WIDTH: float
        CHANNEL_THICKNESS: float
        CHANNEL_RADIUS: float
        CHANNEL_RADIUS2: float
        CHANNEL_SYNCCORNERFILLETS: bool
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
        GRAVITY: float
        SELFCOLLISION: bool
        SOLIDCOLLISION: bool
        SCALE: float
        USESEWINGSPRINGS: bool
        STARTFRAME: int
        TIMESTEP: float
        SHOWSEWINGSPRINGS: bool
        SUBSAMPLE: int
        ENDFRAME: int
        ENABLEENDFRAME: bool
        CHECKINTERSECTIONS: bool
        CLOTHCLOTHMETHOD: int
        USEGRAVITY: bool
        SIMONRENDER: bool
        SIMPRIORITY: int
        ADVANCEDPINCHING: bool
        RELATIVEVELOCITY: float
        TIMESCALE: float
        IGNOREBACKFACING: bool
        SIMONMOUSEDOWN: bool
        SHOWCURRENTSTATE: bool
        SHOWTARGETSTATE: bool
        SHOWENABLEDSOLIDCOLLISION: bool
        SHOWENABLEDCLOTHCOLLISION: bool
        SHOWTENSION: bool
        TENSIONSCALE: float
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
        RED: int
        GREEN: int
        BLUE: int
        PRESERVELUM: bool
        IGNOREBACK: bool
        ...
    class ColorMan(Interface):
        ...
    class ColorPicker(MAXWrapperNonRefTarg):
        ...
    class ColorPickerDlg(Primitive):
        ...
    class ColorReferenceTarget(ReferenceTarget):
        TYPE: int
        COLOR: MXSWrapperBase
        RED: int
        GREEN: int
        BLUE: int
        HUE: int
        SATURATION: int
        VALUE: int
        USE_RGB_E1: bool
        USE_RGB_E2: bool
        USE_RGB_E3: bool
        USE_HSV_E1: bool
        USE_HSV_E2: bool
        USE_HSV_E3: bool
        USE_RGB_I1: bool
        USE_RGB_I2: bool
        USE_RGB_I3: bool
        USE_HSV_I1: bool
        USE_HSV_I2: bool
        USE_HSV_I3: bool
        VARIATION_TYPE: int
        USE_RED_VARIATION: bool
        USE_GREEN_VARIATION: bool
        USE_BLUE_VARIATION: bool
        USE_HUE_VARIATION: bool
        USE_SATURATION_VARIATION: bool
        USE_VALUE_VARIATION: bool
        RED_VARIATION: int
        GREEN_VARIATION: int
        BLUE_VARIATION: int
        HUE_VARIATION: int
        SATURATION_VARIATION: int
        VALUE_VARIATION: int
        USE_RGB_E4: bool
        USE_RGB_E5: bool
        USE_RGB_E6: bool
        USE_HSV_E4: bool
        USE_HSV_E5: bool
        USE_HSV_E6: bool
        USE_RGB_I4: bool
        USE_RGB_I5: bool
        USE_RGB_I6: bool
        USE_HSV_I4: bool
        USE_HSV_I5: bool
        USE_HSV_I6: bool
        SYNC_TYPE: int
        USE_E7: bool
        RANDOM_SEED: int
        USE_E8: bool
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        INPUT_7: None
        INPUT_8: None
        ...
    class CompareBitmaps(Primitive):
        ...
    class Composite(Generic):
        ...
    class CompositeTexture(TextureMap):
        MAPENABLED: MXSWrapperBase
        MASKENABLED: MXSWrapperBase
        BLENDMODE: MXSWrapperBase
        LAYERNAME: MXSWrapperBase
        DLGOPENED: MXSWrapperBase
        OPACITY: MXSWrapperBase
        MAPLIST: MXSWrapperBase
        MASK: MXSWrapperBase
        ...
    class Compositematerial(Material):
        MATERIALLIST: MXSWrapperBase
        MIXTYPE: MXSWrapperBase
        MAPENABLES: MXSWrapperBase
        AMOUNT: MXSWrapperBase
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
        FRAMEPAD: int
        FONTSCALE: int
        DIMBG: bool
        ALPHABLEND: bool
        REQDDISTANCE: int
        TYPETEXTTL: int
        TYPETEXTTC: int
        TYPETEXTTR: int
        TYPETEXTBL: int
        TYPETEXTBC: int
        TYPETEXTBR: int
        EDITTEXTTL: str
        EDITTEXTTC: str
        EDITTEXTTR: str
        EDITTEXTBL: str
        EDITTEXTBC: str
        EDITTEXTBR: str
        USEIMAGE: bool
        IMAGEFNAME: str
        IMAGE_X: int
        IMAGE_Y: int
        IMGOPACITY: int
        TRANSFER_MODE: int
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
        MAP1: None
        MAP2: None
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        SIZE: float
        STRENGTH: float
        ITERATIONS: int
        COORDS: MXSWrapperBase
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
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        BACKGROUNDCOLOR: MXSWrapperBase
        LIGHTINGON: bool
        SHADOWSON: bool
        TARGETMAPSLOTNAME: str
        ...
    class DiffuseRenderElement(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
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
        MATERIAL1: MXSWrapperBase
        MATERIAL2: MXSWrapperBase
        MAP1ENABLED: bool
        MAP2ENABLED: bool
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
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
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
        MAP1AMOUNT: float
        MAP1: None
        MAP1ON: bool
        COLOR2: MXSWrapperBase
        MAP2AMOUNT: float
        MAP2: None
        MAP2ON: bool
        TYPE: int
        DIRECTION: int
        NODE: None
        MTLIOROVERRIDE: bool
        IOR: float
        EXTRAPOLATEON: bool
        NEARDISTANCE: float
        FARDISTANCE: float
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
        CHANNELTYPE: int
        CAMERANODE: None
        NEARZ: float
        FARZ: float
        FITSCENE: bool
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
        BLURAMOUNT: float
        DISTORTIONAMOUNT: float
        LEVEL: float
        SIZE: float
        PHASE: float
        APPLYBLUR: bool
        NTHFRAME: int
        FRAME: int
        USEENVIROMENT: bool
        APPLYTOFACEID: bool
        FACEID: int
        DISTORTIONTYPE: int
        NOISETYPE: int
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
        UPPER_LIMIT: float
        LOWER_LIMIT: float
        UPPER_LIMIT_ENABLED: bool
        LOWER_LIMIT_ENABLED: bool
        STATIC_VALUE: float
        UPPER_SMOOTHING: float
        LOWER_SMOOTHING: float
        ...
    class Float_List(FloatController):
        WEIGHT: MXSWrapperBase
        AVERAGE: bool
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
        RGB: MXSWrapperBase
        MULTIPLIER: float
        CONTRAST: float
        SOFTENDIFFUSEEDGE: float
        ATMOSSHADOWS: bool
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        SHADOWMULTIPLIER: float
        TARGETDISTANCE: None
        USEGLOBALSHADOWSETTINGS: bool
        HASTARGET: bool
        ON: bool
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        CASTSHADOWS: bool
        ...
    class FreeSceneBitmaps(Primitive):
        ...
    class FreeSpot(Light):
        ASPECT: float
        RGB: MXSWrapperBase
        COLOR: MXSWrapperBase
        CONTRAST: float
        ENABLED: bool
        ON: bool
        TYPE: MXSWrapperBase
        VALUE: int
        FALLOFF: float
        EXCLUDELIST: MXSWrapperBase
        INCLUDELIST: None
        SHOWCONE: bool
        MULTIPLIER: float
        SOFTENDIFFUSEEDGE: float
        HOTSPOT: float
        FARATTENSTART: float
        FARATTENEND: float
        NEARATTENSTART: float
        NEARATTENEND: float
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        DECAYRADIUS: float
        SHADOWCOLOR: MXSWrapperBase
        SHADOWMULTIPLIER: float
        HSV: MXSWrapperBase
        HUE: int
        SATURATION: int
        INCLEXCLTYPE: int
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        USENEARATTEN: bool
        SHOWNEARATTEN: bool
        USEFARATTEN: bool
        SHOWFARATTEN: bool
        ATTENDECAY: int
        PROJECTOR: bool
        PROJECTORMAP: None
        CASTSHADOWS: bool
        USEGLOBALSHADOWSETTINGS: bool
        RAYTRACEDSHADOWS: bool
        OVERSHOOT: bool
        CONESHAPE: int
        LIGHTSHAPE: int
        ATMOSSHADOWS: bool
        LIGHTAFFECTSSHADOW: bool
        SHADOWPROJECTORMAP: None
        USESHADOWPROJECTORMAP: bool
        AMBIENTONLY: bool
        SHADOWGENERATOR: MXSWrapperBase
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
        TYPE: int
        USE_SUB_MATERIAL: bool
        SUB_MATERIAL_INDEX: int
        MAP_CHANNEL_INDEX: int
        GRADIENT_DELTA: float
        STATIC_OBJECTS: bool
        ANIMATED_SURFACE: bool
        GEOMETRY_SAFE_MODE: bool
        SUBFRAME_PLACEMENT: bool
        SUBFRAME_GEOMETRY: bool
        SEPARATE_GROUP_MEMBERS: bool
        SEPARATE_CHILDREN: bool
        USE_T2: bool
        USE_I3: bool
        USE_V4: bool
        USE_V5: bool
        USE_R6: bool
        RANDOM_SEED: int
        USE_E7: bool
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        INPUT_7: None
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
        STRENGTH: float
        DECAY: float
        GRAVITYTYPE: int
        ICONSIZE: float
        HOOPSON: bool
        ...
    class Gray(Color):
        ...
    class Green(Color):
        ...
    class Grid(Helper):
        LENGTH: float
        WIDTH: float
        GRID: float
        ACTIVECOLOR: int
        DISPLAYPLANE: int
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
        TYPE: int
        STATIC_ICON: bool
        SUBFRAME_PLACEMENT: bool
        SUBFRAME_GEOMETRY: bool
        USE_T1: bool
        USE_V3: bool
        USE_V4: bool
        RANDOM_SEED: int
        USE_E4: bool
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
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
        STEPS: int
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
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
        USESOFTSELECTION: bool
        SOFTSELUSEEDGEDISTANCE: bool
        SOFTSELEDGEDIST: int
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELBUBBLE: float
        USETEXTUREMAP: bool
        TEXTURE: None
        MAP: int
        MAPCHANNEL: int
        GRAVITY: float
        IGNOREBACKFACING: bool
        SHOWTARGETSTATE: bool
        SHOWTENSION: bool
        TENSIONSCALE: float
        WELDMETHOD: int
        THICKNESS: float
        SELF_THICKNESS: float
        SOLVER_ITERATIONS: int
        BENDINESS: float
        HARD_STRETCH_LIMITATION: float
        STRETCHINESS: float
        DENSITY: float
        DAMPING_COEFFICIENT: float
        FRICTION: float
        PRESSURE: float
        TEAR_FACTOR: float
        COLLISION_RESPONSE_COEFFICIENT: float
        ATTACHMENT_RESPONSE_COEFFICIENT: float
        ATTACHMENT_TEAR_FACTOR: float
        TO_FLUID_RESPONSE_COEFFICIENT: float
        FROM_FLUID_RESPONSE_COEFFICIENT: float
        COMPRESSIONS_LIMIT: float
        COMPRESSIONS_STIFFNESS: float
        MIN_ADHERE_VELOCITY: float
        ATTACHTOCOLLIDE: bool
        DO_PRESSURE: bool
        IS_STATIC: bool
        ENABLE_COLLISION: bool
        SELF_COLLISION: bool
        VISUALIZATION: bool
        DO_GRAVITY: bool
        DO_BENDING: bool
        DO_BENDING_ORTHO: bool
        DAMPING: float
        TWO_WAY_COLLISION: bool
        HARDWARE: bool
        COM_DAMPING: bool
        VALIDBOUNDS: bool
        DO_FLUID_COLLISION: bool
        DISABLE_DYNAMIC_CCD: bool
        DO_ADHERE: bool
        DO_HARD_STRETCH_LIMITATION: bool
        DO_UNTANGLING: bool
        DO_INTER_COLLISION: bool
        TEARABLE: bool
        INHERIT_VELOCITY: bool
        SOLVER_ITERATIONS: int
        HIERARCHICAL_LEVELS: int
        BEHAVIOR: int
        FORCELIST: MXSWrapperBase
        ENABLELIVEDRAG: bool
        UNTILFRAMEENABLE: bool
        KINEMATIC_UNTIL_FRAME: int
        USESOFTSELECTION: bool
        SOFTSELUSEEDGEDISTANCE: bool
        SOFTSELEDGEDIST: int
        SOFTSELAFFECTBACKFACING: bool
        SOFTSELFALLOFF: float
        SOFTSELPINCH: float
        SOFTSELBUBBLE: float
        USETEXTUREMAP: bool
        TEXTURE: None
        MAP: int
        MAPCHANNEL: int
        ...
    class MP_Buoyancy(Helper):
        DENSITY: float
        LEVEL_TYPE: int
        LEVEL_HEIGHT: float
        GRID_GEOMETRY: None
        USE_QUADRATIC_DRAG: bool
        QUADRATIC_DRAG: float
        USE_LINEAR_DRAG: bool
        LINEAR_DRAG: float
        USE_ANGULAR_DRAG: bool
        ANGULAR_DRAG: float
        SURFACE_UNIT: float
        ICON_SHAPE: int
        ICON_LENGTH: float
        ICON_WIDTH: float
        ICON_HEIGHT: float
        LIMIT_BUOYANCY_BY_ICON: bool
        COLOR_COORDINATED: bool
        ...
    class MP_Collision(Helper):
        DEFLECTORS: MXSWrapperBase
        TEST_TRUE: bool
        TEST_TYPE: int
        MIN_SPEED: float
        MAX_SPEED: float
        COLLISION_COUNT: int
        REPORT_TO_DATA_OPERATOR: bool
        ADDITIVE_COUNT: bool
        COLLISION_GROUP: int
        ...
    class MP_Drag(Helper):
        TIMING_TYPE: int
        APPLY_LINEAR_DAMPING: bool
        LINEAR_DAMPING: float
        APPLY_ANGULAR_DAMPING: bool
        ANGULAR_DAMPING: float
        SYNC: int
        SPEED_MULTIPLIER: bool
        SPEED_UNIT: float
        SPIN_UNIT: float
        USE_DATA_WIRING: bool
        LINEAR_DAMPING_FROM_DATA: bool
        LINEAR_DAMPING_DATA_CREATOR: None
        ANGULAR_DAMPING_FROM_DATA: bool
        ANGULAR_DAMPING_DATA_CREATOR: None
        ...
    class MP_Force(Helper):
        FORCE_TYPE: int
        FORCE_VARIATION_THRESHOLD: bool
        SHAPE_SIZE: float
        INFLUENCE: float
        SYNC: int
        FORCE_SPACE_WARPS: MXSWrapperBase
        FORCE_OVERLAPPING: int
        IMPULSE_ON_EVENT_ENTRY: bool
        TIME_WARP: int
        EXPONENT: int
        USE_SCRIPT_FLOAT: int
        ...
    class MP_Glue(Helper):
        TIMING_TYPE: int
        BIND_DISTANCE: float
        USE_BIND_GAP_CONDITION: bool
        BIND_GAP: float
        BIND_CENTER_ALIGNED_ONLY: bool
        ALIGN_MARGIN: float
        ALLOW_BINDING_PENETRATION: bool
        TYPE: int
        BREAKABLE_BY_FORCE: bool
        MAX_FORCE: float
        MAX_TORQUE: float
        MAX_BY_BIND_DISTANCE: bool
        DISTANCE_UNIT: float
        CONTINUOUS_ADJUSTMENT: bool
        SYNC: int
        MAX_BINDS_PER_PARTICLE: int
        TEST_TRUE: bool
        TEST_TYPE: int
        BIND_IN_CURRENT_EVENT: bool
        BIND_WITH_OTHER_EVENTS: bool
        EVENTS_TO_BIND_WITH: MXSWrapperBase
        BIND_WITH_DEFLECTORS: bool
        BIND_WITH_GROUND: bool
        DEFLECTORS_TO_BIND_WITH: MXSWrapperBase
        VISUALIZE_BINDING: bool
        COLOR: MXSWrapperBase
        SIMPLIFIED_BINDING_ANCHOR_TYPE: int
        RIGID_BINDING_ANCHOR_TYPE: int
        SOLVER_FACTOR: float
        USE_MINIMUM_DISTANCE_LIMIT: bool
        MINIMUM_DISTANCE_TYPE: int
        MINIMUM_ABSOLUTE_DISTANCE: float
        MINIMUM_RELATIVE_DISTANCE: float
        USE_MAXIMUM_DISTANCE_LIMIT: bool
        MAXIMUM_DISTANCE_TYPE: int
        MAXIMUM_ABSOLUTE_DISTANCE: float
        MAXIMUM_RELATIVE_DISTANCE: float
        ENABLE_SPRING_FORCE: bool
        ADJUST_BY_PARTICLE_MASS: bool
        SPRING_COEF: float
        DAMPER_COEF: float
        BURY_BINDING_ANCHORS: bool
        DEPTH: float
        BREAKABLE_BY_OVERSTRETCH: bool
        OVERSTRETCH_TYPE: int
        OVERSTRETCH_ABSOLUTE_LIMIT: float
        OVERSTRETCH_RELATIVE_LIMIT: float
        BIND_DISTANCE_FROM_DATA: bool
        BIND_DISTANCE_DATA_CREATOR: None
        BIND_GAP_FROM_DATA: bool
        BIND_GAP_DATA_CREATOR: None
        BREAKABILITY_MAX_FORCE_FROM_DATA: bool
        BREAKABILITY_MAX_FORCE_DATA_CREATOR: None
        BREAKABILITY_MAX_TORQUE_FROM_DATA: bool
        BREAKABILITY_MAX_TORQUE_DATA_CREATOR: None
        MAX_BINDS_PER_PARTICLE_FROM_DATA: bool
        MAX_BINDS_PER_PARTICLE_DATA_CREATOR: None
        BINDING_GROUPS_FROM_DATA: bool
        BINDING_GROUPS_DATA_CREATOR: None
        MINIMUM_DISTANCE_LIMIT_FROM_DATA: bool
        MINIMUM_DISTANCE_LIMIT_DATA_CREATOR: None
        MAXIMUM_DISTANCE_LIMIT_FROM_DATA: bool
        MAXIMUM_DISTANCE_LIMIT_DATA_CREATOR: None
        SPRING_FORCE_COEF_FROM_DATA: bool
        SPRING_FORCE_COEF_DATA_CREATOR: None
        SPRING_DAMPER_COEF_FROM_DATA: bool
        SPRING_DAMPER_COEF_DATA_CREATOR: None
        OVERSTRETCH_DISTANCE_LIMIT_FROM_DATA: bool
        OVERSTRETCH_DISTANCE_LIMIT_DATA_CREATOR: None
        NUM_ACTIVE_BINDINGS_TO_DATA: bool
        NUM_ACTIVE_BINDINGS_DATA_CREATOR: None
        NUM_BROKEN_BINDINGS_TO_DATA: bool
        NUM_BROKEN_BINDINGS_DATA_CREATOR: None
        NUM_BROKEN_BY_FORCE_TO_DATA: bool
        NUM_BROKEN_BY_FORCE_DATA_CREATOR: None
        AVERAGE_BINDING_LENGTH_TO_DATA: bool
        AVERAGE_BINDING_LENGTH_DATA_CREATOR: None
        MINIMUM_BINDING_LENGTH_TO_DATA: bool
        MINIMUM_BINDING_LENGTH_DATA_CREATOR: None
        MAXIMUM_BINDING_LENGTH_TO_DATA: bool
        MAXIMUM_BINDING_LENGTH_DATA_CREATOR: None
        AVERAGE_BREAKING_IMPULSE_TO_DATA: bool
        AVERAGE_BREAKING_IMPULSE_DATA_CREATOR: None
        MAXIMUM_BREAKING_IMPULSE_TO_DATA: bool
        MAXIMUM_BREAKING_IMPULSE_DATA_CREATOR: None
        ...
    class MP_InterCollision(Helper):
        SCOPE_TYPE: int
        SELECTED_EVENTS: MXSWrapperBase
        TEST_TYPE: int
        MIN_SPEED: float
        MAX_SPEED: float
        COLLISION_COUNT: int
        REPORT_TO_DATA_OPERATOR: bool
        ADDITIVE_COUNT: bool
        ...
    class MP_Shape(Helper):
        COLLIDE_TYPE: int
        DISPLAY_TYPE: int
        CONFORM_TO_PARTICLE_SHAPE: bool
        SHAPE_LENGTH: float
        SHAPE_WIDTH: float
        SHAPE_HEIGHT: float
        SCALE_TYPE: int
        SCALE: MXSWrapperBase
        COLOR: MXSWrapperBase
        WELD_THRESHOLD: float
        INFLATE_WIDTH: float
        SCALE_MARGIN: float
        RESTITUTION: float
        STATIC_FRICTION: float
        DYNAMIC_FRICTION: float
        MASS_TYPE: int
        MASS: float
        DENSITY: float
        INTERPENETRATION_TOLERANCE: float
        GENERATE_TOLERANCE_CHANNEL: bool
        COLLISION_GROUP: int
        ...
    class MP_Solvent(Helper):
        PARTICLES_TO_PARTICLES: bool
        PARTICLES_TO_DEFLECTORS: bool
        PARTICLES_TO_GROUND: bool
        LIMIT_SOLVENT_BY_LIST: bool
        GLUE_TESTS: MXSWrapperBase
        LIMIT_SOLVENT_BY_TIME: bool
        START: int
        STOP: int
        LIMIT_SOLVENT_BY_DATA: bool
        DATA_CHANNEL: None
        LIMIT_SOLVENT_BY_ICON: bool
        MODE: int
        ICON_SHAPE: int
        ICON_SIZE: float
        COLOR_COORDINATED: bool
        ...
    class MP_Switch(Helper):
        MATCH_POSITION: bool
        MATCH_SPEED: bool
        POSITION_SPEED_MATCH_TYPE: int
        POSITION_SPEED_START: int
        POSITION_SPEED_STOP: int
        POSITION_SPEED_ACTIVE: bool
        POSITION_SPEED_SYNC_TYPE: int
        USE_SPEED_LIMIT: bool
        SPEED_LIMIT: float
        MATCH_ROTATION: bool
        MATCH_SPIN: bool
        ROTATION_SPIN_MATCH_TYPE: int
        ROTATION_SPIN_START: int
        ROTATION_SPIN_STOP: int
        ROTATION_SPIN_ACTIVE: bool
        ROTATION_SPIN_SYNC_TYPE: int
        USE_SPIN_LIMIT: bool
        SPIN_LIMIT: float
        APPLY_ANTI_GRAVITY: bool
        ANTIGRAVITY_TYPE: int
        ANTIGRAVITY_START: int
        ANTIGRAVITY_STOP: int
        ANTIGRAVITY_ACTIVE: bool
        ANTI_GRAVITY_SYNC_TYPE: int
        TURN_OFF_SIMULATION: bool
        TURN_OFF_SIMULATION_TYPE: int
        TURN_OFF_START: int
        TURN_OFF_STOP: int
        TURN_OFF_ACTIVE: bool
        TURN_OFF_SYNC_TYPE: int
        ...
    class MP_World(Helper):
        PHYSX_WORLD_DRIVER: None
        SUPPRESS_EXPRESS_SAVE: bool
        PHYSX_DRIVER_TYPE: int
        ...
    class MP_Worldhelper(Helper):
        APPLY_GRAVITY: bool
        GRAVITY_ACCELERATION: float
        GROUND_COLLISION_PLANE: bool
        SET_WORLD_LIMITS: bool
        ICON_LENGTH: float
        ICON_WIDTH: float
        ICON_HEIGHT: float
        COLLISION_GROUP: int
        DEFAULT_RESTITUTION: float
        DEFAULT_STATIC_FRICTION: float
        DEFAULT_DYNAMIC_FRICTION: float
        RUN_BAKED_SIMULATION: bool
        RANGE_TYPE: int
        RANGE_START: int
        RANGE_FINISH: int
        UPDATE_VIEWPORTS: bool
        HIDE_ICON: bool
        HIDE_PARTICLE_BINDINGS: bool
        SHOW_BAKE_DIALOG: int
        SUBFRAME_FACTOR: int
        SUBFRAME_TYPE: int
        USE_TIME_SCALE: bool
        TIME_SCALE: float
        ENERGY_THRESHOLD: float
        SPEED_THRESHOLD: float
        SPIN_RATE_THRESHOLD: float
        SLEEP_THRESHOLD_TYPE: int
        BOUNCE_THRESHOLD: float
        ENABLE_MULTI_THREADING: bool
        THREAD_COUNT: int
        USE_HARDWARE_PPU: bool
        RESTRICTED_BROADPHASE: bool
        SAFE_MODE_SIMULATION: bool
        CALCULATION_LIMIT: int
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
        U_MAP: float
        V_MAP: float
        W_MAP: float
        SYNC_TYPE: int
        CHANNEL_TYPE: int
        MAP_CHANNEL: int
        SHOW_IN_VIEWPORT: bool
        ...
    class MappinglayerData(AttributeDef):
        ...
    class MaskTex(TextureMap):
        MAP: None
        MASK: None
        MAPENABLED: bool
        MASKENABLED: bool
        MASKINVERTED: bool
        ...
    class Material(MAXWrapper):
        ...
    class MaterialID(NodeGeneric):
        ...
    class MaterialIDRenderElement(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
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
        MR_NUMAREASAMPLES: int
        MR_ENABLELIGHTSHAPERENDERING: bool
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
        TYPEINCREATIONMETHOD: int
        TYPEINPOS: MXSWrapperBase
        TYPEINLENGTH: float
        TYPEINWIDTH: float
        LENGTH: float
        WIDTH: float
        LENGTHSEGS: int
        WIDTHSEGS: int
        DENSITY: float
        RENDERSCALE: float
        MAPCOORDS: bool
        ...
    class Mesh_Weld_Overlapping_Vertices(Primitive):
        ...
    class Meshsmooth(Modifier):
        SUBDIVMETHOD: int
        IGNORESEL: bool
        OLDMAPPING: bool
        ITERATIONS: int
        SMOOTHNESS: float
        USERENDERITERATIONS: bool
        RENDERITERATIONS: int
        USERENDERSMOOTHNESS: bool
        RENDERSMOOTHNESS: float
        FACETYPE: int
        KEEPCONVEX: bool
        UPDATE: int
        STRENGTH: float
        RELAX: float
        LIMITSURFACE: bool
        SMOOTHRESULT: bool
        SEPBYMATS: bool
        SEPBYSMGROUPS: bool
        IGNOREBACKFACING: bool
        DISPLAYCAGE: bool
        ISOLINEDISPLAY: bool
        CONTROLLEVEL: int
        USESOFTSEL: bool
        USEEDGEDIST: bool
        EDGEDIST: int
        AFFECTBACKFACING: bool
        FALLOFF: float
        PINCH: float
        BUBBLE: float
        RESET: int
        CAGECOLOR: MXSWrapperBase
        SELECTEDCAGECOLOR: MXSWrapperBase
        ...
    class MessageBox(Primitive):
        ...
    class MessageTextColor(Color):
        ...
    class Mirror(Modifier):
        COPY: bool
        OFFSET: float
        MIRROR_AXIS: int
        ...
    class MissingPathCache(Interface):
        ...
    class MixTexture(TextureMap):
        MIXAMOUNT: float
        LOWER: float
        UPPER: float
        USECURVE: bool
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1: None
        MAP2: None
        MASK: None
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        MASKENABLED: bool
        OUTPUT: MXSWrapperBase
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
        MR_NUMAREASAMPLES: int
        MR_ENABLELIGHTSHAPERENDERING: bool
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
        USETARGETDISTANCE: bool
        FOCALDEPTH: float
        DISPLAYPASSES: bool
        USEORIGINALLOCATION: bool
        TOTALPASSES: int
        SAMPLERADIUS: float
        SAMPLEBIAS: float
        NORMALIZEWEIGHTS: bool
        DITHERSTRENGTH: float
        TILESIZE: int
        DISABLEFILTERING: bool
        DISABLEANTIALIASING: bool
        ...
    class MultiPassMotionBlur(MPassCamEffect):
        DISPLAYPASSES: bool
        TOTALPASSES: int
        DURATION: float
        BIAS: float
        NORMALIZEWEIGHTS: bool
        DITHERSTRENGTH: float
        TILESIZE: int
        DISABLEFILTERING: bool
        DISABLEANTIALIASING: bool
        ...
    class MultiSubMaterial(Material):
        MATERIALLIST: MXSWrapperBase
        MAPENABLED: MXSWrapperBase
        NAMES: MXSWrapperBase
        MATERIALIDLIST: MXSWrapperBase
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
        WIDTH: float
        LENGTH: float
        HEIGHT: float
        WIDTHSEGS: int
        LENGTHSEGS: int
        HEIGHTSEGS: int
        ...
    class NvCapsule(GeometryClass):
        RADIUS: float
        HEIGHT: float
        HEIGHTTYPE: int
        ...
    class NvConstraint(Helper):
        BODY0: None
        BODY1: None
        HELPERSIZE: float
        LINEARMODEX: int
        LINEARMODEY: int
        LINEARMODEZ: int
        LINEARPOSITION: float
        LINEARRESTITUTION: float
        LINEARSPRING: float
        LINEARDAMPING: float
        SWING1MODE: int
        SWING1ANGLE: float
        SWING1RESTITUTION: float
        SWING1SPRING: float
        SWING1DAMPING: float
        SWING2MODE: int
        SWING2ANGLE: float
        SWING2RESTITUTION: float
        SWING2SPRING: float
        SWING2DAMPING: float
        TWISTMODE: int
        TWISTANGLELOW: float
        TWISTANGLEHIGH: float
        TWISTRESTITUTIONLOW: float
        TWISTRESTITUTIONHIGH: float
        TWISTSPRINGLOW: float
        TWISTSPRINGHIGH: float
        TWISTDAMPINGLOW: float
        TWISTDAMPINGHIGH: float
        POSSPRING: float
        POSDAMPING: float
        SWINGSPRING: float
        SWINGDAMPING: float
        TWISTSPRING: float
        TWISTDAMPING: float
        COLLISION: bool
        BREAKABLE: bool
        MAXFORCE: float
        MAXTORQUE: float
        GEARING: bool
        GEARRATIO: float
        USEPROJECTION: bool
        PROJECTIONMODE: int
        PROJECTIONDIST: float
        PROJECTIONANGLE: float
        CHILDATTACHPOINT: MXSWrapperBase
        CHILDINITIALTWIST: float
        SHOWVISUALIZER: bool
        USEACCELERATION: bool
        USEHARDLIMITS: bool
        ...
    class NvRagdoll(Helper):
        HELPERSIZE: float
        BONEGROUPS: None
        ROOTBONE: None
        RAGDOLLNODE: None
        RBTYPE: int
        MESHTYPE: int
        INFLATION: float
        WEIGHT: float
        JOINTS: None
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
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        COLORMODE: int
        ...
    class ObjectReferenceTarget(ReferenceTarget):
        TYPE: int
        STATIC_OBJECTS: bool
        SUBFRAME_PLACEMENT: bool
        SEPARATE_GROUP_MEMBERS: bool
        SEPARATE_CHILDREN: bool
        USE_T2: bool
        USE_I3: bool
        USE_V4: bool
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
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
        RENDERLOD: int
        VIEWLOD: int
        FACETHRESHOLD1: float
        EDGETHRESHOLD1: float
        BIAS1: float
        PRESERVEMAT1: bool
        PRESERVESMOOTH1: bool
        MAXEDGELENGTH1: float
        FACETHRESHOLD2: float
        EDGETHRESHOLD2: float
        BIAS2: float
        PRESERVEMAT2: bool
        PRESERVESMOOTH2: bool
        MAXEDGELENGTH2: float
        MANUALUPDATE: bool
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
        TYPE: int
        ANGLE_VALUE: float
        FLOAT_VALUE: float
        INTEGER_VALUE: int
        PERCENT_VALUE: float
        TIME_VALUE: int
        WORLD_VALUE: float
        SYNC_TYPE: int
        RANDOM_SEED: int
        USE_AS_MODIFIER: bool
        MODIFIER_TYPE: int
        ANGLE_OFFSET: float
        FLOAT_OFFSET: float
        INTEGER_OFFSET: int
        PERCENT_OFFSET: float
        TIME_OFFSET: int
        WORLD_UNIT_OFFSET: float
        REAL_FACTOR: float
        INTEGER_FACTOR: int
        FILTER: None
        INPUT_1: None
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
        PICK: None
        RENDERTIMEONLY: bool
        TIME: float
        RADIUS: float
        USECUSTOMBOUNDS: bool
        BOUNDSMIN: MXSWrapperBase
        BOUNDSMAX: MXSWrapperBase
        USEALLPFEVENTS: bool
        PFEVENTLIST: MXSWrapperBase
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
        PERCENT: float
        FOLLOW: bool
        PATH: None
        BANK: bool
        BANKAMOUNT: float
        SMOOTHNESS: float
        ALLOWUPSIDEDOWN: bool
        CONSTANTVEL: bool
        AXIS: int
        AXISFLIP: bool
        WEIGHT: MXSWrapperBase
        LOOP: bool
        RELATIVE: bool
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
        MAP1: None
        MAP2: None
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        SATURATION1: float
        SATURATION2: float
        SIZE: float
        LEVEL: float
        COORDS: MXSWrapperBase
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
        HEIGHT: float
        WIDTH: float
        DEPTH: float
        DOUBLE_DOORS: int
        FLIP_SWING: bool
        FLIP_HINGE: bool
        CREATE_FRAME: bool
        FRAME_WIDTH: float
        FRAME_DEPTH: float
        DOOR_OFFSET: float
        LEAF_THICKNESS: float
        STILES_TOP_RAIL: float
        BOTTOM_RAIL: float
        NUMBER_OF_PANELS_HORIZONTALLY: int
        NUMBER_OF_PANELS_VERTICALLY: int
        MUNTIN: float
        PANEL_TYPE: int
        GLASS_THICKNESS: float
        BEVEL_ANGLE: float
        PANEL_THICKNESS_1: float
        PANEL_THICKNESS_2: float
        PANEL_MIDDLE_THICKNESS: float
        PANEL_WIDTH_1: float
        PANEL_WIDTH_2: float
        GENERATE_MAPPING_COORDS: bool
        OPEN__DEGREES: float
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
        WEIGHT: MXSWrapperBase
        AVERAGE: bool
        ...
    class Point3_Script(Point3Controller):
        SCRIPT: str
        ...
    class Point4Controller(MAXWrapper):
        ...
    class Point4_ListDummyEntry(Point4Controller):
        ...
    class Point4_List(Point4Controller):
        WEIGHT: MXSWrapperBase
        AVERAGE: bool
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
        WEIGHT: MXSWrapperBase
        AVERAGE: bool
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
        HEIGHT: float
        WIDTH: float
        DEPTH: float
        HORIZONTAL_FRAME_WIDTH: float
        VERTICAL_FRAME_WIDTH: float
        FRAME_THICKNESS: float
        GLAZING_THICKNESS: float
        RAIL_WIDTH: float
        PERCENT_OPEN: int
        GENERATE_MAPPING_COORDS: bool
        MIDDLE_HEIGHT: float
        BOTTOM_HEIGHT: float
        ...
    class Prs(Matrix3Controller):
        ...
    class PseudoColorExposureControl(ToneOperator):
        MINIMUM: float
        MAXIMUM: float
        QUANTITY: int
        DISPLAY: int
        PHYSICALSCALE: float
        AUTOMATIC: bool
        SCALEFUNCTION: int
        UNITSYSTEMUSED: int
        ACTIVE: bool
        PROCESSBG: bool
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
        BODY0: None
        BODY1: None
        BREAKABLE: bool
        MAXFORCE: float
        MAXTORQUE: float
        COLLISION: bool
        PROJECTIONMODE: int
        PROJECTIONDIST: float
        PROJECTIONANGLE: float
        GEARING: bool
        GEARRATIO: float
        APTYPE: int
        SWING1_LIMITED: bool
        SWING1_LOCKED: bool
        SWING1_ANGLE: float
        SWING1_REST: float
        SWING1_SPRING: float
        SWING1_DAMP: float
        SWING2_LIMITED: bool
        SWING2_LOCKED: bool
        SWING2_ANGLE: float
        SWING2_REST: float
        SWING2_SPRING: float
        SWING2_DAMP: float
        TWIST_ENBL: bool
        TWISTLOW: float
        TWISTHIGH: float
        TWIST_REST: float
        TWIST_SPRING: float
        TWIST_DAMP: float
        TWIST_LMT: bool
        HELPERSIZE: float
        X_STATE: int
        Y_STATE: int
        Z_STATE: int
        XLATE_RAD: float
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
        WIDTH: float
        WIDTHSEGS: int
        MAPCOORDS: bool
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
        OUTPUT_TYPE: int
        INTEGER_DISTRIBUTION_TYPE: int
        REAL_DISTRIBUTION_TYPE: int
        VECTOR_DISTRIBUTION_TYPE: int
        PARAMETER_1: float
        PARAMETER_2: float
        PARAMETER_3: float
        POSITIVE_PARAMETER_1: float
        POSITIVE_PARAMETER_2: float
        POSITIVE_PARAMETER_3: float
        INTEGER_PARAMETER_1: int
        INTEGER_PARAMETER_2: int
        INTEGER_PARAMETER_3: int
        SYNC_TYPE: int
        RANDOM_SEED: int
        USE_E3: bool
        USE_E4: bool
        USE_E5: bool
        USE_E6: bool
        USE_E7: bool
        ITERATIONS: float
        FILTER: None
        INPUT_1: None
        INPUT_2: None
        INPUT_3: None
        INPUT_4: None
        INPUT_5: None
        INPUT_6: None
        INPUT_7: None
        ...
    class RaytraceShadow(Shadow):
        RAYTRACEBIAS: float
        MAXDEPTH: int
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
        SIZE: int
        BLUR: float
        BLUROFFSET: float
        NEAR: float
        FAR: float
        SOURCE: int
        USEATMOSPHERICMAP: bool
        APPLY: bool
        FRAMETYPE: int
        NTHFRAME: int
        BITMAPNAME: MXSWrapperBase
        OUTPUTNAME: None
        ...
    class ReflectionRenderElement(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ...
    class RefractionRenderElement(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
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
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1: None
        MAP2: None
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        ALPHAFROM: int
        ...
    class RgbTint(TextureMap):
        RED: MXSWrapperBase
        GREEN: MXSWrapperBase
        BLUE: MXSWrapperBase
        MAP1: None
        MAP1ENABLED: bool
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
        EULER_X: float
        EULER_Y: float
        EULER_Z: float
        DIVERGENCE: float
        RESTRICT_DIVERGENCE_TO_AXIS: bool
        DIVERGENCE_AXIS_X: float
        DIVERGENCE_AXIS_Y: float
        DIVERGENCE_AXIS_Z: float
        RANDOM_SEED: int
        ...
    class RotationController(MAXWrapper):
        ...
    class Rotation_ListDummyEntry(RotationController):
        ...
    class Rotation_List(RotationController):
        WEIGHT: MXSWrapperBase
        AVERAGE: bool
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
        WEIGHT: MXSWrapperBase
        AVERAGE: bool
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
        LENGTH: float
        WIDTH: float
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
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
        TWOSIDEDSHADOWS: bool
        MAPSIZE: int
        SAMPLERANGE: float
        MAPBIAS: float
        ABSOLUTEMAPBIAS: bool
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
        VALUE: float
        MINVAL: float
        MAXVAL: float
        XPOS: float
        YPOS: float
        WIDTH: float
        HIDE: bool
        SLDNAME: str
        SNAPTOGGLE: bool
        SNAPVAL: float
        ...
    class SliderTime(Time):
        ...
    class Smooth(Modifier):
        AUTOSMOOTH: bool
        PREVENTINDIRECT: bool
        THRESHOLD: float
        SMOOTHINGBITS: int
        ...
    class SmoothReferenceTarget(ReferenceTarget):
        OBJECTS: MXSWrapperBase
        FILTERDELEGATES: bool
        WHOLEANIM: int
        FROM: int
        TO: int
        POSITIONS: bool
        ROTATIONS: bool
        REDUCE: bool
        N: int
        FILTER: bool
        PASTKEYS: int
        FUTUREKEYS: int
        SMOOTHNESS: int
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
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        OUTPUTSZX: int
        OUTPUTSZY: int
        AUTOSZON: bool
        FILENAME: str
        FILENAMEUNIQUE: bool
        FILETYPE: str
        BACKGROUNDCOLOR: MXSWrapperBase
        LIGHTINGON: bool
        SHADOWSON: bool
        TARGETMAPSLOTNAME: str
        ...
    class SpecularRenderElement(RenderElement):
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
        ...
    class Speed(Helper):
        SPEED: float
        VARIATION: float
        DIRECTION: int
        REVERSE: bool
        DIVERGENCE: float
        RANDOM_SEED: int
        ...
    class Spin(Helper):
        SPINRATE: float
        VARIATION: float
        DIRECTION: int
        SPIN_X_AXIS: float
        SPIN_Y_AXIS: float
        SPIN_Z_AXIS: float
        DIVERGENCE: float
        RANDOM_SEED: int
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
        SHADERTYPE: int
        WIRE: bool
        TWOSIDED: bool
        FACEMAP: bool
        FACETED: bool
        SHADERBYNAME: str
        OPACITYTYPE: int
        OPACITY: float
        FILTERCOLOR: MXSWrapperBase
        FILTERMAP: None
        OPACITYFALLOFFTYPE: int
        OPACITYFALLOFF: float
        IOR: float
        WIRESIZE: float
        WIREUNITS: int
        APPLYREFLECTIONDIMMING: bool
        DIMLEVEL: float
        REFLECTIONLEVEL: float
        SAMPLER: int
        SAMPLERQUALITY: float
        SAMPLERENABLE: bool
        SAMPLERADAPTTHRESHOLD: float
        SAMPLERADAPTON: bool
        SUBSAMPLETEXTUREON: bool
        SAMPLERADVANCEDOPTIONS: bool
        SAMPLERBYNAME: str
        USERPARAM0: float
        USERPARAM1: float
        SAMPLERUSEGLOBAL: bool
        MAPENABLES: MXSWrapperBase
        MAPS: MXSWrapperBase
        MAPAMOUNTS: MXSWrapperBase
        ADTEXTURELOCK: bool
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
        SIZE: float
        SUBDIVIDEDOENFORCEQUALITY: bool
        SUBDIVIDEDOSUBDIVIDETRIANGLES: bool
        SHOWALLTRIANGLES: bool
        SUBDIVIDEMAXSTEINERPOINTS: int
        SUBDIVIDEQUADAREARATIO: float
        SUBDIVIDEDIAGONALRATIO: float
        SUBDIVIDENUMBUCKETS: int
        SUBDIVIDEDOFORMQUADS: bool
        SUBDIVIDEREFINEMENTTYPE: int
        MANUALUPDATE: int
        REMESHTYPE: int
        PRESERVEMESHDATA: bool
        PRESERVEDMAPINDEX: int
        PRESERVESHARPEDGESBYANGLE: bool
        PRESERVEDSHARPEDGEANGLE: float
        DELAUNAYSIZE: float
        DELAUNAYRELAXATIONCOEFF: float
        DELAUNAYRELAXATIONITERATIONS: int
        ADAPTIVEEDGELENGTH: float
        ADAPTIVEREGULARITY: float
        ADAPTIVETHRESHOLD: float
        VARIABLECURVATUREEDGELENGTH: float
        VARIABLECURVATUREREGULARITY: float
        VARIABLECURVATURETHRESHOLD: float
        VARIABLECURVATUREVARIABLEDENSITY: float
        VARIABLECURVATUREITERATIONS: int
        VARIABLECURVATURETRANSITION: float
        ...
    class SubdivideSegment(Primitive):
        ...
    class SubdivideSpacewarpModifier(SpacewarpModifier):
        SIZE: float
        SUBDIVIDEDOENFORCEQUALITY: bool
        SUBDIVIDEDOSUBDIVIDETRIANGLES: bool
        SHOWALLTRIANGLES: bool
        SUBDIVIDEMAXSTEINERPOINTS: int
        SUBDIVIDEQUADAREARATIO: float
        SUBDIVIDEDIAGONALRATIO: float
        SUBDIVIDENUMBUCKETS: int
        SUBDIVIDEDOFORMQUADS: bool
        SUBDIVIDEREFINEMENTTYPE: int
        MANUALUPDATE: int
        REMESHTYPE: int
        PRESERVEMESHDATA: bool
        PRESERVEDMAPINDEX: int
        PRESERVESHARPEDGESBYANGLE: bool
        PRESERVEDSHARPEDGEANGLE: float
        DELAUNAYSIZE: float
        DELAUNAYRELAXATIONCOEFF: float
        DELAUNAYRELAXATIONITERATIONS: int
        ADAPTIVEEDGELENGTH: float
        ADAPTIVEREGULARITY: float
        ADAPTIVETHRESHOLD: float
        VARIABLECURVATUREEDGELENGTH: float
        VARIABLECURVATUREREGULARITY: float
        VARIABLECURVATURETHRESHOLD: float
        VARIABLECURVATUREVARIABLEDENSITY: float
        VARIABLECURVATUREITERATIONS: int
        VARIABLECURVATURETRANSITION: float
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
        SHAPES: MXSWrapperBase
        UNIONINTERSECTIONS: bool
        CUSTOMSHAPENAME: None
        CURRENTBUILTINSHAPE: int
        CUSTOMSHAPE: int
        MIRRORXZPLANE: bool
        MIRRORXYPLANE: bool
        XOFFSET: float
        YOFFSET: float
        ANGLE: float
        GENERATEMAPPINGCOORDS: bool
        REALWORLDMAPSIZE: bool
        GENMATIDS: bool
        USESECTIONIDS: bool
        USEPATHIDS: bool
        PIVOTALIGNMENT: int
        SMOOTHSECTION: bool
        SMOOTHPATH: bool
        BANKING: bool
        ASSIGNCSTYPE: int
        ...
    class Swirl(TextureMap):
        SWIRL: MXSWrapperBase
        BASE: MXSWrapperBase
        SWIRL_INTENSITY: float
        TWIST: float
        COLOR_CONTRAST: float
        CENTER_POSITION_Y: float
        CENTER_POSITION_X: float
        SWIRL_AMOUNT: float
        CONSTANT_DETAIL: int
        RANDOM_SEED: float
        LOCK_BACKGROUND: int
        SWIRLMAP: None
        BASEMAP: None
        SWIRLMAPENABLED: bool
        BASEMAPENABLED: bool
        COORDS: MXSWrapperBase
        ...
    class Symmetry(Modifier):
        AXIS: int
        FLIP: bool
        SLICE: int
        WELD: int
        THRESHOLD: float
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
        ASPECT: float
        RGB: MXSWrapperBase
        COLOR: MXSWrapperBase
        CONTRAST: float
        ENABLED: bool
        ON: bool
        TYPE: MXSWrapperBase
        VALUE: int
        FALLOFF: float
        EXCLUDELIST: MXSWrapperBase
        INCLUDELIST: None
        SHOWCONE: bool
        MULTIPLIER: float
        SOFTENDIFFUSEEDGE: float
        HOTSPOT: float
        FARATTENSTART: float
        FARATTENEND: float
        NEARATTENSTART: float
        NEARATTENEND: float
        ATMOSOPACITY: float
        ATMOSCOLORAMT: float
        DECAYRADIUS: float
        SHADOWCOLOR: MXSWrapperBase
        SHADOWMULTIPLIER: float
        HSV: MXSWrapperBase
        HUE: int
        SATURATION: int
        INCLEXCLTYPE: int
        AFFECTDIFFUSE: bool
        AFFECTSPECULAR: bool
        USENEARATTEN: bool
        SHOWNEARATTEN: bool
        USEFARATTEN: bool
        SHOWFARATTEN: bool
        ATTENDECAY: int
        PROJECTOR: bool
        PROJECTORMAP: None
        CASTSHADOWS: bool
        USEGLOBALSHADOWSETTINGS: bool
        RAYTRACEDSHADOWS: bool
        OVERSHOOT: bool
        CONESHAPE: int
        LIGHTSHAPE: int
        ATMOSSHADOWS: bool
        LIGHTAFFECTSSHADOW: bool
        SHADOWPROJECTORMAP: None
        USESHADOWPROJECTORMAP: bool
        AMBIENTONLY: bool
        SHADOWGENERATOR: MXSWrapperBase
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
        TYPE: int
        TENSION: float
        ITERATIONS: int
        FACETYPE: int
        UPDATEWHEN: int
        ...
    class Test_Safearray(Primitive):
        ...
    class Text(Shape):
        SIZE: float
        STEPS: int
        TEXT: str
        RENDER_RENDERABLE: bool
        RENDER_MAPCOORDS: bool
        RENDER_VIEWPORT_THICKNESS: float
        RENDER_VIEWPORT_SIDES: int
        RENDER_VIEWPORT_ANGLE: float
        RENDER_DISPLAYRENDERMESH: bool
        RENDER_USEVIEWPORTSETTINGS: bool
        RENDER_DISPLAYRENDERSETTINGS: bool
        THICKNESS: float
        SIDES: int
        ANGLE: float
        RENDERABLE: bool
        MAPCOORDS: bool
        VIEWPORT_THICKNESS: float
        VIEWPORT_SIDES: int
        VIEWPORT_ANGLE: float
        DISPLAYRENDERMESH: bool
        USEVIEWPORTSETTINGS: bool
        DISPLAYRENDERSETTINGS: bool
        CAP: bool
        OPTIMIZE: bool
        ADAPTIVE: bool
        RENDER_VIEWPORT_LENGTH: float
        RENDER_VIEWPORT_WIDTH: float
        RENDER_VIEWPORT_ANGLE2: float
        RENDER_RECTANGULAR: bool
        RENDER_VIEWPORT_RECTANGULAR: bool
        RENDER_ASPECT_LOCKED: bool
        RENDER_VIEWPORT_ASPECT_LOCKED: bool
        RENDER_AUTO_SMOOTH: bool
        REALWORLDMAPSIZE: bool
        TWIST_CORRECTION: bool
        QUAD_CAP: bool
        SPHERE_CAP: float
        CAP_SEGMENTS: int
        KERNING: float
        LEADING: float
        FONT: str
        ITALIC: bool
        UNDERLINE: bool
        ALIGNMENT: int
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
        NODES: MXSWrapperBase
        DRAWRING: bool
        DRAWNORMAL: bool
        DRAWTRACE: bool
        MINSIZE: float
        MAXSIZE: float
        MINSTR: float
        MAXSTR: float
        ADDITIVEMODE: bool
        FALLOFFGRAPH: MXSWrapperBase
        PRESSUREENABLE: bool
        PRESSUREAFFECTS: int
        UPDATEONMOUSEUP: bool
        QUADDEPTH: int
        PREDEFINEDSTRENABLE: bool
        PREDEFINEDSTRGRAPH: MXSWrapperBase
        PREDEFINEDSIZEENABLE: bool
        PREDEFINEDSIZEGRAPH: MXSWrapperBase
        MIRRORENABLE: bool
        MIRRORAXIS: int
        MIRROROFFSET: float
        MIRRORGIZMOSIZE: float
        POINTGATHERENABLE: bool
        BUILDVNORMALS: bool
        LAGRATE: int
        NORMALSCALE: float
        MARKER: float
        MARKERENABLE: bool
        OFFMESHHITTYPE: bool
        OFFMESHHITZDEPTH: float
        OFFMESHHITPOS: MXSWrapperBase
        STRDRAGLIMITMIN: float
        STRDRAGLIMITMAX: float
        SPLINECONSTRAINTNODE: None
        ...
    class ThinWallRefraction(TextureMap):
        BLUR: float
        THICKNESSOFFSET: float
        BUMPMAPEFFECT: float
        APPLYBLUR: bool
        NTHFRAME: int
        USEENVIROMENT: bool
        FRAME: int
        ...
    class Threads(Primitive):
        ...
    class Tifio(BitmapIO):
        ...
    class Tiles(TextureMap):
        BRICKS: None
        MORTAR_MAP: None
        BRICKS_MAP: None
        MORTAR: None
        RANDOM_SEED: int
        MORTAR_COLOR: MXSWrapperBase
        BRICK_COLOR: MXSWrapperBase
        HORIZONTAL_COUNT: float
        VERTICAL_COUNT: float
        COLOR_VARIANCE: float
        VERTICAL_GAP: float
        HORIZONTAL_GAP: float
        LINE_SHIFT: float
        RANDOM_SHIFT: float
        HOLES: int
        LOCK_GAP_SYMMETRY: int
        FADE_VARIANCE: float
        EDGE_ROUGHNESS: float
        SHOW_TEXTURE_SWATCHES: int
        USE_ROW_EDIT: int
        USE_COLUMN_EDIT: int
        CHANGE_ROW: float
        CHANGE_COLUMN: float
        PER_COLUMN: int
        PER_ROW: int
        TILE_TYPE: int
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
        TOPMATERIAL: MXSWrapperBase
        BOTTOMMATERIAL: MXSWrapperBase
        MAP1ENABLED: bool
        MAP2ENABLED: bool
        BLEND: float
        POSITION: float
        COORDINATES: int
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
        WIDTH: float
        MAPCOORDS: bool
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
        ENABLED: bool
        FILTERON: bool
        ELEMENTNAME: str
        BITMAP: None
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
        NUMWAVESETS: int
        WAVERADIUS: float
        WAVELENMIN: float
        WAVELENMAX: float
        AMPLITUDE: float
        PHASE: float
        DISTRIBUTION: int
        RANDOMSEED: int
        COLOR1: MXSWrapperBase
        COLOR2: MXSWrapperBase
        MAP1: None
        MAP2: None
        MAP1ON: bool
        MAP2ON: bool
        COORDS: MXSWrapperBase
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
