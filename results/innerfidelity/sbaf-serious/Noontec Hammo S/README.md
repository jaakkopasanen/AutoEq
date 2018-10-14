# Noontec Hammo S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.6; 25 0.4; 28 0.2; 31 0.0; 34 -0.1; 37 -0.2; 41 -0.3; 45 -0.4; 49 -0.5; 54 -0.6; 60 -0.7; 66 -0.8; 72 -0.9; 79 -1.0; 87 -1.1; 96 -1.0; 106 -0.6; 116 -0.5; 128 -1.4; 141 -2.5; 155 -3.1; 170 -1.9; 187 -2.8; 206 -2.8; 227 -2.5; 249 -1.9; 274 -1.3; 302 -0.6; 332 0.1; 365 0.9; 402 1.6; 442 1.9; 486 2.1; 535 2.1; 588 1.8; 647 1.0; 712 0.5; 783 0.9; 861 0.9; 947 0.7; 1042 -0.4; 1146 -1.0; 1261 -1.7; 1387 -2.2; 1526 -2.5; 1678 -2.6; 1846 -2.3; 2031 -1.4; 2234 -0.3; 2457 1.3; 2703 2.4; 2973 3.3; 3270 2.9; 3597 -0.5; 3957 1.3; 4353 -0.1; 4788 3.3; 5267 5.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.9; 10263 -0.2; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Hammo S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 224 Hz  |  0.81 | -4.3 dB |
| Peaking | 425 Hz  |  0.8  | 3.7 dB  |
| Peaking | 1599 Hz |  1.52 | -3.3 dB |
| Peaking | 2863 Hz |  3.71 | 3.8 dB  |
| Peaking | 5758 Hz |  3.33 | 6.9 dB  |
| Peaking | 16 Hz   |  1.68 | 1.0 dB  |
| Peaking | 156 Hz  | 10.74 | -0.7 dB |
| Peaking | 2454 Hz |  5.44 | 0.4 dB  |
| Peaking | 3633 Hz | 15.99 | -1.9 dB |
| Peaking | 9298 Hz |  4.43 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Hammo%20S/Noontec%20Hammo%20S.png)