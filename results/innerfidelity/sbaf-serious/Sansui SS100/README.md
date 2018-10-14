# Sansui SS100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 5.9; 128 5.4; 141 4.8; 155 4.3; 170 3.9; 187 3.4; 206 3.0; 227 2.8; 249 2.4; 274 2.2; 302 1.8; 332 1.3; 365 0.9; 402 0.9; 442 1.5; 486 1.2; 535 1.2; 588 1.3; 647 1.3; 712 0.7; 783 0.3; 861 0.4; 947 0.2; 1042 0.2; 1146 0.5; 1261 0.5; 1387 0.3; 1526 0.8; 1678 0.4; 1846 0.6; 2031 0.6; 2234 0.1; 2457 0.1; 2703 1.1; 2973 1.0; 3270 2.0; 3597 2.0; 3957 0.9; 4353 0.2; 4788 2.8; 5267 5.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sansui SS100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.09 | 6.1 dB  |
| Peaking | 108 Hz  | 1.47 | 1.4 dB  |
| Peaking | 363 Hz  | 3.52 | -0.7 dB |
| Peaking | 569 Hz  | 2.08 | 0.7 dB  |
| Peaking | 5744 Hz | 2.96 | 6.7 dB  |
| Peaking | 2359 Hz | 7.9  | -1.2 dB |
| Peaking | 4312 Hz | 4.58 | -4.4 dB |
| Peaking | 4586 Hz | 1.19 | 4.2 dB  |
| Peaking | 6409 Hz | 1.53 | -4.0 dB |
| Peaking | 6596 Hz | 6.44 | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sansui%20SS100/Sansui%20SS100.png)