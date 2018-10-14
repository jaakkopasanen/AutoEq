# Denon AH-D1001

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.8; 49 5.4; 54 5.0; 60 4.8; 66 4.5; 72 4.0; 79 3.4; 87 2.7; 96 2.1; 106 1.8; 116 1.6; 128 1.2; 141 1.1; 155 1.0; 170 1.1; 187 1.2; 206 1.4; 227 1.7; 249 2.1; 274 2.5; 302 2.9; 332 3.3; 365 3.6; 402 3.9; 442 4.2; 486 4.1; 535 3.9; 588 3.5; 647 2.4; 712 1.1; 783 0.5; 861 -0.1; 947 -0.0; 1042 0.2; 1146 0.7; 1261 1.3; 1387 1.4; 1526 1.6; 1678 2.1; 1846 3.1; 2031 4.1; 2234 4.2; 2457 3.6; 2703 2.2; 2973 4.0; 3270 4.6; 3597 1.7; 3957 0.9; 4353 -0.5; 4788 0.5; 5267 3.4; 5793 4.8; 6373 3.5; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -2.0; 10263 -1.5; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.52 | 6.4 dB  |
| Peaking | 429 Hz  | 1.34 | 4.3 dB  |
| Peaking | 2125 Hz | 2.56 | 4.2 dB  |
| Peaking | 3169 Hz | 6.36 | 4.1 dB  |
| Peaking | 5941 Hz | 4.22 | 4.9 dB  |
| Peaking | 583 Hz  | 5.74 | 1.1 dB  |
| Peaking | 859 Hz  | 3.45 | -1.3 dB |
| Peaking | 4421 Hz | 6.09 | -2.4 dB |
| Peaking | 5624 Hz | 0.87 | 0.7 dB  |
| Peaking | 9563 Hz | 4.56 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D1001/Denon%20AH-D1001.png)