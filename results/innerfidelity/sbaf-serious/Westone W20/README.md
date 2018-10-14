# Westone W20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.0; 25 1.9; 28 1.7; 31 1.5; 34 1.4; 37 1.2; 41 1.0; 45 0.8; 49 0.6; 54 0.4; 60 0.1; 66 -0.3; 72 -0.7; 79 -1.0; 87 -1.5; 96 -1.9; 106 -2.2; 116 -2.4; 128 -2.8; 141 -3.1; 155 -3.2; 170 -3.4; 187 -3.4; 206 -3.5; 227 -3.4; 249 -3.4; 274 -3.2; 302 -3.1; 332 -2.9; 365 -2.6; 402 -2.3; 442 -1.9; 486 -1.7; 535 -1.3; 588 -0.7; 647 -0.3; 712 -0.1; 783 0.3; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.4; 1387 -0.9; 1526 -1.4; 1678 -1.8; 1846 -1.8; 2031 -1.6; 2234 -1.3; 2457 0.4; 2703 2.6; 2973 5.7; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.5; 5267 4.3; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.52 | 2.2 dB  |
| Peaking | 192 Hz  | 0.6  | -3.8 dB |
| Peaking | 2077 Hz | 1.79 | -4.5 dB |
| Peaking | 3486 Hz | 1.26 | 7.5 dB  |
| Peaking | 6035 Hz | 4.68 | 4.3 dB  |
| Peaking | 815 Hz  | 2.95 | 1.0 dB  |
| Peaking | 1544 Hz | 6.73 | -0.7 dB |
| Peaking | 4617 Hz | 8.63 | 1.5 dB  |
| Peaking | 6661 Hz | 6.65 | 2.1 dB  |
| Peaking | 7578 Hz | 1.68 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W20/Westone%20W20.png)