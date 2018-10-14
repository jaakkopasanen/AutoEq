# Bose QuietComfort 20 Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.5; 37 4.6; 41 3.5; 45 2.4; 49 1.5; 54 0.5; 60 -0.6; 66 -1.5; 72 -2.3; 79 -3.0; 87 -3.6; 96 -4.1; 106 -4.3; 116 -4.2; 128 -4.1; 141 -3.7; 155 -3.2; 170 -2.7; 187 -2.3; 206 -2.3; 227 -2.7; 249 -3.3; 274 -3.7; 302 -3.7; 332 -3.2; 365 -2.2; 402 -1.1; 442 0.2; 486 1.1; 535 2.1; 588 2.9; 647 2.9; 712 2.5; 783 2.2; 861 1.4; 947 0.5; 1042 -0.3; 1146 -1.1; 1261 -2.1; 1387 -3.3; 1526 -4.1; 1678 -3.2; 1846 -0.2; 2031 3.3; 2234 5.8; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 5.9; 3957 1.0; 4353 0.5; 4788 4.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.1; 7711 -1.2; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 30 Hz    |  0.61 | 9.8 dB   |
| Peaking | 82 Hz    |  0.36 | -6.4 dB  |
| Peaking | 1544 Hz  |  1.77 | -15.1 dB |
| Peaking | 1848 Hz  |  0.63 | 11.0 dB  |
| Peaking | 5785 Hz  |  4.95 | 4.6 dB   |
| Peaking | 331 Hz   |  1.65 | -4.7 dB  |
| Peaking | 821 Hz   |  0.44 | 6.7 dB   |
| Peaking | 1063 Hz  |  0.9  | -7.4 dB  |
| Peaking | 4130 Hz  | 10.12 | -5.6 dB  |
| Peaking | 21620 Hz |  1.59 | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2020%20Passive/Bose%20QuietComfort%2020%20Passive.png)