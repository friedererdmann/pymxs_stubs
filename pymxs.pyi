class MXSWrapperBase():
    ...
class MXSWrapperObjectSet():
    ...
class MXSWrapperObjectSetIter():
    ...
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
        format: str
        Quality: str
        exposure: str
        renderType: str
        width: int
        height: int
        NotifyByEmail: bool
        alpha: bool
        ...
    class A360RendererPresetsHelper(ReferenceTarget):
        ...
    class A360_Cloud_Rendering(RendererClass):
        format: str
        Quality: str
        exposure: str
        renderType: str
        width: int
        height: int
        NotifyByEmail: bool
        alpha: bool
        ...
    class ACIS_SAT(ExporterPlugin):
        ...
    class ADTCategory(ReferenceTarget):
        ...
    class ADTObjMgrWrapper(floatController):
        ...
    class ADTStyle(ReferenceTarget):
        ...
    class ADTStyleComp(ReferenceTarget):
        ...
    class ADT_Category(ReferenceTarget):
        ...
    class ADT_Object_Manager(ReferenceTarget):
        ...
    class ADT_Object_Manager_Wrapper(floatController):
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
        enable_iterations: bool
        iterations: int
        quality_db: float
        enable_time: bool
        time_in_seconds: int
        time_split_seconds: int
        time_split_minutes: int
        time_split_hours: int
        motion_blur_all_objects: bool
        render_method: int
        point_light_diameter: float
        enable_outlier_clamp: bool
        anti_aliasing_filter_diameter: float
        enable_animated_noise: bool
        enable_noise_filter: bool
        noise_filter_strength: float
        noise_filter_strength_percentage: float
        texture_bake_resolution: int
        maximum_interactive_down_res_factor: int
        ...
    class ART_Renderer_Noise_Filter(RenderElement):
        elementName: str
        enabled: bool
        bitmap: bool
        strength: float
        strength_percentage: float
        ...
    class ASec_Element(ReferenceTarget):
        elementName: str
        minSize: float
        intensity: float
        maxSize: float
        axis: float
        quantity: int
        sides: int
        on: bool
        Squeeze: bool
        occlusion: float
        presets: int
        colorSource: float
        radialColor1: MXSWrapperBase
        radialColor2: MXSWrapperBase
        radialColor3: MXSWrapperBase
        radialColor4: MXSWrapperBase
        colorRadius1: float
        colorRadius2: float
        colorRadius3: float
        colorRadius4: float
        radialMtl: None
        useRadialMtl: bool
        radialMap: None
        useRadialMap: bool
        circularColorMix: float
        quadrant1Color: MXSWrapperBase
        quadrant2Color: MXSWrapperBase
        quadrant3Color: MXSWrapperBase
        quadrant4Color: MXSWrapperBase
        circularMtl: None
        useCircularMtl: bool
        circularMap: None
        useCircularMap: bool
        radialSizeMap: None
        useRadialSizeMap: bool
        applyLights: bool
        applyImage: bool
        applyImageCenters: bool
        sourceObjectID: bool
        objectID: int
        sourceEffectsID: bool
        effectsID: int
        sourceUnclampedColor: bool
        unclampedColor: float
        unclampedColorInvert: bool
        sourceSurfaceNormal: bool
        surfaceNormal: float
        surfaceNormalInvert: bool
        sourceWhole: bool
        sourceAlpha: bool
        alpha: int
        sourceZBuffer: bool
        zHi: float
        zLo: float
        filterAll: bool
        filterEdge: bool
        filterPerimeterAlpha: bool
        filterPerimeter: bool
        filterBrightness: bool
        brightness: int
        brightnessInvert: bool
        filterHue: bool
        hue: MXSWrapperBase
        hueRange: int
        applyNoise: bool
        noiseMap: None
        radialDensity: None
        useRadialDensity: bool
        ...
    class ATF_Alias_Import(ImporterPlugin):
        ...
    class ATF_Alias_importer(ImporterPlugin):
        ...
    class ATF_CATIA_V4_Import(ImporterPlugin):
        ...
    class ATF_CATIA_V4_importer(ImporterPlugin):
        ...
    class ATF_CATIA_V5_Import(ImporterPlugin):
        ...
    class ATF_CATIA_V5_importer(ImporterPlugin):
        ...
    class ATF_IGES_Import(ImporterPlugin):
        ...
    class ATF_IGES_importer(ImporterPlugin):
        ...
    class ATF_JT_Import(ImporterPlugin):
        ...
    class ATF_JT_importer(ImporterPlugin):
        ...
    class ATF_ProE_Import(ImporterPlugin):
        ...
    class ATF_ProE_importer(ImporterPlugin):
        ...
    class ATF_SKETCHUP_Import(ImporterPlugin):
        ...
    class ATF_STEP_Import(ImporterPlugin):
        ...
    class ATF_STEP_importer(ImporterPlugin):
        ...
    class ATF_Solidworks_Import(ImporterPlugin):
        ...
    class ATF_Solidworks_importer(ImporterPlugin):
        ...
    class ATF_UG_NX_Import(ImporterPlugin):
        ...
    class ATF_UG_NX_importer(ImporterPlugin):
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
        Enable: bool
        Quality: float
        Enable_Adaptive: bool
        Adaptive_Threshold: float
        ...
    class Adaptive_Uniform(SamplerClass):
        Enable: bool
        Quality: float
        Enable_Adaptive: bool
        Adaptive_Threshold: float
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
        shadow_Mode: int
        pass1: int
        pass2: int
        ray_Bias: float
        blur: float
        jitter_amt: float
        twoSidedShadows: bool
        noAreaShadows: bool
        shadow_Transparent: bool
        aa_threshold: MXSWrapperBase
        suppress_mat_aa: bool
        suppress_reflt_aa: bool
        skip_coplanar: bool
        coplanar_threshold: float
        ...
    class AdvancedWood(textureMap):
        coords: MXSWrapperBase
        preSet: int
        roughness: float
        early_wood_color: MXSWrapperBase
        early_wood_color_map: None
        late_wood_color_power: float
        use_manual_late_wood_color: bool
        manual_late_wood_color: MXSWrapperBase
        manual_late_wood_color_map: None
        ring_thickness: float
        diffuse_lobe_weight: float
        use_pores: bool
        pore_type: int
        pore_cell_dim: float
        pore_radius: float
        pore_color_power: float
        pore_depth: float
        use_rays: bool
        ray_color_power: float
        ray_seg_length_z: float
        ray_num_slices: int
        ray_ellipse_scale_x: float
        ray_ellipse_z2x: float
        late_wood_ratio: float
        early_wood_sharpness: float
        late_wood_sharpness: float
        fiber_perlin_scale_z: float
        diffuse_perlin_scale_z: float
        use_late_wood_bump: bool
        late_wood_bump_depth: float
        use_groove_roughness: bool
        groove_roughness: float
        use_fiber_perlin: bool
        use_fiber_cosine: bool
        use_growth_perlin: bool
        use_early_wood_color_perlin: bool
        use_late_wood_color_perlin: bool
        use_diffuse_perlin: bool
        fiber_perlin_prof: str
        fiber_cosine_prof: str
        growth_perlin_prof: str
        diffuse_perlin_prof: str
        early_wood_color_perlin_prof: str
        late_wood_color_perlin_prof: str
        scale: float
        axis: int
        unit_dependent: bool
        ...
    class Advanced_Lighting_Override(material):
        reflectanceScale: float
        colorBleed: float
        transmittanceScale: float
        luminanceScale: float
        bumpScale: float
        baseMaterial: MXSWrapperBase
        ...
    class Advanced_Ray_traced(Shadow):
        shadow_Mode: int
        pass1: int
        pass2: int
        ray_Bias: float
        blur: float
        jitter_amt: float
        twoSidedShadows: bool
        noAreaShadows: bool
        shadow_Transparent: bool
        aa_threshold: MXSWrapperBase
        suppress_mat_aa: bool
        suppress_reflt_aa: bool
        skip_coplanar: bool
        coplanar_threshold: float
        ...
    class Affect_Region(modifier):
        falloff: float
        ignoreBackfacing: int
        pinch: float
        bubble: float
        ...
    class Age_Test(helper):
        Test_Type: int
        Condition_Type: int
        Test_Value: int
        variation: int
        Subframe_Sampling: bool
        Random_Seed: int
        Adjustable_Age: bool
        ...
    class AlembicCamera(camera):
        ...
    class AlembicContainer(GeometryClass):
        nodes: MXSWrapperBase
        iconScale: float
        showIcon: bool
        ...
    class AlembicDummyObject(helper):
        ...
    class AlembicExport(ExporterPlugin):
        ...
    class AlembicFloat(floatController):
        source: str
        object: None
        playbackType: int
        playbackStart: float
        playbackEnd: float
        playbackFrame: float
        propertyPath: None
        visControl: bool
        rankIndex: int
        importVisibility: bool
        playbackTypeGen: int
        playbackStartGen: int
        playbackEndGen: int
        playbackFrameGen: int
        ...
    class AlembicImport(ImporterPlugin):
        ...
    class AlembicObject(GeometryClass):
        source: str
        object: None
        playbackType: int
        playbackStart: float
        playbackEnd: float
        playbackFrame: float
        importUVs: bool
        importNormals: bool
        importVertexColors: bool
        importExtraChannels: bool
        importVelocity: bool
        importMaterialIDs: bool
        importCustomAttributes: bool
        playbackTypeGen: int
        playbackStartGen: int
        playbackEndGen: int
        playbackFrameGen: int
        generationId: int
        ...
    class AlembicXform(Matrix3Controller):
        source: str
        object: None
        playbackType: int
        playbackStart: float
        playbackEnd: float
        playbackFrame: float
        maxcoords: bool
        playbackTypeGen: int
        playbackStartGen: int
        playbackEndGen: int
        playbackFrameGen: int
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
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        ...
    class AlwaysEqualFilter(ReferenceMaker):
        ...
    class AmbientOcclusionBakeElement(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        Samples: int
        bright: MXSWrapperBase
        dark: MXSWrapperBase
        spread: float
        maxDistance: float
        falloff: float
        ...
    class Ambient_Occlusion(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        Samples: int
        bright: MXSWrapperBase
        dark: MXSWrapperBase
        spread: float
        maxDistance: float
        falloff: float
        ...
    class AmountChange(ReferenceTarget):
        type: int
        Sub_Type: int
        Reset_Particle_Age: bool
        Spawns_As_New_In_Event: bool
        Proceed_Type: int
        History_Dependent: bool
        Execution_Order: int
        Use_Is_Current_Parent: bool
        Is_Current_Parent_Data_Channel: None
        Use_Is_Current_Spawn: bool
        Is_Current_Spawn_Data_Channel: None
        Use_Parent_ID: bool
        Parent_ID_Data_Channel: None
        Use_Last_Spawn_ID: bool
        Last_Spawn_ID_Data_Channel: None
        Use_First_Spawn_ID: bool
        First_Spawn_ID_Data_Channel: None
        Use_Current_First_Spawn_ID: bool
        Current_First_Spawn_ID_Data_Channel: None
        Use_Older_Sibling_ID: bool
        Older_Sibling_ID_Data_Channel: None
        Use_Current_Spawn_Count: bool
        Current_Spawn_Count_Data_Channel: None
        Use_Total_Spawn_Count: bool
        Total_Spawn_Count_Data_Channel: None
        Use_Current_Spawn_Order: bool
        Current_Spawn_Order_Data_Channel: None
        filter: None
        Input_1: None
        ...
    class AnaglyphFragment(GraphicsFragmentPlugin):
        ...
    class Anchor(helper):
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
    class Apollo_Effect(renderEffect):
        seed: int
        size: float
        angle: float
        intensity: float
        Squeeze: float
        affectAlpha: bool
        affectZBuffer: bool
        distAffectsSize: bool
        distAffectsIntensity: bool
        centerAffectsSize: bool
        centerAffectsIntensity: bool
        innerOcclusionRadius: float
        occlusionAffectsSize: bool
        outerOcclusionRadius: float
        occlusionAffectsIntensity: bool
        affectByAtmosphere: bool
        lightDirectionAffectsSize: bool
        lightDirectionAffectsIntensity: bool
        ...
    class Apollo_Param_Container(GeometryClass):
        ...
    class AppendSubSelSet(Primitive):
        ...
    class ApplyOperation(MAXScriptFunction):
        ...
    class ApplyUVAsColor(modifier):
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class ApplyUVAsHSLColor(modifier):
        Hue_Minimum: float
        Hue_Maximum: float
        Saturation_Minimum: float
        Saturation_Maximum: float
        Luminance_Minimum: float
        Luminance_Maximum: float
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class ApplyUVAsHSLGradient(modifier):
        Use_V_for_Hue: bool
        Color_1: MXSWrapperBase
        Color_2: MXSWrapperBase
        Color_3: MXSWrapperBase
        Use_V_for_Saturation: bool
        Use_V_for_Lightness: bool
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class ApplyUVAsHSLGradientWithMidpoint(modifier):
        Use_V_for_Hue: bool
        Midpoint: float
        Color_1: MXSWrapperBase
        Color_2: MXSWrapperBase
        Ease_A: float
        Color_3: MXSWrapperBase
        Ease_B: float
        Use_V_for_Saturation: bool
        Use_V_for_Lightness: bool
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class ArbAxis(Primitive):
        ...
    class ArbBone(Matrix3Controller):
        ...
    class ArbBoneTrans(Matrix3Controller):
        ...
    class Arc(shape):
        steps: int
        to: float
        radius: float
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        reverse: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        pie: bool
        ...
    class Architectural(material):
        template: str
        Diffuse: MXSWrapperBase
        ior: float
        twoSided: bool
        emitLuminance: bool
        colorBleed: float
        reflectanceScale: float
        indirectBumpAmount: float
        transmittanceScale: float
        useTextureSize: bool
        textureWidth: float
        textureHeight: float
        textureUOffset: float
        textureVOffset: float
        rawDiffuseTexture: bool
        sampler: int
        samplerQuality: float
        samplerEnable: bool
        samplerAdaptThreshold: float
        samplerAdaptOn: bool
        subSampleTextureOn: bool
        samplerAdvancedOptions: bool
        samplerByName: str
        UserParam0: float
        UserParam1: float
        samplerUseGlobal: bool
        diffuseMap: None
        filterMap: None
        shininessMap: None
        luminanceMap: None
        bumpMap: None
        displacementMap: None
        translucencyMap: None
        cutoutMap: None
        intensityMap: None
        diffuseMapAmount: float
        shininess: float
        transparency: float
        luminance: float
        bumpMapAmount: float
        displacementMapAmount: float
        translucency: float
        cutoutMapAmount: float
        intensityMapAmount: float
        diffuseMapEnable: bool
        shininessMapEnable: bool
        transparencyMapEnable: bool
        luminanceMapEnable: bool
        bumpMapEnable: bool
        displacementMapEnable: bool
        translucencyEnable: bool
        cutoutMapEnable: bool
        intensityMapEnable: bool
        maps: MXSWrapperBase
        mapAmounts: MXSWrapperBase
        mapsEnables: MXSWrapperBase
        ...
    class ArchitecturalMaterial(material):
        template: str
        Diffuse: MXSWrapperBase
        ior: float
        twoSided: bool
        emitLuminance: bool
        colorBleed: float
        reflectanceScale: float
        indirectBumpAmount: float
        transmittanceScale: float
        useTextureSize: bool
        textureWidth: float
        textureHeight: float
        textureUOffset: float
        textureVOffset: float
        rawDiffuseTexture: bool
        sampler: int
        samplerQuality: float
        samplerEnable: bool
        samplerAdaptThreshold: float
        samplerAdaptOn: bool
        subSampleTextureOn: bool
        samplerAdvancedOptions: bool
        samplerByName: str
        UserParam0: float
        UserParam1: float
        samplerUseGlobal: bool
        diffuseMap: None
        filterMap: None
        shininessMap: None
        luminanceMap: None
        bumpMap: None
        displacementMap: None
        translucencyMap: None
        cutoutMap: None
        intensityMap: None
        diffuseMapAmount: float
        shininess: float
        transparency: float
        luminance: float
        bumpMapAmount: float
        displacementMapAmount: float
        translucency: float
        cutoutMapAmount: float
        intensityMapAmount: float
        diffuseMapEnable: bool
        shininessMapEnable: bool
        transparencyMapEnable: bool
        luminanceMapEnable: bool
        bumpMapEnable: bool
        displacementMapEnable: bool
        translucencyEnable: bool
        cutoutMapEnable: bool
        intensityMapEnable: bool
        maps: MXSWrapperBase
        mapAmounts: MXSWrapperBase
        mapsEnables: MXSWrapperBase
        ...
    class Area(filter):
        ...
    class Area_Shadows(Shadow):
        shadow_Mode: int
        pass1: int
        pass2: int
        ray_Bias: float
        blur: float
        shadow_width: float
        shadow_length: float
        shadow_height: float
        jitter_amt: float
        twoSidedShadows: bool
        shadow_Transparent: bool
        aa_threshold: MXSWrapperBase
        suppress_mat_aa: bool
        suppress_reflt_aa: bool
        skip_coplanar: bool
        coplanar_threshold: float
        ...
    class Arnold(RendererClass):
        prepass_enabled: bool
        prepass_samples: int
        AA_samples: int
        GI_diffuse_samples: int
        GI_diffuse_depth: int
        GI_specular_samples: int
        GI_specular_depth: int
        GI_transmission_samples: int
        GI_transmission_depth: int
        GI_sss_samples: int
        GI_volume_samples: int
        GI_volume_depth: int
        enable_adaptive_sampling: bool
        AA_samples_max: int
        Adaptive_Threshold: float
        progressive_render: bool
        GI_total_depth: int
        auto_transparency_depth: int
        low_light_threshold: float
        lock_sampling_pattern: bool
        sss_use_autobump: bool
        indirect_specular_blur: float
        filter: int
        filter_width: float
        AA_sample_clamp_enabled: bool
        AA_sample_clamp_affects_aovs: bool
        AA_sample_clamp: float
        indirect_sample_clamp: float
        physical_material_sss_type: int
        dielectric_priorities: bool
        env_mode: int
        env_ibl_samples: int
        env_phys_bgnd_mode: int
        env_phys_bgnd_color: MXSWrapperBase
        env_phys_bgnd_map: None
        env_ibl_enable: bool
        env_adv_ibl_multiplier: float
        env_adv_ibl_volume_samples: int
        env_adv_ibl_portal_mode: int
        env_adv_ibl_max_bounces: int
        env_adv_ibl_resolution_enable: bool
        env_adv_ibl_resolution: int
        env_adv_ibl_emit_camera: bool
        env_adv_ibl_emit_diffuse: bool
        env_adv_ibl_emit_specular: bool
        env_adv_ibl_emit_transmission: bool
        env_adv_ibl_affect_sss: bool
        env_adv_ibl_affect_indirect: bool
        env_adv_ibl_affect_volume: bool
        env_adv_ibl_camera_mult: float
        env_adv_ibl_diffuse_mult: float
        env_adv_ibl_specular_mult: float
        env_adv_ibl_transmission_mult: float
        env_adv_ibl_sss_mult: float
        env_adv_ibl_indirect_mult: float
        env_adv_ibl_volume_mult: float
        env_adv_ibl_cast_shadows: bool
        env_adv_ibl_shadow_color: MXSWrapperBase
        env_adv_ibl_shadow_density: float
        env_adv_bgnd_mode: int
        env_adv_bgnd_visible_to_camera: bool
        env_adv_bgnd_visible_to_diffuse_reflections: bool
        env_adv_bgnd_visible_to_specular_reflections: bool
        env_adv_bgnd_visible_to_diffuse_transmission: bool
        env_adv_bgnd_visible_to_specular_transmission: bool
        env_adv_bgnd_visible_to_volume_scattering: bool
        env_adv_bgnd_custom_color: MXSWrapperBase
        env_adv_bgnd_custom_map: None
        env_adv_bgnd_custom_shader: None
        Atmosphere: None
        respect_physical_camera_motion_blur: bool
        enable_transform_keys: bool
        transform_keys: int
        enable_deform_keys: bool
        deform_keys: int
        shutter_length: float
        shutter_position: int
        auto_shutter: bool
        shutter_open: float
        shutter_close: float
        shutter_type: int
        ignore_motion_blur: bool
        max_subdivisions: int
        geometry_dicing_camera: None
        subdiv_frustum_culling: bool
        subdiv_frustum_padding: float
        displacement_default_subdiv_type: int
        displacement_default_subdiv_iterations: int
        displacement_default_subdiv_adaptive_error: float
        curves_default_basis: int
        curves_default_mode: int
        curves_default_min_pixel_width: float
        texture_automip: bool
        texture_accept_unmipped: bool
        texture_enable_autotile: bool
        texture_autotile: int
        texture_accept_untiled: bool
        use_existing_tx: bool
        texture_max_memory_MB: int
        texture_max_open_files: int
        gpu_max_texture_resolution: int
        bucket_scanning: int
        bucket_size: int
        show_bucket_corners_prod: bool
        show_bucket_corners_as: bool
        abort_on_license_fail: bool
        skip_license_check: bool
        legacy_3ds_max_map_support: bool
        autodetect_threads: bool
        threads: int
        gpu_selection: MXSWrapperBase
        gpu_rendering: bool
        render_device: int
        render_device_fallback: int
        default_gpu_names: str
        default_gpu_min_memory_MB: int
        gpu_auto_selection: bool
        use_optix_on_beauty: bool
        noice_input: str
        noice_output: str
        noice_anim_range: int
        noice_start_frame: int
        noice_end_frame: int
        noice_additional_frames: int
        noice_variance: float
        noice_search_radius: int
        noice_patch_radius: int
        noice_light_aov_names: str
        output_denoising_aovs: bool
        procedural_searchpath: None
        plugin_searchpath: None
        texture_searchpath: None
        verbosity_level: int
        log_to_console: bool
        log_to_file: bool
        log_file: None
        max_warnings: int
        texture_per_file_stats: bool
        log_render_stats: bool
        render_stats_file: None
        render_stats_mode: int
        log_render_profile: bool
        render_profile_file: None
        abort_on_error: bool
        abort_on_error_activeshade: bool
        error_color_bad_texture: MXSWrapperBase
        error_color_bad_shader: MXSWrapperBase
        error_color_bad_pixel: MXSWrapperBase
        ignore_textures: bool
        ignore_shaders: bool
        ignore_atmosphere: bool
        ignore_lights: bool
        ignore_shadows: bool
        ignore_subdivision: bool
        ignore_displacement: bool
        ignore_bump: bool
        ignore_smoothing: bool
        ignore_motion: bool
        ignore_dof: bool
        ignore_sss: bool
        ignore_operators: bool
        shader_override_enabled: bool
        shader_override: None
        enable_user_options: bool
        user_options: None
        export_to_ass: bool
        ass_file_path: None
        export_option: bool
        export_cameras: bool
        export_driversfilters: bool
        export_lights: bool
        export_geometry: bool
        export_shaders: bool
        export_operators: bool
        export_binary: bool
        expand_procedurals: bool
        export_to_mtlx: bool
        mtlx_file_path: None
        mtlx_look: str
        mtlx_properties: None
        mtlx_relative: bool
        mtlx_use_current_selection: bool
        operator_root: None
        operator_export_list: MXSWrapperBase
        operator_export_tree: bool
        material_export_list: MXSWrapperBase
        retranslate_all_frames: bool
        use_quads: int
        export_to_ass_origin: int
        use_render_view: bool
        render_view_settings: str
        imager_0: None
        AOV_Manager: None
        driver_type: None
        aov_shaders_mat_0: None
        aov_shaders_mat_1: None
        aov_shaders_mat_2: None
        aov_shaders_map_0: None
        aov_shaders_map_1: None
        aov_shaders_map_2: None
        ...
    class ArnoldAOV(ReferenceTarget):
        active: bool
        denoised: bool
        data: str
        name: None
        filter: str
        filterWidth: float
        lightGroup: str
        layerTolerance: float
        layerEnableFiltering: bool
        layerHalfPrecision: bool
        ...
    class ArnoldAOVsManager(ReferenceTarget):
        ...
    class ArnoldAOVsManagerClassDescCreator(Interface):
        ...
    class ArnoldDEEPEXRDriver(ReferenceTarget):
        active: bool
        filenameSuffix: None
        name: None
        useAovName: bool
        tiled: bool
        append: bool
        subpixelMerge: bool
        useRGBOpacity: bool
        alphaTolerance: float
        depthTolerance: float
        alphaHalfPrecision: bool
        depthHalfPrecision: bool
        customAttributes: None
        aovList: MXSWrapperBase
        lightGroup: str
        ...
    class ArnoldEXRDriver(ReferenceTarget):
        active: bool
        filenameSuffix: None
        name: None
        useAovName: bool
        compression: str
        halfPrecision: bool
        tiled: bool
        preserveLayerName: bool
        autocrop: bool
        append: bool
        customAttributes: None
        aovList: MXSWrapperBase
        lightGroup: str
        ...
    class ArnoldFluidUtility(Interface):
        ...
    class ArnoldGeometryPropertiesModifier(modifier):
        enable_visibility_options: bool
        primary_visibility: bool
        visible_to_diffuse_reflections: bool
        visible_to_specular_reflections: bool
        visible_to_diffuse_transmission: bool
        visible_to_specular_transmission: bool
        visible_to_volume_scattering: bool
        enable_shadow_options: bool
        casts_shadows: bool
        receive_shadows: bool
        self_shadows: bool
        enable_general_options: bool
        double_sided: bool
        invert_normals: bool
        opaque: bool
        Matte: bool
        enable_mikkt: bool
        mikkt_uv_channel: int
        enable_displacement_options: bool
        displacement_height: float
        displacement_zero: float
        displacement_bounds_padding: float
        displacement_enable_autobump: bool
        autobump_camera: bool
        autobump_diffuse_reflections: bool
        autobump_specular_reflections: bool
        autobump_diffuse_transmission: bool
        autobump_specular_transmission: bool
        autobump_volume_scattering: bool
        displacement_map_on: bool
        displacement_map: None
        enable_subdivision_options: bool
        subdivision_type: int
        subdivision_iterations: int
        subdivision_metric: int
        subdivision_adaptive_error: float
        subdivision_space: int
        subdivision_uv_type: int
        subdivision_smooth_tangents: bool
        subdiv_frustum_ignore: bool
        motion_blur_use_transform: bool
        motion_blur_transform_keys: int
        motion_blur_use_deformation: bool
        motion_blur_deformation_keys: int
        enable_sss_options: bool
        sss_set_name: None
        enable_toon_options: bool
        toon_id: None
        enable_volume: bool
        Step_Size: float
        volume_padding: float
        enable_points: bool
        min_pixel_width: float
        mode: int
        particle_sys_as_points: bool
        enable_user_options: bool
        user_options: None
        trace_sets: None
        enable_light_group: bool
        light_group: MXSWrapperBase
        enable_shadow_group: bool
        shadow_group: MXSWrapperBase
        enable_camera: bool
        radial_distortion: float
        enable_filtermap: bool
        filterMap: None
        enable_uv_remap: bool
        uv_remap: None
        radial_distortion_type: int
        ...
    class ArnoldJPEGDriver(ReferenceTarget):
        active: bool
        filenameSuffix: None
        name: None
        useAovName: bool
        outputPadded: bool
        color_space: int
        dither: bool
        Quality: int
        aovList: MXSWrapperBase
        lightGroup: str
        ...
    class ArnoldLightBlockerFilterModifier(modifier):
        geometry_type: int
        density: float
        roundness: float
        width_edge: float
        height_edge: float
        ramp: float
        axis: int
        positionX: float
        positionY: float
        positionZ: float
        rotationX: float
        rotationY: float
        rotationZ: float
        scaleX: float
        scaleY: float
        scaleZ: float
        object: None
        useShader: bool
        Shader: None
        ...
    class ArnoldLightFilterModifier(modifier):
        lightFilter: None
        viewportShape: None
        viewportData: None
        ...
    class ArnoldMapToMtl(material):
        SurfaceShader: None
        SurfaceShaderEnabled: bool
        OpaqueEnabled: bool
        ...
    class ArnoldPNGDriver(ReferenceTarget):
        active: bool
        filenameSuffix: None
        name: None
        useAovName: bool
        format: None
        outputPadded: bool
        color_space: int
        dither: bool
        aovList: MXSWrapperBase
        lightGroup: str
        ...
    class ArnoldSceneSourceExport(ExporterPlugin):
        ...
    class ArnoldShadersLoader(GlobalUtilityPlugin):
        ...
    class ArnoldTIFFDriver(ReferenceTarget):
        active: bool
        filenameSuffix: None
        name: None
        useAovName: bool
        compression: str
        format: None
        tiled: bool
        outputPadded: bool
        color_space: int
        dither: bool
        unpremultAlpha: bool
        skipAlpha: bool
        append: bool
        aovList: MXSWrapperBase
        lightGroup: str
        ...
    class Arnold_A(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_Alembic_Object(GeometryClass):
        filename: str
        name_space: str
        nameprefix: str
        objectpath: str
        frame: float
        fps: float
        exclude_xform: bool
        make_instance: bool
        subdiv_iterations: int
        flip_v: bool
        scene_camera: str
        pull_user_params: bool
        velocity_ignore: bool
        velocity_scale: float
        visibility_ignore: bool
        expand_hidden: bool
        radius_attribute: str
        radius_default: float
        radius_scale: float
        UpAxis: int
        BBoxLow: MXSWrapperBase
        BBoxHi: MXSWrapperBase
        operator: None
        Layers: MXSWrapperBase
        animated: bool
        AnimSequenceStart: int
        AnimSequenceEnd: int
        AnimAnimStart: int
        AnimAnimEnd: int
        AnimSpeed: float
        AnimPingPong: bool
        AnimLoop: bool
        AnimExtend: bool
        viewport_mode: int
        bbox_threshold: float
        use_bbox_threshold: bool
        animation_cache: int
        use_animation_cache: bool
        use_vp_animation: bool
        ...
    class Arnold_Barndoor(modifier):
        arnold_node: str
        arnold_node_barndoor_top_left: float
        arnold_node_barndoor_top_right: float
        arnold_node_barndoor_top_edge: float
        arnold_node_barndoor_right_top: float
        arnold_node_barndoor_right_bottom: float
        arnold_node_barndoor_right_edge: float
        arnold_node_barndoor_bottom_left: float
        arnold_node_barndoor_bottom_right: float
        arnold_node_barndoor_bottom_edge: float
        arnold_node_barndoor_left_top: float
        arnold_node_barndoor_left_bottom: float
        arnold_node_barndoor_left_edge: float
        ...
    class Arnold_Light(light):
        on: bool
        targeted: bool
        targdist: float
        useColor: bool
        color: MXSWrapperBase
        usePreset: bool
        preSet: int
        useKelvin: bool
        kelvin: float
        filter: MXSWrapperBase
        intensity: float
        exposure: float
        normalize: bool
        Samples: int
        volume_samples: int
        shapeType: int
        lightRadius: float
        lightShapeVisible: bool
        cast_shadows: bool
        cast_volumetric_shadows: bool
        shadow_color: MXSWrapperBase
        shadow_density: float
        camera: float
        Diffuse: float
        Specular: float
        transmission: float
        sss: float
        indirect: float
        max_bounces: int
        affectViewport: bool
        spread: float
        quadX: float
        quadY: float
        height: float
        angle: float
        lens_radius: float
        penumbra_angle: float
        aspect_ratio: float
        spotRoundness: float
        quadRoundness: float
        soft_edge: float
        userOptions: None
        filename: str
        resolution: int
        format: int
        useTexmap: bool
        texmap: None
        lightMesh: None
        alwaysVisibleInViewport: bool
        volume: float
        aov: str
        Cone_Angle: float
        photometricRadius: float
        portal: bool
        portal_mode: int
        aov_indirect: bool
        ...
    class Arnold_Light_Decay(modifier):
        arnold_node: str
        arnold_node_use_near_atten: bool
        show_near_atten: bool
        arnold_node_near_start: float
        arnold_node_near_end: float
        arnold_node_use_far_atten: bool
        show_far_atten: bool
        arnold_node_far_start: float
        arnold_node_far_end: float
        ...
    class Arnold_Light_Gobo(modifier):
        arnold_node: str
        arnold_node_density: float
        arnold_node_filter_mode: int
        arnold_node_slidemap: MXSWrapperBase
        arnold_link_slidemap: None
        arnold_node_offset: MXSWrapperBase
        arnold_node_sscale: float
        arnold_node_tscale: float
        arnold_node_swrap: int
        arnold_node_twrap: int
        ...
    class Arnold_N(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_P(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_Procedural_Object(GeometryClass):
        Procedural: str
        UpAxis: int
        BBoxLow: MXSWrapperBase
        BBoxHi: MXSWrapperBase
        auto_instancing: bool
        animated: bool
        AnimFrames: int
        AnimSequenceEnd: int
        AnimSpeed: float
        AnimOffset: int
        AnimSequenceStart: int
        AnimAnimStart: int
        AnimAnimEnd: int
        AnimPingPong: bool
        AnimLoop: bool
        AnimExtend: bool
        name_space: str
        operator: None
        viewport_mode: int
        bbox_threshold: float
        use_bbox_threshold: bool
        animation_cache: int
        use_animation_cache: bool
        ...
    class Arnold_RGBA(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_RGBA_denoise(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_Shape(helper):
        Shape_Object: None
        Group_Members: bool
        Object_And_Children: bool
        Object_Elements: bool
        Scale_Value: float
        variation: float
        Acquire_Mapping: bool
        Acquire_Material: bool
        SubMtl_ID_Offset: int
        Random_Shape: bool
        Animated_Shape: bool
        Acquire_Shape: bool
        Fast_Shape_Evaluation: bool
        Sync_Type: int
        Add_Random_Offset: bool
        Random_Offset: int
        Random_Seed: int
        Set_Scale: bool
        Report_Node_Handles: int
        Handles_To_Report: MXSWrapperBase
        ...
    class Arnold_USD_Object(GeometryClass):
        filename: str
        name_space: str
        objectpath: str
        debug: bool
        frame: float
        UpAxis: int
        BBoxLow: MXSWrapperBase
        BBoxHi: MXSWrapperBase
        operator: None
        viewport_mode: int
        bbox_threshold: float
        use_bbox_threshold: bool
        animation_cache: int
        use_animation_cache: bool
        use_vp_animation: bool
        ...
    class Arnold_Volume_Object(GeometryClass):
        VDBFile: str
        UpAxis: int
        BBoxAuto: bool
        BBoxLow: MXSWrapperBase
        BBoxHi: MXSWrapperBase
        BBoxPadding: float
        Shader: None
        Grids: str
        VelGrids: str
        VelocityScale: float
        StepMode: int
        StepScale: float
        stepsize: float
        VelocityOutlierThreshold: float
        animated: bool
        AnimFrames: int
        AnimSequenceEnd: int
        AnimSpeed: float
        AnimOffset: int
        AnimSequenceStart: int
        AnimAnimStart: int
        AnimAnimEnd: int
        AnimPingPong: bool
        AnimLoop: bool
        AnimExtend: bool
        ...
    class Arnold_advanced_map(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_albedo(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_coat(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_coat_albedo(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_coat_direct(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_coat_indirect(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_denoise_albedo(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_diffuse(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_diffuse_albedo(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_diffuse_direct(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_diffuse_indirect(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_direct(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_emission(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_indirect(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_map_override(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_metalness(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_roughness(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_shadow_matte(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_sheen(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_sheen_albedo(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_sheen_direct(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_sheen_indirect(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_specular(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_sss(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_sss_albedo(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_sss_direct(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_sss_indirect(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Arnold_volume_Z(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        shaders: str
        parameter: str
        map: None
        ...
    class Array(Value):
        ...
    class ArrayParameter(Value):
        ...
    class ArrowHelper(helper):
        iconSize: float
        color: MXSWrapperBase
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
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class AtmosphericClass(Value):
        ...
    class AttachObjects(Primitive):
        ...
    class Attachment(positionController):
        align: bool
        node: None
        manupdate: bool
        ...
    class AttributeDef(Value):
        ...
    class AudioClip(helper):
        ...
    class AudioFile(SoundClass):
        ...
    class AudioFloat(floatController):
        ...
    class AudioPoint3(point3Controller):
        ...
    class AudioPosition(positionController):
        ...
    class AudioRotation(rotationController):
        ...
    class AudioScale(scaleController):
        ...
    class AutoCADImport(ImporterPlugin):
        ...
    class AutoCam(GlobalUtilityPlugin):
        ...
    class AutoTangentMan(Interface):
        ...
    class Auto_Secondary_Element(ReferenceTarget):
        elementName: str
        minSize: float
        intensity: float
        maxSize: float
        axis: float
        quantity: int
        sides: int
        on: bool
        Squeeze: bool
        occlusion: float
        presets: int
        colorSource: float
        radialColor1: MXSWrapperBase
        radialColor2: MXSWrapperBase
        radialColor3: MXSWrapperBase
        radialColor4: MXSWrapperBase
        colorRadius1: float
        colorRadius2: float
        colorRadius3: float
        colorRadius4: float
        radialMtl: None
        useRadialMtl: bool
        radialMap: None
        useRadialMap: bool
        circularColorMix: float
        quadrant1Color: MXSWrapperBase
        quadrant2Color: MXSWrapperBase
        quadrant3Color: MXSWrapperBase
        quadrant4Color: MXSWrapperBase
        circularMtl: None
        useCircularMtl: bool
        circularMap: None
        useCircularMap: bool
        radialSizeMap: None
        useRadialSizeMap: bool
        applyLights: bool
        applyImage: bool
        applyImageCenters: bool
        sourceObjectID: bool
        objectID: int
        sourceEffectsID: bool
        effectsID: int
        sourceUnclampedColor: bool
        unclampedColor: float
        unclampedColorInvert: bool
        sourceSurfaceNormal: bool
        surfaceNormal: float
        surfaceNormalInvert: bool
        sourceWhole: bool
        sourceAlpha: bool
        alpha: int
        sourceZBuffer: bool
        zHi: float
        zLo: float
        filterAll: bool
        filterEdge: bool
        filterPerimeterAlpha: bool
        filterPerimeter: bool
        filterBrightness: bool
        brightness: int
        brightnessInvert: bool
        filterHue: bool
        hue: MXSWrapperBase
        hueRange: int
        applyNoise: bool
        noiseMap: None
        radialDensity: None
        useRadialDensity: bool
        ...
    class Autodesk360(Interface):
        ...
    class AutodeskMap(textureMap):
        ...
    class AutodeskMaterial(material):
        ...
    class AutodeskMaterialManager(Interface):
        ...
    class Autodesk_Map(textureMap):
        ...
    class Autodesk_Material(material):
        ...
    class AutomaticAdaptiveExposureControl(ToneOperator):
        physicalScale: float
        chromaticAdaptation: bool
        colorDifferentiation: bool
        whiteColor: MXSWrapperBase
        active: bool
        processBG: bool
        exposureValue: float
        contrast: float
        brightess: float
        ...
    class AutomaticLinearExposureControl(ToneOperator):
        physicalScale: float
        chromaticAdaptation: bool
        colorDifferentiation: bool
        whiteColor: MXSWrapperBase
        active: bool
        processBG: bool
        exposureValue: float
        contrast: float
        brightess: float
        ...
    class Automatic_Exposure_Control(ToneOperator):
        physicalScale: float
        chromaticAdaptation: bool
        colorDifferentiation: bool
        whiteColor: MXSWrapperBase
        active: bool
        processBG: bool
        exposureValue: float
        contrast: float
        brightess: float
        ...
    class AverageSelVertCenter(Primitive):
        ...
    class AverageSelVertNormal(Primitive):
        ...
    class AvoidBehavior(ReferenceTarget):
        name: str
        obstacles: MXSWrapperBase
        lookAhead: int
        hardRadius: float
        showHardRadius: bool
        detourAngle: float
        brakePressure: float
        repelStrength: float
        repelRadius: float
        repelFalloff: float
        showRepelRadius: bool
        vfieldStrength: float
        vfieldFalloff: float
        showPotentialCols: bool
        showRepelActivity: bool
        showLookAhead: bool
        forceColor: MXSWrapperBase
        displayForce: bool
        ...
    class Avoid_Behavior(ReferenceTarget):
        name: str
        obstacles: MXSWrapperBase
        lookAhead: int
        hardRadius: float
        showHardRadius: bool
        detourAngle: float
        brakePressure: float
        repelStrength: float
        repelRadius: float
        repelFalloff: float
        showRepelRadius: bool
        vfieldStrength: float
        vfieldFalloff: float
        showPotentialCols: bool
        showRepelActivity: bool
        showLookAhead: bool
        forceColor: MXSWrapperBase
        displayForce: bool
        ...
    class Awning(GeometryClass):
        height: float
        width: float
        depth: float
        Horizontal_Frame_Width: float
        Vertical_Frame_Width: float
        Frame_Thickness: float
        Glazing_Thickness: float
        Rail_Width: float
        Number_of_Panels: int
        Percent_Open: int
        Generate_Mapping_Coords: bool
        ...
    class AxisDisplayClass(MAXWrapper):
        ...
    class AxisHelperObj(helper):
        ...
    class AxisTripodLocked(Primitive):
        ...
    class Axis_Helper(helper):
        ...
    class BMP(BitmapIO):
        ...
    class Background(helper):
        ...
    class BackgroundFragment(GraphicsFragmentPlugin):
        ...
    class BackgroundRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
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
    class Bend(modifier):
        BendAngle: float
        BendDir: float
        BendAxis: int
        FromTo: bool
        BendFrom: float
        BendTo: float
        ...
    class BendMod(modifier):
        BendAngle: float
        BendDir: float
        BendAxis: int
        FromTo: bool
        BendFrom: float
        BendTo: float
        ...
    class BendModWSM(SpacewarpObject):
        ...
    class Bevel(modifier):
        segments: int
        Cap_Bottom: int
        Cap_Top: int
        Cap_Type: int
        Side_Type: int
        Smooth_Levels: int
        Produce_Mapping_Coords: int
        Keep_Lines_From_Crossing: int
        Separation_Between_Lines: float
        Starting_Outline: float
        Level_1_Height: float
        Level_1_Outline: float
        Use_Level_2: int
        Level_2_Height: float
        Level_2_Outline: float
        Use_Level_3: int
        Level_3_Height: float
        Level_3_Outline: float
        ...
    class BevelProfileMod(modifier):
        Produce_Mapping_Coords: bool
        Cap_Bottom: bool
        Cap_Top: bool
        Cap_Type: int
        Keep_Lines_From_Crossing: bool
        Separation_Between_Lines: float
        ClassicOrImproved: int
        extrudeamount: float
        extrudesegments: int
        beveldepth: float
        usebevelwidth: bool
        bevelwidth: float
        bevelsteps: int
        bevelpush: float
        beveloptimize: bool
        beveloffset: float
        capStart: int
        capstartconstrain: bool
        capEnd: int
        capendconstrain: bool
        capType: int
        startcapmaterial: int
        startbevelmaterial: int
        sidematerial: int
        endbevelmaterial: int
        endcapmaterial: int
        ...
    class BevelProfileUtilityInterface(UtilityPlugin):
        ...
    class Bevel_Profile(modifier):
        Produce_Mapping_Coords: bool
        Cap_Bottom: bool
        Cap_Top: bool
        Cap_Type: int
        Keep_Lines_From_Crossing: bool
        Separation_Between_Lines: float
        ClassicOrImproved: int
        extrudeamount: float
        extrudesegments: int
        beveldepth: float
        usebevelwidth: bool
        bevelwidth: float
        bevelsteps: int
        bevelpush: float
        beveloptimize: bool
        beveloffset: float
        capStart: int
        capstartconstrain: bool
        capEnd: int
        capendconstrain: bool
        capType: int
        startcapmaterial: int
        startbevelmaterial: int
        sidematerial: int
        endbevelmaterial: int
        endcapmaterial: int
        ...
    class BezierFontLoaderClass(MAXWrapperNonRefTarg):
        ...
    class BezierShapeValue(Value):
        ...
    class Bezier_Point2(Point2Controller):
        ...
    class BiFold(GeometryClass):
        height: float
        open: float
        width: float
        depth: float
        Double_Doors: int
        Flip_Swing: bool
        Flip_Hinge: bool
        Create_Frame: bool
        Frame_Width: float
        Frame_Depth: float
        Door_Offset: float
        Leaf_Thickness: float
        Stiles_Top_Rail: float
        Bottom_Rail: float
        Number_of_Panels_Horizontally: int
        Number_of_Panels_Vertically: int
        Muntin: float
        Panel_Type: int
        Glass_Thickness: float
        Bevel_Angle: float
        Panel_Thickness_1: float
        Panel_Thickness_2: float
        Panel_Middle_Thickness: float
        Panel_Width_1: float
        Panel_Width_2: float
        Generate_Mapping_Coords: bool
        ...
    class BigMatrix(Value):
        ...
    class BigMatrixRowArray(Value):
        ...
    class Billboard(helper):
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
    class Biped_SubAnim(floatController):
        posactive: bool
        rotactive: bool
        scaleactive: bool
        keep: bool
        perframe: bool
        ...
    class Birth(helper):
        Emit_Start: int
        Emit_Stop: int
        type: int
        amount: int
        Subframe_Sampling: bool
        rate: float
        ...
    class BirthGrid(helper):
        Emit_Time: int
        Grid_Base_Type: int
        Grid_Size: float
        Use_Non_Uniform_Grid: bool
        Grid_Width: float
        Grid_Length: float
        Grid_Height: float
        Use_Alternating_Lateral_Offset: bool
        Compact_Vertical_Size: bool
        Use_Random_Vertical_Offset: bool
        Grid_Offset: float
        Random_Seed: int
        Restrict_By_Mesh_Volume: bool
        Delete_Internal_Particles: bool
        Reference_Geometry: None
        Icon_Width: float
        Icon_Length: float
        Icon_Height: float
        Color_Type: bool
        Upper_Limit: int
        Save_Grid_Data_With_File: bool
        External_Layers: int
        Interactive_Update: bool
        ...
    class BirthGroup(helper):
        Emit_Time: int
        Particle_Objects: MXSWrapperBase
        Split_By_Group_Members: bool
        Split_By_Children: bool
        Split_By_Elements: bool
        Acquire_Shapes: bool
        Acquire_Mapping: bool
        Acquire_Material: bool
        SubMtl_ID_Offset: int
        Report_Node_Handles: int
        Handles_To_Report: MXSWrapperBase
        ...
    class BirthStream(helper):
        Emit_Start: int
        Emit_Stop: int
        rate: float
        Separation: float
        Delay_Birth_If_Overlap: bool
        speed: float
        Inherit_Icon_Movement: bool
        multiplier: float
        Random_Seed: int
        Icon_Type: int
        Icon_Width: float
        Icon_Length: float
        Color_Type: bool
        Max_Attempts: int
        ...
    class BirthTexture(helper):
        Emit_Start: int
        Emit_Stop: int
        Lock_On_Emitter: bool
        Data_Start: int
        Data_Stop: int
        Delay_Variation: int
        Use_Latency: bool
        Latency: int
        Precision: int
        Emission_Type: int
        Maximum_Amount: int
        Maximum_Rate: float
        Separate_Distance: float
        Adjust_Separation_By_Scale_Factor: bool
        Fast_Approximate_Separation: bool
        Use_Subdivision: bool
        Subdivision_Length: float
        Amount_Limit: int
        Animated_Shape: bool
        Emission_By: int
        Emission_RGB_Channels: MXSWrapperBase
        Emission_Texture_SubMaterial_ID: int
        Whiteness: float
        Surface_Normal_Offset: bool
        Surface_Offset_Minimum: float
        Surface_Offset_Maximum: float
        Scale_Type: int
        Scale_Factor_SubMtl_ID: int
        Black_Scale: float
        White_Scale: float
        Show_Particles: bool
        Display_Type: int
        Show_Only_When_Selected: bool
        icon_size: float
        Color_Coordinated: bool
        Random_Seed: int
        Emitter_Objects: MXSWrapperBase
        ...
    class Birth_File(helper):
        Particle_File: str
        Particle_File_Valid: bool
        File_Nb_Frames: int
        File_Start: int
        File_End: int
        File_Rate: float
        File_Channel_Mask: int
        FileTime: int
        DataFile_ThisFrame: None
        Nb_Particles_ThisFrame: int
        Range_Type: int
        Range_Start: int
        Range_End: int
        Emit_Start: int
        Speed_Factor: float
        Extrapolation_Type: int
        Use_Position_Channel: bool
        Use_Orientation_Channel: bool
        Orientation_Up_Vector: int
        Use_Scale_Channel: bool
        Use_Speed_Channel: bool
        Use_Color_Channel: bool
        Color_Map_Channel: int
        Use_Opacity_Channel: bool
        Opacity_Map_Channel: int
        ...
    class Birth_Group(helper):
        Emit_Time: int
        Particle_Objects: MXSWrapperBase
        Split_By_Group_Members: bool
        Split_By_Children: bool
        Split_By_Elements: bool
        Acquire_Shapes: bool
        Acquire_Mapping: bool
        Acquire_Material: bool
        SubMtl_ID_Offset: int
        Report_Node_Handles: int
        Handles_To_Report: MXSWrapperBase
        ...
    class Birth_Paint(helper):
        Particle_Paint_Helper: None
        Emit_Start: int
        Emit_Type: int
        Emit_Stop: int
        duration: int
        Subframe_Sampling: bool
        Lock_Position: bool
        Lock_Rotation: bool
        Acquire_Selection: bool
        Selection_Type: int
        ...
    class Birth_Script(helper):
        Random_Seed: int
        Proceed_Script: str
        Emit_Start: int
        ...
    class Birth_Texture(helper):
        Emit_Start: int
        Emit_Stop: int
        Lock_On_Emitter: bool
        Data_Start: int
        Data_Stop: int
        Delay_Variation: int
        Use_Latency: bool
        Latency: int
        Precision: int
        Emission_Type: int
        Maximum_Amount: int
        Maximum_Rate: float
        Separate_Distance: float
        Adjust_Separation_By_Scale_Factor: bool
        Fast_Approximate_Separation: bool
        Use_Subdivision: bool
        Subdivision_Length: float
        Amount_Limit: int
        Animated_Shape: bool
        Emission_By: int
        Emission_RGB_Channels: MXSWrapperBase
        Emission_Texture_SubMaterial_ID: int
        Whiteness: float
        Surface_Normal_Offset: bool
        Surface_Offset_Minimum: float
        Surface_Offset_Maximum: float
        Scale_Type: int
        Scale_Factor_SubMtl_ID: int
        Black_Scale: float
        White_Scale: float
        Show_Particles: bool
        Display_Type: int
        Show_Only_When_Selected: bool
        icon_size: float
        Color_Coordinated: bool
        Random_Seed: int
        Emitter_Objects: MXSWrapperBase
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
    class Bitmaptexture(textureMap):
        clipu: float
        clipv: float
        clipw: float
        cliph: float
        jitter: float
        useJitter: bool
        apply: bool
        cropPlace: int
        filtering: int
        monoOutput: int
        rgbOutput: int
        alphaSource: int
        preMultAlpha: bool
        bitmap: None
        coords: MXSWrapperBase
        output: MXSWrapperBase
        filename: str
        starttime: MXSWrapperBase
        playBackRate: float
        endCondition: int
        tieTimeToMatIDs: bool
        ...
    class Blackman(filter):
        ...
    class Blend(material):
        mixAmount: float
        lower: float
        upper: float
        useCurve: bool
        interactive: int
        map1: MXSWrapperBase
        map2: MXSWrapperBase
        Mask: None
        map1Enabled: bool
        map2Enabled: bool
        maskEnabled: bool
        ...
    class BlendFragment(GraphicsFragmentPlugin):
        ...
    class BlendMap(BakeElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        backgroundColor: MXSWrapperBase
        lightingOn: bool
        shadowsOn: bool
        diffuseOn: bool
        ambientOn: bool
        specularOn: bool
        emissionOn: bool
        reflectionOn: bool
        refractionOn: bool
        targetMapSlotName: str
        ...
    class BlendRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        atmosphereOn: bool
        shadowOn: bool
        diffuseOn: bool
        ambientOn: bool
        specularOn: bool
        emissionOn: bool
        reflectionOn: bool
        refractionOn: bool
        inkOn: bool
        paintOn: bool
        ...
    class BlendedBoxMap(textureMap):
        coords: MXSWrapperBase
        mode: int
        colors: MXSWrapperBase
        tex: MXSWrapperBase
        mapEnabled: MXSWrapperBase
        mapscale: float
        Blend: float
        texturespace: int
        node: None
        posu: float
        posv: float
        posu2: float
        posv2: float
        posLock: bool
        rota: float
        rotb: float
        rotc: float
        rota2: float
        rotb2: float
        rotc2: float
        rotLock: bool
        scaleu: float
        scalev: float
        scaleu2: float
        scalev2: float
        scaleLock: bool
        useRandom: bool
        seed: int
        renderResolution: int
        FORSeed: int
        randx: bool
        randy: bool
        randz: bool
        cube: bool
        cubeMode: int
        lockToFrame: bool
        lockFrame: int
        blendMapStrength: float
        cubeSize: float
        cubeNode: None
        ...
    class Blendfilter(filter):
        Blend: float
        ...
    class Blinn(Shader):
        ...
    class Blinn2(Shader):
        ...
    class BlitFragment(GraphicsFragmentPlugin):
        ...
    class Blizzard(GeometryClass):
        size: float
        seed: int
        speed: float
        mappingType: int
        viewType: int
        viewPercent: float
        emitterHidden: bool
        quantityMethod: int
        particleType: int
        standardParticle: int
        metaballRenderCoarsness: float
        metaballViewCoarsness: float
        metaballAutoCoarsness: bool
        instanceSubTree: bool
        instanceKeyOffsetType: int
        instanceFrameOffset: int
        materialSource: int
        spinAxisType: int
        spawnType: int
        spawnSpeedType: int
        spawnInheritVelocity: bool
        spawnSpeedFixed: bool
        spawnScaleType: int
        spawnScaleFixed: bool
        motionInfluence: float
        motionMultiplier: float
        motionVariation: float
        instancingObject: None
        lifespanValueQueue: MXSWrapperBase
        objectMutationQueue: MXSWrapperBase
        subsampleEmitterTranslation: bool
        subsampleEmitterRotation: bool
        subsampleCreationTime: bool
        life: MXSWrapperBase
        tumble: float
        Tumble_Rate: float
        Emitter_Length: float
        Speed_Variation: float
        Birth_Rate: int
        Total_Number: int
        Emitter_Start: MXSWrapperBase
        Emitter_Stop: MXSWrapperBase
        Display_Until: MXSWrapperBase
        Life_Variation: MXSWrapperBase
        Size_Variation: float
        Growth_Time: MXSWrapperBase
        Fade_Time: MXSWrapperBase
        Emitter_Width: float
        Metaparticle_Tension: float
        Metaparticle_Tension_Variation: float
        Mapping_Time_Base: MXSWrapperBase
        Mapping_Distance_Base: float
        Spin_Time: MXSWrapperBase
        Spin_Time_Variation: float
        Spin_Phase: float
        Spin_Phase_Variation: float
        X_Spin_Vector: float
        Y_Spin_Vector: float
        Z_Spin_Vector: float
        Spin_Axis_Variation: float
        Spawn_Direction_Chaos: float
        Spawn_Speed_Chaos: float
        Spawn_Scale_Chaos: float
        Spawn_Affects: int
        Spawn_Multiplier_Variation: float
        Bubble_Phase_Variation: int
        Die__X_frames_after_collision: MXSWrapperBase
        Die__X_frames_after_collision_variation: float
        Interparticle_Collisions_On: int
        Interparticle_Collision_Steps: int
        Interparticle_Collision_Bounce: float
        Interparticle_Collision_Bounce_Variation: float
        ...
    class BlobMesh(GeometryClass):
        size: float
        tension: float
        renderCoarseness: float
        viewportCoarseness: float
        relativeCoarseness: bool
        nodeList: MXSWrapperBase
        useSoftSelection: bool
        minSize: float
        largeDataSetOptimization: bool
        useAllPFEvents: bool
        pfEventList: MXSWrapperBase
        offInView: bool
        ...
    class Block(floatController):
        ...
    class BlockInstanceFilter(ReferenceMaker):
        ...
    class BlockMgrWrapper(floatController):
        ...
    class Block_Control(MasterBlockController):
        ...
    class Block_Manager_Wrapper(floatController):
        ...
    class BloomAdsk(GraphicsFragmentPlugin):
        ...
    class BlurWind(helper):
        ...
    class Body_Cutter(GeometryClass):
        AutoExtract: bool
        GroupResults: bool
        StockOutside: bool
        StockInside: bool
        CutterOutside: bool
        ...
    class Body_Join(GeometryClass):
        BrepOperation: int
        MakeIntoSolid: bool
        ToBrepObjectHelp: bool
        ...
    class Body_Object(GeometryClass):
        ...
    class Body_Utility(GeometryClass):
        ShowResultOP: bool
        ShowAllOperandsOP: bool
        OP_NOT_USED1: int
        OP_NOT_USED2: bool
        TwoSidedMeshesOP: bool
        OP_NOT_USED3: bool
        OP_NOT_USED4: bool
        SaveBrepsOP: bool
        ShowSelectedOperandsOP: bool
        FastEditOP: bool
        RenderRadioRA: int
        FaceApproxAngleRA: float
        EdgeApproxAngleRA: float
        FaceChordRA: float
        EdgeChordRA: float
        MaxEdgeRA: float
        LowQualityRA: bool
        MediumQualityRA: bool
        HighQualityRA: bool
        WeldAndSmoothRA: bool
        SaveRenderMeshRA: bool
        RenderViewportMeshRA: bool
        FilletAllEdgesFAO: bool
        FirstOrEndEdgesFAO: bool
        SecondOrSideEdgesFAO: bool
        ThirdOrStartEdgesFAO: bool
        FAO_NOT_USED1: bool
        FAO_NOT_USED2: bool
        FAO_NOT_USED3: bool
        FilletRadiusFAO: float
        ApproximateArcFAO: bool
        ConstantDistanceFAO: bool
        LinearCrossSectionFAO: bool
        ShellStartFaceFAO: bool
        ShellEndFaceFAO: bool
        ShellRadioFAO: int
        OffsetRadiusFAO: float
        FAO_NOT_USED4: bool
        CornerExtensionFAO: bool
        SectionTypeFAO: int
        BlendStrengthFAO: float
        DisplayRadioVDS: int
        VDS_NOT_USED1: bool
        ULinesVDS: float
        VLinesVDS: float
        IsoAngleDS: float
        IsoChordHeightVDS: float
        FaceApproxAngleVDS: float
        EdgeApproxAngleVDS: float
        FaceChordHeightVDS: float
        EdgeChordHeightVDS: float
        MaxEdgeLengthPctVDS: float
        CleanMeshVDS: bool
        SubDMeshVDS: bool
        LowQualityVDS: bool
        MediumQualityVDS: bool
        HighQualityVDS: bool
        DisplaySurfaceKnotsVDS: bool
        SmoothingPassesVDS: float
        DisplayControlPointsSA: bool
        DisplayControlMeshSA: bool
        DisplayCurveCurvatureSA: bool
        CurveCurvatureTypeSA: int
        CurvatureScaleSA: float
        CurvatureDensitySA: float
        DisplaySurfaceCurvatureSA: bool
        SurfaceCurvatureTypeSA: int
        StdDevMultiplesSA: float
        UseMinMaxRangeSA: bool
        StdDevMinRangeSA: float
        StdDevMaxRangeSA: float
        SurfAnalysisQuickHelpSA: bool
        NQ_NOT_USED1: bool
        NQ_NOT_USED2: bool
        ExtrToBrepNQ: bool
        ExtrToNURBSNQ: bool
        ExtrToCurveNQ: bool
        NQ_NOT_USED3: bool
        NQ_NOT_USED4: bool
        NQ_NOT_USED5: bool
        ...
    class Bomb(SpacewarpObject):
        seed: int
        spin: float
        gravity: float
        falloff: float
        strength: float
        chaos: float
        detonation: MXSWrapperBase
        fallOffEnable: bool
        minFragmentSize: int
        maxFragmentSize: int
        ...
    class Bombbinding(SpacewarpModifier):
        ...
    class Bone(helper):
        ...
    class BoneData(floatController):
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
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInLength: float
        typeInWidth: float
        typeInHeight: float
        length: float
        width: float
        height: float
        widthsegs: int
        lengthsegs: int
        heightsegs: int
        mapcoords: bool
        ...
    class Box2(Value):
        ...
    class Box3(Value):
        ...
    class BoxGizmo(helper):
        height: float
        length: float
        width: float
        seed: int
        ...
    class BoxPickNode(Primitive):
        ...
    class Box_2_Global_Utility(GlobalUtilityPlugin):
        ...
    class Bricks(textureMap):
        Bricks: None
        Mortar_Map: None
        Bricks_Map: None
        Mortar: None
        Random_Seed: int
        Mortar_Color: MXSWrapperBase
        Brick_Color: MXSWrapperBase
        Horizontal_Count: float
        Vertical_Count: float
        Color_Variance: float
        Vertical_Gap: float
        Horizontal_Gap: float
        Line_Shift: float
        Random_Shift: float
        Holes: int
        Lock_Gap_Symmetry: int
        Fade_Variance: float
        Edge_Roughness: float
        Show_Texture_Swatches: int
        Use_Row_Edit: int
        Use_Column_Edit: int
        Change_Row: float
        Change_Column: float
        Per_Column: int
        Per_Row: int
        Tile_Type: int
        ...
    class Brightness_and_Contrast(renderEffect):
        brightness: float
        contrast: float
        ignoreBack: bool
        ...
    class BrushPresetMgr(Interface):
        ...
    class Bulge_Angle_Deformer(ReferenceTarget):
        ...
    class ButtonControl(RolloutControl):
        ...
    class CATBone(GeometryClass):
        ...
    class CATBoneData(floatController):
        ...
    class CATBoneDataMatrix3Controller(Matrix3Controller):
        ...
    class CATBoneSegTrans(Matrix3Controller):
        ...
    class CATClipFloat(floatController):
        ...
    class CATClipMatrix3(Matrix3Controller):
        ...
    class CATClipRoot(floatController):
        ...
    class CATClipWeights(floatController):
        ...
    class CATCollapseLayers(MAXScriptFunction):
        ...
    class CATCollarBone(Matrix3Controller):
        ...
    class CATDigitSegTrans(Matrix3Controller):
        ...
    class CATDummyMoveMask(Matrix3Controller):
        ...
    class CATFootBend(floatController):
        ...
    class CATFootLift(floatController):
        ...
    class CATFootTrans2(Matrix3Controller):
        ...
    class CATGizmoTransform(Matrix3Controller):
        ...
    class CATHDPivotTrans(Matrix3Controller):
        PivotLocations: MXSWrapperBase
        ...
    class CATHIPivotTrans(Matrix3Controller):
        ...
    class CATHierarchyBranch(floatController):
        ...
    class CATHierarchyBranch2(floatController):
        ...
    class CATHierarchyLeaf(floatController):
        ...
    class CATHierarchyRoot(floatController):
        ...
    class CATImportBVH(MAXScriptFunction):
        ...
    class CATImportBip(MAXScriptFunction):
        ...
    class CATImportHTR(MAXScriptFunction):
        ...
    class CATKneeAngle(floatController):
        ...
    class CATLegWeight(floatController):
        ...
    class CATLiftOffset(floatController):
        ...
    class CATLiftPlantMod(floatController):
        ...
    class CATLimbData2(ReferenceTarget):
        ...
    class CATLimbData2FloatController(floatController):
        ...
    class CATMonoGraph(floatController):
        ...
    class CATMotionDigitRot(rotationController):
        ...
    class CATMotionHub2(Matrix3Controller):
        ...
    class CATMotionLayer(floatController):
        ...
    class CATMotionLimb(floatController):
        ...
    class CATMotionPlatform(Matrix3Controller):
        ...
    class CATMotionRot(rotationController):
        ...
    class CATMotionRotRotationController(rotationController):
        ...
    class CATMotionTail(point3Controller):
        ...
    class CATMotionTailRot(rotationController):
        ...
    class CATMuscle(helper):
        ...
    class CATParent(helper):
        ...
    class CATParentSetupMode(MAXScriptFunction):
        ...
    class CATParentTrans(Matrix3Controller):
        ...
    class CATPivotPos(floatController):
        ...
    class CATPivotRot(floatController):
        ...
    class CATPoint3(point3Controller):
        ...
    class CATRigRootNodeCtrl(Matrix3Controller):
        ...
    class CATSpineData2(ReferenceTarget):
        ...
    class CATSpineData2FloatController(floatController):
        ...
    class CATSpineTrans2(Matrix3Controller):
        ...
    class CATStepShape(floatController):
        ...
    class CATTransformOffset(Matrix3Controller):
        ...
    class CATUnitsPosition(positionController):
        ...
    class CATUnitsScale(scaleController):
        ...
    class CATWeight(floatController):
        ...
    class CATWeightShift(floatController):
        ...
    class CAT_LiftOffset(floatController):
        ...
    class CAT_LiftPlantMod(floatController):
        ...
    class CAT_OnMaxShutdown(MAXScriptFunction):
        ...
    class CAT_OnMaxStartup(MAXScriptFunction):
        ...
    class CATp3(point3Controller):
        ...
    class CCRootClass(Value):
        ...
    class CFDColorVerticesMod(modifier):
        CFDImport_Object: None
        X_Col: int
        Y_Col: int
        Z_Col: int
        Num_Samples: int
        Red_Amount: float
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class CFDImportData(GeometryClass):
        Weld_Dst: float
        Force_Reload_Signal: bool
        NbHeaderLines: int
        NbBottomLines: int
        CSV_File: str
        separator: str
        Default_Value: float
        X_Pos__Chn: int
        Y_Pos__Chn: int
        Z_Pos__Chn: int
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class CFDInterpOnSpline(GeometryClass):
        Splines: None
        amount: float
        Red_Amount: float
        clone: None
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class CFDKeepNVertices(modifier):
        n: int
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class CFDSplineNode(shape):
        bakeSpline_Signal: bool
        CFD_Points: None
        Spline_Origin_Helper: None
        Spline_Vertices: int
        Refresh_Data_Signal: bool
        Field_Interpolation: int
        Smoothing: float
        Field_Sampling: float
        Material_ID_count: int
        material_animation: int
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class CFDSplinePaths(shape):
        Profile: None
        disable: bool
        Num_Steps: int
        CFDImport_Object: None
        X_Col: int
        Y_Col: int
        Z_Col: int
        Num_Samples: int
        Step_Size: float
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class CFDVelocityField(GeometryClass):
        CFDImport_Object: None
        X_Col: int
        Y_Col: int
        Z_Col: int
        Arrow_Scale: float
        Normalized_lengths: bool
        Min_Length: float
        Max_Length: float
        Red_Amount: float
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class CFDVertexPaintChannel(modifier):
        Update_Caches: bool
        CFDPoints: None
        NbClosest: int
        Smooth_Factor: float
        ChannelID: int
        Local_Norm: bool
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class CFDVertexPaintVelocity(modifier):
        Update_Caches: bool
        CFDPoints: None
        NbClosest: int
        Smooth_Factor: float
        Vx_Chn: int
        Vy_Chn: int
        Vz_Chn: int
        Local_Norm: bool
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
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
    class CV_Curve(shape):
        render_thickness: float
        render_sides: int
        render_angle: float
        sphere_cap: float
        cap_segments: int
        render_width: float
        render_length: float
        render_angle2: float
        render_threshold: float
        ...
    class CV_Curveshape(shape):
        ...
    class CV_Surf(GeometryClass):
        ...
    class C_Ext(GeometryClass):
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInBackLength: float
        typeInSideLength: float
        typeInFrontLength: float
        typeInBackWidth: float
        typeInSideWidth: float
        typeInFrontWidth: float
        typeInHeight: float
        Back_Length: float
        Side_Length: float
        Front_Length: float
        Back_Width: float
        Side_Width: float
        Front_Width: float
        height: float
        Back_Segments: int
        Side_Segments: int
        Front_Segments: int
        Width_Segments: int
        Height_Segments: int
        mapcoords: bool
        centerCreate: bool
        ...
    class Cache(helper):
        Use_At: int
        Update_Type: int
        Cache_Test_Results: bool
        Range_Type: int
        Start_Time: MXSWrapperBase
        End_Time: MXSWrapperBase
        Sampling_Type: int
        Every_Nth_Frame: int
        Cache_With_File: bool
        Cache_With_Hold: bool
        Clear_Range_Type: int
        Clear_Start_Time: MXSWrapperBase
        Clear_End_Time: MXSWrapperBase
        Update_Viewports: bool
        Memory_Limit: int
        Memory_Total: int
        Memory_for_Current_Frame: int
        ...
    class CacheDisk(helper):
        Use_At: int
        Range_Type: int
        Start_Time: MXSWrapperBase
        End_Time: MXSWrapperBase
        Sampling_Type: int
        Every_Nth_Frame: int
        Cache_Test_Results: bool
        Write_To_File: None
        Update_Clear_Range_Type: int
        Update_Clear_Start_Time: MXSWrapperBase
        Update_Clear_End_Time: MXSWrapperBase
        Update_Viewports: bool
        Exclude_Shape: bool
        Exclude_Scale: bool
        Exclude_Mapping: bool
        Exclude_Script_Data: bool
        Exclude_Material_ID: bool
        Exclude_Rotation: bool
        Use_Post_Cache_Operators: bool
        Post_Cache_Operators: MXSWrapperBase
        Memory_Limit: int
        ...
    class CacheFile(ReferenceTarget):
        ...
    class CacheSelective(helper):
        Use_At: int
        Range_Type: int
        Start_Time: MXSWrapperBase
        End_Time: MXSWrapperBase
        Sampling_Type: int
        Every_Nth_Frame: int
        Cache_Test_Results: bool
        Save_Cache_With_File: bool
        Save_Cache_With_Hold: bool
        Update_Clear_Range_Type: int
        Update_Clear_Start_Time: MXSWrapperBase
        Update_Clear_End_Time: MXSWrapperBase
        Update_Viewports: bool
        Exclude_Shape: bool
        Exclude_Scale: bool
        Exclude_Mapping: bool
        Exclude_Script_Data: bool
        Exclude_Material_ID: bool
        Exclude_Rotation: bool
        Use_Post_Cache_Operators: bool
        Post_Cache_Operators: MXSWrapperBase
        Memory_Limit: int
        ...
    class CacheSubGraphOutputFragment(GraphicsFragmentPlugin):
        ...
    class Cache_Disk(helper):
        Use_At: int
        Range_Type: int
        Start_Time: MXSWrapperBase
        End_Time: MXSWrapperBase
        Sampling_Type: int
        Every_Nth_Frame: int
        Cache_Test_Results: bool
        Write_To_File: None
        Update_Clear_Range_Type: int
        Update_Clear_Start_Time: MXSWrapperBase
        Update_Clear_End_Time: MXSWrapperBase
        Update_Viewports: bool
        Exclude_Shape: bool
        Exclude_Scale: bool
        Exclude_Mapping: bool
        Exclude_Script_Data: bool
        Exclude_Material_ID: bool
        Exclude_Rotation: bool
        Use_Post_Cache_Operators: bool
        Post_Cache_Operators: MXSWrapperBase
        Memory_Limit: int
        ...
    class Cache_Selective(helper):
        Use_At: int
        Range_Type: int
        Start_Time: MXSWrapperBase
        End_Time: MXSWrapperBase
        Sampling_Type: int
        Every_Nth_Frame: int
        Cache_Test_Results: bool
        Save_Cache_With_File: bool
        Save_Cache_With_Hold: bool
        Update_Clear_Range_Type: int
        Update_Clear_Start_Time: MXSWrapperBase
        Update_Clear_End_Time: MXSWrapperBase
        Update_Viewports: bool
        Exclude_Shape: bool
        Exclude_Scale: bool
        Exclude_Mapping: bool
        Exclude_Script_Data: bool
        Exclude_Material_ID: bool
        Exclude_Rotation: bool
        Use_Post_Cache_Operators: bool
        Post_Cache_Operators: MXSWrapperBase
        Memory_Limit: int
        ...
    class Caddy(GlobalUtilityPlugin):
        ...
    class CallbackFn1(MAXScriptFunction):
        ...
    class CamMatchDataCustAttrib(CustAttrib):
        xLine1_b: MXSWrapperBase
        xLine1_e: MXSWrapperBase
        xLine2_b: MXSWrapperBase
        xLine2_e: MXSWrapperBase
        yLine1_b: MXSWrapperBase
        yLine1_e: MXSWrapperBase
        yLine2_b: MXSWrapperBase
        yLine2_e: MXSWrapperBase
        zLine1_b: MXSWrapperBase
        zLine1_e: MXSWrapperBase
        zLine2_b: MXSWrapperBase
        zLine2_e: MXSWrapperBase
        viewport_size_x: int
        viewport_size_y: int
        axis_mode: int
        ...
    class CamPerspCorrect(modifier):
        paramPerspectCorrectAmount: float
        paramPerspectCorrectDir: float
        ...
    class CamPoint(helper):
        showAxis: bool
        axisLength: float
        ...
    class CameraCulling(helper):
        Use_Active_Camera: bool
        camera: None
        Use_Camera_Clipping_Planes: bool
        Use_Near_Clip: bool
        Near_Clip_Distance: float
        Use_Far_Clip: bool
        Far_Clip_Distance: float
        Culling_Type: int
        Render_Culling: bool
        Viewport_Culling: bool
        Use_For_Group_Selection: bool
        Selection_Type: int
        Subframe_Precision: bool
        ...
    class CameraMBlur(helper):
        Use_Active_Camera: bool
        camera: None
        Use_Event_Multiplier: bool
        multiplier: float
        ...
    class CameraMap(modifier):
        ...
    class CameraMapSpaceWarp(SpacewarpObject):
        ...
    class CameraMapTexture(textureMap):
        camera: None
        mapChannel: int
        texture: None
        backFace: bool
        useZBuffer: bool
        zBuffer: None
        ZFudge: float
        angleThreshold: float
        Mask: None
        useMask: bool
        maskUsesProjection: bool
        affectBehindCam: bool
        aspectMode: int
        haspect: float
        vaspect: float
        ...
    class Camera_Culling(helper):
        Use_Active_Camera: bool
        camera: None
        Use_Camera_Clipping_Planes: bool
        Use_Near_Clip: bool
        Near_Clip_Distance: float
        Use_Far_Clip: bool
        Far_Clip_Distance: float
        Culling_Type: int
        Render_Culling: bool
        Viewport_Culling: bool
        Use_For_Group_Selection: bool
        Selection_Type: int
        Subframe_Precision: bool
        ...
    class Camera_IMBlur(helper):
        Use_Active_Camera: bool
        camera: None
        Use_Event_Multiplier: bool
        multiplier: float
        ...
    class Camera_Map_Per_Pixel(textureMap):
        camera: None
        mapChannel: int
        texture: None
        backFace: bool
        useZBuffer: bool
        zBuffer: None
        ZFudge: float
        angleThreshold: float
        Mask: None
        useMask: bool
        maskUsesProjection: bool
        affectBehindCam: bool
        aspectMode: int
        haspect: float
        vaspect: float
        ...
    class Camera_Match(UtilityPlugin):
        ...
    class Camera_Tracker(UtilityPlugin):
        ...
    class Cap_Holes(modifier):
        smooth: bool
        sm_ends: bool
        vis_edges: bool
        ...
    class Capsule(GeometryClass):
        height: float
        smooth: bool
        radius: float
        sides: int
        mapcoords: bool
        sliceon: bool
        heighttype: int
        heightsegs: int
        slicefrom: float
        sliceto: float
        ...
    class CaptureAnimation(MAXScriptFunction):
        ...
    class CaptureCallStack(Primitive):
        ...
    class Captured_Object_State(ReferenceTarget):
        ...
    class Casement(GeometryClass):
        height: float
        width: float
        depth: float
        Panel_Width: float
        Number_of_Casements: int
        Opens_to_Inside: bool
        Horizontal_Frame_Width: float
        Vertical_Frame_Width: float
        Frame_Thickness: float
        Glazing_Thickness: float
        Percent_Open: int
        Generate_Mapping_Coords: bool
        ...
    class Catmull_Rom(filter):
        ...
    class Cellular(textureMap):
        cellColor: MXSWrapperBase
        divColor1: MXSWrapperBase
        divColor2: MXSWrapperBase
        cellMap: None
        divMap1: None
        divMap2: None
        map1Enabled: bool
        map2Enabled: bool
        map3Enabled: bool
        variation: float
        size: float
        spread: float
        lowThresh: float
        midThresh: float
        highThresh: float
        type: int
        fractal: bool
        iteration: float
        roughness: float
        smooth: float
        adaptive: bool
        coords: MXSWrapperBase
        output: MXSWrapperBase
        ...
    class CenterObject(MappedPrimitive):
        ...
    class CenterPivot(MappedPrimitive):
        ...
    class Chair(GeometryClass):
        gender: int
        motionSeed: int
        id: int
        single: bool
        height: float
        ...
    class Chamfer(modifier):
        amount: float
        segments: int
        tension: float
        openchamfer: bool
        invert: bool
        selectionoption: int
        smoothingoption: int
        materialOption: int
        setmaterial: bool
        materialID: int
        smooth: bool
        SmoothType: int
        smooththreshold: float
        chamfertype: int
        limiteffect: bool
        useminangle: bool
        minangle: float
        usemaxangle: bool
        maxangle: float
        smoothtoadjacent: bool
        quadIntersectionMode: bool
        miteringType: int
        amountType: int
        minAmount: float
        maxAmount: float
        addinset: bool
        insetamount: float
        insetsegments: int
        insetoffset: float
        forcePositiveOffset: bool
        miterEndBias: float
        useConstantOffset: bool
        depth: float
        presetOptionsComboBox: int
        radiusBias: float
        biasEndPoints: bool
        scale: float
        depthType: int
        insetType: int
        angleFactorVertex: float
        ...
    class ChamferBox(GeometryClass):
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInLength: float
        typeInWidth: float
        typeInHeight: float
        typeInFillet: float
        length: float
        width: float
        height: float
        fillet: float
        Length_Segments: int
        Width_Segments: int
        Height_Segments: int
        Fillet_Segments: int
        mapcoords: bool
        smooth: bool
        ...
    class ChamferCyl(GeometryClass):
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInRadius: float
        typeInHeight: float
        typeInFillet: float
        radius: float
        height: float
        fillet: float
        Height_Segments: int
        Fillet_Segments: int
        sides: int
        cap_segments: int
        Smooth_On: bool
        Slice_On: bool
        Slice_From: float
        Slice_To: float
        mapcoords: bool
        ...
    class ChamferMod(modifier):
        amount: float
        segments: int
        tension: float
        openchamfer: bool
        invert: bool
        selectionoption: int
        smoothingoption: int
        materialOption: int
        setmaterial: bool
        materialID: int
        smooth: bool
        SmoothType: int
        smooththreshold: float
        chamfertype: int
        limiteffect: bool
        useminangle: bool
        minangle: float
        usemaxangle: bool
        maxangle: float
        smoothtoadjacent: bool
        quadIntersectionMode: bool
        miteringType: int
        amountType: int
        minAmount: float
        maxAmount: float
        addinset: bool
        insetamount: float
        insetsegments: int
        insetoffset: float
        forcePositiveOffset: bool
        miterEndBias: float
        useConstantOffset: bool
        depth: float
        presetOptionsComboBox: int
        radiusBias: float
        biasEndPoints: bool
        scale: float
        depthType: int
        insetType: int
        angleFactorVertex: float
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
    class Character(helper):
        ...
    class CharacterAssembly(helper):
        characterID: int
        iconSize: int
        displayRes: int
        ...
    class CharacterHelper(helper):
        ...
    class CheckBoxControl(RolloutControl):
        ...
    class CheckButtonControl(RolloutControl):
        ...
    class CheckForSave(Primitive):
        ...
    class Checker(textureMap):
        Soften: float
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1: None
        map2: None
        map1Enabled: bool
        map2Enabled: bool
        coords: MXSWrapperBase
        ...
    class Circle(shape):
        steps: int
        radius: float
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        ...
    class CirclePickNode(Primitive):
        ...
    class CivilView_Alignment(shape):
        StartStation: float
        EndStation: float
        CurrentDataset: int
        DatasetNameArray: MXSWrapperBase
        DatasetSizeArray: MXSWrapperBase
        XYZStationArray: MXSWrapperBase
        RadBearGradeArray: MXSWrapperBase
        AlignEntTypeArray: MXSWrapperBase
        ProfileEntTypeArray: MXSWrapperBase
        isAlignEntStartEnd: MXSWrapperBase
        isProfileEntStartEnd: MXSWrapperBase
        designSpeedComments: MXSWrapperBase
        designSpeedStations: MXSWrapperBase
        designSpeedValues: MXSWrapperBase
        ...
    class CivilView_Pipe(shape):
        DisplayName: str
        description: str
        PartDescription: str
        PartSizeName: str
        PartSubType: str
        StartStructureHandle: str
        EndStructureHandle: str
        HORType: int
        PSEType: int
        FlowDirection: int
        FlowDirectionMethod: int
        CrossSectionalShape: int
        Bearing: float
        radius: float
        Slope: float
        InnerDiameterOrWidth: float
        InnerHeight: float
        OuterDiameterOrWidth: float
        OuterHeight: float
        MinimumCover: float
        MaximumCover: float
        Length2DCenterToCenter: float
        Length3DCenterToCenter: float
        Length2DToInsideEdge: float
        Length3DToInsideEdge: float
        ...
    class Civil_Structure(GeometryClass):
        type: int
        frame_type: int
        structure_widthOrDia: float
        structure_length: float
        structure_height: float
        frame_widthOrDia: float
        frame_length: float
        frame_height: float
        cone_widthOrDia: float
        cone_length: float
        cone_height: float
        floor_thickness: float
        wall_thickness: float
        rim_thickness: float
        concentric_offset_x: float
        concentric_offset_y: float
        use_matid: bool
        mapcoords: bool
        DisplayName: None
        networkName: None
        networkID: None
        cover: None
        frame: None
        grate: None
        materialName: None
        partDefId: None
        partDesc: None
        PartSizeName: None
        PartSubType: None
        connectedPartCount: int
        connectedPipesCount: int
        partType: int
        barrelPipeClearance: float
        ...
    class Civil_View_Divide_Spline(modifier):
        ...
    class Civil_View_Guard_Rail(modifier):
        ...
    class Civil_View_Path___Surface_Constraint(Matrix3Controller):
        ...
    class Civil_View_Path___Surface_ConstraintMatrix3Controller(Matrix3Controller):
        ...
    class Civil_View_Path___Surface_ConstraintMatrix3ControllerMatrix3Controller(Matrix3Controller):
        ...
    class Civil_View_Road_Marking(modifier):
        ...
    class Civil_View_Sight_Checker__Calc(renderEffect):
        ...
    class Civil_View_Spline_to_Mesh(modifier):
        ...
    class Civil_View_Swept_Object(SpacewarpModifier):
        ...
    class Civil_View_Traffic_Data_Constraint(scaleController):
        ...
    class ClayFragment(GraphicsFragmentPlugin):
        ...
    class CleanUp(helper):
        Dummy: int
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
    class Clone_and_Align_Tool(UtilityPlugin):
        ...
    class CloseActiveShade(Primitive):
        ...
    class Cloth(modifier):
        gravity: float
        selfCollision: bool
        solidCollision: bool
        scale: float
        useSewingSprings: bool
        startframe: int
        timestep: float
        showSewingSprings: bool
        subsample: int
        endframe: int
        enableEndFrame: bool
        checkIntersections: bool
        clothclothMethod: int
        useGravity: bool
        simOnRender: bool
        simPriority: int
        advancedPinching: bool
        relativeVelocity: float
        timeScale: float
        ignoreBackfacing: bool
        simOnMouseDown: bool
        showCurrentState: bool
        showTargetState: bool
        showEnabledSolidCollision: bool
        showEnabledClothCollision: bool
        showTension: bool
        tensionScale: float
        weldMethod: int
        ...
    class CmdPanelOptimization(Interface):
        ...
    class CogControl(ReferenceTarget):
        name: str
        startState: None
        states: MXSWrapperBase
        ...
    class CollarBoneTrans(Matrix3Controller):
        ...
    class Collision(helper):
        Collision_Nodes: MXSWrapperBase
        Test_Type: int
        Speed_Option: int
        Min_Speed: float
        Max_Speed: float
        Random_Seed: int
        Will_Collide_Frame: int
        Collision_Count: int
        Collision_Count_Options: int
        ...
    class Collision_Spawn(helper):
        True_for_Particles_Collided: bool
        True_for_Spawn_Particles: bool
        Collision_Nodes: MXSWrapperBase
        Spawn_Type: int
        Delete_Parent: bool
        Number_of_Collisions: int
        Spawn_Able: float
        Number_of_Offsprings: int
        Offsprings_Variation: float
        Sync_Type: int
        Restart_Particle_Age: bool
        Parent_Speed: int
        Offspring_Speed: int
        Speed_Type: int
        speed: float
        Speed_Inherited: float
        Speed_Variation: float
        Divergence: float
        Scale_Factor: float
        Scale_Variation: float
        Random_Seed: int
        ...
    class ColorCorrection(textureMap):
        color: MXSWrapperBase
        map: None
        rewireMode: int
        rewireR: int
        rewireG: int
        rewireB: int
        rewireA: int
        hueShift: float
        saturation: float
        tint: MXSWrapperBase
        tintStrength: float
        lightnessMode: int
        contrast: float
        brightness: float
        exposureMode: int
        enableR: bool
        enableG: bool
        enableB: bool
        gainRGB: float
        gainR: float
        gainG: float
        gainB: float
        gammaRGB: float
        gammaR: float
        gammaG: float
        gammaB: float
        pivotRGB: float
        pivotR: float
        pivotG: float
        pivotB: float
        liftRGB: float
        liftR: float
        liftG: float
        liftB: float
        printerLights: float
        ...
    class ColorMap(textureMap):
        solidcolor: MXSWrapperBase
        map: None
        mapEnabled: bool
        gamma: float
        gain: float
        ReverseGamma: bool
        ...
    class ColorPickerControl(RolloutControl):
        ...
    class ColorTargetToPresentableTargetFragment(GraphicsFragmentPlugin):
        ...
    class Color_Balance(renderEffect):
        red: int
        green: int
        blue: int
        preserveLum: bool
        ignoreBack: bool
        ...
    class Color_Clipboard(UtilityPlugin):
        ...
    class Color_Correction(textureMap):
        color: MXSWrapperBase
        map: None
        rewireMode: int
        rewireR: int
        rewireG: int
        rewireB: int
        rewireA: int
        hueShift: float
        saturation: float
        tint: MXSWrapperBase
        tintStrength: float
        lightnessMode: int
        contrast: float
        brightness: float
        exposureMode: int
        enableR: bool
        enableG: bool
        enableB: bool
        gainRGB: float
        gainR: float
        gainG: float
        gainB: float
        gammaRGB: float
        gammaR: float
        gammaG: float
        gammaB: float
        pivotRGB: float
        pivotR: float
        pivotG: float
        pivotB: float
        liftRGB: float
        liftR: float
        liftG: float
        liftB: float
        printerLights: float
        ...
    class Color_RGB(point3Controller):
        ...
    class Color_RGBA(point4Controller):
        ...
    class ComboBoxControl(RolloutControl):
        ...
    class Combustion(textureMap):
        height: int
        width: int
        ...
    class CommitControllerValue(Primitive):
        ...
    class Compass(helper):
        ...
    class CompleteMap(BakeElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        backgroundColor: MXSWrapperBase
        shadowsOn: bool
        targetMapSlotName: str
        ...
    class CompleteRedraw(Primitive):
        ...
    class CompositeMap(textureMap):
        mapEnabled: MXSWrapperBase
        maskEnabled: MXSWrapperBase
        blendMode: MXSWrapperBase
        layername: MXSWrapperBase
        dlgOpened: MXSWrapperBase
        opacity: MXSWrapperBase
        mapList: MXSWrapperBase
        Mask: MXSWrapperBase
        ...
    class CompositeTexturemap(textureMap):
        mapEnabled: MXSWrapperBase
        maskEnabled: MXSWrapperBase
        blendMode: MXSWrapperBase
        layername: MXSWrapperBase
        dlgOpened: MXSWrapperBase
        opacity: MXSWrapperBase
        mapList: MXSWrapperBase
        Mask: MXSWrapperBase
        ...
    class Condition(ReferenceTarget):
        type: int
        Condition_Type_Real: int
        Use_Input_As_A: bool
        Integer_A: int
        Float_A: float
        Time_A: int
        World_A: float
        Percent_A: float
        Angle_A: float
        Use_Second_Condition: bool
        Use_Input_As_B: bool
        Integer_B: int
        Float_B: float
        Time_B: int
        World_B: float
        Percent_B: float
        Angle_B: float
        Use_As_Speed_Or_Spin_Rate: bool
        Units_Per_Type: int
        Angle_As_Orientation: bool
        Sync_Type: int
        Use_E4: bool
        Condition_Type_Int: int
        Use_As_Acceleration: bool
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        ...
    class Cone(GeometryClass):
        sliceon: bool
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInRadius1: float
        typeInRadius2: float
        typeInHeight: float
        radius1: float
        radius2: float
        height: float
        heightsegs: int
        capsegs: int
        sides: int
        smooth: bool
        slice: bool
        slicefrom: float
        sliceto: float
        mapcoords: bool
        ...
    class ConeAngleManip(helper):
        Origin: MXSWrapperBase
        direction: MXSWrapperBase
        angle: float
        distance: float
        UseSquare: bool
        aspect: float
        ...
    class Cone_Angle(helper):
        Origin: MXSWrapperBase
        direction: MXSWrapperBase
        angle: float
        distance: float
        UseSquare: bool
        aspect: float
        ...
    class ConfigureBitmapPaths(Primitive):
        ...
    class Conform(GeometryClass):
        ...
    class ConformSpaceWarp(SpacewarpObject):
        icon_size: float
        Projection_Distance: float
        Selected_Verts: int
        Standoff_Distance: float
        ...
    class Conjugate(Generic):
        ...
    class Connect(GeometryClass):
        ...
    class ConstrFilterFn(MAXScriptFunction):
        ...
    class Container(helper):
        localDefinitionFilename: str
        unloaded: bool
        accessContent: bool
        allowInPlaceEditing: bool
        accessPublishedContent: bool
        sourceDefinitionFilename: str
        contentBoundingBox: bool
        displayLabel: bool
        overrideNodeProperties: bool
        size: float
        autoUpdateClosed: bool
        displayStatus: bool
        editingUser: str
        updateNeeded: bool
        alternateDefinitionFilename: MXSWrapperBase
        currentAlternateDefinition: int
        duplicateMatchingLayers: bool
        ...
    class ContainerHelper(helper):
        localDefinitionFilename: str
        unloaded: bool
        accessContent: bool
        allowInPlaceEditing: bool
        accessPublishedContent: bool
        sourceDefinitionFilename: str
        contentBoundingBox: bool
        displayLabel: bool
        overrideNodeProperties: bool
        size: float
        autoUpdateClosed: bool
        displayStatus: bool
        editingUser: str
        updateNeeded: bool
        alternateDefinitionFilename: MXSWrapperBase
        currentAlternateDefinition: int
        duplicateMatchingLayers: bool
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
        type: int
        Boolean_Conversion: int
        Integer_Time_Conversion: int
        Matrix_Vector_Conversion: int
        Quaternion_Real_Conversion: int
        Quaternion_Vector_Conversion: int
        Real_Integer_Conversion: int
        Real_Time_Conversion: int
        Real_Vector_Conversion: int
        Vector_Quaternion_Conversion: int
        Vector_Real_Conversion: int
        Pair_Integer_Conversion: int
        Vector_Pair_Conversion: int
        Negative_Up_Toward_Zero: bool
        Use_I3_As_Object_Index: bool
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
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
    class ConvertToPatch(modifier):
        quadsToQuads: bool
        selectionConversion: int
        useSoftSelection: int
        selectionLevel: int
        ...
    class Cook_Variable(filter):
        ...
    class Cookie(VideoPostFilter):
        ...
    class CopyCollection(Value):
        ...
    class Copy_Out(helper):
        Number_Of_Copies: int
        ...
    class Crease(modifier):
        Crease: float
        selectionoption: int
        creasecolor: MXSWrapperBase
        displayColor: bool
        ...
    class CreaseExplorerManager(Interface):
        ...
    class CreaseMod(modifier):
        Crease: float
        selectionoption: int
        creasecolor: MXSWrapperBase
        displayColor: bool
        ...
    class CreaseSet(modifier):
        creasesettype: MXSWrapperBase
        creasesetselect: MXSWrapperBase
        creasesetcolor: MXSWrapperBase
        creasesetname: MXSWrapperBase
        creasesetcrease: MXSWrapperBase
        ignoreBackfacing: bool
        angleselecttype: int
        anglea: float
        angleb: float
        autoSelectNodes: bool
        tolerance: float
        keepExistingSets: bool
        displaySetColors: bool
        ...
    class CreaseSetManager(Interface):
        ...
    class CreaseSetMod(modifier):
        creasesettype: MXSWrapperBase
        creasesetselect: MXSWrapperBase
        creasesetcolor: MXSWrapperBase
        creasesetname: MXSWrapperBase
        creasesetcrease: MXSWrapperBase
        ignoreBackfacing: bool
        angleselecttype: int
        anglea: float
        angleb: float
        autoSelectNodes: bool
        tolerance: float
        keepExistingSets: bool
        displaySetColors: bool
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
    class Create_Out_of_Range_Keys(trackViewUtility):
        ...
    class CrosFade(VideoPostFilter):
        ...
    class CrossSection(modifier):
        ...
    class Crowd(helper):
        simStart: int
        solveStart: int
        solveEnd: int
        deleteKeys: bool
        saveNthPos: int
        saveNthRot: int
        update: bool
        updateFrequency: int
        vectorScale: float
        useScript: bool
        functionName: str
        script: None
        solveForBipeds: bool
        backtracking: bool
        usePriorities: bool
        flashing: bool
        behaviors: MXSWrapperBase
        teams: MXSWrapperBase
        assignments: MXSWrapperBase
        cogcontrols: MXSWrapperBase
        Scatter: MXSWrapperBase
        ObjAssoc: MXSWrapperBase
        smooth: MXSWrapperBase
        Priority: MXSWrapperBase
        iconSize: float
        showCollisions: bool
        whenToShowCollisions: int
        collisionColor: MXSWrapperBase
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
        team: None
        Delegate: None
        behavior: None
        CogControl: None
        weight: float
        active: bool
        ...
    class CrowdDelegate(helper):
        width: float
        depth: float
        height: float
        velocityColor: MXSWrapperBase
        active: bool
        showForces: bool
        showVelocity: bool
        showCogStates: bool
        xyConstrain: bool
        useHierBbox: bool
        averageSpeed: float
        maxaccel: float
        turnDecel: float
        turnDecelAngle: float
        inclineDecel: float
        inclineDecelAngle: float
        declineAccel: float
        declineAccelAngle: float
        maxTurnVel: float
        maxTurnAccel: float
        maxIncline: float
        maxDecline: float
        maxBank: float
        maxBankVel: float
        bankPerTurn: float
        useBiped: bool
        biped: None
        startframe: int
        Priority: int
        startClip: int
        behaviors: MXSWrapperBase
        weights: MXSWrapperBase
        duration: int
        index: int
        randID: int
        simpos: MXSWrapperBase
        ...
    class CrowdDoRestartPathTool(Primitive):
        ...
    class CrowdGroup(ReferenceTarget):
        name: str
        members: MXSWrapperBase
        ...
    class CrowdPathDrawing(Primitive):
        ...
    class CrowdPathExtend(Primitive):
        ...
    class CrowdPathSetDefaultWidth(Primitive):
        ...
    class CrowdState(ReferenceTarget):
        name: str
        behaviors: MXSWrapperBase
        weights: MXSWrapperBase
        transitions: MXSWrapperBase
        ...
    class CrowdTeam(ReferenceTarget):
        name: str
        members: MXSWrapperBase
        ...
    class CrowdTransition(ReferenceTarget):
        Priority: int
        duration: int
        easeIn: float
        easeOut: float
        functionName: str
        script: None
        to: None
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
    class CylGizmo(helper):
        height: float
        radius: float
        seed: int
        ...
    class Cylinder(GeometryClass):
        sliceon: bool
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInRadius: float
        typeInHeight: float
        radius: float
        height: float
        heightsegs: int
        capsegs: int
        sides: int
        smooth: bool
        slice: bool
        slicefrom: float
        sliceto: float
        mapcoords: bool
        ...
    class D6Joint(helper):
        ...
    class DAEEXP(ExporterPlugin):
        ...
    class DAEIMP(ImporterPlugin):
        ...
    class DDS(BitmapIO):
        ...
    class DOFEffect(renderEffect):
        affectAlpha: bool
        focalPoint: int
        focalType: int
        horizFocalLoss: float
        vertFocalLoss: float
        focalRange: float
        focalLimit: float
        camNodeIndex: int
        focalNodeIndex: int
        ...
    class DOSCommand(Primitive):
        ...
    class DSIMDSCC(scaleController):
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
    class DYNrootNodeStore(AttributeDef):
        ...
    class DYNwheelRotationControllerAttributes(AttributeDef):
        ...
    class DaeExporter(ExporterPlugin):
        ...
    class DaeImporter(ImporterPlugin):
        ...
    class Damper(GeometryClass):
        Force: float
        Drag: float
        End_Placement_Method: int
        Free_Damper_Height: float
        Renderable_Spring: int
        Base_Stud_Diameter: float
        Base_Stud_Height: float
        Cylinder_Diameter: float
        Cylinder_Height: float
        Cylinder_Sides: int
        Cylinder_Fillet_1: float
        Cylinder_Fillet_1_Segments: int
        Cylinder_Fillet_2: float
        Cylinder_Fillet_2_Segments: int
        Inside_Diameter: float
        Smooth_Cylinder: int
        Piston_Diameter: float
        Piston_Height: float
        Piston_Sides: int
        Smooth_Piston: int
        Enable_Boot: int
        Boot_Small_Diameter: float
        Boot_Large_Diameter: float
        Boot_Sides: int
        Boot_Folds: int
        Boot_Fold_Resolution: int
        Boot_Stop_Diameter: float
        Boot_Stop_Height: float
        Boot_Stop_Setback: float
        Boot_Stop_Fillet: float
        Boot_Stop_Fillet_Segements: int
        Smooth_Boot: int
        Dynamics_Object_Type: int
        Drag_Units: int
        Damper_Direction: int
        Force_Units: int
        Generate_Mapping_Coordinates: int
        ...
    class DataChannelModifier(modifier):
        Operators: MXSWrapperBase
        operator_enabled: MXSWrapperBase
        operator_ops: MXSWrapperBase
        operator_order: MXSWrapperBase
        display: bool
        operator_frozen: MXSWrapperBase
        debugInfo: bool
        floatDisplay: int
        point3Display: int
        tickSize: int
        normalizeDisplay: bool
        showNumericData: bool
        minColor: MXSWrapperBase
        midColor: MXSWrapperBase
        maxColor: MXSWrapperBase
        numeric_max: int
        numeric_drawdist: int
        ...
    class DataOpDeleteCatcher(ReferenceTarget):
        ...
    class DataOperIcon(helper):
        Visible_Icon: bool
        Icon_Type: int
        Icon_Parameter_1: float
        Icon_Parameter_2: float
        Icon_Parameter_3: float
        Color_Coordinated: bool
        Auto_Update: bool
        SubOperators: MXSWrapperBase
        Selected_SubOperators: MXSWrapperBase
        groups: MXSWrapperBase
        Enable_By_Switch: bool
        Default_Width: int
        Default_Offset: int
        Default_Height: int
        Default_Range_Type: int
        Default_Range_Min: float
        Default_Range_Max: float
        Activity_Type: int
        Time_On: int
        Time_Off: int
        Animatable_Active: bool
        PDView_Origin_X: int
        PDView_Origin_Y: int
        PDView_Width: int
        PDView_Height: int
        PDView_Divider: int
        PDView_Show_Depot: bool
        PDView_Description_Type: int
        PDView_Show_Parameters: bool
        Use_Dynamic_Names_For_New: bool
        Auto_Update_On_Data_View_Close: bool
        Repeats: int
        ...
    class DataOperator(helper):
        Visible_Icon: bool
        Icon_Type: int
        Icon_Parameter_1: float
        Icon_Parameter_2: float
        Icon_Parameter_3: float
        Color_Coordinated: bool
        Auto_Update: bool
        SubOperators: MXSWrapperBase
        Selected_SubOperators: MXSWrapperBase
        groups: MXSWrapperBase
        Enable_By_Switch: bool
        Default_Width: int
        Default_Offset: int
        Default_Height: int
        Default_Range_Type: int
        Default_Range_Min: float
        Default_Range_Max: float
        Activity_Type: int
        Time_On: int
        Time_Off: int
        Animatable_Active: bool
        PDView_Origin_X: int
        PDView_Origin_Y: int
        PDView_Width: int
        PDView_Height: int
        PDView_Divider: int
        PDView_Show_Depot: bool
        PDView_Description_Type: int
        PDView_Show_Parameters: bool
        Use_Dynamic_Names_For_New: bool
        Auto_Update_On_Data_View_Close: bool
        Repeats: int
        ...
    class DataPair(Value):
        ...
    class DataTest(helper):
        Visible_Icon: bool
        Icon_Type: int
        Icon_Parameter_1: float
        Icon_Parameter_2: float
        Icon_Parameter_3: float
        Color_Coordinated: bool
        Auto_Update: bool
        SubOperators: MXSWrapperBase
        Selected_SubOperators: MXSWrapperBase
        groups: MXSWrapperBase
        Enable_By_Switch: bool
        Default_Width: int
        Default_Offset: int
        Default_Height: int
        Default_Range_Type: int
        Default_Range_Min: float
        Default_Range_Max: float
        Activity_Type: int
        Time_On: int
        Time_Off: int
        Animatable_Active: bool
        PDView_Origin_X: int
        PDView_Origin_Y: int
        PDView_Width: int
        PDView_Height: int
        PDView_Divider: int
        PDView_Show_Depot: bool
        PDView_Description_Type: int
        PDView_Show_Parameters: bool
        Use_Dynamic_Names_For_New: bool
        Auto_Update_On_Data_View_Close: bool
        Repeats: int
        ...
    class DataTestIcon(helper):
        Visible_Icon: bool
        Icon_Type: int
        Icon_Parameter_1: float
        Icon_Parameter_2: float
        Icon_Parameter_3: float
        Color_Coordinated: bool
        Auto_Update: bool
        SubOperators: MXSWrapperBase
        Selected_SubOperators: MXSWrapperBase
        groups: MXSWrapperBase
        Enable_By_Switch: bool
        Default_Width: int
        Default_Offset: int
        Default_Height: int
        Default_Range_Type: int
        Default_Range_Min: float
        Default_Range_Max: float
        Activity_Type: int
        Time_On: int
        Time_Off: int
        Animatable_Active: bool
        PDView_Origin_X: int
        PDView_Origin_Y: int
        PDView_Width: int
        PDView_Height: int
        PDView_Divider: int
        PDView_Show_Depot: bool
        PDView_Description_Type: int
        PDView_Show_Parameters: bool
        Use_Dynamic_Names_For_New: bool
        Auto_Update_On_Data_View_Close: bool
        Repeats: int
        ...
    class DataViewGroup(ReferenceTarget):
        ...
    class Data_Icon(helper):
        Visible_Icon: bool
        Icon_Type: int
        Icon_Parameter_1: float
        Icon_Parameter_2: float
        Icon_Parameter_3: float
        Color_Coordinated: bool
        Auto_Update: bool
        SubOperators: MXSWrapperBase
        Selected_SubOperators: MXSWrapperBase
        groups: MXSWrapperBase
        Enable_By_Switch: bool
        Default_Width: int
        Default_Offset: int
        Default_Height: int
        Default_Range_Type: int
        Default_Range_Min: float
        Default_Range_Max: float
        Activity_Type: int
        Time_On: int
        Time_Off: int
        Animatable_Active: bool
        PDView_Origin_X: int
        PDView_Origin_Y: int
        PDView_Width: int
        PDView_Height: int
        PDView_Divider: int
        PDView_Show_Depot: bool
        PDView_Description_Type: int
        PDView_Show_Parameters: bool
        Use_Dynamic_Names_For_New: bool
        Auto_Update_On_Data_View_Close: bool
        Repeats: int
        ...
    class Data_Operator(helper):
        Visible_Icon: bool
        Icon_Type: int
        Icon_Parameter_1: float
        Icon_Parameter_2: float
        Icon_Parameter_3: float
        Color_Coordinated: bool
        Auto_Update: bool
        SubOperators: MXSWrapperBase
        Selected_SubOperators: MXSWrapperBase
        groups: MXSWrapperBase
        Enable_By_Switch: bool
        Default_Width: int
        Default_Offset: int
        Default_Height: int
        Default_Range_Type: int
        Default_Range_Min: float
        Default_Range_Max: float
        Activity_Type: int
        Time_On: int
        Time_Off: int
        Animatable_Active: bool
        PDView_Origin_X: int
        PDView_Origin_Y: int
        PDView_Width: int
        PDView_Height: int
        PDView_Divider: int
        PDView_Show_Depot: bool
        PDView_Description_Type: int
        PDView_Show_Parameters: bool
        Use_Dynamic_Names_For_New: bool
        Auto_Update_On_Data_View_Close: bool
        Repeats: int
        ...
    class Data_Test(helper):
        Visible_Icon: bool
        Icon_Type: int
        Icon_Parameter_1: float
        Icon_Parameter_2: float
        Icon_Parameter_3: float
        Color_Coordinated: bool
        Auto_Update: bool
        SubOperators: MXSWrapperBase
        Selected_SubOperators: MXSWrapperBase
        groups: MXSWrapperBase
        Enable_By_Switch: bool
        Default_Width: int
        Default_Offset: int
        Default_Height: int
        Default_Range_Type: int
        Default_Range_Min: float
        Default_Range_Max: float
        Activity_Type: int
        Time_On: int
        Time_Off: int
        Animatable_Active: bool
        PDView_Origin_X: int
        PDView_Origin_Y: int
        PDView_Width: int
        PDView_Height: int
        PDView_Divider: int
        PDView_Show_Depot: bool
        PDView_Description_Type: int
        PDView_Show_Parameters: bool
        Use_Dynamic_Names_For_New: bool
        Auto_Update_On_Data_View_Close: bool
        Repeats: int
        ...
    class Daylight(System):
        ...
    class DaylightAssemblyHead(helper):
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
    class Daylight_Slave_Intensity_Controller(floatController):
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
    class Default_Color_Picker(colorPicker):
        ...
    class Default_Scanline_Renderer(RendererClass):
        ...
    class Default_Sound(SoundClass):
        ...
    class Deflector(SpacewarpObject):
        Bounce: float
        width: float
        length: float
        variation: float
        chaos: float
        friction: float
        inheritVelocity: float
        ...
    class Deflectorbinding(SpacewarpModifier):
        ...
    class Deform_Curve(ReferenceMaker):
        ...
    class Deformable_gPoly(GeometryClass):
        ...
    class DegToRad(Primitive):
        ...
    class Delegate(helper):
        width: float
        depth: float
        height: float
        velocityColor: MXSWrapperBase
        active: bool
        showForces: bool
        showVelocity: bool
        showCogStates: bool
        xyConstrain: bool
        useHierBbox: bool
        averageSpeed: float
        maxaccel: float
        turnDecel: float
        turnDecelAngle: float
        inclineDecel: float
        inclineDecelAngle: float
        declineAccel: float
        declineAccelAngle: float
        maxTurnVel: float
        maxTurnAccel: float
        maxIncline: float
        maxDecline: float
        maxBank: float
        maxBankVel: float
        bankPerTurn: float
        useBiped: bool
        biped: None
        startframe: int
        Priority: int
        startClip: int
        behaviors: MXSWrapperBase
        weights: MXSWrapperBase
        duration: int
        index: int
        randID: int
        simpos: MXSWrapperBase
        ...
    class DeleteMesh(modifier):
        ...
    class DeleteParticles(helper):
        type: int
        Life_Span: int
        variation: int
        Random_Seed: int
        ...
    class DeletePatch(modifier):
        ...
    class DeleteSplineModifier(modifier):
        ...
    class DeleteTw(BipedGeneric):
        ...
    class DeleteWeight(BipedGeneric):
        ...
    class Dent(textureMap):
        map1: None
        map2: None
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1Enabled: bool
        map2Enabled: bool
        size: float
        strength: float
        iterations: int
        coords: MXSWrapperBase
        ...
    class DepthFragment(GraphicsFragmentPlugin):
        ...
    class Depth_of_Field(renderEffect):
        affectAlpha: bool
        focalPoint: int
        focalType: int
        horizFocalLoss: float
        vertFocalLoss: float
        focalRange: float
        focalLimit: float
        camNodeIndex: int
        focalNodeIndex: int
        ...
    class Depth_of_FieldMPassCamEffect(MPassCamEffect):
        useTargetDistance: bool
        focalDepth: float
        displayPasses: bool
        useOriginalLocation: bool
        totalPasses: int
        sampleRadius: float
        sampleBias: float
        normalizeWeights: bool
        ditherStrength: float
        tileSize: int
        disableFiltering: bool
        disableAntialiasing: bool
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
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        lightingOn: bool
        ...
    class DigitData(ReferenceTarget):
        ...
    class DigitDataFloatController(floatController):
        ...
    class DigitSegTrans(Matrix3Controller):
        ...
    class DirectX_9_Shader(material):
        effectFile: str
        useshaderfx: int
        shaderfxgraph: None
        technique: int
        renderEnabled: bool
        renderMaterial: MXSWrapperBase
        engineresource: None
        presetmaterial: int
        parentmaterial: None
        ...
    class DirectX_9_ShaderReferenceTarget(ReferenceTarget):
        ...
    class Directionallight(light):
        aspect: float
        rgb: MXSWrapperBase
        color: MXSWrapperBase
        contrast: float
        enabled: bool
        on: bool
        type: MXSWrapperBase
        value: int
        falloff: float
        excludeList: MXSWrapperBase
        includeList: None
        showCone: bool
        multiplier: float
        softenDiffuseEdge: float
        hotspot: float
        farAttenStart: float
        farAttenEnd: float
        nearAttenStart: float
        nearAttenEnd: float
        atmosOpacity: float
        atmosColorAmt: float
        decayRadius: float
        shadowColor: MXSWrapperBase
        shadowMultiplier: float
        hsv: MXSWrapperBase
        hue: int
        saturation: int
        inclExclType: int
        affectDiffuse: bool
        affectSpecular: bool
        useNearAtten: bool
        showNearAtten: bool
        useFarAtten: bool
        showFarAtten: bool
        attenDecay: int
        projector: bool
        projectorMap: None
        castShadows: bool
        useGlobalShadowSettings: bool
        raytracedShadows: bool
        overShoot: bool
        coneShape: int
        lightShape: int
        atmosShadows: bool
        lightAffectsShadow: bool
        shadowProjectorMap: None
        useShadowProjectorMap: bool
        ambientOnly: bool
        shadowgenerator: MXSWrapperBase
        ...
    class DisableSceneRedraw(Primitive):
        ...
    class DisableStatusXYZ(Primitive):
        ...
    class DiscreetRadiosityMaterial(material):
        reflectanceScale: float
        colorBleed: float
        transmittanceScale: float
        luminanceScale: float
        bumpScale: float
        baseMaterial: MXSWrapperBase
        ...
    class Discreet_Radiosity(RadiosityEffect):
        radInitialQuality: float
        radGlobalRefineSteps: int
        radSelectionRefineSteps: int
        radFiltering: int
        radProcessObjectRefineSteps: bool
        radDisplayInViewport: bool
        radProcessInRenderOnly: bool
        radDirectFiltering: int
        meshingEnabled: bool
        meshingSize: float
        useAdaptiveMeshing: bool
        minimumMeshSize: float
        initialMeshSize: float
        contrastThreshold: float
        includePointLights: bool
        includeLinearLights: bool
        includeAreaLights: bool
        includeSelfEmittingLights: bool
        shootDirectLights: bool
        includeSkylight: bool
        minimumSelfEmittingSize: float
        lightPaintingIntensity: float
        lightPaintingPressure: float
        lightUnitsUsed: int
        rmRegather: bool
        rmReuseDirectIllumination: bool
        rmRaysPerSample: int
        rmFilterRadius: float
        rmClampEnabled: bool
        rmClampValue: float
        rmAdaptiveEnabled: bool
        rmSampleSpacing: int
        rmMinSampleSpacing: int
        rmSubdivisionContrast: float
        rmShowSamples: bool
        statNumFaces: int
        statRefineIterations: int
        statSolutionQuality: float
        statNumGeomObjects: int
        statNumLightObjects: int
        statMeshSize: float
        elapsedTime: int
        ...
    class Discretizator(ReferenceTarget):
        type: int
        Base_Integer: int
        Base_Float: float
        Base_Time: int
        Base_World: float
        Base_Percent: float
        Base_Angle: float
        Step_Integer: int
        Step_Float: float
        Step_Time: int
        Step_World: float
        Step_Percent: float
        Step_Angle: float
        Use_As_Speed_Or_Spin_Rate: bool
        Units_Per_Type: int
        filter: None
        Input: None
        ...
    class Disp_Approx(modifier):
        ...
    class Displace(modifier):
        axis: int
        bitmap: None
        blur: float
        height: float
        length: float
        map: None
        width: float
        cap: bool
        U_Tile: float
        V_Tile: float
        decay: float
        maptype: int
        lumCenter: float
        lumCenterEnable: bool
        useMap: bool
        applyMap: bool
        U_Flip: bool
        V_Flip: bool
        W_Flip: bool
        strength: float
        W_Tile: float
        Map_or_Vertex_Color: int
        Map_Channel: int
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
    class DisplayData(helper):
        color: MXSWrapperBase
        Show_Numbering: bool
        Add_Prefix: bool
        Prefix_Text: str
        Data_Channel: None
        Data_Handle: int
        Real_Show_As: int
        Vector_Show_As: int
        Quaternion_Show_As: int
        Matrix_Show_As: int
        Complex_Show_As: int
        Pair_Show_As: int
        Rate_Value: bool
        Units_Per_Type: int
        Offset_LeftRight: int
        Offset_UpDown: int
        Offset_InOut: int
        Precision: int
        Filter_Type: int
        Group_Selection: None
        Execution_Order: int
        ...
    class DisplayManager(Interface):
        ...
    class DisplayParticles(helper):
        type: int
        visible: float
        color: MXSWrapperBase
        Show_Numbering: bool
        Selected_Type: int
        ...
    class DisplayScriptParticles(helper):
        color: MXSWrapperBase
        Show_Numbering: bool
        Add_Prefix: bool
        Prefix_Text: str
        Script_Data_Type: int
        Offset_LeftRight: int
        Offset_UpDown: int
        Offset_InOut: int
        Precision: int
        Filter_Type: int
        Group_Selection: None
        Execution_Order: int
        ...
    class DisplayTempPrompt(Primitive):
        ...
    class Display_Script(helper):
        color: MXSWrapperBase
        Show_Numbering: bool
        Add_Prefix: bool
        Prefix_Text: str
        Script_Data_Type: int
        Offset_LeftRight: int
        Offset_UpDown: int
        Offset_InOut: int
        Precision: int
        Filter_Type: int
        Group_Selection: None
        Execution_Order: int
        ...
    class DoesSelectedContainInterface(MAXScriptFunction):
        ...
    class Donut(shape):
        steps: int
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        radius1: float
        radius2: float
        ...
    class Double(Value):
        ...
    class DoublePacket(ReferenceMaker):
        ...
    class DoubleSided(material):
        material1: MXSWrapperBase
        material2: MXSWrapperBase
        map1Enabled: bool
        map2Enabled: bool
        translucency: float
        ...
    class Drag(SpacewarpObject):
        timeOn: MXSWrapperBase
        timeOff: MXSWrapperBase
        symmetry: int
        dampingX: float
        rangeX: float
        fallOffX: float
        dampingY: float
        rangeY: float
        fallOffY: float
        dampingZ: float
        rangeZ: float
        fallOffZ: float
        dampingR: float
        rangeR: float
        fallOffR: float
        dampingGC: float
        rangeGC: float
        fallOffGC: float
        dampingRC: float
        rangeRC: float
        fallOffRC: float
        dampingC: float
        rangeC: float
        fallOffC: float
        dampingAX: float
        rangeAX: float
        fallOffAX: float
        rangeless: bool
        iconSize: float
        ...
    class DragMod(SpacewarpModifier):
        ...
    class Dummy(helper):
        boxsize: MXSWrapperBase
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
    class DxMaterial(material):
        effectFile: str
        useshaderfx: int
        shaderfxgraph: None
        technique: int
        renderEnabled: bool
        renderMaterial: MXSWrapperBase
        engineresource: None
        presetmaterial: int
        parentmaterial: None
        k_a: MXSWrapperBase
        k_d: MXSWrapperBase
        k_s: MXSWrapperBase
        n: int
        g_AlphaVertex: bool
        g_AddVertexColor: bool
        g_UseParallax: bool
        g_ParallaxScale: float
        g_ParallaxBias: float
        g_AmbientOccEnable: bool
        g_TopDiffuseEnable: bool
        g_BottomDiffuseEnable: bool
        g_SpecularEnable: bool
        g_NormalEnable: bool
        g_FlipGreen: bool
        useMikkT: bool
        CalculateBitangentPerPixel: bool
        orthogonalizeTangentBitangentPerPixel: bool
        g_BumpScale: float
        g_ReflectionEnable: bool
        g_ReflectAmount: float
        g_AmbientOccTexture: None
        g_TopTexture: None
        g_TopTexturemapChannel: int
        g_BottomTexture: None
        g_BottomTexturemapChannel: int
        g_SpecularTexture: None
        g_NormalTexture: None
        g_ReflectionTexture: None
        Lamp0Pos: int
        k_a: MXSWrapperBase
        k_d: MXSWrapperBase
        k_s: MXSWrapperBase
        n: int
        g_AlphaVertex: bool
        g_AddVertexColor: bool
        g_UseParallax: bool
        g_ParallaxScale: float
        g_ParallaxBias: float
        g_AmbientOccEnable: bool
        g_TopDiffuseEnable: bool
        g_BottomDiffuseEnable: bool
        g_SpecularEnable: bool
        g_NormalEnable: bool
        g_FlipGreen: bool
        useMikkT: bool
        CalculateBitangentPerPixel: bool
        orthogonalizeTangentBitangentPerPixel: bool
        g_BumpScale: float
        g_ReflectionEnable: bool
        g_ReflectAmount: float
        g_AmbientOccTexture: None
        g_TopTexture: None
        g_TopTexturemapChannel: int
        g_BottomTexture: None
        g_BottomTexturemapChannel: int
        g_SpecularTexture: None
        g_NormalTexture: None
        g_ReflectionTexture: None
        Lamp0Pos: int
        k_a: MXSWrapperBase
        k_d: MXSWrapperBase
        k_s: MXSWrapperBase
        n: int
        g_AlphaVertex: bool
        g_AddVertexColor: bool
        g_UseParallax: bool
        g_ParallaxScale: float
        g_ParallaxBias: float
        g_AmbientOccEnable: bool
        g_TopDiffuseEnable: bool
        g_BottomDiffuseEnable: bool
        g_SpecularEnable: bool
        g_NormalEnable: bool
        g_FlipGreen: bool
        useMikkT: bool
        CalculateBitangentPerPixel: bool
        orthogonalizeTangentBitangentPerPixel: bool
        g_BumpScale: float
        g_ReflectionEnable: bool
        g_ReflectAmount: float
        g_AmbientOccTexture: None
        g_TopTexture: None
        g_TopTexturemapChannel: int
        g_BottomTexture: None
        g_BottomTexturemapChannel: int
        g_SpecularTexture: None
        g_NormalTexture: None
        g_ReflectionTexture: None
        Lamp0Pos: int
        k_a: MXSWrapperBase
        k_d: MXSWrapperBase
        k_s: MXSWrapperBase
        n: int
        g_AlphaVertex: bool
        g_AddVertexColor: bool
        g_UseParallax: bool
        g_ParallaxScale: float
        g_ParallaxBias: float
        g_AmbientOccEnable: bool
        g_TopDiffuseEnable: bool
        g_BottomDiffuseEnable: bool
        g_SpecularEnable: bool
        g_NormalEnable: bool
        g_FlipGreen: bool
        useMikkT: bool
        CalculateBitangentPerPixel: bool
        orthogonalizeTangentBitangentPerPixel: bool
        g_BumpScale: float
        g_ReflectionEnable: bool
        g_ReflectAmount: float
        g_AmbientOccTexture: None
        g_TopTexture: None
        g_TopTexturemapChannel: int
        g_BottomTexture: None
        g_BottomTexturemapChannel: int
        g_SpecularTexture: None
        g_NormalTexture: None
        g_ReflectionTexture: None
        Lamp0Pos: int
        k_a: MXSWrapperBase
        k_d: MXSWrapperBase
        k_s: MXSWrapperBase
        n: int
        g_AlphaVertex: bool
        g_AddVertexColor: bool
        g_UseParallax: bool
        g_ParallaxScale: float
        g_ParallaxBias: float
        g_AmbientOccEnable: bool
        g_TopDiffuseEnable: bool
        g_BottomDiffuseEnable: bool
        g_SpecularEnable: bool
        g_NormalEnable: bool
        g_FlipGreen: bool
        useMikkT: bool
        CalculateBitangentPerPixel: bool
        orthogonalizeTangentBitangentPerPixel: bool
        g_BumpScale: float
        g_ReflectionEnable: bool
        g_ReflectAmount: float
        g_AmbientOccTexture: None
        g_TopTexture: None
        g_TopTexturemapChannel: int
        g_BottomTexture: None
        g_BottomTexturemapChannel: int
        g_SpecularTexture: None
        g_NormalTexture: None
        g_ReflectionTexture: None
        Lamp0Pos: int
        k_a: MXSWrapperBase
        k_d: MXSWrapperBase
        k_s: MXSWrapperBase
        n: int
        g_AlphaVertex: bool
        g_AddVertexColor: bool
        g_UseParallax: bool
        g_ParallaxScale: float
        g_ParallaxBias: float
        g_AmbientOccEnable: bool
        g_TopDiffuseEnable: bool
        g_BottomDiffuseEnable: bool
        g_SpecularEnable: bool
        g_NormalEnable: bool
        g_FlipGreen: bool
        useMikkT: bool
        CalculateBitangentPerPixel: bool
        orthogonalizeTangentBitangentPerPixel: bool
        g_BumpScale: float
        g_ReflectionEnable: bool
        g_ReflectAmount: float
        g_AmbientOccTexture: None
        g_TopTexture: None
        g_TopTexturemapChannel: int
        g_BottomTexture: None
        g_BottomTexturemapChannel: int
        g_SpecularTexture: None
        g_NormalTexture: None
        g_ReflectionTexture: None
        Lamp0Pos: int
        k_a: MXSWrapperBase
        k_d: MXSWrapperBase
        k_s: MXSWrapperBase
        n: int
        g_AlphaVertex: bool
        g_AddVertexColor: bool
        g_UseParallax: bool
        g_ParallaxScale: float
        g_ParallaxBias: float
        g_AmbientOccEnable: bool
        g_TopDiffuseEnable: bool
        g_BottomDiffuseEnable: bool
        g_SpecularEnable: bool
        g_NormalEnable: bool
        g_FlipGreen: bool
        useMikkT: bool
        CalculateBitangentPerPixel: bool
        orthogonalizeTangentBitangentPerPixel: bool
        g_BumpScale: float
        g_ReflectionEnable: bool
        g_ReflectAmount: float
        g_AmbientOccTexture: None
        g_TopTexture: None
        g_TopTexturemapChannel: int
        g_BottomTexture: None
        g_BottomTexturemapChannel: int
        g_SpecularTexture: None
        g_NormalTexture: None
        g_ReflectionTexture: None
        Lamp0Pos: int
        k_a: MXSWrapperBase
        k_d: MXSWrapperBase
        k_s: MXSWrapperBase
        n: int
        g_AlphaVertex: bool
        g_AddVertexColor: bool
        g_UseParallax: bool
        g_ParallaxScale: float
        g_ParallaxBias: float
        g_AmbientOccEnable: bool
        g_TopDiffuseEnable: bool
        g_BottomDiffuseEnable: bool
        g_SpecularEnable: bool
        g_NormalEnable: bool
        g_FlipGreen: bool
        useMikkT: bool
        CalculateBitangentPerPixel: bool
        orthogonalizeTangentBitangentPerPixel: bool
        g_BumpScale: float
        g_ReflectionEnable: bool
        g_ReflectAmount: float
        g_AmbientOccTexture: None
        g_TopTexture: None
        g_TopTexturemapChannel: int
        g_BottomTexture: None
        g_BottomTexturemapChannel: int
        g_SpecularTexture: None
        g_NormalTexture: None
        g_ReflectionTexture: None
        Lamp0Pos: int
        k_a: MXSWrapperBase
        k_d: MXSWrapperBase
        k_s: MXSWrapperBase
        n: int
        g_AlphaVertex: bool
        g_AddVertexColor: bool
        g_UseParallax: bool
        g_ParallaxScale: float
        g_ParallaxBias: float
        g_AmbientOccEnable: bool
        g_TopDiffuseEnable: bool
        g_BottomDiffuseEnable: bool
        g_SpecularEnable: bool
        g_NormalEnable: bool
        g_FlipGreen: bool
        useMikkT: bool
        CalculateBitangentPerPixel: bool
        orthogonalizeTangentBitangentPerPixel: bool
        g_BumpScale: float
        g_ReflectionEnable: bool
        g_ReflectAmount: float
        g_AmbientOccTexture: None
        g_TopTexture: None
        g_TopTexturemapChannel: int
        g_BottomTexture: None
        g_BottomTexturemapChannel: int
        g_SpecularTexture: None
        g_NormalTexture: None
        g_ReflectionTexture: None
        Lamp0Pos: int
        ...
    class DynBuilding(modifier):
        Xamount: float
        Xsegs: int
        XcapStart: bool
        XcapEnd: bool
        XcapType: int
        Xoutput: int
        XmatIDs: bool
        XuseShapeIDs: bool
        Xsmooth: bool
        XmapCoords: bool
        XrealWorldMapSize: bool
        Xfloors: int
        XwallMatIDs: int
        XmapWidth: float
        XmapType: int
        ...
    class DynDiv(modifier):
        ...
    class DynGRail(modifier):
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
    class DynMarks(modifier):
        ...
    class DynSMesh(modifier):
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
    class Ease(floatController):
        ...
    class EdgeSelection(Value):
        ...
    class EditAtmosphere(Primitive):
        ...
    class EditNormals(modifier):
        selectBy: int
        ignoreBackfacing: bool
        showHandles: bool
        displayLength: float
        ...
    class EditPolyMod(modifier):
        currentOperation: int
        animationMode: int
        showcage: bool
        useStackSelection: bool
        SelectByVertex: bool
        ignoreBackfacing: bool
        SelectByAngle: bool
        selectAngle: float
        useSoftSel: bool
        ssUseEdgeDist: bool
        ssEdgeDist: int
        affectBackfacing: bool
        falloff: float
        pinch: float
        bubble: float
        lockSoftSel: bool
        paintselmode: int
        paintSelValue: float
        paintSelSize: float
        paintSelStrength: float
        paintdeformmode: int
        paintDeformValue: float
        paintDeformSize: float
        paintDeformStrength: float
        paintDeformAxis: int
        constrainType: int
        preserveUVs: bool
        split: bool
        smoothness: float
        separateBySmoothing: bool
        separateByMaterial: bool
        deleteIsolatedverts: bool
        extrudeFaceType: int
        extrudeFaceHeight: float
        extrudeVertexHeight: float
        extrudeEdgeHeight: float
        extrudeVertexWidth: float
        extrudeEdgeWidth: float
        bevelType: int
        bevelHeight: float
        bevelOutline: float
        outlineAmount: float
        insetamount: float
        insetType: int
        chamferVertexAmount: float
        chamferVertexOpen: bool
        chamferEdgeAmount: float
        edgeChamferSegments: int
        chamferEdgeOpen: bool
        weldVertexThreshold: float
        weldEdgeThreshold: float
        tessellateByFace: int
        tessTension: float
        connectEdgeSegments: int
        extrudeAlongSplineNode: None
        extrudeAlongSplineSegments: int
        extrudeAlongSplineTaper: float
        extrudeAlongSplineTaperCurve: float
        extrudeAlongSplineTwist: float
        extrudeAlongSplineRotation: float
        extrudeAlongSplineAlign: bool
        worldToObjectTransform: MXSWrapperBase
        hingeAngle: float
        hingeBase: MXSWrapperBase
        hingeDirection: MXSWrapperBase
        hingeSegments: int
        alignType: int
        alignPlaneNormal: MXSWrapperBase
        alignPlaneOffset: float
        autoSmoothThreshold: float
        smoothingGroupsToSet: int
        smoothingGroupsToClear: int
        materialIDToSet: int
        selectByMaterialID: int
        selectByMaterialClear: bool
        selectBySmoothingGroup: int
        selectBySmoothingGroupClear: bool
        bridgeSegments: int
        bridgeTaper: float
        bridgeBias: float
        bridgeSmoothThreshold: float
        bridgeSelected: int
        bridgeTwist1: int
        bridgeTwist2: int
        bridgeTarget1: int
        bridgeTarget2: int
        relaxAmount: float
        relaxIterations: int
        relaxHoldBoundaryPoints: bool
        relaxHoldOuterPoints: bool
        bridgeEdgeAdjacent: float
        bridgeReverseTriangle: int
        connectEdgePinch: int
        connectEdgeSlide: int
        breakDistance: float
        remveEdgeCtrlKey: bool
        cageColor: MXSWrapperBase
        selectedCageColor: MXSWrapperBase
        selectMode: int
        edgeChamferMiteringType: int
        edgeChamferTension: float
        edgeChamferDepth: float
        edgeChamferEndBias: float
        edgeChamferRadialBias: float
        edgeChamferInvert: bool
        edgeChamferSmooth: bool
        edgeChamferSmoothType: int
        edgeChamferSmoothThreshold: float
        dataChannel: int
        dataValue: float
        hardedgedisplaycolor: MXSWrapperBase
        hardedgedisplay: int
        lastDeltaIndex: int
        extrudeFaceBias: float
        bevelFaceBias: float
        edgeChamferTypeOBSOLETE: int
        edgeChamferQuadIntersectionsOBSOLETE: bool
        chamferVertexSegments: int
        chamferVertexDepth: float
        chamferVertexSmooth: bool
        chamferVertexSmoothType: int
        chamferVertexSmoothThreshold: float
        ...
    class EditPolyModReadyToBridge(Primitive):
        ...
    class EditRenderRegion(Interface):
        ...
    class EditTextControl(RolloutControl):
        ...
    class Edit_Mesh(modifier):
        ...
    class Edit_Normals(modifier):
        selectBy: int
        ignoreBackfacing: bool
        showHandles: bool
        displayLength: float
        ...
    class Edit_Patch(modifier):
        ...
    class Edit_Poly(modifier):
        currentOperation: int
        animationMode: int
        showcage: bool
        useStackSelection: bool
        SelectByVertex: bool
        ignoreBackfacing: bool
        SelectByAngle: bool
        selectAngle: float
        useSoftSel: bool
        ssUseEdgeDist: bool
        ssEdgeDist: int
        affectBackfacing: bool
        falloff: float
        pinch: float
        bubble: float
        lockSoftSel: bool
        paintselmode: int
        paintSelValue: float
        paintSelSize: float
        paintSelStrength: float
        paintdeformmode: int
        paintDeformValue: float
        paintDeformSize: float
        paintDeformStrength: float
        paintDeformAxis: int
        constrainType: int
        preserveUVs: bool
        split: bool
        smoothness: float
        separateBySmoothing: bool
        separateByMaterial: bool
        deleteIsolatedverts: bool
        extrudeFaceType: int
        extrudeFaceHeight: float
        extrudeVertexHeight: float
        extrudeEdgeHeight: float
        extrudeVertexWidth: float
        extrudeEdgeWidth: float
        bevelType: int
        bevelHeight: float
        bevelOutline: float
        outlineAmount: float
        insetamount: float
        insetType: int
        chamferVertexAmount: float
        chamferVertexOpen: bool
        chamferEdgeAmount: float
        edgeChamferSegments: int
        chamferEdgeOpen: bool
        weldVertexThreshold: float
        weldEdgeThreshold: float
        tessellateByFace: int
        tessTension: float
        connectEdgeSegments: int
        extrudeAlongSplineNode: None
        extrudeAlongSplineSegments: int
        extrudeAlongSplineTaper: float
        extrudeAlongSplineTaperCurve: float
        extrudeAlongSplineTwist: float
        extrudeAlongSplineRotation: float
        extrudeAlongSplineAlign: bool
        worldToObjectTransform: MXSWrapperBase
        hingeAngle: float
        hingeBase: MXSWrapperBase
        hingeDirection: MXSWrapperBase
        hingeSegments: int
        alignType: int
        alignPlaneNormal: MXSWrapperBase
        alignPlaneOffset: float
        autoSmoothThreshold: float
        smoothingGroupsToSet: int
        smoothingGroupsToClear: int
        materialIDToSet: int
        selectByMaterialID: int
        selectByMaterialClear: bool
        selectBySmoothingGroup: int
        selectBySmoothingGroupClear: bool
        bridgeSegments: int
        bridgeTaper: float
        bridgeBias: float
        bridgeSmoothThreshold: float
        bridgeSelected: int
        bridgeTwist1: int
        bridgeTwist2: int
        bridgeTarget1: int
        bridgeTarget2: int
        relaxAmount: float
        relaxIterations: int
        relaxHoldBoundaryPoints: bool
        relaxHoldOuterPoints: bool
        bridgeEdgeAdjacent: float
        bridgeReverseTriangle: int
        connectEdgePinch: int
        connectEdgeSlide: int
        breakDistance: float
        remveEdgeCtrlKey: bool
        cageColor: MXSWrapperBase
        selectedCageColor: MXSWrapperBase
        selectMode: int
        edgeChamferMiteringType: int
        edgeChamferTension: float
        edgeChamferDepth: float
        edgeChamferEndBias: float
        edgeChamferRadialBias: float
        edgeChamferInvert: bool
        edgeChamferSmooth: bool
        edgeChamferSmoothType: int
        edgeChamferSmoothThreshold: float
        dataChannel: int
        dataValue: float
        hardedgedisplaycolor: MXSWrapperBase
        hardedgedisplay: int
        lastDeltaIndex: int
        extrudeFaceBias: float
        bevelFaceBias: float
        edgeChamferTypeOBSOLETE: int
        edgeChamferQuadIntersectionsOBSOLETE: bool
        chamferVertexSegments: int
        chamferVertexDepth: float
        chamferVertexSmooth: bool
        chamferVertexSmoothType: int
        chamferVertexSmoothThreshold: float
        ...
    class Edit_Spline(modifier):
        ...
    class EditablePolyMesh(GeometryClass):
        ...
    class Editable_Patch(GeometryClass):
        ...
    class Editable_Poly(GeometryClass):
        ...
    class Editable_mesh(GeometryClass):
        ...
    class EffectClass(Value):
        ...
    class Egg(shape):
        steps: int
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        egg_outline: bool
        egg_thickness: float
        egg_angle: float
        egg_length: float
        egg_width: float
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
    class Ellipse(shape):
        steps: int
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        length: float
        width: float
        ellipse_thickness: float
        ellipse_outline: bool
        ...
    class EmptyClass(Value):
        ...
    class EmptyModifier(modifier):
        ...
    class EmptyModifier_Old(modifier):
        myparam: str
        ...
    class EmptySource(ReferenceTarget):
        ...
    class Empty_Flow(ReferenceTarget):
        ...
    class Emulator(textureMap):
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
    class Euler_Filter(trackViewUtility):
        ...
    class Euler_XYZ(rotationController):
        axisOrder: int
        ...
    class Event(helper):
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
    class ExposeTm(helper):
        localEuler: MXSWrapperBase
        localEulerX: float
        localEulerY: float
        localEulerZ: float
        worldEuler: MXSWrapperBase
        worldEulerX: float
        worldEulerY: float
        worldEulerZ: float
        localPosition: MXSWrapperBase
        localPositionX: float
        localpositionY: float
        localPositionZ: float
        worldPosition: MXSWrapperBase
        worldPositionX: float
        worldPositionY: float
        worldPositionZ: float
        distance: float
        worldBoundingBoxSize: MXSWrapperBase
        worldBoundingBoxWidth: float
        worldBoundingBoxLength: float
        worldBoundingBoxHeight: float
        angle: float
        exposeNode: None
        localReferenceNode: None
        useParent: bool
        stripNUScale: bool
        eulerXOrder: int
        eulerYOrder: int
        eulerZOrder: int
        useTimeOffset: bool
        timeoffset: MXSWrapperBase
        size: float
        centermarker: bool
        axistripod: bool
        cross: bool
        Box: bool
        constantscreensize: bool
        drawontop: bool
        displayExposedVals: bool
        ...
    class ExposeTransform(helper):
        localEuler: MXSWrapperBase
        localEulerX: float
        localEulerY: float
        localEulerZ: float
        worldEuler: MXSWrapperBase
        worldEulerX: float
        worldEulerY: float
        worldEulerZ: float
        localPosition: MXSWrapperBase
        localPositionX: float
        localpositionY: float
        localPositionZ: float
        worldPosition: MXSWrapperBase
        worldPositionX: float
        worldPositionY: float
        worldPositionZ: float
        distance: float
        worldBoundingBoxSize: MXSWrapperBase
        worldBoundingBoxWidth: float
        worldBoundingBoxLength: float
        worldBoundingBoxHeight: float
        angle: float
        exposeNode: None
        localReferenceNode: None
        useParent: bool
        stripNUScale: bool
        eulerXOrder: int
        eulerYOrder: int
        eulerZOrder: int
        useTimeOffset: bool
        timeoffset: MXSWrapperBase
        size: float
        centermarker: bool
        axistripod: bool
        cross: bool
        Box: bool
        constantscreensize: bool
        drawontop: bool
        displayExposedVals: bool
        ...
    class Expose_Euler_Control(rotationController):
        ...
    class Expose_Float_Control(floatController):
        ...
    class Expose_Point3_Control(point3Controller):
        ...
    class ExpressSave(helper):
        ...
    class Express_Save(helper):
        ...
    class Extrude(modifier):
        matIDs: bool
        smooth: bool
        capStart: bool
        capEnd: bool
        capType: int
        segs: int
        mapcoords: bool
        output: int
        amount: float
        useShapeIDs: bool
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
    class FFD2x2x2(modifier):
        dispLattice: bool
        dispSource: bool
        deformType: int
        inPoints: bool
        outPoints: bool
        offset: float
        ...
    class FFD3x3x3(modifier):
        dispLattice: bool
        dispSource: bool
        deformType: int
        inPoints: bool
        outPoints: bool
        offset: float
        ...
    class FFD4x4x4(modifier):
        dispLattice: bool
        dispSource: bool
        deformType: int
        inPoints: bool
        outPoints: bool
        offset: float
        ...
    class FFDBox(modifier):
        dispLattice: bool
        dispSource: bool
        deformType: int
        falloff: float
        tension: float
        continuity: float
        inPoints: bool
        outPoints: bool
        offset: float
        ...
    class FFDCyl(modifier):
        dispLattice: bool
        dispSource: bool
        deformType: int
        falloff: float
        tension: float
        continuity: float
        inPoints: bool
        outPoints: bool
        offset: float
        ...
    class FFD_2x2x2(modifier):
        dispLattice: bool
        dispSource: bool
        deformType: int
        inPoints: bool
        outPoints: bool
        offset: float
        ...
    class FFD_3x3x3(modifier):
        dispLattice: bool
        dispSource: bool
        deformType: int
        inPoints: bool
        outPoints: bool
        offset: float
        ...
    class FFD_4x4x4(modifier):
        dispLattice: bool
        dispSource: bool
        deformType: int
        inPoints: bool
        outPoints: bool
        offset: float
        ...
    class FFD_Binding(SpacewarpModifier):
        ...
    class FFD_Select(modifier):
        ...
    class FaceSelection(Value):
        ...
    class Face_Extrude(modifier):
        scale: float
        amount: float
        extrudeFromCenter: bool
        ...
    class FacesOrientation(Interface):
        ...
    class Faces_Orientation(GlobalUtilityPlugin):
        ...
    class Fade(VideoPostFilter):
        ...
    class FalloffManip(helper):
        ...
    class Falloff_Manipulator(helper):
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
    class FileLink_LinkTable(floatController):
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
    class File_Output(renderEffect):
        active: bool
        affectSource: bool
        channelType: int
        cameraNode: None
        nearZ: float
        farZ: float
        fitScene: bool
        ...
    class Fillet_Chamfer(modifier):
        ...
    class FilmGrain(renderEffect):
        Grain: float
        Mask_Background: bool
        ...
    class Film_Grain(renderEffect):
        Grain: float
        Mask_Background: bool
        ...
    class FilterMeshColorsByHue(modifier):
        filter_width: float
        filter_value: float
        filter_depth: float
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class FilterString(Primitive):
        ...
    class Filter_kernel_plug_in_not_found(filter):
        ...
    class FindLengthSegAndParam(Primitive):
        ...
    class FindPMod(MAXScriptFunction):
        ...
    class FindPathSegAndParam(Primitive):
        ...
    class Find_Target(helper):
        Speed_Type: int
        Use_Cruise_Speed: bool
        Cruise_Speed: float
        Cruise_Speed_Variation: float
        Acceleration_Limit: float
        Sync_Type: int
        Test_Distance: float
        Timing_Type: int
        time: int
        Time_Variation: int
        Subframe_Sampling: bool
        Use_Docking_Speed: bool
        Docking_Speed: float
        Docking_Speed_Variation: float
        Target_Type: int
        Target_Objects: MXSWrapperBase
        Animated_Shape: bool
        Follow_Target: bool
        Lock_On_Target: bool
        Aim_Point_Type: int
        Assignment_Type: int
        Docking_Type: int
        icon_size: float
        Random_Seed: int
        Test_Type: int
        Ease_In: float
        Target_Sync_Type: int
        Docking_Distance: float
        Color_Type: bool
        ...
    class Fire_Effect(atmospheric):
        Stretch: float
        Smoke: int
        phase: float
        Samples: int
        density: float
        Inner_Color: MXSWrapperBase
        Outer_Color: MXSWrapperBase
        Smoke_Color: MXSWrapperBase
        Flame_Type: int
        Regularity: float
        Flame_Size: float
        Flame_Detail: float
        Drift: float
        Explosion: int
        Fury: float
        ...
    class FixAmbient(UtilityPlugin):
        ...
    class FixInvalidMaterialsForDaylightSimulation(MAXScriptFunction):
        ...
    class Fix_Ambient(UtilityPlugin):
        ...
    class Fixed(GeometryClass):
        height: float
        width: float
        depth: float
        Chamfered_Profile: bool
        Number_of_Panels_Horizontally: int
        Number_of_Panels_Vertically: int
        Horizontal_Frame_Width: float
        Vertical_Frame_Width: float
        Frame_Thickness: float
        Glazing_Thickness: float
        Rail_Width: float
        Generate_Mapping_Coords: bool
        ...
    class FlashNodes(Primitive):
        ...
    class Flat_Mirror(textureMap):
        blurAmount: float
        distortionAmount: float
        level: float
        size: float
        phase: float
        applyBlur: bool
        nthframe: int
        frame: int
        useEnviroment: bool
        applyToFaceID: bool
        faceID: int
        distortionType: int
        noiseType: int
        ...
    class Flex(modifier):
        Flex: float
        strength: float
        sway: float
        referenceFrame: int
        paintStrength: float
        paintRadius: float
        paintFeather: float
        paintBackface: bool
        forceNode: MXSWrapperBase
        absolute: bool
        solver: int
        Samples: int
        chase: bool
        enableCenter: bool
        endframe: int
        enableEndFrame: bool
        colliderNode: MXSWrapperBase
        stretchStrength: float
        stretchSway: float
        torqueStrength: float
        torqueSway: float
        extraStrength: MXSWrapperBase
        extraSway: MXSWrapperBase
        holdRadius: float
        addMode: int
        displaySprings: bool
        holdLength: bool
        holdLengthPercent: float
        lazyEval: bool
        Stretch: float
        Stiffness: float
        enableAdvanceSprings: bool
        springColors: MXSWrapperBase
        customSpringDisplay: MXSWrapperBase
        affectAll: bool
        createSpringDepth: int
        createSpringMult: float
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
        TexEnv: int
        ...
    class FlippedFacesClass(GlobalUtilityPlugin):
        ...
    class FlippedUVWFaces(Interface):
        ...
    class FlippedUVWFacesClass(GlobalUtilityPlugin):
        ...
    class Flipped_UVW_Faces(GlobalUtilityPlugin):
        ...
    class FloatLimitCtrl(floatController):
        Enable: bool
        Upper_Limit: float
        lower_limit: float
        upper_limit_enabled: bool
        lower_limit_enabled: bool
        static_value: float
        upper_smoothing: float
        lower_smoothing: float
        ...
    class FloatList(floatController):
        weight: MXSWrapperBase
        average: bool
        ...
    class FloatPacket(ReferenceMaker):
        ...
    class FloatReactor(floatController):
        ...
    class FloatXRefCtrl(floatController):
        ...
    class Float_Expression(floatController):
        ...
    class Float_Layer(floatController):
        ...
    class Float_Mixer_Controller(floatController):
        ...
    class Float_Motion_Capture(floatController):
        ...
    class Float_Reactor(floatController):
        ...
    class Float_Wire(floatController):
        ...
    class Float_XRef_Controller(floatController):
        ...
    class Flow(GeometryClass):
        width: float
        laneWidth: float
        directionIndex: int
        positionSample: int
        genderSample: int
        linkPortals: bool
        density: float
        speed: float
        running: float
        gender: float
        density2: float
        speed2: float
        running2: float
        gender2: float
        ...
    class FlowRaytraceInterface(Interface):
        ...
    class FltGUP(GlobalUtilityPlugin):
        ...
    class FltImport(ImporterPlugin):
        ...
    class FltTextureAttrCustAttrib(CustAttrib):
        TexEnv: int
        ...
    class FluidLoader(GeometryClass):
        iconSize: float
        showIcon: int
        cacheTab: MXSWrapperBase
        cacheNameTab: MXSWrapperBase
        cacheFlagsTab: MXSWrapperBase
        displayCacheLimit: float
        materialID_Tab: MXSWrapperBase
        playbackMode_Tab: MXSWrapperBase
        startOnly_Tab: MXSWrapperBase
        startFrame_Tab: MXSWrapperBase
        endFrame_Tab: MXSWrapperBase
        playbackFrame_Tab: MXSWrapperBase
        materialIDIndirect: int
        playbackModeIndirect: int
        startOnlyIndirect: int
        startFrameIndirect: int
        endFrameIndirect: int
        playbackFrameIndirect: int
        displayTypeMode: int
        viewportPercentAccessor: float
        colorChannelMode: int
        staticColor: MXSWrapperBase
        colorChannelMin: MXSWrapperBase
        colorChannelMax: MXSWrapperBase
        opacityChannelMode: float
        staticOpacity: float
        opacityChannelMin: float
        opacityChannelMax: float
        sizeChannelMode: float
        staticSize: float
        sizeChannelMin: float
        sizeChannelMax: float
        customNode: None
        foamViewportPercentAccessor: float
        foamDisplayTypeMode: int
        foamColorChannelMode: int
        foamStaticColor: MXSWrapperBase
        foamColorChannelMin: MXSWrapperBase
        foamColorChannelMax: MXSWrapperBase
        foamOpacityChannelMode: int
        foamStaticOpacity: float
        foamOpacityChannelMin: float
        foamOpacityChannelMax: float
        foamSizeChannelMode: int
        foamStaticSize: float
        foamSizeChannelMin: float
        foamSizeChannelMax: float
        meshingDropletRevealFactorAccessor: float
        meshingDropletRevealFactorTab: MXSWrapperBase
        meshingSurfaceRadiusAccessor: float
        meshingSurfaceRadiusTab: MXSWrapperBase
        meshingDropletRadiusAccessor: float
        meshingDropletRadiusTab: MXSWrapperBase
        meshingKernelFactorAccessor: float
        meshingKernelFactorTab: MXSWrapperBase
        meshingSmoothingAccessor: int
        meshingSmoothingTab: MXSWrapperBase
        meshingResolutionFactorAccessor: float
        meshingResolutionFactorTab: MXSWrapperBase
        meshingHoleKillThresholdAccessor: float
        meshingHoleKillThresholdTab: MXSWrapperBase
        meshingFlipFaceNormalAccessor: bool
        meshingFlipFaceNormalTab: MXSWrapperBase
        enableGPUPoints: bool
        liquidRenderType: int
        liquidRenderStaticSize: float
        liquidRenderSizeMin: float
        liquidRenderSizeMax: float
        liquidRenderSizeMinDomain: float
        liquidRenderSizeMaxDomain: float
        foamRenderType: int
        foamRenderStaticSize: float
        foamRenderSizeMin: float
        foamRenderSizeMax: float
        foamRenderSizeMinDomain: float
        foamRenderSizeMaxDomain: float
        liquidCustomRenderNode: None
        foamCustomRenderNode: None
        liquidRenderSizeChannel: str
        foamRenderSizeChannel: str
        liquidSizeChannelType: int
        foamSizeChannelType: int
        renderChannelMapName: MXSWrapperBase
        renderChannelMapIndex: MXSWrapperBase
        arnoldSurfaceType: int
        arnoldRenderComponentType: int
        arnoldDropletRevealFactor: float
        arnoldSurfaceRadius: float
        arnoldDropletRadius: float
        arnoldResolutionFactor: float
        arnoldHoleKillThreshold: float
        arnoldFilteringDilate: float
        arnoldFilteringSmooth: float
        arnoldFilteringSmoothMode: int
        arnoldFilteringSmoothIterations: int
        arnoldFilteringErode: float
        arnoldUseOceanBlending: bool
        arnoldOceanMeshPlane: None
        arnoldOceanBlendingBoundaryRadius: float
        arnoldMeshSubdivisions: int
        arnoldMeshSmoothing: bool
        arnoldImplicitStepSize: float
        arnoldImplicitSamples: int
        arnoldFoamSurfaceType: int
        arnoldFoamDropletRevealFactor: float
        arnoldFoamSurfaceRadius: float
        arnoldFoamDropletRadius: float
        arnoldFoamResolutionFactor: float
        arnoldFoamHoleKillThreshold: float
        arnoldFoamFilteringDilate: float
        arnoldFoamFilteringSmooth: float
        arnoldFoamFilteringSmoothMode: int
        arnoldFoamFilteringSmoothIterations: int
        arnoldFoamFilteringErode: float
        arnoldFoamUseOceanBlending: bool
        arnoldFoamOceanMeshPlane: None
        arnoldFoamOceanBlendingBoundaryRadius: float
        arnoldFoamMeshSubdivisions: int
        arnoldFoamMeshSmoothing: bool
        arnoldFoamImplicitStepSize: float
        arnoldFoamImplicitSamples: int
        arnoldPointRadiusChannel: int
        arnoldPointRadius: float
        arnoldPointStepSize: float
        arnoldPointChunkSize: int
        displayCacheLimitEnable: bool
        useLoaderObjectTransform: bool
        arnoldSurfaceChannelNameTab: MXSWrapperBase
        ...
    class FluidSimObjectManager(Interface):
        ...
    class Fog(atmospheric):
        size: float
        angle: float
        falloff: int
        phase: float
        density: float
        Bottom: float
        top: float
        fog_color: MXSWrapperBase
        fog_background: int
        fog_type: int
        near: float
        far: float
        exponential: int
        Use_Color_Map: int
        Use_Opacity_Map: int
        Horizon_Noise: int
        ...
    class FogHelper(helper):
        ...
    class Foliage(GeometryClass):
        height: float
        seed: int
        density: float
        Pruning: float
        CanopyMode: int
        GenUV: bool
        ShowTrunk: bool
        ShowBranches: bool
        ShowLeaves: bool
        ShowFruit: bool
        ShowFlowers: bool
        ShowRoots: bool
        LevelOfDetail: int
        ...
    class FoliagetextureMap(textureMap):
        ...
    class Follow_Bank(UtilityPlugin):
        ...
    class FootBend(floatController):
        ...
    class FootLift(floatController):
        ...
    class FootTrans(Matrix3Controller):
        ...
    class Footsteps(MAXWrapper):
        ...
    class Force(helper):
        Influence: float
        Sync: int
        Force_Space_Warps: MXSWrapperBase
        Force_Overlapping: int
        Use_Script_Float: int
        ...
    class ForceCompleteRedraw(Primitive):
        ...
    class FragmentGraph(GraphicsFragmentPlugin):
        ...
    class FrameTagManager(Interface):
        ...
    class Free_Area(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Free_Cylinder(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Free_Disc(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Free_Light(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Free_Linear(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Free_Point(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Free_Rectangle(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Free_Sphere(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Freecamera(camera):
        type: MXSWrapperBase
        fov: float
        targetDistance: None
        nearrange: float
        farrange: float
        nearclip: float
        near_clip: float
        farclip: float
        far_clip: float
        mpassEnabled: bool
        mpassRenderPerPass: bool
        curFOV: float
        fovType: int
        orthoProjection: bool
        showCone: bool
        showHorizon: bool
        showRanges: bool
        clipManually: bool
        mpassEffect: MXSWrapperBase
        ...
    class FreehandSpline(shape):
        steps: int
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        curveType: int
        ShowKnots: bool
        enableClosedCurve: bool
        constrainOffset: float
        enableConstrainShowNormals: bool
        enableConstrain: bool
        granularity: int
        endCreateOnButtonUp: bool
        knots: MXSWrapperBase
        normals: MXSWrapperBase
        shape_knots: MXSWrapperBase
        sampling: int
        threshold: int
        ...
    class Function(Value):
        ...
    class FunctionReferenceTarget(ReferenceTarget):
        First_Operand_Type: int
        Use_R_As_Factor_For_First_Operand: bool
        Factor_For_First_Operand: float
        Integer_Factor_For_First_Operand: int
        Use_Second_Operand: bool
        Second_Operand_Type_For_Integer_Real: int
        Second_Operand_Type_For_Quaternion: int
        Second_Operand_Type_For_Vector: int
        Use_R_As_Factor_For_Second_Operand: bool
        Factor_For_Second_Operand: float
        Integer_Factor_For_Second_Operand: int
        Function_Type_For_Boolean_Single: int
        Function_Type_For_Boolean_And_Boolean: int
        Function_Type_For_Time_Single: int
        Function_Type_For_Time_And_Time: int
        Function_Type_For_Matrix_Single: int
        Function_Type_For_Matrix_And_Matrix: int
        Function_Type_For_Quaternion_Single: int
        Function_Type_For_Quaternion_And_Quaternion: int
        Function_Type_For_Quaternion_And_Real: int
        Function_Type_For_Quaternion_And_Integer_Time: int
        Function_Type_For_Integer_Real_Single: int
        Function_Type_For_Integer_And_Real: int
        Function_Type_For_Vector_Single: int
        Function_Type_For_Vector_And_Quaternion: int
        Function_Type_For_Vector_And_Matrix: int
        Function_Type_For_Vector_And_Real: int
        Function_Type_For_Vector_And_Integer_Time: int
        Function_Type_For_Vector_And_Vector: int
        Post_Factor: float
        Integer_Post_Factor: int
        Sync_Type: int
        Use_E5: bool
        Offset_For_First_Operand: float
        Integer_Offset_For_First_Operand: int
        Restrict_By_Group_ID: bool
        Group_ID_Data_Channel: None
        Group_ID_Data_Handle: int
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        Input_5: None
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
    class Garment_Maker(modifier):
        density: float
        autoMesh: bool
        Preserve: bool
        outputType: int
        stretchMapping: bool
        figure: None
        stripwidth: float
        striptexturescale: float
        showMesh: bool
        showSeams: bool
        Relax: bool
        ...
    class Garmentize2(modifier):
        density: float
        autoMesh: bool
        Preserve: bool
        outputType: int
        stretchMapping: bool
        figure: None
        stripwidth: float
        striptexturescale: float
        showMesh: bool
        showSeams: bool
        Relax: bool
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
        height: float
        smooth: int
        radius: float
        sides: int
        mapcoords: int
        fillet: float
        Fillet_Segments: int
        Side_Segments: int
        Height_Segments: int
        ...
    class GeoSphere(GeometryClass):
        creationMethod: int
        typeInPos: MXSWrapperBase
        typeInRadius: float
        hemisphere: bool
        segs: int
        radius: float
        baseType: int
        baseToPivot: bool
        smooth: bool
        mapcoords: bool
        ...
    class GeomFilterFn(MAXScriptFunction):
        ...
    class GeomObject(Value):
        ...
    class GeometryCheckerManager(GlobalUtilityPlugin):
        ...
    class GeometryClass(node):
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
        elementName: str
        size: float
        intensity: float
        on: bool
        objectsHide: bool
        Squeeze: bool
        occlusion: float
        useSourceColor: float
        centerColor: MXSWrapperBase
        edgeColor: MXSWrapperBase
        radialMtl: None
        useRadialMtl: bool
        radialMap: None
        useRadialMap: bool
        circularColorMix: float
        quadrant1Color: MXSWrapperBase
        quadrant2Color: MXSWrapperBase
        quadrant3Color: MXSWrapperBase
        quadrant4Color: MXSWrapperBase
        circularMtl: None
        useCircularMtl: bool
        circularMap: None
        useCircularMap: bool
        radialSizeMap: None
        useRadialSizeMap: bool
        applyLights: bool
        applyImage: bool
        applyImageCenters: bool
        sourceObjectID: bool
        objectID: int
        sourceEffectsID: bool
        effectsID: int
        sourceUnclampedColor: bool
        unclampedColor: float
        unclampedColorInvert: bool
        sourceSurfaceNormal: bool
        surfaceNormal: float
        surfaceNormalInvert: bool
        sourceWhole: bool
        sourceAlpha: bool
        alpha: int
        sourceZBuffer: bool
        zHi: float
        zLo: float
        filterAll: bool
        filterEdge: bool
        filterPerimeterAlpha: bool
        filterPerimeter: bool
        filterBrightness: bool
        brightness: int
        brightnessInvert: bool
        filterHue: bool
        hue: MXSWrapperBase
        hueRange: int
        applyNoise: bool
        noiseMap: None
        radialDensity: None
        useRadialDensity: bool
        ...
    class Gnormal(textureMap):
        mult_spin: float
        bump_spin: float
        normal_map: None
        bump_map: None
        map1on: bool
        map2on: bool
        method: int
        flipred: bool
        flipgreen: bool
        swap_rg: bool
        ...
    class Go_To_Rotation(helper):
        Send_Out: bool
        Transition_Type: int
        time: int
        variation: int
        Target_Rotation: int
        Match_Initial_Spin: bool
        SpinRate: float
        Spin_Rate_Variation: float
        Ease_In: float
        Stop_Spinning: bool
        Random_Seed: int
        ...
    class Gradient(textureMap):
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        color3: MXSWrapperBase
        map1: None
        map2: None
        map3: None
        map1Enabled: bool
        map2Enabled: bool
        map3Enabled: bool
        color2Pos: float
        gradientType: int
        noiseAmount: float
        noiseType: int
        noiseSize: float
        noisePhase: float
        noiseLevels: float
        noiseThresholdLow: float
        noiseThresholdHigh: float
        noiseThresholdSMooth: float
        coords: MXSWrapperBase
        output: MXSWrapperBase
        ...
    class Gradient_GradCtlData(ReferenceTarget):
        ...
    class Gradient_Ramp(textureMap):
        size: float
        phase: float
        amount: float
        Gradient_Type: int
        Noise_Type: int
        Levels: float
        Low_Threshold: float
        High_Threshold: float
        Threshold_Smoothing: float
        Source_Map_On: int
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
    class GroupOperator(helper):
        Group_Selection: None
        Event_With_Operators: None
        Group_Selection_Operators: MXSWrapperBase
        Selection_Condition: int
        ...
    class GroupSelection(helper):
        Update_Type: int
        Reverse_Selection: bool
        Selection_Type: int
        Snapshot_Type: int
        Snapshot_Particle_System: int
        Snapshot_Indices: MXSWrapperBase
        Icon_Type: int
        Subframe_Sampling: bool
        Inside_Object: None
        Animated_Shape: bool
        Property_Type: int
        Age_From: int
        Age_To: int
        Age_Variation: int
        Speed_From: float
        Speed_To: float
        Speed_Variation: float
        Divergence: float
        Divergence_Variation: float
        Scale_From: float
        Scale_To: float
        Scale_Variation: float
        Size_From: float
        Size_To: float
        Size_Variation: float
        Index_From: int
        Index_To: int
        Index_Variation: int
        Float_From: float
        Float_To: float
        Float_Variation: float
        Chance: float
        Combine_Type: int
        Group_A: None
        Group_B: None
        icon_size: float
        Logo_Size: float
        Random_Seed: int
        Color_Coordinated: bool
        ...
    class GroupStartControl(RolloutControl):
        ...
    class Group_Operator(helper):
        Group_Selection: None
        Event_With_Operators: None
        Group_Selection_Operators: MXSWrapperBase
        Selection_Condition: int
        ...
    class Group_Select(helper):
        Update_Type: int
        Reverse_Selection: bool
        Selection_Type: int
        Snapshot_Type: int
        Snapshot_Particle_System: int
        Snapshot_Indices: MXSWrapperBase
        Icon_Type: int
        Subframe_Sampling: bool
        Inside_Object: None
        Animated_Shape: bool
        Property_Type: int
        Age_From: int
        Age_To: int
        Age_Variation: int
        Speed_From: float
        Speed_To: float
        Speed_Variation: float
        Divergence: float
        Divergence_Variation: float
        Scale_From: float
        Scale_To: float
        Scale_Variation: float
        Size_From: float
        Size_To: float
        Size_Variation: float
        Index_From: int
        Index_To: int
        Index_Variation: int
        Float_From: float
        Float_To: float
        Float_Variation: float
        Chance: float
        Combine_Type: int
        Group_A: None
        Group_B: None
        icon_size: float
        Logo_Size: float
        Random_Seed: int
        Color_Coordinated: bool
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
    class HSDS(modifier):
        LevelOfDetail: int
        displayLevel: int
        ignoreBackface: bool
        onlyCurrentLevel: bool
        vertexType: int
        Crease: float
        matID: int
        forceQuads: bool
        smoothResult: bool
        useSoftSel: bool
        useEdgeDist: bool
        affectBackface: bool
        edgeDistance: int
        falloff: float
        pinch: float
        bubble: float
        ...
    class HSDSObject(modifier):
        LevelOfDetail: int
        displayLevel: int
        ignoreBackface: bool
        onlyCurrentLevel: bool
        vertexType: int
        Crease: float
        matID: int
        forceQuads: bool
        smoothResult: bool
        useSoftSel: bool
        useEdgeDist: bool
        affectBackface: bool
        edgeDistance: int
        falloff: float
        pinch: float
        bubble: float
        ...
    class HSDS_Modifier(modifier):
        LevelOfDetail: int
        displayLevel: int
        ignoreBackface: bool
        onlyCurrentLevel: bool
        vertexType: int
        Crease: float
        matID: int
        forceQuads: bool
        smoothResult: bool
        useSoftSel: bool
        useEdgeDist: bool
        affectBackface: bool
        edgeDistance: int
        falloff: float
        pinch: float
        bubble: float
        ...
    class HSUtil(ReferenceMaker):
        ...
    class Hair(Interface):
        ...
    class HairAtmospheric(atmospheric):
        ...
    class HairAtmosphericGizmo(helper):
        ...
    class HairEffect(renderEffect):
        overSampling: int
        occlusionSetType: int
        occlusionNodes: MXSWrapperBase
        compositionMethod: int
        mbIntervalType: int
        hairMode: int
        lightingMode: int
        useAllLights: bool
        mbDuration: float
        shadowDensity: float
        mrVoxelRes: int
        applyGI: bool
        GI_Multiplier: float
        Raytrace_Reflections_Refractions: bool
        tileMemoryUsage: int
        transparencyDepth: int
        ...
    class HairGIAtmospheric(atmospheric):
        ...
    class HairLightAttr(CustAttrib):
        lightHair: bool
        shadowResolution: int
        shadowFuzz: float
        ...
    class HairMRGeomShader(textureMap):
        ...
    class HairMRIntanceGeomShader(textureMap):
        ...
    class HairMRObj(GeometryClass):
        ...
    class HairMaxUtility(UtilityPlugin):
        ...
    class HairMod(SpacewarpModifier):
        HairCount: int
        HairSegments: int
        HairPasses: int
        HairDensity: float
        HairScale: float
        HairCutLength: float
        HairRandScale: float
        HairRootThickness: float
        HairTipThickness: float
        HairDisplacement: float
        HairInterpolateGuides: bool
        MaterialSelfShadow: float
        MaterialGeomShadow: float
        MaterialSpecular: float
        MaterialSpecTint: MXSWrapperBase
        MaterialGlossness: float
        MaterialOccludedAmb: float
        MaterialTipColor: MXSWrapperBase
        MaterialTipFade: bool
        MaterialHueVariation: float
        MaterialValueVariation: float
        MaterialRootColor: MXSWrapperBase
        MaterialMutantHairColor: MXSWrapperBase
        MaterialPercentMutantHair: float
        MaterialGeomMtlID: int
        MaterialSquirrel: bool
        MaterialSpecTint2: MXSWrapperBase
        MR_ApplyShader: bool
        MR_Shader: None
        MR_SubMtlsToReplace: MXSWrapperBase
        FlyawayPerc: int
        FlyawayStren: float
        MessStren: float
        Clumps: int
        ClumpsStren: float
        ClumpsScruff: float
        ClumpsRot: float
        ClumpsOffset: float
        ClumpsColors: float
        ClumpsRand: float
        ClumpsFlat: float
        FrizzRoot: float
        FrizzTip: float
        FrizzFreqX: float
        FrizzFreqY: float
        FrizzFreqZ: float
        FrizzAnim: float
        FrizzAnimSpeed: float
        FrizzAnimDir: MXSWrapperBase
        KinkRoot: float
        KinkTip: float
        KinkFreqX: float
        KinkFreqY: float
        KinkFreqZ: float
        MultiStrandCount: int
        MultiStrandRootSplay: float
        MultiStrandTipSplay: float
        MultiRandomize: float
        MultiStrandTwist: float
        MultiStrandOffset: float
        MultiStrandAspect: float
        dynamicsMode: int
        simulationStart: int
        simulationEnd: int
        DynamicsStiffness: float
        DynamicsRootHold: float
        DynamicsDampen: float
        DynamicsGravity: float
        collisionNodes: MXSWrapperBase
        autoCollision: bool
        collisionMethod: int
        displayShowGuides: bool
        DisplayGuideColor: MXSWrapperBase
        displayShowHairs: bool
        displayHairAsGeometry: bool
        DisplayOverrideHairColor: bool
        DisplayHairColor: MXSWrapperBase
        DisplayHairPercent: float
        DisplayMaxHairs: int
        maps: MXSWrapperBase
        mapEnables: MXSWrapperBase
        forceFields: MXSWrapperBase
        mergeInstanceMaterial: bool
        byVertex: bool
        ignoreBackfacing: bool
        instanceGeomName: str
        ToolsSplineLockNode: None
        RandomSeed: int
        ...
    class HairRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class Hair_Atmospheric(atmospheric):
        ...
    class Hair_Atmospheric_Gizmo(helper):
        ...
    class Hair_GI_Atmospheric(atmospheric):
        ...
    class Hair_Instanced_Geometry_MR_Shader(textureMap):
        ...
    class Hair_MR_Geom_Shader(textureMap):
        ...
    class Hair_MR_Object(GeometryClass):
        ...
    class HalfRound(shape):
        ...
    class Hammersley(SamplerClass):
        Enable: bool
        Quality: float
        Sub_sample_Textures: bool
        ...
    class HasDictValue(Primitive):
        ...
    class HashTable(Value):
        ...
    class HdlObjObj(helper):
        ...
    class HdlTrans(Matrix3Controller):
        ...
    class Hedra(GeometryClass):
        vertices: MXSWrapperBase
        radius: float
        mapcoords: bool
        family: int
        p: float
        q: float
        scalep: float
        scaleq: float
        scaler: float
        vertType: int
        ...
    class HeightMap(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        ...
    class Helix(shape):
        height: float
        bias: float
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        radius1: float
        radius2: float
        turns: float
        direction: int
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
        Hose_Height: float
        Segments_Along_Hose: int
        Smooth_Spring: int
        Renderable_Hose: int
        Hose_Cross_Section_Type: int
        Round_Hose_Diameter: float
        Round_Hose_Sides: int
        Rectangular_Hose_Width: float
        Rectangular_Hose_Depth: float
        Rectangular_Hose_Fillet_Size: float
        Rectangular_Hose_Fillet_Segs: int
        Rectangular_Hose_Section_Rotation: float
        D_Section_Hose_Width: float
        D_Section_Hose_Depth: float
        D_Section_Hose_Fillet_Size: float
        D_Section_Hose_Fillet_Segs: int
        D_Section_Hose_Round_Segs: int
        D_Section_Hose_Section_Rotation: float
        Flex_Section_Enabled: int
        Flex_Section_Start: float
        Flex_Section_Stop: float
        Flex_Cycle_Count: int
        Flex_Section_Diameter: float
        Top_Tension: float
        Bottom_Tension: float
        End_Placement_Method: int
        Generate_Mapping_Coordinates: int
        ...
    class HotspotManip(helper):
        ...
    class Hotspot_Manip(helper):
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
    class IES_Sky(light):
        multiplier: float
        color: MXSWrapperBase
        rays_per_sample: int
        ray_Bias: float
        on: bool
        castShadows: bool
        Sky_Cover: float
        ...
    class IES_Sun(light):
        rgb: MXSWrapperBase
        multiplier: float
        contrast: float
        softenDiffuseEdge: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        targetDistance: None
        useGlobalShadowSettings: bool
        hasTarget: bool
        on: bool
        affectDiffuse: bool
        affectSpecular: bool
        castShadows: bool
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
    class IKEndSpTwistManip(helper):
        ...
    class IKHISolver(IKSolver):
        ...
    class IKLimb(IKSolver):
        ...
    class IKSolver(MAXWrapperNonRefTarg):
        ...
    class IKStartSpTwistManip(helper):
        ...
    class IKSwivelManip(helper):
        ...
    class IKSys(Interface):
        ...
    class IKTargTrans(Matrix3Controller):
        ...
    class IKTarget(helper):
        ...
    class IKTargetObj(helper):
        ...
    class IK_Chain_Object(helper):
        ...
    class IK_Controller(ReferenceTarget):
        ...
    class IK_ControllerMatrix3Controller(Matrix3Controller):
        ...
    class IK_Position_Controller(positionController):
        ...
    class IK_Spline_End_Twist_Manip(helper):
        ...
    class IK_Spline_Start_Twist_Manip(helper):
        ...
    class IK_Swivel_Manip(helper):
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
        density: float
        groups: float
        pair: float
        gender: float
        orient: float
        orientspread: float
        lookat: None
        lookatobj: None
        randseedGroup: int
        randseedIndiv: int
        randseedRot: int
        randseedGen: int
        randseedMtn: int
        id: int
        ...
    class IdleAreaSubtractArea(Primitive):
        ...
    class IesSkyLight(light):
        multiplier: float
        color: MXSWrapperBase
        rays_per_sample: int
        ray_Bias: float
        on: bool
        castShadows: bool
        Sky_Cover: float
        ...
    class IlluminanceFragment(GraphicsFragmentPlugin):
        ...
    class IlluminanceRenderElement(RenderElement):
        enabledOn: bool
        filterOn: bool
        atmosphereOn: bool
        shadowOn: bool
        elementName: str
        bitmap: None
        ScaleFactor: float
        ...
    class Illuminance_HDR_Data(RenderElement):
        enabledOn: bool
        filterOn: bool
        atmosphereOn: bool
        shadowOn: bool
        elementName: str
        bitmap: None
        ScaleFactor: float
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
    class InfluenceHelper(helper):
        on: bool
        nearDist: float
        farDist: float
        FalloffType: int
        EnableBias: bool
        BiasSelected: bool
        bias: float
        invert: bool
        showNear: bool
        showFar: bool
        nearColor: MXSWrapperBase
        farColor: MXSWrapperBase
        ...
    class InitialState(helper):
        Emit_Time: int
        Max_Spread: float
        Magnitude_Variation: float
        Divergence: float
        State_From_Type: int
        Particle_System: None
        Selected_Events: MXSWrapperBase
        Use_Age: bool
        Use_Speed: bool
        Use_Scale: bool
        Use_Rotation: bool
        Use_Spin: bool
        Use_Mapping: bool
        Use_Material_ID: bool
        Use_Script_Data: bool
        Use_Shape: bool
        Use_Selection: bool
        Lock_Position: bool
        Lock_Speed: bool
        icon_size: float
        Random_Seed: int
        Auto_Sync_Emit_Time: bool
        Color_Coordinated: bool
        ...
    class Initial_State(helper):
        Emit_Time: int
        Max_Spread: float
        Magnitude_Variation: float
        Divergence: float
        State_From_Type: int
        Particle_System: None
        Selected_Events: MXSWrapperBase
        Use_Age: bool
        Use_Speed: bool
        Use_Scale: bool
        Use_Rotation: bool
        Use_Spin: bool
        Use_Mapping: bool
        Use_Material_ID: bool
        Use_Script_Data: bool
        Use_Shape: bool
        Use_Selection: bool
        Lock_Position: bool
        Lock_Speed: bool
        icon_size: float
        Random_Seed: int
        Auto_Sync_Emit_Time: bool
        Color_Coordinated: bool
        ...
    class InitializeTimeWarp(BipedGeneric):
        ...
    class Ink(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class InkNPaint(material):
        fog_bg: bool
        bump_map_on: bool
        dsp_map_on: bool
        face_map_on: bool
        two_side_on: bool
        faceted_on: bool
        bump_map_amt: float
        dsp_map_amt: float
        bump_map: None
        dsp_map: None
        pixel_grid_on: bool
        opaque_alpha_on: bool
        mat1: None
        mat1_on: bool
        paint_color: MXSWrapperBase
        spec_color: MXSWrapperBase
        spec_gloss: float
        paint_levels: int
        paint_on: bool
        spec_on: bool
        paint_map_on: bool
        spec_map_on: bool
        sub_mtl_amt: float
        paint_map_amt: float
        spec_map_amt: float
        paint_map: None
        spec_map: None
        shade_color: MXSWrapperBase
        shade_color_map_on: bool
        shade_color_map_amt: float
        shade_color_map: None
        shade_amt_on: bool
        shade_amt: float
        color1: MXSWrapperBase
        min_ink_width: float
        ink_quality: int
        edge_ang_thresh: float
        smgroup_edge_ink_color: MXSWrapperBase
        matid_ink_color: MXSWrapperBase
        edge_ang_ink_color: MXSWrapperBase
        max_ink_width: float
        out_ink_on: bool
        smgroup_edge_ink_on: bool
        matid_ink_on: bool
        edge_ang_ink_on: bool
        ink_auto_vary_on: bool
        width_map_on: bool
        ink_on: bool
        out_ink_map_on: bool
        smgroup_edge_map_on: bool
        matid_map_on: bool
        edge_ang_ink_map_on: bool
        width_map_amt: float
        out_ink_map_amt: float
        smgroup_edge_map_amt: float
        matid_map_amt: float
        edge_ang_ink_map_amt: float
        width_map: None
        out_ink_map: None
        smgroup_edge_map: None
        matid_map: None
        edge_ang_ink_map: None
        self_overlap_ink_on: bool
        self_overlap_ink_map_on: bool
        self_overlap_ink_color: MXSWrapperBase
        self_overlap_bias: float
        self_overlap_ink_map_amt: float
        self_overlap_ink_map: None
        self_underlap_ink_on: bool
        self_underlap_ink_map_on: bool
        self_underlap_ink_color: MXSWrapperBase
        self_underlap_bias: float
        self_underlap_ink_map_amt: float
        self_underlap_ink_map: None
        intersect_bias: float
        matid_adj_req_on: bool
        matid_intersect_bias: float
        ink_width_clamp_on: bool
        sampler: int
        samplerQuality: float
        samplerEnable: bool
        samplerAdaptThreshold: float
        samplerAdaptOn: bool
        subSampleTextureOn: bool
        samplerAdvancedOptions: bool
        samplerByName: str
        UserParam0: float
        UserParam1: float
        samplerUseGlobal: bool
        init_fail_on: bool
        init_fail_color: MXSWrapperBase
        backface_error_on: bool
        backface_error_color: MXSWrapperBase
        missed_rays_error_on: bool
        missed_rays_error_color: MXSWrapperBase
        ...
    class InkRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class Inline(helper):
        ...
    class InputCustom(ReferenceTarget):
        Data_Channel: None
        Data_Handle: int
        Use_Proxy_Particles: bool
        Use_I2: bool
        I3_Usage: int
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        ...
    class InputPhysX(ReferenceTarget):
        Data_Type: int
        Match_Type: int
        Threshold_Type: int
        Collision_Type: int
        filter: None
        ...
    class InputProxy(ReferenceTarget):
        Use_I2: bool
        I3_Usage: int
        Data_Type: int
        ParticleID_Type: int
        Time_Type: int
        Position_Type: int
        Speed_Type: int
        Rotation_Type: int
        Spin_Type: int
        Scale_Type: int
        Size_Type: int
        Adjusted_By_Scale: bool
        Shape_Type: int
        Script_Type: int
        TM_Type: int
        Mapping_Type: int
        Map_Channel: int
        Group_Selection_Operator: None
        Group_Type: int
        Use_E4: bool
        Acceleration_Type: int
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        Input_5: None
        ...
    class InputStandard(ReferenceTarget):
        Data_Type: int
        ParticleID_Type: int
        Time_Type: int
        Position_Type: int
        Speed_Type: int
        Rotation_Type: int
        Spin_Type: int
        Scale_Type: int
        Size_Type: int
        Adjusted_By_Scale: bool
        Shape_Type: int
        Script_Type: int
        TM_Type: int
        Mapping_Type: int
        Map_Channel: int
        Group_Selection_Operator: None
        Group_Type: int
        Use_E1: bool
        Acceleration_Type: int
        Visibility_Type: int
        Viewport_Render_Operator: None
        filter: None
        Input_1: None
        Input_2: None
        ...
    class Input_Proxy(ReferenceTarget):
        Use_I2: bool
        I3_Usage: int
        Data_Type: int
        ParticleID_Type: int
        Time_Type: int
        Position_Type: int
        Speed_Type: int
        Rotation_Type: int
        Spin_Type: int
        Scale_Type: int
        Size_Type: int
        Adjusted_By_Scale: bool
        Shape_Type: int
        Script_Type: int
        TM_Type: int
        Mapping_Type: int
        Map_Channel: int
        Group_Selection_Operator: None
        Group_Type: int
        Use_E4: bool
        Acceleration_Type: int
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        Input_5: None
        ...
    class Input_mParticles(ReferenceTarget):
        Data_Type: int
        Match_Type: int
        Threshold_Type: int
        Collision_Type: int
        filter: None
        ...
    class InsertWarpAtOrgTime(BipedGeneric):
        ...
    class InstanceDuplMap(UtilityPlugin):
        ...
    class InstanceMgr(Interface):
        ...
    class InstanceMgrWrapper(floatController):
        ...
    class Instance_Duplicate_Maps(UtilityPlugin):
        ...
    class Instance_Manager_Wrapper(floatController):
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
        BrepOperation: int
        MakeIntoSolid: bool
        ToBrepObjectHelp: bool
        ...
    class Joint_Angle_Deformer(ReferenceTarget):
        ...
    class Joystick_Input_Device(ReferenceTarget):
        ...
    class Joystick_Input_DeviceMotionCaptureDeviceBindingClass(MotionCaptureDeviceBindingClass):
        ...
    class Joystick_Input_DeviceMotionCaptureDeviceClass(MotionCaptureDeviceClass):
        ...
    class Keep_Apart(helper):
        Force: float
        Use_Accel_Limit: bool
        Accel_Limit: float
        Use_Speed_Limit: bool
        Speed_Limit: float
        Range_Type: int
        Core_Size: float
        Falloff_Size: float
        Core_Percentage: float
        Falloff_Percentage: float
        variation: float
        Scope_Type: int
        Selected_Events: MXSWrapperBase
        Selected_Systems: MXSWrapperBase
        Random_Seed: int
        Use_Script_Float: int
        Use_Script_Vector: int
        ...
    class KeyValueUtility(trackViewUtility):
        ...
    class Keyboard_Input_Device(MotionCaptureDeviceClass):
        ...
    class Keyboard_Input_DeviceMotionCaptureDeviceBindingClass(MotionCaptureDeviceBindingClass):
        ...
    class KindOfRenderElement(MAXScriptFunction):
        ...
    class KneeAngle(floatController):
        ...
    class LOD(helper):
        ...
    class LOD_Controller(floatController):
        ...
    class LTypeStair(GeometryClass):
        StepType: int
        GenerateStringers: bool
        GenerateCarriage: bool
        GenerateInsideRailing: bool
        GenerateOutsideRailing: bool
        Stepwidth: float
        StepThickness: float
        GenerateMapping: bool
        StepDepth_X: bool
        StepDepth: float
        StepHeight: float
        StepCount: int
        StringerDepth: float
        StringerWidth: float
        StringerOffset: float
        StringerSpringFloor: bool
        CarriageWidth: float
        CarriageIntOffs: float
        CarriageExtOffs: float
        CarriageSpace: float
        CarriageCount: int
        CarriageContext: int
        CarriageSpacingType: int
        CarriageHeight: float
        CarriageSpringFloor: bool
        RailingHeight: float
        RailingOffs: float
        RailingSegments: int
        RailingRadius: float
        length: float
        length2: float
        angle: float
        UpperOffset: float
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
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInSideLength: float
        typeInFrontLength: float
        typeInSideWidth: float
        typeInFrontWidth: float
        typeInHeight: float
        Side_Length: float
        Front_Length: float
        Side_Width: float
        Front_Width: float
        height: float
        Side_Segments: int
        Front_Segments: int
        Width_Segments: int
        Height_Segments: int
        mapcoords: bool
        centerCreate: bool
        ...
    class L_Type_Stair(GeometryClass):
        StepType: int
        GenerateStringers: bool
        GenerateCarriage: bool
        GenerateInsideRailing: bool
        GenerateOutsideRailing: bool
        Stepwidth: float
        StepThickness: float
        GenerateMapping: bool
        StepDepth_X: bool
        StepDepth: float
        StepHeight: float
        StepCount: int
        StringerDepth: float
        StringerWidth: float
        StringerOffset: float
        StringerSpringFloor: bool
        CarriageWidth: float
        CarriageIntOffs: float
        CarriageExtOffs: float
        CarriageSpace: float
        CarriageCount: int
        CarriageContext: int
        CarriageSpacingType: int
        CarriageHeight: float
        CarriageSpringFloor: bool
        RailingHeight: float
        RailingOffs: float
        RailingSegments: int
        RailingRadius: float
        length: float
        length2: float
        angle: float
        UpperOffset: float
        ...
    class LabelControl(RolloutControl):
        ...
    class LandXMLImport(ImporterPlugin):
        ...
    class LandXML___DEM_Model_Import(ImporterPlugin):
        ...
    class Lathe(modifier):
        matIDs: bool
        smooth: bool
        capStart: bool
        capEnd: bool
        capType: int
        weldCore: bool
        flipNormals: bool
        segs: int
        mapcoords: bool
        output: int
        degrees: float
        useShapeIDs: bool
        ...
    class Lattice(modifier):
        Strut_Segments: int
        Strut_Sides: int
        Joint_Radius: float
        Joint_Segs: int
        Strut_Radius: float
        ...
    class LayerFloat(floatController):
        ...
    class LayerInfo(floatController):
        ...
    class LayerManager(Interface):
        ...
    class LayerMatrix3(Matrix3Controller):
        ...
    class LayerRoot(floatController):
        ...
    class LayerTransform(Matrix3Controller):
        ...
    class LayerWeights(floatController):
        ...
    class Layer_Manager(ReferenceTarget):
        ...
    class Layer_Output(floatController):
        ...
    class LegWeight(floatController):
        ...
    class Lens_Effects(renderEffect):
        seed: int
        size: float
        angle: float
        intensity: float
        Squeeze: float
        affectAlpha: bool
        affectZBuffer: bool
        distAffectsSize: bool
        distAffectsIntensity: bool
        centerAffectsSize: bool
        centerAffectsIntensity: bool
        innerOcclusionRadius: float
        occlusionAffectsSize: bool
        outerOcclusionRadius: float
        occlusionAffectsIntensity: bool
        affectByAtmosphere: bool
        lightDirectionAffectsSize: bool
        lightDirectionAffectsIntensity: bool
        ...
    class Lens_Effects_Flare_Filter(VideoPostFilter):
        ...
    class Lens_Effects_Focus_Filter(VideoPostFilter):
        ...
    class Lens_Effects_Glow_Filter(VideoPostFilter):
        ...
    class Lens_Effects_Hilight_Filter(VideoPostFilter):
        ...
    class Level_of_Detail(UtilityPlugin):
        ...
    class LightCreationZHeight(MAXScriptFunction):
        ...
    class LightMap(ReferenceTarget):
        lightmap_texture: None
        diffuse_texture: None
        diffuse_mapping: int
        lightmap_filename: str
        diffuse_filename: str
        lightmap_on: bool
        diffuse_on: bool
        lightmap_mapping: int
        ...
    class LightMeter(helper):
        ...
    class LightMeterManager(Interface):
        ...
    class LightTrace(RadiosityEffect):
        rays: int
        sky_lights: float
        bounces: int
        ray_Bias: float
        filter_size: float
        sky_lights_on: bool
        global_multiplier: float
        object_multiplier: float
        color_bleed: float
        color_filter: MXSWrapperBase
        extra_ambient: MXSWrapperBase
        Cone_Angle: float
        volumes_on: bool
        volumes: float
        adaptive_undersampling_on: bool
        initial_sample_spacing: int
        subdivide_down_to: int
        subdivision_contrast: float
        show_samples: bool
        ...
    class Light_RollAngle_Manipulator(helper):
        ...
    class Light_Tracer(RadiosityEffect):
        rays: int
        sky_lights: float
        bounces: int
        ray_Bias: float
        filter_size: float
        sky_lights_on: bool
        global_multiplier: float
        object_multiplier: float
        color_bleed: float
        color_filter: MXSWrapperBase
        extra_ambient: MXSWrapperBase
        Cone_Angle: float
        volumes_on: bool
        volumes: float
        adaptive_undersampling_on: bool
        initial_sample_spacing: int
        subdivide_down_to: int
        subdivision_contrast: float
        show_samples: bool
        ...
    class Lighting(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        shadowsOn: bool
        directOn: bool
        indirectOn: bool
        ...
    class LightingAnalysisOverlay(renderEffect):
        ...
    class LightingAnalysisOverlayFactory(Interface):
        ...
    class LightingMap(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        shadowsOn: bool
        directOn: bool
        indirectOn: bool
        targetMapSlotName: str
        ...
    class LightingRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        shadowsOn: bool
        directOn: bool
        indirectOn: bool
        ...
    class LightingUnits(Interface):
        ...
    class Lighting_Analysis_Data(RenderElement):
        ...
    class Lighting_Analysis_Overlay(renderEffect):
        ...
    class LightscapeExposureControl(ToneOperator):
        physicalScale: float
        chromaticAdaptation: bool
        colorDifferentiation: bool
        whiteColor: MXSWrapperBase
        active: bool
        processBG: bool
        brightness: float
        contrast: float
        Daylight: bool
        exterior: bool
        exteriorDaylight: bool
        midTones: float
        indirectOnly: bool
        useLegacyAlgorithm: bool
        ...
    class LimbData2(ReferenceTarget):
        ...
    class LinearShape(shape):
        ...
    class Linear_Exposure_Control(ToneOperator):
        physicalScale: float
        chromaticAdaptation: bool
        colorDifferentiation: bool
        whiteColor: MXSWrapperBase
        active: bool
        processBG: bool
        exposureValue: float
        contrast: float
        brightess: float
        ...
    class Lines(shape):
        ...
    class Link(Matrix3Controller):
        key_mode: int
        key_nodes_mode: int
        key_hierarchy_mode: int
        ...
    class LinkBlockInstance(GeometryClass):
        ...
    class LinkBlockInstanceshape(shape):
        ...
    class LinkComposite(GeometryClass):
        ...
    class LinkCompositeshape(shape):
        ...
    class LinkControl(RolloutControl):
        ...
    class LinkLeaf(GeometryClass):
        ...
    class LinkLeafshape(shape):
        ...
    class LinkOriginPtHelper(helper):
        ...
    class LinkTimeControl(floatController):
        ...
    class Link_Constraint(Matrix3Controller):
        key_mode: int
        key_nodes_mode: int
        key_hierarchy_mode: int
        ...
    class Link_Inheritance__Selected(UtilityPlugin):
        ...
    class Link_Transform(Matrix3Controller):
        ...
    class LinkedXForm(modifier):
        backTransform: bool
        ...
    class Linked_XForm(modifier):
        backTransform: bool
        ...
    class ListBoxControl(RolloutControl):
        ...
    class LnDif(Generic):
        ...
    class LoadDefaultMatLib(Primitive):
        ...
    class LoadSaveAnimation(Interface):
        ...
    class Local_Euler_XYZ(rotationController):
        axisOrder: int
        ...
    class LockAxisTripods(Primitive):
        ...
    class Lock_Bond(helper):
        Lock_Type: int
        Animated_Surface: bool
        Snap_To_Surface: bool
        Restrict_Position_To_Surface: bool
        Use_Position_Offset_Limit: bool
        Position_Offset_Limit: float
        Use_Speed_Limit: bool
        Speed_Limit: float
        Position_Force: float
        Position_Dampening_Type: int
        Dampening_Friction: float
        Dampening_Resistance: float
        Speed_Unit: float
        Use_No_Acceleration_Zone: bool
        Use_No_Dampening_Zone: bool
        Zone_Radius: float
        Use_Break_Off_Test: bool
        Break_Off_Type: int
        Break_Off_Speed: float
        Break_Off_Acceleration: float
        Break_If_Outwards_Only: bool
        Use_Rotation_Offset_Limit: bool
        Rotation_Offset_Limit: float
        Use_Spin_Limit: bool
        Spin_Limit: float
        Rotation_Force: float
        Rotation_Dampening: float
        Sync_Type: int
        Induced_By_Speed_Change: bool
        Inertial_Size: float
        Break_Off_Variation: float
        Random_Seed: int
        Lock_On_Objects: MXSWrapperBase
        ...
    class LockedComponentsMan(Interface):
        ...
    class LockedMapWrapper(textureMap):
        ...
    class LockedMaterialWrapper(material):
        ...
    class LockedModifierWrapper(modifier):
        ...
    class LockedObjectWrapper(helper):
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
        physicalScale: float
        chromaticAdaptation: bool
        colorDifferentiation: bool
        whiteColor: MXSWrapperBase
        active: bool
        processBG: bool
        brightness: float
        contrast: float
        Daylight: bool
        exterior: bool
        exteriorDaylight: bool
        midTones: float
        indirectOnly: bool
        useLegacyAlgorithm: bool
        ...
    class LookAt_Constraint(rotationController):
        weight: MXSWrapperBase
        relative: bool
        lookat_vector_length: float
        set_orientation: bool
        target_axis: int
        target_axisFlip: bool
        upnode_axis: int
        upnode_world: bool
        pickUpNode: None
        StoUP_axis: int
        StoUP_axisFlip: bool
        viewline_length_abs: bool
        upnode_ctrl: int
        ...
    class Luminaire(helper):
        dimmer: float
        FilterColor: MXSWrapperBase
        ...
    class LuminaireHelper(helper):
        dimmer: float
        FilterColor: MXSWrapperBase
        ...
    class LuminanceRenderElement(RenderElement):
        enabledOn: bool
        filterOn: bool
        atmosphereOn: bool
        shadowOn: bool
        elementName: str
        bitmap: None
        ScaleFactor: float
        ...
    class Luminance_HDR_Data(RenderElement):
        enabledOn: bool
        filterOn: bool
        atmosphereOn: bool
        shadowOn: bool
        elementName: str
        bitmap: None
        ScaleFactor: float
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
        prepass_enabled: bool
        prepass_samples: int
        AA_samples: int
        GI_diffuse_samples: int
        GI_diffuse_depth: int
        GI_specular_samples: int
        GI_specular_depth: int
        GI_transmission_samples: int
        GI_transmission_depth: int
        GI_sss_samples: int
        GI_volume_samples: int
        GI_volume_depth: int
        enable_adaptive_sampling: bool
        AA_samples_max: int
        Adaptive_Threshold: float
        progressive_render: bool
        GI_total_depth: int
        auto_transparency_depth: int
        low_light_threshold: float
        lock_sampling_pattern: bool
        sss_use_autobump: bool
        indirect_specular_blur: float
        filter: int
        filter_width: float
        AA_sample_clamp_enabled: bool
        AA_sample_clamp_affects_aovs: bool
        AA_sample_clamp: float
        indirect_sample_clamp: float
        physical_material_sss_type: int
        dielectric_priorities: bool
        env_mode: int
        env_ibl_samples: int
        env_phys_bgnd_mode: int
        env_phys_bgnd_color: MXSWrapperBase
        env_phys_bgnd_map: None
        env_ibl_enable: bool
        env_adv_ibl_multiplier: float
        env_adv_ibl_volume_samples: int
        env_adv_ibl_portal_mode: int
        env_adv_ibl_max_bounces: int
        env_adv_ibl_resolution_enable: bool
        env_adv_ibl_resolution: int
        env_adv_ibl_emit_camera: bool
        env_adv_ibl_emit_diffuse: bool
        env_adv_ibl_emit_specular: bool
        env_adv_ibl_emit_transmission: bool
        env_adv_ibl_affect_sss: bool
        env_adv_ibl_affect_indirect: bool
        env_adv_ibl_affect_volume: bool
        env_adv_ibl_camera_mult: float
        env_adv_ibl_diffuse_mult: float
        env_adv_ibl_specular_mult: float
        env_adv_ibl_transmission_mult: float
        env_adv_ibl_sss_mult: float
        env_adv_ibl_indirect_mult: float
        env_adv_ibl_volume_mult: float
        env_adv_ibl_cast_shadows: bool
        env_adv_ibl_shadow_color: MXSWrapperBase
        env_adv_ibl_shadow_density: float
        env_adv_bgnd_mode: int
        env_adv_bgnd_visible_to_camera: bool
        env_adv_bgnd_visible_to_diffuse_reflections: bool
        env_adv_bgnd_visible_to_specular_reflections: bool
        env_adv_bgnd_visible_to_diffuse_transmission: bool
        env_adv_bgnd_visible_to_specular_transmission: bool
        env_adv_bgnd_visible_to_volume_scattering: bool
        env_adv_bgnd_custom_color: MXSWrapperBase
        env_adv_bgnd_custom_map: None
        env_adv_bgnd_custom_shader: None
        Atmosphere: None
        respect_physical_camera_motion_blur: bool
        enable_transform_keys: bool
        transform_keys: int
        enable_deform_keys: bool
        deform_keys: int
        shutter_length: float
        shutter_position: int
        auto_shutter: bool
        shutter_open: float
        shutter_close: float
        shutter_type: int
        ignore_motion_blur: bool
        max_subdivisions: int
        geometry_dicing_camera: None
        subdiv_frustum_culling: bool
        subdiv_frustum_padding: float
        displacement_default_subdiv_type: int
        displacement_default_subdiv_iterations: int
        displacement_default_subdiv_adaptive_error: float
        curves_default_basis: int
        curves_default_mode: int
        curves_default_min_pixel_width: float
        texture_automip: bool
        texture_accept_unmipped: bool
        texture_enable_autotile: bool
        texture_autotile: int
        texture_accept_untiled: bool
        use_existing_tx: bool
        texture_max_memory_MB: int
        texture_max_open_files: int
        gpu_max_texture_resolution: int
        bucket_scanning: int
        bucket_size: int
        show_bucket_corners_prod: bool
        show_bucket_corners_as: bool
        abort_on_license_fail: bool
        skip_license_check: bool
        legacy_3ds_max_map_support: bool
        autodetect_threads: bool
        threads: int
        gpu_selection: MXSWrapperBase
        gpu_rendering: bool
        render_device: int
        render_device_fallback: int
        default_gpu_names: str
        default_gpu_min_memory_MB: int
        gpu_auto_selection: bool
        use_optix_on_beauty: bool
        noice_input: str
        noice_output: str
        noice_anim_range: int
        noice_start_frame: int
        noice_end_frame: int
        noice_additional_frames: int
        noice_variance: float
        noice_search_radius: int
        noice_patch_radius: int
        noice_light_aov_names: str
        output_denoising_aovs: bool
        procedural_searchpath: None
        plugin_searchpath: None
        texture_searchpath: None
        verbosity_level: int
        log_to_console: bool
        log_to_file: bool
        log_file: None
        max_warnings: int
        texture_per_file_stats: bool
        log_render_stats: bool
        render_stats_file: None
        render_stats_mode: int
        log_render_profile: bool
        render_profile_file: None
        abort_on_error: bool
        abort_on_error_activeshade: bool
        error_color_bad_texture: MXSWrapperBase
        error_color_bad_shader: MXSWrapperBase
        error_color_bad_pixel: MXSWrapperBase
        ignore_textures: bool
        ignore_shaders: bool
        ignore_atmosphere: bool
        ignore_lights: bool
        ignore_shadows: bool
        ignore_subdivision: bool
        ignore_displacement: bool
        ignore_bump: bool
        ignore_smoothing: bool
        ignore_motion: bool
        ignore_dof: bool
        ignore_sss: bool
        ignore_operators: bool
        shader_override_enabled: bool
        shader_override: None
        enable_user_options: bool
        user_options: None
        export_to_ass: bool
        ass_file_path: None
        export_option: bool
        export_cameras: bool
        export_driversfilters: bool
        export_lights: bool
        export_geometry: bool
        export_shaders: bool
        export_operators: bool
        export_binary: bool
        expand_procedurals: bool
        export_to_mtlx: bool
        mtlx_file_path: None
        mtlx_look: str
        mtlx_properties: None
        mtlx_relative: bool
        mtlx_use_current_selection: bool
        operator_root: None
        operator_export_list: MXSWrapperBase
        operator_export_tree: bool
        material_export_list: MXSWrapperBase
        retranslate_all_frames: bool
        use_quads: int
        export_to_ass_origin: int
        use_render_view: bool
        render_view_settings: str
        imager_0: None
        AOV_Manager: None
        driver_type: None
        aov_shaders_mat_0: None
        aov_shaders_mat_1: None
        aov_shaders_mat_2: None
        aov_shaders_map_0: None
        aov_shaders_map_1: None
        aov_shaders_map_2: None
        ...
    class MAXtoA_Menu(GlobalUtilityPlugin):
        ...
    class MAXtoA_OperatorCustomAttribute(CustAttrib):
        ...
    class MCG_Donut(shape):
        radius1: float
        radius2: float
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class MCG_MeshEdgesToSpline(shape):
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class MCG_SinWave(shape):
        segments: int
        Domain: float
        range: float
        offset: float
        Amplitude: float
        closed: bool
        Smoothing_Factor: float
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class MCG_lookAt(rotationController):
        Billboard: bool
        targetAxisFlip: bool
        Targets_Tab: MXSWrapperBase
        Weights_Tab: MXSWrapperBase
        targetAxis: int
        upnodeAxis: int
        srcUpnodeAxisFlip: bool
        upnodeControl: int
        upnodeAlignAxis: int
        upnodeWorld: bool
        upnode: None
        rotYOffset: float
        rotXOffset: float
        rotZOffset: float
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class MCG_rayToSurfaceOrientation(rotationController):
        Surfaces_Tab: MXSWrapperBase
        Ray_to_Surface_Pivot: bool
        Ray_Origin: None
        flip: bool
        Ray_Axis: int
        LclUpAxis: int
        Use_Surface_Normal: bool
        LclFwdAxis: int
        Use_Forward_Object: bool
        Forward_Object: None
        World_Axis: int
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class MCG_rayToSurfacePosition(positionController):
        Surfaces_Tab: MXSWrapperBase
        Ray_to_Surface_Pivot: bool
        Ray_Origin: None
        flip: bool
        Ray_Axis: int
        Use_Surface_Normal: bool
        offset: float
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class MCG_rayToSurfaceTransform(Matrix3Controller):
        Surfaces_Tab: MXSWrapperBase
        Ray_to_Surface_Pivot: bool
        Ray_Origin: None
        flip: bool
        Ray_Axis: int
        LclUpAxis: int
        Use_Surface_Normal: bool
        LclFwdAxis: int
        Use_Forward_Object: bool
        Forward_Object: None
        World_Axis: int
        offset: float
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        ...
    class MCG_rotationalSpring1DOFTransform(Matrix3Controller):
        Parent_Object: None
        Geometry_Hull: None
        mass: float
        Axis_XYZ: int
        lowerlimit: float
        upperlimit: float
        limitIsReversed: bool
        Damping: float
        Bounce: float
        Stiffness: float
        gravity: float
        deactivate_spring: bool
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        StepsPerFrame: float
        ...
    class MCG_rotationalSpring3DOFTransform(Matrix3Controller):
        Parent_Object: None
        Geometry_Hull: None
        mass: float
        useAxisLimits: bool
        lowerLimitX: float
        lowerLimitY: float
        lowerLimitZ: float
        upperLimitX: float
        upperLimitY: float
        upperLimitZ: float
        Damping: float
        Bounce: float
        Stiffness: float
        gravity: float
        deactivate_spring: bool
        _dummy: bool
        pluginGraph: str
        pluginGraphDependencies: MXSWrapperBase
        StepsPerFrame: float
        ...
    class MEditBkgnd(textureMap):
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
    class MSEmulator(textureMap):
        ...
    class MSPluginClass(Value):
        ...
    class MSec_Element(ReferenceTarget):
        elementName: str
        size: float
        intensity: float
        Plane: float
        sides: int
        on: bool
        Squeeze: bool
        occlusion: float
        presets: int
        colorSource: float
        radialColor1: MXSWrapperBase
        radialColor2: MXSWrapperBase
        radialColor3: MXSWrapperBase
        radialColor4: MXSWrapperBase
        colorRadius1: float
        colorRadius2: float
        colorRadius3: float
        colorRadius4: float
        radialMtl: None
        useRadialMtl: bool
        radialMap: None
        useRadialMap: bool
        circularColorMix: float
        quadrant1Color: MXSWrapperBase
        quadrant2Color: MXSWrapperBase
        quadrant3Color: MXSWrapperBase
        quadrant4Color: MXSWrapperBase
        circularMtl: None
        useCircularMtl: bool
        circularMap: None
        useCircularMap: bool
        radialSizeMap: None
        useRadialSizeMap: bool
        applyLights: bool
        applyImage: bool
        applyImageCenters: bool
        sourceObjectID: bool
        objectID: int
        sourceEffectsID: bool
        effectsID: int
        sourceUnclampedColor: bool
        unclampedColor: float
        unclampedColorInvert: bool
        sourceSurfaceNormal: bool
        surfaceNormal: float
        surfaceNormalInvert: bool
        sourceWhole: bool
        sourceAlpha: bool
        alpha: int
        sourceZBuffer: bool
        zHi: float
        zLo: float
        filterAll: bool
        filterEdge: bool
        filterPerimeterAlpha: bool
        filterPerimeter: bool
        filterBrightness: bool
        brightness: int
        brightnessInvert: bool
        filterHue: bool
        hue: MXSWrapperBase
        hueRange: int
        applyNoise: bool
        noiseMap: None
        radialDensity: None
        useRadialDensity: bool
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
        elementName: str
        size: float
        intensity: float
        Plane: float
        sides: int
        on: bool
        Squeeze: bool
        occlusion: float
        presets: int
        colorSource: float
        radialColor1: MXSWrapperBase
        radialColor2: MXSWrapperBase
        radialColor3: MXSWrapperBase
        radialColor4: MXSWrapperBase
        colorRadius1: float
        colorRadius2: float
        colorRadius3: float
        colorRadius4: float
        radialMtl: None
        useRadialMtl: bool
        radialMap: None
        useRadialMap: bool
        circularColorMix: float
        quadrant1Color: MXSWrapperBase
        quadrant2Color: MXSWrapperBase
        quadrant3Color: MXSWrapperBase
        quadrant4Color: MXSWrapperBase
        circularMtl: None
        useCircularMtl: bool
        circularMap: None
        useCircularMap: bool
        radialSizeMap: None
        useRadialSizeMap: bool
        applyLights: bool
        applyImage: bool
        applyImageCenters: bool
        sourceObjectID: bool
        objectID: int
        sourceEffectsID: bool
        effectsID: int
        sourceUnclampedColor: bool
        unclampedColor: float
        unclampedColorInvert: bool
        sourceSurfaceNormal: bool
        surfaceNormal: float
        surfaceNormalInvert: bool
        sourceWhole: bool
        sourceAlpha: bool
        alpha: int
        sourceZBuffer: bool
        zHi: float
        zLo: float
        filterAll: bool
        filterEdge: bool
        filterPerimeterAlpha: bool
        filterPerimeter: bool
        filterBrightness: bool
        brightness: int
        brightnessInvert: bool
        filterHue: bool
        hue: MXSWrapperBase
        hueRange: int
        applyNoise: bool
        noiseMap: None
        radialDensity: None
        useRadialDensity: bool
        ...
    class MapButtonControl(Value):
        ...
    class MapChannelAdd(modifier):
        ...
    class MapChannelDelete(modifier):
        mapID: int
        ...
    class MapChannelPaste(modifier):
        ...
    class MapMtlClipboard(GlobalUtilityPlugin):
        ...
    class MapOverride_BTT_Only(BakeElement):
        ...
    class MapScaler(SpacewarpModifier):
        scale: float
        uOffset: float
        vOffset: float
        wrap: bool
        channel: int
        upDirection: int
        wrapUsingSmoothingGroups: bool
        ...
    class MapScalerModifier(modifier):
        scale: float
        uOffset: float
        vOffset: float
        wrap: bool
        channel: int
        wrapUsingSmoothingGroups: bool
        ...
    class MapScalerOSM(modifier):
        scale: float
        uOffset: float
        vOffset: float
        wrap: bool
        channel: int
        wrapUsingSmoothingGroups: bool
        ...
    class MapScalerSpaceWarp(SpacewarpObject):
        ...
    class MapScalerSpacewarpModifier(SpacewarpModifier):
        scale: float
        uOffset: float
        vOffset: float
        wrap: bool
        channel: int
        upDirection: int
        wrapUsingSmoothingGroups: bool
        ...
    class MapSupportClass(Value):
        ...
    class Map_to_Material_Conversion(material):
        Shader: None
        shader_on: bool
        ...
    class MappedGeneric(Value):
        ...
    class MappedPrimitive(Value):
        ...
    class MappingObject(helper):
        Mapping_Type: int
        Acquire_SubMaterial_Index: bool
        Uniform_Color_Per_Particle: bool
        Mapping_From_Objects: MXSWrapperBase
        Static_Objects: bool
        Animated_Surface: bool
        Acquire_From_Mapping_Channels: MXSWrapperBase
        Use_Vertex_Color: bool
        U_Variation: float
        V_Variation: float
        W_Variation: float
        Exclude_Tiling: bool
        Blend_Mapping_By_Time: bool
        Blend_Type: int
        Blend_Time: int
        Blend_Mapping_By_Distance: bool
        Finish_Distance: float
        Show_Map_In_Viewport: bool
        Random_Seed: int
        ...
    class Mapping_Object(helper):
        Mapping_Type: int
        Acquire_SubMaterial_Index: bool
        Uniform_Color_Per_Particle: bool
        Mapping_From_Objects: MXSWrapperBase
        Static_Objects: bool
        Animated_Surface: bool
        Acquire_From_Mapping_Channels: MXSWrapperBase
        Use_Vertex_Color: bool
        U_Variation: float
        V_Variation: float
        W_Variation: float
        Exclude_Tiling: bool
        Blend_Mapping_By_Time: bool
        Blend_Type: int
        Blend_Time: int
        Blend_Mapping_By_Distance: bool
        Finish_Distance: float
        Show_Map_In_Viewport: bool
        Random_Seed: int
        ...
    class Marble(textureMap):
        map1: None
        map2: None
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1Enabled: bool
        map2Enabled: bool
        size: float
        width: float
        coords: MXSWrapperBase
        ...
    class Mask(textureMap):
        map: None
        Mask: None
        mapEnabled: bool
        maskEnabled: bool
        maskInverted: bool
        ...
    class MassFX_Loader_Linkage(GlobalUtilityPlugin):
        ...
    class MassFX_RBody(modifier):
        type: int
        switchType: bool
        switchTypeAtFrame: int
        enableGravity: bool
        continuousCollisionDetection: bool
        sleepAtStart: bool
        CollideWithRigidBodies: bool
        extraShapes: None
        manualSetup: bool
        materialID: int
        density: float
        volume: float
        mass: float
        staticFriction: float
        dynamicFriction: float
        bounciness: float
        EnableAdvancedSettings: int
        contactShellOverrideGlobals: bool
        contactShellContactDistance: float
        contactShellRestDepth: float
        SolverIter: bool
        SolverIterValue: int
        InitialMotionStyle: int
        InitialVelocityX: float
        InitialVelocityY: float
        InitialVelocityZ: float
        VelocitySpeed: float
        InitialSpinX: float
        InitialSpinY: float
        InitialSpinZ: float
        SpinSpeed: float
        massCenterX: float
        massCenterY: float
        massCenterZ: float
        linearDamping: float
        AngularDamping: float
        baked: int
        meshType: int
        meshCustomMesh: None
        meshVerticesLimit: int
        meshInflation: float
        meshConvexStyle: int
        meshRadius: float
        meshLength: float
        meshWidth: float
        meshHeight: float
        meshOverrideMaterial: bool
        compositeMaxVertices: int
        compositeMaxConcavity: float
        smallClusterThreshold: float
        enableSolidMeshes: bool
        compositeHighQuality: bool
        massCenterMode: int
        EnableBackfaceCollision: bool
        ForcesList: MXSWrapperBase
        showPhysicalMesh: bool
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
    class Master_Controller_plugin_not_found(MasterBlockController):
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
    class MaterialByElement(modifier):
        Random_Seed: int
        method: int
        Material_ID__1: float
        Material_ID__2: float
        Material_ID__3: float
        Material_ID__4: float
        Material_ID__5: float
        Material_ID__6: float
        Material_ID__7: float
        Material_ID__8: float
        Material_ID_count: int
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
    class Material_Dynamic(helper):
        Assign_Material: bool
        Assigned_Material: None
        Assign_Material_ID: bool
        Show_In_Viewport: bool
        SubMtl_ID_Offset: int
        type: int
        Reset_Particle_Age: bool
        Randomize_Age: bool
        Max_Age_Offset: MXSWrapperBase
        Material_ID: int
        Number_of_Sub_Materials: int
        Sub_Materials_Rate: float
        loop: bool
        Sync_Type: int
        Add_Random_Offset: bool
        Random_Offset: int
        Random_Seed: int
        ...
    class Material_Editor(Value):
        ...
    class Material_EditorReferenceMaker(ReferenceMaker):
        ...
    class Material_Frequency(helper):
        Assign_Material: bool
        Assigned_Material: None
        Assign_Material_ID: bool
        Show_In_Viewport: bool
        SubMtl_ID_Offset: int
        Mtl_ID_1: float
        Mtl_ID_2: float
        Mtl_ID_3: float
        Mtl_ID_4: float
        Mtl_ID_5: float
        Mtl_ID_6: float
        Mtl_ID_7: float
        Mtl_ID_8: float
        Mtl_ID_9: float
        Mtl_ID_10: float
        Random_Seed: int
        ...
    class Material_ID(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class Material_Static(helper):
        Assign_Material: bool
        Assigned_Material: None
        Assign_Material_ID: bool
        Show_In_Viewport: bool
        SubMtl_ID_Offset: int
        type: int
        Material_ID: int
        Number_of_Sub_Materials: int
        Rate_Type: int
        Rate_Per_Second: float
        Rate_Per_Particle: float
        loop: bool
        Random_Seed: int
        ...
    class Materialmodifier(modifier):
        materialID: int
        ...
    class Matrix3(Value):
        ...
    class Matrix3Controller(MAXWrapper):
        ...
    class Matrix3_Mixer_Controller(Matrix3Controller):
        ...
    class MatrixFromNormal(Primitive):
        ...
    class Matte(material):
        opaqueAlpha: bool
        applyAtmosphere: bool
        atmosphereDepth: int
        receiveshadows: bool
        affectAlpha: bool
        shadowBrightness: float
        color: MXSWrapperBase
        amount: float
        map: None
        useReflMap: bool
        additiveReflection: int
        ...
    class MatteRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        mtlIDOn: bool
        gbufIDOn: bool
        gbufID: int
        mtlID: int
        includeOn: bool
        ...
    class MatteShadow(material):
        opaqueAlpha: bool
        applyAtmosphere: bool
        atmosphereDepth: int
        receiveshadows: bool
        affectAlpha: bool
        shadowBrightness: float
        color: MXSWrapperBase
        amount: float
        map: None
        useReflMap: bool
        additiveReflection: int
        ...
    class MaxFluidSolverClass(MAXWrapper):
        ...
    class MaxLiquid(GeometryClass):
        iconSize: float
        solvers: MXSWrapperBase
        emitterType: int
        emitterLength: float
        emitterwidth: float
        emitterheight: float
        emitter_Meshes: MXSWrapperBase
        collider_Meshes: MXSWrapperBase
        foammask_Meshes: MXSWrapperBase
        guide_Meshes: MXSWrapperBase
        field_Meshes: MXSWrapperBase
        killplanes: MXSWrapperBase
        accelerator_Meshes: MXSWrapperBase
        killVolumeNode: None
        scratchCache: str
        maxScratchCacheRAM: float
        useProjectFolders: bool
        rootSimDirectory: str
        cacheOutputFilePattern: str
        exportPRTFiles: bool
        lastSelectedSolverIndex: int
        renderSolveIndex: int
        renderSolveLock: bool
        showVoxelGrid: bool
        guideEmitter_Meshes: MXSWrapperBase
        showIcon: bool
        displayCacheLimitEnable: bool
        displayCacheLimit: float
        enableGPUPoints: bool
        channelField_Meshes: MXSWrapperBase
        ...
    class MaxLiquidSolver(MaxFluidSolverClass):
        ...
    class MaxMotionClipImp(MasterBlockController):
        globalclipassociations: MXSWrapperBase
        clipassociations: MXSWrapperBase
        ...
    class MaxMotionClipMaster(CtrlUserDataTypeClass):
        ...
    class MaxMotionField(SpacewarpObject):
        magnitudeUI: float
        magnitude: float
        evaluationType: int
        Enable: bool
        enableTurbulence: bool
        enableVelocitySpeed: bool
        enableGeometry: bool
        enableBoundary: bool
        enableDirection: bool
        enableDrag: bool
        velocityGrid: bool
        velocityGridResolution: int
        velocityDrawScale: float
        boundaryShape: int
        width: float
        length: float
        fieldMaxDepth: float
        sectionRadius: float
        height: float
        enableMaxDepth: bool
        boundaryFalloff: float
        radius: float
        invertFalloff: bool
        directionMagnitude: float
        enableConcentric: bool
        concentricMagnitude: float
        enableAlongAxis: bool
        alongAxisMagnitude: float
        enableAroundAxis: bool
        aroundAxisMagnitude: float
        enableAwayFromAxis: bool
        awayFromAxisMagnitude: float
        Drag: float
        normalDrag: float
        turbulenceMagnitude: float
        turbulenceFrequency: float
        turbulenceSpeed: float
        turbulenceScaleX: float
        turbulenceScaleY: float
        turbulenceScaleZ: float
        turbulenceOffsetX: float
        turbulenceOffsetY: float
        turbulenceOffsetZ: float
        turbulenceType: int
        worldspaceTurbulence: bool
        enableNoise: bool
        noiseMagnitude: float
        turbulenceTime: float
        turbulenceScale: MXSWrapperBase
        turbulenceOffset: MXSWrapperBase
        enableGeometryFalloff: bool
        geometryMinDistance: float
        geometryMaxDistance: float
        geometryAlongNormal: float
        geometryFriction: float
        inheritVelocity: float
        motionFields_Meshes: None
        motionFields_proxyObjectName: str
        motionFields_voxelScale: float
        motionFields_enableBoundary: bool
        motionFields_boundaryShape: int
        motionFields_transform: MXSWrapperBase
        motionFields_invert: bool
        enableVelocityScale: bool
        velocityScaleX: float
        velocityScaleY: float
        velocityScaleZ: float
        clampSpeed: bool
        minspeed: float
        maxspeed: float
        VelocityScale: MXSWrapperBase
        direction: MXSWrapperBase
        directionZ: float
        directionY: float
        directionX: float
        transform: MXSWrapperBase
        scaleAffectsSpeed: bool
        drawTimeSpan: int
        iconSize: float
        drawVelocityArrows: bool
        drawAdditiveVelocity: bool
        colorOptions: int
        startColor: MXSWrapperBase
        endColor: MXSWrapperBase
        sampleOptions: int
        tempSpeedFix: int
        enableDisplay: bool
        enableDirectionRollup: bool
        enableVelocityRollup: bool
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
        Enable: bool
        Quality: float
        Sub_sample_Textures: bool
        ...
    class Max_Master_Clip(ReferenceTarget):
        ...
    class Max_Mixer_Clip(CtrlUserDataTypeClass):
        ...
    class Max_MotionClip_Implementation(MasterBlockController):
        globalclipassociations: MXSWrapperBase
        clipassociations: MXSWrapperBase
        ...
    class MaxscriptParticleContainer(ReferenceTarget):
        ...
    class Mb_select(GlobalUtilityPlugin):
        ...
    class Measure(UtilityPlugin):
        ...
    class Melt(modifier):
        axis: int
        spread: float
        Melt_Amount: float
        Confine_To_Gizmo: int
        Cut_Off__obsolete: float
        Solidity_Preset: int
        Solidity_Custom_Value: float
        Negative_Axis: int
        ...
    class MemoryTargetToOGSTargetFragment(GraphicsFragmentPlugin):
        ...
    class MeshCollision(ReferenceMaker):
        ...
    class MeshDeformPW(modifier):
        mesh: None
        threshold: float
        engine: int
        falloff: float
        distance: float
        faceLimit: int
        showLoops: bool
        showAxis: bool
        showFaceLimit: bool
        showMirrorData: bool
        mirrorPlane: int
        mirrorOffset: float
        meshList: MXSWrapperBase
        showUnassignedVerts: bool
        showVerts: bool
        weightAllVerts: bool
        mirrorThreshold: float
        Blend: bool
        blendDistance: float
        ...
    class MeshINI(Interface):
        ...
    class MeshInspector(Interface):
        ...
    class MeshProjIntersect(ReferenceTarget):
        ...
    class MeshSelect(modifier):
        useSoftSelection: bool
        softselUseEdgeDistance: bool
        softselEdgeDist: int
        softselAffectBackfacing: bool
        softselFalloff: float
        softselPinch: float
        softselBubble: float
        byVertex: bool
        ignoreBackfacing: bool
        materialID: int
        ignoreVisibleEdges: bool
        planarThreshold: float
        ...
    class Mesh_Select(modifier):
        useSoftSelection: bool
        softselUseEdgeDistance: bool
        softselEdgeDist: int
        softselAffectBackfacing: bool
        softselFalloff: float
        softselPinch: float
        softselBubble: float
        byVertex: bool
        ignoreBackfacing: bool
        materialID: int
        ignoreVisibleEdges: bool
        planarThreshold: float
        ...
    class Mesher(GeometryClass):
        pick: None
        renderTimeOnly: bool
        time: float
        radius: float
        useCustomBounds: bool
        boundsMin: MXSWrapperBase
        boundsMax: MXSWrapperBase
        useAllPFEvents: bool
        pfEventList: MXSWrapperBase
        ...
    class MetaSLProxyMaterial(material):
        Shader: None
        shader_on: bool
        ...
    class Metal2(Shader):
        ...
    class MetalShader(Shader):
        ...
    class Metal_Bump(ReferenceTarget):
        Diffuse: None
        normal: None
        DETAIL: None
        Mask: None
        Reflection: None
        BUMP: None
        diffuse_on: bool
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
        Sync: bool
        SPIN_REFLECTSCALE: int
        ALPHA_ON: bool
        ...
    class Metal_Bump9(ReferenceTarget):
        Diffuse: None
        normal: None
        DETAIL: None
        Mask: None
        Reflection: None
        BUMP: None
        diffuse_on: bool
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
        Sync: bool
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
    class Missing_Atmospheric(atmospheric):
        ...
    class Missing_Camera(camera):
        ...
    class Missing_Custom_Attribute_Plugin(CustAttrib):
        ...
    class Missing_DataChannelEngine(IDataChannelEngineClass):
        ...
    class Missing_Exposure_Control(ToneOperator):
        ...
    class Missing_Float_Control(floatController):
        ...
    class Missing_GeomObject(GeometryClass):
        ...
    class Missing_Helper(helper):
        ...
    class Missing_Light(light):
        ...
    class Missing_Matrix3_Control(Matrix3Controller):
        ...
    class Missing_MaxFluid_Solver(MaxFluidSolverClass):
        ...
    class Missing_Morph_Control(MorphController):
        ...
    class Missing_MotCapDev(MotionCaptureDeviceBindingClass):
        ...
    class Missing_Mtl(material):
        ...
    class Missing_OSM(modifier):
        ...
    class Missing_Point3_Control(point3Controller):
        ...
    class Missing_Point4_Control(point4Controller):
        ...
    class Missing_Position_Control(positionController):
        ...
    class Missing_Radiosity(RadiosityEffect):
        ...
    class Missing_RefMaker(ReferenceMaker):
        ...
    class Missing_RefTarget(ReferenceTarget):
        ...
    class Missing_Render_Effect(renderEffect):
        ...
    class Missing_Render_Element_Plug_in(RenderElement):
        ...
    class Missing_Renderer(RendererClass):
        ...
    class Missing_Rotation_Control(rotationController):
        ...
    class Missing_Sampler(SamplerClass):
        ...
    class Missing_Scale_Control(scaleController):
        ...
    class Missing_Shader_Plug_in(Shader):
        ...
    class Missing_Shadow_Type(Shadow):
        ...
    class Missing_Shape(shape):
        ...
    class Missing_SoundObj(SoundClass):
        ...
    class Missing_System(System):
        ...
    class Missing_TextureMap(textureMap):
        ...
    class Missing_Texture_Bake_Element(BakeElement):
        ...
    class Missing_Texture_Output_Plug_in(TexOutputClass):
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
    class Mitchell_Netravali(filter):
        blur: float
        Ringing: float
        ...
    class Mix(textureMap):
        mixAmount: float
        lower: float
        upper: float
        useCurve: bool
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1: None
        map2: None
        Mask: None
        map1Enabled: bool
        map2Enabled: bool
        maskEnabled: bool
        output: MXSWrapperBase
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
    class MocapLayer(floatController):
        ...
    class MocapLayerInfo(floatController):
        ...
    class ModRBClass(modifier):
        type: int
        switchType: bool
        switchTypeAtFrame: int
        enableGravity: bool
        continuousCollisionDetection: bool
        sleepAtStart: bool
        CollideWithRigidBodies: bool
        extraShapes: None
        manualSetup: bool
        materialID: int
        density: float
        volume: float
        mass: float
        staticFriction: float
        dynamicFriction: float
        bounciness: float
        EnableAdvancedSettings: int
        contactShellOverrideGlobals: bool
        contactShellContactDistance: float
        contactShellRestDepth: float
        SolverIter: bool
        SolverIterValue: int
        InitialMotionStyle: int
        InitialVelocityX: float
        InitialVelocityY: float
        InitialVelocityZ: float
        VelocitySpeed: float
        InitialSpinX: float
        InitialSpinY: float
        InitialSpinZ: float
        SpinSpeed: float
        massCenterX: float
        massCenterY: float
        massCenterZ: float
        linearDamping: float
        AngularDamping: float
        baked: int
        meshType: int
        meshCustomMesh: None
        meshVerticesLimit: int
        meshInflation: float
        meshConvexStyle: int
        meshRadius: float
        meshLength: float
        meshWidth: float
        meshHeight: float
        meshOverrideMaterial: bool
        compositeMaxVertices: int
        compositeMaxConcavity: float
        smallClusterThreshold: float
        enableSolidMeshes: bool
        compositeHighQuality: bool
        massCenterMode: int
        EnableBackfaceCollision: bool
        ForcesList: MXSWrapperBase
        showPhysicalMesh: bool
        ...
    class ModifierClass(Value):
        ...
    class MonoGraph(floatController):
        ...
    class Morph(GeometryClass):
        ...
    class MorphByBone(modifier):
        Bones: MXSWrapperBase
        morphName: None
        influenceAngle: float
        falloff: int
        showMirrorPlane: bool
        mirrorPlane: int
        mirrorOffset: float
        mirrorThreshold: float
        previewVerts: bool
        previewBone: bool
        jointType: int
        targetNodes: MXSWrapperBase
        falloffGraphs: MXSWrapperBase
        reloadSelected: bool
        safemode: bool
        showDriverBone: bool
        showMorphBone: bool
        showCurrentAngle: bool
        showLimitAngle: bool
        matrixSize: float
        showDeltas: bool
        showX: bool
        showY: bool
        showZ: bool
        bonesize: float
        softSelectionGraph: MXSWrapperBase
        useSoftSelection: bool
        selectionRadius: float
        edgeLimit: int
        useEdgeLimit: bool
        enabled: bool
        showedges: bool
        ...
    class MorphController(MAXWrapper):
        ...
    class Morph_Angle_Deformer(ReferenceTarget):
        ...
    class Morpher(modifier):
        Use_Limits: int
        Spinner_Minimum: float
        Spinner_Maximum: float
        Value_Increments: int
        Autoload_of_targets: int
        Use_Selection: int
        ...
    class MorpherMaterial(material):
        Mat_1: None
        Mat_2: None
        Mat_3: None
        Mat_4: None
        Mat_5: None
        Mat_6: None
        Mat_7: None
        Mat_8: None
        Mat_9: None
        Mat_10: None
        Mat_11: None
        Mat_12: None
        Mat_13: None
        Mat_14: None
        Mat_15: None
        Mat_16: None
        Mat_17: None
        Mat_18: None
        Mat_19: None
        Mat_20: None
        Mat_21: None
        Mat_22: None
        Mat_23: None
        Mat_24: None
        Mat_25: None
        Mat_26: None
        Mat_27: None
        Mat_28: None
        Mat_29: None
        Mat_30: None
        Mat_31: None
        Mat_32: None
        Mat_33: None
        Mat_34: None
        Mat_35: None
        Mat_36: None
        Mat_37: None
        Mat_38: None
        Mat_39: None
        Mat_40: None
        Mat_41: None
        Mat_42: None
        Mat_43: None
        Mat_44: None
        Mat_45: None
        Mat_46: None
        Mat_47: None
        Mat_48: None
        Mat_49: None
        Mat_50: None
        Mat_51: None
        Mat_52: None
        Mat_53: None
        Mat_54: None
        Mat_55: None
        Mat_56: None
        Mat_57: None
        Mat_58: None
        Mat_59: None
        Mat_60: None
        Mat_61: None
        Mat_62: None
        Mat_63: None
        Mat_64: None
        Mat_65: None
        Mat_66: None
        Mat_67: None
        Mat_68: None
        Mat_69: None
        Mat_70: None
        Mat_71: None
        Mat_72: None
        Mat_73: None
        Mat_74: None
        Mat_75: None
        Mat_76: None
        Mat_77: None
        Mat_78: None
        Mat_79: None
        Mat_80: None
        Mat_81: None
        Mat_82: None
        Mat_83: None
        Mat_84: None
        Mat_85: None
        Mat_86: None
        Mat_87: None
        Mat_88: None
        Mat_89: None
        Mat_90: None
        Mat_91: None
        Mat_92: None
        Mat_93: None
        Mat_94: None
        Mat_95: None
        Mat_96: None
        Mat_97: None
        Mat_98: None
        Mat_99: None
        Mat_100: None
        base: MXSWrapperBase
        Channel_0: float
        Channel_1: float
        Channel_2: float
        Channel_3: float
        Channel_4: float
        Channel_5: float
        Channel_6: float
        Channel_7: float
        Channel_8: float
        Channel_9: float
        Channel_10: float
        Channel_11: float
        Channel_12: float
        Channel_13: float
        Channel_14: float
        Channel_15: float
        Channel_16: float
        Channel_17: float
        Channel_18: float
        Channel_19: float
        Channel_20: float
        Channel_21: float
        Channel_22: float
        Channel_23: float
        Channel_24: float
        Channel_25: float
        Channel_26: float
        Channel_27: float
        Channel_28: float
        Channel_29: float
        Channel_30: float
        Channel_31: float
        Channel_32: float
        Channel_33: float
        Channel_34: float
        Channel_35: float
        Channel_36: float
        Channel_37: float
        Channel_38: float
        Channel_39: float
        Channel_40: float
        Channel_41: float
        Channel_42: float
        Channel_43: float
        Channel_44: float
        Channel_45: float
        Channel_46: float
        Channel_47: float
        Channel_48: float
        Channel_49: float
        Channel_50: float
        Channel_51: float
        Channel_52: float
        Channel_53: float
        Channel_54: float
        Channel_55: float
        Channel_56: float
        Channel_57: float
        Channel_58: float
        Channel_59: float
        Channel_60: float
        Channel_61: float
        Channel_62: float
        Channel_63: float
        Channel_64: float
        Channel_65: float
        Channel_66: float
        Channel_67: float
        Channel_68: float
        Channel_69: float
        Channel_70: float
        Channel_71: float
        Channel_72: float
        Channel_73: float
        Channel_74: float
        Channel_75: float
        Channel_76: float
        Channel_77: float
        Channel_78: float
        Channel_79: float
        Channel_80: float
        Channel_81: float
        Channel_82: float
        Channel_83: float
        Channel_84: float
        Channel_85: float
        Channel_86: float
        Channel_87: float
        Channel_88: float
        Channel_89: float
        Channel_90: float
        Channel_91: float
        Channel_92: float
        Channel_93: float
        Channel_94: float
        Channel_95: float
        Channel_96: float
        Channel_97: float
        Channel_98: float
        Channel_99: float
        Channel_100: int
        ...
    class MotionCaptureDeviceBindingClass(MAXWrapper):
        ...
    class MotionCaptureDeviceClass(MAXWrapperNonRefTarg):
        ...
    class MotionRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        velocityMax: float
        velocityOn: bool
        ...
    class MotionTracker(Value):
        ...
    class Motion_Blur(renderEffect):
        duration: float
        transparency: bool
        ...
    class Motion_BlurMPassCamEffect(MPassCamEffect):
        displayPasses: bool
        totalPasses: int
        duration: float
        bias: float
        normalizeWeights: bool
        ditherStrength: float
        tileSize: int
        disableFiltering: bool
        disableAntialiasing: bool
        ...
    class Motion_Capture(UtilityPlugin):
        ...
    class Motion_Clip(floatController):
        ...
    class Motion_ClipFloatController(floatController):
        ...
    class Motion_Clip_SlaveFloat(floatController):
        ...
    class Motion_Clip_SlavePoint3(point3Controller):
        ...
    class Motion_Clip_SlavePos(positionController):
        ...
    class Motion_Clip_SlaveRotation(rotationController):
        ...
    class Motion_Clip_SlaveScale(scaleController):
        ...
    class Motor(SpacewarpObject):
        units: int
        icon_size: float
        On_Time: MXSWrapperBase
        Off_Time: MXSWrapperBase
        Basic_Torque: float
        Feedback_On: int
        Reversible: int
        Target_Revs: float
        Revs_Units: int
        Control_Gain: float
        Enable_Variation: int
        Variation_Period_1: MXSWrapperBase
        Amplitude_1: float
        Variation_Phase_1: float
        Variation_Period_2: MXSWrapperBase
        Amplitude_2: float
        Variation_Phase_2: float
        Range_Enable: int
        Range_Value: float
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
    class MrmMod(modifier):
        vertexCount: int
        vertexPercent: float
        mergeVertex: bool
        mergeThreshold: float
        mergeWithinMesh: bool
        BoundaryMetric: bool
        baseVertices: bool
        multiVertNorm: bool
        creaseAngle: float
        reqGenerate: bool
        resetParams: bool
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
        averageSpeed1: float
        maxAccel1: float
        turnDecel1: float
        turnDecelAngle1: float
        inclineDecel1: float
        inclineDecelAngle1: float
        declineDecel1: float
        declineDecelAngle1: float
        maxHeading1: float
        maxHeadingRate1: float
        maxIncline1: float
        maxDecline1: float
        maxbank1: float
        maxbankRate1: float
        bankfactor1: float
        startFrame1: int
        priority1: int
        averageSpeed2: float
        maxAccel2: float
        turnDecel2: float
        turnDecelAngle2: float
        inclineDecel2: float
        inclineDecelAngle2: float
        declineDecel2: float
        declineDecelAngle2: float
        maxHeading2: float
        maxHeadingRate2: float
        maxIncline2: float
        maxDecline2: float
        maxbank2: float
        maxbankRate2: float
        bankfactor2: float
        startFrame2: int
        priority2: int
        active: bool
        showForces: bool
        showVelocity: bool
        showCogStates: bool
        xyConstrain: bool
        velocityColor: MXSWrapperBase
        useHierBbox: bool
        useBiped: bool
        startClip: int
        rand1: bool
        rand2: bool
        rand3: bool
        rand4: bool
        rand5: bool
        rand6: bool
        rand7: bool
        rand8: bool
        rand9: bool
        rand10: bool
        rand11: bool
        rand12: bool
        rand13: bool
        rand17: bool
        rand18: bool
        rand14: bool
        rand15: bool
        set1: bool
        set2: bool
        set3: bool
        set4: bool
        set5: bool
        set6: bool
        set7: bool
        set8: bool
        set9: bool
        set10: bool
        set11: bool
        set12: bool
        set13: bool
        set14: bool
        set15: bool
        set16: bool
        set17: bool
        set18: bool
        set19: bool
        set20: bool
        set21: bool
        set22: bool
        set24: bool
        set25: bool
        set26: bool
        delegates: MXSWrapperBase
        settings: MXSWrapperBase
        editSetting: MXSWrapperBase
        bipedAssociationType: bool
        bipedAssociationUseBip: bool
        bipeds: MXSWrapperBase
        bipedDelegates: MXSWrapperBase
        animObjNode: None
        ...
    class MultiLayer(Shader):
        ...
    class MultiListBoxControl(RolloutControl):
        ...
    class MultiMaterialClass(Value):
        ...
    class MultiOutputChannelTexmapToTexmap(textureMap):
        sourceMap: None
        outputChannelIndex: int
        ...
    class MultiRes(modifier):
        vertexCount: int
        vertexPercent: float
        mergeVertex: bool
        mergeThreshold: float
        mergeWithinMesh: bool
        BoundaryMetric: bool
        baseVertices: bool
        multiVertNorm: bool
        creaseAngle: float
        reqGenerate: bool
        resetParams: bool
        ...
    class MultiTile(textureMap):
        ...
    class MultiTileMap(textureMap):
        ...
    class Multi_Layer(Shader):
        ...
    class Multimaterial(material):
        materialList: MXSWrapperBase
        mapEnabled: MXSWrapperBase
        names: MXSWrapperBase
        materialIDList: MXSWrapperBase
        ...
    class Multimaterial_empty(material):
        ...
    class MultipleEdgeClass(GlobalUtilityPlugin):
        ...
    class MultipleEdges(Interface):
        ...
    class MultipleFSParams(Value):
        ...
    class Multiple_Delegate_Settings(ReferenceTarget):
        averageSpeed1: float
        maxAccel1: float
        turnDecel1: float
        turnDecelAngle1: float
        inclineDecel1: float
        inclineDecelAngle1: float
        declineDecel1: float
        declineDecelAngle1: float
        maxturn1: float
        maxturnAccel1: float
        maxIncline1: float
        maxDecline1: float
        maxbank1: float
        maxbankAccel1: float
        bankfactor1: float
        startFrame1: int
        priority1: int
        averageSpeed2: float
        maxAccel2: float
        turnDecel2: float
        turnDecelAngle2: float
        inclineDecel2: float
        inclineDecelAngle2: float
        declineDecel2: float
        declineDecelAngle2: float
        maxturn2: float
        maxturnAccel2: float
        maxIncline2: float
        maxDecline2: float
        maxbank2: float
        maxbankAccel2: float
        bankfactor2: float
        startFrame2: int
        priority2: int
        active: bool
        showForces: bool
        showVelocity: bool
        showCogStates: bool
        xyConstrain: bool
        velocityColor: MXSWrapperBase
        useHierBbox: bool
        useBiped: bool
        startClip: int
        rand1: bool
        rand2: bool
        rand3: bool
        rand4: bool
        rand5: bool
        rand6: bool
        rand7: bool
        rand8: bool
        rand9: bool
        rand10: bool
        rand11: bool
        rand12: bool
        rand16: bool
        rand17: bool
        rand18: bool
        rand13: bool
        rand14: bool
        rand15: bool
        set1: bool
        set2: bool
        set3: bool
        set4: bool
        set5: bool
        set6: bool
        set7: bool
        set8: bool
        set9: bool
        set10: bool
        set11: bool
        set12: bool
        set13: bool
        set14: bool
        set15: bool
        set16: bool
        set17: bool
        set18: bool
        set19: bool
        set20: bool
        set21: bool
        set22: bool
        set23: bool
        set24: bool
        set25: bool
        set26: bool
        delegates: MXSWrapperBase
        name: None
        ...
    class Multiple_Delegates(ReferenceTarget):
        averageSpeed1: float
        maxAccel1: float
        turnDecel1: float
        turnDecelAngle1: float
        inclineDecel1: float
        inclineDecelAngle1: float
        declineDecel1: float
        declineDecelAngle1: float
        maxHeading1: float
        maxHeadingRate1: float
        maxIncline1: float
        maxDecline1: float
        maxbank1: float
        maxbankRate1: float
        bankfactor1: float
        startFrame1: int
        priority1: int
        averageSpeed2: float
        maxAccel2: float
        turnDecel2: float
        turnDecelAngle2: float
        inclineDecel2: float
        inclineDecelAngle2: float
        declineDecel2: float
        declineDecelAngle2: float
        maxHeading2: float
        maxHeadingRate2: float
        maxIncline2: float
        maxDecline2: float
        maxbank2: float
        maxbankRate2: float
        bankfactor2: float
        startFrame2: int
        priority2: int
        active: bool
        showForces: bool
        showVelocity: bool
        showCogStates: bool
        xyConstrain: bool
        velocityColor: MXSWrapperBase
        useHierBbox: bool
        useBiped: bool
        startClip: int
        rand1: bool
        rand2: bool
        rand3: bool
        rand4: bool
        rand5: bool
        rand6: bool
        rand7: bool
        rand8: bool
        rand9: bool
        rand10: bool
        rand11: bool
        rand12: bool
        rand13: bool
        rand17: bool
        rand18: bool
        rand14: bool
        rand15: bool
        set1: bool
        set2: bool
        set3: bool
        set4: bool
        set5: bool
        set6: bool
        set7: bool
        set8: bool
        set9: bool
        set10: bool
        set11: bool
        set12: bool
        set13: bool
        set14: bool
        set15: bool
        set16: bool
        set17: bool
        set18: bool
        set19: bool
        set20: bool
        set21: bool
        set22: bool
        set24: bool
        set25: bool
        set26: bool
        delegates: MXSWrapperBase
        settings: MXSWrapperBase
        editSetting: MXSWrapperBase
        bipedAssociationType: bool
        bipedAssociationUseBip: bool
        bipeds: MXSWrapperBase
        bipedDelegates: MXSWrapperBase
        animObjNode: None
        ...
    class Multiple_Edges(GlobalUtilityPlugin):
        ...
    class MusclePatch(helper):
        ...
    class MuscleStrand(helper):
        ...
    class Muscle_Handle(helper):
        ...
    class Muscle_Strand(helper):
        ...
    class MxsUnitResults(Interface):
        ...
    class NCurve_Sel(modifier):
        ...
    class NLAInfo(floatController):
        ...
    class NPRFragment(GraphicsFragmentPlugin):
        ...
    class NSurf_Sel(modifier):
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
    class NURBSCurveshape(shape):
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
    class NavInfo(helper):
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
    class Ngon(shape):
        steps: int
        radius: float
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        cornerRadius: float
        nsides: int
        circular: bool
        scribe: int
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
    class NoMaterial(material):
        ...
    class NoTexture(textureMap):
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
    class NodeObject(node):
        ...
    class NodeTrajectoryTest(Interface):
        ...
    class NodeTransformMonitor(ReferenceTarget):
        ...
    class Noise(textureMap):
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1: None
        map2: None
        map1Enabled: bool
        map2Enabled: bool
        size: float
        phase: float
        Levels: float
        thresholdLow: float
        thresholdHigh: float
        type: int
        coords: MXSWrapperBase
        output: MXSWrapperBase
        ...
    class Noise_float(floatController):
        positive: bool
        seed: int
        frequency: float
        fractal: bool
        roughness: float
        rampin: MXSWrapperBase
        rampout: MXSWrapperBase
        ...
    class Noise_point3(point3Controller):
        seed: int
        frequency: float
        fractal: bool
        roughness: float
        rampin: MXSWrapperBase
        rampout: MXSWrapperBase
        x_positive: bool
        y_positive: bool
        z_positive: bool
        ...
    class Noise_position(positionController):
        seed: int
        frequency: float
        fractal: bool
        roughness: float
        rampin: MXSWrapperBase
        rampout: MXSWrapperBase
        x_positive: bool
        y_positive: bool
        z_positive: bool
        ...
    class Noise_rotation(rotationController):
        seed: int
        frequency: float
        fractal: bool
        roughness: float
        rampin: MXSWrapperBase
        rampout: MXSWrapperBase
        x_positive: bool
        y_positive: bool
        z_positive: bool
        ...
    class Noise_scale(scaleController):
        seed: int
        frequency: float
        fractal: bool
        roughness: float
        rampin: MXSWrapperBase
        rampout: MXSWrapperBase
        x_positive: bool
        y_positive: bool
        z_positive: bool
        ...
    class Noisemodifier(modifier):
        animate: bool
        scale: float
        seed: int
        frequency: float
        fractal: bool
        roughness: float
        phase: MXSWrapperBase
        strength: MXSWrapperBase
        iterations: float
        ...
    class NormalMappingManager(Interface):
        ...
    class Normal_Bump(textureMap):
        mult_spin: float
        bump_spin: float
        normal_map: None
        bump_map: None
        map1on: bool
        map2on: bool
        method: int
        flipred: bool
        flipgreen: bool
        swap_rg: bool
        ...
    class Normalize_Spl(modifier):
        ...
    class Normalize_Spline(modifier):
        ...
    class Normalize_Spline2(modifier):
        length: float
        NormalizeType: int
        numKnots: int
        insertNum: int
        weighted: bool
        MaxKnots: int
        UseMaxKnots: bool
        UseStraightSegments: bool
        RetainKnots: bool
        RetainPercent: int
        ForEachSpline: bool
        RetainTangents: bool
        ShowKnots: bool
        SimpleInterpolation: bool
        ...
    class Normalmodifier(modifier):
        flip: bool
        unify: bool
        ...
    class NormalsMap(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        useNormalBump: bool
        useHeightAsAlpha: bool
        ...
    class NoteTrack(Value):
        ...
    class Notes(helper):
        Comments: None
        ...
    class NotesReferenceTarget(ReferenceTarget):
        Comments: None
        filter: None
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
    class OSLMap(textureMap):
        OSLPath: str
        oslCode: str
        OSLAutoUpdate: bool
        OSLShaderName: str
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        Input_A: MXSWrapperBase
        Input_B: MXSWrapperBase
        Mixer: float
        Input_A_map: None
        Input_B_map: None
        Mixer_map: None
        a: MXSWrapperBase
        b: MXSWrapperBase
        a: MXSWrapperBase
        b: MXSWrapperBase
        ...
    class OSnap(Primitive):
        ...
    class ObRefModAppClass(MAXWrapper):
        ...
    class ObjAssoc(ReferenceTarget):
        objects: MXSWrapperBase
        delegates: MXSWrapperBase
        alignScale: bool
        ...
    class ObjExp(ExporterPlugin):
        ...
    class ObjImp(ImporterPlugin):
        ...
    class ObjectParameter(ReferenceTarget):
        object: None
        Subframe_Sampling: bool
        Use_As_Speed_Or_Spin_Rate: bool
        Units_Per_Type: int
        filter: None
        Input: None
        ...
    class ObjectSet(Set):
        ...
    class ObjectSpaceSubdivideMod(modifier):
        size: float
        subdivideDoEnforceQuality: bool
        subdivideDoSubdivideTriangles: bool
        showAllTriangles: bool
        subdivideMaxSteinerPoints: int
        subdivideQuadAreaRatio: float
        subdivideDiagonalRatio: float
        subdivideNumBuckets: int
        subdivideDoFormQuads: bool
        subdivideRefinementType: int
        manualupdate: int
        remeshType: int
        preserveMeshData: bool
        preservedMapIndex: int
        preserveSharpEdgesByAngle: bool
        preservedSharpEdgeAngle: float
        delaunaySize: float
        delaunayRelaxationCoeff: float
        delaunayRelaxationIterations: int
        adaptiveEdgeLength: float
        adaptiveRegularity: float
        adaptiveThreshold: float
        variableCurvatureEdgeLength: float
        variableCurvatureRegularity: float
        variableCurvatureThreshold: float
        variableCurvatureVariableDensity: float
        variableCurvatureIterations: int
        variableCurvatureTransition: float
        ...
    class Object_Display_Culling(UtilityPlugin):
        ...
    class Object_ID(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        colorMode: int
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
        height: float
        radius: float
        sides: int
        mapcoords: int
        Blend: float
        Cap_Height: float
        Smooth_On: int
        Slice_On: int
        Slice_From: float
        Slice_To: float
        Height_Segments: int
        ...
    class OkClass(Value):
        ...
    class OkMtlForScene(Primitive):
        ...
    class OldBoolean(GeometryClass):
        ...
    class OldVertexPaint(modifier):
        ...
    class Old_PointCache(modifier):
        ...
    class Old_PointCacheWSM(SpacewarpModifier):
        ...
    class Old_Point_Cache(modifier):
        ...
    class Old_Point_CacheSpacewarpModifier(SpacewarpModifier):
        ...
    class Omnilight(light):
        rgb: MXSWrapperBase
        color: MXSWrapperBase
        contrast: float
        enabled: bool
        on: bool
        type: MXSWrapperBase
        value: int
        excludeList: MXSWrapperBase
        includeList: None
        multiplier: float
        softenDiffuseEdge: float
        farAttenStart: float
        farAttenEnd: float
        nearAttenStart: float
        nearAttenEnd: float
        atmosOpacity: float
        atmosColorAmt: float
        decayRadius: float
        shadowColor: MXSWrapperBase
        shadowMultiplier: float
        hsv: MXSWrapperBase
        hue: int
        saturation: int
        inclExclType: int
        affectDiffuse: bool
        affectSpecular: bool
        useNearAtten: bool
        showNearAtten: bool
        useFarAtten: bool
        showFarAtten: bool
        attenDecay: int
        projector: bool
        projectorMap: None
        castShadows: bool
        useGlobalShadowSettings: bool
        raytracedShadows: bool
        atmosShadows: bool
        lightAffectsShadow: bool
        shadowProjectorMap: None
        useShadowProjectorMap: bool
        ambientOnly: bool
        shadowgenerator: MXSWrapperBase
        ...
    class On_Off(floatController):
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
    class OpenSubdiv(modifier):
        isolineDisplay: bool
        iterations: int
        useRenderIterations: bool
        renderIterations: int
        mode: int
        vertboundary: int
        fvarboundary: int
        propagatecorners: bool
        smoothtriangles: bool
        creasemethod: int
        update: int
        solvertype: int
        adaptive: bool
        adaptiveIterations: int
        ...
    class OpenSubdivMod(modifier):
        isolineDisplay: bool
        iterations: int
        useRenderIterations: bool
        renderIterations: int
        mode: int
        vertboundary: int
        fvarboundary: int
        propagatecorners: bool
        smoothtriangles: bool
        creasemethod: int
        update: int
        solvertype: int
        adaptive: bool
        adaptiveIterations: int
        ...
    class Open_Edges(GlobalUtilityPlugin):
        ...
    class OperatorGraph(ReferenceTarget):
        nodes: MXSWrapperBase
        data: str
        ...
    class OperatorGraphCustomAttribute(CustAttrib):
        graph: None
        ...
    class OperatorGraphNode(ReferenceTarget):
        operator_id: int
        operator_map: None
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
    class Optimize_Spline(modifier):
        reducedMaxKnots: int
        iterations: int
        adaptive: bool
        percent: int
        reduce_method: int
        subsegment: int
        reducedMinKnots: int
        ShowKnots: bool
        ...
    class Orbaz_Mix(VideoPostFilter):
        ...
    class OrenNayarBlinn(Shader):
        ...
    class Oren_Nayar_Blinn(Shader):
        ...
    class OrientationBehavior(ReferenceTarget):
        name: str
        headingRelative: bool
        minHeading: float
        maxHeading: float
        maxHeadingVel: float
        headingResponse: float
        pitchRelative: bool
        minpitch: float
        maxpitch: float
        maxPitchVel: float
        pitchResponse: float
        maxBank: float
        maxBankVel: float
        bankPerTurn: float
        ...
    class Orientation_Behavior(ReferenceTarget):
        name: str
        headingRelative: bool
        minHeading: float
        maxHeading: float
        maxHeadingVel: float
        headingResponse: float
        pitchRelative: bool
        minpitch: float
        maxpitch: float
        maxPitchVel: float
        pitchResponse: float
        maxBank: float
        maxBankVel: float
        bankPerTurn: float
        ...
    class Orientation_Constraint(rotationController):
        weight: MXSWrapperBase
        relative: bool
        local_world: int
        ...
    class Orthogonalize(MappedGeneric):
        ...
    class OutputCustom(ReferenceTarget):
        Data_Channel: None
        Data_Handle: int
        Proceed_Type: int
        History_Dependent: bool
        Execution_Order: int
        Priority_Order: int
        filter: None
        Input_1: None
        ...
    class OutputNew(ReferenceTarget):
        Data_Type: int
        Scope_Type: int
        Data_Handle: int
        Proceed_Type: int
        History_Dependent: bool
        Execution_Order: int
        Priority_Order: int
        filter: None
        Input_1: None
        ...
    class OutputPhysX(ReferenceTarget):
        Data_Type: int
        Match_Type: int
        Threshold_Type: int
        Proceed_Type: int
        History_Dependent: bool
        Execution_Order: int
        Priority_Order: int
        filter: None
        Input: None
        ...
    class OutputStandard(ReferenceTarget):
        Data_Type: int
        Time_Type: int
        Position_Type: int
        Speed_Type: int
        Rotation_Type: int
        Spin_Type: int
        Scale_Type: int
        Script_Type: int
        TM_Type: int
        Mapping_Type: int
        Map_Channel: int
        Proceed_Type: int
        History_Dependent: bool
        Execution_Order: int
        Priority_Order: int
        Use_T2: bool
        Use_E2: bool
        Acceleration_Type: int
        Visibility_Type: int
        Viewport_Render_Operator: None
        filter: None
        Input_1: None
        Input_2: None
        ...
    class OutputTest(ReferenceTarget):
        type: int
        Use_T2: bool
        Proceed_Type: int
        History_Dependent: bool
        Execution_Order: int
        Priority_Order: int
        filter: None
        Input_1: None
        Input_2: None
        ...
    class Output_mParticles(ReferenceTarget):
        Data_Type: int
        Match_Type: int
        Threshold_Type: int
        Proceed_Type: int
        History_Dependent: bool
        Execution_Order: int
        Priority_Order: int
        filter: None
        Input: None
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
        size: float
        seed: int
        iconSize: float
        speed: float
        mappingType: int
        formation: int
        viewType: int
        viewPercent: float
        quantityMethod: int
        particleType: int
        standardParticle: int
        metaballRenderCoarsness: float
        metaballViewCoarsness: float
        metaballAutoCoarsness: bool
        instanceSubTree: bool
        instanceKeyOffsetType: int
        instanceFrameOffset: int
        materialSource: int
        spinAxisType: int
        spawnType: int
        spawnSpeedType: int
        spawnInheritVelocity: bool
        spawnSpeedFixed: bool
        spawnScaleType: int
        spawnScaleFixed: bool
        motionInfluence: float
        motionMultiplier: float
        motionVariation: float
        emitter: None
        instancingObject: None
        lifespanValueQueue: MXSWrapperBase
        objectMutationQueue: MXSWrapperBase
        subsampleEmitterTranslation: bool
        subsampleEmitterRotation: bool
        subsampleCreationTime: bool
        iconHidden: bool
        numDistinctPoints: int
        fragmentMethod: int
        fragChunkMinimum: int
        fragSmoothingAngle: float
        fragEdgeMatID: int
        fragOutsideMatID: int
        fragBackMatID: int
        life: MXSWrapperBase
        Divergence_Angle: float
        Fragment_Thickness: float
        Bubble_Amplitude: float
        Bubble_Amplitude_Variation: float
        Bubble_Period: MXSWrapperBase
        Bubble_Period_Variation: float
        Bubble_Phase: float
        Blur_Stretch: int
        Spawn_Generations: int
        Spawn_Multiplier: int
        Spawn_Lifespan: int
        Use_Selected_Subobjects: int
        Speed_Variation: float
        Birth_Rate: int
        Total_Number: int
        Emitter_Start: MXSWrapperBase
        Emitter_Stop: MXSWrapperBase
        Display_Until: MXSWrapperBase
        Life_Variation: MXSWrapperBase
        Size_Variation: float
        Growth_Time: MXSWrapperBase
        Fade_Time: MXSWrapperBase
        Metaparticle_Tension: float
        Metaparticle_Tension_Variation: float
        Mapping_Time_Base: MXSWrapperBase
        Mapping_Distance_Base: float
        Spin_Time: MXSWrapperBase
        Spin_Time_Variation: float
        Spin_Phase: float
        Spin_Phase_Variation: float
        X_Spin_Vector: float
        Y_Spin_Vector: float
        Z_Spin_Vector: float
        Spin_Axis_Variation: float
        Spawn_Direction_Chaos: float
        Spawn_Speed_Chaos: float
        Spawn_Scale_Chaos: float
        Spawn_Affects: int
        Spawn_Multiplier_Variation: float
        Bubble_Phase_Variation: float
        Die__X_frames_after_collision: MXSWrapperBase
        Die__X_frames_after_collision_variation: float
        Interparticle_Collisions_On: int
        Interparticle_Collision_Steps: int
        Interparticle_Collision_Bounce: float
        Interparticle_Collision_Bounce_Variation: float
        ...
    class PB2Parameter(ReferenceTarget):
        ...
    class PBEndTrack(Primitive):
        ...
    class PBRImporter(UtilityPlugin):
        ...
    class PBRMetalRough(material):
        ao_affects_diffuse: bool
        ao_affects_reflection: bool
        normal_flip_red: bool
        normal_flip_green: bool
        basecolor: MXSWrapperBase
        base_color_map: None
        metalness: float
        metalness_map: None
        roughness: float
        roughness_map: None
        useGlossiness: int
        ao_map: None
        bump_map_amt: float
        norm_map: None
        emit_color: MXSWrapperBase
        emit_color_map: None
        opacity_map: None
        displacement_amt: float
        displacement_map: None
        ...
    class PBRSpecGloss(material):
        ao_affects_diffuse: bool
        ao_affects_reflection: bool
        normal_flip_red: bool
        normal_flip_green: bool
        basecolor: MXSWrapperBase
        base_color_map: None
        Specular: MXSWrapperBase
        specular_map: None
        glossiness: float
        glossiness_map: None
        useGlossiness: int
        ao_map: None
        bump_map_amt: float
        norm_map: None
        emit_color: MXSWrapperBase
        emit_color_map: None
        opacity_map: None
        displacement_amt: float
        displacement_map: None
        ...
    class PBStartTrack(Primitive):
        ...
    class PBTrackGetToolActive(Primitive):
        ...
    class PBomb(SpacewarpObject):
        range: float
        symmetry: int
        strength: float
        chaos: float
        icon_size: float
        Lasts_For: MXSWrapperBase
        Decay_Type: int
        Start_Time: MXSWrapperBase
        ...
    class PBombMod(SpacewarpModifier):
        ...
    class PCloud(GeometryClass):
        size: float
        seed: int
        speed: float
        mappingType: int
        formation: int
        viewType: int
        viewPercent: float
        emitterHidden: bool
        quantityMethod: int
        motionType: int
        directionVariation: float
        particleType: int
        standardParticle: int
        metaballRenderCoarsness: float
        metaballViewCoarsness: float
        metaballAutoCoarsness: bool
        instanceSubTree: bool
        instanceKeyOffsetType: int
        instanceFrameOffset: int
        materialSource: int
        spinAxisType: int
        spawnType: int
        spawnSpeedType: int
        spawnInheritVelocity: bool
        spawnSpeedFixed: bool
        spawnScaleType: int
        spawnScaleFixed: bool
        motionInfluence: float
        motionMultiplier: float
        motionVariation: float
        emitter: None
        motionReferenceObject: None
        instancingObject: None
        lifespanValueQueue: MXSWrapperBase
        objectMutationQueue: MXSWrapperBase
        life: MXSWrapperBase
        Direction_Vector_X: float
        Direction_Vector_Y: float
        Direction_Vector_Z: float
        Emitter_Rad_Len: float
        Emitter_Height: float
        Bubble_Amplitude: float
        Bubble_Amplitude_Variation: float
        Bubble_Period: MXSWrapperBase
        Bubble_Period_Variation: float
        Bubble_Phase: float
        Blur_Stretch: int
        Spawn_Generations: int
        Spawn_Multiplier: int
        Spawn_Lifespan: int
        Speed_Variation: float
        Birth_Rate: int
        Total_Number: int
        Emitter_Start: MXSWrapperBase
        Emitter_Stop: MXSWrapperBase
        Display_Until: MXSWrapperBase
        Life_Variation: MXSWrapperBase
        Size_Variation: float
        Growth_Time: MXSWrapperBase
        Fade_Time: MXSWrapperBase
        Emitter_Width: float
        Metaparticle_Tension: float
        Metaparticle_Tension_Variation: float
        Mapping_Time_Base: MXSWrapperBase
        Mapping_Distance_Base: float
        Spin_Time: MXSWrapperBase
        Spin_Time_Variation: float
        Spin_Phase: float
        Spin_Phase_Variation: float
        X_Spin_Vector: float
        Y_Spin_Vector: float
        Z_Spin_Vector: float
        Spin_Axis_Variation: float
        Spawn_Direction_Chaos: float
        Spawn_Speed_Chaos: float
        Spawn_Scale_Chaos: float
        Bubble_Phase_Variation: float
        Die__X_frames_after_collision: MXSWrapperBase
        Die__X_frames_after_collision_variation: float
        Interparticle_Collisions_On: int
        Interparticle_Collision_Steps: int
        Interparticle_Collision_Bounce: float
        Interparticle_Collision_Bounce_Variation: float
        ...
    class PDAlpha(VideoPostFilter):
        ...
    class PFActionListPool(ReferenceTarget):
        ...
    class PFArrow(helper):
        ...
    class PFBoxMeshWrapper(ReferenceTarget):
        ...
    class PFCapsuleMeshWrapper(ReferenceTarget):
        ...
    class PFConvexMeshWrapper(ReferenceTarget):
        ...
    class PFDataOperatorState(ReferenceTarget):
        ...
    class PFEngine(helper):
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
        Enable_Particles: bool
        Logo_Size: float
        Emitter_Type: int
        Emitter_Length: float
        Emitter_Width: float
        Emitter_Height: float
        Show_Logo: bool
        Show_Emitter: bool
        Quantity_Viewport: float
        Quantity_Render: float
        Select_By_Particle_ID: int
        Clear_Selection: bool
        Selected_Particles: MXSWrapperBase
        Selection_Level: int
        Particle_Amount_Limit: int
        Integration_for_Viewport: int
        Integration_for_Render: int
        Enable_Script_for_Every_Step_Update: bool
        Every_Step_Update_Script: str
        Use_File_for_Every_Step_Update: bool
        Every_Step_Update_Script_File: str
        Enable_Script_for_Final_Step_Update: bool
        Final_Step_Update_Script: str
        Use_File_for_Final_Step_Update: bool
        Final_Step_Update_Script_File: str
        X_Coord: int
        Y_Coord: int
        Z_Order: int
        width: int
        ...
    class PFlow_Collision_Shape(SpacewarpModifier):
        shape: int
        Smooth_Surface: bool
        Restitution: float
        Static_Friction: float
        Dynamic_Friction: float
        Visualize_Collision_Shape: bool
        thickness: float
        Normal_Offset: float
        Side_Overlap: float
        Placement_Vertices: bool
        Placement_Edges: bool
        Placement_Polygons: bool
        Selected_Only: bool
        active: bool
        Primitive_Size_Type: int
        ...
    class PMAlpha(VideoPostFilter):
        ...
    class POmniFlect(SpacewarpObject):
        timeOn: MXSWrapperBase
        timeOff: MXSWrapperBase
        affects: float
        Bounce: float
        bounceVar: float
        chaos: float
        inheritVelocity: float
        refracts: float
        deceleration: float
        decelVar: float
        Refraction: float
        refractionVar: float
        diffusion: float
        diffusionVar: float
        width: float
        height: float
        Spawn: float
        passVelocity: float
        passVelocityVar: float
        friction: float
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
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class PaintLayerMod(modifier):
        ignoreBackfacing: bool
        mapChannel: int
        layerMode: str
        layerOpacity: float
        layerIsolated: bool
        surviveCondense: bool
        lightingModel: int
        colorBy: int
        castShadows: bool
        useMaps: bool
        useRadiosity: bool
        radiosityOnly: bool
        hideUnselSubobjs: bool
        radiosityOption: int
        ...
    class PaintRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class PaintSoftSelPresetContext(Interface):
        ...
    class Paintbox(UserDataTypeClass):
        ...
    class PaintboxStartup(GlobalUtilityPlugin):
        ...
    class PainterInterface(ReferenceTarget):
        nodes: MXSWrapperBase
        drawRing: bool
        drawNormal: bool
        drawTrace: bool
        minSize: float
        maxSize: float
        minStr: float
        maxStr: float
        additiveMode: bool
        falloffGraph: MXSWrapperBase
        pressureEnable: bool
        pressureAffects: int
        updateOnMouseUp: bool
        quadDepth: int
        predefinedStrEnable: bool
        predefinedStrGraph: MXSWrapperBase
        predefinedSizeEnable: bool
        predefinedSizeGraph: MXSWrapperBase
        mirrorEnable: bool
        mirrorAxis: int
        mirrorOffset: float
        mirrorGizmoSize: float
        pointGatherEnable: bool
        buildVNormals: bool
        lagRate: int
        normalScale: float
        marker: float
        markerEnable: bool
        offMeshHitType: bool
        offMeshHitZDepth: float
        offMeshHitPos: MXSWrapperBase
        strDragLimitMin: float
        strDragLimitMax: float
        SplineConstraintNode: None
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
    class ParticleCreatorOSM(modifier):
        type: int
        Before_Hide: bool
        After_Hide: bool
        Time_On: int
        Time_Off: int
        Particle_Flow_Systems: MXSWrapperBase
        All_Particle_Flow_Events: bool
        Particle_Flow_Events: MXSWrapperBase
        Zone_Size: float
        Scale_Influence: float
        Zone_Weight: float
        Multiply_By_Scale: bool
        Blend_Particles: bool
        Split_Precision_Type: int
        Relative_Precision: float
        Absolute_Precision: float
        Sync_Type: int
        Use_Time_Off: bool
        ...
    class ParticleGroup(GeometryClass):
        ...
    class ParticleSkinnerOSM(modifier):
        Before_Hide: bool
        After_Hide: bool
        Time_On: int
        Time_Off: int
        Particle_Flow_Systems: MXSWrapperBase
        All_Particle_Flow_Events: bool
        Particle_Flow_Events: MXSWrapperBase
        falloff: float
        Distance_Influence_Type: int
        Absolute_Influence: float
        Size_Influence: float
        Binding_Influence: float
        Controllers_Limit: int
        Control_By_Inside_Inclusion: bool
        Rip_Surface_Apart: int
        Distance_Type: int
        Relative_Distance: float
        Absolute_Distance: float
        Split_Precision_Type: int
        Relative_Precision: float
        Absolute_Precision: float
        Binding_List_Type: int
        PhysX_Glue_Tests: MXSWrapperBase
        Remove_Uncontrolled: bool
        Sustain_Topology: bool
        Interval_Ticks: int
        Use_Visibility_Data_Channel: bool
        Visibility_Data_Creator: None
        Use_Data_Channel: bool
        Data_Channel_Creator: None
        Map_Channel_Type: int
        Map_Channel: int
        Display_Influence: bool
        Display_Unassigned_Points: bool
        Display_Control_Particles: bool
        Use_Time_Off: bool
        ...
    class ParticleView(helper):
        ...
    class Particle_Age(textureMap):
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        color3: MXSWrapperBase
        map1: None
        map2: None
        map3: None
        map1Enabled: bool
        map2Enabled: bool
        map3Enabled: bool
        age1: float
        age2: float
        age3: float
        output: MXSWrapperBase
        ...
    class Particle_Bitmap(textureMap):
        ...
    class Particle_Cache(SpacewarpModifier):
        ...
    class Particle_Face_Creator(modifier):
        type: int
        Before_Hide: bool
        After_Hide: bool
        Time_On: int
        Time_Off: int
        Particle_Flow_Systems: MXSWrapperBase
        All_Particle_Flow_Events: bool
        Particle_Flow_Events: MXSWrapperBase
        Zone_Size: float
        Scale_Influence: float
        Zone_Weight: float
        Multiply_By_Scale: bool
        Blend_Particles: bool
        Split_Precision_Type: int
        Relative_Precision: float
        Absolute_Precision: float
        Sync_Type: int
        Use_Time_Off: bool
        ...
    class Particle_Flow_Global_Actions(GlobalUtilityPlugin):
        ...
    class Particle_Flow_Tools_Global_Utility(GlobalUtilityPlugin):
        ...
    class Particle_Flow_Utility(UtilityPlugin):
        ...
    class Particle_MBlur(textureMap):
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        sharp: float
        ...
    class Particle_Paint(helper):
        Spray_Radius: float
        Density_Center: float
        Density_Sides: float
        Per_Jet_Limit: int
        Rate_Type: int
        Rate_Drops_Per_Second: float
        Rate_Drops_Per_Length_Unit: float
        Rate_Drops_Per_Jet: int
        Display_Type: int
        Display_Size: float
        Jet_Start_Type: int
        Jet_Start_Time: int
        Jet_Stop_Type: int
        Time_Scale: float
        Jet_Stop_Time: int
        Jet_Duration: int
        AutoAdjust_Current_Frame: bool
        Adjust_Global_Timing: bool
        icon_size: float
        Random_Seed: int
        Use_Radius_Graph: bool
        Spray_Radius_Graph: None
        Use_Rate_Graph: bool
        Spray_Radius_Rate: None
        Spray_At_Type: int
        Spray_At_Objects: MXSWrapperBase
        Objects_Animated_Surface: bool
        Include_Spray_Children: bool
        Include_Spray_Group_Members: bool
        Use_Mask_Objects: bool
        Masks: MXSWrapperBase
        Include_Mask_Children: bool
        Include_Mask_Group_Members: bool
        Selection_Filter_Type: int
        Location_Type: int
        distance: float
        Distance_Variation: float
        Use_Separation: bool
        Separation_Distance: float
        Maximum_Number_Of_Attempts: int
        Stack_Up_For_Separation: bool
        Generate_Rotation: bool
        Priority_Axis: int
        Reverse_X_Axis: bool
        Reverse_Z_Axis: bool
        Orientation_Type_For_X_Axis: int
        Orientation_Type_For_Z_Axis: int
        Divergence_For_X_Axis: float
        Divergence_For_Z_Axis: float
        Acquire_Sub_Material_Index: bool
        Generate_Mapping: bool
        Assign_To_Mapping_Channels: MXSWrapperBase
        Mapping_Type: int
        Mapping_Start_Value: float
        Mapping_End_Value: float
        Mapping_Offset_Value_Per_Second: float
        Mapping_Offset_Value_Per_Drop: float
        Show_Particle_Timing: bool
        Late_Color: MXSWrapperBase
        Editing_Start_At: int
        Editing_Stop_Type: int
        Editing_Stop_At: int
        Editing_Duration: int
        Editing_Adjust_Global_Timing: bool
        Selected_Strokes: MXSWrapperBase
        Auto_Sync_Timing_By_Selected_Stroke: bool
        ...
    class Particle_Paint_Cursor(GeometryClass):
        ...
    class Particle_Skinner(modifier):
        Before_Hide: bool
        After_Hide: bool
        Time_On: int
        Time_Off: int
        Particle_Flow_Systems: MXSWrapperBase
        All_Particle_Flow_Events: bool
        Particle_Flow_Events: MXSWrapperBase
        falloff: float
        Distance_Influence_Type: int
        Absolute_Influence: float
        Size_Influence: float
        Binding_Influence: float
        Controllers_Limit: int
        Control_By_Inside_Inclusion: bool
        Rip_Surface_Apart: int
        Distance_Type: int
        Relative_Distance: float
        Absolute_Distance: float
        Split_Precision_Type: int
        Relative_Precision: float
        Absolute_Precision: float
        Binding_List_Type: int
        PhysX_Glue_Tests: MXSWrapperBase
        Remove_Uncontrolled: bool
        Sustain_Topology: bool
        Interval_Ticks: int
        Use_Visibility_Data_Channel: bool
        Visibility_Data_Creator: None
        Use_Data_Channel: bool
        Data_Channel_Creator: None
        Map_Channel_Type: int
        Map_Channel: int
        Display_Influence: bool
        Display_Unassigned_Points: bool
        Display_Control_Particles: bool
        Use_Time_Off: bool
        ...
    class Particle_View(helper):
        ...
    class Particle_View_Global_Actions(GlobalUtilityPlugin):
        ...
    class Particles(ReferenceTarget):
        type: int
        Use_Proxy_Filter: bool
        Filter_Data_Channel: None
        Filter_Data_Handle: int
        Outer_Radius: float
        Use_Core_Radius: bool
        Core_Radius: float
        Field_Of_Vision: float
        Apply_Double_Filtering: bool
        Use_Proxy_Particles: bool
        Use_R2: bool
        Use_R3: bool
        Use_R4: bool
        FOV_Direction_Type: int
        Use_V6: bool
        Use_Custom_Particle_Weight: bool
        Weight_Data_Channel: None
        Weight_Data_Handle: int
        Prevalent_Data_Channel: None
        Prevalent_Data_Handle: int
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        Input_5: None
        Input_6: None
        ...
    class PasteSkinWeights(modifier):
        ...
    class Paste_Skin_Weights(modifier):
        ...
    class PatchDeform(modifier):
        rotation: float
        V_Stretch: float
        Plane_to_Patch_Deform: int
        Flip_deformation_axis: int
        U_Stretch: float
        V_Percent: float
        U_Percent: float
        ...
    class Patch_Select(modifier):
        ...
    class PathDeform(modifier):
        axis: int
        rotation: float
        Twist: float
        Stretch: float
        path: None
        Flip_deformation_axis: int
        Percent_along_path: float
        ...
    class PathDeformSpaceWarp(SpacewarpObject):
        ...
    class PathFollowBehavior(ReferenceTarget):
        name: str
        path: None
        radius: float
        awareness: float
        awareDeviation: float
        start: int
        direction: int
        endAction: int
        seed: int
        forceColor: MXSWrapperBase
        displayForce: bool
        targetColor: MXSWrapperBase
        displayTarget: bool
        targetScale: float
        ...
    class PathName(Value):
        ...
    class Path_Constraint(positionController):
        percent: float
        follow: bool
        path: None
        bank: bool
        bankAmount: float
        smoothness: float
        allowUpsideDown: bool
        constantVel: bool
        axis: int
        axisFlip: bool
        weight: MXSWrapperBase
        loop: bool
        relative: bool
        ...
    class Path_Deform2(modifier):
        spline: None
        Percent_along_path: float
        Stretch: float
        rotation: float
        Twist: float
        auto_stretch: bool
        auto_amount: float
        flip: bool
        axis: int
        uniform: bool
        x_offset: float
        y_offset: float
        z_offset: float
        AcrossShapes: int
        AdoptMatID: bool
        RoundMatID: int
        Loopback: bool
        Apply_U: bool
        Apply_V: bool
        Apply_W: bool
        channel: int
        upVector: int
        MoveBeforeRotation: bool
        UsePivotPoint: bool
        RotationEnable: bool
        DrivingRotScale: float
        PreserveForm: bool
        AdaptiveUpVector: bool
        LookAtNode: None
        rotationCurve: MXSWrapperBase
        ScaleEnable: bool
        scaleCurve: MXSWrapperBase
        DrivingScaleScale: float
        use_legacy: bool
        by_element: bool
        ...
    class Path_Follow(SpacewarpObject):
        icon_size: float
        Range_Limited: int
        Spline_Follow_Type: int
        Tangent_Chaos: float
        Tang_Chaos_Var: float
        Tangent_Dir: int
        Spiral_Chaos: float
        Spiral_Chaos_Var: float
        Spiral_Dir: int
        Travel_Time: MXSWrapperBase
        Travel_Var: float
        Stop_Time: MXSWrapperBase
        Constant_Speed: int
        Range_Value: float
        Start_Time: MXSWrapperBase
        ...
    class Path_FollowMod(SpacewarpModifier):
        ...
    class Path_Follow_Behavior(ReferenceTarget):
        name: str
        path: None
        radius: float
        awareness: float
        awareDeviation: float
        start: int
        direction: int
        endAction: int
        seed: int
        forceColor: MXSWrapperBase
        displayForce: bool
        targetColor: MXSWrapperBase
        displayTarget: bool
        targetScale: float
        ...
    class PerezAllWeather(Interface):
        ...
    class Perlin_Marble(textureMap):
        map1: None
        map2: None
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1Enabled: bool
        map2Enabled: bool
        saturation1: float
        saturation2: float
        size: float
        level: float
        coords: MXSWrapperBase
        ...
    class PersistentIsolationData(ReferenceTarget):
        ...
    class PersistentNodeSet(ReferenceTarget):
        ...
    class Perspective_Match(UtilityPlugin):
        ...
    class PhilBitmap(textureMap):
        ...
    class Phong(Shader):
        ...
    class Phong2(Shader):
        ...
    class PhysSunSky_ShaderGenerator(Interface):
        ...
    class PhysXBuoyancy(helper):
        density: float
        Level_Type: int
        Level_Height: float
        Grid_Geometry: None
        Use_Quadratic_Drag: bool
        Quadratic_Drag: float
        Use_Linear_Drag: bool
        Linear_Drag: float
        Use_Angular_Drag: bool
        Angular_Drag: float
        Surface_Unit: float
        Icon_Shape: int
        Icon_Length: float
        Icon_Width: float
        Icon_Height: float
        Limit_Buoyancy_By_Icon: bool
        Color_Coordinated: bool
        ...
    class PhysXCollision(helper):
        Deflectors: MXSWrapperBase
        Test_True: bool
        Test_Type: int
        Min_Speed: float
        Max_Speed: float
        Collision_Count: int
        Report_To_Data_Operator: bool
        Additive_Count: bool
        Collision_Group: int
        ...
    class PhysXDrag(helper):
        Timing_Type: int
        Apply_Linear_Damping: bool
        Linear_Damping: float
        Apply_Angular_Damping: bool
        Angular_Damping: float
        Sync: int
        Speed_Multiplier: bool
        Speed_Unit: float
        Spin_Unit: float
        Use_Data_Wiring: bool
        Linear_Damping_From_Data: bool
        Linear_Damping_Data_Creator: None
        Angular_Damping_From_Data: bool
        Angular_Damping_Data_Creator: None
        ...
    class PhysXFlow(ReferenceTarget):
        ...
    class PhysXForce(helper):
        Force_Type: int
        Force_Variation_Threshold: bool
        Shape_Size: float
        Influence: float
        Sync: int
        Force_Space_Warps: MXSWrapperBase
        Force_Overlapping: int
        Impulse_On_Event_Entry: bool
        Time_Warp: int
        Exponent: int
        Use_Script_Float: int
        ...
    class PhysXGlue(helper):
        Timing_Type: int
        Bind_Distance: float
        Use_Bind_Gap_Condition: bool
        Bind_Gap: float
        Bind_Center_Aligned_Only: bool
        Align_Margin: float
        Allow_Binding_Penetration: bool
        type: int
        Breakable_By_Force: bool
        Max_Force: float
        Max_Torque: float
        Max_By_Bind_Distance: bool
        Distance_Unit: float
        Continuous_Adjustment: bool
        Sync: int
        Max_Binds_Per_Particle: int
        Test_True: bool
        Test_Type: int
        Bind_In_Current_Event: bool
        Bind_With_Other_Events: bool
        Events_To_Bind_With: MXSWrapperBase
        Bind_With_Deflectors: bool
        Bind_With_Ground: bool
        Deflectors_To_Bind_With: MXSWrapperBase
        Visualize_Binding: bool
        color: MXSWrapperBase
        Simplified_Binding_Anchor_Type: int
        Rigid_Binding_Anchor_Type: int
        Solver_Factor: float
        Use_Minimum_Distance_Limit: bool
        Minimum_Distance_Type: int
        Minimum_Absolute_Distance: float
        Minimum_Relative_Distance: float
        Use_Maximum_Distance_Limit: bool
        Maximum_Distance_Type: int
        Maximum_Absolute_Distance: float
        Maximum_Relative_Distance: float
        Enable_Spring_Force: bool
        Adjust_By_Particle_Mass: bool
        Spring_Coef: float
        Damper_Coef: float
        Bury_Binding_Anchors: bool
        depth: float
        Breakable_By_Overstretch: bool
        Overstretch_Type: int
        Overstretch_Absolute_Limit: float
        Overstretch_Relative_Limit: float
        Bind_Distance_From_Data: bool
        Bind_Distance_Data_Creator: None
        Bind_Gap_From_Data: bool
        Bind_Gap_Data_Creator: None
        Breakability_Max_Force_From_Data: bool
        Breakability_Max_Force_Data_Creator: None
        Breakability_Max_Torque_From_Data: bool
        Breakability_Max_Torque_Data_Creator: None
        Max_Binds_Per_Particle_From_Data: bool
        Max_Binds_Per_Particle_Data_Creator: None
        Binding_Groups_From_Data: bool
        Binding_Groups_Data_Creator: None
        Minimum_Distance_Limit_From_Data: bool
        Minimum_Distance_Limit_Data_Creator: None
        Maximum_Distance_Limit_From_Data: bool
        Maximum_Distance_Limit_Data_Creator: None
        Spring_Force_Coef_From_Data: bool
        Spring_Force_Coef_Data_Creator: None
        Spring_Damper_Coef_From_Data: bool
        Spring_Damper_Coef_Data_Creator: None
        Overstretch_Distance_Limit_From_Data: bool
        Overstretch_Distance_Limit_Data_Creator: None
        Num_Active_Bindings_To_Data: bool
        Num_Active_Bindings_Data_Creator: None
        Num_Broken_Bindings_To_Data: bool
        Num_Broken_Bindings_Data_Creator: None
        Num_Broken_By_Force_To_Data: bool
        Num_Broken_By_Force_Data_Creator: None
        Average_Binding_Length_To_Data: bool
        Average_Binding_Length_Data_Creator: None
        Minimum_Binding_Length_To_Data: bool
        Minimum_Binding_Length_Data_Creator: None
        Maximum_Binding_Length_To_Data: bool
        Maximum_Binding_Length_Data_Creator: None
        Average_Breaking_Impulse_To_Data: bool
        Average_Breaking_Impulse_Data_Creator: None
        Maximum_Breaking_Impulse_To_Data: bool
        Maximum_Breaking_Impulse_Data_Creator: None
        ...
    class PhysXInterCollision(helper):
        Scope_Type: int
        Selected_Events: MXSWrapperBase
        Test_Type: int
        Min_Speed: float
        Max_Speed: float
        Collision_Count: int
        Report_To_Data_Operator: bool
        Additive_Count: bool
        ...
    class PhysXModRB(modifier):
        type: int
        switchType: bool
        switchTypeAtFrame: int
        enableGravity: bool
        continuousCollisionDetection: bool
        sleepAtStart: bool
        CollideWithRigidBodies: bool
        extraShapes: None
        manualSetup: bool
        materialID: int
        density: float
        volume: float
        mass: float
        staticFriction: float
        dynamicFriction: float
        bounciness: float
        EnableAdvancedSettings: int
        contactShellOverrideGlobals: bool
        contactShellContactDistance: float
        contactShellRestDepth: float
        SolverIter: bool
        SolverIterValue: int
        InitialMotionStyle: int
        InitialVelocityX: float
        InitialVelocityY: float
        InitialVelocityZ: float
        VelocitySpeed: float
        InitialSpinX: float
        InitialSpinY: float
        InitialSpinZ: float
        SpinSpeed: float
        massCenterX: float
        massCenterY: float
        massCenterZ: float
        linearDamping: float
        AngularDamping: float
        baked: int
        meshType: int
        meshCustomMesh: None
        meshVerticesLimit: int
        meshInflation: float
        meshConvexStyle: int
        meshRadius: float
        meshLength: float
        meshWidth: float
        meshHeight: float
        meshOverrideMaterial: bool
        compositeMaxVertices: int
        compositeMaxConcavity: float
        smallClusterThreshold: float
        enableSolidMeshes: bool
        compositeHighQuality: bool
        massCenterMode: int
        EnableBackfaceCollision: bool
        ForcesList: MXSWrapperBase
        showPhysicalMesh: bool
        ...
    class PhysXPanel(ReferenceTarget):
        enableGravity: bool
        gravityDirection: int
        gravity: float
        sleepSpeed: float
        sleepSpin: float
        solverIteration: int
        useGroundPlane: bool
        onLastFrame: int
        loopAnimation: int
        useFirst: bool
        physicalMeshes: int
        subSteps: int
        UseMultiThread: bool
        UseHardwareScene: bool
        enableCCD: bool
        sleepThresholdsAutomatic: int
        ccdMinSpeedAutomatic: int
        bounceMinSpeedAutomatic: int
        ccdMinSpeedThreshold: float
        bounceMinSpeedThreshold: float
        visualizerEnable: bool
        visualizerScale: float
        bodyAxis: bool
        bodyLinearVel: bool
        bodyAngularVel: bool
        jointLocalAxis: bool
        jointWorldAxis: bool
        jointLimits: bool
        contactPoints: bool
        contactNormal: bool
        contactForce: bool
        collisionShapes: bool
        collisionCompounds: bool
        collisionSpheres: bool
        gravityMode: int
        gravityObject: None
        groundHeight: float
        shapePerElement: bool
        exporterMode: int
        sleepEnergy: float
        pluginBuild: str
        UseAdaptiveForce: bool
        destructionRadius: float
        destructionDamage: float
        destructionMomentum: float
        contactShellLegacyMode: bool
        contactShellContactDistance: float
        skinWidth: float
        pluginPropertyVersion: int
        unitType: int
        unitScale: float
        dynamicFrictionScale: float
        staticFrictionScale: float
        maxAngleVelocity: float
        ccdEpsilon: float
        geometryScale: float
        restoreOriginalPose: bool
        ...
    class PhysXPanelGUP(GlobalUtilityPlugin):
        ...
    class PhysXPanelGlobalUtilityPlugin(GlobalUtilityPlugin):
        ...
    class PhysXPanelInterface(Interface):
        ...
    class PhysXPanelReferenceTarget(ReferenceTarget):
        enableGravity: bool
        gravityDirection: int
        gravity: float
        sleepSpeed: float
        sleepSpin: float
        solverIteration: int
        useGroundPlane: bool
        onLastFrame: int
        loopAnimation: int
        useFirst: bool
        physicalMeshes: int
        subSteps: int
        UseMultiThread: bool
        UseHardwareScene: bool
        enableCCD: bool
        sleepThresholdsAutomatic: int
        ccdMinSpeedAutomatic: int
        bounceMinSpeedAutomatic: int
        ccdMinSpeedThreshold: float
        bounceMinSpeedThreshold: float
        visualizerEnable: bool
        visualizerScale: float
        bodyAxis: bool
        bodyLinearVel: bool
        bodyAngularVel: bool
        jointLocalAxis: bool
        jointWorldAxis: bool
        jointLimits: bool
        contactPoints: bool
        contactNormal: bool
        contactForce: bool
        collisionShapes: bool
        collisionCompounds: bool
        collisionSpheres: bool
        gravityMode: int
        gravityObject: None
        groundHeight: float
        shapePerElement: bool
        exporterMode: int
        sleepEnergy: float
        pluginBuild: str
        UseAdaptiveForce: bool
        destructionRadius: float
        destructionDamage: float
        destructionMomentum: float
        contactShellLegacyMode: bool
        contactShellContactDistance: float
        skinWidth: float
        pluginPropertyVersion: int
        unitType: int
        unitScale: float
        dynamicFrictionScale: float
        staticFrictionScale: float
        maxAngleVelocity: float
        ccdEpsilon: float
        geometryScale: float
        restoreOriginalPose: bool
        ...
    class PhysXShape(helper):
        Collide_Type: int
        Display_Type: int
        Conform_To_Particle_Shape: bool
        Shape_Length: float
        Shape_Width: float
        Shape_Height: float
        Scale_Type: int
        scale: MXSWrapperBase
        color: MXSWrapperBase
        Weld_Threshold: float
        Inflate_Width: float
        Scale_Margin: float
        Restitution: float
        Static_Friction: float
        Dynamic_Friction: float
        Mass_Type: int
        mass: float
        density: float
        Interpenetration_Tolerance: float
        Generate_Tolerance_Channel: bool
        Collision_Group: int
        ...
    class PhysXShapeConvex(GeometryClass):
        ...
    class PhysXShapeWSM(SpacewarpModifier):
        shape: int
        Smooth_Surface: bool
        Restitution: float
        Static_Friction: float
        Dynamic_Friction: float
        Visualize_Collision_Shape: bool
        thickness: float
        Normal_Offset: float
        Side_Overlap: float
        Placement_Vertices: bool
        Placement_Edges: bool
        Placement_Polygons: bool
        Selected_Only: bool
        active: bool
        Primitive_Size_Type: int
        ...
    class PhysXSolvent(helper):
        Particles_To_Particles: bool
        Particles_To_Deflectors: bool
        Particles_To_Ground: bool
        Limit_Solvent_By_List: bool
        Glue_Tests: MXSWrapperBase
        Limit_Solvent_By_Time: bool
        start: int
        stop: int
        Limit_Solvent_By_Data: bool
        Data_Channel: None
        Limit_Solvent_By_Icon: bool
        mode: int
        Icon_Shape: int
        icon_size: float
        Color_Coordinated: bool
        ...
    class PhysXSwitch(helper):
        Match_Position: bool
        Match_Speed: bool
        Position_Speed_Match_Type: int
        Position_Speed_Start: int
        Position_Speed_Stop: int
        Position_Speed_Active: bool
        Position_Speed_Sync_Type: int
        Use_Speed_Limit: bool
        Speed_Limit: float
        Match_Rotation: bool
        Match_Spin: bool
        Rotation_Spin_Match_Type: int
        Rotation_Spin_Start: int
        Rotation_Spin_Stop: int
        Rotation_Spin_Active: bool
        Rotation_Spin_Sync_Type: int
        Use_Spin_Limit: bool
        Spin_Limit: float
        Apply_Anti_Gravity: bool
        AntiGravity_Type: int
        AntiGravity_Start: int
        AntiGravity_Stop: int
        AntiGravity_Active: bool
        Anti_Gravity_Sync_Type: int
        Turn_Off_Simulation: bool
        Turn_Off_Simulation_Type: int
        Turn_Off_Start: int
        Turn_Off_Stop: int
        Turn_Off_Active: bool
        Turn_Off_Sync_Type: int
        ...
    class PhysXWorld(helper):
        Apply_Gravity: bool
        Gravity_Acceleration: float
        Ground_Collision_Plane: bool
        Set_World_Limits: bool
        Icon_Length: float
        Icon_Width: float
        Icon_Height: float
        Collision_Group: int
        Default_Restitution: float
        Default_Static_Friction: float
        Default_Dynamic_Friction: float
        Run_Baked_Simulation: bool
        Range_Type: int
        Range_Start: int
        Range_Finish: int
        Update_Viewports: bool
        Hide_Icon: bool
        Hide_Particle_Bindings: bool
        Show_Bake_Dialog: int
        Subframe_Factor: int
        Subframe_Type: int
        Use_Time_Scale: bool
        Time_Scale: float
        Energy_Threshold: float
        Speed_Threshold: float
        Spin_Rate_Threshold: float
        Sleep_Threshold_Type: int
        Bounce_Threshold: float
        Enable_Multi_Threading: bool
        Thread_Count: int
        Use_Hardware_PPU: bool
        Restricted_Broadphase: bool
        Safe_Mode_Simulation: bool
        Calculation_Limit: int
        ...
    class PhysX_Debug_Visualizer(UtilityPlugin):
        ...
    class PhysX_Shape_Convex(GeometryClass):
        ...
    class PhysX_World(helper):
        PhysX_World_Driver: None
        Suppress_Express_Save: bool
        PhysX_Driver_Type: int
        ...
    class PhysX_and_APEX_Exporter(ExporterPlugin):
        ...
    class Physical(camera):
        targeted: bool
        target_distance: float
        show_camera_cone: int
        horizon_on: bool
        show_focus_plane_in_cam_view: bool
        film_preset: str
        film_width_mm: float
        focal_length_mm: float
        specify_fov: bool
        fov: float
        zoom_factor: float
        f_number: float
        use_dof: bool
        specify_focus: int
        focus_distance: float
        lens_breathing_amount: float
        shutter_unit_type: int
        shutter_length_seconds: float
        shutter_offset_seconds: float
        shutter_length_frames: float
        shutter_offset_frames: float
        shutter_offset_enabled: bool
        motion_blur_enabled: bool
        exposure_gain_type: int
        iso: float
        exposure_value: float
        white_balance_type: int
        white_balance_illuminant: int
        white_balance_kelvin: float
        white_balance_custom: MXSWrapperBase
        vignetting_enabled: bool
        vignetting_amount: float
        bokeh_shape: int
        bokeh_blades_number: int
        pb_bokeh_blades_rotation_degrees: float
        bokeh_texture: None
        bokeh_texture_affect_exposure: bool
        bokeh_optical_vignetting: float
        bokeh_center_bias: float
        bokeh_anisotropy: float
        horizontal_shift: float
        vertical_shift: float
        horizontal_tilt_correction: float
        vertical_tilt_correction: float
        auto_vertical_tilt_correction: bool
        distortion_type: int
        distortion_cubic_amount: float
        distortion_texture: None
        clip_on: bool
        clip_near: float
        clip_far: float
        environment_near: float
        environment_far: float
        ...
    class PhysicalMaterial(material):
        material_mode: int
        base_weight: float
        base_color: MXSWrapperBase
        reflectivity: float
        roughness: float
        roughness_inv: bool
        metalness: float
        refl_color: MXSWrapperBase
        diff_roughness: float
        brdf_mode: bool
        brdf_low: float
        brdf_high: float
        brdf_curve: float
        anisotropy: float
        anisoangle: float
        aniso_mode: int
        aniso_channel: int
        transparency: float
        trans_color: MXSWrapperBase
        trans_depth: float
        trans_roughness: float
        trans_roughness_inv: bool
        trans_roughness_lock: bool
        trans_ior: float
        thin_walled: bool
        scattering: float
        sss_color: MXSWrapperBase
        sss_depth: float
        sss_scale: float
        sss_scatter_color: MXSWrapperBase
        emission: float
        emit_color: MXSWrapperBase
        emit_luminance: float
        emit_kelvin: float
        coating: float
        coat_color: MXSWrapperBase
        coat_roughness: float
        coat_roughness_inv: bool
        coat_affect_color: float
        coat_affect_roughness: float
        coat_ior: float
        base_weight_map: None
        base_color_map: None
        reflectivity_map: None
        refl_color_map: None
        roughness_map: None
        metalness_map: None
        diff_rough_map: None
        anisotropy_map: None
        aniso_angle_map: None
        transparency_map: None
        trans_color_map: None
        trans_rough_map: None
        trans_ior_map: None
        scattering_map: None
        sss_color_map: None
        sss_scale_map: None
        emission_map: None
        emit_color_map: None
        coat_map: None
        coat_color_map: None
        coat_rough_map: None
        bump_map: None
        coat_bump_map: None
        displacement_map: None
        cutout_map: None
        base_weight_map_on: bool
        base_color_map_on: bool
        reflectivity_map_on: bool
        refl_color_map_on: bool
        roughness_map_on: bool
        metalness_map_on: bool
        diff_rough_map_on: bool
        anisotropy_map_on: bool
        aniso_angle_map_on: bool
        transparency_map_on: bool
        trans_color_map_on: bool
        trans_rough_map_on: bool
        trans_ior_map_on: bool
        scattering_map_on: bool
        sss_color_map_on: bool
        sss_scale_map_on: bool
        emission_map_on: bool
        emit_color_map_on: bool
        coat_map_on: bool
        coat_color_map_on: bool
        coat_rough_map_on: bool
        bump_map_on: bool
        coat_bump_map_on: bool
        displacement_map_on: bool
        cutout_map_on: bool
        bump_map_amt: float
        clearcoat_bump_map_amt: float
        displacement_map_amt: float
        ...
    class PhysicalMaterialManager(GlobalUtilityPlugin):
        ...
    class PhysicalSunSkyEnv(textureMap):
        sun_position_object: None
        global_intensity: float
        haze: float
        sun_enabled: bool
        sun_disc_intensity: float
        sun_glow_intensity: float
        sun_disc_scale: float
        sun_disc_scale_percent: float
        sky_intensity: float
        night_color: MXSWrapperBase
        night_intensity: float
        horizon_height_deg: float
        horizon_blur_deg: float
        ground_color: MXSWrapperBase
        saturation: float
        tint: MXSWrapperBase
        illuminance_model: int
        perez_diffuse_horizontal_illuminance: float
        perez_direct_normal_illuminance: float
        ...
    class Physical_Camera(camera):
        targeted: bool
        target_distance: float
        show_camera_cone: int
        horizon_on: bool
        show_focus_plane_in_cam_view: bool
        film_preset: str
        film_width_mm: float
        focal_length_mm: float
        specify_fov: bool
        fov: float
        zoom_factor: float
        f_number: float
        use_dof: bool
        specify_focus: int
        focus_distance: float
        lens_breathing_amount: float
        shutter_unit_type: int
        shutter_length_seconds: float
        shutter_offset_seconds: float
        shutter_length_frames: float
        shutter_offset_frames: float
        shutter_offset_enabled: bool
        motion_blur_enabled: bool
        exposure_gain_type: int
        iso: float
        exposure_value: float
        white_balance_type: int
        white_balance_illuminant: int
        white_balance_kelvin: float
        white_balance_custom: MXSWrapperBase
        vignetting_enabled: bool
        vignetting_amount: float
        bokeh_shape: int
        bokeh_blades_number: int
        pb_bokeh_blades_rotation_degrees: float
        bokeh_texture: None
        bokeh_texture_affect_exposure: bool
        bokeh_optical_vignetting: float
        bokeh_center_bias: float
        bokeh_anisotropy: float
        horizontal_shift: float
        vertical_shift: float
        horizontal_tilt_correction: float
        vertical_tilt_correction: float
        auto_vertical_tilt_correction: bool
        distortion_type: int
        distortion_cubic_amount: float
        distortion_texture: None
        clip_on: bool
        clip_near: float
        clip_far: float
        environment_near: float
        environment_far: float
        ...
    class Physical_Camera_Exposure_Control(ToneOperator):
        Highlights: float
        midTones: float
        shadows: float
        saturation: float
        physical_scale_mode: int
        physical_scale: float
        use_physical_camera_controls: bool
        use_global_ev: int
        global_ev: float
        ev_compensation: float
        active: bool
        processBG: bool
        white_balance_type: int
        white_balance_illuminant: int
        white_balance_illuminant_colorpreview: MXSWrapperBase
        white_balance_kelvin: float
        white_balance_kelvin_colorpreview: MXSWrapperBase
        white_balance_custom: MXSWrapperBase
        vignetting_enabled: bool
        vignetting_amount: float
        ...
    class Physical_Material(material):
        material_mode: int
        base_weight: float
        base_color: MXSWrapperBase
        reflectivity: float
        roughness: float
        roughness_inv: bool
        metalness: float
        refl_color: MXSWrapperBase
        diff_roughness: float
        brdf_mode: bool
        brdf_low: float
        brdf_high: float
        brdf_curve: float
        anisotropy: float
        anisoangle: float
        aniso_mode: int
        aniso_channel: int
        transparency: float
        trans_color: MXSWrapperBase
        trans_depth: float
        trans_roughness: float
        trans_roughness_inv: bool
        trans_roughness_lock: bool
        trans_ior: float
        thin_walled: bool
        scattering: float
        sss_color: MXSWrapperBase
        sss_depth: float
        sss_scale: float
        sss_scatter_color: MXSWrapperBase
        emission: float
        emit_color: MXSWrapperBase
        emit_luminance: float
        emit_kelvin: float
        coating: float
        coat_color: MXSWrapperBase
        coat_roughness: float
        coat_roughness_inv: bool
        coat_affect_color: float
        coat_affect_roughness: float
        coat_ior: float
        base_weight_map: None
        base_color_map: None
        reflectivity_map: None
        refl_color_map: None
        roughness_map: None
        metalness_map: None
        diff_rough_map: None
        anisotropy_map: None
        aniso_angle_map: None
        transparency_map: None
        trans_color_map: None
        trans_rough_map: None
        trans_ior_map: None
        scattering_map: None
        sss_color_map: None
        sss_scale_map: None
        emission_map: None
        emit_color_map: None
        coat_map: None
        coat_color_map: None
        coat_rough_map: None
        bump_map: None
        coat_bump_map: None
        displacement_map: None
        cutout_map: None
        base_weight_map_on: bool
        base_color_map_on: bool
        reflectivity_map_on: bool
        refl_color_map_on: bool
        roughness_map_on: bool
        metalness_map_on: bool
        diff_rough_map_on: bool
        anisotropy_map_on: bool
        aniso_angle_map_on: bool
        transparency_map_on: bool
        trans_color_map_on: bool
        trans_rough_map_on: bool
        trans_ior_map_on: bool
        scattering_map_on: bool
        sss_color_map_on: bool
        sss_scale_map_on: bool
        emission_map_on: bool
        emit_color_map_on: bool
        coat_map_on: bool
        coat_color_map_on: bool
        coat_rough_map_on: bool
        bump_map_on: bool
        coat_bump_map_on: bool
        displacement_map_on: bool
        cutout_map_on: bool
        bump_map_amt: float
        clearcoat_bump_map_amt: float
        displacement_map_amt: float
        ...
    class Physical_Sun___Sky_Environment(textureMap):
        sun_position_object: None
        global_intensity: float
        haze: float
        sun_enabled: bool
        sun_disc_intensity: float
        sun_glow_intensity: float
        sun_disc_scale: float
        sun_disc_scale_percent: float
        sky_intensity: float
        night_color: MXSWrapperBase
        night_intensity: float
        horizon_height_deg: float
        horizon_blur_deg: float
        ground_color: MXSWrapperBase
        saturation: float
        tint: MXSWrapperBase
        illuminance_model: int
        perez_diffuse_horizontal_illuminance: float
        perez_direct_normal_illuminance: float
        ...
    class Physique(modifier):
        ...
    class PickerControl(RolloutControl):
        ...
    class Pipe(shape):
        ...
    class PipeReferenceTarget(ReferenceTarget):
        Data_Type: int
        Valve_Type: int
        Vector_Valve_Type: int
        Integer_Valve_Type: int
        Angle_Conditions: MXSWrapperBase
        Float_Conditions: MXSWrapperBase
        Integer_Conditions: MXSWrapperBase
        Percent_Conditions: MXSWrapperBase
        Time_Conditions: MXSWrapperBase
        World_Unit_Conditions: MXSWrapperBase
        Condition_Is_Rate: bool
        Units_Per_Type: int
        filter: None
        Input_Valve: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        Input_5: None
        Input_6: None
        Input_7: None
        Input_8: None
        ...
    class PivotPos(floatController):
        ...
    class PivotRot(floatController):
        ...
    class Pivoted(GeometryClass):
        height: float
        width: float
        depth: float
        Vertical_Rotation: bool
        Horizontal_Frame_Width: float
        Vertical_Frame_Width: float
        Frame_Thickness: float
        Glazing_Thickness: float
        Rail_Width: float
        Percent_Open: int
        Generate_Mapping_Coords: bool
        ...
    class PlacementTool(Interface):
        ...
    class Placement_Paint(helper):
        Particle_Paint_Helper: None
        Update_Type: int
        Acquire_Paint_Position: bool
        Position_Type: int
        Snap_If_Close: bool
        Snap_Distance: float
        Acquire_Paint_Rotation: bool
        BlendIn_Rotation: bool
        Near_Distance: float
        Far_Distance: float
        Acquire_Paint_Mapping: bool
        Acquire_Paint_MaterialID: bool
        Acquire_Paint_Selection: bool
        Selection_Type: int
        Order_Type: int
        Stop_If_Count_Overflow: bool
        Obey_Quantity_Multiplier: bool
        Separate_Streams_Indexing: bool
        Random_Seed: int
        ...
    class PlanarCollision(ReferenceMaker):
        ...
    class Plane(GeometryClass):
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInLength: float
        typeInWidth: float
        length: float
        width: float
        lengthsegs: int
        widthsegs: int
        density: float
        renderScale: float
        mapcoords: bool
        ...
    class PlaneAngleManip(helper):
        Origin: MXSWrapperBase
        NormalVec: MXSWrapperBase
        UpVec: MXSWrapperBase
        angle: float
        distance: float
        size: float
        ...
    class Plane_Angle(helper):
        Origin: MXSWrapperBase
        NormalVec: MXSWrapperBase
        UpVec: MXSWrapperBase
        angle: float
        distance: float
        size: float
        ...
    class Planet(textureMap):
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        color3: MXSWrapperBase
        color4: MXSWrapperBase
        color5: MXSWrapperBase
        color6: MXSWrapperBase
        color7: MXSWrapperBase
        color8: MXSWrapperBase
        continentSize: float
        islandFactor: float
        oceanPercent: float
        RandomSeed: int
        blendWaterLand: bool
        coords: MXSWrapperBase
        ...
    class Plate_Match_MAX_R2(filter):
        ...
    class Plug_in_Manager(GlobalUtilityPlugin):
        ...
    class PluginMarkerForBox3(ReferenceTarget):
        ...
    class PluginPackageManager(Interface):
        ...
    class Point(helper):
        size: float
        centermarker: bool
        axistripod: bool
        cross: bool
        Box: bool
        constantscreensize: bool
        drawontop: bool
        ...
    class Point2(Value):
        ...
    class Point2Controller(MAXWrapper):
        ...
    class Point3Layer(point3Controller):
        ...
    class Point3List(point3Controller):
        weight: MXSWrapperBase
        average: bool
        ...
    class Point3Reactor(point3Controller):
        ...
    class Point3Spring(point3Controller):
        ...
    class Point3XRefCtrl(point3Controller):
        ...
    class Point3_Expression(point3Controller):
        ...
    class Point3_Layer(point3Controller):
        ...
    class Point3_Mixer_Controller(point3Controller):
        ...
    class Point3_Motion_Capture(point3Controller):
        ...
    class Point3_Reactor(point3Controller):
        ...
    class Point3_Wire(point3Controller):
        ...
    class Point3_XRef_Controller(point3Controller):
        ...
    class Point3_XYZ(point3Controller):
        ...
    class Point4(Value):
        ...
    class Point4Layer(point4Controller):
        ...
    class Point4List(point4Controller):
        weight: MXSWrapperBase
        average: bool
        ...
    class Point4XRefCtrl(point4Controller):
        ...
    class Point4_Layer(point4Controller):
        ...
    class Point4_Mixer_Controller(point4Controller):
        ...
    class Point4_Wire(point4Controller):
        ...
    class Point4_XRef_Controller(point4Controller):
        ...
    class Point4_XYZW(point4Controller):
        ...
    class PointCache(modifier):
        filename: str
        recordStart: float
        recordEnd: float
        sampleRate: float
        strength: float
        relativeOffset: bool
        playbackType: int
        playbackStart: float
        playbackEnd: float
        playbackORTbefore: int
        playbackORTafter: int
        playbackFrame: float
        interpolationType: int
        applyMeshToSpline: bool
        preLoadCache: bool
        clampGraph: bool
        forceUncPath: bool
        loadType: int
        applyToWholeObject: bool
        loadTypeSlave: int
        fileCount: int
        ...
    class PointCacheWSM(SpacewarpModifier):
        filename: str
        recordStart: float
        recordEnd: float
        sampleRate: float
        strength: float
        relativeOffset: bool
        playbackType: int
        playbackStart: float
        playbackEnd: float
        playbackORTbefore: int
        playbackORTafter: int
        playbackFrame: float
        interpolationType: int
        applyMeshToSpline: bool
        preLoadCache: bool
        clampGraph: bool
        forceUncPath: bool
        loadType: int
        applyToWholeObject: bool
        loadTypeSlave: int
        fileCount: int
        ...
    class PointCloud(GeometryClass):
        filename: str
        scanFiles: MXSWrapperBase
        PtsVisible: MXSWrapperBase
        voxelSize: float
        asPixelPointSize: float
        realWorldScalePointSize: float
        pointSizeType: int
        displayTechnique: int
        singleColor: MXSWrapperBase
        gradientTexmap: MXSWrapperBase
        performanceQuality: int
        fixedLODEnable: bool
        fixedLODLevel: int
        enableLimitPlanes: bool
        GlobalEnableVolumes: bool
        GlobalInvertVolumes: bool
        VolumeObjects: MXSWrapperBase
        Shader: None
        ...
    class PointHelperObj(helper):
        size: float
        centermarker: bool
        axistripod: bool
        cross: bool
        Box: bool
        constantscreensize: bool
        drawontop: bool
        ...
    class PointPacket(ReferenceMaker):
        ...
    class PointSelection(Primitive):
        ...
    class Point_Cache(modifier):
        filename: str
        recordStart: float
        recordEnd: float
        sampleRate: float
        strength: float
        relativeOffset: bool
        playbackType: int
        playbackStart: float
        playbackEnd: float
        playbackORTbefore: int
        playbackORTafter: int
        playbackFrame: float
        interpolationType: int
        applyMeshToSpline: bool
        preLoadCache: bool
        clampGraph: bool
        forceUncPath: bool
        loadType: int
        applyToWholeObject: bool
        loadTypeSlave: int
        fileCount: int
        ...
    class Point_CacheSpacewarpModifier(SpacewarpModifier):
        filename: str
        recordStart: float
        recordEnd: float
        sampleRate: float
        strength: float
        relativeOffset: bool
        playbackType: int
        playbackStart: float
        playbackEnd: float
        playbackORTbefore: int
        playbackORTafter: int
        playbackFrame: float
        interpolationType: int
        applyMeshToSpline: bool
        preLoadCache: bool
        clampGraph: bool
        forceUncPath: bool
        loadType: int
        applyToWholeObject: bool
        loadTypeSlave: int
        fileCount: int
        ...
    class Point_Curve(shape):
        render_thickness: float
        render_sides: int
        render_angle: float
        sphere_cap: float
        cap_segments: int
        render_width: float
        render_length: float
        render_angle2: float
        render_threshold: float
        ...
    class Point_Curveshape(shape):
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
    class PolyMesh_Select(modifier):
        useSoftSelection: bool
        softselUseEdgeDistance: bool
        softselEdgeDist: int
        softselAffectBackfacing: bool
        softselFalloff: float
        softselPinch: float
        softselBubble: float
        lockSoftSel: bool
        paintselmode: int
        paintSelValue: float
        paintSelSize: float
        paintSelStrength: float
        byVertex: bool
        ignoreBackfacing: bool
        materialID: int
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
    class Poly_Select(modifier):
        useSoftSelection: bool
        softselUseEdgeDistance: bool
        softselEdgeDist: int
        softselAffectBackfacing: bool
        softselFalloff: float
        softselPinch: float
        softselBubble: float
        lockSoftSel: bool
        paintselmode: int
        paintSelValue: float
        paintSelSize: float
        paintSelStrength: float
        byVertex: bool
        ignoreBackfacing: bool
        materialID: int
        ...
    class Polygon_Counter(UtilityPlugin):
        ...
    class PolymorphicGeom(GeometryClass):
        ...
    class PolymorphicGeomshape(shape):
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
    class Populate(floatController):
        ...
    class PopupMenu(Primitive):
        ...
    class Portable_Network_Graphics(BitmapIO):
        ...
    class PositionLayer(positionController):
        ...
    class PositionList(positionController):
        weight: MXSWrapperBase
        average: bool
        ...
    class PositionManip(helper):
        ...
    class PositionReactor(positionController):
        ...
    class PositionSpring(positionController):
        effectHow: int
        forceNode: MXSWrapperBase
        steps: int
        x_effect: float
        y_effect: float
        z_effect: float
        start: int
        ...
    class PositionValueManip(helper):
        ...
    class Position_Constraint(positionController):
        weight: MXSWrapperBase
        relative: bool
        ...
    class Position_Expression(positionController):
        ...
    class Position_Icon(helper):
        Lock_On_Emitter: bool
        Inherit_Emitter_Movement: bool
        multiplier: float
        location: int
        Distinct_Points_Only: bool
        Total_Distinct_Points: int
        Subframe_Sampling: bool
        Random_Seed: int
        ...
    class Position_Layer(positionController):
        ...
    class Position_Manip(helper):
        ...
    class Position_Mixer_Controller(positionController):
        ...
    class Position_Motion_Capture(positionController):
        ...
    class Position_Object(helper):
        Lock_On_Emitter: bool
        Inherit_Emitter_Movement: bool
        multiplier: float
        variation: float
        Emitter_Objects: MXSWrapperBase
        Animated_Shape: bool
        Subframe_Sampling: bool
        location: int
        Use_Surface_Offset: bool
        Surface_Offset_Minimum: float
        Surface_Offset_Maximum: float
        Density_By_Emitter_Material: bool
        Density_Type: int
        Use_Sub_Material: bool
        Material_ID: int
        Apart_Placement: bool
        Apart_Distance: float
        Distinct_Points_Only: bool
        Total_Distinct_Points: int
        delete: bool
        Random_Seed: int
        Maximum_Number_Of_Attempts: int
        ...
    class Position_Reactor(positionController):
        ...
    class Position_Value(helper):
        ...
    class Position_Wire(positionController):
        ...
    class Position_XYZ(positionController):
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
    class Preserve(modifier):
        iterations: int
        Edge_Length_Weight: float
        Face_Angle_Weight: float
        Volume_Weight: float
        Apply_to_Whole_Mesh: int
        Selected_Verts_Only: int
        Invert_Selection: int
        ...
    class PresetDummyOperIcon(helper):
        ...
    class PresetDummyOperator(helper):
        ...
    class PresetDummyTest(helper):
        ...
    class PresetFlow(ReferenceTarget):
        ...
    class PresetOperIcon(helper):
        Icon_Type: int
        Icon_Parameter_1: float
        Icon_Parameter_2: float
        Icon_Parameter_3: float
        Color_Coordinated: bool
        Auto_Update: bool
        SubOperators: MXSWrapperBase
        Selected_SubOperators: MXSWrapperBase
        groups: MXSWrapperBase
        Enable_By_Switch: bool
        Default_Width: int
        Default_Offset: int
        Default_Height: int
        Default_Range_Type: int
        Default_Range_Min: float
        Default_Range_Max: float
        Activity_Type: int
        Time_On: int
        Time_Off: int
        Animatable_Active: bool
        PDView_Origin_X: int
        PDView_Origin_Y: int
        PDView_Width: int
        PDView_Height: int
        PDView_Divider: int
        PDView_Show_Depot: bool
        PDView_Description_Type: int
        PDView_Show_Parameters: bool
        Use_Dynamic_Names_For_New: bool
        Auto_Update_On_Data_View_Close: bool
        Repeats: int
        ...
    class PresetOperator(helper):
        Icon_Type: int
        Icon_Parameter_1: float
        Icon_Parameter_2: float
        Icon_Parameter_3: float
        Color_Coordinated: bool
        Auto_Update: bool
        SubOperators: MXSWrapperBase
        Selected_SubOperators: MXSWrapperBase
        groups: MXSWrapperBase
        Enable_By_Switch: bool
        Default_Width: int
        Default_Offset: int
        Default_Height: int
        Default_Range_Type: int
        Default_Range_Min: float
        Default_Range_Max: float
        Activity_Type: int
        Time_On: int
        Time_Off: int
        Animatable_Active: bool
        PDView_Origin_X: int
        PDView_Origin_Y: int
        PDView_Width: int
        PDView_Height: int
        PDView_Divider: int
        PDView_Show_Depot: bool
        PDView_Description_Type: int
        PDView_Show_Parameters: bool
        Use_Dynamic_Names_For_New: bool
        Auto_Update_On_Data_View_Close: bool
        Repeats: int
        ...
    class PresetTest(helper):
        Icon_Type: int
        Icon_Parameter_1: float
        Icon_Parameter_2: float
        Icon_Parameter_3: float
        Color_Coordinated: bool
        Auto_Update: bool
        SubOperators: MXSWrapperBase
        Selected_SubOperators: MXSWrapperBase
        groups: MXSWrapperBase
        Enable_By_Switch: bool
        Default_Width: int
        Default_Offset: int
        Default_Height: int
        Default_Range_Type: int
        Default_Range_Min: float
        Default_Range_Max: float
        Activity_Type: int
        Time_On: int
        Time_Off: int
        Animatable_Active: bool
        PDView_Origin_X: int
        PDView_Origin_Y: int
        PDView_Width: int
        PDView_Height: int
        PDView_Divider: int
        PDView_Show_Depot: bool
        PDView_Description_Type: int
        PDView_Show_Parameters: bool
        Use_Dynamic_Names_For_New: bool
        Auto_Update_On_Data_View_Close: bool
        Repeats: int
        ...
    class PresetTestIcon(helper):
        Icon_Type: int
        Icon_Parameter_1: float
        Icon_Parameter_2: float
        Icon_Parameter_3: float
        Color_Coordinated: bool
        Auto_Update: bool
        SubOperators: MXSWrapperBase
        Selected_SubOperators: MXSWrapperBase
        groups: MXSWrapperBase
        Enable_By_Switch: bool
        Default_Width: int
        Default_Offset: int
        Default_Height: int
        Default_Range_Type: int
        Default_Range_Min: float
        Default_Range_Max: float
        Activity_Type: int
        Time_On: int
        Time_Off: int
        Animatable_Active: bool
        PDView_Origin_X: int
        PDView_Origin_Y: int
        PDView_Width: int
        PDView_Height: int
        PDView_Divider: int
        PDView_Show_Depot: bool
        PDView_Description_Type: int
        PDView_Show_Parameters: bool
        Use_Dynamic_Names_For_New: bool
        Auto_Update_On_Data_View_Close: bool
        Repeats: int
        ...
    class Preset_Flow(ReferenceTarget):
        ...
    class Preset_Maker(modifier):
        ...
    class Primitive(Value):
        ...
    class Priority(ReferenceTarget):
        start: int
        delegates: MXSWrapperBase
        object: None
        grid: None
        increment: int
        showPriorities: bool
        showStartFrames: bool
        ...
    class Prism(GeometryClass):
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInSide1Length: float
        typeInSide2Length: float
        typeInSide3Length: float
        typeInHeight: float
        side1Length: float
        side2Length: float
        side3Length: float
        height: float
        side1Segs: int
        side2Segs: int
        side3Segs: int
        heightsegs: int
        mapcoords: bool
        ...
    class ProBoolObj(GeometryClass):
        ...
    class ProBoolean(GeometryClass):
        ...
    class ProCutter(GeometryClass):
        ...
    class ProOptimizer(modifier):
        vertexPercent: float
        vertexCount: int
        Calculate: bool
        OptimizationMode: int
        LockMat: bool
        KeepUV: bool
        LockUV: bool
        ToleranceUV: float
        KeepVC: bool
        LockVC: bool
        ToleranceVC: int
        KeepNormals: bool
        NormalMode: int
        NormalThreshold: float
        MergePoints: bool
        MergePointsThreshold: float
        MergeFaces: bool
        MergeFacesAngle: float
        PreserveSelection: bool
        InvertSelection: bool
        SymmetryMode: int
        SymmetryTolerance: float
        CompactFaces: bool
        PreventFlip: bool
        LockPoints: bool
        ...
    class ProSound(SoundClass):
        ...
    class Project_Mapping(ReferenceTarget):
        ...
    class Project_Mapping_Holder(modifier):
        ...
    class Projection(modifier):
        ignoreBackfacing: bool
        materialID: int
        smoothGroup: int
        mapChannel: int
        clearSelection: bool
        useSoftSelection: bool
        softselUseEdgeDistance: bool
        softselEdgeDist: int
        softselAffectBackfacing: bool
        softselFalloff: float
        softselPinch: float
        softselBubble: float
        displayCage: bool
        displayCageShaded: bool
        displayCageOffset: bool
        pushValue: float
        pushPercent: float
        autoWrapTolerance: float
        autoWrapAlwaysUpdate: bool
        geomNames: MXSWrapperBase
        selLevels: MXSWrapperBase
        mapProportions: MXSWrapperBase
        IDs: MXSWrapperBase
        geomNodes: MXSWrapperBase
        geomNodeIDs: MXSWrapperBase
        geomNodeVisible: MXSWrapperBase
        displayToggleEnable: bool
        displayToggleMode: int
        projectionTypes: MXSWrapperBase
        selectionCheckType: int
        selectionCheckSelFaces: bool
        ...
    class ProjectionHolderUVW(modifier):
        ...
    class ProjectionIntersectorMgr(Interface):
        ...
    class ProjectionMod(modifier):
        ignoreBackfacing: bool
        materialID: int
        smoothGroup: int
        mapChannel: int
        clearSelection: bool
        useSoftSelection: bool
        softselUseEdgeDistance: bool
        softselEdgeDist: int
        softselAffectBackfacing: bool
        softselFalloff: float
        softselPinch: float
        softselBubble: float
        displayCage: bool
        displayCageShaded: bool
        displayCageOffset: bool
        pushValue: float
        pushPercent: float
        autoWrapTolerance: float
        autoWrapAlwaysUpdate: bool
        geomNames: MXSWrapperBase
        selLevels: MXSWrapperBase
        mapProportions: MXSWrapperBase
        IDs: MXSWrapperBase
        geomNodes: MXSWrapperBase
        geomNodeIDs: MXSWrapperBase
        geomNodeVisible: MXSWrapperBase
        displayToggleEnable: bool
        displayToggleMode: int
        projectionTypes: MXSWrapperBase
        selectionCheckType: int
        selectionCheckSelFaces: bool
        ...
    class ProjectionModTypeUVW(ReferenceTarget):
        ...
    class ProjectionRenderMgr(Interface):
        ...
    class PromptForNameRollout(RolloutClass):
        ...
    class Protractor(helper):
        ...
    class ProxSensor(helper):
        ...
    class PseudoColorManager(Interface):
        ...
    class Pseudo_Color_Exposure_Control(ToneOperator):
        minimum: float
        maximum: float
        quantity: int
        display: int
        physicalScale: float
        automatic: bool
        scaleFunction: int
        unitSystemUsed: int
        active: bool
        processBG: bool
        ...
    class Publish(modifier):
        ...
    class Push(modifier):
        Push_Value: float
        ...
    class PushMod(SpacewarpModifier):
        ...
    class PushPrompt(Primitive):
        ...
    class PushQtTranslationFromFile(Primitive):
        ...
    class PushSpaceWarp(SpacewarpObject):
        units: int
        icon_size: float
        Basic_Force: float
        Target_Speed: float
        On_Time: MXSWrapperBase
        Off_Time: MXSWrapperBase
        Feedback_On: int
        Reversible: int
        Control_Gain: float
        Enable_Variation: int
        Variation_Period_1: MXSWrapperBase
        Amplitude_1: float
        Variation_Phase_1: float
        Variation_Period_2: MXSWrapperBase
        Amplitude_2: float
        Variation_Phase_2: float
        Range_Enable: int
        Range_Value: float
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
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInWidth: float
        typeInDepth: float
        typeInHeight: float
        width: float
        depth: float
        height: float
        widthsegs: int
        depthSegs: int
        heightsegs: int
        mapcoords: bool
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
    class QuadMesh(modifier):
        quadsize: float
        ...
    class Quadify_Mesh(modifier):
        quadsize: float
        ...
    class Quadratic(filter):
        ...
    class QuarterRound(shape):
        ...
    class Quat(Value):
        ...
    class Quicksilver_Hardware_Renderer(RendererClass):
        ...
    class RAMPlayer(Primitive):
        ...
    class RCMenu(Value):
        ...
    class RElements2cws(MAXScriptFunction):
        ...
    class RGB_Multiply(textureMap):
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1: None
        map2: None
        map1Enabled: bool
        map2Enabled: bool
        alphaFrom: int
        ...
    class RGB_Tint(textureMap):
        red: MXSWrapperBase
        green: MXSWrapperBase
        blue: MXSWrapperBase
        map1: None
        map1Enabled: bool
        ...
    class RLA(BitmapIO):
        ...
    class RPF(BitmapIO):
        ...
    class RadioControl(RolloutControl):
        ...
    class Radiosity(RadiosityEffect):
        radInitialQuality: float
        radGlobalRefineSteps: int
        radSelectionRefineSteps: int
        radFiltering: int
        radProcessObjectRefineSteps: bool
        radDisplayInViewport: bool
        radProcessInRenderOnly: bool
        radDirectFiltering: int
        meshingEnabled: bool
        meshingSize: float
        useAdaptiveMeshing: bool
        minimumMeshSize: float
        initialMeshSize: float
        contrastThreshold: float
        includePointLights: bool
        includeLinearLights: bool
        includeAreaLights: bool
        includeSelfEmittingLights: bool
        shootDirectLights: bool
        includeSkylight: bool
        minimumSelfEmittingSize: float
        lightPaintingIntensity: float
        lightPaintingPressure: float
        lightUnitsUsed: int
        rmRegather: bool
        rmReuseDirectIllumination: bool
        rmRaysPerSample: int
        rmFilterRadius: float
        rmClampEnabled: bool
        rmClampValue: float
        rmAdaptiveEnabled: bool
        rmSampleSpacing: int
        rmMinSampleSpacing: int
        rmSubdivisionContrast: float
        rmShowSamples: bool
        statNumFaces: int
        statRefineIterations: int
        statSolutionQuality: float
        statNumGeomObjects: int
        statNumLightObjects: int
        statMeshSize: float
        elapsedTime: int
        ...
    class RadiosityEffect(MAXWrapper):
        ...
    class RadiosityPreferences(Interface):
        ...
    class Radiosity_Override(material):
        reflectanceScale: float
        colorBleed: float
        transmittanceScale: float
        luminanceScale: float
        bumpScale: float
        baseMaterial: MXSWrapperBase
        ...
    class RagdollHelper(helper):
        ...
    class RagdollVisualizer(helper):
        ...
    class Railing(GeometryClass):
        Top_Rail_Depth: float
        Top_Rail_Width: float
        Top_surface_of_Top_Rail_Height: float
        Railing_Length: float
        Top_Rail_Profile: int
        Lower_Rail_Depth: float
        Lower_Rail_Width: float
        Lowest_Rail_Height: float
        Lower_Rail_Spacing: float
        Number_of_Lower_Rails: int
        Top_Rail_Spacing_to_Next_Rail: float
        Lower_Rail_Profile: int
        Post_Depth: float
        Post_Width: float
        First_Post_Offset: float
        Post_Spacing: float
        Number_of_Posts: int
        Posts_oriented_with_curved_Railing: bool
        Last_Post_Offset: float
        Post_Extension_beyond_bottom_of_Top_Rail: float
        Post_Profile: int
        Fencing_Type: int
        Picket_Depth: float
        Picket_Width: float
        First_Picket_Offset: float
        Picket_Spacing: float
        Number_of_Pickets_between_each_pair_of_Posts: int
        Pickets_oriented_with_curved_Railing: bool
        Last_Picket_Spacing_to_Post: float
        Picket_Profile: int
        Picket_Extension_beyond_bottom_of_Top_Rail: float
        Picket_Bottom_Offset: float
        Fill_Thickness: float
        Fill_Top_Offset: float
        Fill_Bottom_Offset: float
        Fill_Left_Offset: float
        Fill_Right_Offset: float
        Texture_Mapped: bool
        Number_of_segments_between_each_pair_of_Posts: int
        Respect_Path_Corners_in_rails: bool
        ...
    class RandomWalk(helper):
        ...
    class Randomize_Keys(trackViewUtility):
        ...
    class RapidRT_Noise_Filter(RenderElement):
        elementName: str
        enabled: bool
        bitmap: bool
        strength: float
        strength_percentage: float
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
        nodeList: MXSWrapperBase
        ...
    class Ray_Element(ReferenceTarget):
        elementName: str
        size: float
        intensity: float
        angle: float
        Number: int
        sharpness: float
        on: bool
        objectsHide: bool
        Squeeze: bool
        occlusion: float
        colorSource: float
        centerColor: MXSWrapperBase
        edgeColor: MXSWrapperBase
        radialMtl: None
        useRadialMtl: bool
        radialMap: None
        useRadialMap: bool
        circularColorMix: float
        quadrant1Color: MXSWrapperBase
        quadrant2Color: MXSWrapperBase
        quadrant3Color: MXSWrapperBase
        quadrant4Color: MXSWrapperBase
        circularMtl: None
        useCircularMtl: bool
        circularMap: None
        useCircularMap: bool
        radialSizeMap: None
        useRadialSizeMap: bool
        applyLights: bool
        applyImage: bool
        applyImageCenters: bool
        sourceObjectID: bool
        objectID: int
        sourceEffectsID: bool
        effectsID: int
        sourceUnclampedColor: bool
        unclampedColor: float
        unclampedColorInvert: bool
        sourceSurfaceNormal: bool
        surfaceNormal: float
        surfaceNormalInvert: bool
        sourceWhole: bool
        sourceAlpha: bool
        alpha: int
        sourceZBuffer: bool
        zHi: float
        zLo: float
        filterAll: bool
        filterEdge: bool
        filterPerimeterAlpha: bool
        filterPerimeter: bool
        filterBrightness: bool
        brightness: int
        brightnessInvert: bool
        filterHue: bool
        hue: MXSWrapperBase
        hueRange: int
        applyNoise: bool
        noiseMap: None
        radialDensity: None
        useRadialDensity: bool
        ...
    class Ray_Engine(ReferenceTarget):
        ...
    class Raytrace(textureMap):
        ...
    class RaytraceGlobalSettings(ReferenceTarget):
        excludeList: MXSWrapperBase
        includeList: None
        showMessages: bool
        showProgressDlg: bool
        max_levels_specify_color: MXSWrapperBase
        adaptive_antialiasing_enable_flag: bool
        adaptive_antialiasing_threshold: float
        antialiasing_minimum_rays_to_fire: int
        antialiasing_maximum_rays_to_fire: int
        blurring_amount: float
        blurring_aspect_ratio: float
        defocusing_amount: float
        defocusing_aspect_ratio: float
        vox_maxdepth: int
        vox_previs: float
        vox_dim: int
        vox_face_limit: int
        enable_raytracing: bool
        enable_antialiasing: bool
        enable_self_reflect_refract: bool
        enable_atmosphere: bool
        enable_objects_in_raytrace_objects: bool
        enable_atmosphere_in_raytrace_objects: bool
        enable_refract_special_effects: bool
        enable_material_id_rendering_support: bool
        adaptive_ray_depth_threshold: float
        max_ray_depth: int
        max_levels_color_mode: int
        ...
    class RaytraceMaterial(material):
        effectsChannel: int
        ambientMap: None
        diffuseMap: None
        specularMap: None
        bumpMap: None
        reflectionMap: None
        displacementMap: None
        ambientMapAmount: float
        diffuseMapAmount: float
        specularMapAmount: float
        bumpMapAmount: float
        reflectionMapAmount: float
        displacementMapAmount: float
        ambientMapEnable: bool
        diffuseMapEnable: bool
        specularMapEnable: bool
        bumpMapEnable: bool
        reflectionMapEnable: bool
        displacementMapEnable: bool
        glossinessMap: None
        glossinessMapEnable: bool
        glossinessMapAmount: float
        specularLevelMap: None
        specularLevelMapEnable: bool
        specularLevelMapAmount: float
        luminosityMap: None
        luminosityMapEnable: bool
        luminosityMapAmount: float
        transparencyMap: None
        transparencyMapEnable: bool
        transparencyMapAmount: float
        environmentMap: None
        environmentMapEnable: bool
        environmentMapAmount: float
        transEnvMap: None
        transEnvMapEnable: bool
        transEnvMapAmount: float
        iorMap: None
        iorMapEnable: bool
        iorMapAmount: float
        translucencyMap: None
        translucencyMapEnable: bool
        translucencyMapAmount: float
        extraLightingMap: None
        extraLightingMapEnable: bool
        extraLightingMapAmount: float
        fluorescenceMap: None
        fluorescenceMapEnable: bool
        fluorescenceMapAmount: float
        colorDensityMap: None
        colorDensityMapEnable: bool
        colorDensityMapAmount: float
        fogColorMap: None
        fogColorMapEnable: bool
        fogColorMapAmount: float
        diffusionMap: None
        diffusionMapEnable: bool
        diffusionMapAmount: float
        Soften: float
        Diffuse: MXSWrapperBase
        shaderType: int
        shaderByName: str
        wire: bool
        twoSided: bool
        faceMap: bool
        supersample: bool
        wireUnits: int
        glossiness: float
        fog_color: MXSWrapperBase
        anisotropy: float
        orientation: float
        translucency: MXSWrapperBase
        ambient: MXSWrapperBase
        Ambient_Amount: float
        Ambient_Color_On: bool
        Reflect: MXSWrapperBase
        Reflect_amount: float
        Reflect_Color_On: int
        Luminosity: MXSWrapperBase
        Self_Illum_Amount: float
        Luminosity_Color_On: bool
        Transparecy: MXSWrapperBase
        Transparency_Amount: float
        Transparency_Color_On: bool
        Index_of_Refraction: float
        Spec__Color: MXSWrapperBase
        Specular_Level: float
        Extra_Lighting: MXSWrapperBase
        Fluorescence: MXSWrapperBase
        Fluorescence_Bias: float
        Wire_Size: float
        Color_Density_Color: MXSWrapperBase
        Color_Density_Enable: bool
        Color_Density_Start: float
        Color_Density_End: float
        Color_Density_Amount: float
        Fog_Enable: bool
        Fog_Start: float
        Fog_End: float
        Fog_Amount: float
        Reflection_Type: int
        Reflection_Gain: float
        Enable_Raytraced_Reflections: bool
        Enable_Raytraced_Refractions: bool
        Reflection_Falloff_Mode: int
        Reflection_Falloff_End_Distance: float
        Refraction_Falloff_Mode: int
        Refraction_Falloff_End_Distance: float
        Enable_Reflection_Falloff: bool
        Reflection_Falloff_Distance: float
        Enable_Refraction_Falloff: bool
        Refraction_Falloff_Distance: float
        Bump_Map_Effect: float
        Override_Global_Antialiasing_Settings: bool
        Adaptive_Antialiasing_On: bool
        Local_Min__Rays: int
        Local_Max__Rays: int
        Local_Threshold: float
        Local_Blur_Offset: float
        Local_Blur_Aspect: float
        Local_Defocus: float
        Local_Defocus_Aspect: float
        Blur_Map: bool
        Defocus_Map: bool
        Options___Raytracer_Enable: bool
        Options___Antialiasing_Enable: bool
        Options___Self_Reflect_Refract: bool
        Options___Raytrace_Atmospherics: bool
        Options___Reflect_Refract_Material_ID_s: bool
        Options___Raytrace_Objects_in_Glass: bool
        Options___Raytrace_Atmospherics_in_Glass: bool
        Options___Color_Density___Fog_Enable: bool
        Attenuation_Start: float
        Attenuation_Exponent: float
        Attenuation_Near: float
        Attenuation_Control_1: float
        Attenuation_Control_2: float
        Attenuation_Far: float
        Attenuation_Color_Mode: int
        Attenuation_Color: MXSWrapperBase
        Bounce_Coefficient: float
        Sliding_Friction: float
        Static_Friction: float
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
    class ReactorAngleManip(helper):
        ...
    class Reactor_Angle_Manip(helper):
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
    class Rectangle(shape):
        length: float
        steps: int
        width: float
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        cornerRadius: float
        ...
    class RefTargContainer(ReferenceTarget):
        ...
    class RefTargMonitor(ReferenceTarget):
        ...
    class ReferenceMaker(MAXWrapper):
        ...
    class ReferenceTarget(MAXWrapper):
        ...
    class Reflect_Refract(textureMap):
        size: int
        blur: float
        blurOffset: float
        near: float
        far: float
        source: int
        useAtmosphericMap: bool
        apply: bool
        frametype: int
        nthframe: int
        bitmapName: MXSWrapperBase
        outputname: None
        ...
    class Reflection(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class ReflectionFragment(GraphicsFragmentPlugin):
        ...
    class Refraction(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class Relax(modifier):
        iterations: int
        Relax_Value: float
        Keep_Boundary_Pts_Fixed: int
        ...
    class RemoveDictValue(Primitive):
        ...
    class RemoveSubRollout(Primitive):
        ...
    class RemoveTempPrompt(Primitive):
        ...
    class RendSpline(modifier):
        thickness: float
        viewport_thickness: float
        sides: int
        viewport_sides: int
        angle: float
        viewport_angle: float
        renderable: bool
        mapcoords: bool
        displayRenderSettings: bool
        useViewportSettings: bool
        ViewportOrRender: int
        SymmetricalOrRectangular: int
        width: float
        length: float
        Angle2: float
        LockAspect: bool
        Viewport_SymmetricalOrRectangular: int
        Viewport_Width: float
        Viewport_Length: float
        Viewport_Angle2: float
        Viewport_LockAspect: bool
        autosmooth: bool
        threshold: float
        twist_correction: bool
        cap: bool
        quad_cap: bool
        cap_segments: int
        sphere_cap: float
        ...
    class RenderElement(MAXWrapper):
        ...
    class RenderElementMgr(ReferenceTarget):
        ...
    class RenderEnhancements(Interface):
        ...
    class RenderEnvironment(atmospheric):
        ...
    class RenderParticles(helper):
        type: int
        visible: float
        Split_Type: int
        Mesh_Count: int
        Particles_Per_Mesh: int
        ...
    class Renderable_Spline(modifier):
        thickness: float
        viewport_thickness: float
        sides: int
        viewport_sides: int
        angle: float
        viewport_angle: float
        renderable: bool
        mapcoords: bool
        displayRenderSettings: bool
        useViewportSettings: bool
        ViewportOrRender: int
        SymmetricalOrRectangular: int
        width: float
        length: float
        Angle2: float
        LockAspect: bool
        Viewport_SymmetricalOrRectangular: int
        Viewport_Width: float
        Viewport_Length: float
        Viewport_Angle2: float
        Viewport_LockAspect: bool
        autosmooth: bool
        threshold: float
        twist_correction: bool
        cap: bool
        quad_cap: bool
        cap_segments: int
        sphere_cap: float
        ...
    class RendererClass(MAXWrapper):
        ...
    class RepelBehavior(ReferenceTarget):
        name: str
        repulsionSources: MXSWrapperBase
        targetComp: int
        repelMethod: int
        useRadii: bool
        innerRadius: float
        outerRadius: float
        falloff: float
        showRadii: bool
        forceColor: MXSWrapperBase
        displayForce: bool
        ...
    class Repel_Behavior(ReferenceTarget):
        name: str
        repulsionSources: MXSWrapperBase
        targetComp: int
        repelMethod: int
        useRadii: bool
        innerRadius: float
        outerRadius: float
        falloff: float
        showRadii: bool
        forceColor: MXSWrapperBase
        displayForce: bool
        ...
    class ReplacePrompt(Primitive):
        ...
    class RescaleWorldUnits(Primitive):
        ...
    class Rescale_World_Units(UtilityPlugin):
        ...
    class Reservoir(floatController):
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
    class Retimer(floatController):
        ...
    class RetimerCtrl(floatController):
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
    class Revit_importer(ImporterPlugin):
        ...
    class RingArray(Interface):
        ...
    class RingWave(GeometryClass):
        Time_On: int
        time_growing: int
        Display_Until: int
        Repeats: int
        max_diameter: float
        ring_width: float
        ring_segments: int
        Outer_Edge_Breakup: bool
        Major_Cycles_Outer: int
        Major_Cycle_Flux_Outer: float
        Major_Cycle_Flux_Per_Outer: int
        Minor_Cycles_Outer: int
        Minor_Cycle_Flux_Outer: float
        Minor_Cycle_Flux_Per_Outer: int
        Inner_Edge_Breakup: bool
        Major_Cycles_Inner: int
        Major_Cycle_Flux_Inner: float
        Major_Cycle_Flux_Per_Inner: int
        Minor_Cycles_Inner: int
        Minor_Cycle_Flux_Inner: float
        Minor_Cycle_Flux_Per_Inner: int
        height: float
        Height_Segs: int
        Radius_Segs: int
        Mapping_Coords: bool
        Smoothing: bool
        ...
    class Ring_Array(System):
        ...
    class Ring_Element(ReferenceTarget):
        elementName: str
        size: float
        intensity: float
        Plane: float
        thickness: float
        on: bool
        objectsHide: bool
        Squeeze: bool
        occlusion: float
        colorSource: float
        centerColor: MXSWrapperBase
        edgeColor: MXSWrapperBase
        radialMtl: None
        useRadialMtl: bool
        radialMap: None
        useRadialMap: bool
        circularColorMix: float
        quadrant1Color: MXSWrapperBase
        quadrant2Color: MXSWrapperBase
        quadrant3Color: MXSWrapperBase
        quadrant4Color: MXSWrapperBase
        circularMtl: None
        useCircularMtl: bool
        circularMap: None
        useCircularMap: bool
        radialSizeMap: None
        useRadialSizeMap: bool
        applyLights: bool
        applyImage: bool
        applyImageCenters: bool
        sourceObjectID: bool
        objectID: int
        sourceEffectsID: bool
        effectsID: int
        sourceUnclampedColor: bool
        unclampedColor: float
        unclampedColorInvert: bool
        sourceSurfaceNormal: bool
        surfaceNormal: float
        surfaceNormalInvert: bool
        sourceWhole: bool
        sourceAlpha: bool
        alpha: int
        sourceZBuffer: bool
        zHi: float
        zLo: float
        filterAll: bool
        filterEdge: bool
        filterPerimeterAlpha: bool
        filterPerimeter: bool
        filterBrightness: bool
        brightness: int
        brightnessInvert: bool
        filterHue: bool
        hue: MXSWrapperBase
        hueRange: int
        applyNoise: bool
        noiseMap: None
        radialDensity: None
        useRadialDensity: bool
        ...
    class Ripple(modifier):
        amplitude1: float
        amplitude2: float
        wavelength: float
        phase: float
        decay: float
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
    class RootNodeClass(node):
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
    class RotationLayer(rotationController):
        ...
    class RotationList(rotationController):
        weight: MXSWrapperBase
        average: bool
        ...
    class RotationReactor(rotationController):
        ...
    class Rotation_Layer(rotationController):
        ...
    class Rotation_Mixer_Controller(rotationController):
        ...
    class Rotation_Motion_Capture(rotationController):
        ...
    class Rotation_Reactor(rotationController):
        ...
    class Rotation_Wire(rotationController):
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
        Bounce: float
        bounceVar: float
        chaos: float
        radius: float
        inheritVelocity: float
        friction: float
        ...
    class SLAP(renderEffect):
        ...
    class SME(Interface):
        ...
    class SMEGUP(GlobalUtilityPlugin):
        ...
    class SOmniFlect(SpacewarpObject):
        timeOn: MXSWrapperBase
        timeOff: MXSWrapperBase
        affects: float
        Bounce: float
        bounceVar: float
        chaos: float
        inheritVelocity: float
        refracts: float
        deceleration: float
        decelVar: float
        Refraction: float
        refractionVar: float
        diffusion: float
        diffusionVar: float
        radius: float
        Spawn: float
        passVelocity: float
        passVelocityVar: float
        friction: float
        ...
    class SOmniFlectMod(SpacewarpModifier):
        ...
    class STL_Check(modifier):
        Material_ID: int
        Select_Faces: int
        Check_Now: int
        Change_MatID: int
        Selection_Type: int
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
        Output_Type: int
        Angle_Value: float
        Angle_Variation: float
        Boolean_Value: int
        Float_Value: float
        Float_Variation: float
        Integer_Value: int
        Integer_Variation: int
        Percent_Value: float
        Percent_Variation: float
        Time_Value: int
        Time_Variation: int
        World_Value: float
        World_Variation: float
        Use_As_Speed_Or_Spin_Rate: bool
        Use_For_Time_Related_Addition: bool
        Use_For_Time_Related_Multiplication: bool
        Units_Per_Type: int
        Sync_Type: int
        Random_Seed: int
        Use_E1: bool
        Use_E2: bool
        Use_E3: bool
        Use_E4: bool
        Use_As_Acceleration: bool
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        ...
    class ScaleLayer(scaleController):
        ...
    class ScaleList(scaleController):
        weight: MXSWrapperBase
        average: bool
        ...
    class ScaleMatrix(Primitive):
        ...
    class ScaleParticles(helper):
        type: int
        X_Scale_Factor: float
        Y_Scale_Factor: float
        Z_Scale_Factor: float
        Constrain_Scale: bool
        X_Scale_Variation: float
        Y_Scale_Variation: float
        Z_Scale_Variation: float
        Constrain_Scale_Variation: bool
        bias: int
        Sync_Type: int
        Random_Seed: int
        ...
    class ScaleReactor(scaleController):
        ...
    class ScaleXYZ(scaleController):
        ...
    class Scale_Expression(scaleController):
        ...
    class Scale_Layer(scaleController):
        ...
    class Scale_Mixer_Controller(scaleController):
        ...
    class Scale_Motion_Capture(scaleController):
        ...
    class Scale_Reactor(scaleController):
        ...
    class Scale_Test(helper):
        Test_Type: int
        Axis_Type: int
        Condition_Type: int
        Size_Value: float
        Size_Variation: float
        Scale_Value: float
        Scale_Variation: float
        Sync_Type: int
        Random_Seed: int
        ...
    class Scale_Wire(scaleController):
        ...
    class Scatter(GeometryClass):
        ...
    class ScatterReferenceTarget(ReferenceTarget):
        cloneObject: None
        numClones: int
        cloneType: int
        cloneHierarchy: bool
        cloneControllers: bool
        positionSpace: int
        surfaceOffset: float
        positionObject: None
        centerX: float
        centerY: float
        centerZ: float
        radius: float
        xyPlane: bool
        childBbox: bool
        spacing: float
        positionSeed: int
        incPositionSeed: bool
        forwardAxis: int
        UpAxis: int
        forwardAxisSign: bool
        UpAxisSign: bool
        lookFrom: int
        lookFromObject: None
        lookTowards: int
        lookAtTarget: None
        sideDeviation: float
        upDownDeviation: float
        rotationSeed: int
        incRotationSeed: bool
        xScale: float
        xScaleDeviation: float
        matchXtoYscale: bool
        matchXtoZscale: bool
        yScale: float
        yScaleDeviation: float
        matchYtoXscale: bool
        matchYtoZscale: bool
        zScale: float
        zScaleDeviation: float
        matchZtoXScale: bool
        matchZtoYScale: bool
        scaleSeed: int
        incScaleSeed: bool
        ComputeClones: bool
        ComputePositions: bool
        ComputeRotations: bool
        ComputeScales: bool
        IncPosSeed: bool
        IncRotSeed: bool
        IncSclSeed: bool
        ObjectsToScatter: MXSWrapperBase
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
    class Scene_Effect_Loader(floatController):
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
    class Script_Operator(helper):
        Random_Seed: int
        Proceed_Script: str
        ...
    class Script_Test(helper):
        Random_Seed: int
        Proceed_Script: str
        ...
    class ScriptedBehavior(ReferenceTarget):
        name: str
        scriptContextName: str
        script: None
        type: int
        ...
    class Scripted_Behavior(ReferenceTarget):
        name: str
        scriptContextName: str
        script: None
        type: int
        ...
    class Seat(GeometryClass):
        gender: int
        motionSeed: int
        id: int
        single: bool
        height: float
        ...
    class SecurityTools(Interface):
        ...
    class SecurityToolsUtility(GlobalUtilityPlugin):
        ...
    class SeekBehavior(ReferenceTarget):
        name: str
        targets: MXSWrapperBase
        targetComp: int
        seekMethod: int
        useRadii: bool
        innerRadius: float
        outerRadius: float
        falloff: float
        showRadii: bool
        forceColor: MXSWrapperBase
        displayForce: bool
        ...
    class Seek_Behavior(ReferenceTarget):
        name: str
        targets: MXSWrapperBase
        targetComp: int
        seekMethod: int
        useRadii: bool
        innerRadius: float
        outerRadius: float
        falloff: float
        showRadii: bool
        forceColor: MXSWrapperBase
        displayForce: bool
        ...
    class SegTrans(Matrix3Controller):
        ...
    class SelectByChannel(modifier):
        selectionType: int
        mapID: int
        mapSubID: int
        ...
    class SelectSaveBitMap(Primitive):
        ...
    class Select_By_Channel(modifier):
        selectionType: int
        mapID: int
        mapSubID: int
        ...
    class Select_Keys_by_Time(trackViewUtility):
        ...
    class Select_Object(ReferenceTarget):
        type: int
        Single_Or_Multiple: int
        object: None
        objects: MXSWrapperBase
        Independent_PFlow_System: bool
        filter: None
        ...
    class Select_the_Biped_for_use_as_a_retargeting_reference(ReferenceTarget):
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
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class Send_Out(helper):
        Condition_Type: int
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
    class SetKeyCtrl(floatController):
        keyIndex: int
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
    class Set_Key_Crtl(floatController):
        keyIndex: int
        ...
    class Setting(ReferenceTarget):
        averageSpeed1: float
        maxAccel1: float
        turnDecel1: float
        turnDecelAngle1: float
        inclineDecel1: float
        inclineDecelAngle1: float
        declineDecel1: float
        declineDecelAngle1: float
        maxturn1: float
        maxturnAccel1: float
        maxIncline1: float
        maxDecline1: float
        maxbank1: float
        maxbankAccel1: float
        bankfactor1: float
        startFrame1: int
        priority1: int
        averageSpeed2: float
        maxAccel2: float
        turnDecel2: float
        turnDecelAngle2: float
        inclineDecel2: float
        inclineDecelAngle2: float
        declineDecel2: float
        declineDecelAngle2: float
        maxturn2: float
        maxturnAccel2: float
        maxIncline2: float
        maxDecline2: float
        maxbank2: float
        maxbankAccel2: float
        bankfactor2: float
        startFrame2: int
        priority2: int
        active: bool
        showForces: bool
        showVelocity: bool
        showCogStates: bool
        xyConstrain: bool
        velocityColor: MXSWrapperBase
        useHierBbox: bool
        useBiped: bool
        startClip: int
        rand1: bool
        rand2: bool
        rand3: bool
        rand4: bool
        rand5: bool
        rand6: bool
        rand7: bool
        rand8: bool
        rand9: bool
        rand10: bool
        rand11: bool
        rand12: bool
        rand16: bool
        rand17: bool
        rand18: bool
        rand13: bool
        rand14: bool
        rand15: bool
        set1: bool
        set2: bool
        set3: bool
        set4: bool
        set5: bool
        set6: bool
        set7: bool
        set8: bool
        set9: bool
        set10: bool
        set11: bool
        set12: bool
        set13: bool
        set14: bool
        set15: bool
        set16: bool
        set17: bool
        set18: bool
        set19: bool
        set20: bool
        set21: bool
        set22: bool
        set23: bool
        set24: bool
        set25: bool
        set26: bool
        delegates: MXSWrapperBase
        name: None
        ...
    class Shader(MAXWrapper):
        ...
    class Shadow(MAXWrapper):
        ...
    class ShadowClass(Value):
        ...
    class ShadowRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class ShadowsMap(BakeElement):
        enabled: bool
        filterOn: bool
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        elementName: str
        bitmap: None
        backgroundColor: MXSWrapperBase
        targetMapSlotName: str
        ...
    class ShapeBooleanObject(shape):
        ...
    class ShapeControl(ReferenceTarget):
        Particle_Geometry_Object: None
        Proceed_Type: int
        History_Dependent: bool
        Execution_Order: int
        Priority_Order: int
        Animated_Shape: bool
        Acquire_Mapping: bool
        Discrete_Optimization: bool
        filter: None
        Input_Time: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        Input_5: None
        Input_6: None
        Input_7: None
        Input_8: None
        ...
    class ShapeFilterFn(MAXScriptFunction):
        ...
    class ShapeLibrary(helper):
        Dimension_Type: int
        Type_2D: int
        Type_3D: int
        size: float
        Use_Scale: bool
        Scale_Value: float
        Scale_Variation: float
        Random_Multi_Shape_Order: bool
        Random_Seed: int
        Generate_Mapping_Coords: bool
        Fit_Mapping: bool
        ...
    class ShapeMap(textureMap):
        filter: bool
        mipmap: bool
        monoOutput: int
        rgbOutput: int
        applycrop: bool
        croporplace: int
        crop_u: float
        crop_v: float
        crop_w: float
        crop_h: float
        jitter: bool
        jitteramt: float
        alphaSource: int
        coords: MXSWrapperBase
        output: MXSWrapperBase
        restype: int
        finiteresolution: int
        shapeobject: None
        outlinecolor: MXSWrapperBase
        fillcolor: MXSWrapperBase
        bgcolor: MXSWrapperBase
        fillbg: bool
        renderopen: bool
        endtype: int
        filledclosed: bool
        outlinedclosed: bool
        outlinewidth: float
        boundstype: int
        manualwidth: float
        manualheight: float
        stricthierarchy: bool
        boundsobject: None
        renderchildren: bool
        renderroot: bool
        mergeshapes: bool
        usefillcolor: bool
        hwbitmapsize: int
        ...
    class ShapeMerge(GeometryClass):
        Operation_Type: int
        Remove_Interior_Exterior: int
        Output_Sub_Mesh_Selection: int
        ...
    class ShapeStandard(helper):
        shape: int
        size: float
        Use_Scale: bool
        Scale_Value: float
        ...
    class Shape_Check(UtilityPlugin):
        ...
    class Shape_Facing(helper):
        Look_At_Object: None
        parallel: bool
        Size_Space: int
        units: float
        Inherited_Scale: float
        Proportion: float
        variation: float
        Pivot_At: int
        WH_Ratio: float
        Random_Seed: int
        orientation: int
        ...
    class Shape_Instance(helper):
        Shape_Object: None
        Group_Members: bool
        Object_And_Children: bool
        Object_Elements: bool
        Scale_Value: float
        variation: float
        Acquire_Mapping: bool
        Acquire_Material: bool
        SubMtl_ID_Offset: int
        Random_Shape: bool
        Animated_Shape: bool
        Acquire_Shape: bool
        Fast_Shape_Evaluation: bool
        Sync_Type: int
        Add_Random_Offset: bool
        Random_Offset: int
        Random_Seed: int
        Set_Scale: bool
        Report_Node_Handles: int
        Handles_To_Report: MXSWrapperBase
        ...
    class Shape_Mark(helper):
        Contact_Object: None
        Surface_Animation: bool
        Align_To: int
        Divergence: float
        Size_Space: int
        width: float
        length: float
        Inherited_Scale: float
        variation: float
        Angle_Distortion: bool
        Max_Distortion: float
        Mark_Type: int
        height: float
        Multi_Elements: bool
        Pivot_Offset: float
        Surface_Offset: float
        Surface_Offset_Variation: float
        Vertex_Noise: float
        Continuous_Update: bool
        Generate_Mapping_Coords: bool
        Random_Seed: int
        ...
    class SharedMoflow(ReferenceTarget):
        name: str
        figFileLoaded: bool
        bipeds: MXSWrapperBase
        ...
    class SharedMoflowList(ReferenceTarget):
        SharedMoFlows: MXSWrapperBase
        EditedSharedMoFlow: None
        ...
    class SharedMotionFlow(ReferenceTarget):
        name: str
        figFileLoaded: bool
        bipeds: MXSWrapperBase
        ...
    class SharedMotionFlows(ReferenceTarget):
        SharedMoFlows: MXSWrapperBase
        EditedSharedMoFlow: None
        ...
    class SharedMotionFlowsFloatController(floatController):
        ...
    class SharedViews(UtilityPlugin):
        ...
    class Sharp_Quadratic(filter):
        ...
    class ShaveStylinIcon(helper):
        ...
    class Shell(modifier):
        innerAmount: float
        outerAmount: float
        overrideMatID: bool
        matID: int
        overrideSmoothingGroup: bool
        smoothGroup: int
        edgeMapping: int
        tvOffset: float
        overrideInnerMatID: bool
        matInnerID: int
        selectEdgeFaces: bool
        selectInnerFaces: bool
        segments: int
        straightenCorners: bool
        autosmooth: bool
        autoSmoothAngle: float
        selectOuterFaces: bool
        overrideOuterMatID: bool
        matOuterID: int
        Bevel: bool
        bevelShape: None
        ...
    class ShellLaunch(Primitive):
        ...
    class Shell_Material(material):
        originalMaterial: MXSWrapperBase
        bakedMaterial: MXSWrapperBase
        viewportMtlIndex: int
        renderMtlIndex: int
        ...
    class Shellac(material):
        shellacMtl1: MXSWrapperBase
        shellacMtl2: MXSWrapperBase
        shellacColorBlend: float
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
    class Simple_Shape(shape):
        ...
    class Simple_Spline(shape):
        ...
    class SingleWeakRefMakerClass(MAXWrapperNonRefTarg):
        ...
    class Skeleton(helper):
        ...
    class Skew(modifier):
        axis: int
        direction: float
        limit: bool
        upperlimit: float
        lowerlimit: float
        amount: float
        ...
    class Skin(modifier):
        effect: float
        filter_vertices: bool
        filter_envelopes: bool
        filter_cross_sections: bool
        draw_all_envelopes: bool
        draw_vertices: bool
        ref_frame: int
        paint_radius: float
        paint_feather: float
        cross_radius: float
        always_deform: bool
        paint_str: float
        localSquash: MXSWrapperBase
        initialSquash: MXSWrapperBase
        initialStaticEnvelope: bool
        initialInnerEnvelopePercent: float
        initialOuterEnvelopePercent: float
        initialEnvelopeInner: float
        initialEnvelopeOuter: float
        paintBlendMode: bool
        backfacecull: bool
        weightTool_tolerance: float
        weightTool_scale: float
        weightTool_weight: float
        selectElement: bool
        mirrorPlane: int
        mirrorOffset: float
        mirrorUseInitialTM: bool
        mirrorEnabled: bool
        mirrorThreshold: float
        mirrorProjection: int
        manualupdate: bool
        mirrorFast: bool
        draw_all_envelopes: bool
        draw_vertices: bool
        draw_all_gizmos: bool
        draw_all_vertices: bool
        shadeweights: bool
        envelopesAlwaysOnTop: bool
        crossSectionsAlwaysOnTop: bool
        showNoEnvelopes: bool
        colorAllWeights: bool
        weightColors: MXSWrapperBase
        showHiddenVertices: bool
        ref_frame: int
        rigid_vertices: bool
        rigid_handles: bool
        fast_update: bool
        no_update: bool
        updateOnMouseUp: bool
        bone_Limit: int
        backTransform: bool
        shortenBoneNames: bool
        fastSubAnims: bool
        fastTMCache: bool
        fastVertexWeighting: bool
        fastGizmos: bool
        ignoreBoneScale: bool
        animatableEnvelopes: bool
        weightAllVertices: bool
        clearZeroLimit: float
        enableDQ: bool
        wt_affectSelected: bool
        wt_showAffectedBones: bool
        wt_updateOnMouseUp: bool
        wt_flipUI: bool
        wt_showAttributes: bool
        wt_showGlobal: bool
        wt_shortenLabels: bool
        wt_showExclusions: bool
        wt_showLocks: bool
        wt_showOptionsUI: bool
        wt_showSetUI: bool
        wt_showCopyPasteUI: bool
        wt_showMenu: bool
        wt_tableY: int
        wt_precision: float
        wt_fontSize: int
        wt_winXPos: int
        wt_winYPos: int
        wt_winWidth: int
        wt_winHeight: int
        wt_dragLeftRightMode: bool
        wt_activeVertexSet: int
        wt_showMarker: bool
        wt_markerType: int
        wt_markerColor: MXSWrapperBase
        debugMode: bool
        wt_attribLabelHeight: int
        rightJustifyBoneText: bool
        gizmos: MXSWrapperBase
        ...
    class SkinTools(UtilityPlugin):
        ...
    class SkinUtilities(UtilityPlugin):
        ...
    class SkinUtils(Interface):
        ...
    class SkinWrapPatch(modifier):
        patch: None
        sampleRate: int
        ...
    class Skin_Morph(modifier):
        Bones: MXSWrapperBase
        morphName: None
        influenceAngle: float
        falloff: int
        showMirrorPlane: bool
        mirrorPlane: int
        mirrorOffset: float
        mirrorThreshold: float
        previewVerts: bool
        previewBone: bool
        jointType: int
        targetNodes: MXSWrapperBase
        falloffGraphs: MXSWrapperBase
        reloadSelected: bool
        safemode: bool
        showDriverBone: bool
        showMorphBone: bool
        showCurrentAngle: bool
        showLimitAngle: bool
        matrixSize: float
        showDeltas: bool
        showX: bool
        showY: bool
        showZ: bool
        bonesize: float
        softSelectionGraph: MXSWrapperBase
        useSoftSelection: bool
        selectionRadius: float
        edgeLimit: int
        useEdgeLimit: bool
        enabled: bool
        showedges: bool
        ...
    class Skin_Wrap(modifier):
        mesh: None
        threshold: float
        engine: int
        falloff: float
        distance: float
        faceLimit: int
        showLoops: bool
        showAxis: bool
        showFaceLimit: bool
        showMirrorData: bool
        mirrorPlane: int
        mirrorOffset: float
        meshList: MXSWrapperBase
        showUnassignedVerts: bool
        showVerts: bool
        weightAllVerts: bool
        mirrorThreshold: float
        Blend: bool
        blendDistance: float
        ...
    class Skin_Wrap_Patch(modifier):
        patch: None
        sampleRate: int
        ...
    class Skylight(light):
        multiplier: float
        color: MXSWrapperBase
        rays_per_sample: int
        ray_Bias: float
        on: bool
        castShadows: bool
        sky_color_map: None
        sky_color_map_on: bool
        sky_color_map_amt: float
        sky_mode: int
        ...
    class SlateDragDropBridge(Interface):
        ...
    class SlaveFloat(floatController):
        ...
    class SlaveMatrix3(Matrix3Controller):
        ...
    class SlavePoint3(point3Controller):
        ...
    class SlavePoint4(point4Controller):
        ...
    class SlavePos(positionController):
        ...
    class SlaveRotation(rotationController):
        ...
    class SlaveScale(scaleController):
        ...
    class Slave_Control(Matrix3Controller):
        ...
    class Slave_Point3(point3Controller):
        ...
    class Slerp(Generic):
        ...
    class SliceModifier(modifier):
        Slice_Type: int
        Faces___Polygons_Toggle: int
        ...
    class SliderControl(RolloutControl):
        ...
    class SliderManip(helper):
        ...
    class Slider_Manip(helper):
        ...
    class SlidingDoor(GeometryClass):
        height: float
        open: float
        width: float
        depth: float
        Double_Doors: int
        Flip_Swing: bool
        Flip_Hinge: bool
        Create_Frame: bool
        Frame_Width: float
        Frame_Depth: float
        Door_Offset: float
        Leaf_Thickness: float
        Stiles_Top_Rail: float
        Bottom_Rail: float
        Number_of_Panels_Horizontally: int
        Number_of_Panels_Vertically: int
        Muntin: float
        Panel_Type: int
        Glass_Thickness: float
        Bevel_Angle: float
        Panel_Thickness_1: float
        Panel_Thickness_2: float
        Panel_Middle_Thickness: float
        Panel_Width_1: float
        Panel_Width_2: float
        Generate_Mapping_Coords: bool
        ...
    class SlidingWindow(GeometryClass):
        height: float
        width: float
        depth: float
        Hung: bool
        Chamfered_Profile: bool
        Number_of_Panels_Horizontally: int
        Number_of_Panels_Vertically: int
        Horizontal_Frame_Width: float
        Vertical_Frame_Width: float
        Frame_Thickness: float
        Glazing_Thickness: float
        Rail_Width: float
        Percent_Open: int
        Generate_Mapping_Coords: bool
        ...
    class Smoke(textureMap):
        size: float
        iterations: int
        Exponent: float
        phase: float
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1: None
        map2: None
        map1on: bool
        map2on: bool
        coords: MXSWrapperBase
        ...
    class SmoothModifier(modifier):
        autosmooth: bool
        preventIndirect: bool
        threshold: float
        smoothingBits: int
        ...
    class Snow(GeometryClass):
        display: int
        start: MXSWrapperBase
        constant: bool
        render: int
        speed: float
        viewportcount: int
        rendercount: int
        flakesize: float
        variation: float
        starttime: MXSWrapperBase
        lifetime: MXSWrapperBase
        life: MXSWrapperBase
        birthrate: float
        emitterwidth: float
        emitterheight: float
        hideemitter: bool
        tumble: float
        tumblescale: float
        ...
    class SoftSelectTool(UserDataTypeClass):
        ...
    class SoftSelectionManager(trackViewUtility):
        ...
    class Soft_Selection_Tool(UserDataTypeClass):
        ...
    class Soften(filter):
        ...
    class SortKey(ReferenceTarget):
        ...
    class Sound(helper):
        ...
    class SoundClass(MAXWrapper):
        ...
    class SpaceBend(SpacewarpObject):
        ...
    class SpaceCameraMap(SpacewarpModifier):
        camera: None
        ...
    class SpaceConform(SpacewarpModifier):
        ...
    class SpaceFFDBox(SpacewarpObject):
        dispLattice: bool
        dispSource: bool
        deformType: int
        falloff: float
        tension: float
        continuity: float
        length: float
        width: float
        height: float
        ...
    class SpaceFFDCyl(SpacewarpObject):
        dispLattice: bool
        dispSource: bool
        deformType: int
        falloff: float
        tension: float
        continuity: float
        radius: float
        height: float
        ...
    class SpaceNoise(SpacewarpObject):
        ...
    class SpacePatchDeform(SpacewarpModifier):
        rotation: float
        V_Stretch: float
        Plane_to_Patch_Deform: int
        Flip_deformation_axis: int
        U_Stretch: float
        V_Percent: float
        U_Percent: float
        ...
    class SpacePathDeform(SpacewarpModifier):
        axis: int
        rotation: float
        Twist: float
        Stretch: float
        path: None
        Flip_deformation_axis: int
        Percent_along_path: float
        ...
    class SpaceSkew(SpacewarpObject):
        height: float
        length: float
        width: float
        decay: float
        ...
    class SpaceStretch(SpacewarpObject):
        height: float
        length: float
        width: float
        decay: float
        ...
    class SpaceSurfDeform(SpacewarpModifier):
        rotation: float
        surface: None
        V_Stretch: float
        Plane_to_Patch_Deform: int
        Flip_deformation_axis: int
        U_Stretch: float
        V_Percent: float
        U_Percent: float
        ...
    class SpaceTaper(SpacewarpObject):
        height: float
        length: float
        width: float
        decay: float
        ...
    class SpaceTwist(SpacewarpObject):
        height: float
        length: float
        width: float
        decay: float
        ...
    class Space_Warp_Behavior(ReferenceTarget):
        name: str
        spaceWarp: None
        forceColor: MXSWrapperBase
        displayForce: bool
        ...
    class Spacedisplace(SpacewarpObject):
        axis: int
        bitmap: None
        blur: float
        height: float
        length: float
        map: None
        width: float
        cap: bool
        U_Tile: float
        V_Tile: float
        decay: float
        maptype: int
        lumCenter: float
        lumCenterEnable: bool
        useMap: bool
        applyMap: bool
        U_Flip: bool
        V_Flip: bool
        W_Flip: bool
        strength: float
        W_Tile: float
        ...
    class Spaceripple(SpacewarpObject):
        amplitude1: float
        amplitude2: float
        wavelength: float
        phase: float
        decay: float
        circles: int
        segments: int
        divisions: int
        ...
    class SpacewarpModifier(MAXWrapper):
        ...
    class SpacewarpObject(node):
        ...
    class Spacewave(SpacewarpObject):
        amplitude1: float
        amplitude2: float
        wavelength: float
        phase: float
        decay: float
        circles: int
        segments: int
        divisions: int
        ...
    class Spawn(helper):
        Spawn_Type: int
        Delete_Parent: bool
        Spawn_Rate: float
        Spawn_Step_Size: float
        Spawn_Able: float
        Number_of_Offsprings: int
        Offsprings_Variation: float
        Sync_Type: int
        Restart_Particle_Age: bool
        Speed_Type: int
        speed: float
        Speed_Inherited: float
        Speed_Variation: float
        Divergence: float
        Scale_Factor: float
        Scale_Variation: float
        Random_Seed: int
        ...
    class Speckle(textureMap):
        size: float
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1: None
        map2: None
        map1on: bool
        map2on: bool
        coords: MXSWrapperBase
        ...
    class Specular(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class SpeedByIcon(helper):
        Accel_Limit: float
        Influence: float
        Use_Speed_Variation: bool
        Speed_Minimum: float
        Speed_Maximum: float
        Use_Icon_Orientation: bool
        Steer_Towards_Trajectory: bool
        distance: float
        Sync_Type_Param_Animation: int
        Sync_Type_Icon_Animation: int
        icon_size: float
        Color_Type: bool
        Random_Seed: int
        ...
    class SpeedVaryBehavior(ReferenceTarget):
        name: str
        Period: int
        periodDeviation: float
        centerSpeed: float
        speedDeviation: float
        accelPeriod: float
        accelDeviation: float
        seed: int
        ...
    class Speed_By_Surface(helper):
        Speed_Type: int
        Set_Speed_Magnitude: bool
        Speed_Value: float
        Speed_Variation: float
        Surface_Objects: MXSWrapperBase
        Animated_Shape: bool
        Subframe_Sampling: bool
        Set_Speed_By_Surface_Material: bool
        Material_Type: int
        Use_Sub_Material: bool
        Material_ID: int
        Direction_Type: int
        Divergence: float
        Acceleration_Limit: float
        Unlimited_Range: bool
        range: float
        falloff: float
        Sync_Type: int
        Random_Seed: int
        ...
    class Speed_Test(helper):
        Test_Type: int
        Condition_Type: int
        Unit_Value: float
        Unit_Variation: float
        Angle_Value: float
        Angle_Variation: float
        Sync_Type: int
        Random_Seed: int
        ...
    class Speed_Vary_Behavior(ReferenceTarget):
        name: str
        Period: int
        periodDeviation: float
        centerSpeed: float
        speedDeviation: float
        accelPeriod: float
        accelDeviation: float
        seed: int
        ...
    class Sphere(GeometryClass):
        sliceon: bool
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInRadius: float
        radius: float
        segs: int
        smooth: bool
        hemisphere: float
        chop: int
        recenter: bool
        mapcoords: bool
        slice: bool
        slicefrom: float
        sliceto: float
        ...
    class SphereGizmo(helper):
        radius: float
        seed: int
        hemisphere: bool
        ...
    class SphericalCollision(ReferenceMaker):
        ...
    class Spherify(modifier):
        percent: float
        ...
    class SpinLimit(helper):
        ...
    class Spindle(GeometryClass):
        height: float
        radius: float
        sides: int
        mapcoords: int
        Blend: float
        cap_segments: int
        Cap_Height: float
        Smooth_On: int
        Slice_On: int
        Slice_From: float
        Slice_To: float
        Height_Segments: int
        ...
    class SpineData2(ReferenceTarget):
        ...
    class SpineTrans2(Matrix3Controller):
        ...
    class SpinnerControl(RolloutControl):
        ...
    class Spiral_Stair(GeometryClass):
        StepType: int
        GenerateStringers: bool
        GenerateCarriage: bool
        GenerateInsideRailing: bool
        GenerateOutsideRailing: bool
        Stepwidth: float
        StepThickness: float
        GenerateMapping: bool
        StepDepth_X: bool
        StepDepth: float
        StepHeight: float
        StepCount: int
        StringerDepth: float
        StringerWidth: float
        StringerOffset: float
        StringerSpringFloor: bool
        CarriageWidth: float
        CarriageIntOffs: float
        CarriageExtOffs: float
        CarriageSpace: float
        CarriageCount: int
        CarriageContext: int
        CarriageSpacingType: int
        CarriageHeight: float
        CarriageSpringFloor: bool
        RailingHeight: float
        RailingOffs: float
        RailingSegments: int
        RailingRadius: float
        CenterPoleRadius: float
        CenterPoleSegments: int
        CenterPoleHeight_X: bool
        CenterPoleHeight: float
        GenerateCenterPole: bool
        direction: int
        radius: float
        Revolutions: float
        StepSegments_X: bool
        StepSegments: int
        ...
    class Splat(textureMap):
        size: float
        iterations: int
        threshold: float
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1: None
        map2: None
        map1on: bool
        map2on: bool
        coords: MXSWrapperBase
        ...
    class SplineIKChain(Matrix3Controller):
        ...
    class SplineIKSolver(IKSolver):
        ...
    class SplineInfluence(modifier):
        ShowKnots: bool
        NearInfluence: float
        FarInfluence: float
        InfluenceNodes: MXSWrapperBase
        FalloffType: int
        EnableBias: bool
        BiasSelected: bool
        bias: float
        ExistingSelection: int
        invert: bool
        ConvertSelections: bool
        FalloffMethod: int
        SelectionFalloffType: int
        FalloffKnots: int
        FalloffPercent: float
        ...
    class SplineMirror(modifier):
        axis: int
        flip: bool
        slice: bool
        weld: bool
        threshold: float
        ShowKnots: bool
        tangents: bool
        ...
    class SplineMorph(modifier):
        MorphMethod: int
        amount: float
        Use_Softselection: bool
        invert: bool
        ShowKnots: bool
        Target1: None
        TargetOn1: bool
        TargetWeight1: float
        Target2: None
        TargetOn2: bool
        TargetWeight2: float
        Target3: None
        TargetOn3: bool
        TargetWeight3: float
        Target4: None
        TargetOn4: bool
        TargetWeight4: float
        Target5: None
        TargetOn5: bool
        TargetWeight5: float
        Target6: None
        TargetOn6: bool
        TargetWeight6: float
        Target7: None
        TargetOn7: bool
        TargetWeight7: float
        Target8: None
        TargetOn8: bool
        TargetWeight8: float
        Target9: None
        TargetOn9: bool
        TargetWeight9: float
        Target10: None
        TargetOn10: bool
        TargetWeight10: float
        ...
    class SplineOverlap(modifier):
        thickness: float
        Drape: float
        UseNormals: bool
        useSelection: bool
        ShowKnots: bool
        ...
    class SplineRelax(modifier):
        amount: float
        iterations: int
        tangents: bool
        knots: bool
        useSelection: bool
        ShowKnots: bool
        ...
    class SplineSelect(modifier):
        ...
    class SplineShape(shape):
        steps: int
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        ...
    class Spline_Chamfer(modifier):
        ShowKnots: bool
        amount: float
        depth: float
        bias: float
        limiteffect: bool
        useSelection: bool
        useminangle: bool
        minangle: float
        CornerKnotsOnly: bool
        ...
    class Spline_IK_Control(modifier):
        helper_list: MXSWrapperBase
        helper_size: float
        helper_centermarker: bool
        helper_axistripod: bool
        helper_cross: bool
        Box: bool
        constantscreensize: bool
        drawontop: bool
        linkTypes: int
        ...
    class Split_Amount(helper):
        Test_Type: int
        ratio: float
        Every_Nth: int
        First_N: int
        Per_Emission_Source: bool
        Random_Seed: int
        ...
    class Split_Group(helper):
        Group_Selection_Operator: None
        Condition_Type: int
        Use_Proxy_Particles: bool
        Proxy_Particle_System: None
        multiplier: float
        Index_Offset: int
        Group_Selection_Operators: MXSWrapperBase
        ...
    class Split_Selected(helper):
        Condition_Type: int
        ...
    class Split_Source(helper):
        Condition_Type: int
        Selected_Sources: MXSWrapperBase
        ...
    class Spray(GeometryClass):
        display: int
        start: MXSWrapperBase
        constant: bool
        render: int
        speed: float
        viewportcount: int
        rendercount: int
        variation: float
        starttime: MXSWrapperBase
        lifetime: MXSWrapperBase
        life: MXSWrapperBase
        birthrate: float
        emitterwidth: float
        emitterheight: float
        hideemitter: bool
        dropsize: float
        ...
    class SprayBirth(helper):
        Particle_Paint_Helper: None
        Emit_Start: int
        Emit_Type: int
        Emit_Stop: int
        duration: int
        Subframe_Sampling: bool
        Lock_Position: bool
        Lock_Rotation: bool
        Acquire_Selection: bool
        Selection_Type: int
        ...
    class SprayCursor(GeometryClass):
        ...
    class SprayMaster(helper):
        Spray_Radius: float
        Density_Center: float
        Density_Sides: float
        Per_Jet_Limit: int
        Rate_Type: int
        Rate_Drops_Per_Second: float
        Rate_Drops_Per_Length_Unit: float
        Rate_Drops_Per_Jet: int
        Display_Type: int
        Display_Size: float
        Jet_Start_Type: int
        Jet_Start_Time: int
        Jet_Stop_Type: int
        Time_Scale: float
        Jet_Stop_Time: int
        Jet_Duration: int
        AutoAdjust_Current_Frame: bool
        Adjust_Global_Timing: bool
        icon_size: float
        Random_Seed: int
        Use_Radius_Graph: bool
        Spray_Radius_Graph: None
        Use_Rate_Graph: bool
        Spray_Radius_Rate: None
        Spray_At_Type: int
        Spray_At_Objects: MXSWrapperBase
        Objects_Animated_Surface: bool
        Include_Spray_Children: bool
        Include_Spray_Group_Members: bool
        Use_Mask_Objects: bool
        Masks: MXSWrapperBase
        Include_Mask_Children: bool
        Include_Mask_Group_Members: bool
        Selection_Filter_Type: int
        Location_Type: int
        distance: float
        Distance_Variation: float
        Use_Separation: bool
        Separation_Distance: float
        Maximum_Number_Of_Attempts: int
        Stack_Up_For_Separation: bool
        Generate_Rotation: bool
        Priority_Axis: int
        Reverse_X_Axis: bool
        Reverse_Z_Axis: bool
        Orientation_Type_For_X_Axis: int
        Orientation_Type_For_Z_Axis: int
        Divergence_For_X_Axis: float
        Divergence_For_Z_Axis: float
        Acquire_Sub_Material_Index: bool
        Generate_Mapping: bool
        Assign_To_Mapping_Channels: MXSWrapperBase
        Mapping_Type: int
        Mapping_Start_Value: float
        Mapping_End_Value: float
        Mapping_Offset_Value_Per_Second: float
        Mapping_Offset_Value_Per_Drop: float
        Show_Particle_Timing: bool
        Late_Color: MXSWrapperBase
        Editing_Start_At: int
        Editing_Stop_Type: int
        Editing_Stop_At: int
        Editing_Duration: int
        Editing_Adjust_Global_Timing: bool
        Selected_Strokes: MXSWrapperBase
        Auto_Sync_Timing_By_Selected_Stroke: bool
        ...
    class SprayPlacement(helper):
        Particle_Paint_Helper: None
        Update_Type: int
        Acquire_Paint_Position: bool
        Position_Type: int
        Snap_If_Close: bool
        Snap_Distance: float
        Acquire_Paint_Rotation: bool
        BlendIn_Rotation: bool
        Near_Distance: float
        Far_Distance: float
        Acquire_Paint_Mapping: bool
        Acquire_Paint_MaterialID: bool
        Acquire_Paint_Selection: bool
        Selection_Type: int
        Order_Type: int
        Stop_If_Count_Overflow: bool
        Obey_Quantity_Multiplier: bool
        Separate_Streams_Indexing: bool
        Random_Seed: int
        ...
    class Spring(GeometryClass):
        wire: int
        diameter: float
        Number_of_Turns: float
        Turn_Direction: int
        Segmentation_Method: int
        Segments_Per_Turn: int
        Segments_Along_Turn: int
        Round_Wire_Diameter: float
        Round_Wire_Side_Count: int
        Rectangular_Wire_Width: float
        Rectangular_Wire_Depth: float
        Rectangular_Wire_Fillet_Size: float
        Rectangular_Fillet_Sides: int
        Rectangular_Wire_Rotation_Angle: float
        D_Section_Wire_Width: float
        D_Section_Wire_Depth: float
        D_Section_Wire_Fillet_Size: float
        D_Section_Wire_Fillet_Sides: int
        D_Section_Round_Sides: int
        D_Section_Wire_Rotation_Angle: float
        Dynamics_Spring_Relaxed_Height: float
        Dynamics_K_Constant_Value: float
        Dynamics_K_Constant_Units: int
        Dynamics_Spring_Direction: int
        Enable_Nonlinearity: int
        Free_Spring_Height: float
        Smooth_Spring: int
        End_Placement_Method: int
        Renderable_Spring: int
        Generate_Mapping_Coordinates: int
        ...
    class SpringPoint3Controller(point3Controller):
        ...
    class SpringPositionController(positionController):
        effectHow: int
        forceNode: MXSWrapperBase
        steps: int
        x_effect: float
        y_effect: float
        z_effect: float
        start: int
        ...
    class Squad(Generic):
        ...
    class Squeeze(modifier):
        bias: float
        volume: float
        Bulge_Amount: float
        Bulge_Curviture: float
        Squeeze_Amount: float
        Squeeze_Curvature: float
        Limit_Squeeze_Effects: int
        Squeeze_Upper_Limit: float
        Squeeze_Lower_Limit: float
        ...
    class StPathClass(shape):
        ...
    class StackPerformance(Interface):
        ...
    class StandardMaterialClass(Value):
        ...
    class StandardTextureOutput(TexOutputClass):
        invert: bool
        clamp: bool
        alphaFromRGB: bool
        RGB_Level: float
        RGB_Offset: float
        Output_Amount: float
        Bump_Amount: float
        ...
    class StandardUVGen(UVGenClass):
        blur: float
        mapping: int
        mapChannel: int
        mappingType: int
        UVW_Type: int
        U_Mirror: bool
        V_Mirror: bool
        U_Tile: bool
        V_Tile: bool
        showMapOnBack: bool
        Noise_On: bool
        Noise_Animate: bool
        UVTransform: MXSWrapperBase
        realWorldScale: bool
        realWorldHeight: float
        realWorldWidth: float
        phase: float
        U_Offset: float
        V_Offset: float
        U_Tiling: float
        V_Tiling: float
        U_Angle: float
        V_Angle: float
        W_Angle: float
        Noise_Amount: float
        Noise_Size: float
        Noise_Levels: int
        Blur_Offset: float
        ...
    class StandardXYZGen(XYZGenClass):
        blur: float
        offset: MXSWrapperBase
        angle: MXSWrapperBase
        coordType: int
        mapChannel: int
        Blur_Offset: float
        Tiling: MXSWrapperBase
        ...
    class Standard_16_bit(BitmapStorageClass):
        ...
    class Standard_16_bit_Grayscale(BitmapStorageClass):
        ...
    class Standard_1_bit(BitmapStorageClass):
        ...
    class Standard_24_bit_LogLUV_Storage(BitmapStorageClass):
        ...
    class Standard_24_bit_LogLUV_Storage_with_alpha(BitmapStorageClass):
        ...
    class Standard_32_bit(BitmapStorageClass):
        ...
    class Standard_32_bit_Floating_Point_Storage(BitmapStorageClass):
        ...
    class Standard_32_bit_Floating_Point_Storage_Grayscale(BitmapStorageClass):
        ...
    class Standard_32_bit_LogLUV_Storage(BitmapStorageClass):
        ...
    class Standard_32_bit_RealPixel_Storage(BitmapStorageClass):
        ...
    class Standard_64_bit_Storage(BitmapStorageClass):
        ...
    class Standard_8_bit_Grayscale(BitmapStorageClass):
        ...
    class Standard_8_bit_Paletted(BitmapStorageClass):
        ...
    class Standard_Flow(ReferenceTarget):
        ...
    class Standardmaterial(material):
        shaderType: int
        wire: bool
        twoSided: bool
        faceMap: bool
        faceted: bool
        shaderByName: str
        opacityType: int
        opacity: float
        FilterColor: MXSWrapperBase
        filterMap: None
        opacityFallOffType: int
        opacityFallOff: float
        ior: float
        wireSize: float
        wireUnits: int
        applyReflectionDimming: bool
        dimLevel: float
        reflectionLevel: float
        sampler: int
        samplerQuality: float
        samplerEnable: bool
        samplerAdaptThreshold: float
        samplerAdaptOn: bool
        subSampleTextureOn: bool
        samplerAdvancedOptions: bool
        samplerByName: str
        UserParam0: float
        UserParam1: float
        samplerUseGlobal: bool
        mapEnables: MXSWrapperBase
        maps: MXSWrapperBase
        mapAmounts: MXSWrapperBase
        adTextureLock: bool
        ...
    class Standin_for_missing_MultiPass_Camera_Effect_Plugin(MPassCamEffect):
        ...
    class Star(shape):
        steps: int
        numPoints: int
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        radius1: float
        radius2: float
        points: int
        distort: float
        fillet1: float
        fillet2: float
        ...
    class Star_Element(ReferenceTarget):
        elementName: str
        size: float
        intensity: float
        width: float
        angle: float
        Taper: float
        sharp: float
        quantity: int
        on: bool
        objectsHide: bool
        Squeeze: bool
        occlusion: float
        colorSource: float
        centerColor: MXSWrapperBase
        edgeColor: MXSWrapperBase
        radialMtl: None
        useRadialMtl: bool
        radialMap: None
        useRadialMap: bool
        circularColorMix: float
        leftSectionColor: MXSWrapperBase
        centerSectionColor: MXSWrapperBase
        rightSectionColor: MXSWrapperBase
        circularMtl: None
        useCircularMtl: bool
        circularMap: None
        useCircularMap: bool
        radialSizeMap: None
        useRadialSizeMap: bool
        applyLights: bool
        applyImage: bool
        applyImageCenters: bool
        sourceObjectID: bool
        objectID: int
        sourceEffectsID: bool
        effectsID: int
        sourceUnclampedColor: bool
        unclampedColor: float
        unclampedColorInvert: bool
        sourceSurfaceNormal: bool
        surfaceNormal: float
        surfaceNormalInvert: bool
        sourceWhole: bool
        sourceAlpha: bool
        alpha: int
        sourceZBuffer: bool
        zHi: float
        zLo: float
        filterAll: bool
        filterEdge: bool
        filterPerimeterAlpha: bool
        filterPerimeter: bool
        filterBrightness: bool
        brightness: int
        brightnessInvert: bool
        filterHue: bool
        hue: MXSWrapperBase
        hueRange: int
        applyNoise: bool
        noiseMap: None
        radialDensity: None
        useRadialDensity: bool
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
        shadow_Mode: int
        pass1: int
        pass2: int
        ray_Bias: float
        blur: float
        jitter_amt: float
        twoSidedShadows: bool
        noAreaShadows: bool
        shadow_Transparent: bool
        aa_threshold: MXSWrapperBase
        suppress_mat_aa: bool
        suppress_reflt_aa: bool
        skip_coplanar: bool
        coplanar_threshold: float
        ...
    class SteeringWheelsOps(Interface):
        ...
    class StepShape(floatController):
        ...
    class StereoFragment(GraphicsFragmentPlugin):
        ...
    class StopCreating(Primitive):
        ...
    class Stop_Gradually(helper):
        position: MXSWrapperBase
        rotation: MXSWrapperBase
        Timing_Start_Type: int
        Slow_Down_Start_Time: int
        Start_Time_Variation: int
        Use_Different_Types: bool
        Stop_Type: int
        Stop_Time: int
        Stop_Time_Variation: int
        Random_Seed: int
        ...
    class Straight_Stair(GeometryClass):
        StepType: int
        GenerateStringers: bool
        GenerateCarriage: bool
        GenerateInsideRailing: bool
        GenerateOutsideRailing: bool
        Stepwidth: float
        StepThickness: float
        GenerateMapping: bool
        StepDepth_X: bool
        StepDepth: float
        StepHeight: float
        StepCount: int
        StringerDepth: float
        StringerWidth: float
        StringerOffset: float
        StringerSpringFloor: bool
        CarriageWidth: float
        CarriageIntOffs: float
        CarriageExtOffs: float
        CarriageSpace: float
        CarriageCount: int
        CarriageContext: int
        CarriageSpacingType: int
        CarriageHeight: float
        CarriageSpringFloor: bool
        RailingHeight: float
        RailingOffs: float
        RailingSegments: int
        RailingRadius: float
        length: float
        ...
    class Strauss(Shader):
        ...
    class Streak_Element(ReferenceTarget):
        elementName: str
        size: float
        intensity: float
        width: float
        angle: float
        Taper: float
        sharp: float
        on: bool
        objectsHide: bool
        Squeeze: bool
        occlusion: float
        colorSource: float
        centerColor: MXSWrapperBase
        edgeColor: MXSWrapperBase
        radialMtl: None
        useRadialMtl: bool
        radialMap: None
        useRadialMap: bool
        circularColorMix: float
        quadrant1Color: MXSWrapperBase
        quadrant2Color: MXSWrapperBase
        quadrant3Color: MXSWrapperBase
        circularMtl: None
        useCircularMtl: bool
        circularMap: None
        useCircularMap: bool
        radialSizeMap: None
        useRadialSizeMap: bool
        applyLights: bool
        applyImage: bool
        applyImageCenters: bool
        sourceObjectID: bool
        objectID: int
        sourceEffectsID: bool
        effectsID: int
        sourceUnclampedColor: bool
        unclampedColor: float
        unclampedColorInvert: bool
        sourceSurfaceNormal: bool
        surfaceNormal: float
        surfaceNormalInvert: bool
        sourceWhole: bool
        sourceAlpha: bool
        alpha: int
        sourceZBuffer: bool
        zHi: float
        zLo: float
        filterAll: bool
        filterEdge: bool
        filterPerimeterAlpha: bool
        filterPerimeter: bool
        filterBrightness: bool
        brightness: int
        brightnessInvert: bool
        filterHue: bool
        hue: MXSWrapperBase
        hueRange: int
        applyNoise: bool
        noiseMap: None
        radialDensity: None
        useRadialDensity: bool
        ...
    class Stretch(modifier):
        axis: int
        to: float
        Stretch: float
        limit: int
        Amplify: float
        ...
    class StringPacket(ReferenceMaker):
        ...
    class StringStream(Value):
        ...
    class Strokes(UtilityPlugin):
        ...
    class StructDef(Value):
        ...
    class Stucco(textureMap):
        size: float
        thickness: float
        threshold: float
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1: None
        map2: None
        map1on: bool
        map2on: bool
        coords: MXSWrapperBase
        ...
    class SubstManager(Interface):
        ...
    class Substance(textureMap):
        SubstanceFilename: str
        coords: MXSWrapperBase
        globalTextureWidth: int
        globalModeScale: int
        localRelativeTextureWidth: int
        localAbsoluteTextureWidth: int
        localMode: int
        globalTextureHeight: int
        localRelativeTextureHeight: int
        localAbsoluteTextureHeight: int
        lockAspectRatio: int
        rolloutStates: int
        ...
    class Substance2(textureMap):
        SubstanceFilePath: str
        ExportPresetFilePath: str
        ImportPresetFilePath: str
        ...
    class Substance2MenuManager(GlobalUtilityPlugin):
        ...
    class Substance2Output(textureMap):
        ...
    class SubstanceOutput(textureMap):
        ...
    class SubstancePBWrapper(ReferenceTarget):
        ...
    class SubstanceTexWrapper(ReferenceTarget):
        ...
    class SubstanceTexture(textureMap):
        SubstanceFilename: str
        coords: MXSWrapperBase
        globalTextureWidth: int
        globalModeScale: int
        localRelativeTextureWidth: int
        localAbsoluteTextureWidth: int
        localMode: int
        globalTextureHeight: int
        localRelativeTextureHeight: int
        localAbsoluteTextureHeight: int
        lockAspectRatio: int
        rolloutStates: int
        ...
    class Substance_Output(textureMap):
        ...
    class Substituion_Offset_Transform(Matrix3Controller):
        ...
    class Substitute(modifier):
        displayInViewport: bool
        DisplayInRender: bool
        ObjectReference: None
        objectName: str
        MoveCopyInstance: int
        SubstituteType: str
        RetainPosition: bool
        RetainLocalRotation: bool
        RetainLocalScale: bool
        ...
    class SubstituteMod(modifier):
        displayInViewport: bool
        DisplayInRender: bool
        ObjectReference: None
        objectName: str
        MoveCopyInstance: int
        SubstituteType: str
        RetainPosition: bool
        RetainLocalRotation: bool
        RetainLocalScale: bool
        ...
    class SubstituteObject(helper):
        ...
    class Substitute_Manager(UtilityPlugin):
        ...
    class Substitute_Object(helper):
        ...
    class Summed_area(BitmapFilterClass):
        ...
    class SunPositioner(light):
        show_compass: bool
        compass_radius: float
        sun_distance: float
        mode: int
        julian_day: int
        time_in_seconds: int
        hours: int
        minutes: int
        day: int
        month: int
        year: int
        time_zone: float
        dst: bool
        dst_use_date_range: bool
        dst_start_day: int
        dst_start_month: int
        dst_end_day: int
        dst_end_month: int
        location: str
        latitude_deg: float
        longitude_deg: float
        north_direction_deg: float
        manual_sun_position: MXSWrapperBase
        azimuth_deg: float
        altitude_deg: float
        weather_file: str
        ...
    class Sun_Positioner(light):
        show_compass: bool
        compass_radius: float
        sun_distance: float
        mode: int
        julian_day: int
        time_in_seconds: int
        hours: int
        minutes: int
        day: int
        month: int
        year: int
        time_zone: float
        dst: bool
        dst_use_date_range: bool
        dst_start_day: int
        dst_start_month: int
        dst_end_day: int
        dst_end_month: int
        location: str
        latitude_deg: float
        longitude_deg: float
        north_direction_deg: float
        manual_sun_position: MXSWrapperBase
        azimuth_deg: float
        altitude_deg: float
        weather_file: str
        ...
    class Sunlight(System):
        ...
    class Sunlight_Daylight_Slave_Controller(Matrix3Controller):
        ...
    class Sunlight_Daylight_Slave_ControllerMatrix3Controller(Matrix3Controller):
        ...
    class Sunlight_Daylight_Slave_Intensity_Controller(floatController):
        ...
    class Sunlight_Daylight_Slave_Intensity_ControllerFloatController(floatController):
        ...
    class Sunlight_Slave_Controller(Matrix3Controller):
        ...
    class Sunlight_Slave_Intensity_Controller(floatController):
        ...
    class SuperSpray(GeometryClass):
        size: float
        seed: int
        iconSize: float
        speed: float
        mappingType: int
        viewType: int
        viewPercent: float
        quantityMethod: int
        particleType: int
        standardParticle: int
        metaballRenderCoarsness: float
        metaballViewCoarsness: float
        metaballAutoCoarsness: bool
        instanceSubTree: bool
        instanceKeyOffsetType: int
        instanceFrameOffset: int
        spinAxisType: int
        spawnType: int
        spawnSpeedType: int
        spawnInheritVelocity: bool
        spawnSpeedFixed: bool
        spawnScaleType: int
        spawnScaleFixed: bool
        motionInfluence: float
        motionMultiplier: float
        motionVariation: float
        instancingObject: None
        lifespanValueQueue: MXSWrapperBase
        objectMutationQueue: MXSWrapperBase
        subsampleEmitterTranslation: bool
        subsampleEmitterRotation: bool
        subsampleCreationTime: bool
        iconHidden: bool
        life: MXSWrapperBase
        Off_Axis: float
        Axis_Spread: float
        Off_Plane: float
        Plane_Spread: float
        Bubble_Amplitude: float
        Bubble_Amplitude_Variation: float
        Bubble_Period: MXSWrapperBase
        Bubble_Period_Variation: float
        Bubble_Phase: float
        Blur_Stretch: int
        Speed_Variation: float
        Birth_Rate: int
        Total_Number: int
        Emitter_Start: MXSWrapperBase
        Emitter_Stop: MXSWrapperBase
        Display_Until: MXSWrapperBase
        Life_Variation: MXSWrapperBase
        Size_Variation: float
        Growth_Time: MXSWrapperBase
        Fade_Time: MXSWrapperBase
        Metaparticle_Tension: float
        Metaparticle_Tension_Variation: float
        Mapping_Time_Base: MXSWrapperBase
        Mapping_Distance_Base: float
        Spin_Time: MXSWrapperBase
        Spin_Time_Variation: float
        Spin_Phase: float
        Spin_Phase_Variation: float
        X_Spin_Vector: float
        Y_Spin_Vector: float
        Z_Spin_Vector: float
        Spin_Axis_Variation: float
        Spawn_Direction_Chaos: float
        Spawn_Speed_Chaos: float
        Spawn_Scale_Chaos: float
        Spawn_Affects: int
        Spawn_Multiplier_Variation: float
        Bubble_Phase_Variation: float
        Die__X_frames_after_collision: MXSWrapperBase
        Die__X_frames_after_collision_variation: float
        Interparticle_Collisions_On: int
        Interparticle_Collision_Steps: int
        Interparticle_Collision_Bounce: float
        Interparticle_Collision_Bounce_Variation: float
        ...
    class SurfDeform(modifier):
        rotation: float
        surface: None
        V_Stretch: float
        Plane_to_Patch_Deform: int
        Flip_deformation_axis: int
        U_Stretch: float
        V_Percent: float
        U_Percent: float
        ...
    class SurfaceArriveBehavior(ReferenceTarget):
        name: str
        surfaces: MXSWrapperBase
        disableAfterArriving: bool
        rate: float
        rateDeviation: float
        speed: float
        speedDeviation: float
        distance: float
        distanceDeviation: float
        offset: float
        facing: bool
        random_closest: int
        everyFrame: bool
        displayOffset: bool
        height: float
        heightDeviation: float
        descentStart: float
        descentstartDeviation: float
        useNormal: bool
        xNormal: float
        yNormal: float
        zNormal: float
        seed: int
        targetColor: MXSWrapperBase
        displayTarget: bool
        targetScale: float
        ...
    class SurfaceFilterFn(MAXScriptFunction):
        ...
    class SurfaceFollowBehavior(ReferenceTarget):
        name: str
        surfaces: MXSWrapperBase
        useProjection: bool
        xVector: float
        yVector: float
        zVector: float
        offset: float
        displayOffset: bool
        targetColor: MXSWrapperBase
        displayTarget: bool
        targetScale: float
        ...
    class Surface_Approximation(UtilityPlugin):
        ...
    class Surface_Arrive_Behavior(ReferenceTarget):
        name: str
        surfaces: MXSWrapperBase
        disableAfterArriving: bool
        rate: float
        rateDeviation: float
        speed: float
        speedDeviation: float
        distance: float
        distanceDeviation: float
        offset: float
        facing: bool
        random_closest: int
        everyFrame: bool
        displayOffset: bool
        height: float
        heightDeviation: float
        descentStart: float
        descentstartDeviation: float
        useNormal: bool
        xNormal: float
        yNormal: float
        zNormal: float
        seed: int
        targetColor: MXSWrapperBase
        displayTarget: bool
        targetScale: float
        ...
    class Surface_Follow_Behavior(ReferenceTarget):
        name: str
        surfaces: MXSWrapperBase
        useProjection: bool
        xVector: float
        yVector: float
        zVector: float
        offset: float
        displayOffset: bool
        targetColor: MXSWrapperBase
        displayTarget: bool
        targetScale: float
        ...
    class Surface_Mapper(SpacewarpModifier):
        ...
    class Surface_position(positionController):
        align: int
        flip: bool
        surface: None
        ...
    class SuspendEditing(Primitive):
        ...
    class SvfExporter(ExporterPlugin):
        ...
    class Switch(ReferenceTarget):
        type: int
        Active_Input: int
        Render_Viewport_Switch: bool
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        Input_5: None
        Input_6: None
        Input_7: None
        Input_8: None
        ...
    class System(node):
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
    class Tape(helper):
        length: float
        ...
    class Taper(modifier):
        curve: float
        symmetry: bool
        limit: bool
        upperlimit: float
        lowerlimit: float
        amount: float
        primaryaxis: int
        effectaxis: int
        ...
    class Targa(BitmapIO):
        ...
    class TargetDirectionallight(light):
        aspect: float
        rgb: MXSWrapperBase
        color: MXSWrapperBase
        contrast: float
        enabled: bool
        on: bool
        type: MXSWrapperBase
        value: int
        falloff: float
        excludeList: MXSWrapperBase
        includeList: None
        showCone: bool
        multiplier: float
        softenDiffuseEdge: float
        hotspot: float
        farAttenStart: float
        farAttenEnd: float
        nearAttenStart: float
        nearAttenEnd: float
        atmosOpacity: float
        atmosColorAmt: float
        decayRadius: float
        shadowColor: MXSWrapperBase
        shadowMultiplier: float
        hsv: MXSWrapperBase
        hue: int
        saturation: int
        inclExclType: int
        affectDiffuse: bool
        affectSpecular: bool
        useNearAtten: bool
        showNearAtten: bool
        useFarAtten: bool
        showFarAtten: bool
        attenDecay: int
        projector: bool
        projectorMap: None
        castShadows: bool
        useGlobalShadowSettings: bool
        raytracedShadows: bool
        overShoot: bool
        coneShape: int
        lightShape: int
        atmosShadows: bool
        lightAffectsShadow: bool
        shadowProjectorMap: None
        useShadowProjectorMap: bool
        ambientOnly: bool
        shadowgenerator: MXSWrapperBase
        ...
    class Target_Area(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Target_Cylinder(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Target_Disc(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Target_Light(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Target_Linear(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Target_Point(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Target_Rectangle(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Target_Sphere(light):
        on: bool
        castShadows: bool
        rgbFilter: MXSWrapperBase
        intensity: float
        kelvin: float
        useKelvin: bool
        intensityAt: float
        intensityType: int
        flux: float
        originalintensity: float
        originalFlux: float
        useMultiplier: bool
        multiplier: float
        shiftColorWhenDimming: bool
        useFarAttenuation: bool
        displayFarAttenuationGizmo: bool
        startFarAttenuation: float
        endFarAttenuation: float
        contrast: float
        softenDiffuseEdge: float
        projector: bool
        projectorMap: None
        affectDiffuse: bool
        affectSpecular: bool
        ambientOnly: bool
        targetDistance: None
        light_length: float
        light_Width: float
        light_Radius: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        shadowColorMapEnable: bool
        shadowColor: MXSWrapperBase
        lightAffectsShadow: bool
        useGlobalShadowSettings: bool
        shadowProjectorMap: None
        hotspot: float
        falloff: float
        showCone: bool
        webfile: str
        xRotation: float
        yRotation: float
        zRotation: float
        ...
    class Targetcamera(camera):
        type: MXSWrapperBase
        fov: float
        nearrange: float
        farrange: float
        nearclip: float
        near_clip: float
        farclip: float
        far_clip: float
        mpassEnabled: bool
        mpassRenderPerPass: bool
        curFOV: float
        fovType: int
        orthoProjection: bool
        showCone: bool
        showHorizon: bool
        showRanges: bool
        clipManually: bool
        mpassEffect: MXSWrapperBase
        ...
    class Targetobject(GeometryClass):
        ...
    class Teapot(GeometryClass):
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInRadius: float
        radius: float
        segs: int
        smooth: bool
        body: bool
        handle: bool
        spout: bool
        lid: bool
        mapcoords: bool
        ...
    class Tee(shape):
        steps: int
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        typeIn_x: float
        typeIn_y: float
        typeIn_z: float
        typeIn_Length: float
        typeIn_Width: float
        typeIn_Thickness: float
        typeIn_Radius: float
        typeIn_creationMethod: bool
        tee_length: float
        tee_width: float
        tee_thickness: float
        tee_radius: float
        ...
    class TempObjectClass(TemporaryMergeNodeObjectClass):
        ...
    class TemporaryMergeNodeObjectClass(MAXWrapper):
        ...
    class Terrain(GeometryClass):
        display: int
        update: int
        retriangulate: bool
        numOps: int
        stitchBorder: bool
        horizSimplification: int
        vertSimplification: int
        form: int
        ...
    class Test_Icon(helper):
        Visible_Icon: bool
        Icon_Type: int
        Icon_Parameter_1: float
        Icon_Parameter_2: float
        Icon_Parameter_3: float
        Color_Coordinated: bool
        Auto_Update: bool
        SubOperators: MXSWrapperBase
        Selected_SubOperators: MXSWrapperBase
        groups: MXSWrapperBase
        Enable_By_Switch: bool
        Default_Width: int
        Default_Offset: int
        Default_Height: int
        Default_Range_Type: int
        Default_Range_Min: float
        Default_Range_Max: float
        Activity_Type: int
        Time_On: int
        Time_Off: int
        Animatable_Active: bool
        PDView_Origin_X: int
        PDView_Origin_Y: int
        PDView_Width: int
        PDView_Height: int
        PDView_Divider: int
        PDView_Show_Depot: bool
        PDView_Description_Type: int
        PDView_Show_Parameters: bool
        Use_Dynamic_Names_For_New: bool
        Auto_Update_On_Data_View_Close: bool
        Repeats: int
        ...
    class TexOutputClass(material):
        ...
    class TexSkyLight(light):
        multiplier: float
        color: MXSWrapperBase
        rays_per_sample: int
        ray_Bias: float
        on: bool
        castShadows: bool
        sky_color_map: None
        sky_color_map_on: bool
        sky_color_map_amt: float
        sky_mode: int
        ...
    class Texmaps_RaytraceMtl(ReferenceMaker):
        ...
    class TextBaselineManipulator(helper):
        ...
    class TextBevelProfileCurve(ReferenceMaker):
        ...
    class TextDisplayOnlyManipulator(helper):
        ...
    class TextKerningManipulator(helper):
        ...
    class TextMap(textureMap):
        filter: bool
        mipmap: bool
        monoOutput: int
        rgbOutput: int
        applycrop: bool
        croporplace: int
        crop_u: float
        crop_v: float
        crop_w: float
        crop_h: float
        jitter: bool
        jitteramt: float
        alphaSource: int
        coords: MXSWrapperBase
        output: MXSWrapperBase
        restype: int
        finiteresolution: int
        textobject: None
        outlinecolor: MXSWrapperBase
        fillcolor: MXSWrapperBase
        bgcolor: MXSWrapperBase
        fillbg: bool
        glyphoption: int
        filledcharacters: bool
        outlinedcharacters: bool
        outlinewidth: float
        boundstype: int
        manualwidth: float
        manualheight: float
        stricthierarchy: bool
        boundsobject: None
        renderchildren: bool
        renderroot: bool
        mergeshapes: bool
        usefillcolor: bool
        hwbitmapsize: int
        ...
    class TextObject2(GeometryClass):
        interpolationsteps: int
        optimize: int
        adaptive: int
        layouttype: int
        Plane: int
        length: float
        width: float
        alignment: int
        size: float
        tracking: float
        leading: float
        vScale: float
        hscale: float
        generateGeometry: int
        elementType: int
        charKerningOffset: MXSWrapperBase
        charBaselineOffset: MXSWrapperBase
        charXScale: MXSWrapperBase
        charYScale: MXSWrapperBase
        extrudeamount: float
        extrudesegments: int
        applybevel: bool
        beveldepth: float
        usebevelwidth: bool
        bevelwidth: float
        bevelsteps: int
        bevelpush: float
        beveloptimize: bool
        capStart: int
        capstartconstrain: bool
        capEnd: int
        capendconstrain: bool
        capType: int
        startcapmaterial: int
        startbevelmaterial: int
        sidematerial: int
        endbevelmaterial: int
        endcapmaterial: int
        beveloffset: float
        macroname: MXSWrapperBase
        macrovalue: MXSWrapperBase
        UpAxis: int
        axisFlip: bool
        nodeElements: MXSWrapperBase
        nodeElementsCenters: MXSWrapperBase
        ...
    class TextPlus(GeometryClass):
        interpolationsteps: int
        optimize: int
        adaptive: int
        layouttype: int
        Plane: int
        length: float
        width: float
        alignment: int
        size: float
        tracking: float
        leading: float
        vScale: float
        hscale: float
        generateGeometry: int
        elementType: int
        charKerningOffset: MXSWrapperBase
        charBaselineOffset: MXSWrapperBase
        charXScale: MXSWrapperBase
        charYScale: MXSWrapperBase
        extrudeamount: float
        extrudesegments: int
        applybevel: bool
        beveldepth: float
        usebevelwidth: bool
        bevelwidth: float
        bevelsteps: int
        bevelpush: float
        beveloptimize: bool
        capStart: int
        capstartconstrain: bool
        capEnd: int
        capendconstrain: bool
        capType: int
        startcapmaterial: int
        startbevelmaterial: int
        sidematerial: int
        endbevelmaterial: int
        endcapmaterial: int
        beveloffset: float
        macroname: MXSWrapperBase
        macrovalue: MXSWrapperBase
        UpAxis: int
        axisFlip: bool
        nodeElements: MXSWrapperBase
        nodeElementsCenters: MXSWrapperBase
        ...
    class TextTrackingManipulator(helper):
        ...
    class TextUniformScaleManipulator(helper):
        ...
    class TextXScaleManipulator(helper):
        ...
    class TextYScaleManipulator(helper):
        ...
    class Text_Baseline_Manipulator(helper):
        ...
    class Text_Display_Only_Manipulator(helper):
        ...
    class Text_Kerning_Manipulator(helper):
        ...
    class Text_Tracking_Manipulator(helper):
        ...
    class Text_Uniform_Scale_Manipulator(helper):
        ...
    class Text_X_Scale_Manipulator(helper):
        ...
    class Text_Y_Scale_Manipulator(helper):
        ...
    class TextureClass(Value):
        ...
    class TextureObjMask(textureMap):
        coords: MXSWrapperBase
        object: None
        color0: MXSWrapperBase
        color1: MXSWrapperBase
        transitionrange: float
        subtex0: None
        subtex1: None
        map1Enabled: bool
        map2Enabled: bool
        displaceamount: float
        displacetex: None
        displaceEnabled: bool
        transitionbias: float
        ...
    class Texture_Sky(light):
        multiplier: float
        color: MXSWrapperBase
        rays_per_sample: int
        ray_Bias: float
        on: bool
        castShadows: bool
        sky_color_map: None
        sky_color_map_on: bool
        sky_color_map_amt: float
        sky_mode: int
        ...
    class Thin_Wall_Refraction(textureMap):
        blur: float
        thicknessOffset: float
        bumpMapEffect: float
        applyBlur: bool
        nthframe: int
        useEnviroment: bool
        frame: int
        ...
    class This_Data(ReferenceTarget):
        ...
    class TimeSensor(helper):
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
    class TopBottom(material):
        topMaterial: MXSWrapperBase
        bottomMaterial: MXSWrapperBase
        map1Enabled: bool
        map2Enabled: bool
        Blend: float
        position: float
        Coordinates: int
        ...
    class Torus(GeometryClass):
        sliceon: bool
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInRadius1: float
        typeInRadius2: float
        radius1: float
        radius2: float
        tubeRotation: float
        tubeTwist: float
        segs: int
        sides: int
        smooth: int
        slice: bool
        sliceto: float
        slicefrom: float
        mapcoords: bool
        ...
    class Torus_Knot(GeometryClass):
        smooth: int
        radius: float
        sides: int
        Twist: float
        U_Tile: float
        V_Tile: float
        segments: int
        radius2: float
        p: float
        q: float
        Lump_Offset: float
        Eccentricity: float
        Lumps: float
        Lump_Height: float
        Base_Curve: int
        Gen_UV: int
        Warp_Height: float
        Warp_Count: float
        U_Offset: float
        V_Offset: float
        ...
    class TouchSensor(helper):
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
        Priority: int
        duration: int
        easeIn: float
        easeOut: float
        functionName: str
        script: None
        to: None
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
    class Trim_Extend(modifier):
        ...
    class TrueType(BezierFontLoaderClass):
        ...
    class Tube(GeometryClass):
        sliceon: bool
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInRadius1: float
        typeInRadius2: float
        typeInHeight: float
        radius1: float
        radius2: float
        height: float
        sides: int
        capsegs: int
        heightsegs: int
        smooth: bool
        slice: bool
        slicefrom: float
        sliceto: float
        mapcoords: bool
        ...
    class TurboSmooth(modifier):
        iterations: int
        useRenderIterations: bool
        renderIterations: int
        isolineDisplay: bool
        explicitNormals: bool
        smoothResult: bool
        sepByMats: bool
        sepBySmGroups: bool
        update: int
        ...
    class TurnOffMCGProfiling(MAXScriptFunction):
        ...
    class TurnOnMCGProfiling(MAXScriptFunction):
        ...
    class TurnOnMacroRecorderContext(MAXScriptFunction):
        ...
    class TurnToSeq(MAXScriptFunction):
        ...
    class Turn_to_Mesh(modifier):
        useInvisibleEdges: bool
        selectionConversion: int
        useSoftSelection: bool
        selectionLevel: int
        ...
    class Turn_to_Patch(modifier):
        quadsToQuads: bool
        selectionConversion: int
        useSoftSelection: int
        selectionLevel: int
        ...
    class Turn_to_Poly(modifier):
        keepConvex: bool
        limitPolySize: bool
        maxPolySize: int
        requirePlanar: bool
        planarThresh: float
        removeMidEdgeVertices: bool
        selectionConversion: int
        useSoftSelection: bool
        selectionLevel: int
        ...
    class Twist(modifier):
        axis: int
        bias: float
        angle: float
        limit: bool
        upperlimit: float
        lowerlimit: float
        ...
    class UConstraint(helper):
        body0: None
        body1: None
        helpersize: float
        linearModeX: int
        linearModeY: int
        linearModeZ: int
        linearPosition: float
        linearRestitution: float
        linearSpring: float
        linearDamping: float
        swing1Mode: int
        swing1Angle: float
        swing1Restitution: float
        swing1Spring: float
        swing1Damping: float
        swing2Mode: int
        swing2Angle: float
        swing2Restitution: float
        swing2Spring: float
        swing2Damping: float
        twistMode: int
        twistAngleLow: float
        twistAngleHigh: float
        twistRestitutionLow: float
        twistRestitutionHigh: float
        twistSpringLow: float
        twistSpringHigh: float
        twistDampingLow: float
        twistDampingHigh: float
        posSpring: float
        posDamping: float
        swingSpring: float
        swingDamping: float
        twistSpring: float
        twistDamping: float
        Collision: bool
        breakable: bool
        maxForce: float
        maxTorque: float
        gearing: bool
        gearRatio: float
        useProjection: bool
        projectionMode: int
        projectionDist: float
        projectionAngle: float
        childAttachPoint: MXSWrapperBase
        childInitialTwist: float
        showVisualizer: bool
        useAcceleration: bool
        useHardLimits: bool
        ...
    class UDeflector(SpacewarpObject):
        Bounce: float
        bounceVar: float
        chaos: float
        radius: float
        friction: float
        inheritVelocity: float
        ...
    class UDeflectorMod(SpacewarpModifier):
        ...
    class UIAccessor(Interface):
        ...
    class UOmniFlect(SpacewarpObject):
        timeOn: MXSWrapperBase
        timeOff: MXSWrapperBase
        affects: float
        Bounce: float
        bounceVar: float
        chaos: float
        friction: float
        inheritVelocity: float
        refracts: float
        deceleration: float
        decelVar: float
        Refraction: float
        refractionVar: float
        diffusion: float
        diffusionVar: float
        radius: float
        Spawn: float
        passVelocity: float
        passVelocityVar: float
        ...
    class UOmniFlectMod(SpacewarpModifier):
        ...
    class USetup(Primitive):
        ...
    class UTypeStair(GeometryClass):
        StepType: int
        GenerateStringers: bool
        GenerateCarriage: bool
        GenerateInsideRailing: bool
        GenerateOutsideRailing: bool
        Stepwidth: float
        StepThickness: float
        GenerateMapping: bool
        StepDepth_X: bool
        StepDepth: float
        StepHeight: float
        StepCount: int
        StringerDepth: float
        StringerWidth: float
        StringerOffset: float
        StringerSpringFloor: bool
        CarriageWidth: float
        CarriageIntOffs: float
        CarriageExtOffs: float
        CarriageSpace: float
        CarriageCount: int
        CarriageContext: int
        CarriageSpacingType: int
        CarriageHeight: float
        CarriageSpringFloor: bool
        RailingHeight: float
        RailingOffs: float
        RailingSegments: int
        RailingRadius: float
        direction: int
        length: float
        length2: float
        UpperOffset: float
        ...
    class UVGenClass(material):
        ...
    class UVWUnwrap(modifier):
        texMapList: MXSWrapperBase
        checkerMaterial: MXSWrapperBase
        baseMaterial: None
        texMapIDList: MXSWrapperBase
        gridSnap: bool
        vertexSnap: bool
        edgeSnap: bool
        showImageAlpha: bool
        renderuv_width: int
        renderuv_height: int
        renderuv_edgeColor: MXSWrapperBase
        renderuv_edgealpha: float
        renderuv_seamColor: MXSWrapperBase
        renderuv_visibleedges: bool
        renderuv_invisibleedges: bool
        renderuv_seamedges: bool
        renderuv_showframebuffer: bool
        renderuv_force2sided: bool
        renderuv_fillmode: int
        renderuv_fillalpha: float
        renderuv_fillColor: MXSWrapperBase
        renderuv_showoverlap: bool
        renderuv_overlapColor: MXSWrapperBase
        quick_map_preview: bool
        quick_map_align: int
        baseMaterial_list: MXSWrapperBase
        splinemap_node: None
        splinemap_manualseams: bool
        splinemap_projectiontype: int
        splinemap_display: bool
        splinemap_uscale: float
        splinemap_vscale: float
        splinemap_uoffset: float
        splinemap_voffset: float
        localDistortion: bool
        splinemap_iterations: int
        splinemap_resampleCount: int
        splinemap_advanceMethod: int
        toolBarVisible: bool
        buttonpanel_visible: bool
        buttonpanel_width: int
        buttonpanel_height1: int
        buttonpanel_height2: int
        weldOnlyShared: bool
        groupName: MXSWrapperBase
        groupDensity: MXSWrapperBase
        groupDisplay: bool
        autoPin: bool
        filterPin: bool
        peelAutoEdit: bool
        TextureCheckerMaterial: None
        ...
    class UVW_Mapping_Add(modifier):
        ...
    class UVW_Mapping_Clear(modifier):
        mapID: int
        ...
    class UVW_Mapping_Paste(modifier):
        ...
    class UVW_Remove(UtilityPlugin):
        ...
    class UVW_Xform(modifier):
        U_Tile: float
        V_Tile: float
        U_Flip: int
        V_Flip: int
        W_Flip: int
        W_Offset: float
        Rotation_Angle: float
        Rotation_Center: int
        U_Offset: float
        V_Offset: float
        W_Tile: float
        Map_or_Vertex_Color: int
        Map_Channel: int
        ...
    class U_Type_Stair(GeometryClass):
        StepType: int
        GenerateStringers: bool
        GenerateCarriage: bool
        GenerateInsideRailing: bool
        GenerateOutsideRailing: bool
        Stepwidth: float
        StepThickness: float
        GenerateMapping: bool
        StepDepth_X: bool
        StepDepth: float
        StepHeight: float
        StepCount: int
        StringerDepth: float
        StringerWidth: float
        StringerOffset: float
        StringerSpringFloor: bool
        CarriageWidth: float
        CarriageIntOffs: float
        CarriageExtOffs: float
        CarriageSpace: float
        CarriageCount: int
        CarriageContext: int
        CarriageSpacingType: int
        CarriageHeight: float
        CarriageSpringFloor: bool
        RailingHeight: float
        RailingOffs: float
        RailingSegments: int
        RailingRadius: float
        direction: int
        length: float
        length2: float
        UpperOffset: float
        ...
    class UiCustomization(Interface):
        ...
    class UndefinedClass(Value):
        ...
    class UnsuppliedClass(Value):
        ...
    class Unwrap_UVW(modifier):
        texMapList: MXSWrapperBase
        checkerMaterial: MXSWrapperBase
        baseMaterial: None
        texMapIDList: MXSWrapperBase
        gridSnap: bool
        vertexSnap: bool
        edgeSnap: bool
        showImageAlpha: bool
        renderuv_width: int
        renderuv_height: int
        renderuv_edgeColor: MXSWrapperBase
        renderuv_edgealpha: float
        renderuv_seamColor: MXSWrapperBase
        renderuv_visibleedges: bool
        renderuv_invisibleedges: bool
        renderuv_seamedges: bool
        renderuv_showframebuffer: bool
        renderuv_force2sided: bool
        renderuv_fillmode: int
        renderuv_fillalpha: float
        renderuv_fillColor: MXSWrapperBase
        renderuv_showoverlap: bool
        renderuv_overlapColor: MXSWrapperBase
        quick_map_preview: bool
        quick_map_align: int
        baseMaterial_list: MXSWrapperBase
        splinemap_node: None
        splinemap_manualseams: bool
        splinemap_projectiontype: int
        splinemap_display: bool
        splinemap_uscale: float
        splinemap_vscale: float
        splinemap_uoffset: float
        splinemap_voffset: float
        localDistortion: bool
        splinemap_iterations: int
        splinemap_resampleCount: int
        splinemap_advanceMethod: int
        toolBarVisible: bool
        buttonpanel_visible: bool
        buttonpanel_width: int
        buttonpanel_height1: int
        buttonpanel_height2: int
        weldOnlyShared: bool
        groupName: MXSWrapperBase
        groupDensity: MXSWrapperBase
        groupDisplay: bool
        autoPin: bool
        filterPin: bool
        peelAutoEdit: bool
        TextureCheckerMaterial: None
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
    class Uvwmap(modifier):
        axis: int
        height: float
        length: float
        width: float
        channel: int
        cap: bool
        mapChannel: int
        maptype: int
        utile: float
        vtile: float
        wtile: float
        uflip: bool
        vflip: bool
        wflip: bool
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
    class VDM(textureMap):
        mult_spin: float
        vector_map_enabled: bool
        Vector_Map: None
        vector_map_is_hdr: bool
        method: int
        ...
    class VFB_Rollout_Bottom(RolloutClass):
        ...
    class VFB_Rollout_TopLeft(RolloutClass):
        ...
    class VFB_Rollout_TopRight(RolloutClass):
        ...
    class VIZ_Radiosity(RadiosityEffect):
        radInitialQuality: float
        radGlobalRefineSteps: int
        radSelectionRefineSteps: int
        radFiltering: int
        radProcessObjectRefineSteps: bool
        radDisplayInViewport: bool
        radProcessInRenderOnly: bool
        radDirectFiltering: int
        meshingEnabled: bool
        meshingSize: float
        useAdaptiveMeshing: bool
        minimumMeshSize: float
        initialMeshSize: float
        contrastThreshold: float
        includePointLights: bool
        includeLinearLights: bool
        includeAreaLights: bool
        includeSelfEmittingLights: bool
        shootDirectLights: bool
        includeSkylight: bool
        minimumSelfEmittingSize: float
        lightPaintingIntensity: float
        lightPaintingPressure: float
        lightUnitsUsed: int
        rmRegather: bool
        rmReuseDirectIllumination: bool
        rmRaysPerSample: int
        rmFilterRadius: float
        rmClampEnabled: bool
        rmClampValue: float
        rmAdaptiveEnabled: bool
        rmSampleSpacing: int
        rmMinSampleSpacing: int
        rmSubdivisionContrast: float
        rmShowSamples: bool
        statNumFaces: int
        statRefineIterations: int
        statSolutionQuality: float
        statNumGeomObjects: int
        statNumLightObjects: int
        statMeshSize: float
        elapsedTime: int
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
        type: int
        Angle_X: float
        Angle_Y: float
        Angle_Z: float
        Axial_Radius: float
        Bearing: float
        Coord_X: float
        Coord_Y: float
        Coord_Z: float
        Float_X: float
        Float_Y: float
        Float_Z: float
        Latitude: float
        Percent_X: float
        Percent_Y: float
        Percent_Z: float
        radius: float
        Use_Length_Variation: bool
        Use_Divergence: bool
        Angle_Variation: float
        Float_Variation: float
        Length_Variation: float
        Percent_Variation: float
        Divergence: float
        Use_As_Speed_Value: bool
        Units_Per_Type: int
        Sync_Type: int
        Random_Seed: int
        Use_E1: bool
        Use_E2: bool
        Use_E3: bool
        Use_E4: bool
        Use_E5: bool
        Use_E6: bool
        Use_E7: bool
        Use_As_Acceleration: bool
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        Input_5: None
        Input_6: None
        Input_7: None
        ...
    class VectorField(SpacewarpObject):
        length: float
        width: float
        height: float
        lenSegs: int
        widSegs: int
        hgtSegs: int
        showLattice: bool
        showRange: bool
        showVectors: bool
        showSurfSamps: bool
        vecScale: float
        iconSize: float
        strength: float
        falloff: float
        direction: int
        pull: float
        object: None
        range: float
        resolution: int
        flipFaces: bool
        blendStart: float
        blendFalloff: float
        blendWidSegs: int
        blendLenSegs: int
        blendHgtSegs: int
        ...
    class VectorMap(textureMap):
        vectorfile: str
        filter: bool
        mipmap: bool
        monoOutput: int
        rgbOutput: int
        applycrop: bool
        croporplace: int
        crop_u: float
        crop_v: float
        crop_w: float
        crop_h: float
        jitter: bool
        jitteramt: float
        alphaSource: int
        coords: MXSWrapperBase
        output: MXSWrapperBase
        restype: int
        finiteresolution: int
        patternname: int
        patternrepeat: float
        linewidth: float
        linecolor: MXSWrapperBase
        backColor: MXSWrapperBase
        linecap: int
        pdf_page: float
        continous: bool
        transition_mode: int
        transparent: bool
        pagecolor: MXSWrapperBase
        transitiondir: int
        preview: bool
        memlimit: int
        hwbitmapsize: int
        ...
    class Vector_Displacement(textureMap):
        mult_spin: float
        vector_map_enabled: bool
        Vector_Map: None
        vector_map_is_hdr: bool
        method: int
        ...
    class Vector_Field(SpacewarpObject):
        length: float
        width: float
        height: float
        lenSegs: int
        widSegs: int
        hgtSegs: int
        showLattice: bool
        showRange: bool
        showVectors: bool
        showSurfSamps: bool
        vecScale: float
        iconSize: float
        strength: float
        falloff: float
        direction: int
        pull: float
        object: None
        range: float
        resolution: int
        flipFaces: bool
        blendStart: float
        blendFalloff: float
        blendWidSegs: int
        blendLenSegs: int
        blendHgtSegs: int
        ...
    class Vector_Field_Modifier(SpacewarpModifier):
        ...
    class Vector_Map(textureMap):
        vectorfile: str
        filter: bool
        mipmap: bool
        monoOutput: int
        rgbOutput: int
        applycrop: bool
        croporplace: int
        crop_u: float
        crop_v: float
        crop_w: float
        crop_h: float
        jitter: bool
        jitteramt: float
        alphaSource: int
        coords: MXSWrapperBase
        output: MXSWrapperBase
        restype: int
        finiteresolution: int
        patternname: int
        patternrepeat: float
        linewidth: float
        linecolor: MXSWrapperBase
        backColor: MXSWrapperBase
        linecap: int
        pdf_page: float
        continous: bool
        transition_mode: int
        transparent: bool
        pagecolor: MXSWrapperBase
        transitiondir: int
        preview: bool
        memlimit: int
        hwbitmapsize: int
        ...
    class VertexColor(textureMap):
        map: int
        subid: int
        ...
    class VertexPaint(modifier):
        ignoreBackfacing: bool
        mapChannel: int
        layerMode: str
        layerOpacity: float
        layerIsolated: bool
        surviveCondense: bool
        lightingModel: int
        colorBy: int
        castShadows: bool
        useMaps: bool
        useRadiosity: bool
        radiosityOnly: bool
        hideUnselSubobjs: bool
        radiosityOption: int
        ...
    class VertexPaintTool(Primitive):
        ...
    class VertexSelection(Value):
        ...
    class VertexWeld(modifier):
        threshold: float
        ...
    class Vertex_Color(textureMap):
        map: int
        subid: int
        ...
    class Vertex_Colors(modifier):
        ...
    class Vertex_Paint_Floater(UserDataTypeClass):
        ...
    class Vertex_Paint_Startup_GUP(GlobalUtilityPlugin):
        ...
    class Vertex_Weld(modifier):
        threshold: float
        ...
    class Vertical_Horizontal_Turn(MAXWrapper):
        ...
    class Video(filter):
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
        enabled: bool
        effect: int
        dxStdMat: bool
        SaveFXFile: None
        ...
    class ViewportSSB(Interface):
        ...
    class VisualMSUtil(UtilityPlugin):
        ...
    class Visual_MAXScript(UtilityPlugin):
        ...
    class Vol__Select(modifier):
        level: int
        method: int
        type: int
        volume: int
        invert: bool
        node: None
        texture: None
        map: int
        mapChannel: int
        matID: int
        smGroup: int
        autofit: bool
        UseAffectRegion: bool
        falloff: float
        pinch: float
        bubble: float
        ...
    class VolumeHelper(helper):
        volumeType: int
        size: float
        sectionRadius: float
        meshNode: None
        color: MXSWrapperBase
        ...
    class VolumeSelect(modifier):
        level: int
        method: int
        type: int
        volume: int
        invert: bool
        node: None
        texture: None
        map: int
        mapChannel: int
        matID: int
        smGroup: int
        autofit: bool
        UseAffectRegion: bool
        falloff: float
        pinch: float
        bubble: float
        ...
    class Volume_Fog(atmospheric):
        invert: int
        size: float
        phase: float
        density: float
        fog_color: MXSWrapperBase
        fog_background: int
        exponential: int
        Uniformity: float
        Max_Steps: int
        Wind_Direction: int
        Wind_Strength: float
        Soften_Gizmo_Edges: float
        Noise_Type: int
        Levels: float
        Low_Threshold: float
        High_Threshold: float
        Step_Size: float
        ...
    class Volume_Light(atmospheric):
        invert: int
        size: float
        Noise_On: int
        phase: float
        Samples: int
        density: float
        fog_color: MXSWrapperBase
        exponential: int
        Uniformity: float
        Wind_Direction: int
        Wind_Strength: float
        Max_Light: float
        Min_Light: float
        Atten__Start: float
        Atten__End: float
        Filter_Shadows: int
        Auto_Sample: int
        Link_To_Light: int
        Use_Attenuation_Color: int
        Attenuation_Color_Multiplier: float
        Noise_Amount: float
        Attenuation_Color: MXSWrapperBase
        Noise_Type: int
        Levels: float
        Low_Threshold: float
        High_Threshold: float
        ...
    class Vortex(SpacewarpObject):
        timeOn: MXSWrapperBase
        timeOff: MXSWrapperBase
        axialStrength: float
        axialRange: float
        axialFallOff: float
        axialDamping: float
        rotationStrength: float
        rotationRange: float
        rotationFallOff: float
        rotationDamping: float
        radialStrength: float
        radialRange: float
        radialFallOff: float
        radialDamping: float
        taperStrength: float
        taperShape: float
        direction: int
        rangeless: bool
        iconSize: float
        ...
    class VortexMod(SpacewarpModifier):
        ...
    class VrmlImp(ImporterPlugin):
        ...
    class Vsp_Gantry(GeometryClass):
        length: float
        height: float
        radius: float
        dia: float
        xfall: float
        matID: int
        lStyle: bool
        signals: bool
        numberOfSignals: int
        SignalGap: float
        flipSignals: bool
        SignalOffset: float
        ...
    class Vsp_GantryNZ(GeometryClass):
        length: float
        height: float
        radius: float
        dia: float
        xfall: float
        matID: int
        lStyle: bool
        signals: bool
        numberOfSignals: int
        SignalGap: float
        flipSignals: bool
        SignalOffset: float
        ...
    class Vsp_GantrySA(GeometryClass):
        length: float
        height: float
        radius: float
        dia: float
        xfall: float
        matID: int
        lStyle: bool
        signals: bool
        numberOfSignals: int
        SignalGap: float
        flipSignals: bool
        SignalOffset: float
        ...
    class Vsp_Lamp(GeometryClass):
        height: float
        depth: float
        kink1: float
        kink2: float
        matID: int
        onOff: bool
        dia1: float
        dia2: float
        radius: float
        armLen: float
        angle: float
        headScaleX: float
        headScaleY: float
        leftArm: bool
        rightArm: bool
        ...
    class Vsp_Sign(GeometryClass):
        width: float
        height: float
        type: int
        pHeight: float
        depth: float
        posts: int
        edgeoff: float
        ...
    class Vsp_Signal(GeometryClass):
        width: float
        height: float
        type: int
        pHeight: float
        depth: float
        posts: int
        edgeoff: float
        numphases: int
        curPhase: int
        ...
    class Vsp_Symb(GeometryClass):
        width: float
        height: float
        type: int
        ...
    class Vsp_Tree(GeometryClass):
        NFaces: int
        height: float
        width: float
        matID: int
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
        height: float
        width: float
        Justification: int
        Generate_Mapping_Coords: int
        ...
    class WallRepelBehavior(ReferenceTarget):
        name: str
        repelGrids: MXSWrapperBase
        repelMethod: int
        repelDirection: int
        useDistance: bool
        innerDistance: float
        outerDistance: float
        falloff: float
        showDistance: bool
        gridSpacing: int
        gridEnd: bool
        forceColor: MXSWrapperBase
        displayForce: bool
        ...
    class WallSeekBehavior(ReferenceTarget):
        name: str
        seekGrid: None
        seekMethod: int
        seekDirection: int
        useDistance: bool
        innerDistance: float
        outerDistance: float
        falloff: float
        showDistance: bool
        gridSpacing: int
        gridEnd: bool
        forceColor: MXSWrapperBase
        displayForce: bool
        ...
    class Wall_Repel_Behavior(ReferenceTarget):
        name: str
        repelGrids: MXSWrapperBase
        repelMethod: int
        repelDirection: int
        useDistance: bool
        innerDistance: float
        outerDistance: float
        falloff: float
        showDistance: bool
        gridSpacing: int
        gridEnd: bool
        forceColor: MXSWrapperBase
        displayForce: bool
        ...
    class Wall_Seek_Behavior(ReferenceTarget):
        name: str
        seekGrid: None
        seekMethod: int
        seekDirection: int
        useDistance: bool
        innerDistance: float
        outerDistance: float
        falloff: float
        showDistance: bool
        gridSpacing: int
        gridEnd: bool
        forceColor: MXSWrapperBase
        displayForce: bool
        ...
    class WalledRectangle(shape):
        steps: int
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        typeIn_x: float
        typeIn_y: float
        typeIn_z: float
        typeIn_Length: float
        typeIn_Width: float
        typeIn_Thickness: float
        typeIn_Radius: float
        typeIn_radius2: float
        typeIn_creationMethod: bool
        wrect_length: float
        wrect_width: float
        wrect_thickness: float
        wrect_radius: float
        wrect_radius2: float
        wrect_syncCornerFillets: bool
        ...
    class WanderBehavior(ReferenceTarget):
        name: str
        Period: int
        periodDeviation: float
        turnAngle: float
        turnPeriod: float
        turnPeriodDeviation: float
        seed: int
        forceColor: MXSWrapperBase
        displayForce: bool
        ...
    class Wander_Behavior(ReferenceTarget):
        name: str
        Period: int
        periodDeviation: float
        turnAngle: float
        turnPeriod: float
        turnPeriodDeviation: float
        seed: int
        forceColor: MXSWrapperBase
        displayForce: bool
        ...
    class Water(textureMap):
        numWaveSets: int
        waveRadius: float
        waveLenMin: float
        waveLenMax: float
        Amplitude: float
        phase: float
        Distribution: int
        RandomSeed: int
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1: None
        map2: None
        map1on: bool
        map2on: bool
        coords: MXSWrapperBase
        ...
    class Wave(modifier):
        amplitude1: float
        amplitude2: float
        wavelength: float
        phase: float
        decay: float
        ...
    class WaveMaster(SoundClass):
        ...
    class WaveObject(SoundClass):
        ...
    class Wavebinding(SpacewarpModifier):
        ...
    class Waveform_Float(floatController):
        ...
    class WeightShift(floatController):
        ...
    class WeightedNormalsMod(modifier):
        useAreaWeight: bool
        useAngleWeight: bool
        useConvexAngle: bool
        blendingCoeff: float
        smoothingCoeff: float
        relaxationCoeff: float
        boundaryCoeff: float
        smoothingIterLimit: int
        useSmoothingGroups: bool
        useHardEdgeAngle: bool
        hardEdgeAngle: float
        displayNormals: bool
        normalLength: float
        snapToLargestFace: bool
        useUVSeams: bool
        uvChannelIndex: int
        useTotalCoplanarArea: bool
        ...
    class Weighted_Normals(modifier):
        useAreaWeight: bool
        useAngleWeight: bool
        useConvexAngle: bool
        blendingCoeff: float
        smoothingCoeff: float
        relaxationCoeff: float
        boundaryCoeff: float
        smoothingIterLimit: int
        useSmoothingGroups: bool
        useHardEdgeAngle: bool
        hardEdgeAngle: float
        displayNormals: bool
        normalLength: float
        snapToLargestFace: bool
        useUVSeams: bool
        uvChannelIndex: int
        useTotalCoplanarArea: bool
        ...
    class WelcomeScreenLaunchCount(Primitive):
        ...
    class WelcomeScreenShowAtStartup(Primitive):
        ...
    class Welder(modifier):
        threshold: float
        weldMethod: int
        dontWeldSelectedEdges: bool
        ...
    class WideFlange(shape):
        steps: int
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        typeIn_x: float
        typeIn_y: float
        typeIn_z: float
        typeIn_Length: float
        typeIn_Width: float
        typeIn_Thickness: float
        typeIn_Radius: float
        typeIn_creationMethod: bool
        wide_flange_length: float
        wide_flange_width: float
        wide_flange_thickness: float
        wide_flange_radius: float
        ...
    class Wind(SpacewarpObject):
        strength: float
        decay: float
        windtype: int
        turbulence: float
        frequency: float
        scale: MXSWrapperBase
        iconSize: float
        hoopson: bool
        ...
    class Windbinding(SpacewarpModifier):
        ...
    class WindowStream(Value):
        ...
    class Wipe(VideoPostFilter):
        ...
    class WireFloat(floatController):
        ...
    class WirePoint3(point3Controller):
        ...
    class WirePoint4(point4Controller):
        ...
    class WirePosition(positionController):
        ...
    class WireRotation(rotationController):
        ...
    class WireScale(scaleController):
        ...
    class WireframeFragment(GraphicsFragmentPlugin):
        ...
    class Wood(textureMap):
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
        size: float
        subdivideDoEnforceQuality: bool
        subdivideDoSubdivideTriangles: bool
        showAllTriangles: bool
        subdivideMaxSteinerPoints: int
        subdivideQuadAreaRatio: float
        subdivideDiagonalRatio: float
        subdivideNumBuckets: int
        subdivideDoFormQuads: bool
        subdivideRefinementType: int
        manualupdate: int
        remeshType: int
        preserveMeshData: bool
        preservedMapIndex: int
        preserveSharpEdgesByAngle: bool
        preservedSharpEdgeAngle: float
        delaunaySize: float
        delaunayRelaxationCoeff: float
        delaunayRelaxationIterations: int
        adaptiveEdgeLength: float
        adaptiveRegularity: float
        adaptiveThreshold: float
        variableCurvatureEdgeLength: float
        variableCurvatureRegularity: float
        variableCurvatureThreshold: float
        variableCurvatureVariableDensity: float
        variableCurvatureIterations: int
        variableCurvatureTransition: float
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
        name: str
        spaceWarp: None
        forceColor: MXSWrapperBase
        displayForce: bool
        ...
    class XForm(modifier):
        PreserveNormals: bool
        ...
    class XFormMat(Generic):
        ...
    class XMLImp2(ImporterPlugin):
        ...
    class XORRenderFragment(GraphicsFragmentPlugin):
        ...
    class XRefAtmosWrapper(atmospheric):
        ...
    class XRefObject(System):
        ...
    class XRefScene(Value):
        ...
    class XRef_Controller(Matrix3Controller):
        ...
    class XRef_Material(material):
        enableOverride: bool
        overrideMaterial: MXSWrapperBase
        ...
    class XRefmaterial(material):
        enableOverride: bool
        overrideMaterial: MXSWrapperBase
        ...
    class XYZGenClass(material):
        ...
    class YUV(BitmapIO):
        ...
    class ZRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        zMin: float
        zMax: float
        zUpdate: bool
        ...
    class Z_Depth(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        zMin: float
        zMax: float
        zUpdate: bool
        ...
    class Zero(MappedGeneric):
        ...
    class Zoom(Generic):
        ...
    class abs(Generic):
        ...
    class acos(Generic):
        ...
    class actionMan(Interface):
        ...
    class add(VideoPostFilter):
        ...
    class addAndWeld(NodeGeneric):
        ...
    class addAtmospheric(Primitive):
        ...
    class addEaseCurve(MappedGeneric):
        ...
    class addEffect(Primitive):
        ...
    class addKnot(NodeGeneric):
        ...
    class addModifier(NodeGeneric):
        ...
    class addModifierWithLocalData(Primitive):
        ...
    class addMorphTarget(Primitive):
        ...
    class addMultiplierCurve(Generic):
        ...
    class addNURBSSet(Primitive):
        ...
    class addNewKey(MappedGeneric):
        ...
    class addNewNoteKey(Generic):
        ...
    class addNewSpline(NodeGeneric):
        ...
    class addNoteTrack(Primitive):
        ...
    class addPluginRollouts(Generic):
        ...
    class addRollout(Primitive):
        ...
    class addScript(BipedGeneric):
        ...
    class addSnippet(BipedGeneric):
        ...
    class addTrackViewController(Primitive):
        ...
    class addTranInfo(BipedGeneric):
        ...
    class addTransition(BipedGeneric):
        ...
    class affectRegionVal(Primitive):
        ...
    class aiPBParameter(ReferenceTarget):
        ...
    class aiPBParameterClassDescCreator(Interface):
        ...
    class ai_Max_Adapter(textureMap):
        ...
    class ai_Max_UVGenerator(textureMap):
        ...
    class ai_abs(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        ...
    class ai_add(textureMap):
        input1: MXSWrapperBase
        input1_connected: bool
        input1_shader: None
        input2: MXSWrapperBase
        input2_connected: bool
        input2_shader: None
        ...
    class ai_ambient_occlusion(textureMap):
        Samples: int
        spread: float
        spread_connected: bool
        spread_shader: None
        near_clip: float
        near_clip_connected: bool
        near_clip_shader: None
        far_clip: float
        far_clip_connected: bool
        far_clip_shader: None
        falloff: float
        falloff_connected: bool
        falloff_shader: None
        black: MXSWrapperBase
        black_connected: bool
        black_shader: None
        white: MXSWrapperBase
        white_connected: bool
        white_shader: None
        normal: MXSWrapperBase
        normal_connected: bool
        normal_shader: None
        invert_normals: bool
        trace_set: str
        inclusive: bool
        self_only: bool
        ...
    class ai_aov_read_float(textureMap):
        aov_name: str
        ...
    class ai_aov_read_int(textureMap):
        aov_name: str
        ...
    class ai_aov_read_rgb(textureMap):
        aov_name: str
        ...
    class ai_aov_read_rgba(textureMap):
        aov_name: str
        ...
    class ai_aov_write_float(material):
        passthrough: None
        aov_input: float
        aov_input_connected: bool
        aov_input_shader: None
        aov_name: str
        blend_opacity: bool
        ...
    class ai_aov_write_int(material):
        passthrough: None
        aov_input: int
        aov_input_connected: bool
        aov_input_shader: None
        aov_name: str
        ...
    class ai_aov_write_rgb(material):
        passthrough: None
        aov_input: MXSWrapperBase
        aov_input_connected: bool
        aov_input_shader: None
        aov_name: str
        blend_opacity: bool
        ...
    class ai_aov_write_rgba(material):
        passthrough: None
        aov_input: MXSWrapperBase
        aov_input_connected: bool
        aov_input_shader: None
        aov_name: str
        blend_opacity: bool
        ...
    class ai_aov_write_vector(material):
        passthrough: None
        aov_input: MXSWrapperBase
        aov_input_connected: bool
        aov_input_shader: None
        aov_name: str
        blend_opacity: bool
        ...
    class ai_atan(textureMap):
        y: MXSWrapperBase
        y_connected: bool
        y_shader: None
        x: MXSWrapperBase
        x_connected: bool
        x_shader: None
        units: int
        ...
    class ai_atmosphere_volume(material):
        density: float
        density_connected: bool
        density_shader: None
        Samples: int
        Eccentricity: float
        eccentricity_connected: bool
        eccentricity_shader: None
        attenuation: float
        attenuation_connected: bool
        attenuation_shader: None
        affect_camera: float
        affect_camera_connected: bool
        affect_camera_shader: None
        affect_diffuse: float
        affect_diffuse_connected: bool
        affect_diffuse_shader: None
        affect_specular: float
        affect_specular_connected: bool
        affect_specular_shader: None
        rgb_density: MXSWrapperBase
        rgb_density_connected: bool
        rgb_density_shader: None
        rgb_attenuation: MXSWrapperBase
        rgb_attenuation_connected: bool
        rgb_attenuation_shader: None
        ...
    class ai_barndoor(textureMap):
        ...
    class ai_blackbody(textureMap):
        temperature: float
        temperature_connected: bool
        temperature_shader: None
        normalize: bool
        intensity: float
        intensity_connected: bool
        intensity_shader: None
        ...
    class ai_blackman_harris_filter(textureMap):
        ...
    class ai_box_filter(textureMap):
        ...
    class ai_bump2d(textureMap):
        bump_map: float
        bump_map_connected: bool
        bump_map_shader: None
        bump_height: float
        bump_height_connected: bool
        bump_height_shader: None
        normal: MXSWrapperBase
        normal_connected: bool
        normal_shader: None
        ...
    class ai_bump3d(textureMap):
        bump_map: float
        bump_map_connected: bool
        bump_map_shader: None
        bump_height: float
        bump_height_connected: bool
        bump_height_shader: None
        epsilon: float
        epsilon_connected: bool
        epsilon_shader: None
        normal: MXSWrapperBase
        normal_connected: bool
        normal_shader: None
        ...
    class ai_cache(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        ...
    class ai_camera_projection(textureMap):
        projection_color: MXSWrapperBase
        projection_color_connected: bool
        projection_color_shader: None
        offscreen_color: MXSWrapperBase
        offscreen_color_connected: bool
        offscreen_color_shader: None
        Mask: float
        mask_connected: bool
        mask_shader: None
        camera: None
        camera_connected: bool
        camera_shader: None
        aspect_ratio: float
        front_facing: bool
        back_facing: bool
        use_shading_normal: bool
        coord_space: int
        pref_name: str
        p: MXSWrapperBase
        P_connected: bool
        P_shader: None
        ...
    class ai_car_paint(material):
        base: float
        base_connected: bool
        base_shader: None
        base_color: MXSWrapperBase
        base_color_connected: bool
        base_color_shader: None
        base_roughness: float
        base_roughness_connected: bool
        base_roughness_shader: None
        Specular: float
        specular_connected: bool
        specular_shader: None
        specular_color: MXSWrapperBase
        specular_color_connected: bool
        specular_color_shader: None
        specular_flip_flop: MXSWrapperBase
        specular_flip_flop_connected: bool
        specular_flip_flop_shader: None
        specular_light_facing: MXSWrapperBase
        specular_light_facing_connected: bool
        specular_light_facing_shader: None
        specular_falloff: float
        specular_falloff_connected: bool
        specular_falloff_shader: None
        specular_roughness: float
        specular_roughness_connected: bool
        specular_roughness_shader: None
        specular_IOR: float
        specular_IOR_connected: bool
        specular_IOR_shader: None
        transmission_color: MXSWrapperBase
        transmission_color_connected: bool
        transmission_color_shader: None
        flake_color: MXSWrapperBase
        flake_color_connected: bool
        flake_color_shader: None
        flake_flip_flop: MXSWrapperBase
        flake_flip_flop_connected: bool
        flake_flip_flop_shader: None
        flake_light_facing: MXSWrapperBase
        flake_light_facing_connected: bool
        flake_light_facing_shader: None
        flake_falloff: float
        flake_falloff_connected: bool
        flake_falloff_shader: None
        flake_roughness: float
        flake_roughness_connected: bool
        flake_roughness_shader: None
        flake_IOR: float
        flake_IOR_connected: bool
        flake_IOR_shader: None
        flake_scale: float
        flake_scale_connected: bool
        flake_scale_shader: None
        flake_density: float
        flake_density_connected: bool
        flake_density_shader: None
        flake_layers: int
        flake_layers_connected: bool
        flake_layers_shader: None
        flake_normal_randomize: float
        flake_normal_randomize_connected: bool
        flake_normal_randomize_shader: None
        flake_coord_space: int
        pref_name: str
        coat: float
        coat_connected: bool
        coat_shader: None
        coat_color: MXSWrapperBase
        coat_color_connected: bool
        coat_color_shader: None
        coat_roughness: float
        coat_roughness_connected: bool
        coat_roughness_shader: None
        coat_ior: float
        coat_IOR_connected: bool
        coat_IOR_shader: None
        coat_normal: MXSWrapperBase
        coat_normal_connected: bool
        coat_normal_shader: None
        ...
    class ai_catrom_filter(textureMap):
        ...
    class ai_cell_noise(textureMap):
        pattern: int
        additive: bool
        Octaves: int
        randomness: float
        randomness_connected: bool
        randomness_shader: None
        Lacunarity: float
        lacunarity_connected: bool
        lacunarity_shader: None
        Amplitude: float
        amplitude_connected: bool
        amplitude_shader: None
        scale: MXSWrapperBase
        scale_connected: bool
        scale_shader: None
        offset: MXSWrapperBase
        offset_connected: bool
        offset_shader: None
        coord_space: int
        pref_name: str
        p: MXSWrapperBase
        P_connected: bool
        P_shader: None
        time: float
        time_connected: bool
        time_shader: None
        color: MXSWrapperBase
        color_connected: bool
        color_shader: None
        palette: MXSWrapperBase
        palette_connected: bool
        palette_shader: None
        density: float
        density_connected: bool
        density_shader: None
        ...
    class ai_checkerboard(textureMap):
        color1: MXSWrapperBase
        color1_connected: bool
        color1_shader: None
        color2: MXSWrapperBase
        color2_connected: bool
        color2_shader: None
        u_frequency: float
        u_frequency_connected: bool
        u_frequency_shader: None
        v_frequency: float
        v_frequency_connected: bool
        v_frequency_shader: None
        U_Offset: float
        u_offset_connected: bool
        u_offset_shader: None
        V_Offset: float
        v_offset_connected: bool
        v_offset_shader: None
        contrast: float
        contrast_connected: bool
        contrast_shader: None
        filter_strength: float
        filter_strength_connected: bool
        filter_strength_shader: None
        filter_offset: float
        filter_offset_connected: bool
        filter_offset_shader: None
        UVSet: str
        ...
    class ai_clamp(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        mode: int
        mode_connected: bool
        mode_shader: None
        min: float
        min_connected: bool
        min_shader: None
        max: float
        max_connected: bool
        max_shader: None
        min_color: MXSWrapperBase
        min_color_connected: bool
        min_color_shader: None
        max_color: MXSWrapperBase
        max_color_connected: bool
        max_color_shader: None
        ...
    class ai_clip_geo(material):
        intersection: None
        trace_set: str
        inclusive: bool
        ...
    class ai_closest_filter(textureMap):
        ...
    class ai_collection(textureMap):
        ...
    class ai_color_convert(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        to: int
        ...
    class ai_color_correct(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        alpha_is_luminance: bool
        alpha_multiply: float
        alpha_multiply_connected: bool
        alpha_multiply_shader: None
        alpha_add: float
        alpha_add_connected: bool
        alpha_add_shader: None
        invert: bool
        invert_alpha: bool
        gamma: float
        gamma_connected: bool
        gamma_shader: None
        hue_shift: float
        hue_shift_connected: bool
        hue_shift_shader: None
        saturation: float
        saturation_connected: bool
        saturation_shader: None
        contrast: float
        contrast_connected: bool
        contrast_shader: None
        contrast_pivot: float
        contrast_pivot_connected: bool
        contrast_pivot_shader: None
        exposure: float
        exposure_connected: bool
        exposure_shader: None
        multiply: MXSWrapperBase
        multiply_connected: bool
        multiply_shader: None
        add: MXSWrapperBase
        add_connected: bool
        add_shader: None
        Mask: float
        mask_connected: bool
        mask_shader: None
        ...
    class ai_color_jitter(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        data_input: int
        data_input_connected: bool
        data_input_shader: None
        data_gain_min: float
        data_gain_min_connected: bool
        data_gain_min_shader: None
        data_gain_max: float
        data_gain_max_connected: bool
        data_gain_max_shader: None
        data_hue_min: float
        data_hue_min_connected: bool
        data_hue_min_shader: None
        data_hue_max: float
        data_hue_max_connected: bool
        data_hue_max_shader: None
        data_saturation_min: float
        data_saturation_min_connected: bool
        data_saturation_min_shader: None
        data_saturation_max: float
        data_saturation_max_connected: bool
        data_saturation_max_shader: None
        data_seed: int
        data_seed_connected: bool
        data_seed_shader: None
        proc_gain_min: float
        proc_gain_min_connected: bool
        proc_gain_min_shader: None
        proc_gain_max: float
        proc_gain_max_connected: bool
        proc_gain_max_shader: None
        proc_hue_min: float
        proc_hue_min_connected: bool
        proc_hue_min_shader: None
        proc_hue_max: float
        proc_hue_max_connected: bool
        proc_hue_max_shader: None
        proc_saturation_min: float
        proc_saturation_min_connected: bool
        proc_saturation_min_shader: None
        proc_saturation_max: float
        proc_saturation_max_connected: bool
        proc_saturation_max_shader: None
        proc_seed: int
        proc_seed_connected: bool
        proc_seed_shader: None
        obj_gain_min: float
        obj_gain_min_connected: bool
        obj_gain_min_shader: None
        obj_gain_max: float
        obj_gain_max_connected: bool
        obj_gain_max_shader: None
        obj_hue_min: float
        obj_hue_min_connected: bool
        obj_hue_min_shader: None
        obj_hue_max: float
        obj_hue_max_connected: bool
        obj_hue_max_shader: None
        obj_saturation_min: float
        obj_saturation_min_connected: bool
        obj_saturation_min_shader: None
        obj_saturation_max: float
        obj_saturation_max_connected: bool
        obj_saturation_max_shader: None
        obj_seed: int
        obj_seed_connected: bool
        obj_seed_shader: None
        face_gain_min: float
        face_gain_min_connected: bool
        face_gain_min_shader: None
        face_gain_max: float
        face_gain_max_connected: bool
        face_gain_max_shader: None
        face_hue_min: float
        face_hue_min_connected: bool
        face_hue_min_shader: None
        face_hue_max: float
        face_hue_max_connected: bool
        face_hue_max_shader: None
        face_saturation_min: float
        face_saturation_min_connected: bool
        face_saturation_min_shader: None
        face_saturation_max: float
        face_saturation_max_connected: bool
        face_saturation_max_shader: None
        face_seed: int
        face_seed_connected: bool
        face_seed_shader: None
        face_mode: int
        ...
    class ai_compare(textureMap):
        test: int
        input1: float
        input1_connected: bool
        input1_shader: None
        input2: float
        input2_connected: bool
        input2_shader: None
        ...
    class ai_complement(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        ...
    class ai_complex_ior(textureMap):
        ...
    class ai_composite(textureMap):
        ...
    class ai_contour_filter(textureMap):
        ...
    class ai_cross(textureMap):
        input1: MXSWrapperBase
        input1_connected: bool
        input1_shader: None
        input2: MXSWrapperBase
        input2_connected: bool
        input2_shader: None
        ...
    class ai_cryptomatte(textureMap):
        sidecar_manifests: bool
        sidecar_manifests_connected: bool
        sidecar_manifests_shader: None
        cryptomatte_depth: int
        cryptomatte_depth_connected: bool
        cryptomatte_depth_shader: None
        strip_obj_namespaces: bool
        strip_obj_namespaces_connected: bool
        strip_obj_namespaces_shader: None
        strip_mat_namespaces: bool
        strip_mat_namespaces_connected: bool
        strip_mat_namespaces_shader: None
        aov_crypto_asset: str
        aov_crypto_asset_connected: bool
        aov_crypto_asset_shader: None
        aov_crypto_object: str
        aov_crypto_object_connected: bool
        aov_crypto_object_shader: None
        aov_crypto_material: str
        aov_crypto_material_connected: bool
        aov_crypto_material_shader: None
        preview_in_exr: bool
        preview_in_exr_connected: bool
        preview_in_exr_shader: None
        process_maya: bool
        process_maya_connected: bool
        process_maya_shader: None
        process_paths: bool
        process_paths_connected: bool
        process_paths_shader: None
        process_obj_path_pipes: bool
        process_obj_path_pipes_connected: bool
        process_obj_path_pipes_shader: None
        process_mat_path_pipes: bool
        process_mat_path_pipes_connected: bool
        process_mat_path_pipes_shader: None
        process_legacy: bool
        process_legacy_connected: bool
        process_legacy_shader: None
        user_crypto_aov_0: str
        user_crypto_aov_0_connected: bool
        user_crypto_aov_0_shader: None
        user_crypto_src_0: str
        user_crypto_src_0_connected: bool
        user_crypto_src_0_shader: None
        user_crypto_aov_1: str
        user_crypto_aov_1_connected: bool
        user_crypto_aov_1_shader: None
        user_crypto_src_1: str
        user_crypto_src_1_connected: bool
        user_crypto_src_1_shader: None
        user_crypto_aov_2: str
        user_crypto_aov_2_connected: bool
        user_crypto_aov_2_shader: None
        user_crypto_src_2: str
        user_crypto_src_2_connected: bool
        user_crypto_src_2_shader: None
        user_crypto_aov_3: str
        user_crypto_aov_3_connected: bool
        user_crypto_aov_3_shader: None
        user_crypto_src_3: str
        user_crypto_src_3_connected: bool
        user_crypto_src_3_shader: None
        ...
    class ai_cryptomatte_filter(textureMap):
        ...
    class ai_curvature(textureMap):
        output: int
        Samples: int
        radius: float
        radius_connected: bool
        radius_shader: None
        spread: float
        spread_connected: bool
        spread_shader: None
        threshold: float
        threshold_connected: bool
        threshold_shader: None
        bias: float
        bias_connected: bool
        bias_shader: None
        multiply: float
        multiply_connected: bool
        multiply_shader: None
        trace_set: str
        inclusive: bool
        self_only: bool
        ...
    class ai_denoise_optix_filter(textureMap):
        ...
    class ai_diff_filter(textureMap):
        ...
    class ai_disable(textureMap):
        ...
    class ai_divide(textureMap):
        input1: MXSWrapperBase
        input1_connected: bool
        input1_shader: None
        input2: MXSWrapperBase
        input2_connected: bool
        input2_shader: None
        ...
    class ai_dot(textureMap):
        input1: MXSWrapperBase
        input1_connected: bool
        input1_shader: None
        input2: MXSWrapperBase
        input2_connected: bool
        input2_shader: None
        ...
    class ai_exp(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        ...
    class ai_facing_ratio(textureMap):
        bias: float
        gain: float
        linear: bool
        invert: bool
        ...
    class ai_farthest_filter(textureMap):
        ...
    class ai_flakes(textureMap):
        scale: float
        scale_connected: bool
        scale_shader: None
        density: float
        density_connected: bool
        density_shader: None
        step: float
        step_connected: bool
        step_shader: None
        depth: float
        depth_connected: bool
        depth_shader: None
        ior: float
        IOR_connected: bool
        IOR_shader: None
        normal_randomize: float
        normal_randomize_connected: bool
        normal_randomize_shader: None
        coord_space: int
        pref_name: str
        output_space: int
        ...
    class ai_flat(textureMap):
        color: MXSWrapperBase
        color_connected: bool
        color_shader: None
        ...
    class ai_float_to_int(textureMap):
        Input: float
        input_connected: bool
        input_shader: None
        mode: int
        mode_connected: bool
        mode_shader: None
        ...
    class ai_float_to_matrix(textureMap):
        input_00: float
        input_00_connected: bool
        input_00_shader: None
        input_01: float
        input_01_connected: bool
        input_01_shader: None
        input_02: float
        input_02_connected: bool
        input_02_shader: None
        input_03: float
        input_03_connected: bool
        input_03_shader: None
        input_10: float
        input_10_connected: bool
        input_10_shader: None
        input_11: float
        input_11_connected: bool
        input_11_shader: None
        input_12: float
        input_12_connected: bool
        input_12_shader: None
        input_13: float
        input_13_connected: bool
        input_13_shader: None
        input_20: float
        input_20_connected: bool
        input_20_shader: None
        input_21: float
        input_21_connected: bool
        input_21_shader: None
        input_22: float
        input_22_connected: bool
        input_22_shader: None
        input_23: float
        input_23_connected: bool
        input_23_shader: None
        input_30: float
        input_30_connected: bool
        input_30_shader: None
        input_31: float
        input_31_connected: bool
        input_31_shader: None
        input_32: float
        input_32_connected: bool
        input_32_shader: None
        input_33: float
        input_33_connected: bool
        input_33_shader: None
        ...
    class ai_float_to_rgb(textureMap):
        r: float
        r_connected: bool
        r_shader: None
        g: float
        g_connected: bool
        g_shader: None
        b: float
        B_connected: bool
        B_shader: None
        ...
    class ai_float_to_rgba(textureMap):
        r: float
        r_connected: bool
        r_shader: None
        g: float
        g_connected: bool
        g_shader: None
        b: float
        B_connected: bool
        B_shader: None
        a: float
        A_connected: bool
        A_shader: None
        ...
    class ai_fog(material):
        distance: float
        distance_connected: bool
        distance_shader: None
        height: float
        height_connected: bool
        height_shader: None
        color: MXSWrapperBase
        color_connected: bool
        color_shader: None
        ground_point: MXSWrapperBase
        ground_point_connected: bool
        ground_point_shader: None
        ground_normal: MXSWrapperBase
        ground_normal_connected: bool
        ground_normal_shader: None
        ...
    class ai_fraction(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        ...
    class ai_gaussian_filter(textureMap):
        ...
    class ai_gobo(textureMap):
        ...
    class ai_hair(material):
        ...
    class ai_heatmap_filter(textureMap):
        ...
    class ai_image(textureMap):
        filename: str
        Image_Frame_Number: int
        color_space: int
        filter: int
        mipmap_bias: int
        single_channel: bool
        start_channel: int
        swrap: int
        twrap: int
        sscale: float
        tscale: float
        sflip: bool
        tflip: bool
        sOffset: float
        toffset: float
        swap_st: bool
        uvcoords: MXSWrapperBase
        uvcoords_connected: bool
        uvcoords_shader: None
        UVSet: int
        multiply: MXSWrapperBase
        multiply_connected: bool
        multiply_shader: None
        offset: MXSWrapperBase
        offset_connected: bool
        offset_shader: None
        ignore_missing_textures: bool
        missing_texture_color: MXSWrapperBase
        missing_texture_color_connected: bool
        missing_texture_color_shader: None
        ...
    class ai_imager_color_correct(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        Enable: bool
        layer_selection: str
        main_saturation: float
        main_contrast: float
        main_gamma: float
        main_gain: MXSWrapperBase
        main_offset: MXSWrapperBase
        shadows_saturation: float
        shadows_contrast: float
        shadows_gamma: float
        shadows_gain: MXSWrapperBase
        shadows_offset: MXSWrapperBase
        midtones_saturation: float
        midtones_contrast: float
        midtones_gamma: float
        midtones_gain: MXSWrapperBase
        midtones_offset: MXSWrapperBase
        highlights_saturation: float
        highlights_contrast: float
        highlights_gamma: float
        highlights_gain: MXSWrapperBase
        highlights_offset: MXSWrapperBase
        ...
    class ai_imager_exposure(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        Enable: bool
        layer_selection: str
        exposure: float
        ...
    class ai_imager_lens_effects(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        Enable: bool
        layer_selection: str
        vignetting: float
        ...
    class ai_imager_tonemap(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        Enable: bool
        layer_selection: str
        mode: int
        filmic_toe_strength: float
        filmic_toe_length: float
        filmic_shoulder_strength: float
        filmic_shoulder_length: float
        filmic_shoulder_angle: float
        reinhard_highlights: float
        reinhard_shadows: float
        preserve_saturation: bool
        gamma: float
        ...
    class ai_imager_white_balance(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        Enable: bool
        layer_selection: str
        mode: int
        temperature: float
        illuminant: int
        custom: MXSWrapperBase
        ...
    class ai_include_graph(textureMap):
        ...
    class ai_is_finite(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        ...
    class ai_lambert(material):
        Kd: float
        Kd_connected: bool
        Kd_shader: None
        Kd_color: MXSWrapperBase
        Kd_color_connected: bool
        Kd_color_shader: None
        opacity: MXSWrapperBase
        opacity_connected: bool
        opacity_shader: None
        normal: MXSWrapperBase
        normal_connected: bool
        normal_shader: None
        ...
    class ai_layer_float(textureMap):
        enable1: bool
        name1: str
        input1: float
        input1_connected: bool
        input1_shader: None
        mix1: float
        mix1_connected: bool
        mix1_shader: None
        enable2: bool
        name2: str
        input2: float
        input2_connected: bool
        input2_shader: None
        mix2: float
        mix2_connected: bool
        mix2_shader: None
        enable3: bool
        name3: str
        input3: float
        input3_connected: bool
        input3_shader: None
        mix3: float
        mix3_connected: bool
        mix3_shader: None
        enable4: bool
        name4: str
        input4: float
        input4_connected: bool
        input4_shader: None
        mix4: float
        mix4_connected: bool
        mix4_shader: None
        enable5: bool
        name5: str
        input5: float
        input5_connected: bool
        input5_shader: None
        mix5: float
        mix5_connected: bool
        mix5_shader: None
        enable6: bool
        name6: str
        input6: float
        input6_connected: bool
        input6_shader: None
        mix6: float
        mix6_connected: bool
        mix6_shader: None
        enable7: bool
        name7: str
        input7: float
        input7_connected: bool
        input7_shader: None
        mix7: float
        mix7_connected: bool
        mix7_shader: None
        enable8: bool
        name8: str
        input8: float
        input8_connected: bool
        input8_shader: None
        mix8: float
        mix8_connected: bool
        mix8_shader: None
        ...
    class ai_layer_rgba(textureMap):
        enable1: bool
        name1: str
        input1: MXSWrapperBase
        input1_connected: bool
        input1_shader: None
        mix1: float
        mix1_connected: bool
        mix1_shader: None
        operation1: int
        alpha_operation1: int
        enable2: bool
        name2: str
        input2: MXSWrapperBase
        input2_connected: bool
        input2_shader: None
        mix2: float
        mix2_connected: bool
        mix2_shader: None
        operation2: int
        alpha_operation2: int
        enable3: bool
        name3: str
        input3: MXSWrapperBase
        input3_connected: bool
        input3_shader: None
        mix3: float
        mix3_connected: bool
        mix3_shader: None
        operation3: int
        alpha_operation3: int
        enable4: bool
        name4: str
        input4: MXSWrapperBase
        input4_connected: bool
        input4_shader: None
        mix4: float
        mix4_connected: bool
        mix4_shader: None
        operation4: int
        alpha_operation4: int
        enable5: bool
        name5: str
        input5: MXSWrapperBase
        input5_connected: bool
        input5_shader: None
        mix5: float
        mix5_connected: bool
        mix5_shader: None
        operation5: int
        alpha_operation5: int
        enable6: bool
        name6: str
        input6: MXSWrapperBase
        input6_connected: bool
        input6_shader: None
        mix6: float
        mix6_connected: bool
        mix6_shader: None
        operation6: int
        alpha_operation6: int
        enable7: bool
        name7: str
        input7: MXSWrapperBase
        input7_connected: bool
        input7_shader: None
        mix7: float
        mix7_connected: bool
        mix7_shader: None
        operation7: int
        alpha_operation7: int
        enable8: bool
        name8: str
        input8: MXSWrapperBase
        input8_connected: bool
        input8_shader: None
        mix8: float
        mix8_connected: bool
        mix8_shader: None
        operation8: int
        alpha_operation8: int
        clamp: bool
        ...
    class ai_layer_shader(material):
        enable1: bool
        name1: str
        input1: None
        mix1: float
        mix1_connected: bool
        mix1_shader: None
        enable2: bool
        name2: str
        input2: None
        mix2: float
        mix2_connected: bool
        mix2_shader: None
        enable3: bool
        name3: str
        input3: None
        mix3: float
        mix3_connected: bool
        mix3_shader: None
        enable4: bool
        name4: str
        input4: None
        mix4: float
        mix4_connected: bool
        mix4_shader: None
        enable5: bool
        name5: str
        input5: None
        mix5: float
        mix5_connected: bool
        mix5_shader: None
        enable6: bool
        name6: str
        input6: None
        mix6: float
        mix6_connected: bool
        mix6_shader: None
        enable7: bool
        name7: str
        input7: None
        mix7: float
        mix7_connected: bool
        mix7_shader: None
        enable8: bool
        name8: str
        input8: None
        mix8: float
        mix8_connected: bool
        mix8_shader: None
        ...
    class ai_length(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        mode: int
        ...
    class ai_light_blocker(textureMap):
        ...
    class ai_light_decay(textureMap):
        ...
    class ai_log(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        base: MXSWrapperBase
        base_connected: bool
        base_shader: None
        ...
    class ai_materialx(textureMap):
        ...
    class ai_matrix_interpolate(textureMap):
        ...
    class ai_matrix_multiply_vector(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        type: int
        matrix: MXSWrapperBase
        matrix_connected: bool
        matrix_shader: None
        ...
    class ai_matrix_transform(textureMap):
        transform_order: int
        Rotation_Type: int
        units: int
        rotation_order: int
        rotation: MXSWrapperBase
        rotation_connected: bool
        rotation_shader: None
        axis: MXSWrapperBase
        axis_connected: bool
        axis_shader: None
        angle: float
        angle_connected: bool
        angle_shader: None
        Translate: MXSWrapperBase
        translate_connected: bool
        translate_shader: None
        scale: MXSWrapperBase
        scale_connected: bool
        scale_shader: None
        pivot: MXSWrapperBase
        pivot_connected: bool
        pivot_shader: None
        ...
    class ai_matte(material):
        passthrough: None
        color: MXSWrapperBase
        color_connected: bool
        color_shader: None
        opacity: MXSWrapperBase
        opacity_connected: bool
        opacity_shader: None
        ...
    class ai_max(textureMap):
        input1: MXSWrapperBase
        input1_connected: bool
        input1_shader: None
        input2: MXSWrapperBase
        input2_connected: bool
        input2_shader: None
        ...
    class ai_merge(textureMap):
        ...
    class ai_min(textureMap):
        input1: MXSWrapperBase
        input1_connected: bool
        input1_shader: None
        input2: MXSWrapperBase
        input2_connected: bool
        input2_shader: None
        ...
    class ai_mitnet_filter(textureMap):
        ...
    class ai_mix_rgba(textureMap):
        input1: MXSWrapperBase
        input1_connected: bool
        input1_shader: None
        input2: MXSWrapperBase
        input2_connected: bool
        input2_shader: None
        Mix: float
        mix_connected: bool
        mix_shader: None
        ...
    class ai_mix_shader(material):
        mode: int
        Mix: float
        mix_connected: bool
        mix_shader: None
        add_transparency: bool
        shader1: None
        shader2: None
        ...
    class ai_modulo(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        divisor: MXSWrapperBase
        divisor_connected: bool
        divisor_shader: None
        ...
    class ai_motion_vector(textureMap):
        raw: bool
        time0: float
        time1: float
        max_displace: float
        ...
    class ai_multiply(textureMap):
        input1: MXSWrapperBase
        input1_connected: bool
        input1_shader: None
        input2: MXSWrapperBase
        input2_connected: bool
        input2_shader: None
        ...
    class ai_negate(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        ...
    class ai_noise(textureMap):
        Octaves: int
        distortion: float
        distortion_connected: bool
        distortion_shader: None
        Lacunarity: float
        lacunarity_connected: bool
        lacunarity_shader: None
        Amplitude: float
        amplitude_connected: bool
        amplitude_shader: None
        scale: MXSWrapperBase
        scale_connected: bool
        scale_shader: None
        offset: MXSWrapperBase
        offset_connected: bool
        offset_shader: None
        coord_space: int
        pref_name: str
        p: MXSWrapperBase
        P_connected: bool
        P_shader: None
        time: float
        time_connected: bool
        time_shader: None
        color1: MXSWrapperBase
        color1_connected: bool
        color1_shader: None
        color2: MXSWrapperBase
        color2_connected: bool
        color2_shader: None
        mode: int
        ...
    class ai_normal_map(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        tangent: MXSWrapperBase
        tangent_connected: bool
        tangent_shader: None
        normal: MXSWrapperBase
        normal_connected: bool
        normal_shader: None
        order: int
        invert_x: bool
        invert_y: bool
        invert_z: bool
        color_to_signed: bool
        tangent_space: bool
        strength: float
        strength_connected: bool
        strength_shader: None
        ...
    class ai_normalize(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        ...
    class ai_osl(textureMap):
        ...
    class ai_passthrough(material):
        passthrough: None
        eval1: None
        eval2: None
        eval3: None
        eval4: None
        eval5: None
        eval6: None
        eval7: None
        eval8: None
        eval9: None
        eval10: None
        eval11: None
        eval12: None
        eval13: None
        eval14: None
        eval15: None
        eval16: None
        eval17: None
        eval18: None
        eval19: None
        eval20: None
        normal: MXSWrapperBase
        normal_connected: bool
        normal_shader: None
        ...
    class ai_physical_sky(textureMap):
        turbidity: float
        ground_albedo: MXSWrapperBase
        use_degrees: bool
        elevation: float
        azimuth: float
        sun_direction: MXSWrapperBase
        enable_sun: bool
        sun_size: float
        sun_tint: MXSWrapperBase
        sky_tint: MXSWrapperBase
        intensity: float
        x: MXSWrapperBase
        y: MXSWrapperBase
        z: MXSWrapperBase
        ...
    class ai_pow(textureMap):
        base: MXSWrapperBase
        base_connected: bool
        base_shader: None
        Exponent: MXSWrapperBase
        exponent_connected: bool
        exponent_shader: None
        ...
    class ai_procedural_operator(textureMap):
        ...
    class ai_ramp_float(textureMap):
        type: int
        Input: float
        input_connected: bool
        input_shader: None
        position: MXSWrapperBase
        value: MXSWrapperBase
        interpolation: MXSWrapperBase
        UVSet: str
        use_implicit_uvs: int
        wrap_uvs: bool
        ...
    class ai_ramp_rgb(textureMap):
        type: int
        Input: float
        input_connected: bool
        input_shader: None
        position: MXSWrapperBase
        color: MXSWrapperBase
        interpolation: MXSWrapperBase
        UVSet: str
        use_implicit_uvs: int
        wrap_uvs: bool
        ...
    class ai_random(textureMap):
        input_type: int
        input_int: int
        input_int_connected: bool
        input_int_shader: None
        input_float: float
        input_float_connected: bool
        input_float_shader: None
        input_color: MXSWrapperBase
        input_color_connected: bool
        input_color_shader: None
        seed: int
        seed_connected: bool
        seed_shader: None
        grayscale: bool
        ...
    class ai_range(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        input_min: float
        input_min_connected: bool
        input_min_shader: None
        input_max: float
        input_max_connected: bool
        input_max_shader: None
        output_min: float
        output_min_connected: bool
        output_min_shader: None
        output_max: float
        output_max_connected: bool
        output_max_shader: None
        smoothstep: bool
        contrast: float
        contrast_connected: bool
        contrast_shader: None
        contrast_pivot: float
        contrast_pivot_connected: bool
        contrast_pivot_shader: None
        bias: float
        bias_connected: bool
        bias_shader: None
        gain: float
        gain_connected: bool
        gain_shader: None
        ...
    class ai_ray_switch_rgba(textureMap):
        camera: MXSWrapperBase
        camera_connected: bool
        camera_shader: None
        Shadow: MXSWrapperBase
        shadow_connected: bool
        shadow_shader: None
        diffuse_reflection: MXSWrapperBase
        diffuse_reflection_connected: bool
        diffuse_reflection_shader: None
        diffuse_transmission: MXSWrapperBase
        diffuse_transmission_connected: bool
        diffuse_transmission_shader: None
        specular_reflection: MXSWrapperBase
        specular_reflection_connected: bool
        specular_reflection_shader: None
        specular_transmission: MXSWrapperBase
        specular_transmission_connected: bool
        specular_transmission_shader: None
        volume: MXSWrapperBase
        volume_connected: bool
        volume_shader: None
        ...
    class ai_ray_switch_shader(material):
        camera: None
        Shadow: None
        diffuse_reflection: None
        diffuse_transmission: None
        specular_reflection: None
        specular_transmission: None
        volume: None
        ...
    class ai_reciprocal(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        ...
    class ai_rgb_to_float(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        mode: int
        mode_connected: bool
        mode_shader: None
        ...
    class ai_rgb_to_vector(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        mode: int
        mode_connected: bool
        mode_shader: None
        ...
    class ai_rgba_to_float(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        mode: int
        mode_connected: bool
        mode_shader: None
        ...
    class ai_round_corners(textureMap):
        Samples: int
        radius: float
        radius_connected: bool
        radius_shader: None
        normal: MXSWrapperBase
        normal_connected: bool
        normal_shader: None
        trace_set: str
        inclusive: bool
        self_only: bool
        object_space: bool
        ...
    class ai_set_parameter(textureMap):
        ...
    class ai_set_transform(textureMap):
        ...
    class ai_shadow_matte(textureMap):
        Background: int
        background_connected: bool
        background_shader: None
        shadow_color: MXSWrapperBase
        shadow_color_connected: bool
        shadow_color_shader: None
        shadow_opacity: float
        shadow_opacity_connected: bool
        shadow_opacity_shader: None
        Background_Color: MXSWrapperBase
        background_color_connected: bool
        background_color_shader: None
        diffuse_color: MXSWrapperBase
        diffuse_color_connected: bool
        diffuse_color_shader: None
        diffuse_use_background: bool
        diffuse_intensity: float
        diffuse_intensity_connected: bool
        diffuse_intensity_shader: None
        backlighting: float
        backlighting_connected: bool
        backlighting_shader: None
        indirect_diffuse_enable: bool
        indirect_specular_enable: bool
        specular_color: MXSWrapperBase
        specular_color_connected: bool
        specular_color_shader: None
        specular_intensity: float
        specular_intensity_connected: bool
        specular_intensity_shader: None
        specular_roughness: float
        specular_roughness_connected: bool
        specular_roughness_shader: None
        specular_IOR: float
        specular_IOR_connected: bool
        specular_IOR_shader: None
        alpha_mask: bool
        alpha_mask_connected: bool
        alpha_mask_shader: None
        aov_group: str
        aov_shadow: str
        aov_shadow_diff: str
        aov_shadow_mask: str
        ...
    class ai_shuffle(textureMap):
        color: MXSWrapperBase
        color_connected: bool
        color_shader: None
        alpha: float
        alpha_connected: bool
        alpha_shader: None
        channel_r: int
        channel_g: int
        channel_b: int
        channel_a: int
        negate_r: bool
        negate_g: bool
        negate_b: bool
        negate_a: bool
        ...
    class ai_sign(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        ...
    class ai_sinc_filter(textureMap):
        ...
    class ai_skin(material):
        ...
    class ai_sky(material):
        ...
    class ai_space_transform(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        type: int
        to: int
        tangent: MXSWrapperBase
        tangent_connected: bool
        tangent_shader: None
        normal: MXSWrapperBase
        normal_connected: bool
        normal_shader: None
        normalize: bool
        scale: float
        scale_connected: bool
        scale_shader: None
        ...
    class ai_sqrt(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        ...
    class ai_standard(material):
        ...
    class ai_standard_hair(material):
        base: float
        base_connected: bool
        base_shader: None
        base_color: MXSWrapperBase
        base_color_connected: bool
        base_color_shader: None
        melanin: float
        melanin_connected: bool
        melanin_shader: None
        melanin_redness: float
        melanin_redness_connected: bool
        melanin_redness_shader: None
        melanin_randomize: float
        melanin_randomize_connected: bool
        melanin_randomize_shader: None
        roughness: float
        roughness_connected: bool
        roughness_shader: None
        roughness_azimuthal: float
        roughness_azimuthal_connected: bool
        roughness_azimuthal_shader: None
        roughness_anisotropic: bool
        ior: float
        IOR_connected: bool
        IOR_shader: None
        shift: float
        shift_connected: bool
        shift_shader: None
        specular_tint: MXSWrapperBase
        specular_tint_connected: bool
        specular_tint_shader: None
        specular2_tint: MXSWrapperBase
        specular2_tint_connected: bool
        specular2_tint_shader: None
        transmission_tint: MXSWrapperBase
        transmission_tint_connected: bool
        transmission_tint_shader: None
        Diffuse: float
        diffuse_connected: bool
        diffuse_shader: None
        diffuse_color: MXSWrapperBase
        diffuse_color_connected: bool
        diffuse_color_shader: None
        emission: float
        emission_connected: bool
        emission_shader: None
        emission_color: MXSWrapperBase
        emission_color_connected: bool
        emission_color_shader: None
        opacity: MXSWrapperBase
        opacity_connected: bool
        opacity_shader: None
        indirect_diffuse: float
        indirect_specular: float
        extra_depth: int
        extra_samples: int
        aov_id1: str
        id1: MXSWrapperBase
        id1_connected: bool
        id1_shader: None
        aov_id2: str
        id2: MXSWrapperBase
        id2_connected: bool
        id2_shader: None
        aov_id3: str
        id3: MXSWrapperBase
        id3_connected: bool
        id3_shader: None
        aov_id4: str
        id4: MXSWrapperBase
        id4_connected: bool
        id4_shader: None
        aov_id5: str
        id5: MXSWrapperBase
        id5_connected: bool
        id5_shader: None
        aov_id6: str
        id6: MXSWrapperBase
        id6_connected: bool
        id6_shader: None
        aov_id7: str
        id7: MXSWrapperBase
        id7_connected: bool
        id7_shader: None
        aov_id8: str
        id8: MXSWrapperBase
        id8_connected: bool
        id8_shader: None
        ...
    class ai_standard_surface(material):
        base: float
        base_connected: bool
        base_shader: None
        base_color: MXSWrapperBase
        base_color_connected: bool
        base_color_shader: None
        diffuse_roughness: float
        diffuse_roughness_connected: bool
        diffuse_roughness_shader: None
        Specular: float
        specular_connected: bool
        specular_shader: None
        specular_color: MXSWrapperBase
        specular_color_connected: bool
        specular_color_shader: None
        specular_roughness: float
        specular_roughness_connected: bool
        specular_roughness_shader: None
        specular_IOR: float
        specular_IOR_connected: bool
        specular_IOR_shader: None
        specular_anisotropy: float
        specular_anisotropy_connected: bool
        specular_anisotropy_shader: None
        specular_rotation: float
        specular_rotation_connected: bool
        specular_rotation_shader: None
        metalness: float
        metalness_connected: bool
        metalness_shader: None
        transmission: float
        transmission_connected: bool
        transmission_shader: None
        transmission_color: MXSWrapperBase
        transmission_color_connected: bool
        transmission_color_shader: None
        transmission_depth: float
        transmission_depth_connected: bool
        transmission_depth_shader: None
        transmission_scatter: MXSWrapperBase
        transmission_scatter_connected: bool
        transmission_scatter_shader: None
        transmission_scatter_anisotropy: float
        transmission_scatter_anisotropy_connected: bool
        transmission_scatter_anisotropy_shader: None
        transmission_dispersion: float
        transmission_dispersion_connected: bool
        transmission_dispersion_shader: None
        transmission_extra_roughness: float
        transmission_extra_roughness_connected: bool
        transmission_extra_roughness_shader: None
        transmit_aovs: bool
        subsurface: float
        subsurface_connected: bool
        subsurface_shader: None
        subsurface_color: MXSWrapperBase
        subsurface_color_connected: bool
        subsurface_color_shader: None
        subsurface_radius: MXSWrapperBase
        subsurface_radius_connected: bool
        subsurface_radius_shader: None
        subsurface_scale: float
        subsurface_scale_connected: bool
        subsurface_scale_shader: None
        subsurface_anisotropy: float
        subsurface_anisotropy_connected: bool
        subsurface_anisotropy_shader: None
        subsurface_type: int
        sheen: float
        sheen_connected: bool
        sheen_shader: None
        sheen_color: MXSWrapperBase
        sheen_color_connected: bool
        sheen_color_shader: None
        sheen_roughness: float
        sheen_roughness_connected: bool
        sheen_roughness_shader: None
        thin_walled: bool
        normal: MXSWrapperBase
        normal_connected: bool
        normal_shader: None
        tangent: MXSWrapperBase
        tangent_connected: bool
        tangent_shader: None
        coat: float
        coat_connected: bool
        coat_shader: None
        coat_color: MXSWrapperBase
        coat_color_connected: bool
        coat_color_shader: None
        coat_roughness: float
        coat_roughness_connected: bool
        coat_roughness_shader: None
        coat_ior: float
        coat_IOR_connected: bool
        coat_IOR_shader: None
        coat_anisotropy: float
        coat_anisotropy_connected: bool
        coat_anisotropy_shader: None
        coat_rotation: float
        coat_rotation_connected: bool
        coat_rotation_shader: None
        coat_normal: MXSWrapperBase
        coat_normal_connected: bool
        coat_normal_shader: None
        coat_affect_color: float
        coat_affect_color_connected: bool
        coat_affect_color_shader: None
        coat_affect_roughness: float
        coat_affect_roughness_connected: bool
        coat_affect_roughness_shader: None
        thin_film_thickness: float
        thin_film_thickness_connected: bool
        thin_film_thickness_shader: None
        thin_film_IOR: float
        thin_film_IOR_connected: bool
        thin_film_IOR_shader: None
        emission: float
        emission_connected: bool
        emission_shader: None
        emission_color: MXSWrapperBase
        emission_color_connected: bool
        emission_color_shader: None
        opacity: MXSWrapperBase
        opacity_connected: bool
        opacity_shader: None
        caustics: bool
        internal_reflections: bool
        exit_to_background: bool
        indirect_diffuse: float
        indirect_specular: float
        dielectric_priority: int
        aov_id1: str
        id1: MXSWrapperBase
        id1_connected: bool
        id1_shader: None
        aov_id2: str
        id2: MXSWrapperBase
        id2_connected: bool
        id2_shader: None
        aov_id3: str
        id3: MXSWrapperBase
        id3_connected: bool
        id3_shader: None
        aov_id4: str
        id4: MXSWrapperBase
        id4_connected: bool
        id4_shader: None
        aov_id5: str
        id5: MXSWrapperBase
        id5_connected: bool
        id5_shader: None
        aov_id6: str
        id6: MXSWrapperBase
        id6_connected: bool
        id6_shader: None
        aov_id7: str
        id7: MXSWrapperBase
        id7_connected: bool
        id7_shader: None
        aov_id8: str
        id8: MXSWrapperBase
        id8_connected: bool
        id8_shader: None
        ...
    class ai_standard_volume(material):
        density: float
        density_connected: bool
        density_shader: None
        density_channel: str
        Scatter: float
        scatter_connected: bool
        scatter_shader: None
        scatter_color: MXSWrapperBase
        scatter_color_connected: bool
        scatter_color_shader: None
        scatter_color_channel: str
        scatter_anisotropy: float
        scatter_anisotropy_connected: bool
        scatter_anisotropy_shader: None
        transparent: MXSWrapperBase
        transparent_connected: bool
        transparent_shader: None
        transparent_depth: float
        transparent_channel: str
        emission_mode: int
        emission: float
        emission_connected: bool
        emission_shader: None
        emission_color: MXSWrapperBase
        emission_color_connected: bool
        emission_color_shader: None
        emission_channel: str
        temperature: float
        temperature_connected: bool
        temperature_shader: None
        temperature_channel: str
        blackbody_kelvin: float
        blackbody_kelvin_connected: bool
        blackbody_kelvin_shader: None
        blackbody_intensity: float
        blackbody_intensity_connected: bool
        blackbody_intensity_shader: None
        displacement: MXSWrapperBase
        displacement_connected: bool
        displacement_shader: None
        interpolation: int
        ...
    class ai_state_float(textureMap):
        variable: int
        ...
    class ai_state_int(textureMap):
        variable: int
        ...
    class ai_state_vector(textureMap):
        variable: int
        ...
    class ai_string_replace(textureMap):
        ...
    class ai_subtract(textureMap):
        input1: MXSWrapperBase
        input1_connected: bool
        input1_shader: None
        input2: MXSWrapperBase
        input2_connected: bool
        input2_shader: None
        ...
    class ai_switch_operator(textureMap):
        ...
    class ai_switch_rgba(textureMap):
        index: int
        index_connected: bool
        index_shader: None
        input0: MXSWrapperBase
        input0_connected: bool
        input0_shader: None
        input1: MXSWrapperBase
        input1_connected: bool
        input1_shader: None
        input2: MXSWrapperBase
        input2_connected: bool
        input2_shader: None
        input3: MXSWrapperBase
        input3_connected: bool
        input3_shader: None
        input4: MXSWrapperBase
        input4_connected: bool
        input4_shader: None
        input5: MXSWrapperBase
        input5_connected: bool
        input5_shader: None
        input6: MXSWrapperBase
        input6_connected: bool
        input6_shader: None
        input7: MXSWrapperBase
        input7_connected: bool
        input7_shader: None
        input8: MXSWrapperBase
        input8_connected: bool
        input8_shader: None
        input9: MXSWrapperBase
        input9_connected: bool
        input9_shader: None
        input10: MXSWrapperBase
        input10_connected: bool
        input10_shader: None
        input11: MXSWrapperBase
        input11_connected: bool
        input11_shader: None
        input12: MXSWrapperBase
        input12_connected: bool
        input12_shader: None
        input13: MXSWrapperBase
        input13_connected: bool
        input13_shader: None
        input14: MXSWrapperBase
        input14_connected: bool
        input14_shader: None
        input15: MXSWrapperBase
        input15_connected: bool
        input15_shader: None
        input16: MXSWrapperBase
        input16_connected: bool
        input16_shader: None
        input17: MXSWrapperBase
        input17_connected: bool
        input17_shader: None
        input18: MXSWrapperBase
        input18_connected: bool
        input18_shader: None
        input19: MXSWrapperBase
        input19_connected: bool
        input19_shader: None
        ...
    class ai_switch_shader(material):
        index: int
        index_connected: bool
        index_shader: None
        input0: None
        input1: None
        input2: None
        input3: None
        input4: None
        input5: None
        input6: None
        input7: None
        input8: None
        input9: None
        input10: None
        input11: None
        input12: None
        input13: None
        input14: None
        input15: None
        input16: None
        input17: None
        input18: None
        input19: None
        ...
    class ai_thin_film(textureMap):
        ...
    class ai_toon(textureMap):
        mask_color: MXSWrapperBase
        mask_color_connected: bool
        mask_color_shader: None
        edge_color: MXSWrapperBase
        edge_color_connected: bool
        edge_color_shader: None
        edge_tonemap: MXSWrapperBase
        edge_tonemap_connected: bool
        edge_tonemap_shader: None
        edge_opacity: float
        edge_opacity_connected: bool
        edge_opacity_shader: None
        edge_width_scale: float
        edge_width_scale_connected: bool
        edge_width_scale_shader: None
        silhouette_color: MXSWrapperBase
        silhouette_color_connected: bool
        silhouette_color_shader: None
        silhouette_tonemap: MXSWrapperBase
        silhouette_tonemap_connected: bool
        silhouette_tonemap_shader: None
        silhouette_opacity: float
        silhouette_opacity_connected: bool
        silhouette_opacity_shader: None
        silhouette_width_scale: float
        silhouette_width_scale_connected: bool
        silhouette_width_scale_shader: None
        Priority: int
        enable_silhouette: bool
        ignore_throughput: bool
        Enable: bool
        id_difference: bool
        shader_difference: bool
        uv_threshold: float
        uv_threshold_connected: bool
        uv_threshold_shader: None
        angle_threshold: float
        angle_threshold_connected: bool
        angle_threshold_shader: None
        normal_type: int
        base: float
        base_connected: bool
        base_shader: None
        base_color: MXSWrapperBase
        base_color_connected: bool
        base_color_shader: None
        base_tonemap: MXSWrapperBase
        base_tonemap_connected: bool
        base_tonemap_shader: None
        Specular: float
        specular_connected: bool
        specular_shader: None
        specular_color: MXSWrapperBase
        specular_color_connected: bool
        specular_color_shader: None
        specular_roughness: float
        specular_roughness_connected: bool
        specular_roughness_shader: None
        specular_anisotropy: float
        specular_anisotropy_connected: bool
        specular_anisotropy_shader: None
        specular_rotation: float
        specular_rotation_connected: bool
        specular_rotation_shader: None
        specular_tonemap: MXSWrapperBase
        specular_tonemap_connected: bool
        specular_tonemap_shader: None
        lights: str
        highlight_color: MXSWrapperBase
        highlight_color_connected: bool
        highlight_color_shader: None
        highlight_size: float
        highlight_size_connected: bool
        highlight_size_shader: None
        aov_highlight: str
        rim_light: str
        rim_light_color: MXSWrapperBase
        rim_light_color_connected: bool
        rim_light_color_shader: None
        rim_light_width: float
        rim_light_width_connected: bool
        rim_light_width_shader: None
        rim_light_tint: float
        rim_light_tint_connected: bool
        rim_light_tint_shader: None
        aov_rim_light: str
        transmission: float
        transmission_connected: bool
        transmission_shader: None
        transmission_color: MXSWrapperBase
        transmission_color_connected: bool
        transmission_color_shader: None
        transmission_roughness: float
        transmission_roughness_connected: bool
        transmission_roughness_shader: None
        transmission_anisotropy: float
        transmission_anisotropy_connected: bool
        transmission_anisotropy_shader: None
        transmission_rotation: float
        transmission_rotation_connected: bool
        transmission_rotation_shader: None
        sheen: float
        sheen_connected: bool
        sheen_shader: None
        sheen_color: MXSWrapperBase
        sheen_color_connected: bool
        sheen_color_shader: None
        sheen_roughness: float
        sheen_roughness_connected: bool
        sheen_roughness_shader: None
        emission: float
        emission_connected: bool
        emission_shader: None
        emission_color: MXSWrapperBase
        emission_color_connected: bool
        emission_color_shader: None
        ior: float
        IOR_connected: bool
        IOR_shader: None
        normal: MXSWrapperBase
        normal_connected: bool
        normal_shader: None
        tangent: MXSWrapperBase
        tangent_connected: bool
        tangent_shader: None
        indirect_diffuse: float
        indirect_specular: float
        bump_mode: int
        energy_conserving: bool
        user_id: bool
        aov_prefix: str
        ...
    class ai_trace_set(material):
        passthrough: None
        trace_set: str
        inclusive: bool
        ...
    class ai_triangle_filter(textureMap):
        ...
    class ai_trigo(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        Function: int
        units: int
        frequency: float
        frequency_connected: bool
        frequency_shader: None
        phase: float
        phase_connected: bool
        phase_shader: None
        ...
    class ai_triplanar(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        scale: MXSWrapperBase
        scale_connected: bool
        scale_shader: None
        Rotate: MXSWrapperBase
        rotate_connected: bool
        rotate_shader: None
        offset: MXSWrapperBase
        offset_connected: bool
        offset_shader: None
        coord_space: int
        pref_name: str
        Blend: float
        blend_connected: bool
        blend_shader: None
        cell: bool
        cell_connected: bool
        cell_shader: None
        cell_rotate: float
        cell_rotate_connected: bool
        cell_rotate_shader: None
        cell_blend: float
        cell_blend_connected: bool
        cell_blend_shader: None
        ...
    class ai_two_sided(material):
        front: None
        back: None
        ...
    class ai_user_data_float(textureMap):
        Attribute: str
        default: float
        default_connected: bool
        default_shader: None
        ...
    class ai_user_data_int(textureMap):
        Attribute: str
        default: int
        default_connected: bool
        default_shader: None
        ...
    class ai_user_data_rgb(textureMap):
        Attribute: str
        default: MXSWrapperBase
        default_connected: bool
        default_shader: None
        ...
    class ai_user_data_rgba(textureMap):
        Attribute: str
        default: MXSWrapperBase
        default_connected: bool
        default_shader: None
        ...
    class ai_user_data_string(textureMap):
        Attribute: str
        default: str
        default_connected: bool
        default_shader: None
        ...
    class ai_utility(textureMap):
        color_mode: int
        shade_mode: int
        overlay_mode: int
        color: MXSWrapperBase
        color_connected: bool
        color_shader: None
        ao_distance: float
        ao_distance_connected: bool
        ao_distance_shader: None
        roughness: float
        roughness_connected: bool
        roughness_shader: None
        normal: MXSWrapperBase
        normal_connected: bool
        normal_shader: None
        ...
    class ai_uv_projection(textureMap):
        projection_color: MXSWrapperBase
        projection_color_connected: bool
        projection_color_shader: None
        projection_type: int
        coord_space: int
        pref_name: str
        p: MXSWrapperBase
        P_connected: bool
        P_shader: None
        U_Angle: float
        u_angle_connected: bool
        u_angle_shader: None
        V_Angle: float
        v_angle_connected: bool
        v_angle_shader: None
        clamp: bool
        default_color: MXSWrapperBase
        default_color_connected: bool
        default_color_shader: None
        matrix: MXSWrapperBase
        matrix_connected: bool
        matrix_shader: None
        ...
    class ai_uv_transform(textureMap):
        passthrough: MXSWrapperBase
        passthrough_connected: bool
        passthrough_shader: None
        unit: int
        UVSet: str
        coverage: MXSWrapperBase
        coverage_connected: bool
        coverage_shader: None
        scale_frame: MXSWrapperBase
        scale_frame_connected: bool
        scale_frame_shader: None
        translate_frame: MXSWrapperBase
        translate_frame_connected: bool
        translate_frame_shader: None
        rotate_frame: float
        rotate_frame_connected: bool
        rotate_frame_shader: None
        pivot_frame: MXSWrapperBase
        pivot_frame_connected: bool
        pivot_frame_shader: None
        wrap_frame_u: int
        wrap_frame_v: int
        wrap_frame_color: MXSWrapperBase
        wrap_frame_color_connected: bool
        wrap_frame_color_shader: None
        Repeat: MXSWrapperBase
        repeat_connected: bool
        repeat_shader: None
        offset: MXSWrapperBase
        offset_connected: bool
        offset_shader: None
        Rotate: float
        rotate_connected: bool
        rotate_shader: None
        pivot: MXSWrapperBase
        pivot_connected: bool
        pivot_shader: None
        Noise: MXSWrapperBase
        noise_connected: bool
        noise_shader: None
        mirror_u: bool
        mirror_v: bool
        flip_u: bool
        flip_v: bool
        swap_uv: bool
        stagger: bool
        ...
    class ai_variance_filter(textureMap):
        ...
    class ai_vector_map(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        tangent: MXSWrapperBase
        tangent_connected: bool
        tangent_shader: None
        normal: MXSWrapperBase
        normal_connected: bool
        normal_shader: None
        order: int
        invert_x: bool
        invert_y: bool
        invert_z: bool
        color_to_signed: bool
        tangent_space: bool
        scale: float
        scale_connected: bool
        scale_shader: None
        ...
    class ai_vector_to_rgb(textureMap):
        Input: MXSWrapperBase
        input_connected: bool
        input_shader: None
        mode: int
        mode_connected: bool
        mode_shader: None
        ...
    class ai_visible_light(textureMap):
        ...
    class ai_volume_collector(material):
        ...
    class ai_volume_sample_float(textureMap):
        channel: str
        position_offset: MXSWrapperBase
        position_offset_connected: bool
        position_offset_shader: None
        interpolation: int
        volume_type: int
        sdf_offset: float
        sdf_offset_connected: bool
        sdf_offset_shader: None
        sdf_blend: float
        sdf_blend_connected: bool
        sdf_blend_shader: None
        sdf_invert: bool
        input_min: float
        input_max: float
        contrast: float
        contrast_pivot: float
        bias: float
        gain: float
        output_min: float
        output_max: float
        clamp_min: bool
        clamp_max: bool
        ...
    class ai_volume_sample_rgb(textureMap):
        channel: str
        position_offset: MXSWrapperBase
        position_offset_connected: bool
        position_offset_shader: None
        interpolation: int
        gamma: float
        hue_shift: float
        saturation: float
        contrast: float
        contrast_pivot: float
        exposure: float
        multiply: float
        add: float
        ...
    class ai_wireframe(textureMap):
        line_width: float
        line_width_connected: bool
        line_width_shader: None
        fill_color: MXSWrapperBase
        fill_color_connected: bool
        fill_color_shader: None
        line_color: MXSWrapperBase
        line_color_connected: bool
        line_color_shader: None
        raster_space: bool
        raster_space_connected: bool
        raster_space_shader: None
        edge_type: int
        edge_type_connected: bool
        edge_type_shader: None
        ...
    class alpha(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class alphaRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class amax(Primitive):
        ...
    class ambientColor(Color):
        ...
    class ambientColorController(bezier_color):
        ...
    class amin(Primitive):
        ...
    class angle(shape):
        steps: int
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        typeIn_x: float
        typeIn_y: float
        typeIn_z: float
        typeIn_Length: float
        typeIn_Width: float
        typeIn_Thickness: float
        typeIn_Radius: float
        typeIn_radius2: float
        typeIn_creationMethod: bool
        typeIn_EdgeFillet: float
        angle_length: float
        angle_width: float
        angle_thickness: float
        angle_radius: float
        angle_radius2: float
        angle_syncCornerFillets: bool
        angle_EdgeFillet: float
        ...
    class animateAll(Primitive):
        ...
    class animateVertex(Primitive):
        ...
    class animationRange(Interval):
        ...
    class apolloParamContainer(GeometryClass):
        ...
    class append(Generic):
        ...
    class appendClip(BipedGeneric):
        ...
    class appendCurve(NURBSGenericMethodsWrapper):
        ...
    class appendCurveByID(NURBSGenericMethodsWrapper):
        ...
    class appendGizmo(Generic):
        ...
    class appendIfUnique(Primitive):
        ...
    class appendKey(Primitive):
        ...
    class appendMaxClip(BipedGeneric):
        ...
    class appendObject(NURBSGenericMethodsWrapper):
        ...
    class appendTrack(BipedGeneric):
        ...
    class appendTrackgroup(BipedGeneric):
        ...
    class appendUCurve(NURBSGenericMethodsWrapper):
        ...
    class appendUCurveByID(NURBSGenericMethodsWrapper):
        ...
    class appendVCurve(NURBSGenericMethodsWrapper):
        ...
    class appendVCurveByID(NURBSGenericMethodsWrapper):
        ...
    class applyEaseCurve(Generic):
        ...
    class applyOffset(Primitive):
        ...
    class applymaxIKCA(AttributeDef):
        ...
    class apropos(Primitive):
        ...
    class archiveMaxFile(Primitive):
        ...
    class areMtlAndRendererCompatible(Primitive):
        ...
    class areNodesInstances(Primitive):
        ...
    class arnold_cyl_camera(camera):
        arnold_node: str
        arnold_node_horizontal_fov: float
        arnold_node_vertical_fov: float
        arnold_node_projective: bool
        ...
    class arnold_fisheye_camera(camera):
        arnold_node: str
        arnold_node_fov: float
        arnold_node_autocrop: bool
        ...
    class arnold_spherical_camera(camera):
        arnold_node: str
        ...
    class arnold_vr_camera(camera):
        arnold_node: str
        arnold_node_mode: int
        arnold_node_projection: int
        arnold_node_eye_separation: float
        arnold_node_eye_to_neck: float
        arnold_node_top_merge_mode: int
        arnold_node_top_merge_angle: float
        arnold_node_bottom_merge_mode: int
        arnold_node_bottom_merge_angle: float
        ...
    class arnoldlight_cylindermanip(helper):
        ...
    class arnoldlight_quadmanip(helper):
        ...
    class arnoldlight_radiusmanip(helper):
        ...
    class arnoldlight_spotmanip(helper):
        ...
    class asin(Generic):
        ...
    class assemblyMgr(Interface):
        ...
    class assert_array_equal(Primitive):
        ...
    class assert_bitarray_equal(Primitive):
        ...
    class assert_defined(Primitive):
        ...
    class assert_equal(Primitive):
        ...
    class assert_false(Primitive):
        ...
    class assert_float(Primitive):
        ...
    class assert_float_equal(Primitive):
        ...
    class assert_matchpattern(Primitive):
        ...
    class assert_matrix_equal(Primitive):
        ...
    class assert_not_equal(Primitive):
        ...
    class assert_point2_equal(Primitive):
        ...
    class assert_point3_equal(Primitive):
        ...
    class assert_point4_equal(Primitive):
        ...
    class assert_string_equal(Primitive):
        ...
    class assert_true(Primitive):
        ...
    class assert_undefined(Primitive):
        ...
    class assetUser(Name):
        ...
    class assignKey(Primitive):
        ...
    class atan(Generic):
        ...
    class atan2(Generic):
        ...
    class atmosphereRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class atmospheric(MAXWrapper):
        ...
    class attach(Generic):
        ...
    class attachNodesToGroup(Primitive):
        ...
    class autoProjectSwitcherOnFilePreOpen(MAXScriptFunction):
        ...
    class autosave(Interface):
        ...
    class backgroundColor(Color):
        ...
    class backgroundColorController(bezier_color):
        ...
    class bakeSetupController_AbsoluteMode(MAXScriptFunction):
        ...
    class bakeSetupController_AdditiveMode(MAXScriptFunction):
        ...
    class bakeShell(material):
        originalMaterial: MXSWrapperBase
        bakedMaterial: MXSWrapperBase
        viewportMtlIndex: int
        renderMtlIndex: int
        ...
    class bakeUnsetupController_DontRevert(MAXScriptFunction):
        ...
    class bakeUnsetupController_Revert(MAXScriptFunction):
        ...
    class batchRenderMgr(Interface):
        ...
    class beautyRenderElement(RenderElement):
        ...
    class bezier_color(point3Controller):
        ...
    class bezier_float(floatController):
        ...
    class bezier_point3(point3Controller):
        ...
    class bezier_point4(point4Controller):
        ...
    class bezier_position(positionController):
        ...
    class bezier_rgba(point4Controller):
        ...
    class bezier_rotation(rotationController):
        ...
    class bezier_scale(scaleController):
        ...
    class beziershape(MAXBezierShapeClass):
        ...
    class bgndRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class bindKnot(NodeGeneric):
        ...
    class bindSpaceWarp(NodeGeneric):
        ...
    class bipedSystem(System):
        ...
    class bitmap(Value):
        ...
    class bitmapTex(textureMap):
        clipu: float
        clipv: float
        clipw: float
        cliph: float
        jitter: float
        useJitter: bool
        apply: bool
        cropPlace: int
        filtering: int
        monoOutput: int
        rgbOutput: int
        alphaSource: int
        preMultAlpha: bool
        bitmap: None
        coords: MXSWrapperBase
        output: MXSWrapperBase
        filename: str
        starttime: MXSWrapperBase
        playBackRate: float
        endCondition: int
        tieTimeToMatIDs: bool
        ...
    class black(Color):
        ...
    class blockMgr(Interface):
        ...
    class blue(Color):
        ...
    class blur(renderEffect):
        blur_type: int
        bUnifPixRad: float
        bUnifAlpha: bool
        bDirUPixRad: float
        bDirVPixRad: float
        bDirUTrail: float
        bDirVTrail: float
        bDirRotation: int
        bDirAlpha: bool
        bRadialPixRad: float
        bRadialTrail: float
        bRadialAlpha: bool
        bRadialXOrig: int
        bRadialYOrig: int
        bRadialUseNode: bool
        bRadialNode: None
        selImageActive: bool
        selImageBrighten: float
        selImageBlend: float
        selIBackActive: bool
        selIBackBrighten: float
        selIBackBlend: float
        selIBackFRadius: float
        selLumActive: bool
        selLumBrighten: float
        selLumBlend: float
        selLumMin: float
        selLumMax: float
        selLumFRadius: float
        selMaskActive: bool
        selMaskMap: None
        selMaskChannel: int
        selMaskBrighten: float
        selMaskBlend: float
        selMaskMin: float
        selMaskMax: float
        selMaskFRadius: float
        selObjIdsActive: bool
        selObjIdsIds: MXSWrapperBase
        selObjIdsBrighten: float
        selObjIdsBlend: float
        selObjIdsFRadius: float
        selObjIdsLumMin: float
        selObjIdsLumMax: float
        selMatIdsActive: bool
        selMatIdsIds: MXSWrapperBase
        selMatIdsBrighten: float
        selMatIdsBlend: float
        selMatIdsFRadius: float
        selMatIdsLumMin: float
        selMatIdsLumMax: float
        selGenBrightType: int
        ...
    class bmpio(BitmapIO):
        ...
    class boolcntrl(floatController):
        ...
    class boolean_float(floatController):
        ...
    class breakCurve(Primitive):
        ...
    class breakSurface(Primitive):
        ...
    class briteCon(renderEffect):
        brightness: float
        contrast: float
        ignoreBack: bool
        ...
    class brown(Color):
        ...
    class bsearch(Primitive):
        ...
    class buildTVFaces(Generic):
        ...
    class buildVCFaces(Generic):
        ...
    class camera(node):
        ...
    class cameras(ObjectSet):
        ...
    class canConvertTo(Generic):
        ...
    class cancelTryContinueBox(Primitive):
        ...
    class cavityMap(Primitive):
        ...
    class ccCurve(Value):
        ...
    class ccPoint(Value):
        ...
    class ceil(Generic):
        ...
    class cellularTex(textureMap):
        cellColor: MXSWrapperBase
        divColor1: MXSWrapperBase
        divColor2: MXSWrapperBase
        cellMap: None
        divMap1: None
        divMap2: None
        map1Enabled: bool
        map2Enabled: bool
        map3Enabled: bool
        variation: float
        size: float
        spread: float
        lowThresh: float
        midThresh: float
        highThresh: float
        type: int
        fractal: bool
        iteration: float
        roughness: float
        smooth: float
        adaptive: bool
        coords: MXSWrapperBase
        output: MXSWrapperBase
        ...
    class channel(shape):
        steps: int
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        typeIn_x: float
        typeIn_y: float
        typeIn_z: float
        typeIn_Length: float
        typeIn_Width: float
        typeIn_Thickness: float
        typeIn_Radius: float
        typeIn_radius2: float
        typeIn_creationMethod: bool
        channel_length: float
        channel_width: float
        channel_thickness: float
        channel_radius: float
        channel_radius2: float
        channel_syncCornerFillets: bool
        ...
    class checkBakedPositionName(MAXScriptFunction):
        ...
    class checkBakedRotationName(MAXScriptFunction):
        ...
    class classOf(Generic):
        ...
    class clear(Generic):
        ...
    class clearAllAppData(Generic):
        ...
    class clearCacheEntry(Generic):
        ...
    class clearControllerNewFlag(Primitive):
        ...
    class clearListener(Primitive):
        ...
    class clearMixer(BipedGeneric):
        ...
    class clearProdTess(NURBSGenericMethodsWrapper):
        ...
    class clearSelection(Primitive):
        ...
    class clearTrack(BipedGeneric):
        ...
    class clearTrackgroup(BipedGeneric):
        ...
    class clearUndoBuffer(Primitive):
        ...
    class clearViewTess(NURBSGenericMethodsWrapper):
        ...
    class close(Generic):
        ...
    class closeCameraTracker(Primitive):
        ...
    class closeRolloutFloater(Primitive):
        ...
    class closeU(NURBSGenericMethodsWrapper):
        ...
    class closeUtility(Primitive):
        ...
    class closeV(NURBSGenericMethodsWrapper):
        ...
    class close_enough(Primitive):
        ...
    class closelog(Primitive):
        ...
    class clothfx(modifier):
        gravity: float
        selfCollision: bool
        solidCollision: bool
        scale: float
        useSewingSprings: bool
        startframe: int
        timestep: float
        showSewingSprings: bool
        subsample: int
        endframe: int
        enableEndFrame: bool
        checkIntersections: bool
        clothclothMethod: int
        useGravity: bool
        simOnRender: bool
        simPriority: int
        advancedPinching: bool
        relativeVelocity: float
        timeScale: float
        ignoreBackfacing: bool
        simOnMouseDown: bool
        showCurrentState: bool
        showTargetState: bool
        showEnabledSolidCollision: bool
        showEnabledClothCollision: bool
        showTension: bool
        tensionScale: float
        weldMethod: int
        ...
    class cmdPanel(Interface):
        ...
    class collapse(UtilityPlugin):
        ...
    class collapseStack(NodeGeneric):
        ...
    class collapseface(Generic):
        ...
    class color(Value):
        ...
    class colorBalance(renderEffect):
        red: int
        green: int
        blue: int
        preserveLum: bool
        ignoreBack: bool
        ...
    class colorMan(Interface):
        ...
    class colorPicker(MAXWrapperNonRefTarg):
        ...
    class colorPickerDlg(Primitive):
        ...
    class colorReferenceTarget(ReferenceTarget):
        type: int
        color: MXSWrapperBase
        red: int
        green: int
        blue: int
        hue: int
        saturation: int
        value: int
        Use_RGB_E1: bool
        Use_RGB_E2: bool
        Use_RGB_E3: bool
        Use_HSV_E1: bool
        Use_HSV_E2: bool
        Use_HSV_E3: bool
        Use_RGB_I1: bool
        Use_RGB_I2: bool
        Use_RGB_I3: bool
        Use_HSV_I1: bool
        Use_HSV_I2: bool
        Use_HSV_I3: bool
        Variation_Type: int
        Use_Red_Variation: bool
        Use_Green_Variation: bool
        Use_Blue_Variation: bool
        Use_Hue_Variation: bool
        Use_Saturation_Variation: bool
        Use_Value_Variation: bool
        Red_Variation: int
        Green_Variation: int
        Blue_Variation: int
        Hue_Variation: int
        Saturation_Variation: int
        Value_Variation: int
        Use_RGB_E4: bool
        Use_RGB_E5: bool
        Use_RGB_E6: bool
        Use_HSV_E4: bool
        Use_HSV_E5: bool
        Use_HSV_E6: bool
        Use_RGB_I4: bool
        Use_RGB_I5: bool
        Use_RGB_I6: bool
        Use_HSV_I4: bool
        Use_HSV_I5: bool
        Use_HSV_I6: bool
        Sync_Type: int
        Use_E7: bool
        Random_Seed: int
        Use_E8: bool
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        Input_5: None
        Input_6: None
        Input_7: None
        Input_8: None
        ...
    class compareBitmaps(Primitive):
        ...
    class composite(Generic):
        ...
    class compositeTexture(textureMap):
        mapEnabled: MXSWrapperBase
        maskEnabled: MXSWrapperBase
        blendMode: MXSWrapperBase
        layername: MXSWrapperBase
        dlgOpened: MXSWrapperBase
        opacity: MXSWrapperBase
        mapList: MXSWrapperBase
        Mask: MXSWrapperBase
        ...
    class compositematerial(material):
        materialList: MXSWrapperBase
        mixType: MXSWrapperBase
        mapEnables: MXSWrapperBase
        amount: MXSWrapperBase
        ...
    class computeAnimation(BipedGeneric):
        ...
    class conformToShape(Primitive):
        ...
    class contains(Generic):
        ...
    class contrast(VideoPostFilter):
        ...
    class convertTo(NodeGeneric):
        ...
    class convertToMesh(NodeGeneric):
        ...
    class convertToNURBSCurve(Primitive):
        ...
    class convertToNURBSSurface(Primitive):
        ...
    class convertToPoly(NodeGeneric):
        ...
    class convertToSplineShape(NodeGeneric):
        ...
    class copy(NodeGeneric):
        ...
    class copyFile(Primitive):
        ...
    class copyMixdownToBiped(BipedGeneric):
        ...
    class copyPasteKeys(Primitive):
        ...
    class cos(Generic):
        ...
    class cosh(Generic):
        ...
    class cpptests(Interface):
        ...
    class createFloatControllerWithRandomValues(Primitive):
        ...
    class createInstance(Generic):
        ...
    class createMorphObject(Primitive):
        ...
    class createNumberedFilename(Primitive):
        ...
    class createOLEObject(Primitive):
        ...
    class createPointCloudMaterial(MAXScriptFunction):
        ...
    class createReaction(Primitive):
        ...
    class createfile(Primitive):
        ...
    class crop(Generic):
        ...
    class cross(Generic):
        ...
    class cubic(filter):
        ...
    class currentTime(Time):
        ...
    class curveLength(NodeGeneric):
        ...
    class custAttribCollapseManager(Interface):
        ...
    class cwsWarn(MAXScriptFunction):
        ...
    class dSightRender(renderEffect):
        framePad: int
        fontScale: int
        dimBG: bool
        alphaBlend: bool
        reqdDistance: int
        TypeTextTL: int
        TypeTextTC: int
        TypeTextTR: int
        TypeTextBL: int
        TypeTextBC: int
        TypeTextBR: int
        EditTextTL: str
        EditTextTC: str
        EditTextTR: str
        EditTextBL: str
        EditTextBC: str
        EditTextBR: str
        useImage: bool
        imageFName: str
        image_x: int
        image_y: int
        imgOpacity: int
        transfer_mode: int
        ...
    class debugVisualizerApexClothingAutoUI(MAXScriptFunction):
        ...
    class debugVisualizerAutoUI(MAXScriptFunction):
        ...
    class debugVisualizerClothingAutoUI(MAXScriptFunction):
        ...
    class deepCopy(Primitive):
        ...
    class defaultActions(Interface):
        ...
    class defaultVCFaces(Generic):
        ...
    class delINISetting(Primitive):
        ...
    class delete(Primitive):
        ...
    class deleteAllChangeHandlers(Primitive):
        ...
    class deleteAllCopies(BipedGeneric):
        ...
    class deleteAppData(Generic):
        ...
    class deleteAtmospheric(Primitive):
        ...
    class deleteChangeHandler(Primitive):
        ...
    class deleteCopy(BipedGeneric):
        ...
    class deleteEaseCurve(MappedGeneric):
        ...
    class deleteEffect(Primitive):
        ...
    class deleteFile(Primitive):
        ...
    class deleteGizmo(Generic):
        ...
    class deleteItem(Generic):
        ...
    class deleteKey(Generic):
        ...
    class deleteKeys(MappedGeneric):
        ...
    class deleteKnot(NodeGeneric):
        ...
    class deleteModifier(NodeGeneric):
        ...
    class deleteMorphTarget(Primitive):
        ...
    class deleteMultiplierCurve(Generic):
        ...
    class deleteNoteKey(Generic):
        ...
    class deleteNoteKeys(Generic):
        ...
    class deleteNoteTrack(Primitive):
        ...
    class deleteObjects(NURBSGenericMethodsWrapper):
        ...
    class deletePoint(CurveCtlGeneric):
        ...
    class deleteReaction(Primitive):
        ...
    class deleteScript(BipedGeneric):
        ...
    class deleteSnippet(BipedGeneric):
        ...
    class deleteSpline(NodeGeneric):
        ...
    class deleteTime(MappedGeneric):
        ...
    class deleteTrack(BipedGeneric):
        ...
    class deleteTrackViewController(Primitive):
        ...
    class deleteTrackViewNode(Primitive):
        ...
    class deleteTracker(Generic):
        ...
    class deleteTrackgroup(BipedGeneric):
        ...
    class deleteTranInfo(BipedGeneric):
        ...
    class deleteTransition(BipedGeneric):
        ...
    class deleteTransitionsTo(BipedGeneric):
        ...
    class deleteUserProp(Primitive):
        ...
    class deleteface(Generic):
        ...
    class deletevert(Generic):
        ...
    class densityMap(Primitive):
        ...
    class dents(textureMap):
        map1: None
        map2: None
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1Enabled: bool
        map2Enabled: bool
        size: float
        strength: float
        iterations: int
        coords: MXSWrapperBase
        ...
    class dependsOn(Primitive):
        ...
    class deselect(NodeGeneric):
        ...
    class deselectKey(Generic):
        ...
    class deselectKeys(MappedGeneric):
        ...
    class detachFaces(Generic):
        ...
    class detachNodesFromGroup(Primitive):
        ...
    class detachVerts(Generic):
        ...
    class diffuseMap(BakeElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        backgroundColor: MXSWrapperBase
        lightingOn: bool
        shadowsOn: bool
        targetMapSlotName: str
        ...
    class diffuseRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        lightingOn: bool
        ...
    class disableDisplayFilterCallbacks(Primitive):
        ...
    class disableRedrawViewsCallbacks(Primitive):
        ...
    class disableRefMsgs(Primitive):
        ...
    class disableSelectFilterCallbacks(Primitive):
        ...
    class disableTimeCallbacks(Primitive):
        ...
    class disconnect(NURBSGenericMethodsWrapper):
        ...
    class displacementToPreset(Generic):
        ...
    class display(Generic):
        ...
    class displayControlDialog(Primitive):
        ...
    class displayFilterCallbacksEnabled(Primitive):
        ...
    class distance(Generic):
        ...
    class doesDirectoryExist(Primitive):
        ...
    class doesFileExist(Primitive):
        ...
    class doesUserPropExist(Primitive):
        ...
    class dontCollect(UndefinedClass):
        ...
    class dot(Generic):
        ...
    class dotNetClass(Value):
        ...
    class dotNetControl(RolloutControl):
        ...
    class dotNetMXSValue(Value):
        ...
    class dotNetMethod(Value):
        ...
    class dotNetObject(Value):
        ...
    class doubleSidedMat(material):
        material1: MXSWrapperBase
        material2: MXSWrapperBase
        map1Enabled: bool
        map2Enabled: bool
        translucency: float
        ...
    class dragAndDrop(Interface):
        ...
    class dumpMAXStrings(Primitive):
        ...
    class dustMap(Primitive):
        ...
    class dxshadermanager(Interface):
        ...
    class edit(Primitive):
        ...
    class editAtmospheric(Primitive):
        ...
    class editEffect(Primitive):
        ...
    class emissionRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class empty(Generic):
        ...
    class emptyVal(EmptyClass):
        ...
    class enableDisplayFilterCallbacks(Primitive):
        ...
    class enableHardwareMaterial(Primitive):
        ...
    class enableORTs(MappedGeneric):
        ...
    class enableRedrawViewsCallbacks(Primitive):
        ...
    class enableRefMsgs(Primitive):
        ...
    class enableSelectFilterCallbacks(Primitive):
        ...
    class enableTimeCallbacks(Primitive):
        ...
    class enableUndo(Primitive):
        ...
    class encryptFile(Primitive):
        ...
    class encryptScript(Primitive):
        ...
    class enlargeBy(UserGeneric):
        ...
    class enumerateFiles(Primitive):
        ...
    class eof(Generic):
        ...
    class eulerToQuat(Primitive):
        ...
    class evalPos(NURBSGenericMethodsWrapper):
        ...
    class evalTangent(NURBSGenericMethodsWrapper):
        ...
    class evalUTangent(NURBSGenericMethodsWrapper):
        ...
    class evalVTangent(NURBSGenericMethodsWrapper):
        ...
    class execute(Generic):
        ...
    class executeScriptFile(Primitive):
        ...
    class exp(Generic):
        ...
    class expandToInclude(UserGeneric):
        ...
    class explodeGroup(Primitive):
        ...
    class exportFile(Primitive):
        ...
    class exprForMAXObject(Generic):
        ...
    class extrudeface(Generic):
        ...
    class falloff(textureMap):
        color1: MXSWrapperBase
        map1Amount: float
        map1: None
        map1on: bool
        color2: MXSWrapperBase
        map2Amount: float
        map2: None
        map2on: bool
        type: int
        direction: int
        node: None
        mtlIOROverride: bool
        ior: float
        extrapolateOn: bool
        nearDistance: float
        farDistance: float
        ...
    class fallofftextureMap(textureMap):
        ...
    class fclose(Primitive):
        ...
    class fetchMaxFile(Primitive):
        ...
    class fflush(Primitive):
        ...
    class fileOut(renderEffect):
        active: bool
        affectSource: bool
        channelType: int
        cameraNode: None
        nearZ: float
        farZ: float
        fitScene: bool
        ...
    class filein(Primitive):
        ...
    class filenameFromPath(Primitive):
        ...
    class filepos(Generic):
        ...
    class filter(MAXWrapper):
        ...
    class findItem(Generic):
        ...
    class findPattern(Generic):
        ...
    class findProjectFolderFromFileName(MAXScriptFunction):
        ...
    class findString(Generic):
        ...
    class findobject(MAXScriptFunction):
        ...
    class flagChanged(Generic):
        ...
    class flagForeground(NodeGeneric):
        ...
    class flagSendPropertiesToEditor(Primitive):
        ...
    class flatMirror(textureMap):
        blurAmount: float
        distortionAmount: float
        level: float
        size: float
        phase: float
        applyBlur: bool
        nthframe: int
        frame: int
        useEnviroment: bool
        applyToFaceID: bool
        faceID: int
        distortionType: int
        noiseType: int
        ...
    class flightstudioimage(BitmapIO):
        ...
    class float(Value):
        ...
    class floatController(MAXWrapper):
        ...
    class float_ListDummyEntry(floatController):
        ...
    class float_limit(floatController):
        Enable: bool
        Upper_Limit: float
        lower_limit: float
        upper_limit_enabled: bool
        lower_limit_enabled: bool
        static_value: float
        upper_smoothing: float
        lower_smoothing: float
        ...
    class float_list(floatController):
        weight: MXSWrapperBase
        average: bool
        ...
    class float_script(floatController):
        script: str
        ...
    class floor(Generic):
        ...
    class flush(Generic):
        ...
    class flushlog(Primitive):
        ...
    class fopen(Primitive):
        ...
    class fopenexr(BitmapIO):
        ...
    class forceReloadBitmapFile(Primitive):
        ...
    class format(Primitive):
        ...
    class formattedPrint(Primitive):
        ...
    class fractalNoise(Primitive):
        ...
    class free(Generic):
        ...
    class freeIesSun(light):
        rgb: MXSWrapperBase
        multiplier: float
        contrast: float
        softenDiffuseEdge: float
        atmosShadows: bool
        atmosOpacity: float
        atmosColorAmt: float
        shadowMultiplier: float
        targetDistance: None
        useGlobalShadowSettings: bool
        hasTarget: bool
        on: bool
        affectDiffuse: bool
        affectSpecular: bool
        castShadows: bool
        ...
    class freeSceneBitmaps(Primitive):
        ...
    class freeSpot(light):
        aspect: float
        rgb: MXSWrapperBase
        color: MXSWrapperBase
        contrast: float
        enabled: bool
        on: bool
        type: MXSWrapperBase
        value: int
        falloff: float
        excludeList: MXSWrapperBase
        includeList: None
        showCone: bool
        multiplier: float
        softenDiffuseEdge: float
        hotspot: float
        farAttenStart: float
        farAttenEnd: float
        nearAttenStart: float
        nearAttenEnd: float
        atmosOpacity: float
        atmosColorAmt: float
        decayRadius: float
        shadowColor: MXSWrapperBase
        shadowMultiplier: float
        hsv: MXSWrapperBase
        hue: int
        saturation: int
        inclExclType: int
        affectDiffuse: bool
        affectSpecular: bool
        useNearAtten: bool
        showNearAtten: bool
        useFarAtten: bool
        showFarAtten: bool
        attenDecay: int
        projector: bool
        projectorMap: None
        castShadows: bool
        useGlobalShadowSettings: bool
        raytracedShadows: bool
        overShoot: bool
        coneShape: int
        lightShape: int
        atmosShadows: bool
        lightAffectsShadow: bool
        shadowProjectorMap: None
        useShadowProjectorMap: bool
        ambientOnly: bool
        shadowgenerator: MXSWrapperBase
        ...
    class freeze(NodeGeneric):
        ...
    class freezeSelection(Primitive):
        ...
    class fseek(Primitive):
        ...
    class ftell(Primitive):
        ...
    class gPxGroundHeight(Double):
        ...
    class gPxVolumeUnitChange(Double):
        ...
    class gSimClock(dotNetObject):
        ...
    class gc(Primitive):
        ...
    class genClassID(Primitive):
        ...
    class genGUID(Primitive):
        ...
    class generateAPIList(Primitive):
        ...
    class geometry(ObjectSet):
        ...
    class geometryReferenceTarget(ReferenceTarget):
        type: int
        Use_Sub_Material: bool
        Sub_Material_Index: int
        Map_Channel_Index: int
        Gradient_Delta: float
        Static_Objects: bool
        Animated_Surface: bool
        Geometry_Safe_Mode: bool
        Subframe_Placement: bool
        Subframe_Geometry: bool
        Separate_Group_Members: bool
        Separate_Children: bool
        Use_T2: bool
        Use_I3: bool
        Use_V4: bool
        Use_V5: bool
        Use_R6: bool
        Random_Seed: int
        Use_E7: bool
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        Input_5: None
        Input_6: None
        Input_7: None
        ...
    class getActiveCamera(Primitive):
        ...
    class getAfterORT(Generic):
        ...
    class getAnimByHandle(Primitive):
        ...
    class getAnimByPointer(Primitive):
        ...
    class getAnimPointer(Primitive):
        ...
    class getAppData(Generic):
        ...
    class getAtmospheric(Primitive):
        ...
    class getAvailableSubstanceGraphsAndOutputsFromPackage(Primitive):
        ...
    class getBeforeORT(Generic):
        ...
    class getBitmapInfo(Primitive):
        ...
    class getBitmapOpenFileName(Primitive):
        ...
    class getBitmapSaveFileName(Primitive):
        ...
    class getCINCfg(MAXScriptFunction):
        ...
    class getCPTM(Primitive):
        ...
    class getCV(NURBSGenericMethodsWrapper):
        ...
    class getChannel(Generic):
        ...
    class getChannelAsMask(Generic):
        ...
    class getClassCounts(Primitive):
        ...
    class getClassInstances(Primitive):
        ...
    class getClassName(Primitive):
        ...
    class getClip(BipedGeneric):
        ...
    class getCopy(BipedGeneric):
        ...
    class getCoreInterfaces(Primitive):
        ...
    class getCurNameSelSet(Primitive):
        ...
    class getCurrentException(Primitive):
        ...
    class getCurrentExceptionCallStack(Primitive):
        ...
    class getCurrentExceptionStackTrace(Primitive):
        ...
    class getCurrentSelection(Primitive):
        ...
    class getCursorPos(Primitive):
        ...
    class getCurve(NURBSGenericMethodsWrapper):
        ...
    class getCurveID(NURBSGenericMethodsWrapper):
        ...
    class getCurveStartPoint(NURBSGenericMethodsWrapper):
        ...
    class getD3DMeshAllocated(Primitive):
        ...
    class getD3DMeshAllocatedFaces(Primitive):
        ...
    class getD3DTimer(Primitive):
        ...
    class getDimensions(Primitive):
        ...
    class getDirectories(Primitive):
        ...
    class getDisplacementMapping(Generic):
        ...
    class getEaseCurve(Primitive):
        ...
    class getEdge(NURBSGenericMethodsWrapper):
        ...
    class getEdgeSelection(NodeGeneric):
        ...
    class getEdgeVis(Generic):
        ...
    class getEffect(Primitive):
        ...
    class getErrorSourceFileLine(Primitive):
        ...
    class getErrorSourceFileName(Primitive):
        ...
    class getErrorSourceFileOffset(Primitive):
        ...
    class getFace(Generic):
        ...
    class getFaceMatID(Generic):
        ...
    class getFaceNormal(Generic):
        ...
    class getFaceSelection(NodeGeneric):
        ...
    class getFaceSmoothGroup(Generic):
        ...
    class getFileAttribute(Primitive):
        ...
    class getFileCreateDate(Primitive):
        ...
    class getFileModDate(Primitive):
        ...
    class getFileSecurityInfo(Primitive):
        ...
    class getFileSize(Primitive):
        ...
    class getFileVersion(Primitive):
        ...
    class getFilenameFile(Primitive):
        ...
    class getFilenamePath(Primitive):
        ...
    class getFilenameType(Primitive):
        ...
    class getFiles(Primitive):
        ...
    class getFilter(BipedGeneric):
        ...
    class getFlip(NURBSGenericMethodsWrapper):
        ...
    class getFlipTrim(NURBSGenericMethodsWrapper):
        ...
    class getGenerateUVs(NURBSGenericMethodsWrapper):
        ...
    class getGizmo(Generic):
        ...
    class getHandleByAnim(Primitive):
        ...
    class getHashValue(Primitive):
        ...
    class getINISetting(Primitive):
        ...
    class getIconAsBitmap(Primitive):
        ...
    class getIconSizes(Primitive):
        ...
    class getInVec(NodeGeneric):
        ...
    class getIndexedPixels(Generic):
        ...
    class getIndexedProperty(Primitive):
        ...
    class getInheritanceFlags(Primitive):
        ...
    class getInterface(Generic):
        ...
    class getInterfaces(Generic):
        ...
    class getKBChar(Primitive):
        ...
    class getKBLine(Primitive):
        ...
    class getKBPoint(Primitive):
        ...
    class getKBValue(Primitive):
        ...
    class getKey(Generic):
        ...
    class getKeyIndex(Generic):
        ...
    class getKeyTime(Generic):
        ...
    class getKnot(NURBSGenericMethodsWrapper):
        ...
    class getKnotPoint(NodeGeneric):
        ...
    class getKnotSelection(Primitive):
        ...
    class getKnotType(NodeGeneric):
        ...
    class getLastMergedNodes(Primitive):
        ...
    class getLastRenderedImage(Primitive):
        ...
    class getListenerSel(Primitive):
        ...
    class getListenerSelText(Primitive):
        ...
    class getLocalTime(Primitive):
        ...
    class getLog(Primitive):
        ...
    class getMAXClass(Primitive):
        ...
    class getMAXFileAssetMetadata(Primitive):
        ...
    class getMAXFileObjectNames(Primitive):
        ...
    class getMAXOpenFileName(Primitive):
        ...
    class getMAXSaveFileName(Primitive):
        ...
    class getMAXWindowPos(Primitive):
        ...
    class getMAXWindowSize(Primitive):
        ...
    class getMKKey(Primitive):
        ...
    class getMKKeyIndex(Primitive):
        ...
    class getMKTargetNames(Primitive):
        ...
    class getMKTargetWeights(Primitive):
        ...
    class getMKTime(Primitive):
        ...
    class getMKWeight(Primitive):
        ...
    class getMTLMEditFlags(Primitive):
        ...
    class getMTLMeditObjType(Primitive):
        ...
    class getMTLMeditTiling(Primitive):
        ...
    class getMaterialID(Primitive):
        ...
    class getMaxExtensionVersion(Primitive):
        ...
    class getMaxFileVersionData(Primitive):
        ...
    class getMaxscriptStartupState(Primitive):
        ...
    class getMeditMaterial(Primitive):
        ...
    class getModContextBBox(Primitive):
        ...
    class getModContextBBoxMax(Generic):
        ...
    class getModContextBBoxMin(Generic):
        ...
    class getModContextTM(Generic):
        ...
    class getMultiplierCurve(Primitive):
        ...
    class getMultiplierValue(Generic):
        ...
    class getNURBSSelection(Primitive):
        ...
    class getNURBSSet(Primitive):
        ...
    class getNodeBBox(Primitive):
        ...
    class getNodeByName(Primitive):
        ...
    class getNodeEventCallbacks(Primitive):
        ...
    class getNodeTM(Primitive):
        ...
    class getNoteKeyIndex(Generic):
        ...
    class getNoteKeyTime(Generic):
        ...
    class getNoteTrack(Primitive):
        ...
    class getNumCPVVerts(Generic):
        ...
    class getNumFaces(Generic):
        ...
    class getNumSubMtls(Primitive):
        ...
    class getNumSubTexmaps(Primitive):
        ...
    class getNumTVerts(Generic):
        ...
    class getNumVerts(Generic):
        ...
    class getObject(NURBSGenericMethodsWrapper):
        ...
    class getObjectName(Primitive):
        ...
    class getOpenFileName(Primitive):
        ...
    class getOutVec(NodeGeneric):
        ...
    class getParent(NURBSGenericMethodsWrapper):
        ...
    class getParentID(NURBSGenericMethodsWrapper):
        ...
    class getPixels(Generic):
        ...
    class getPoint(NURBSGenericMethodsWrapper):
        ...
    class getPointController(Primitive):
        ...
    class getPointControllers(Primitive):
        ...
    class getPointPos(Primitive):
        ...
    class getProdTess(NURBSGenericMethodsWrapper):
        ...
    class getProgressCancel(Primitive):
        ...
    class getPropNames(Generic):
        ...
    class getProperty(Primitive):
        ...
    class getPropertyController(Primitive):
        ...
    class getQtTextExtent(Primitive):
        ...
    class getRadius(NURBSGenericMethodsWrapper):
        ...
    class getReactionCount(Primitive):
        ...
    class getReactionFalloff(Primitive):
        ...
    class getReactionInfluence(Primitive):
        ...
    class getReactionName(Primitive):
        ...
    class getReactionState(Primitive):
        ...
    class getReactionStrength(Primitive):
        ...
    class getReactionValue(Primitive):
        ...
    class getSaveFileName(Primitive):
        ...
    class getSavePath(Primitive):
        ...
    class getSaveRequired(Primitive):
        ...
    class getScriptIndex(BipedGeneric):
        ...
    class getSeed(NURBSGenericMethodsWrapper):
        ...
    class getSegLengths(Primitive):
        ...
    class getSegSelection(Primitive):
        ...
    class getSegmentType(NodeGeneric):
        ...
    class getSelectedPts(CurveCtlGeneric):
        ...
    class getSelectedReactionNum(Primitive):
        ...
    class getSelectionLevel(Primitive):
        ...
    class getSimilarNodes(Primitive):
        ...
    class getSnippetIndex(BipedGeneric):
        ...
    class getSourceFileLine(Primitive):
        ...
    class getSourceFileName(Primitive):
        ...
    class getSourceFileOffSet(Primitive):
        ...
    class getSplineSelection(Primitive):
        ...
    class getSplitMesh(Generic):
        ...
    class getSubAnim(Generic):
        ...
    class getSubAnimName(Generic):
        ...
    class getSubAnimNames(Generic):
        ...
    class getSubMtl(Primitive):
        ...
    class getSubMtlSlotName(Primitive):
        ...
    class getSubTexmap(Primitive):
        ...
    class getSubTexmapSlotName(Primitive):
        ...
    class getSubdivisionDisplacement(Generic):
        ...
    class getTVFace(Generic):
        ...
    class getTextExtent(Primitive):
        ...
    class getTextureSurface(NURBSGenericMethodsWrapper):
        ...
    class getTextureUVs(NURBSGenericMethodsWrapper):
        ...
    class getThisScriptFilename(Primitive):
        ...
    class getTiling(NURBSGenericMethodsWrapper):
        ...
    class getTilingOffset(NURBSGenericMethodsWrapper):
        ...
    class getTimeRange(Generic):
        ...
    class getTrack(BipedGeneric):
        ...
    class getTracker(Generic):
        ...
    class getTrackgroup(BipedGeneric):
        ...
    class getTransformAxis(Primitive):
        ...
    class getTransformLockFlags(Primitive):
        ...
    class getTrimSurface(NURBSGenericMethodsWrapper):
        ...
    class getUCurve(NURBSGenericMethodsWrapper):
        ...
    class getUCurveID(NURBSGenericMethodsWrapper):
        ...
    class getUKnot(NURBSGenericMethodsWrapper):
        ...
    class getUniversalTime(Primitive):
        ...
    class getUserProp(NodeGeneric):
        ...
    class getUserPropBuffer(NodeGeneric):
        ...
    class getUserPropVal(Primitive):
        ...
    class getVCFace(Generic):
        ...
    class getVCurve(NURBSGenericMethodsWrapper):
        ...
    class getVCurveID(NURBSGenericMethodsWrapper):
        ...
    class getVKnot(NURBSGenericMethodsWrapper):
        ...
    class getValue(CurveCtlGeneric):
        ...
    class getVert(Generic):
        ...
    class getVertSelection(NodeGeneric):
        ...
    class getVertexPaintAmounts(Primitive):
        ...
    class getVertexPaintColors(Primitive):
        ...
    class getViewFOV(Primitive):
        ...
    class getViewSize(Primitive):
        ...
    class getViewTM(Primitive):
        ...
    class getViewTess(NURBSGenericMethodsWrapper):
        ...
    class getXYZControllers(Primitive):
        ...
    class getclipboardBitmap(Primitive):
        ...
    class getclipboardText(Primitive):
        ...
    class getnormal(Generic):
        ...
    class gettvert(Generic):
        ...
    class getvertcolor(Generic):
        ...
    class gizmoBulge(ReferenceTarget):
        ...
    class gizmoJoint(ReferenceTarget):
        ...
    class gizmoJointMorph(ReferenceTarget):
        ...
    class globalDXDisplayManager(Interface):
        ...
    class globalInpoint(BipedGeneric):
        ...
    class globalOutpoint(BipedGeneric):
        ...
    class globalToLocal(BipedGeneric):
        ...
    class globalToScaledLocal(BipedGeneric):
        ...
    class globalTracks(MAXTVNode):
        ...
    class go(Primitive):
        ...
    class gotoFrame(Generic):
        ...
    class gravity(SpacewarpObject):
        strength: float
        decay: float
        gravitytype: int
        iconSize: float
        hoopson: bool
        ...
    class gray(Color):
        ...
    class green(Color):
        ...
    class grid(helper):
        length: float
        width: float
        grid: float
        activeColor: int
        displayPlane: int
        ...
    class gridPrefs(Interface):
        ...
    class group(Primitive):
        ...
    class hasCurrentExceptionCallStack(Primitive):
        ...
    class hasCurrentExceptionStackTrace(Primitive):
        ...
    class hasINISetting(Primitive):
        ...
    class hasMacroRecorderContext(MAXScriptFunction):
        ...
    class hasNoteTracks(Primitive):
        ...
    class hasProperty(Primitive):
        ...
    class heapCheck(Primitive):
        ...
    class heightManager(Interface):
        ...
    class help(MAXScriptFunction):
        ...
    class helper(node):
        ...
    class helpers(ObjectSet):
        ...
    class hide(NodeGeneric):
        ...
    class hideSelectedSegments(NodeGeneric):
        ...
    class hideSelectedSplines(NodeGeneric):
        ...
    class hideSelectedVerts(NodeGeneric):
        ...
    class holdMaxFile(Primitive):
        ...
    class hotspotAngleSeparation(Double):
        ...
    class iDisplayGamma(Interface):
        ...
    class iParserLoader(Interface):
        ...
    class icon(ReferenceTarget):
        type: int
        Static_Icon: bool
        Subframe_Placement: bool
        Subframe_Geometry: bool
        Use_T1: bool
        Use_V3: bool
        Use_V4: bool
        Random_Seed: int
        Use_E4: bool
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        ...
    class illumRenderElement(RenderElement):
        ...
    class imageMotionBlur(renderEffect):
        duration: float
        transparency: bool
        ...
    class imerge(Interface):
        ...
    class importFile(Primitive):
        ...
    class include(Primitive):
        ...
    class initGroupMembers(MAXScriptFunction):
        ...
    class inputTextColor(Color):
        ...
    class insertItem(Primitive):
        ...
    class insertPoint(CurveCtlGeneric):
        ...
    class insertSnippet(BipedGeneric):
        ...
    class insertTime(MappedGeneric):
        ...
    class insertTrack(BipedGeneric):
        ...
    class insertTrackgroup(BipedGeneric):
        ...
    class instance(NodeGeneric):
        ...
    class instanceReplace(NodeGeneric):
        ...
    class int(Primitive):
        ...
    class integer(Value):
        ...
    class interpBezier3D(Primitive):
        ...
    class interpCurve3D(Primitive):
        ...
    class intersectRay(NodeGeneric):
        ...
    class intersectRayScene(Primitive):
        ...
    class intersects(NodeGeneric):
        ...
    class invalTrack(Generic):
        ...
    class invalidateTM(MappedPrimitive):
        ...
    class invalidateTreeTM(MappedPrimitive):
        ...
    class invalidateWS(MappedPrimitive):
        ...
    class invert(Generic):
        ...
    class is64bitApplication(Primitive):
        ...
    class isActive(Primitive):
        ...
    class isAnimPlaying(Primitive):
        ...
    class isAnimated(CurveCtlGeneric):
        ...
    class isClosed(NodeGeneric):
        ...
    class isCompatible(Generic):
        ...
    class isController(Primitive):
        ...
    class isCreatingObject(Primitive):
        ...
    class isDeformable(Primitive):
        ...
    class isDeleted(Generic):
        ...
    class isDirectoryWriteable(Primitive):
        ...
    class isEmpty(Generic):
        ...
    class isGroupHead(Primitive):
        ...
    class isGroupMember(Primitive):
        ...
    class isIdentity(Generic):
        ...
    class isKeySelected(Generic):
        ...
    class isKindOf(Generic):
        ...
    class isMSCustAttrib(Primitive):
        ...
    class isMSCustAttribClass(Primitive):
        ...
    class isMSPlugin(Primitive):
        ...
    class isMSPluginClass(Primitive):
        ...
    class isMaxFile(Primitive):
        ...
    class isMtlUsedInSceneMtl(Primitive):
        ...
    class isOpenGroupHead(Primitive):
        ...
    class isOpenGroupMember(Primitive):
        ...
    class isParticleSystem(Primitive):
        ...
    class isProperty(Primitive):
        ...
    class isPropertyAnimatable(Primitive):
        ...
    class isReadOnly(Primitive):
        ...
    class isSceneXRefNode(Primitive):
        ...
    class isSelectionFrozen(Primitive):
        ...
    class isSpace(Primitive):
        ...
    class isStruct(Primitive):
        ...
    class isStructDef(Primitive):
        ...
    class isUsedInScene(Primitive):
        ...
    class isValidNode(Primitive):
        ...
    class isValidObj(Primitive):
        ...
    class isValidValue(Primitive):
        ...
    class isWorldSpaceObject(Primitive):
        ...
    class join(Generic):
        ...
    class joinCurves(Primitive):
        ...
    class joinSurfaces(Primitive):
        ...
    class jpegio(BitmapIO):
        ...
    class length(Generic):
        ...
    class lengthInterp(NodeGeneric):
        ...
    class lengthTangent(NodeGeneric):
        ...
    class lengthToPathParam(NodeGeneric):
        ...
    class light(node):
        ...
    class lightLevel(Double):
        ...
    class lightLevelController(bezier_float):
        ...
    class lightTintColor(Color):
        ...
    class lightTintColorController(bezier_color):
        ...
    class lightingAnalysisDataRenderElement(RenderElement):
        ...
    class lights(ObjectSet):
        ...
    class line(shape):
        steps: int
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        ...
    class linear_float(floatController):
        ...
    class linear_position(positionController):
        ...
    class linear_rotation(rotationController):
        ...
    class linear_scale(scaleController):
        ...
    class listener(WindowStream):
        ...
    class listenerBackgroundColor(Color):
        ...
    class loadCUIScheme(MAXScriptFunction):
        ...
    class loadCurrentPathConfigFile(MAXScriptFunction):
        ...
    class loadDllsFromDir(Primitive):
        ...
    class loadFrames(Generic):
        ...
    class loadMaterialLibrary(Primitive):
        ...
    class loadMaxAnimationFile(BipedGeneric):
        ...
    class loadMaxFile(Primitive):
        ...
    class loadMixFile(BipedGeneric):
        ...
    class loadMoFlowFile(BipedGeneric):
        ...
    class loadPicture(Primitive):
        ...
    class loadSnippetFiles(BipedGeneric):
        ...
    class loadTempMaterialLibrary(Primitive):
        ...
    class loadfile(BipedGeneric):
        ...
    class localToGlobal(BipedGeneric):
        ...
    class localToScaledLocal(BipedGeneric):
        ...
    class locals(Primitive):
        ...
    class log(Generic):
        ...
    class log10(Generic):
        ...
    class lookat(Matrix3Controller):
        ...
    class lumRenderElement(RenderElement):
        ...
    class mCloth(modifier):
        useSoftSelection: bool
        softselUseEdgeDistance: bool
        softselEdgeDist: int
        softselAffectBackfacing: bool
        softselFalloff: float
        softselPinch: float
        softselBubble: float
        useTextureMap: bool
        texture: None
        map: int
        mapChannel: int
        gravity: float
        ignoreBackfacing: bool
        showTargetState: bool
        showTension: bool
        tensionScale: float
        weldMethod: int
        thickness: float
        self_thickness: float
        solver_iterations: int
        bendiness: float
        hard_stretch_limitation: float
        stretchiness: float
        density: float
        damping_coefficient: float
        friction: float
        pressure: float
        tear_factor: float
        collision_response_coefficient: float
        attachment_response_coefficient: float
        attachment_tear_factor: float
        to_fluid_response_coefficient: float
        from_fluid_response_coefficient: float
        compressions_limit: float
        compressions_stiffness: float
        min_adhere_velocity: float
        attachToCollide: bool
        do_pressure: bool
        is_static: bool
        enable_collision: bool
        self_collision: bool
        visualization: bool
        do_gravity: bool
        do_bending: bool
        do_bending_ortho: bool
        Damping: float
        two_way_collision: bool
        hardware: bool
        com_damping: bool
        validbounds: bool
        do_fluid_collision: bool
        disable_dynamic_ccd: bool
        do_adhere: bool
        do_hard_stretch_limitation: bool
        do_untangling: bool
        do_inter_collision: bool
        tearable: bool
        inherit_velocity: bool
        solver_iterations: int
        hierarchical_Levels: int
        behavior: int
        forceList: MXSWrapperBase
        enablelivedrag: bool
        untilframeenable: bool
        kinematic_until_frame: int
        useSoftSelection: bool
        softselUseEdgeDistance: bool
        softselEdgeDist: int
        softselAffectBackfacing: bool
        softselFalloff: float
        softselPinch: float
        softselBubble: float
        useTextureMap: bool
        texture: None
        map: int
        mapChannel: int
        ...
    class mP_Buoyancy(helper):
        density: float
        Level_Type: int
        Level_Height: float
        Grid_Geometry: None
        Use_Quadratic_Drag: bool
        Quadratic_Drag: float
        Use_Linear_Drag: bool
        Linear_Drag: float
        Use_Angular_Drag: bool
        Angular_Drag: float
        Surface_Unit: float
        Icon_Shape: int
        Icon_Length: float
        Icon_Width: float
        Icon_Height: float
        Limit_Buoyancy_By_Icon: bool
        Color_Coordinated: bool
        ...
    class mP_Collision(helper):
        Deflectors: MXSWrapperBase
        Test_True: bool
        Test_Type: int
        Min_Speed: float
        Max_Speed: float
        Collision_Count: int
        Report_To_Data_Operator: bool
        Additive_Count: bool
        Collision_Group: int
        ...
    class mP_Drag(helper):
        Timing_Type: int
        Apply_Linear_Damping: bool
        Linear_Damping: float
        Apply_Angular_Damping: bool
        Angular_Damping: float
        Sync: int
        Speed_Multiplier: bool
        Speed_Unit: float
        Spin_Unit: float
        Use_Data_Wiring: bool
        Linear_Damping_From_Data: bool
        Linear_Damping_Data_Creator: None
        Angular_Damping_From_Data: bool
        Angular_Damping_Data_Creator: None
        ...
    class mP_Force(helper):
        Force_Type: int
        Force_Variation_Threshold: bool
        Shape_Size: float
        Influence: float
        Sync: int
        Force_Space_Warps: MXSWrapperBase
        Force_Overlapping: int
        Impulse_On_Event_Entry: bool
        Time_Warp: int
        Exponent: int
        Use_Script_Float: int
        ...
    class mP_Glue(helper):
        Timing_Type: int
        Bind_Distance: float
        Use_Bind_Gap_Condition: bool
        Bind_Gap: float
        Bind_Center_Aligned_Only: bool
        Align_Margin: float
        Allow_Binding_Penetration: bool
        type: int
        Breakable_By_Force: bool
        Max_Force: float
        Max_Torque: float
        Max_By_Bind_Distance: bool
        Distance_Unit: float
        Continuous_Adjustment: bool
        Sync: int
        Max_Binds_Per_Particle: int
        Test_True: bool
        Test_Type: int
        Bind_In_Current_Event: bool
        Bind_With_Other_Events: bool
        Events_To_Bind_With: MXSWrapperBase
        Bind_With_Deflectors: bool
        Bind_With_Ground: bool
        Deflectors_To_Bind_With: MXSWrapperBase
        Visualize_Binding: bool
        color: MXSWrapperBase
        Simplified_Binding_Anchor_Type: int
        Rigid_Binding_Anchor_Type: int
        Solver_Factor: float
        Use_Minimum_Distance_Limit: bool
        Minimum_Distance_Type: int
        Minimum_Absolute_Distance: float
        Minimum_Relative_Distance: float
        Use_Maximum_Distance_Limit: bool
        Maximum_Distance_Type: int
        Maximum_Absolute_Distance: float
        Maximum_Relative_Distance: float
        Enable_Spring_Force: bool
        Adjust_By_Particle_Mass: bool
        Spring_Coef: float
        Damper_Coef: float
        Bury_Binding_Anchors: bool
        depth: float
        Breakable_By_Overstretch: bool
        Overstretch_Type: int
        Overstretch_Absolute_Limit: float
        Overstretch_Relative_Limit: float
        Bind_Distance_From_Data: bool
        Bind_Distance_Data_Creator: None
        Bind_Gap_From_Data: bool
        Bind_Gap_Data_Creator: None
        Breakability_Max_Force_From_Data: bool
        Breakability_Max_Force_Data_Creator: None
        Breakability_Max_Torque_From_Data: bool
        Breakability_Max_Torque_Data_Creator: None
        Max_Binds_Per_Particle_From_Data: bool
        Max_Binds_Per_Particle_Data_Creator: None
        Binding_Groups_From_Data: bool
        Binding_Groups_Data_Creator: None
        Minimum_Distance_Limit_From_Data: bool
        Minimum_Distance_Limit_Data_Creator: None
        Maximum_Distance_Limit_From_Data: bool
        Maximum_Distance_Limit_Data_Creator: None
        Spring_Force_Coef_From_Data: bool
        Spring_Force_Coef_Data_Creator: None
        Spring_Damper_Coef_From_Data: bool
        Spring_Damper_Coef_Data_Creator: None
        Overstretch_Distance_Limit_From_Data: bool
        Overstretch_Distance_Limit_Data_Creator: None
        Num_Active_Bindings_To_Data: bool
        Num_Active_Bindings_Data_Creator: None
        Num_Broken_Bindings_To_Data: bool
        Num_Broken_Bindings_Data_Creator: None
        Num_Broken_By_Force_To_Data: bool
        Num_Broken_By_Force_Data_Creator: None
        Average_Binding_Length_To_Data: bool
        Average_Binding_Length_Data_Creator: None
        Minimum_Binding_Length_To_Data: bool
        Minimum_Binding_Length_Data_Creator: None
        Maximum_Binding_Length_To_Data: bool
        Maximum_Binding_Length_Data_Creator: None
        Average_Breaking_Impulse_To_Data: bool
        Average_Breaking_Impulse_Data_Creator: None
        Maximum_Breaking_Impulse_To_Data: bool
        Maximum_Breaking_Impulse_Data_Creator: None
        ...
    class mP_InterCollision(helper):
        Scope_Type: int
        Selected_Events: MXSWrapperBase
        Test_Type: int
        Min_Speed: float
        Max_Speed: float
        Collision_Count: int
        Report_To_Data_Operator: bool
        Additive_Count: bool
        ...
    class mP_Shape(helper):
        Collide_Type: int
        Display_Type: int
        Conform_To_Particle_Shape: bool
        Shape_Length: float
        Shape_Width: float
        Shape_Height: float
        Scale_Type: int
        scale: MXSWrapperBase
        color: MXSWrapperBase
        Weld_Threshold: float
        Inflate_Width: float
        Scale_Margin: float
        Restitution: float
        Static_Friction: float
        Dynamic_Friction: float
        Mass_Type: int
        mass: float
        density: float
        Interpenetration_Tolerance: float
        Generate_Tolerance_Channel: bool
        Collision_Group: int
        ...
    class mP_Solvent(helper):
        Particles_To_Particles: bool
        Particles_To_Deflectors: bool
        Particles_To_Ground: bool
        Limit_Solvent_By_List: bool
        Glue_Tests: MXSWrapperBase
        Limit_Solvent_By_Time: bool
        start: int
        stop: int
        Limit_Solvent_By_Data: bool
        Data_Channel: None
        Limit_Solvent_By_Icon: bool
        mode: int
        Icon_Shape: int
        icon_size: float
        Color_Coordinated: bool
        ...
    class mP_Switch(helper):
        Match_Position: bool
        Match_Speed: bool
        Position_Speed_Match_Type: int
        Position_Speed_Start: int
        Position_Speed_Stop: int
        Position_Speed_Active: bool
        Position_Speed_Sync_Type: int
        Use_Speed_Limit: bool
        Speed_Limit: float
        Match_Rotation: bool
        Match_Spin: bool
        Rotation_Spin_Match_Type: int
        Rotation_Spin_Start: int
        Rotation_Spin_Stop: int
        Rotation_Spin_Active: bool
        Rotation_Spin_Sync_Type: int
        Use_Spin_Limit: bool
        Spin_Limit: float
        Apply_Anti_Gravity: bool
        AntiGravity_Type: int
        AntiGravity_Start: int
        AntiGravity_Stop: int
        AntiGravity_Active: bool
        Anti_Gravity_Sync_Type: int
        Turn_Off_Simulation: bool
        Turn_Off_Simulation_Type: int
        Turn_Off_Start: int
        Turn_Off_Stop: int
        Turn_Off_Active: bool
        Turn_Off_Sync_Type: int
        ...
    class mP_World(helper):
        PhysX_World_Driver: None
        Suppress_Express_Save: bool
        PhysX_Driver_Type: int
        ...
    class mP_Worldhelper(helper):
        Apply_Gravity: bool
        Gravity_Acceleration: float
        Ground_Collision_Plane: bool
        Set_World_Limits: bool
        Icon_Length: float
        Icon_Width: float
        Icon_Height: float
        Collision_Group: int
        Default_Restitution: float
        Default_Static_Friction: float
        Default_Dynamic_Friction: float
        Run_Baked_Simulation: bool
        Range_Type: int
        Range_Start: int
        Range_Finish: int
        Update_Viewports: bool
        Hide_Icon: bool
        Hide_Particle_Bindings: bool
        Show_Bake_Dialog: int
        Subframe_Factor: int
        Subframe_Type: int
        Use_Time_Scale: bool
        Time_Scale: float
        Energy_Threshold: float
        Speed_Threshold: float
        Spin_Rate_Threshold: float
        Sleep_Threshold_Type: int
        Bounce_Threshold: float
        Enable_Multi_Threading: bool
        Thread_Count: int
        Use_Hardware_PPU: bool
        Restricted_Broadphase: bool
        Safe_Mode_Simulation: bool
        Calculation_Limit: int
        ...
    class mParticles_Flow(ReferenceTarget):
        ...
    class macroRecorder(WindowStream):
        ...
    class macroRecorderBackgroundColor(Color):
        ...
    class macroRecorderTextColor(Color):
        ...
    class makeCube(UserGeneric):
        ...
    class makeDir(Primitive):
        ...
    class makeIndependent(Primitive):
        ...
    class makeUniqueArray(Primitive):
        ...
    class makeValidName(Primitive):
        ...
    class manip(Interface):
        ...
    class mapKeys(MappedGeneric):
        ...
    class mapPoint(Primitive):
        ...
    class mapScreenToCP(Primitive):
        ...
    class mapScreenToView(Primitive):
        ...
    class mapScreenToWorldRay(Primitive):
        ...
    class mapping(helper):
        U_Map: float
        V_Map: float
        W_Map: float
        Sync_Type: int
        Channel_Type: int
        Map_Channel: int
        Show_In_Viewport: bool
        ...
    class mappinglayerData(AttributeDef):
        ...
    class maskTex(textureMap):
        map: None
        Mask: None
        mapEnabled: bool
        maskEnabled: bool
        maskInverted: bool
        ...
    class material(MAXWrapper):
        ...
    class materialID(NodeGeneric):
        ...
    class materialIDRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class materialhelper(helper):
        ...
    class maxOps(Interface):
        ...
    class maxVersion(Primitive):
        ...
    class maz(Primitive):
        ...
    class measureOffset(Primitive):
        ...
    class medit(Interface):
        ...
    class memStreamMgr(Interface):
        ...
    class mental_ray__Area_Light_custom_attribute(CustAttrib):
        mr_NumAreaSamples: int
        mr_EnableLightShapeRendering: bool
        ...
    class mentalraySun(light):
        ...
    class menuMan(Interface):
        ...
    class menuitem(Value):
        ...
    class merge(Generic):
        ...
    class mergeMaxFile(Primitive):
        ...
    class mesh(MAXMeshClass):
        ...
    class meshGrid(GeometryClass):
        typeinCreationMethod: int
        typeInPos: MXSWrapperBase
        typeInLength: float
        typeInWidth: float
        length: float
        width: float
        lengthsegs: int
        widthsegs: int
        density: float
        renderScale: float
        mapcoords: bool
        ...
    class mesh_weld_overlapping_vertices(Primitive):
        ...
    class meshsmooth(modifier):
        subdivMethod: int
        ignoreSel: bool
        oldMapping: bool
        iterations: int
        smoothness: float
        useRenderIterations: bool
        renderIterations: int
        useRenderSmoothness: bool
        renderSmoothness: float
        faceType: int
        keepConvex: bool
        update: int
        strength: float
        Relax: float
        limitSurface: bool
        smoothResult: bool
        sepByMats: bool
        sepBySmGroups: bool
        ignoreBackfacing: bool
        displayCage: bool
        isolineDisplay: bool
        controlLevel: int
        useSoftSel: bool
        useEdgeDist: bool
        edgeDist: int
        affectBackfacing: bool
        falloff: float
        pinch: float
        bubble: float
        reset: int
        cageColor: MXSWrapperBase
        selectedCageColor: MXSWrapperBase
        ...
    class messageBox(Primitive):
        ...
    class messageTextColor(Color):
        ...
    class mirror(modifier):
        copy: bool
        offset: float
        mirror_axis: int
        ...
    class missingPathCache(Interface):
        ...
    class mixTexture(textureMap):
        mixAmount: float
        lower: float
        upper: float
        useCurve: bool
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1: None
        map2: None
        Mask: None
        map1Enabled: bool
        map2Enabled: bool
        maskEnabled: bool
        output: MXSWrapperBase
        ...
    class mixdown(BipedGeneric):
        ...
    class mod(Generic):
        ...
    class modifier(MAXWrapper):
        ...
    class mouseTrack(Primitive):
        ...
    class move(NodeGeneric):
        ...
    class moveClip(BipedGeneric):
        ...
    class moveKey(Generic):
        ...
    class moveKeys(MappedGeneric):
        ...
    class mrAreaLightCustAttrib(CustAttrib):
        mr_NumAreaSamples: int
        mr_EnableLightShapeRendering: bool
        ...
    class mrPBParameter(ReferenceTarget):
        ...
    class mrPBParameterClassDescCreator(Interface):
        ...
    class mrPhysSkyLight(light):
        ...
    class mr_Sky(light):
        ...
    class mr_Sun(light):
        ...
    class msZip(Interface):
        ...
    class multiPassDOF(MPassCamEffect):
        useTargetDistance: bool
        focalDepth: float
        displayPasses: bool
        useOriginalLocation: bool
        totalPasses: int
        sampleRadius: float
        sampleBias: float
        normalizeWeights: bool
        ditherStrength: float
        tileSize: int
        disableFiltering: bool
        disableAntialiasing: bool
        ...
    class multiPassMotionBlur(MPassCamEffect):
        displayPasses: bool
        totalPasses: int
        duration: float
        bias: float
        normalizeWeights: bool
        ditherStrength: float
        tileSize: int
        disableFiltering: bool
        disableAntialiasing: bool
        ...
    class multiSubMaterial(material):
        materialList: MXSWrapperBase
        mapEnabled: MXSWrapperBase
        names: MXSWrapperBase
        materialIDList: MXSWrapperBase
        ...
    class multiSubMaterial_empty(material):
        ...
    class name(Value):
        ...
    class nearestPathParam(NodeGeneric):
        ...
    class negative(VideoPostFilter):
        ...
    class netrender(Interface):
        ...
    class newRolloutFloater(Primitive):
        ...
    class newScript(Primitive):
        ...
    class newSnippet(BipedGeneric):
        ...
    class newTrackViewNode(Primitive):
        ...
    class node(MAXWrapper):
        ...
    class nodeGetBoundingBox(Primitive):
        ...
    class nodeLocalBoundingBox(Primitive):
        ...
    class nodeSelectionSet(Interface):
        ...
    class noise3(Primitive):
        ...
    class noise4(Primitive):
        ...
    class normalize(Generic):
        ...
    class normtime(Primitive):
        ...
    class notifyDependents(Primitive):
        ...
    class numAtmospherics(Integer):
        ...
    class numCopies(BipedGeneric):
        ...
    class numEaseCurves(Generic):
        ...
    class numEffects(Integer):
        ...
    class numKeys(Generic):
        ...
    class numKnots(NodeGeneric):
        ...
    class numMultiplierCurves(Generic):
        ...
    class numNoteTracks(Primitive):
        ...
    class numPoints(Primitive):
        ...
    class numSegments(NodeGeneric):
        ...
    class numSelKeys(Generic):
        ...
    class numSplines(NodeGeneric):
        ...
    class nvBox(GeometryClass):
        width: float
        length: float
        height: float
        widthsegs: int
        lengthsegs: int
        heightsegs: int
        ...
    class nvCapsule(GeometryClass):
        radius: float
        height: float
        heighttype: int
        ...
    class nvConstraint(helper):
        body0: None
        body1: None
        helpersize: float
        linearModeX: int
        linearModeY: int
        linearModeZ: int
        linearPosition: float
        linearRestitution: float
        linearSpring: float
        linearDamping: float
        swing1Mode: int
        swing1Angle: float
        swing1Restitution: float
        swing1Spring: float
        swing1Damping: float
        swing2Mode: int
        swing2Angle: float
        swing2Restitution: float
        swing2Spring: float
        swing2Damping: float
        twistMode: int
        twistAngleLow: float
        twistAngleHigh: float
        twistRestitutionLow: float
        twistRestitutionHigh: float
        twistSpringLow: float
        twistSpringHigh: float
        twistDampingLow: float
        twistDampingHigh: float
        posSpring: float
        posDamping: float
        swingSpring: float
        swingDamping: float
        twistSpring: float
        twistDamping: float
        Collision: bool
        breakable: bool
        maxForce: float
        maxTorque: float
        gearing: bool
        gearRatio: float
        useProjection: bool
        projectionMode: int
        projectionDist: float
        projectionAngle: float
        childAttachPoint: MXSWrapperBase
        childInitialTwist: float
        showVisualizer: bool
        useAcceleration: bool
        useHardLimits: bool
        ...
    class nvRagdoll(helper):
        helpersize: float
        boneGroups: None
        rootBone: None
        ragdollNode: None
        rbtype: int
        meshType: int
        inflation: float
        weight: float
        joints: None
        ...
    class nvSphere(GeometryClass):
        radius: float
        segs: int
        ...
    class nvpx(Interface):
        ...
    class nvpxConsts(Interface):
        ...
    class objXRefMgr(Interface):
        ...
    class objXRefs(Interface):
        ...
    class object(Value):
        ...
    class objectIDRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        colorMode: int
        ...
    class objectReferenceTarget(ReferenceTarget):
        type: int
        Static_Objects: bool
        Subframe_Placement: bool
        Separate_Group_Members: bool
        Separate_Children: bool
        Use_T2: bool
        Use_I3: bool
        Use_V4: bool
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        ...
    class objects(ObjectSet):
        ...
    class occlusionMap(Primitive):
        ...
    class offsetTimer(floatController):
        ...
    class okCancelBox(Primitive):
        ...
    class okToCreate(Primitive):
        ...
    class open(NodeGeneric):
        ...
    class openBitMap(Primitive):
        ...
    class openCTBitMap(Primitive):
        ...
    class openEdges(Interface):
        ...
    class openEncryptedFile(Primitive):
        ...
    class openUtility(Primitive):
        ...
    class openfile(Primitive):
        ...
    class openlog(Primitive):
        ...
    class optimize(modifier):
        autoEdge: bool
        renderLOD: int
        viewLOD: int
        facethreshold1: float
        edgethreshold1: float
        bias1: float
        preservemat1: bool
        preservesmooth1: bool
        maxedgelength1: float
        facethreshold2: float
        edgethreshold2: float
        bias2: float
        preservemat2: bool
        preservesmooth2: bool
        maxedgelength2: float
        manualupdate: bool
        ...
    class optimizeClipTransition(BipedGeneric):
        ...
    class optimizeTransitions(BipedGeneric):
        ...
    class orange(Color):
        ...
    class osl_Blackbody(textureMap):
        ...
    class osl_CameraProjector(textureMap):
        ...
    class osl_Candy(textureMap):
        ...
    class osl_Checker(textureMap):
        ...
    class osl_ColorAdd(textureMap):
        ...
    class osl_ColorClamp(textureMap):
        ...
    class osl_ColorComp(textureMap):
        ...
    class osl_ColorCurveGrad(textureMap):
        ...
    class osl_ColorCurves(textureMap):
        ...
    class osl_ColorDiv(textureMap):
        ...
    class osl_ColorJuggler(textureMap):
        ...
    class osl_ColorKey(textureMap):
        ...
    class osl_ColorMax(textureMap):
        ...
    class osl_ColorMin(textureMap):
        ...
    class osl_ColorMul(textureMap):
        ...
    class osl_ColorScale(textureMap):
        ...
    class osl_ColorSpace(textureMap):
        ...
    class osl_ColorSub(textureMap):
        ...
    class osl_ColorTweak(textureMap):
        ...
    class osl_Compare(textureMap):
        ...
    class osl_Composite(textureMap):
        ...
    class osl_DegToRad(textureMap):
        ...
    class osl_Digits(textureMap):
        ...
    class osl_EnvironmentBackground(textureMap):
        ...
    class osl_Falloff(textureMap):
        ...
    class osl_Float1ofN(textureMap):
        ...
    class osl_Float1ofNtextureMap(textureMap):
        ...
    class osl_Float2Int(textureMap):
        ...
    class osl_FloatACos(textureMap):
        ...
    class osl_FloatASin(textureMap):
        ...
    class osl_FloatATan(textureMap):
        ...
    class osl_FloatAbs(textureMap):
        ...
    class osl_FloatAdd(textureMap):
        ...
    class osl_FloatAngle(textureMap):
        ...
    class osl_FloatClamp(textureMap):
        ...
    class osl_FloatComp(textureMap):
        ...
    class osl_FloatCos(textureMap):
        ...
    class osl_FloatCurves(textureMap):
        ...
    class osl_FloatDiv(textureMap):
        ...
    class osl_FloatExp(textureMap):
        ...
    class osl_FloatInterpolate(textureMap):
        ...
    class osl_FloatLog(textureMap):
        ...
    class osl_FloatLogX(textureMap):
        ...
    class osl_FloatMax(textureMap):
        ...
    class osl_FloatMin(textureMap):
        ...
    class osl_FloatMod(textureMap):
        ...
    class osl_FloatMul(textureMap):
        ...
    class osl_FloatNegate(textureMap):
        ...
    class osl_FloatPow(textureMap):
        ...
    class osl_FloatRange(textureMap):
        ...
    class osl_FloatRecip(textureMap):
        ...
    class osl_FloatSin(textureMap):
        ...
    class osl_FloatSmoothStep(textureMap):
        ...
    class osl_FloatSqrt(textureMap):
        ...
    class osl_FloatSub(textureMap):
        ...
    class osl_FloatTan(textureMap):
        ...
    class osl_FourPointGradient(textureMap):
        ...
    class osl_GaborNoise(textureMap):
        ...
    class osl_GetAttribute(textureMap):
        ...
    class osl_GetCoordSpace(textureMap):
        ...
    class osl_GetFrame(textureMap):
        ...
    class osl_GetMtlID(textureMap):
        ...
    class osl_GetNodeID(textureMap):
        ...
    class osl_GetNodeName(textureMap):
        ...
    class osl_GetObjSpace(textureMap):
        ...
    class osl_GetObjectID(textureMap):
        ...
    class osl_GetParticleAge(textureMap):
        ...
    class osl_GetTime(textureMap):
        ...
    class osl_GetUVW(textureMap):
        ...
    class osl_GetWireColor(textureMap):
        ...
    class osl_Gradient2(textureMap):
        ...
    class osl_GreaterThan(textureMap):
        ...
    class osl_HDRILights(textureMap):
        ...
    class osl_HDRIenv(textureMap):
        ...
    class osl_HalftoneDots(textureMap):
        ...
    class osl_IdxRndCol(textureMap):
        ...
    class osl_IdxRndFlt(textureMap):
        ...
    class osl_IdxRndVec(textureMap):
        ...
    class osl_Interpolate(textureMap):
        ...
    class osl_LiftGammaGain(textureMap):
        ...
    class osl_Mandelbrot(textureMap):
        ...
    class osl_MatCapUV(textureMap):
        ...
    class osl_MixColor(textureMap):
        ...
    class osl_MixVector(textureMap):
        ...
    class osl_MultiMixColor(textureMap):
        ...
    class osl_Noise(textureMap):
        ...
    class osl_Noise3D(textureMap):
        ...
    class osl_Normal(textureMap):
        ...
    class osl_OSLBitmap2(textureMap):
        ...
    class osl_ObjectProjector(textureMap):
        ...
    class osl_PBRMixer(textureMap):
        ...
    class osl_RadToDeg(textureMap):
        ...
    class osl_RandomBitmaps2(textureMap):
        ...
    class osl_RandomIndex(textureMap):
        ...
    class osl_RandomTilingBitmap(textureMap):
        ...
    class osl_Rivets(textureMap):
        ...
    class osl_SetColor(textureMap):
        ...
    class osl_SetFile(textureMap):
        ...
    class osl_SetFloat(textureMap):
        ...
    class osl_SetInt(textureMap):
        ...
    class osl_SetNumFile(textureMap):
        ...
    class osl_SetString(textureMap):
        ...
    class osl_SetVector(textureMap):
        ...
    class osl_SimpleTiles(textureMap):
        ...
    class osl_SmoothStepC(textureMap):
        ...
    class osl_SpecGlosToPhysical(textureMap):
        ...
    class osl_SphericalProjector(textureMap):
        ...
    class osl_Threads(textureMap):
        ...
    class osl_ToonWidth(textureMap):
        ...
    class osl_TriTone(textureMap):
        ...
    class osl_UVWEnviron(textureMap):
        ...
    class osl_UVWRowOffset(textureMap):
        ...
    class osl_UVWTransform(textureMap):
        ...
    class osl_UberBitmap2(textureMap):
        ...
    class osl_UberColorCorrect(textureMap):
        ...
    class osl_UberNoise(textureMap):
        ...
    class osl_VectorAdd(textureMap):
        ...
    class osl_VectorCross(textureMap):
        ...
    class osl_VectorDist(textureMap):
        ...
    class osl_VectorDiv(textureMap):
        ...
    class osl_VectorDot(textureMap):
        ...
    class osl_VectorInv(textureMap):
        ...
    class osl_VectorJuggler(textureMap):
        ...
    class osl_VectorLength(textureMap):
        ...
    class osl_VectorMax(textureMap):
        ...
    class osl_VectorMin(textureMap):
        ...
    class osl_VectorMul(textureMap):
        ...
    class osl_VectorNorm(textureMap):
        ...
    class osl_VectorScale(textureMap):
        ...
    class osl_VectorSub(textureMap):
        ...
    class osl_WaveLength(textureMap):
        ...
    class osl_Waveform(textureMap):
        ...
    class osl_Weave(textureMap):
        ...
    class osl_WireFrame(textureMap):
        ...
    class output(textureMap):
        map1: None
        map1Enabled: bool
        output: MXSWrapperBase
        ...
    class outputTextColor(Color):
        ...
    class paramPublishMgr(Interface):
        ...
    class paramTypeToTypeName(Primitive):
        ...
    class paramWire(Interface):
        ...
    class parameter(ReferenceTarget):
        type: int
        Angle_Value: float
        Float_Value: float
        Integer_Value: int
        Percent_Value: float
        Time_Value: int
        World_Value: float
        Sync_Type: int
        Random_Seed: int
        Use_As_Modifier: bool
        Modifier_Type: int
        Angle_Offset: float
        Float_Offset: float
        Integer_Offset: int
        Percent_Offset: float
        Time_Offset: int
        World_Unit_Offset: float
        Real_Factor: float
        Integer_Factor: int
        filter: None
        Input_1: None
        ...
    class particleAge(NodeGeneric):
        ...
    class particleBlur(textureMap):
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        sharp: float
        ...
    class particleCenter(Primitive):
        ...
    class particleCount(NodeGeneric):
        ...
    class particleFlow(Interface):
        ...
    class particleFlowUtility(Interface):
        ...
    class particleLife(Primitive):
        ...
    class particleMesher(GeometryClass):
        pick: None
        renderTimeOnly: bool
        time: float
        radius: float
        useCustomBounds: bool
        boundsMin: MXSWrapperBase
        boundsMax: MXSWrapperBase
        useAllPFEvents: bool
        pfEventList: MXSWrapperBase
        ...
    class particlePos(NodeGeneric):
        ...
    class particleSize(NodeGeneric):
        ...
    class particleSize2(Primitive):
        ...
    class particleVelocity(NodeGeneric):
        ...
    class pasteBitmap(Primitive):
        ...
    class path(positionController):
        percent: float
        follow: bool
        path: None
        bank: bool
        bankAmount: float
        smoothness: float
        allowUpsideDown: bool
        constantVel: bool
        axis: int
        axisFlip: bool
        weight: MXSWrapperBase
        loop: bool
        relative: bool
        ...
    class pathInterp(NodeGeneric):
        ...
    class pathIsNetworkPath(Primitive):
        ...
    class pathTangent(NodeGeneric):
        ...
    class pathToLengthParam(NodeGeneric):
        ...
    class peekToken(Primitive):
        ...
    class perlinMarble(textureMap):
        map1: None
        map2: None
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1Enabled: bool
        map2Enabled: bool
        saturation1: float
        saturation2: float
        size: float
        level: float
        coords: MXSWrapperBase
        ...
    class perspectiveMatch(Generic):
        ...
    class pftParticleView(Interface):
        ...
    class physXpaneldata(PhysXPanel):
        ...
    class pi(Double):
        ...
    class pickAnimatable(Primitive):
        ...
    class pickObject(Primitive):
        ...
    class pickOffsetDistance(Primitive):
        ...
    class pickPoint(Primitive):
        ...
    class pivot(GeometryClass):
        height: float
        width: float
        depth: float
        Double_Doors: int
        Flip_Swing: bool
        Flip_Hinge: bool
        Create_Frame: bool
        Frame_Width: float
        Frame_Depth: float
        Door_Offset: float
        Leaf_Thickness: float
        Stiles_Top_Rail: float
        Bottom_Rail: float
        Number_of_Panels_Horizontally: int
        Number_of_Panels_Vertically: int
        Muntin: float
        Panel_Type: int
        Glass_Thickness: float
        Bevel_Angle: float
        Panel_Thickness_1: float
        Panel_Thickness_2: float
        Panel_Middle_Thickness: float
        Panel_Width_1: float
        Panel_Width_2: float
        Generate_Mapping_Coords: bool
        Open__degrees: float
        ...
    class playAnimation(Primitive):
        ...
    class pluginManager(Interface):
        ...
    class pngio(BitmapIO):
        ...
    class point3(Value):
        ...
    class point3Controller(MAXWrapper):
        ...
    class point3_ListDummyEntry(point3Controller):
        ...
    class point3_list(point3Controller):
        weight: MXSWrapperBase
        average: bool
        ...
    class point3_script(point3Controller):
        script: str
        ...
    class point4Controller(MAXWrapper):
        ...
    class point4_ListDummyEntry(point4Controller):
        ...
    class point4_list(point4Controller):
        weight: MXSWrapperBase
        average: bool
        ...
    class point4_script(point4Controller):
        script: str
        ...
    class pop(Interface):
        ...
    class popSkinCharSelected(MAXScriptFunction):
        ...
    class positionController(MAXWrapper):
        ...
    class position_ListDummyEntry(positionController):
        ...
    class position_list(positionController):
        weight: MXSWrapperBase
        average: bool
        ...
    class position_script(positionController):
        script: str
        ...
    class pow(Generic):
        ...
    class print(MappedGeneric):
        ...
    class printstack(NodeGeneric):
        ...
    class productAppID(Name):
        ...
    class progressBar(RolloutControl):
        ...
    class progressEnd(Primitive):
        ...
    class progressStart(Primitive):
        ...
    class progressUpdate(Primitive):
        ...
    class projectChangedRollout(RolloutClass):
        ...
    class projected(GeometryClass):
        height: float
        width: float
        depth: float
        Horizontal_Frame_Width: float
        Vertical_Frame_Width: float
        Frame_Thickness: float
        Glazing_Thickness: float
        Rail_Width: float
        Percent_Open: int
        Generate_Mapping_Coords: bool
        Middle_Height: float
        Bottom_Height: float
        ...
    class prs(Matrix3Controller):
        ...
    class pseudoColorExposureControl(ToneOperator):
        minimum: float
        maximum: float
        quantity: int
        display: int
        physicalScale: float
        automatic: bool
        scaleFunction: int
        unitSystemUsed: int
        active: bool
        processBG: bool
        ...
    class pxBake(MAXScriptFunction):
        ...
    class pxBakeAll(MAXScriptFunction):
        ...
    class pxBakeClothing(MAXScriptFunction):
        ...
    class pxBakeNodes(MAXScriptFunction):
        ...
    class pxBakeNodesUndoOn(MAXScriptFunction):
        ...
    class pxBakeSelection(MAXScriptFunction):
        ...
    class pxBakeSelectionUndoOn(MAXScriptFunction):
        ...
    class pxCurrentNodeType(Integer):
        ...
    class pxDebugVisualizerUndo(MAXScriptFunction):
        ...
    class pxJoint(helper):
        body0: None
        body1: None
        breakable: bool
        maxForce: float
        maxTorque: float
        Collision: bool
        projectionMode: int
        projectionDist: float
        projectionAngle: float
        gearing: bool
        gearRatio: float
        aptype: int
        swing1_limited: bool
        swing1_locked: bool
        swing1_angle: float
        swing1_rest: float
        swing1_spring: float
        swing1_damp: float
        swing2_limited: bool
        swing2_locked: bool
        swing2_angle: float
        swing2_rest: float
        swing2_spring: float
        swing2_damp: float
        twist_enbl: bool
        twistlow: float
        twisthigh: float
        twist_rest: float
        twist_spring: float
        twist_damp: float
        twist_lmt: bool
        helpersize: float
        x_state: int
        y_state: int
        z_state: int
        xlate_rad: float
        ...
    class pxRemoveInstances(MAXScriptFunction):
        ...
    class pxRestoreBake(MAXScriptFunction):
        ...
    class pxUnbake(MAXScriptFunction):
        ...
    class px_UpdateSelectedRigidBodyLists(MAXScriptFunction):
        ...
    class px_add_rigidbody(MAXScriptFunction):
        ...
    class px_current_version(Integer):
        ...
    class px_d6Panel_advanced(RolloutClass):
        ...
    class px_d6Panel_connection(RolloutClass):
        ...
    class px_d6Panel_spring(RolloutClass):
        ...
    class px_d6Panel_swingtwist(RolloutClass):
        ...
    class px_d6Panel_translation(RolloutClass):
        ...
    class px_exporter_clothing(RolloutClass):
        ...
    class px_exporter_destruction(RolloutClass):
        ...
    class px_exporter_general(RolloutClass):
        ...
    class px_exporter_options(RolloutClass):
        ...
    class px_exporter_scene_settings(RolloutClass):
        ...
    class px_filePostOpen(MAXScriptFunction):
        ...
    class px_filePreOpen(MAXScriptFunction):
        ...
    class px_filePreSave(MAXScriptFunction):
        ...
    class px_panel_advancedSettings(RolloutClass):
        ...
    class px_panel_debugVisualizer(RolloutClass):
        ...
    class px_panel_debugVisualizerApexClothing(RolloutClass):
        ...
    class px_panel_debugVisualizerClothing(RolloutClass):
        ...
    class px_panel_engine(RolloutClass):
        ...
    class px_panel_globalParameters(RolloutClass):
        ...
    class px_panel_multiedit_advanced(RolloutClass):
        ...
    class px_panel_multiedit_boxParams(RolloutClass):
        ...
    class px_panel_multiedit_capsuleParams(RolloutClass):
        ...
    class px_panel_multiedit_compositeParams(RolloutClass):
        ...
    class px_panel_multiedit_constraints_advanced(RolloutClass):
        ...
    class px_panel_multiedit_constraints_general(RolloutClass):
        ...
    class px_panel_multiedit_constraints_spring(RolloutClass):
        ...
    class px_panel_multiedit_constraints_swingTwistLimits(RolloutClass):
        ...
    class px_panel_multiedit_constraints_translationLimits(RolloutClass):
        ...
    class px_panel_multiedit_convexParams(RolloutClass):
        ...
    class px_panel_multiedit_customParams(RolloutClass):
        ...
    class px_panel_multiedit_forces(RolloutClass):
        ...
    class px_panel_multiedit_material(RolloutClass):
        ...
    class px_panel_multiedit_materialList(RolloutClass):
        ...
    class px_panel_multiedit_mesh(RolloutClass):
        ...
    class px_panel_multiedit_originalParams(RolloutClass):
        ...
    class px_panel_multiedit_properties(RolloutClass):
        ...
    class px_panel_multiedit_selection(RolloutClass):
        ...
    class px_panel_multiedit_sphereParams(RolloutClass):
        ...
    class px_panel_rigidBodyDisplay(RolloutClass):
        ...
    class px_panel_simulation(RolloutClass):
        ...
    class px_panel_tools_destruction(RolloutClass):
        ...
    class px_panel_tools_simulation(RolloutClass):
        ...
    class px_panel_tools_utilities(RolloutClass):
        ...
    class px_physXPanel(RolloutClass):
        ...
    class px_plugin_unitscale(Double):
        ...
    class px_plugin_unittype(Integer):
        ...
    class px_plugin_version(Integer):
        ...
    class px_rb_solveritertions(Integer):
        ...
    class px_sdk_bouncethresh(Double):
        ...
    class px_sdk_ccd_epsilon(Double):
        ...
    class px_sdk_ccd_motion_threshold(Integer):
        ...
    class px_sdk_contactDistance(Double):
        ...
    class px_sdk_dynamicfrictionscaling(Integer):
        ...
    class px_sdk_gravityDirection(Integer):
        ...
    class px_sdk_gravityx(Integer):
        ...
    class px_sdk_gravityy(Integer):
        ...
    class px_sdk_gravityz(Double):
        ...
    class px_sdk_max_angvel(Double):
        ...
    class px_sdk_skinwidth(Double):
        ...
    class px_sdk_sleep_energy(Double):
        ...
    class px_sdk_staticfrictionscaling(Integer):
        ...
    class px_sdk_sub_sim_steps(Integer):
        ...
    class px_selectionChanged(MAXScriptFunction):
        ...
    class px_selectionChangedDirty(MAXScriptFunction):
        ...
    class px_stopSimulationForEditing(MAXScriptFunction):
        ...
    class px_syncRagdollList(MAXScriptFunction):
        ...
    class px_systemPostNew(MAXScriptFunction):
        ...
    class px_systemPostReset(MAXScriptFunction):
        ...
    class px_systemPreNew(MAXScriptFunction):
        ...
    class px_systemPreReset(MAXScriptFunction):
        ...
    class px_systemPreShutdown(MAXScriptFunction):
        ...
    class python(Interface):
        ...
    class pythonPromptColor(Color):
        ...
    class qorthog(Generic):
        ...
    class qsort(Primitive):
        ...
    class quadMenuSettings(Interface):
        ...
    class quadPatch(GeometryClass):
        length: float
        lengthsegs: int
        width: float
        widthsegs: int
        mapcoords: bool
        ...
    class quatArrayToEulerArray(Primitive):
        ...
    class quatToEuler(Primitive):
        ...
    class quatToEuler2(Primitive):
        ...
    class queryBox(Primitive):
        ...
    class quitMax(Primitive):
        ...
    class rApplyIKChain(RolloutClass):
        ...
    class rCATRigMapping(RolloutClass):
        ...
    class rCaptureAnim(RolloutClass):
        ...
    class rCollapseLayers(RolloutClass):
        ...
    class rGizmos(RolloutClass):
        ...
    class rImportBIP(RolloutClass):
        ...
    class rImportBVH(RolloutClass):
        ...
    class rImportHTR(RolloutClass):
        ...
    class rLMR(RolloutClass):
        ...
    class rLoadFile(RolloutClass):
        ...
    class rMergeAnim(RolloutClass):
        ...
    class rObjectMapping(RolloutClass):
        ...
    class rPoseMixer(RolloutClass):
        ...
    class rSaveFile(RolloutClass):
        ...
    class radToDeg(Primitive):
        ...
    class radianceMap(ReferenceTarget):
        ...
    class radiosityMeshOps(Interface):
        ...
    class radiusManip(helper):
        ...
    class random(Generic):
        ...
    class randomReferenceTarget(ReferenceTarget):
        Output_Type: int
        Integer_Distribution_Type: int
        Real_Distribution_Type: int
        Vector_Distribution_Type: int
        Parameter_1: float
        Parameter_2: float
        Parameter_3: float
        Positive_Parameter_1: float
        Positive_Parameter_2: float
        Positive_Parameter_3: float
        Integer_Parameter_1: int
        Integer_Parameter_2: int
        Integer_Parameter_3: int
        Sync_Type: int
        Random_Seed: int
        Use_E3: bool
        Use_E4: bool
        Use_E5: bool
        Use_E6: bool
        Use_E7: bool
        iterations: float
        filter: None
        Input_1: None
        Input_2: None
        Input_3: None
        Input_4: None
        Input_5: None
        Input_6: None
        Input_7: None
        ...
    class raytraceShadow(Shadow):
        raytraceBias: float
        maxDepth: int
        twoSidedShadows: bool
        ...
    class reactTo(Primitive):
        ...
    class reactionMgr(Interface):
        ...
    class readChar(Generic):
        ...
    class readChars(Generic):
        ...
    class readDelimitedString(Generic):
        ...
    class readExpr(Generic):
        ...
    class readLine(Generic):
        ...
    class readToken(Primitive):
        ...
    class readValue(Generic):
        ...
    class rectify(Generic):
        ...
    class red(Color):
        ...
    class redrawViews(Primitive):
        ...
    class redrawViewsCallbacksEnabled(Primitive):
        ...
    class reduceKeys(MappedGeneric):
        ...
    class reference(NodeGeneric):
        ...
    class referenceReplace(NodeGeneric):
        ...
    class refhierarchy(Interface):
        ...
    class refine(NURBSGenericMethodsWrapper):
        ...
    class refineSegment(NodeGeneric):
        ...
    class refineU(NURBSGenericMethodsWrapper):
        ...
    class refineV(NURBSGenericMethodsWrapper):
        ...
    class reflectRefract(textureMap):
        size: int
        blur: float
        blurOffset: float
        near: float
        far: float
        source: int
        useAtmosphericMap: bool
        apply: bool
        frametype: int
        nthframe: int
        bitmapName: MXSWrapperBase
        outputname: None
        ...
    class reflectionRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class refractionRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class registerDisplayFilterCallback(Primitive):
        ...
    class registerFileChangedFunction(Primitive):
        ...
    class registerOLEInterface(Primitive):
        ...
    class registerRedrawViewsCallback(Primitive):
        ...
    class registerRightClickMenu(Primitive):
        ...
    class registerSelectFilterCallback(Primitive):
        ...
    class registerTimeCallback(Primitive):
        ...
    class registerViewWindow(Primitive):
        ...
    class releaseAllOLEObjects(Primitive):
        ...
    class releaseOLEObject(Primitive):
        ...
    class removeDir(Primitive):
        ...
    class removeObject(NURBSGenericMethodsWrapper):
        ...
    class removeRollout(Primitive):
        ...
    class renameFile(Primitive):
        ...
    class rendEnd(Time):
        ...
    class rendFieldOrder(Integer):
        ...
    class rendFileNumberBase(Integer):
        ...
    class rendImageAspectRatio(Double):
        ...
    class rendImgSeqType(Integer):
        ...
    class rendNTSC_PAL(Integer):
        ...
    class rendNThFrame(Integer):
        ...
    class rendPixelAspectRatio(Double):
        ...
    class rendStart(Time):
        ...
    class rendSuperBlackThresh(Integer):
        ...
    class rendTimeType(Integer):
        ...
    class rendVidCorrectMethod(Integer):
        ...
    class rendViewID(Integer):
        ...
    class render(Primitive):
        ...
    class renderEffect(MAXWrapper):
        ...
    class renderHeight(Integer):
        ...
    class renderMap(Generic):
        ...
    class renderMessageManager(Interface):
        ...
    class renderPixelAspect(Double):
        ...
    class renderPresets(Interface):
        ...
    class renderWidth(Integer):
        ...
    class renderer(Name):
        ...
    class reparameterize(NURBSGenericMethodsWrapper):
        ...
    class replace(Generic):
        ...
    class replaceInstances(Primitive):
        ...
    class replace_CRLF_with_LF(Primitive):
        ...
    class replace_LF_with_CRLF(Primitive):
        ...
    class resample(Generic):
        ...
    class reset(Generic):
        ...
    class resetLattice(Primitive):
        ...
    class resetLengthInterp(Primitive):
        ...
    class resetMaxFile(Primitive):
        ...
    class resetShape(NodeGeneric):
        ...
    class resetZoom(Generic):
        ...
    class retryCancelBox(Primitive):
        ...
    class retryIgnoreAbortBox(Primitive):
        ...
    class reverse(NodeGeneric):
        ...
    class reverseTime(MappedGeneric):
        ...
    class rgb(BitmapIO):
        ...
    class rgbMult(textureMap):
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1: None
        map2: None
        map1Enabled: bool
        map2Enabled: bool
        alphaFrom: int
        ...
    class rgbTint(textureMap):
        red: MXSWrapperBase
        green: MXSWrapperBase
        blue: MXSWrapperBase
        map1: None
        map1Enabled: bool
        ...
    class rolloutFloater(Value):
        ...
    class rollup(Interface):
        ...
    class rootNode(MAXRootNode):
        ...
    class rootScene(Scene):
        ...
    class rotation(helper):
        direction: int
        Euler_X: float
        Euler_Y: float
        Euler_Z: float
        Divergence: float
        Restrict_Divergence_To_Axis: bool
        Divergence_Axis_X: float
        Divergence_Axis_Y: float
        Divergence_Axis_Z: float
        Random_Seed: int
        ...
    class rotationController(MAXWrapper):
        ...
    class rotation_ListDummyEntry(rotationController):
        ...
    class rotation_list(rotationController):
        weight: MXSWrapperBase
        average: bool
        ...
    class rotation_script(rotationController):
        script: str
        ...
    class save(Generic):
        ...
    class saveCurrentPathConfigFile(MAXScriptFunction):
        ...
    class saveMaterialLibrary(Primitive):
        ...
    class saveMaxFile(Primitive):
        ...
    class saveMixFile(BipedGeneric):
        ...
    class saveMoFlowFile(BipedGeneric):
        ...
    class saveNodes(Primitive):
        ...
    class saveTempMaterialLibrary(Primitive):
        ...
    class scale(NodeGeneric):
        ...
    class scaleClip(BipedGeneric):
        ...
    class scaleController(MAXWrapper):
        ...
    class scaleTime(MappedGeneric):
        ...
    class scale_ListDummyEntry(scaleController):
        ...
    class scale_list(scaleController):
        weight: MXSWrapperBase
        average: bool
        ...
    class scale_script(scaleController):
        script: str
        ...
    class scaledLocalToGlobal(BipedGeneric):
        ...
    class scaledLocalToLocal(BipedGeneric):
        ...
    class scanForNewPlugins(Primitive):
        ...
    class sceneStateMgr(Interface):
        ...
    class schematicviews(Interface):
        ...
    class section(shape):
        length: float
        width: float
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        ...
    class seed(Primitive):
        ...
    class seek(Generic):
        ...
    class select(NodeGeneric):
        ...
    class selectBitMap(Primitive):
        ...
    class selectByName(Primitive):
        ...
    class selectCTBitMap(Primitive):
        ...
    class selectFilterCallbacksEnabled(Primitive):
        ...
    class selectKey(Generic):
        ...
    class selectKeys(MappedGeneric):
        ...
    class selectReaction(Primitive):
        ...
    class selection(ObjectSet):
        ...
    class selectionChangeFn(MAXScriptFunction):
        ...
    class selectionToBitmap(Primitive):
        ...
    class selectmore(NodeGeneric):
        ...
    class set(Value):
        ...
    class setActive(Primitive):
        ...
    class setAfterORT(MappedGeneric):
        ...
    class setAppData(Generic):
        ...
    class setArrowCursor(Primitive):
        ...
    class setAsBackground(Generic):
        ...
    class setAtmospheric(Primitive):
        ...
    class setBeforeORT(MappedGeneric):
        ...
    class setCV(NURBSGenericMethodsWrapper):
        ...
    class setCacheEntry(Generic):
        ...
    class setCurve(NURBSGenericMethodsWrapper):
        ...
    class setCurveByID(NURBSGenericMethodsWrapper):
        ...
    class setCurveStartPoint(NURBSGenericMethodsWrapper):
        ...
    class setD3DMeshCacheSize(Primitive):
        ...
    class setDimensions(Primitive):
        ...
    class setDisplacementMapping(Generic):
        ...
    class setEdge(NURBSGenericMethodsWrapper):
        ...
    class setEdgeSelection(NodeGeneric):
        ...
    class setEdgeVis(Generic):
        ...
    class setEffect(Primitive):
        ...
    class setFaceMatID(Generic):
        ...
    class setFaceSelection(NodeGeneric):
        ...
    class setFaceSmoothGroup(Generic):
        ...
    class setFade(Generic):
        ...
    class setFileAttribute(Primitive):
        ...
    class setFilter(BipedGeneric):
        ...
    class setFirstKnot(NodeGeneric):
        ...
    class setFirstSpline(NodeGeneric):
        ...
    class setFlip(NURBSGenericMethodsWrapper):
        ...
    class setFlipTrim(NURBSGenericMethodsWrapper):
        ...
    class setFocus(Primitive):
        ...
    class setForegroundWindow(Primitive):
        ...
    class setGenerateUVs(NURBSGenericMethodsWrapper):
        ...
    class setGroupHead(Primitive):
        ...
    class setGroupMember(Primitive):
        ...
    class setGroupOpen(Primitive):
        ...
    class setINISetting(Primitive):
        ...
    class setInVec(NodeGeneric):
        ...
    class setIndexedPixels(Generic):
        ...
    class setIndexedProperty(Primitive):
        ...
    class setInheritanceFlags(MappedPrimitive):
        ...
    class setIniForceUTF16Default(Primitive):
        ...
    class setKnot(NURBSGenericMethodsWrapper):
        ...
    class setKnotPoint(NodeGeneric):
        ...
    class setKnotSelection(Primitive):
        ...
    class setKnotType(NodeGeneric):
        ...
    class setListenerSel(Primitive):
        ...
    class setListenerSelText(Primitive):
        ...
    class setMAXFileAssetMetadata(Primitive):
        ...
    class setMKTime(Primitive):
        ...
    class setMKWeight(Primitive):
        ...
    class setMTLMEditFlags(Primitive):
        ...
    class setMTLMeditObjType(Primitive):
        ...
    class setMTLMeditTiling(Primitive):
        ...
    class setMaterialID(Primitive):
        ...
    class setMeditMaterial(Primitive):
        ...
    class setMesh(Generic):
        ...
    class setModContextBBox(Primitive):
        ...
    class setModContextTM(Primitive):
        ...
    class setMorphTarget(Primitive):
        ...
    class setMorphTargetName(Primitive):
        ...
    class setNeedsRedraw(Primitive):
        ...
    class setNumCPVVerts(Generic):
        ...
    class setNumFaces(Generic):
        ...
    class setNumTVerts(Generic):
        ...
    class setNumVerts(Generic):
        ...
    class setNumberThreads(Primitive):
        ...
    class setObject(NURBSGenericMethodsWrapper):
        ...
    class setOpenSceneScript(Primitive):
        ...
    class setOutVec(NodeGeneric):
        ...
    class setParent(NURBSGenericMethodsWrapper):
        ...
    class setParentID(NURBSGenericMethodsWrapper):
        ...
    class setPixels(Generic):
        ...
    class setPoint(NURBSGenericMethodsWrapper):
        ...
    class setProdTess(NURBSGenericMethodsWrapper):
        ...
    class setProgressCancel(Primitive):
        ...
    class setProperty(Primitive):
        ...
    class setPropertyController(Primitive):
        ...
    class setRadius(NURBSGenericMethodsWrapper):
        ...
    class setReactionFalloff(Primitive):
        ...
    class setReactionInfluence(Primitive):
        ...
    class setReactionName(Primitive):
        ...
    class setReactionState(Primitive):
        ...
    class setReactionStrength(Primitive):
        ...
    class setReactionValue(Primitive):
        ...
    class setRenderApproximation(Primitive):
        ...
    class setSaveRequired(Primitive):
        ...
    class setSaveSceneScript(Primitive):
        ...
    class setSeed(NURBSGenericMethodsWrapper):
        ...
    class setSegSelection(Primitive):
        ...
    class setSegmentType(NodeGeneric):
        ...
    class setSelectedPts(CurveCtlGeneric):
        ...
    class setSelectionLevel(Primitive):
        ...
    class setSize(Generic):
        ...
    class setSplineSelection(Primitive):
        ...
    class setSplitMesh(Generic):
        ...
    class setStruct(Generic):
        ...
    class setSubMtl(Primitive):
        ...
    class setSubTexmap(Primitive):
        ...
    class setSubdivisionDisplacement(Generic):
        ...
    class setSurfaceDisplay(Primitive):
        ...
    class setTVFace(Generic):
        ...
    class setTextureSurface(NURBSGenericMethodsWrapper):
        ...
    class setTextureUVs(NURBSGenericMethodsWrapper):
        ...
    class setTiling(NURBSGenericMethodsWrapper):
        ...
    class setTilingOffset(NURBSGenericMethodsWrapper):
        ...
    class setTimeRange(MappedGeneric):
        ...
    class setTransformLockFlags(MappedPrimitive):
        ...
    class setTrimSurface(NURBSGenericMethodsWrapper):
        ...
    class setUCurve(NURBSGenericMethodsWrapper):
        ...
    class setUCurveByID(NURBSGenericMethodsWrapper):
        ...
    class setUKnot(NURBSGenericMethodsWrapper):
        ...
    class setUseOldD3DCache(Primitive):
        ...
    class setUserProp(NodeGeneric):
        ...
    class setUserPropBuffer(NodeGeneric):
        ...
    class setUserPropVal(Primitive):
        ...
    class setVCFace(Generic):
        ...
    class setVCurve(NURBSGenericMethodsWrapper):
        ...
    class setVCurveByID(NURBSGenericMethodsWrapper):
        ...
    class setVKnot(NURBSGenericMethodsWrapper):
        ...
    class setVert(Generic):
        ...
    class setVertColor(Generic):
        ...
    class setVertSelection(NodeGeneric):
        ...
    class setVertexPaintAmounts(Primitive):
        ...
    class setVertexPaintColors(Primitive):
        ...
    class setViewApproximation(Primitive):
        ...
    class setViewTess(NURBSGenericMethodsWrapper):
        ...
    class setWaitCursor(Primitive):
        ...
    class setclipboardBitmap(Primitive):
        ...
    class setclipboardText(Primitive):
        ...
    class setface(Generic):
        ...
    class setfacenormal(Generic):
        ...
    class setnormal(Generic):
        ...
    class settvert(Generic):
        ...
    class setupEvents(Primitive):
        ...
    class sgi(BitmapIO):
        ...
    class shadowMap(Shadow):
        twoSidedShadows: bool
        mapsize: int
        samplerange: float
        mapbias: float
        absoluteMapBias: bool
        ...
    class shape(node):
        ...
    class shapes(ObjectSet):
        ...
    class show(MAXScriptFunction):
        ...
    class showClass(Primitive):
        ...
    class showEvents(Generic):
        ...
    class showHWTextureMap(Primitive):
        ...
    class showInterface(Generic):
        ...
    class showInterfaces(Generic):
        ...
    class showMethods(Generic):
        ...
    class showNodeEventCallbacks(Primitive):
        ...
    class showProjectSwitchDialog(MAXScriptFunction):
        ...
    class showProperties(Generic):
        ...
    class showSource(Primitive):
        ...
    class showTextureMap(Primitive):
        ...
    class showTrack(Generic):
        ...
    class showregisteredDisplayFilterCallbacks(Primitive):
        ...
    class showregisteredRedrawViewsCallbacks(Primitive):
        ...
    class showregisteredSelectFilterCallbacks(Primitive):
        ...
    class showregisteredTimeCallbacks(Primitive):
        ...
    class silentValue(NoValueClass):
        ...
    class simpleFaceManager(Interface):
        ...
    class sin(Generic):
        ...
    class sinh(Generic):
        ...
    class sketchUp(ImporterPlugin):
        ...
    class skipSpace(Primitive):
        ...
    class skipToNextLine(Generic):
        ...
    class skipToString(Generic):
        ...
    class sleep(Primitive):
        ...
    class sliderManipulator(helper):
        value: float
        minVal: float
        maxVal: float
        xPos: float
        yPos: float
        width: float
        hide: bool
        sldName: str
        snapToggle: bool
        snapVal: float
        ...
    class sliderTime(Time):
        ...
    class smooth(modifier):
        autosmooth: bool
        preventIndirect: bool
        threshold: float
        smoothingBits: int
        ...
    class smoothReferenceTarget(ReferenceTarget):
        objects: MXSWrapperBase
        filterDelegates: bool
        wholeAnim: int
        to: int
        positions: bool
        rotations: bool
        reduce: bool
        n: int
        filter: bool
        pastkeys: int
        futurekeys: int
        smoothness: int
        ...
    class snapshot(NodeGeneric):
        ...
    class snapshotAsMesh(Primitive):
        ...
    class sort(Generic):
        ...
    class sortKeys(MappedGeneric):
        ...
    class sortNoteKeys(Generic):
        ...
    class spacewarps(ObjectSet):
        ...
    class specularMap(BakeElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        outputSzX: int
        outputSzY: int
        autoSzOn: bool
        filename: str
        filenameUnique: bool
        fileType: str
        backgroundColor: MXSWrapperBase
        lightingOn: bool
        shadowsOn: bool
        targetMapSlotName: str
        ...
    class specularRenderElement(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        ...
    class speed(helper):
        speed: float
        variation: float
        direction: int
        reverse: bool
        Divergence: float
        Random_Seed: int
        ...
    class spin(helper):
        SpinRate: float
        variation: float
        direction: int
        Spin_X_Axis: float
        Spin_Y_Axis: float
        Spin_Z_Axis: float
        Divergence: float
        Random_Seed: int
        ...
    class sqrt(Generic):
        ...
    class squadrev(Primitive):
        ...
    class srr_exports(Interface):
        ...
    class stack(Primitive):
        ...
    class stackLimit(Integer):
        ...
    class standard(material):
        shaderType: int
        wire: bool
        twoSided: bool
        faceMap: bool
        faceted: bool
        shaderByName: str
        opacityType: int
        opacity: float
        FilterColor: MXSWrapperBase
        filterMap: None
        opacityFallOffType: int
        opacityFallOff: float
        ior: float
        wireSize: float
        wireUnits: int
        applyReflectionDimming: bool
        dimLevel: float
        reflectionLevel: float
        sampler: int
        samplerQuality: float
        samplerEnable: bool
        samplerAdaptThreshold: float
        samplerAdaptOn: bool
        subSampleTextureOn: bool
        samplerAdvancedOptions: bool
        samplerByName: str
        UserParam0: float
        UserParam1: float
        samplerUseGlobal: bool
        mapEnables: MXSWrapperBase
        maps: MXSWrapperBase
        mapAmounts: MXSWrapperBase
        adTextureLock: bool
        ...
    class startObjectCreation(Primitive):
        ...
    class startTool(Primitive):
        ...
    class statusPanel(Interface):
        ...
    class stop(helper):
        position: MXSWrapperBase
        rotation: MXSWrapperBase
        ...
    class stopAnimation(Primitive):
        ...
    class stopTool(Primitive):
        ...
    class strRagdollHelperMesh(StringStream):
        ...
    class stricmp(Primitive):
        ...
    class string(Value):
        ...
    class styleMgr(Interface):
        ...
    class subAnim(Value):
        ...
    class subRollout(RolloutControl):
        ...
    class subSurfaceMap(Primitive):
        ...
    class subdivide(modifier):
        size: float
        subdivideDoEnforceQuality: bool
        subdivideDoSubdivideTriangles: bool
        showAllTriangles: bool
        subdivideMaxSteinerPoints: int
        subdivideQuadAreaRatio: float
        subdivideDiagonalRatio: float
        subdivideNumBuckets: int
        subdivideDoFormQuads: bool
        subdivideRefinementType: int
        manualupdate: int
        remeshType: int
        preserveMeshData: bool
        preservedMapIndex: int
        preserveSharpEdgesByAngle: bool
        preservedSharpEdgeAngle: float
        delaunaySize: float
        delaunayRelaxationCoeff: float
        delaunayRelaxationIterations: int
        adaptiveEdgeLength: float
        adaptiveRegularity: float
        adaptiveThreshold: float
        variableCurvatureEdgeLength: float
        variableCurvatureRegularity: float
        variableCurvatureThreshold: float
        variableCurvatureVariableDensity: float
        variableCurvatureIterations: int
        variableCurvatureTransition: float
        ...
    class subdivideSegment(Primitive):
        ...
    class subdivideSpacewarpModifier(SpacewarpModifier):
        size: float
        subdivideDoEnforceQuality: bool
        subdivideDoSubdivideTriangles: bool
        showAllTriangles: bool
        subdivideMaxSteinerPoints: int
        subdivideQuadAreaRatio: float
        subdivideDiagonalRatio: float
        subdivideNumBuckets: int
        subdivideDoFormQuads: bool
        subdivideRefinementType: int
        manualupdate: int
        remeshType: int
        preserveMeshData: bool
        preservedMapIndex: int
        preserveSharpEdgesByAngle: bool
        preservedSharpEdgeAngle: float
        delaunaySize: float
        delaunayRelaxationCoeff: float
        delaunayRelaxationIterations: int
        adaptiveEdgeLength: float
        adaptiveRegularity: float
        adaptiveThreshold: float
        variableCurvatureEdgeLength: float
        variableCurvatureRegularity: float
        variableCurvatureThreshold: float
        variableCurvatureVariableDensity: float
        variableCurvatureIterations: int
        variableCurvatureTransition: float
        ...
    class substituteString(Primitive):
        ...
    class substring(Generic):
        ...
    class superClassOf(Generic):
        ...
    class supportsTimeOperations(Generic):
        ...
    class surface(modifier):
        steps: int
        threshold: float
        ...
    class swap(Primitive):
        ...
    class sweep(modifier):
        shapes: MXSWrapperBase
        UnionIntersections: bool
        CustomShapeName: None
        CurrentBuiltInShape: int
        CustomShape: int
        MirrorXZPlane: bool
        MirrorXYPlane: bool
        XOffset: float
        yOffset: float
        angle: float
        GenerateMappingCoords: bool
        realWorldMapSize: bool
        GenMatIDs: bool
        UseSectionIDs: bool
        UsePathIDs: bool
        PivotAlignment: int
        SmoothSection: bool
        SmoothPath: bool
        Banking: bool
        AssignCSType: int
        ...
    class swirl(textureMap):
        swirl: MXSWrapperBase
        base: MXSWrapperBase
        Swirl_Intensity: float
        Twist: float
        Color_Contrast: float
        Center_Position_Y: float
        Center_Position_X: float
        Swirl_Amount: float
        Constant_Detail: int
        Random_Seed: float
        Lock_Background: int
        swirlMap: None
        baseMap: None
        swirlMapEnabled: bool
        baseMapEnabled: bool
        coords: MXSWrapperBase
        ...
    class symmetry(modifier):
        axis: int
        flip: bool
        slice: int
        weld: int
        threshold: float
        ...
    class systems(ObjectSet):
        ...
    class tan(Generic):
        ...
    class tangentBezier3D(Primitive):
        ...
    class tangentCurve3D(Primitive):
        ...
    class tanh(Generic):
        ...
    class targetSpot(light):
        aspect: float
        rgb: MXSWrapperBase
        color: MXSWrapperBase
        contrast: float
        enabled: bool
        on: bool
        type: MXSWrapperBase
        value: int
        falloff: float
        excludeList: MXSWrapperBase
        includeList: None
        showCone: bool
        multiplier: float
        softenDiffuseEdge: float
        hotspot: float
        farAttenStart: float
        farAttenEnd: float
        nearAttenStart: float
        nearAttenEnd: float
        atmosOpacity: float
        atmosColorAmt: float
        decayRadius: float
        shadowColor: MXSWrapperBase
        shadowMultiplier: float
        hsv: MXSWrapperBase
        hue: int
        saturation: int
        inclExclType: int
        affectDiffuse: bool
        affectSpecular: bool
        useNearAtten: bool
        showNearAtten: bool
        useFarAtten: bool
        showFarAtten: bool
        attenDecay: int
        projector: bool
        projectorMap: None
        castShadows: bool
        useGlobalShadowSettings: bool
        raytracedShadows: bool
        overShoot: bool
        coneShape: int
        lightShape: int
        atmosShadows: bool
        lightAffectsShadow: bool
        shadowProjectorMap: None
        useShadowProjectorMap: bool
        ambientOnly: bool
        shadowgenerator: MXSWrapperBase
        ...
    class tcb_float(floatController):
        ...
    class tcb_point3(point3Controller):
        ...
    class tcb_point4(point4Controller):
        ...
    class tcb_position(positionController):
        ...
    class tcb_rotation(rotationController):
        ...
    class tcb_scale(scaleController):
        ...
    class tessellate(modifier):
        type: int
        tension: float
        iterations: int
        faceType: int
        updateWhen: int
        ...
    class test_safearray(Primitive):
        ...
    class text(shape):
        size: float
        steps: int
        text: str
        render_renderable: bool
        render_mapcoords: bool
        render_viewport_thickness: float
        render_viewport_sides: int
        render_viewport_angle: float
        render_displayRenderMesh: bool
        render_useViewportSettings: bool
        render_displayRenderSettings: bool
        thickness: float
        sides: int
        angle: float
        renderable: bool
        mapcoords: bool
        viewport_thickness: float
        viewport_sides: int
        viewport_angle: float
        displayRenderMesh: bool
        useViewportSettings: bool
        displayRenderSettings: bool
        cap: bool
        optimize: bool
        adaptive: bool
        render_viewport_length: float
        render_viewport_width: float
        render_viewport_angle2: float
        render_rectangular: bool
        render_viewport_rectangular: bool
        render_aspect_locked: bool
        render_viewport_aspect_locked: bool
        render_auto_smooth: bool
        realWorldMapSize: bool
        twist_correction: bool
        quad_cap: bool
        sphere_cap: float
        cap_segments: int
        kerning: float
        leading: float
        font: str
        italic: bool
        underline: bool
        alignment: int
        ...
    class textureMap(material):
        ...
    class textureWrap(Primitive):
        ...
    class tgaio(BitmapIO):
        ...
    class thawSelection(Primitive):
        ...
    class thePainterInterface(ReferenceTarget):
        nodes: MXSWrapperBase
        drawRing: bool
        drawNormal: bool
        drawTrace: bool
        minSize: float
        maxSize: float
        minStr: float
        maxStr: float
        additiveMode: bool
        falloffGraph: MXSWrapperBase
        pressureEnable: bool
        pressureAffects: int
        updateOnMouseUp: bool
        quadDepth: int
        predefinedStrEnable: bool
        predefinedStrGraph: MXSWrapperBase
        predefinedSizeEnable: bool
        predefinedSizeGraph: MXSWrapperBase
        mirrorEnable: bool
        mirrorAxis: int
        mirrorOffset: float
        mirrorGizmoSize: float
        pointGatherEnable: bool
        buildVNormals: bool
        lagRate: int
        normalScale: float
        marker: float
        markerEnable: bool
        offMeshHitType: bool
        offMeshHitZDepth: float
        offMeshHitPos: MXSWrapperBase
        strDragLimitMin: float
        strDragLimitMax: float
        SplineConstraintNode: None
        ...
    class thinWallRefraction(textureMap):
        blur: float
        thicknessOffset: float
        bumpMapEffect: float
        applyBlur: bool
        nthframe: int
        useEnviroment: bool
        frame: int
        ...
    class threads(Primitive):
        ...
    class ticksPerFrame(Integer):
        ...
    class tifio(BitmapIO):
        ...
    class tiles(textureMap):
        Bricks: None
        Mortar_Map: None
        Bricks_Map: None
        Mortar: None
        Random_Seed: int
        Mortar_Color: MXSWrapperBase
        Brick_Color: MXSWrapperBase
        Horizontal_Count: float
        Vertical_Count: float
        Color_Variance: float
        Vertical_Gap: float
        Horizontal_Gap: float
        Line_Shift: float
        Random_Shift: float
        Holes: int
        Lock_Gap_Symmetry: int
        Fade_Variance: float
        Edge_Roughness: float
        Show_Texture_Swatches: int
        Use_Row_Edit: int
        Use_Column_Edit: int
        Change_Row: float
        Change_Column: float
        Per_Column: int
        Per_Row: int
        Tile_Type: int
        ...
    class time(Value):
        ...
    class timeCallbacksEnabled(Primitive):
        ...
    class timeDisplayMode(Name):
        ...
    class timeGetTime(Primitive):
        ...
    class timeSlider(Interface):
        ...
    class timeStamp(Primitive):
        ...
    class tmGizmos(Interface):
        ...
    class toLower(Generic):
        ...
    class toUpper(Generic):
        ...
    class topBottomMat(material):
        topMaterial: MXSWrapperBase
        bottomMaterial: MXSWrapperBase
        map1Enabled: bool
        map2Enabled: bool
        Blend: float
        position: float
        Coordinates: int
        ...
    class tprofiler(GlobalUtilityPlugin):
        ...
    class trackSelectionSets(Interface):
        ...
    class trackViewNodes(MAXTVNode):
        ...
    class trackViewUtility(MAXWrapperNonRefTarg):
        ...
    class trackviews(Interface):
        ...
    class transform(Primitive):
        ...
    class transform_script(Matrix3Controller):
        script: str
        ...
    class transpose(Generic):
        ...
    class triPatch(GeometryClass):
        length: float
        width: float
        mapcoords: bool
        ...
    class triggerNodeEventCallback(Primitive):
        ...
    class trimExtend(Primitive):
        ...
    class trimLeft(Primitive):
        ...
    class trimRight(Primitive):
        ...
    class turbulence(Primitive):
        ...
    class tverts(Interface):
        ...
    class typeNameToParamType(Primitive):
        ...
    class unDisplay(Generic):
        ...
    class unRegisterViewWindow(Primitive):
        ...
    class unbindKnot(NodeGeneric):
        ...
    class unfreeze(NodeGeneric):
        ...
    class ungroup(Primitive):
        ...
    class unhide(NodeGeneric):
        ...
    class unhideSegments(NodeGeneric):
        ...
    class uniqueName(Primitive):
        ...
    class unmaz(Primitive):
        ...
    class unregisterAllRightClickMenus(Primitive):
        ...
    class unregisterDisplayFilterCallback(Primitive):
        ...
    class unregisterRedrawViewsCallback(Primitive):
        ...
    class unregisterRightClickMenu(Primitive):
        ...
    class unregisterSelectFilterCallback(Primitive):
        ...
    class unregisterTimeCallback(Primitive):
        ...
    class unwrapUIdialog(RolloutClass):
        ...
    class update(Generic):
        ...
    class updateBindList(NodeGeneric):
        ...
    class updateMTLInMedit(Primitive):
        ...
    class updateRolloutLayout(Primitive):
        ...
    class updateShape(NodeGeneric):
        ...
    class updateSurfaceMapper(Primitive):
        ...
    class updateToolbarButtons(Primitive):
        ...
    class updateWindow(Primitive):
        ...
    class updateXRef(Generic):
        ...
    class usedMaps(Primitive):
        ...
    class uvchecker_mtl(Standardmaterial):
        ...
    class uvwMappingHeightManip(helper):
        ...
    class uvwMappingLengthManip(helper):
        ...
    class uvwMappingPositionManip(helper):
        ...
    class uvwMappingWidthManip(helper):
        ...
    class validModifier(Primitive):
        ...
    class validateId(Primitive):
        ...
    class validateValueLinkages(Primitive):
        ...
    class value(Value):
        ...
    class velocity(RenderElement):
        enabled: bool
        filterOn: bool
        elementName: str
        bitmap: None
        velocityMax: float
        velocityOn: bool
        ...
    class videoPostTracks(MAXTVNode):
        ...
    class visualMS(Interface):
        ...
    class visualMSCA(Interface):
        ...
    class vptSetting(IObject):
        ...
    class walkThroughOps(Interface):
        ...
    class waves(textureMap):
        numWaveSets: int
        waveRadius: float
        waveLenMin: float
        waveLenMax: float
        Amplitude: float
        phase: float
        Distribution: int
        RandomSeed: int
        color1: MXSWrapperBase
        color2: MXSWrapperBase
        map1: None
        map2: None
        map1on: bool
        map2on: bool
        coords: MXSWrapperBase
        ...
    class weldSpline(Primitive):
        ...
    class white(Color):
        ...
    class write_cws_channel(MAXScriptFunction):
        ...
    class write_cws_cineonConverter(MAXScriptFunction):
        ...
    class write_cws_composite(MAXScriptFunction):
        ...
    class write_cws_composite_settings(MAXScriptFunction):
        ...
    class write_cws_connect(MAXScriptFunction):
        ...
    class write_cws_eof(MAXScriptFunction):
        ...
    class write_cws_footage(MAXScriptFunction):
        ...
    class write_cws_head(MAXScriptFunction):
        ...
    class write_cws_object(MAXScriptFunction):
        ...
    class write_cws_operator(MAXScriptFunction):
        ...
    class write_cws_parenting(MAXScriptFunction):
        ...
    class xView(GlobalUtilityPlugin):
        ...
    class xViewChecker(Interface):
        ...
    class x_axis(Point3):
        ...
    class y_axis(Point3):
        ...
    class yellow(Color):
        ...
    class yesNoCancelBox(Primitive):
        ...
    class z_axis(Point3):
        ...
def undo(onoff, label='MAXScript'): ...
