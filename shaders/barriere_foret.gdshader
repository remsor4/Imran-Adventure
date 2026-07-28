shader_type canvas_item;
render_mode unshaded;

uniform vec4 couleur_sombre : source_color = vec4(0.05, 0.32, 0.16, 0.72);
uniform vec4 couleur_claire : source_color = vec4(0.26, 0.84, 0.51, 0.88);
uniform float vitesse = 2.4;

void fragment() {
	float vague = sin((UV.y * 34.0) - (TIME * vitesse));
	float pulsation = sin((UV.y * 11.0) + (TIME * vitesse * 0.65));
	float melange = clamp((vague * 0.20) + (pulsation * 0.16) + 0.52, 0.0, 1.0);
	vec4 couleur = mix(couleur_sombre, couleur_claire, melange);

	float bord = smoothstep(0.0, 0.20, UV.x) * smoothstep(0.0, 0.20, 1.0 - UV.x);
	couleur.a *= mix(0.58, 1.0, bord);
	COLOR = couleur;
}
