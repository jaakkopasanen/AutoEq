# Sansui SS35

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 4.4; 402 2.3; 442 1.2; 486 1.1; 535 1.4; 588 1.6; 647 1.6; 712 1.4; 783 1.3; 861 0.8; 947 0.3; 1042 -0.3; 1146 -0.6; 1261 -1.0; 1387 -1.1; 1526 -0.5; 1678 0.6; 1846 1.8; 2031 1.4; 2234 -0.8; 2457 0.5; 2703 3.8; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 3.4; 4788 4.1; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sansui SS35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.21 | 6.1 dB  |
| Peaking | 200 Hz  | 1.02 | 3.1 dB  |
| Peaking | 315 Hz  | 3.33 | 3.2 dB  |
| Peaking | 3370 Hz | 2.54 | 6.4 dB  |
| Peaking | 5713 Hz | 2.95 | 6.0 dB  |
| Peaking | 105 Hz  | 2.99 | 0.2 dB  |
| Peaking | 1388 Hz | 2.01 | -4.1 dB |
| Peaking | 1727 Hz | 1.05 | 3.1 dB  |
| Peaking | 2300 Hz | 6.46 | -4.2 dB |
| Peaking | 8306 Hz | 3.7  | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sansui%20SS35/Sansui%20SS35.png)