# Bose QuietComfort 25

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.1; 23 -1.5; 25 -1.7; 28 -1.6; 31 -1.3; 34 -0.9; 37 -0.6; 41 -0.5; 45 -0.7; 49 -0.9; 54 -1.2; 60 -1.4; 66 -1.6; 72 -1.6; 79 -1.7; 87 -1.6; 96 -1.5; 106 -1.4; 116 -1.3; 128 -1.3; 141 -1.3; 155 -1.2; 170 -0.9; 187 -0.8; 206 -0.9; 227 -0.7; 249 -0.5; 274 -0.4; 302 -0.1; 332 0.2; 365 0.5; 402 0.8; 442 1.3; 486 1.4; 535 1.6; 588 2.0; 647 2.0; 712 1.8; 783 1.6; 861 1.0; 947 0.3; 1042 0.3; 1146 0.5; 1261 0.3; 1387 -0.5; 1526 -2.1; 1678 -3.9; 1846 -5.5; 2031 -6.0; 2234 -4.9; 2457 -4.1; 2703 -3.8; 2973 -4.7; 3270 -6.1; 3597 -5.3; 3957 -2.3; 4353 1.0; 4788 4.1; 5267 6.0; 5793 3.6; 6373 0.8; 7010 2.3; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 103 Hz  | 0.2  | -1.5 dB |
| Peaking | 596 Hz  | 0.77 | 2.6 dB  |
| Peaking | 1968 Hz | 2.46 | -6.1 dB |
| Peaking | 3391 Hz | 2.68 | -6.5 dB |
| Peaking | 5148 Hz | 3.25 | 7.3 dB  |
| Peaking | 43 Hz   | 3.13 | 0.6 dB  |
| Peaking | 975 Hz  | 6.5  | -0.8 dB |
| Peaking | 1236 Hz | 4.29 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2025/Bose%20QuietComfort%2025.png)