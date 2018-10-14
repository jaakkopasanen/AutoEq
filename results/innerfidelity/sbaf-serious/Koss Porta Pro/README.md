# Koss Porta Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.8; 31 5.0; 34 4.0; 37 3.1; 41 2.1; 45 1.1; 49 0.3; 54 -0.7; 60 -1.7; 66 -2.5; 72 -3.3; 79 -3.9; 87 -4.6; 96 -5.1; 106 -5.5; 116 -5.5; 128 -5.7; 141 -5.7; 155 -5.6; 170 -5.4; 187 -5.0; 206 -4.7; 227 -4.3; 249 -3.9; 274 -3.5; 302 -3.2; 332 -2.8; 365 -2.3; 402 -1.9; 442 -1.4; 486 -1.1; 535 -0.8; 588 -0.3; 647 -0.2; 712 -0.0; 783 0.2; 861 0.1; 947 -0.0; 1042 -0.0; 1146 -0.2; 1261 -0.6; 1387 -1.4; 1526 -2.4; 1678 -3.4; 1846 -3.9; 2031 -3.5; 2234 -2.2; 2457 0.2; 2703 2.6; 2973 5.1; 3270 6.0; 3597 6.0; 3957 6.0; 4353 3.0; 4788 1.6; 5267 4.3; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 25 Hz   |  0.85 | 7.1 dB  |
| Peaking | 125 Hz  |  0.55 | -6.3 dB |
| Peaking | 1928 Hz |  2.37 | -5.3 dB |
| Peaking | 3371 Hz |  2.03 | 7.1 dB  |
| Peaking | 5929 Hz |  4.35 | 5.8 dB  |
| Peaking | 818 Hz  |  1.62 | 0.8 dB  |
| Peaking | 1558 Hz |  6.75 | -0.7 dB |
| Peaking | 4648 Hz | 12.94 | -2.0 dB |
| Peaking | 6660 Hz |  8.64 | 1.9 dB  |
| Peaking | 7894 Hz |  2.73 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)