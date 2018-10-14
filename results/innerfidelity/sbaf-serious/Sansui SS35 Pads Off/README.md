# Sansui SS35 Pads Off

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.9; 54 5.4; 60 4.8; 66 4.2; 72 3.9; 79 3.6; 87 3.3; 96 2.9; 106 2.9; 116 2.8; 128 2.8; 141 2.6; 155 2.5; 170 3.0; 187 3.0; 206 3.3; 227 4.1; 249 4.5; 274 4.7; 302 4.4; 332 3.4; 365 2.5; 402 1.9; 442 1.7; 486 1.4; 535 1.7; 588 2.7; 647 3.2; 712 3.2; 783 2.8; 861 1.7; 947 0.7; 1042 -0.4; 1146 -0.8; 1261 -0.6; 1387 0.0; 1526 1.8; 1678 3.3; 1846 4.4; 2031 3.7; 2234 1.4; 2457 2.7; 2703 5.8; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sansui SS35 Pads Off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.38 | 6.2 dB  |
| Peaking | 266 Hz  | 1.53 | 4.1 dB  |
| Peaking | 683 Hz  | 3.48 | 3.0 dB  |
| Peaking | 3356 Hz | 1.2  | 6.0 dB  |
| Peaking | 5646 Hz | 2.9  | 4.5 dB  |
| Peaking | 1256 Hz | 2.79 | -2.8 dB |
| Peaking | 1931 Hz | 1.85 | 3.6 dB  |
| Peaking | 2269 Hz | 5.49 | -4.6 dB |
| Peaking | 6563 Hz | 6.52 | 2.5 dB  |
| Peaking | 7703 Hz | 1.86 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sansui%20SS35%20Pads%20Off/Sansui%20SS35%20Pads%20Off.png)