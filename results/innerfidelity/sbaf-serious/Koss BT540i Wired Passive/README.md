# Koss BT540i Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.8; 25 -0.1; 28 -1.2; 31 -2.1; 34 -2.9; 37 -3.6; 41 -4.3; 45 -4.8; 49 -5.3; 54 -5.7; 60 -6.2; 66 -6.6; 72 -6.9; 79 -7.1; 87 -7.2; 96 -7.5; 106 -7.6; 116 -7.3; 128 -7.4; 141 -8.0; 155 -8.6; 170 -7.6; 187 -7.8; 206 -8.0; 227 -7.5; 249 -7.0; 274 -6.1; 302 -4.9; 332 -4.5; 365 -3.1; 402 -1.3; 442 0.1; 486 0.5; 535 1.0; 588 1.5; 647 1.3; 712 0.7; 783 0.5; 861 0.1; 947 -0.0; 1042 0.0; 1146 -0.2; 1261 -0.4; 1387 -1.1; 1526 -1.7; 1678 -2.4; 1846 -2.9; 2031 -3.2; 2234 -4.0; 2457 -4.6; 2703 -5.7; 2973 -6.4; 3270 -5.8; 3597 -3.9; 3957 -1.2; 4353 0.9; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.3; 7010 2.0; 7711 0.1; 8482 -3.3; 9330 -4.9; 10263 -1.4; 11289 0.0; 12418 -0.2; 13660 -1.3; 15026 -1.3; 16529 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss BT540i Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -7.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 85 Hz    | 0.65 | -7.1 dB |
| Peaking | 210 Hz   | 1.44 | -5.8 dB |
| Peaking | 2999 Hz  | 1.4  | -7.1 dB |
| Peaking | 5253 Hz  | 2.66 | 9.1 dB  |
| Peaking | 21 Hz    | 2.73 | 2.9 dB  |
| Peaking | 588 Hz   | 2.33 | 2.7 dB  |
| Peaking | 6391 Hz  | 7.04 | 2.9 dB  |
| Peaking | 9064 Hz  | 4.78 | -5.9 dB |
| Peaking | 14418 Hz | 4.49 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20BT540i%20Wired%20Passive/Koss%20BT540i%20Wired%20Passive.png)