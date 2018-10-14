# Phiaton MS 300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.4; 45 4.5; 49 3.9; 54 3.3; 60 2.7; 66 2.3; 72 2.3; 79 2.2; 87 1.6; 96 1.4; 106 1.1; 116 1.1; 128 0.8; 141 0.9; 155 0.7; 170 0.8; 187 0.9; 206 1.1; 227 1.8; 249 1.5; 274 1.3; 302 1.2; 332 1.0; 365 1.0; 402 1.4; 442 1.3; 486 1.6; 535 2.5; 588 3.8; 647 4.6; 712 4.2; 783 3.5; 861 2.2; 947 0.9; 1042 -0.6; 1146 -1.9; 1261 -2.7; 1387 -3.2; 1526 -2.9; 1678 -2.0; 1846 -1.7; 2031 -0.3; 2234 1.8; 2457 4.7; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.64 | 6.4 dB  |
| Peaking | 242 Hz  | 2.56 | 1.2 dB  |
| Peaking | 693 Hz  | 1.74 | 5.3 dB  |
| Peaking | 1517 Hz | 1.16 | -6.5 dB |
| Peaking | 3419 Hz | 0.77 | 8.0 dB  |
| Peaking | 2062 Hz | 5.5  | -1.1 dB |
| Peaking | 2565 Hz | 4.81 | 1.9 dB  |
| Peaking | 3586 Hz | 2.83 | -1.2 dB |
| Peaking | 6268 Hz | 2.25 | 5.4 dB  |
| Peaking | 7406 Hz | 1.49 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20MS%20300/Phiaton%20MS%20300.png)