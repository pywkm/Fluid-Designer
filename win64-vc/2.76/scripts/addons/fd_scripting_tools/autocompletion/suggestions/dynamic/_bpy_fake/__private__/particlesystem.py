from . particlesystemmodifier import ParticleSystemModifier
from . particlesettings import ParticleSettings
from . struct import Struct
from . particle import Particle
from . childparticle import ChildParticle
from . scene import Scene
from . object import Object
from . pointcache import PointCache
from . particletarget import ParticleTarget
from . clothmodifier import ClothModifier
from . bpy_struct import bpy_struct
import mathutils

class ParticleSystem(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Particle system name'''
        return str()
    @property
    def settings(self):
        '''(ParticleSettings) Particle system settings'''
        return ParticleSettings()
    @property
    def particles(self):
        '''(Sequence of Particle) Particles generated by the particle system'''
        return (Particle(),)
    @property
    def child_particles(self):
        '''(Sequence of ChildParticle) Child particles generated by the particle
        system'''
        return (ChildParticle(),)
    @property
    def seed(self):
        '''(Integer) Offset in the random number table, to get a different
        randomized result'''
        return int()
    @property
    def child_seed(self):
        '''(Integer) Offset in the random number table for child particles, to
        get a different randomized result'''
        return int()
    @property
    def is_global_hair(self):
        '''(Boolean) Hair keys are in global coordinate space'''
        return bool()
    @property
    def use_hair_dynamics(self):
        '''(Boolean) Enable hair dynamics using cloth simulation'''
        return bool()
    @property
    def cloth(self):
        '''(ClothModifier) Cloth dynamics for hair'''
        return ClothModifier()
    @property
    def reactor_target_object(self):
        '''(Object) For reactor systems, the object that has the target particle
        system (empty if same object)'''
        return Object()
    @property
    def reactor_target_particle_system(self):
        '''(Integer) For reactor systems, index of particle system on the target
        object'''
        return int()
    @property
    def use_keyed_timing(self):
        '''(Boolean) Use key times'''
        return bool()
    @property
    def targets(self):
        '''(Sequence of ParticleTarget) Target particle systems'''
        return (ParticleTarget(),)
    @property
    def active_particle_target(self):
        '''(ParticleTarget)'''
        return ParticleTarget()
    @property
    def active_particle_target_index(self):
        '''(Integer)'''
        return int()
    @property
    def billboard_normal_uv(self):
        '''(String) UV map to control billboard normals'''
        return str()
    @property
    def billboard_time_index_uv(self):
        '''(String) UV map to control billboard time index (X-Y)'''
        return str()
    @property
    def billboard_split_uv(self):
        '''(String) UV map to control billboard splitting'''
        return str()
    @property
    def vertex_group_density(self):
        '''(String) Vertex group to control density'''
        return str()
    @property
    def invert_vertex_group_density(self):
        '''(Boolean) Negate the effect of the density vertex group'''
        return bool()
    @property
    def vertex_group_velocity(self):
        '''(String) Vertex group to control velocity'''
        return str()
    @property
    def invert_vertex_group_velocity(self):
        '''(Boolean) Negate the effect of the velocity vertex group'''
        return bool()
    @property
    def vertex_group_length(self):
        '''(String) Vertex group to control length'''
        return str()
    @property
    def invert_vertex_group_length(self):
        '''(Boolean) Negate the effect of the length vertex group'''
        return bool()
    @property
    def vertex_group_clump(self):
        '''(String) Vertex group to control clump'''
        return str()
    @property
    def invert_vertex_group_clump(self):
        '''(Boolean) Negate the effect of the clump vertex group'''
        return bool()
    @property
    def vertex_group_kink(self):
        '''(String) Vertex group to control kink'''
        return str()
    @property
    def invert_vertex_group_kink(self):
        '''(Boolean) Negate the effect of the kink vertex group'''
        return bool()
    @property
    def vertex_group_roughness_1(self):
        '''(String) Vertex group to control roughness 1'''
        return str()
    @property
    def invert_vertex_group_roughness_1(self):
        '''(Boolean) Negate the effect of the roughness 1 vertex group'''
        return bool()
    @property
    def vertex_group_roughness_2(self):
        '''(String) Vertex group to control roughness 2'''
        return str()
    @property
    def invert_vertex_group_roughness_2(self):
        '''(Boolean) Negate the effect of the roughness 2 vertex group'''
        return bool()
    @property
    def vertex_group_roughness_end(self):
        '''(String) Vertex group to control roughness end'''
        return str()
    @property
    def invert_vertex_group_roughness_end(self):
        '''(Boolean) Negate the effect of the roughness end vertex group'''
        return bool()
    @property
    def vertex_group_size(self):
        '''(String) Vertex group to control size'''
        return str()
    @property
    def invert_vertex_group_size(self):
        '''(Boolean) Negate the effect of the size vertex group'''
        return bool()
    @property
    def vertex_group_tangent(self):
        '''(String) Vertex group to control tangent'''
        return str()
    @property
    def invert_vertex_group_tangent(self):
        '''(Boolean) Negate the effect of the tangent vertex group'''
        return bool()
    @property
    def vertex_group_rotation(self):
        '''(String) Vertex group to control rotation'''
        return str()
    @property
    def invert_vertex_group_rotation(self):
        '''(Boolean) Negate the effect of the rotation vertex group'''
        return bool()
    @property
    def vertex_group_field(self):
        '''(String) Vertex group to control field'''
        return str()
    @property
    def invert_vertex_group_field(self):
        '''(Boolean) Negate the effect of the field vertex group'''
        return bool()
    @property
    def point_cache(self):
        '''(PointCache)'''
        return PointCache()
    @property
    def has_multiple_caches(self):
        '''(Boolean) Particle system has multiple point caches'''
        return bool()
    @property
    def parent(self):
        '''(Object) Use this object's coordinate system instead of global
        coordinate system'''
        return Object()
    @property
    def is_editable(self):
        '''(Boolean) Particle system can be edited in particle mode'''
        return bool()
    @property
    def is_edited(self):
        '''(Boolean) Particle system has been edited in particle mode'''
        return bool()
    @property
    def dt_frac(self):
        '''(Float) The current simulation time step size, as a fraction of a
        frame'''
        return float()
    def set_resolution(self, scene, object, resolution):
        '''Set the resolution to use for the number of particles
        
        Parameter:
          scene: (Scene) Scene
          object: (Object) Object
          resolution: (Enum) Resolution settings to apply'''
        return 
    def co_hair(self, object, particle_no, step):
        '''Obtain cache hair data
        
        Parameter:
          object: (Object) Object
          particle_no: (Integer)
          step: (Integer)
        
        Returns:
          co: (Vector 3D) Exported hairkey location'''
        return mathutils.Vector()
    def uv_on_emitter(self, modifier, particle, particle_no, uv_no):
        '''Obtain uv for all particles
        
        Parameter:
          modifier: (ParticleSystemModifier) Particle modifier
          particle: (Particle) Particle
          particle_no: (Integer)
          uv_no: (Integer)
        
        Returns:
          uv: (Vector 2D)'''
        return mathutils.Vector()
    def mcol_on_emitter(self, modifier, particle, particle_no, vcol_no):
        '''Obtain mcol for all particles
        
        Parameter:
          modifier: (ParticleSystemModifier) Particle modifier
          particle: (Particle) Particle
          particle_no: (Integer)
          vcol_no: (Integer)
        
        Returns:
          mcol: (Vector 3D)'''
        return mathutils.Vector()