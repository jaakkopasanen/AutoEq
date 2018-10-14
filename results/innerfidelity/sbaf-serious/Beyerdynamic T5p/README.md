# Beyerdynamic T5p

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.4; 25 0.3; 28 0.3; 31 0.4; 34 0.5; 37 0.5; 41 0.7; 45 0.8; 49 0.9; 54 1.1; 60 1.4; 66 1.8; 72 2.1; 79 1.9; 87 0.7; 96 -0.8; 106 -2.2; 116 -2.7; 128 -3.1; 141 -2.9; 155 -2.0; 170 -1.2; 187 -2.0; 206 -1.6; 227 -0.9; 249 -0.4; 274 0.2; 302 0.7; 332 1.0; 365 1.2; 402 1.2; 442 1.4; 486 1.1; 535 1.1; 588 2.1; 647 4.7; 712 2.0; 783 1.7; 861 0.6; 947 0.4; 1042 0.1; 1146 -0.4; 1261 -1.5; 1387 -2.0; 1526 -2.1; 1678 -2.4; 1846 -1.9; 2031 -1.8; 2234 -3.0; 2457 -1.0; 2703 0.7; 2973 1.5; 3270 2.7; 3597 3.7; 3957 4.7; 4353 2.4; 4788 6.0; 5267 5.5; 5793 0.8; 6373 0.1; 7010 2.3; 7711 0.2; 8482 -2.2; 9330 -0.5; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.0dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 78 Hz   |  1.31 | 3.9 dB  |
| Peaking | 117 Hz  |  1.31 | -4.8 dB |
| Peaking | 646 Hz  |  1.68 | 3.5 dB  |
| Peaking | 1816 Hz |  1.1  | -3.2 dB |
| Peaking | 4207 Hz |  1.58 | 5.5 dB  |
| Peaking | 336 Hz  |  1.07 | -1.8 dB |
| Peaking | 339 Hz  |  1.85 | 2.8 dB  |
| Peaking | 5129 Hz |  9.38 | 3.1 dB  |
| Peaking | 6014 Hz | 10.18 | -2.6 dB |
| Peaking | 8600 Hz |  7.61 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T5p/Beyerdynamic%20T5p.png)