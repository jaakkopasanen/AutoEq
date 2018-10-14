# Fischer Audio Tandem

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.9; 54 5.4; 60 4.6; 66 3.9; 72 3.3; 79 2.6; 87 1.8; 96 1.0; 106 0.6; 116 0.2; 128 -0.5; 141 -0.8; 155 -1.2; 170 -1.5; 187 -1.6; 206 -1.8; 227 -1.8; 249 -2.0; 274 -1.9; 302 -1.8; 332 -1.8; 365 -1.5; 402 -1.4; 442 -1.1; 486 -1.0; 535 -0.8; 588 -0.3; 647 -0.0; 712 -0.1; 783 0.2; 861 0.2; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.1; 1387 0.1; 1526 0.2; 1678 0.4; 1846 1.1; 2031 2.2; 2234 3.4; 2457 5.2; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.9; 4353 2.7; 4788 3.1; 5267 5.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Tandem ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.37 | 7.3 dB  |
| Peaking | 148 Hz  | 0.45 | -4.0 dB |
| Peaking | 3080 Hz | 1.61 | 6.6 dB  |
| Peaking | 5837 Hz | 3.56 | 5.6 dB  |
| Peaking | 797 Hz  | 1.89 | 0.8 dB  |
| Peaking | 1394 Hz | 1.16 | -0.8 dB |
| Peaking | 2481 Hz | 6.35 | 1.3 dB  |
| Peaking | 6616 Hz | 8.44 | 1.9 dB  |
| Peaking | 7853 Hz | 2.37 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20Tandem/Fischer%20Audio%20Tandem.png)