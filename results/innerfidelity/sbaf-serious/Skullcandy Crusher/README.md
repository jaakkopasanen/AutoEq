# Skullcandy Crusher

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.7dB
GraphicEQ: 21 0.0; 23 4.5; 25 3.2; 28 1.5; 31 0.1; 34 -1.1; 37 -2.1; 41 -3.1; 45 -3.7; 49 -4.0; 54 -4.1; 60 -4.4; 66 -4.4; 72 -4.1; 79 -3.7; 87 -3.1; 96 -2.0; 106 -2.7; 116 -3.3; 128 -4.1; 141 -3.8; 155 -4.2; 170 -3.7; 187 -4.2; 206 -4.3; 227 -4.4; 249 -4.5; 274 -4.4; 302 -4.5; 332 -4.1; 365 -3.7; 402 -3.5; 442 -3.5; 486 -3.5; 535 -3.8; 588 -3.6; 647 -3.6; 712 -3.5; 783 -3.0; 861 -2.6; 947 -1.4; 1042 0.1; 1146 1.9; 1261 1.0; 1387 0.6; 1526 -1.3; 1678 -2.5; 1846 -2.4; 2031 -2.7; 2234 -1.8; 2457 -1.8; 2703 -1.0; 2973 -0.3; 3270 -0.8; 3597 -0.4; 3957 -1.3; 4353 -2.1; 4788 4.2; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.7dB` and instead set Global volume in the UI for both channels to **-67**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.59 | 7.2 dB  |
| Peaking | 51 Hz   | 1.11 | -4.3 dB |
| Peaking | 252 Hz  | 0.47 | -4.3 dB |
| Peaking | 674 Hz  | 2.82 | -1.8 dB |
| Peaking | 5758 Hz | 3.74 | 7.2 dB  |
| Peaking | 1245 Hz | 2.79 | 4.8 dB  |
| Peaking | 1675 Hz | 1.13 | -3.1 dB |
| Peaking | 4232 Hz | 8.45 | -4.3 dB |
| Peaking | 4933 Hz | 9.27 | 3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Crusher/Skullcandy%20Crusher.png)