# Pioneer HDJ-1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.2; 79 3.8; 87 2.6; 96 1.7; 106 1.4; 116 1.4; 128 1.3; 141 1.3; 155 1.4; 170 1.6; 187 1.6; 206 1.6; 227 1.8; 249 2.1; 274 2.5; 302 2.7; 332 2.8; 365 3.1; 402 3.6; 442 3.8; 486 2.8; 535 2.3; 588 2.7; 647 2.1; 712 1.4; 783 1.0; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.6; 1387 -2.5; 1526 -3.2; 1678 -3.1; 1846 -2.0; 2031 -0.4; 2234 1.3; 2457 3.2; 2703 4.5; 2973 5.9; 3270 6.0; 3597 5.8; 3957 1.8; 4353 1.9; 4788 5.5; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.58 | 6.8 dB  |
| Peaking | 420 Hz  | 1.03 | 3.4 dB  |
| Peaking | 1588 Hz | 2.06 | -4.4 dB |
| Peaking | 3026 Hz | 2.21 | 6.5 dB  |
| Peaking | 5673 Hz | 2.99 | 6.3 dB  |
| Peaking | 38 Hz   | 2.64 | -0.8 dB |
| Peaking | 67 Hz   | 2.7  | 2.0 dB  |
| Peaking | 97 Hz   | 2.25 | -1.3 dB |
| Peaking | 2396 Hz | 4.37 | 0.3 dB  |
| Peaking | 8310 Hz | 4.45 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20HDJ-1000/Pioneer%20HDJ-1000.png)