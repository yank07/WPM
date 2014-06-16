--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: TipoItemApp_item; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "TipoItemApp_item" (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    tipoitem_fk_id integer NOT NULL
);


ALTER TABLE public."TipoItemApp_item" OWNER TO postgres;

--
-- Name: TipoItemApp_item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "TipoItemApp_item_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."TipoItemApp_item_id_seq" OWNER TO postgres;

--
-- Name: TipoItemApp_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "TipoItemApp_item_id_seq" OWNED BY "TipoItemApp_item".id;


--
-- Name: TipoItemApp_tipoitem; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "TipoItemApp_tipoitem" (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    descripcion character varying(50) NOT NULL,
    observacion character varying(50),
    fecha_creacion date NOT NULL,
    fecha_modificacion date NOT NULL
);


ALTER TABLE public."TipoItemApp_tipoitem" OWNER TO postgres;

--
-- Name: TipoItemApp_tipoitem_atributos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "TipoItemApp_tipoitem_atributos" (
    id integer NOT NULL,
    tipoitem_id integer NOT NULL,
    attribute_id integer NOT NULL
);


ALTER TABLE public."TipoItemApp_tipoitem_atributos" OWNER TO postgres;

--
-- Name: TipoItemApp_tipoitem_atributos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "TipoItemApp_tipoitem_atributos_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."TipoItemApp_tipoitem_atributos_id_seq" OWNER TO postgres;

--
-- Name: TipoItemApp_tipoitem_atributos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "TipoItemApp_tipoitem_atributos_id_seq" OWNED BY "TipoItemApp_tipoitem_atributos".id;


--
-- Name: TipoItemApp_tipoitem_fases; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "TipoItemApp_tipoitem_fases" (
    id integer NOT NULL,
    tipoitem_id integer NOT NULL,
    fase_id integer NOT NULL
);


ALTER TABLE public."TipoItemApp_tipoitem_fases" OWNER TO postgres;

--
-- Name: TipoItemApp_tipoitem_fases_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "TipoItemApp_tipoitem_fases_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."TipoItemApp_tipoitem_fases_id_seq" OWNER TO postgres;

--
-- Name: TipoItemApp_tipoitem_fases_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "TipoItemApp_tipoitem_fases_id_seq" OWNED BY "TipoItemApp_tipoitem_fases".id;


--
-- Name: TipoItemApp_tipoitem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "TipoItemApp_tipoitem_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."TipoItemApp_tipoitem_id_seq" OWNER TO postgres;

--
-- Name: TipoItemApp_tipoitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "TipoItemApp_tipoitem_id_seq" OWNED BY "TipoItemApp_tipoitem".id;


--
-- Name: TipoItemApp_valor; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "TipoItemApp_valor" (
    value_ptr_id integer NOT NULL,
    item_fk_id integer NOT NULL
);


ALTER TABLE public."TipoItemApp_valor" OWNER TO postgres;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: eav_attribute; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE eav_attribute (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    site_id integer NOT NULL,
    slug character varying(50) NOT NULL,
    description character varying(256),
    enum_group_id integer,
    type character varying(20),
    datatype character varying(6) NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    required boolean NOT NULL
);


ALTER TABLE public.eav_attribute OWNER TO postgres;

--
-- Name: eav_attribute_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE eav_attribute_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eav_attribute_id_seq OWNER TO postgres;

--
-- Name: eav_attribute_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE eav_attribute_id_seq OWNED BY eav_attribute.id;


--
-- Name: eav_enumgroup; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE eav_enumgroup (
    id integer NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE public.eav_enumgroup OWNER TO postgres;

--
-- Name: eav_enumgroup_enums; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE eav_enumgroup_enums (
    id integer NOT NULL,
    enumgroup_id integer NOT NULL,
    enumvalue_id integer NOT NULL
);


ALTER TABLE public.eav_enumgroup_enums OWNER TO postgres;

--
-- Name: eav_enumgroup_enums_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE eav_enumgroup_enums_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eav_enumgroup_enums_id_seq OWNER TO postgres;

--
-- Name: eav_enumgroup_enums_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE eav_enumgroup_enums_id_seq OWNED BY eav_enumgroup_enums.id;


--
-- Name: eav_enumgroup_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE eav_enumgroup_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eav_enumgroup_id_seq OWNER TO postgres;

--
-- Name: eav_enumgroup_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE eav_enumgroup_id_seq OWNED BY eav_enumgroup.id;


--
-- Name: eav_enumvalue; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE eav_enumvalue (
    id integer NOT NULL,
    value character varying(50) NOT NULL
);


ALTER TABLE public.eav_enumvalue OWNER TO postgres;

--
-- Name: eav_enumvalue_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE eav_enumvalue_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eav_enumvalue_id_seq OWNER TO postgres;

--
-- Name: eav_enumvalue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE eav_enumvalue_id_seq OWNED BY eav_enumvalue.id;


--
-- Name: eav_value; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE eav_value (
    id integer NOT NULL,
    entity_ct_id integer NOT NULL,
    entity_id integer NOT NULL,
    value_text text,
    value_float double precision,
    value_int integer,
    value_date timestamp with time zone,
    value_bool boolean,
    value_enum_id integer,
    generic_value_id integer,
    generic_value_ct_id integer,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    attribute_id integer NOT NULL
);


ALTER TABLE public.eav_value OWNER TO postgres;

--
-- Name: eav_value_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE eav_value_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eav_value_id_seq OWNER TO postgres;

--
-- Name: eav_value_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE eav_value_id_seq OWNED BY eav_value.id;


--
-- Name: item_historicalitem; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE item_historicalitem (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    tipoitem_id integer,
    fase_id integer,
    complejidad integer NOT NULL,
    costo integer NOT NULL,
    estado character varying(5) NOT NULL,
    descripcion character varying(50) NOT NULL,
    observacion character varying(50) NOT NULL,
    version integer NOT NULL,
    fecha_creacion date NOT NULL,
    fecha_modificacion date NOT NULL,
    archivo text NOT NULL,
    rango_valor_inicio integer NOT NULL,
    rango_valor_final integer NOT NULL,
    history_id integer NOT NULL,
    history_date timestamp with time zone NOT NULL,
    history_user_id integer,
    history_type character varying(1) NOT NULL
);


ALTER TABLE public.item_historicalitem OWNER TO postgres;

--
-- Name: item_historicalitem_history_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE item_historicalitem_history_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.item_historicalitem_history_id_seq OWNER TO postgres;

--
-- Name: item_historicalitem_history_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE item_historicalitem_history_id_seq OWNED BY item_historicalitem.history_id;


--
-- Name: item_item; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE item_item (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    tipoitem_id integer NOT NULL,
    fase_id integer NOT NULL,
    complejidad integer NOT NULL,
    costo integer NOT NULL,
    estado character varying(5) NOT NULL,
    descripcion character varying(50) NOT NULL,
    observacion character varying(50) NOT NULL,
    version integer NOT NULL,
    fecha_creacion date NOT NULL,
    fecha_modificacion date NOT NULL,
    archivo character varying(100) NOT NULL,
    rango_valor_inicio integer NOT NULL,
    rango_valor_final integer NOT NULL
);


ALTER TABLE public.item_item OWNER TO postgres;

--
-- Name: item_item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE item_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.item_item_id_seq OWNER TO postgres;

--
-- Name: item_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE item_item_id_seq OWNED BY item_item.id;


--
-- Name: item_relaciones; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE item_relaciones (
    id integer NOT NULL,
    tipo_relacion character varying(3) NOT NULL,
    item_origen_id integer NOT NULL,
    item_destino_id integer NOT NULL,
    activo boolean NOT NULL,
    item_origen_version integer NOT NULL,
    item_destino_version integer NOT NULL
);


ALTER TABLE public.item_relaciones OWNER TO postgres;

--
-- Name: item_relaciones_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE item_relaciones_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.item_relaciones_id_seq OWNER TO postgres;

--
-- Name: item_relaciones_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE item_relaciones_id_seq OWNED BY item_relaciones.id;


--
-- Name: lineaBase_lineabase; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "lineaBase_lineabase" (
    id integer NOT NULL,
    descripcion character varying(50) NOT NULL,
    estado character varying(20) NOT NULL,
    fase_id integer
);


ALTER TABLE public."lineaBase_lineabase" OWNER TO postgres;

--
-- Name: lineaBase_lineabase_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "lineaBase_lineabase_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."lineaBase_lineabase_id_seq" OWNER TO postgres;

--
-- Name: lineaBase_lineabase_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "lineaBase_lineabase_id_seq" OWNED BY "lineaBase_lineabase".id;


--
-- Name: lineaBase_lineabase_items; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "lineaBase_lineabase_items" (
    id integer NOT NULL,
    lineabase_id integer NOT NULL,
    item_id integer NOT NULL
);


ALTER TABLE public."lineaBase_lineabase_items" OWNER TO postgres;

--
-- Name: lineaBase_lineabase_items_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "lineaBase_lineabase_items_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."lineaBase_lineabase_items_id_seq" OWNER TO postgres;

--
-- Name: lineaBase_lineabase_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "lineaBase_lineabase_items_id_seq" OWNED BY "lineaBase_lineabase_items".id;


--
-- Name: principal_estadosproyecto; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE principal_estadosproyecto (
    id integer NOT NULL,
    descripcion character varying(50) NOT NULL
);


ALTER TABLE public.principal_estadosproyecto OWNER TO postgres;

--
-- Name: principal_estadosproyecto_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE principal_estadosproyecto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.principal_estadosproyecto_id_seq OWNER TO postgres;

--
-- Name: principal_estadosproyecto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE principal_estadosproyecto_id_seq OWNED BY principal_estadosproyecto.id;


--
-- Name: principal_fase; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE principal_fase (
    id integer NOT NULL,
    proyecto_id integer NOT NULL,
    nombre character varying(50) NOT NULL
);


ALTER TABLE public.principal_fase OWNER TO postgres;

--
-- Name: principal_fase_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE principal_fase_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.principal_fase_id_seq OWNER TO postgres;

--
-- Name: principal_fase_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE principal_fase_id_seq OWNED BY principal_fase.id;


--
-- Name: principal_proyecto; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE principal_proyecto (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    presupuesto integer NOT NULL,
    observaciones text NOT NULL,
    estado_id integer
);


ALTER TABLE public.principal_proyecto OWNER TO postgres;

--
-- Name: principal_proyecto_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE principal_proyecto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.principal_proyecto_id_seq OWNER TO postgres;

--
-- Name: principal_proyecto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE principal_proyecto_id_seq OWNED BY principal_proyecto.id;


--
-- Name: principal_userprofile; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE principal_userprofile (
    id integer NOT NULL,
    user_id integer NOT NULL,
    direccion character varying(50) NOT NULL,
    telefono character varying(15) NOT NULL,
    activo boolean NOT NULL
);


ALTER TABLE public.principal_userprofile OWNER TO postgres;

--
-- Name: principal_userprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE principal_userprofile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.principal_userprofile_id_seq OWNER TO postgres;

--
-- Name: principal_userprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE principal_userprofile_id_seq OWNED BY principal_userprofile.id;


--
-- Name: proyecto_fase; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE proyecto_fase (
    id integer NOT NULL,
    proyecto_id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    fecha_creacion date NOT NULL,
    fecha_modificacion date NOT NULL,
    usuario_modificacion_id integer NOT NULL,
    estado character varying(50) NOT NULL
);


ALTER TABLE public.proyecto_fase OWNER TO postgres;

--
-- Name: proyecto_fase_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE proyecto_fase_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.proyecto_fase_id_seq OWNER TO postgres;

--
-- Name: proyecto_fase_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE proyecto_fase_id_seq OWNED BY proyecto_fase.id;


--
-- Name: proyecto_proyecto; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE proyecto_proyecto (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    presupuesto integer NOT NULL,
    observaciones text NOT NULL,
    estado character varying(50) NOT NULL,
    numero_fases integer NOT NULL,
    fecha_creacion date NOT NULL,
    fecha_modificacion date NOT NULL,
    usuario_modificacion_id integer NOT NULL,
    imagen_grafo character varying(100) NOT NULL,
    CONSTRAINT ck_numero_fases_pstv_341b56c02b598285 CHECK ((numero_fases >= 0))
);


ALTER TABLE public.proyecto_proyecto OWNER TO postgres;

--
-- Name: proyecto_proyecto_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE proyecto_proyecto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.proyecto_proyecto_id_seq OWNER TO postgres;

--
-- Name: proyecto_proyecto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE proyecto_proyecto_id_seq OWNED BY proyecto_proyecto.id;


--
-- Name: proyecto_proyecto_miembros; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE proyecto_proyecto_miembros (
    id integer NOT NULL,
    proyecto_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.proyecto_proyecto_miembros OWNER TO postgres;

--
-- Name: proyecto_proyecto_miembros_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE proyecto_proyecto_miembros_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.proyecto_proyecto_miembros_id_seq OWNER TO postgres;

--
-- Name: proyecto_proyecto_miembros_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE proyecto_proyecto_miembros_id_seq OWNED BY proyecto_proyecto_miembros.id;


--
-- Name: solicitudCambio_comite; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "solicitudCambio_comite" (
    id integer NOT NULL,
    primer_integrante_id integer NOT NULL,
    segundo_integrante_id integer NOT NULL,
    tercer_integrante_id integer NOT NULL,
    estado character varying(3) NOT NULL,
    proyecto_id integer NOT NULL
);


ALTER TABLE public."solicitudCambio_comite" OWNER TO postgres;

--
-- Name: solicitudCambio_comite_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "solicitudCambio_comite_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."solicitudCambio_comite_id_seq" OWNER TO postgres;

--
-- Name: solicitudCambio_comite_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "solicitudCambio_comite_id_seq" OWNED BY "solicitudCambio_comite".id;


--
-- Name: solicitudCambio_solicitud; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "solicitudCambio_solicitud" (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    item_id integer NOT NULL,
    fecha_caducar date NOT NULL,
    motivo text NOT NULL,
    impacto integer NOT NULL,
    estado character varying(3) NOT NULL,
    voto_primero integer NOT NULL,
    voto_segundo integer NOT NULL,
    voto_tercero integer NOT NULL,
    conteo integer NOT NULL,
    resultado integer NOT NULL
);


ALTER TABLE public."solicitudCambio_solicitud" OWNER TO postgres;

--
-- Name: solicitudCambio_solicitud_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "solicitudCambio_solicitud_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."solicitudCambio_solicitud_id_seq" OWNER TO postgres;

--
-- Name: solicitudCambio_solicitud_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "solicitudCambio_solicitud_id_seq" OWNED BY "solicitudCambio_solicitud".id;


--
-- Name: south_migrationhistory; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE south_migrationhistory (
    id integer NOT NULL,
    app_name character varying(255) NOT NULL,
    migration character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.south_migrationhistory OWNER TO postgres;

--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE south_migrationhistory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.south_migrationhistory_id_seq OWNER TO postgres;

--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE south_migrationhistory_id_seq OWNED BY south_migrationhistory.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "TipoItemApp_item" ALTER COLUMN id SET DEFAULT nextval('"TipoItemApp_item_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "TipoItemApp_tipoitem" ALTER COLUMN id SET DEFAULT nextval('"TipoItemApp_tipoitem_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "TipoItemApp_tipoitem_atributos" ALTER COLUMN id SET DEFAULT nextval('"TipoItemApp_tipoitem_atributos_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "TipoItemApp_tipoitem_fases" ALTER COLUMN id SET DEFAULT nextval('"TipoItemApp_tipoitem_fases_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY eav_attribute ALTER COLUMN id SET DEFAULT nextval('eav_attribute_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY eav_enumgroup ALTER COLUMN id SET DEFAULT nextval('eav_enumgroup_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY eav_enumgroup_enums ALTER COLUMN id SET DEFAULT nextval('eav_enumgroup_enums_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY eav_enumvalue ALTER COLUMN id SET DEFAULT nextval('eav_enumvalue_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY eav_value ALTER COLUMN id SET DEFAULT nextval('eav_value_id_seq'::regclass);


--
-- Name: history_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY item_historicalitem ALTER COLUMN history_id SET DEFAULT nextval('item_historicalitem_history_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY item_item ALTER COLUMN id SET DEFAULT nextval('item_item_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY item_relaciones ALTER COLUMN id SET DEFAULT nextval('item_relaciones_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "lineaBase_lineabase" ALTER COLUMN id SET DEFAULT nextval('"lineaBase_lineabase_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "lineaBase_lineabase_items" ALTER COLUMN id SET DEFAULT nextval('"lineaBase_lineabase_items_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY principal_estadosproyecto ALTER COLUMN id SET DEFAULT nextval('principal_estadosproyecto_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY principal_fase ALTER COLUMN id SET DEFAULT nextval('principal_fase_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY principal_proyecto ALTER COLUMN id SET DEFAULT nextval('principal_proyecto_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY principal_userprofile ALTER COLUMN id SET DEFAULT nextval('principal_userprofile_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY proyecto_fase ALTER COLUMN id SET DEFAULT nextval('proyecto_fase_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY proyecto_proyecto ALTER COLUMN id SET DEFAULT nextval('proyecto_proyecto_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY proyecto_proyecto_miembros ALTER COLUMN id SET DEFAULT nextval('proyecto_proyecto_miembros_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "solicitudCambio_comite" ALTER COLUMN id SET DEFAULT nextval('"solicitudCambio_comite_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "solicitudCambio_solicitud" ALTER COLUMN id SET DEFAULT nextval('"solicitudCambio_solicitud_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY south_migrationhistory ALTER COLUMN id SET DEFAULT nextval('south_migrationhistory_id_seq'::regclass);


--
-- Data for Name: TipoItemApp_item; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "TipoItemApp_item" (id, nombre, tipoitem_fk_id) FROM stdin;
\.


--
-- Name: TipoItemApp_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"TipoItemApp_item_id_seq"', 1, false);


--
-- Name: TipoItemApp_tipoitem_atributos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"TipoItemApp_tipoitem_atributos_id_seq"', 36, true);



--
-- Name: TipoItemApp_tipoitem_fases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"TipoItemApp_tipoitem_fases_id_seq"', 19, true);


--
-- Name: TipoItemApp_tipoitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"TipoItemApp_tipoitem_id_seq"', 7, true);

--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
3	project_leader
11	desarrollador
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 11, true);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
104	3	73
105	3	74
106	3	75
107	3	55
108	3	56
109	3	57
110	3	58
111	3	59
112	3	60
113	3	61
114	3	62
115	3	63
141	11	49
142	11	50
143	11	51
144	11	52
145	11	53
146	11	54
147	11	64
148	11	65
149	11	66
150	11	67
151	11	68
152	11	69
153	11	73
154	11	74
155	11	75
156	11	76
157	11	77
158	11	78
159	11	79
160	11	80
161	11	81
162	11	82
163	11	83
164	11	84
165	11	85
166	11	86
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 166, true);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add user profile	7	add_userprofile
20	Can change user profile	7	change_userprofile
21	Can delete user profile	7	delete_userprofile
86	aprobar_item	22	aprobar_item
87	Can add solicitud	26	add_solicitud
88	Can change solicitud	26	change_solicitud
89	Can delete solicitud	26	delete_solicitud
90	Can add comite	27	add_comite
91	Can change comite	27	change_comite
92	Can delete comite	27	delete_comite
31	Can add migration history	11	add_migrationhistory
32	Can change migration history	11	change_migrationhistory
33	Can delete migration history	11	delete_migrationhistory
34	Can add site	12	add_site
35	Can change site	12	change_site
36	Can delete site	12	delete_site
37	Can add proyecto	13	add_proyecto
38	Can change proyecto	13	change_proyecto
39	Can delete proyecto	13	delete_proyecto
40	Can add fase	14	add_fase
41	Can change fase	14	change_fase
42	Can delete fase	14	delete_fase
43	Can add enum value	15	add_enumvalue
44	Can change enum value	15	change_enumvalue
45	Can delete enum value	15	delete_enumvalue
46	Can add enum group	16	add_enumgroup
47	Can change enum group	16	change_enumgroup
48	Can delete enum group	16	delete_enumgroup
49	Can add attribute	17	add_attribute
50	Can change attribute	17	change_attribute
51	Can delete attribute	17	delete_attribute
52	Can add value	18	add_value
53	Can change value	18	change_value
54	Can delete value	18	delete_value
55	Can add tipo item	19	add_tipoitem
56	Can change tipo item	19	change_tipoitem
57	Can delete tipo item	19	delete_tipoitem
58	Can add item	20	add_item
59	Can change item	20	change_item
60	Can delete item	20	delete_item
61	Can add valor	21	add_valor
62	Can change valor	21	change_valor
63	Can delete valor	21	delete_valor
64	Can add item	22	add_item
65	Can change item	22	change_item
66	Can delete item	22	delete_item
67	Can add relaciones	23	add_relaciones
68	Can change relaciones	23	change_relaciones
69	Can delete relaciones	23	delete_relaciones
70	Can add historical item	24	add_historicalitem
71	Can change historical item	24	change_historicalitem
72	Can delete historical item	24	delete_historicalitem
73	Can add linea base	25	add_lineabase
74	Can change linea base	25	change_lineabase
75	Can delete linea base	25	delete_lineabase
76	asignar_valor_item	22	asignar_valor_item
77	listar_item	22	listar_item
78	edit_item	22	edit_item
79	listar_item_muerto	22	listar_item_muerto
80	revivir_item	22	revivir_item
81	crear_sucesor	22	crear_sucesor
82	crear_hijo	22	crear_hijo
83	listar_versiones	22	listar_versiones
84	revertir_item	22	revertir_item
85	activar_item	22	activar_item
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 92, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
4	pbkdf2_sha256$12000$rhqaXwNWzfWM$iOp850RRok2zYn417xuTm/FSo0VHBmU1gr8rJJsOu24=	2014-04-11 17:49:24.55173-04	f	user1				f	t	2014-04-11 17:49:24.551824-04
7	pbkdf2_sha256$12000$VcPmjqL2ogHm$2HDFS4r0riH8lIxXzDITd0F5k3BVocPmtwW5U9wUZUM=	2014-06-16 12:19:59.735711-04	f	lauri	Lauri	lauri	lauri@localhost	f	t	2014-04-12 09:03:49.71836-04
6	pbkdf2_sha256$12000$XXqDn77Q4CJX$0Qjur1GckZbMmxztQu4ff2eHAT8ynj+Oo612hlPBAR0=	2014-06-16 13:21:47.673272-04	f	cscg646				f	t	2014-04-12 08:19:49.47841-04
2	pbkdf2_sha256$12000$wwrF2f6D48CV$f3vYfaAq1FhzbVeGDZ5QLygfAmQ/tdojTk1XZk7pjdY=	2014-06-16 13:41:02.853399-04	f	ccaballero	Cristhian	Caballero	ccaballero@localhost	f	t	2014-04-11 11:11:00.190428-04
1	pbkdf2_sha256$12000$LjIK66kpkWj2$N9HzkETcBLdpBAfGp5bxlNG3h5cfDMVVFznBN7MVP4g=	2014-06-16 15:20:18.245145-04	t	super			super@localhost	t	t	2014-04-09 17:23:20.625801-04
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
34	2	11
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 34, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_id_seq', 7, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
1	2014-04-23 21:28:41.320871-04	1	4	1	super	2	Modificado/a password.
2	2014-05-07 07:57:09.237591-04	1	4	1	super	2	Modificado/a password.
3	2014-06-06 17:53:55.300493-04	1	4	5	abcd	3	
4	2014-06-06 17:54:06.552115-04	1	4	3	user	3	
5	2014-06-06 17:54:24.857755-04	1	4	6	cscg646	3	
6	2014-06-06 17:54:24.916696-04	1	4	4	user1	3	
7	2014-06-06 17:54:41.200325-04	1	4	4	user1	3	
8	2014-06-06 17:55:10.963367-04	1	4	1	super	2	Modificado/a password.
9	2014-06-06 17:55:27.019758-04	1	4	1	super	2	Modificado/a password.
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 9, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	log entry	admin	logentry
2	permission	auth	permission
3	group	auth	group
4	user	auth	user
5	content type	contenttypes	contenttype
6	session	sessions	session
7	user profile	principal	userprofile
11	migration history	south	migrationhistory
12	site	sites	site
13	proyecto	proyecto	proyecto
14	fase	proyecto	fase
15	enum value	eav	enumvalue
16	enum group	eav	enumgroup
17	attribute	eav	attribute
18	value	eav	value
19	tipo item	TipoItemApp	tipoitem
20	item	TipoItemApp	item
21	valor	TipoItemApp	valor
22	item	item	item
23	relaciones	item	relaciones
24	historical item	item	historicalitem
25	linea base	lineaBase	lineabase
26	solicitud	solicitudCambio	solicitud
27	comite	solicitudCambio	comite
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 27, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
d0syvz1ve0h9n3w1ecgtw5maba0dm2bh	YTc2OThjYmNmNjA0MzBjZDhkYTE3MzFkODlhOWEwZDMwMDFjNjM5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-06-14 19:01:48.423926-04
hfnmsdq38skwlbzyq7ahqsmxjv80sdu3	YTc2OThjYmNmNjA0MzBjZDhkYTE3MzFkODlhOWEwZDMwMDFjNjM5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-06-26 16:20:09.542618-04
6644a55x32a9qx9ixbj3wj74y6mriow6	YTc2OThjYmNmNjA0MzBjZDhkYTE3MzFkODlhOWEwZDMwMDFjNjM5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-05-14 17:16:46.193784-04
ecs3knwy27pd7u99tmsse4prhy5zhit3	NjA3YTA0ZjQzN2NkM2ZkNzE0YzAyYzNiZGVkY2NlMjVhMWViMmQwZDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=	2014-05-14 17:17:02.715855-04
33y3s92ljz2s0u1z5yvphhu1hvh02s9l	YTc2OThjYmNmNjA0MzBjZDhkYTE3MzFkODlhOWEwZDMwMDFjNjM5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-05-31 09:25:41.598831-04
les353y173nnu2jlggjefc9jmrnsnyyy	NGZkNWVhZGRhMWY1NDVmZmIwNmI2ZjJiMDZhM2RkMzgzNTUzMjQ1MDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6N30=	2014-05-31 09:25:49.377139-04
bwvdi6ys3au8wbi9nlmz5tecbvni6db3	YTc2OThjYmNmNjA0MzBjZDhkYTE3MzFkODlhOWEwZDMwMDFjNjM5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-06-20 17:57:31.326504-04
77hb186dt684tzzfo5gt3375tow1msnd	YzcyZDc1YTg2OWM0ZmQxOTg0OTdjNWE1YTc1OWFlZmE5NTBlOWNmNTp7fQ==	2014-06-21 08:09:39.594848-04
eteeh6rhkjnvoj1eqkamwdy4nq1cb9zw	NjA3YTA0ZjQzN2NkM2ZkNzE0YzAyYzNiZGVkY2NlMjVhMWViMmQwZDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=	2014-06-30 15:20:18.376517-04
h8colfuwwpwu8tu175omtxx0z08eq4ul	YTc2OThjYmNmNjA0MzBjZDhkYTE3MzFkODlhOWEwZDMwMDFjNjM5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-06-21 08:09:55.694305-04
l95pxqu6clf9zka9f0eqo1hkoo63zz7b	YTc2OThjYmNmNjA0MzBjZDhkYTE3MzFkODlhOWEwZDMwMDFjNjM5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-06-21 08:11:19.284854-04
97kh3m1wh5lwj7oif1q40csmo2c6xgzp	YzcyZDc1YTg2OWM0ZmQxOTg0OTdjNWE1YTc1OWFlZmE5NTBlOWNmNTp7fQ==	2014-06-25 19:03:25.630983-04
hvj5rttqtwqbv8tzzjzz4iyu1bz98kzc	YTc2OThjYmNmNjA0MzBjZDhkYTE3MzFkODlhOWEwZDMwMDFjNjM5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-06-25 19:03:41.802914-04
i1j213exeobx4iv3inukgepg0eorvypm	YTc2OThjYmNmNjA0MzBjZDhkYTE3MzFkODlhOWEwZDMwMDFjNjM5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-06-25 19:21:20.290029-04
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);



--
-- Name: eav_attribute_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('eav_attribute_id_seq', 8, true);


--
-- Data for Name: eav_enumgroup; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY eav_enumgroup (id, name) FROM stdin;
\.


--
-- Data for Name: eav_enumgroup_enums; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY eav_enumgroup_enums (id, enumgroup_id, enumvalue_id) FROM stdin;
\.


--
-- Name: eav_enumgroup_enums_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('eav_enumgroup_enums_id_seq', 1, false);


--
-- Name: eav_enumgroup_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('eav_enumgroup_id_seq', 1, false);


--
-- Data for Name: eav_enumvalue; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY eav_enumvalue (id, value) FROM stdin;
\.


--
-- Name: eav_enumvalue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('eav_enumvalue_id_seq', 1, false);


--
-- Name: eav_value_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('eav_value_id_seq', 12, true);




--
-- Name: item_historicalitem_history_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('item_historicalitem_history_id_seq', 135, true);



--
-- Name: item_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('item_item_id_seq', 27, true);



--
-- Name: item_relaciones_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('item_relaciones_id_seq', 17, true);



--
-- Name: lineaBase_lineabase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"lineaBase_lineabase_id_seq"', 17, true);



--
-- Name: lineaBase_lineabase_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"lineaBase_lineabase_items_id_seq"', 24, true);


-- Name: principal_estadosproyecto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('principal_estadosproyecto_id_seq', 1, true);


--
-- Data for Name: principal_fase; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY principal_fase (id, proyecto_id, nombre) FROM stdin;
\.


--
-- Name: principal_fase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('principal_fase_id_seq', 1, false);


--
-- Data for Name: principal_proyecto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY principal_proyecto (id, usuario_id, nombre, presupuesto, observaciones, estado_id) FROM stdin;
1	1	asd	123	asd	\N
2	1	asd	123	asd	\N
3	1	asd	123	asd	\N
4	4	prot1	1000	ninguna	\N
5	7	prueba1	10000	ninmguna	\N
\.


--
-- Name: principal_proyecto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('principal_proyecto_id_seq', 5, true);


--
-- Data for Name: principal_userprofile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY principal_userprofile (id, user_id, direccion, telefono, activo) FROM stdin;
1	1			t
3	4	asdo	1231241	t
5	6	efs	edrgd	t
2	2	no se	0123	t
6	7	asdasd	asdadasda	t
\.


--
-- Name: principal_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('principal_userprofile_id_seq', 7, true);



--
-- Name: proyecto_fase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('proyecto_fase_id_seq', 50, true);

--
-- Name: proyecto_proyecto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('proyecto_proyecto_id_seq', 24, true);



--
-- Name: proyecto_proyecto_miembros_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('proyecto_proyecto_miembros_id_seq', 22, true);



--
-- Name: solicitudCambio_comite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"solicitudCambio_comite_id_seq"', 2, true);



--
-- Name: solicitudCambio_solicitud_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"solicitudCambio_solicitud_id_seq"', 10, true);


--
-- Data for Name: south_migrationhistory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY south_migrationhistory (id, app_name, migration, applied) FROM stdin;
2	proyecto	0001_initial	2014-04-23 20:59:24.768894-04
4	proyecto	0002_auto	2014-04-23 21:03:51.349709-04
5	proyecto	0003_auto__add_field_proyecto_fecha_creacion__add_field_proyecto_fecha_modi	2014-04-26 16:57:58.338923-04
6	TipoItemApp	0001_initial	2014-04-26 17:29:11.368345-04
7	proyecto	0004_auto__add_field_proyecto_usuario_modificacion__add_field_fase_usuario_	2014-04-26 17:45:28.347313-04
8	proyecto	0005_auto__chg_field_proyecto_usuario_modificacion	2014-04-28 15:40:45.723314-04
9	proyecto	0006_auto__chg_field_proyecto_usuario_modificacion	2014-04-28 15:43:26.472167-04
10	proyecto	0007_auto	2014-04-30 17:21:04.323899-04
11	proyecto	0008_auto	2014-04-30 17:21:28.395699-04
12	item	0001_initial	2014-05-06 16:30:02.862984-04
13	item	0002_auto__del_unique_relaciones_item_origen_item_destino__add_unique_relac	2014-05-14 12:48:47.486677-04
14	proyecto	0009_auto__add_field_fase_estado	2014-05-16 16:41:46.902487-04
15	solicitudCambio	0001_initial	2014-05-21 17:07:33.218941-04
16	solicitudCambio	0002_auto__add_field_solicitud_estado__add_field_comite_proyecto	2014-05-22 17:35:03.800497-04
17	solicitudCambio	0003_auto__del_field_solicitud_votos__add_field_solicitud_voto_primero__add	2014-05-23 17:01:42.664449-04
18	solicitudCambio	0004_auto__add_field_solicitud_conteo	2014-05-23 17:29:12.276724-04
19	solicitudCambio	0005_auto__add_field_solicitud_resultado	2014-05-23 17:35:50.533722-04
20	proyecto	0010_auto__add_field_proyecto_imagen_grafo	2014-06-03 19:14:18.679755-04
21	proyecto	0011_auto__chg_field_proyecto_numero_fases	2014-06-16 15:20:02.239956-04
\.


--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('south_migrationhistory_id_seq', 21, true);


--
-- Name: TipoItemApp_item_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "TipoItemApp_item"
    ADD CONSTRAINT "TipoItemApp_item_pkey" PRIMARY KEY (id);


--
-- Name: TipoItemApp_tipoitem_atributo_tipoitem_id_66defda190f28ee2_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "TipoItemApp_tipoitem_atributos"
    ADD CONSTRAINT "TipoItemApp_tipoitem_atributo_tipoitem_id_66defda190f28ee2_uniq" UNIQUE (tipoitem_id, attribute_id);


--
-- Name: TipoItemApp_tipoitem_atributos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "TipoItemApp_tipoitem_atributos"
    ADD CONSTRAINT "TipoItemApp_tipoitem_atributos_pkey" PRIMARY KEY (id);


--
-- Name: TipoItemApp_tipoitem_fases_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "TipoItemApp_tipoitem_fases"
    ADD CONSTRAINT "TipoItemApp_tipoitem_fases_pkey" PRIMARY KEY (id);


--
-- Name: TipoItemApp_tipoitem_fases_tipoitem_id_7d1c65184d3515f1_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "TipoItemApp_tipoitem_fases"
    ADD CONSTRAINT "TipoItemApp_tipoitem_fases_tipoitem_id_7d1c65184d3515f1_uniq" UNIQUE (tipoitem_id, fase_id);


--
-- Name: TipoItemApp_tipoitem_nombre_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "TipoItemApp_tipoitem"
    ADD CONSTRAINT "TipoItemApp_tipoitem_nombre_key" UNIQUE (nombre);


--
-- Name: TipoItemApp_tipoitem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "TipoItemApp_tipoitem"
    ADD CONSTRAINT "TipoItemApp_tipoitem_pkey" PRIMARY KEY (id);


--
-- Name: TipoItemApp_valor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "TipoItemApp_valor"
    ADD CONSTRAINT "TipoItemApp_valor_pkey" PRIMARY KEY (value_ptr_id);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: eav_attribute_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY eav_attribute
    ADD CONSTRAINT eav_attribute_pkey PRIMARY KEY (id);


--
-- Name: eav_attribute_site_id_slug_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY eav_attribute
    ADD CONSTRAINT eav_attribute_site_id_slug_key UNIQUE (site_id, slug);


--
-- Name: eav_enumgroup_enums_enumgroup_id_enumvalue_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY eav_enumgroup_enums
    ADD CONSTRAINT eav_enumgroup_enums_enumgroup_id_enumvalue_id_key UNIQUE (enumgroup_id, enumvalue_id);


--
-- Name: eav_enumgroup_enums_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY eav_enumgroup_enums
    ADD CONSTRAINT eav_enumgroup_enums_pkey PRIMARY KEY (id);


--
-- Name: eav_enumgroup_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY eav_enumgroup
    ADD CONSTRAINT eav_enumgroup_name_key UNIQUE (name);


--
-- Name: eav_enumgroup_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY eav_enumgroup
    ADD CONSTRAINT eav_enumgroup_pkey PRIMARY KEY (id);


--
-- Name: eav_enumvalue_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY eav_enumvalue
    ADD CONSTRAINT eav_enumvalue_pkey PRIMARY KEY (id);


--
-- Name: eav_enumvalue_value_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY eav_enumvalue
    ADD CONSTRAINT eav_enumvalue_value_key UNIQUE (value);


--
-- Name: eav_value_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY eav_value
    ADD CONSTRAINT eav_value_pkey PRIMARY KEY (id);


--
-- Name: item_historicalitem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY item_historicalitem
    ADD CONSTRAINT item_historicalitem_pkey PRIMARY KEY (history_id);


--
-- Name: item_item_nombre_bde299053f75254_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY item_item
    ADD CONSTRAINT item_item_nombre_bde299053f75254_uniq UNIQUE (nombre, version);


--
-- Name: item_item_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY item_item
    ADD CONSTRAINT item_item_pkey PRIMARY KEY (id);


--
-- Name: item_relaciones_item_origen_id_14c378ac791a11f4_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY item_relaciones
    ADD CONSTRAINT item_relaciones_item_origen_id_14c378ac791a11f4_uniq UNIQUE (item_origen_id, item_destino_id, item_destino_version, item_origen_version);


--
-- Name: item_relaciones_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY item_relaciones
    ADD CONSTRAINT item_relaciones_pkey PRIMARY KEY (id);


--
-- Name: lineaBase_lineabase_items_lineabase_id_item_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "lineaBase_lineabase_items"
    ADD CONSTRAINT "lineaBase_lineabase_items_lineabase_id_item_id_key" UNIQUE (lineabase_id, item_id);


--
-- Name: lineaBase_lineabase_items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "lineaBase_lineabase_items"
    ADD CONSTRAINT "lineaBase_lineabase_items_pkey" PRIMARY KEY (id);


--
-- Name: lineaBase_lineabase_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "lineaBase_lineabase"
    ADD CONSTRAINT "lineaBase_lineabase_pkey" PRIMARY KEY (id);


--
-- Name: principal_estadosproyecto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY principal_estadosproyecto
    ADD CONSTRAINT principal_estadosproyecto_pkey PRIMARY KEY (id);


--
-- Name: principal_fase_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY principal_fase
    ADD CONSTRAINT principal_fase_pkey PRIMARY KEY (id);


--
-- Name: principal_proyecto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY principal_proyecto
    ADD CONSTRAINT principal_proyecto_pkey PRIMARY KEY (id);


--
-- Name: principal_userprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY principal_userprofile
    ADD CONSTRAINT principal_userprofile_pkey PRIMARY KEY (id);


--
-- Name: principal_userprofile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY principal_userprofile
    ADD CONSTRAINT principal_userprofile_user_id_key UNIQUE (user_id);


--
-- Name: proyecto_fase_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY proyecto_fase
    ADD CONSTRAINT proyecto_fase_pkey PRIMARY KEY (id);


--
-- Name: proyecto_proyecto_miembros_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY proyecto_proyecto_miembros
    ADD CONSTRAINT proyecto_proyecto_miembros_pkey PRIMARY KEY (id);


--
-- Name: proyecto_proyecto_miembros_proyecto_id_3c307a7de0d74826_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY proyecto_proyecto_miembros
    ADD CONSTRAINT proyecto_proyecto_miembros_proyecto_id_3c307a7de0d74826_uniq UNIQUE (proyecto_id, user_id);


--
-- Name: proyecto_proyecto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY proyecto_proyecto
    ADD CONSTRAINT proyecto_proyecto_pkey PRIMARY KEY (id);


--
-- Name: solicitudCambio_comite_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "solicitudCambio_comite"
    ADD CONSTRAINT "solicitudCambio_comite_pkey" PRIMARY KEY (id);


--
-- Name: solicitudCambio_solicitud_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "solicitudCambio_solicitud"
    ADD CONSTRAINT "solicitudCambio_solicitud_pkey" PRIMARY KEY (id);


--
-- Name: south_migrationhistory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY south_migrationhistory
    ADD CONSTRAINT south_migrationhistory_pkey PRIMARY KEY (id);


--
-- Name: TipoItemApp_item_tipoitem_fk_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "TipoItemApp_item_tipoitem_fk_id" ON "TipoItemApp_item" USING btree (tipoitem_fk_id);


--
-- Name: TipoItemApp_tipoitem_atributos_attribute_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "TipoItemApp_tipoitem_atributos_attribute_id" ON "TipoItemApp_tipoitem_atributos" USING btree (attribute_id);


--
-- Name: TipoItemApp_tipoitem_atributos_tipoitem_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "TipoItemApp_tipoitem_atributos_tipoitem_id" ON "TipoItemApp_tipoitem_atributos" USING btree (tipoitem_id);


--
-- Name: TipoItemApp_tipoitem_fases_fase_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "TipoItemApp_tipoitem_fases_fase_id" ON "TipoItemApp_tipoitem_fases" USING btree (fase_id);


--
-- Name: TipoItemApp_tipoitem_fases_tipoitem_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "TipoItemApp_tipoitem_fases_tipoitem_id" ON "TipoItemApp_tipoitem_fases" USING btree (tipoitem_id);


--
-- Name: TipoItemApp_tipoitem_nombre_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "TipoItemApp_tipoitem_nombre_like" ON "TipoItemApp_tipoitem" USING btree (nombre varchar_pattern_ops);


--
-- Name: TipoItemApp_valor_item_fk_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "TipoItemApp_valor_item_fk_id" ON "TipoItemApp_valor" USING btree (item_fk_id);


--
-- Name: auth_group_name_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_name_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_username_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_session_key_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: eav_attribute_enum_group_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX eav_attribute_enum_group_id ON eav_attribute USING btree (enum_group_id);


--
-- Name: eav_attribute_site_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX eav_attribute_site_id ON eav_attribute USING btree (site_id);


--
-- Name: eav_attribute_slug; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX eav_attribute_slug ON eav_attribute USING btree (slug);


--
-- Name: eav_attribute_slug_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX eav_attribute_slug_like ON eav_attribute USING btree (slug varchar_pattern_ops);


--
-- Name: eav_enumgroup_enums_enumgroup_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX eav_enumgroup_enums_enumgroup_id ON eav_enumgroup_enums USING btree (enumgroup_id);


--
-- Name: eav_enumgroup_enums_enumvalue_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX eav_enumgroup_enums_enumvalue_id ON eav_enumgroup_enums USING btree (enumvalue_id);


--
-- Name: eav_enumgroup_name_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX eav_enumgroup_name_like ON eav_enumgroup USING btree (name varchar_pattern_ops);


--
-- Name: eav_enumvalue_value_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX eav_enumvalue_value_like ON eav_enumvalue USING btree (value varchar_pattern_ops);


--
-- Name: eav_value_attribute_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX eav_value_attribute_id ON eav_value USING btree (attribute_id);


--
-- Name: eav_value_entity_ct_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX eav_value_entity_ct_id ON eav_value USING btree (entity_ct_id);


--
-- Name: eav_value_generic_value_ct_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX eav_value_generic_value_ct_id ON eav_value USING btree (generic_value_ct_id);


--
-- Name: eav_value_value_enum_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX eav_value_value_enum_id ON eav_value USING btree (value_enum_id);


--
-- Name: item_historicalitem_fase_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX item_historicalitem_fase_id ON item_historicalitem USING btree (fase_id);


--
-- Name: item_historicalitem_history_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX item_historicalitem_history_user_id ON item_historicalitem USING btree (history_user_id);


--
-- Name: item_historicalitem_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX item_historicalitem_id ON item_historicalitem USING btree (id);


--
-- Name: item_historicalitem_tipoitem_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX item_historicalitem_tipoitem_id ON item_historicalitem USING btree (tipoitem_id);


--
-- Name: item_item_fase_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX item_item_fase_id ON item_item USING btree (fase_id);


--
-- Name: item_item_tipoitem_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX item_item_tipoitem_id ON item_item USING btree (tipoitem_id);


--
-- Name: item_relaciones_item_destino_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX item_relaciones_item_destino_id ON item_relaciones USING btree (item_destino_id);


--
-- Name: item_relaciones_item_origen_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX item_relaciones_item_origen_id ON item_relaciones USING btree (item_origen_id);


--
-- Name: lineaBase_lineabase_fase_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "lineaBase_lineabase_fase_id" ON "lineaBase_lineabase" USING btree (fase_id);


--
-- Name: lineaBase_lineabase_items_item_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "lineaBase_lineabase_items_item_id" ON "lineaBase_lineabase_items" USING btree (item_id);


--
-- Name: lineaBase_lineabase_items_lineabase_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "lineaBase_lineabase_items_lineabase_id" ON "lineaBase_lineabase_items" USING btree (lineabase_id);


--
-- Name: principal_fase_proyecto_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX principal_fase_proyecto_id ON principal_fase USING btree (proyecto_id);


--
-- Name: principal_proyecto_estado_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX principal_proyecto_estado_id ON principal_proyecto USING btree (estado_id);


--
-- Name: principal_proyecto_usuario_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX principal_proyecto_usuario_id ON principal_proyecto USING btree (usuario_id);


--
-- Name: proyecto_fase_proyecto_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX proyecto_fase_proyecto_id ON proyecto_fase USING btree (proyecto_id);


--
-- Name: proyecto_fase_usuario_modificacion_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX proyecto_fase_usuario_modificacion_id ON proyecto_fase USING btree (usuario_modificacion_id);


--
-- Name: proyecto_proyecto_miembros_proyecto_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX proyecto_proyecto_miembros_proyecto_id ON proyecto_proyecto_miembros USING btree (proyecto_id);


--
-- Name: proyecto_proyecto_miembros_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX proyecto_proyecto_miembros_user_id ON proyecto_proyecto_miembros USING btree (user_id);


--
-- Name: proyecto_proyecto_usuario_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX proyecto_proyecto_usuario_id ON proyecto_proyecto USING btree (usuario_id);


--
-- Name: proyecto_proyecto_usuario_modificacion_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX proyecto_proyecto_usuario_modificacion_id ON proyecto_proyecto USING btree (usuario_modificacion_id);


--
-- Name: solicitudCambio_comite_primer_integrante_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "solicitudCambio_comite_primer_integrante_id" ON "solicitudCambio_comite" USING btree (primer_integrante_id);


--
-- Name: solicitudCambio_comite_segundo_integrante_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "solicitudCambio_comite_segundo_integrante_id" ON "solicitudCambio_comite" USING btree (segundo_integrante_id);


--
-- Name: solicitudCambio_comite_tercer_integrante_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "solicitudCambio_comite_tercer_integrante_id" ON "solicitudCambio_comite" USING btree (tercer_integrante_id);


--
-- Name: solicitudCambio_solicitud_item_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "solicitudCambio_solicitud_item_id" ON "solicitudCambio_solicitud" USING btree (item_id);


--
-- Name: solicitudCambio_solicitud_usuario_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "solicitudCambio_solicitud_usuario_id" ON "solicitudCambio_solicitud" USING btree (usuario_id);


--
-- Name: attribute_id_refs_id_e9f77f46; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "TipoItemApp_tipoitem_atributos"
    ADD CONSTRAINT attribute_id_refs_id_e9f77f46 FOREIGN KEY (attribute_id) REFERENCES eav_attribute(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_93d2d1f8; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT content_type_id_refs_id_93d2d1f8 FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_d043b34a; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_d043b34a FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: eav_attribute_enum_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY eav_attribute
    ADD CONSTRAINT eav_attribute_enum_group_id_fkey FOREIGN KEY (enum_group_id) REFERENCES eav_enumgroup(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: eav_attribute_site_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY eav_attribute
    ADD CONSTRAINT eav_attribute_site_id_fkey FOREIGN KEY (site_id) REFERENCES django_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: eav_enumgroup_enums_enumvalue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY eav_enumgroup_enums
    ADD CONSTRAINT eav_enumgroup_enums_enumvalue_id_fkey FOREIGN KEY (enumvalue_id) REFERENCES eav_enumvalue(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: eav_value_attribute_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY eav_value
    ADD CONSTRAINT eav_value_attribute_id_fkey FOREIGN KEY (attribute_id) REFERENCES eav_attribute(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: eav_value_entity_ct_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY eav_value
    ADD CONSTRAINT eav_value_entity_ct_id_fkey FOREIGN KEY (entity_ct_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: eav_value_generic_value_ct_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY eav_value
    ADD CONSTRAINT eav_value_generic_value_ct_id_fkey FOREIGN KEY (generic_value_ct_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: eav_value_value_enum_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY eav_value
    ADD CONSTRAINT eav_value_value_enum_id_fkey FOREIGN KEY (value_enum_id) REFERENCES eav_enumvalue(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: enumgroup_id_refs_id_0efd2668; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY eav_enumgroup_enums
    ADD CONSTRAINT enumgroup_id_refs_id_0efd2668 FOREIGN KEY (enumgroup_id) REFERENCES eav_enumgroup(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fase_id_refs_id_4222fa25; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY item_item
    ADD CONSTRAINT fase_id_refs_id_4222fa25 FOREIGN KEY (fase_id) REFERENCES proyecto_fase(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fase_id_refs_id_8e6de5ba; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "TipoItemApp_tipoitem_fases"
    ADD CONSTRAINT fase_id_refs_id_8e6de5ba FOREIGN KEY (fase_id) REFERENCES proyecto_fase(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_f4b32aac; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_f4b32aac FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: history_user_id_refs_id_85de1092; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY item_historicalitem
    ADD CONSTRAINT history_user_id_refs_id_85de1092 FOREIGN KEY (history_user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: item_destino_id_refs_id_45f2c243; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY item_relaciones
    ADD CONSTRAINT item_destino_id_refs_id_45f2c243 FOREIGN KEY (item_destino_id) REFERENCES item_item(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: item_fk_id_refs_id_c0818467; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "TipoItemApp_valor"
    ADD CONSTRAINT item_fk_id_refs_id_c0818467 FOREIGN KEY (item_fk_id) REFERENCES "TipoItemApp_item"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: item_id_refs_id_23014bf3; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "solicitudCambio_solicitud"
    ADD CONSTRAINT item_id_refs_id_23014bf3 FOREIGN KEY (item_id) REFERENCES item_item(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: item_origen_id_refs_id_45f2c243; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY item_relaciones
    ADD CONSTRAINT item_origen_id_refs_id_45f2c243 FOREIGN KEY (item_origen_id) REFERENCES item_item(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: lineabase_id_refs_id_c4865be7; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "lineaBase_lineabase_items"
    ADD CONSTRAINT lineabase_id_refs_id_c4865be7 FOREIGN KEY (lineabase_id) REFERENCES "lineaBase_lineabase"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: primer_integrante_id_refs_id_15ef9c47; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "solicitudCambio_comite"
    ADD CONSTRAINT primer_integrante_id_refs_id_15ef9c47 FOREIGN KEY (primer_integrante_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: principal_fase_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY principal_fase
    ADD CONSTRAINT principal_fase_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: principal_proyecto_estado_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY principal_proyecto
    ADD CONSTRAINT principal_proyecto_estado_id_fkey FOREIGN KEY (estado_id) REFERENCES principal_estadosproyecto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: principal_proyecto_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY principal_proyecto
    ADD CONSTRAINT principal_proyecto_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: principal_userprofile_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY principal_userprofile
    ADD CONSTRAINT principal_userprofile_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: proyecto_fase_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY proyecto_fase
    ADD CONSTRAINT proyecto_fase_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES proyecto_proyecto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: proyecto_id_refs_id_6c316775; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "solicitudCambio_comite"
    ADD CONSTRAINT proyecto_id_refs_id_6c316775 FOREIGN KEY (proyecto_id) REFERENCES proyecto_proyecto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: proyecto_id_refs_id_fcec4724; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY proyecto_proyecto_miembros
    ADD CONSTRAINT proyecto_id_refs_id_fcec4724 FOREIGN KEY (proyecto_id) REFERENCES proyecto_proyecto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: proyecto_proyecto_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY proyecto_proyecto
    ADD CONSTRAINT proyecto_proyecto_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: segundo_integrante_id_refs_id_15ef9c47; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "solicitudCambio_comite"
    ADD CONSTRAINT segundo_integrante_id_refs_id_15ef9c47 FOREIGN KEY (segundo_integrante_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tercer_integrante_id_refs_id_15ef9c47; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "solicitudCambio_comite"
    ADD CONSTRAINT tercer_integrante_id_refs_id_15ef9c47 FOREIGN KEY (tercer_integrante_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tipoitem_fk_id_refs_id_7b0dc349; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "TipoItemApp_item"
    ADD CONSTRAINT tipoitem_fk_id_refs_id_7b0dc349 FOREIGN KEY (tipoitem_fk_id) REFERENCES "TipoItemApp_tipoitem"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tipoitem_id_refs_id_12798f5a; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "TipoItemApp_tipoitem_atributos"
    ADD CONSTRAINT tipoitem_id_refs_id_12798f5a FOREIGN KEY (tipoitem_id) REFERENCES "TipoItemApp_tipoitem"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tipoitem_id_refs_id_7ca2d6f2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "TipoItemApp_tipoitem_fases"
    ADD CONSTRAINT tipoitem_id_refs_id_7ca2d6f2 FOREIGN KEY (tipoitem_id) REFERENCES "TipoItemApp_tipoitem"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tipoitem_id_refs_id_d0982b84; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY item_item
    ADD CONSTRAINT tipoitem_id_refs_id_d0982b84 FOREIGN KEY (tipoitem_id) REFERENCES "TipoItemApp_tipoitem"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_20763599; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY proyecto_proyecto_miembros
    ADD CONSTRAINT user_id_refs_id_20763599 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_40c41112; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_40c41112 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_4dc23c39; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_4dc23c39 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_c0d12874; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT user_id_refs_id_c0d12874 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: usuario_id_refs_id_f3046fc4; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "solicitudCambio_solicitud"
    ADD CONSTRAINT usuario_id_refs_id_f3046fc4 FOREIGN KEY (usuario_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: usuario_modificacion_id_refs_id_147452c5; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY proyecto_fase
    ADD CONSTRAINT usuario_modificacion_id_refs_id_147452c5 FOREIGN KEY (usuario_modificacion_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: usuario_modificacion_id_refs_id_e0d533e6; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY proyecto_proyecto
    ADD CONSTRAINT usuario_modificacion_id_refs_id_e0d533e6 FOREIGN KEY (usuario_modificacion_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: value_ptr_id_refs_id_99588838; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "TipoItemApp_valor"
    ADD CONSTRAINT value_ptr_id_refs_id_99588838 FOREIGN KEY (value_ptr_id) REFERENCES eav_value(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

