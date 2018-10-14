# PSB M4U 2 passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 21 -0.2; 23 -0.2; 25 -0.2; 28 -0.2; 31 -0.1; 34 -0.0; 37 0.1; 41 0.3; 45 0.5; 49 0.7; 54 0.9; 60 1.4; 66 1.9; 72 2.4; 79 2.6; 87 1.3; 96 -1.2; 106 -2.4; 116 -2.0; 128 -1.7; 141 -1.6; 155 -0.9; 170 -0.8; 187 -1.3; 206 -0.6; 227 0.0; 249 0.6; 274 1.7; 302 2.1; 332 2.6; 365 2.5; 402 3.2; 442 3.6; 486 3.1; 535 2.8; 588 2.6; 647 2.4; 712 1.6; 783 1.1; 861 0.4; 947 0.1; 1042 0.0; 1146 0.1; 1261 -0.0; 1387 -0.4; 1526 -0.5; 1678 -0.4; 1846 0.3; 2031 0.9; 2234 1.2; 2457 1.7; 2703 2.1; 2973 2.0; 3270 0.9; 3597 -0.1; 3957 -0.6; 4353 0.2; 4788 0.6; 5267 1.9; 5793 4.2; 6373 3.2; 7010 2.3; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.3dB` and instead set Global volume in the UI for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 2 passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 79 Hz   | 1.7  | 7.1 dB  |
| Peaking | 98 Hz   | 1.18 | -5.9 dB |
| Peaking | 434 Hz  | 1.27 | 3.7 dB  |
| Peaking | 2701 Hz | 4.18 | 2.3 dB  |
| Peaking | 6020 Hz | 4.03 | 4.2 dB  |
| Peaking | 192 Hz  | 7.13 | -0.9 dB |
| Peaking | 287 Hz  | 8.43 | 0.8 dB  |
| Peaking | 636 Hz  | 7.95 | 0.7 dB  |
| Peaking | 1441 Hz | 3.27 | -0.9 dB |
| Peaking | 3896 Hz | 6.99 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%202%20passive/PSB%20M4U%202%20passive.png)