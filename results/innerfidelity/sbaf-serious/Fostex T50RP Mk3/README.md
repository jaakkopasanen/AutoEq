# Fostex T50RP Mk3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.5; 54 4.4; 60 3.2; 66 2.1; 72 1.3; 79 0.5; 87 -0.1; 96 -0.4; 106 -0.7; 116 -0.7; 128 -0.8; 141 -0.8; 155 -0.6; 170 -0.2; 187 0.1; 206 0.4; 227 0.7; 249 0.9; 274 1.0; 302 1.1; 332 1.5; 365 1.8; 402 2.1; 442 2.7; 486 2.3; 535 2.4; 588 2.2; 647 2.0; 712 1.4; 783 1.0; 861 0.5; 947 -0.2; 1042 0.2; 1146 0.6; 1261 1.0; 1387 1.2; 1526 1.5; 1678 1.5; 1846 2.0; 2031 2.1; 2234 2.5; 2457 2.2; 2703 2.3; 2973 1.8; 3270 1.4; 3597 0.4; 3957 -0.5; 4353 -1.4; 4788 -0.0; 5267 4.5; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.7; 9330 -4.2; 10263 -1.9; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP Mk3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 1.05 | 7.1 dB  |
| Peaking | 482 Hz  | 1.54 | 2.7 dB  |
| Peaking | 2197 Hz | 1.83 | 2.5 dB  |
| Peaking | 6018 Hz | 4.02 | 6.9 dB  |
| Peaking | 9328 Hz | 4.85 | -4.9 dB |
| Peaking | 50 Hz   | 3.41 | 2.1 dB  |
| Peaking | 108 Hz  | 1.54 | -1.7 dB |
| Peaking | 3057 Hz | 3.22 | 0.9 dB  |
| Peaking | 4518 Hz | 3.44 | -3.4 dB |
| Peaking | 5229 Hz | 6.28 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50RP%20Mk3/Fostex%20T50RP%20Mk3.png)