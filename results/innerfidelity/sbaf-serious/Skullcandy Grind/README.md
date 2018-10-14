# Skullcandy Grind

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 0.0; 23 0.3; 25 -0.2; 28 -0.7; 31 -1.1; 34 -1.4; 37 -1.6; 41 -1.7; 45 -1.8; 49 -1.8; 54 -1.8; 60 -1.7; 66 -1.6; 72 -1.5; 79 -1.5; 87 -1.4; 96 -1.3; 106 -1.2; 116 -1.0; 128 -0.9; 141 -1.2; 155 -1.5; 170 -1.1; 187 -1.2; 206 -1.2; 227 -0.9; 249 -0.6; 274 -0.1; 302 0.1; 332 0.1; 365 0.4; 402 0.9; 442 1.8; 486 2.1; 535 2.6; 588 3.6; 647 4.3; 712 4.8; 783 4.6; 861 1.8; 947 -0.3; 1042 0.8; 1146 1.8; 1261 1.7; 1387 -0.2; 1526 -1.4; 1678 -2.5; 1846 -4.0; 2031 -4.8; 2234 -4.0; 2457 -3.2; 2703 -1.4; 2973 0.7; 3270 2.2; 3597 3.4; 3957 -1.8; 4353 -2.4; 4788 -1.4; 5267 1.9; 5793 3.9; 6373 3.0; 7010 1.1; 7711 -1.3; 8482 -3.9; 9330 -3.6; 10263 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.0dB` and instead set Global volume in the UI for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Grind ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 683 Hz  | 2.08 | 5.1 dB  |
| Peaking | 2066 Hz | 2.45 | -5.2 dB |
| Peaking | 3429 Hz | 8.6  | 4.6 dB  |
| Peaking | 6057 Hz | 5.22 | 4.6 dB  |
| Peaking | 8750 Hz | 4.88 | -4.9 dB |
| Peaking | 17 Hz   | 1.35 | 2.4 dB  |
| Peaking | 44 Hz   | 0.53 | -2.1 dB |
| Peaking | 181 Hz  | 1.87 | -1.1 dB |
| Peaking | 4298 Hz | 1.5  | 2.1 dB  |
| Peaking | 4335 Hz | 4.01 | -5.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Grind/Skullcandy%20Grind.png)