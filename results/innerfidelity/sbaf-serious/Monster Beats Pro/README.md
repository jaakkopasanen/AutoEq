# Monster Beats Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.8; 25 0.1; 28 -0.9; 31 -1.7; 34 -2.4; 37 -3.0; 41 -3.7; 45 -4.3; 49 -4.6; 54 -5.0; 60 -5.2; 66 -5.3; 72 -5.3; 79 -5.5; 87 -5.7; 96 -6.0; 106 -6.2; 116 -6.3; 128 -6.4; 141 -6.6; 155 -6.7; 170 -6.6; 187 -6.4; 206 -6.4; 227 -6.2; 249 -5.9; 274 -5.5; 302 -5.1; 332 -4.6; 365 -3.8; 402 -3.5; 442 -3.4; 486 -3.3; 535 -3.2; 588 -2.6; 647 -2.4; 712 -2.3; 783 -1.7; 861 -1.2; 947 -0.3; 1042 -0.0; 1146 -0.0; 1261 0.1; 1387 0.3; 1526 -0.5; 1678 -1.6; 1846 -2.9; 2031 -4.3; 2234 -6.1; 2457 -7.5; 2703 -8.0; 2973 -6.9; 3270 -5.2; 3597 -3.0; 3957 -1.6; 4353 -3.9; 4788 -4.3; 5267 0.2; 5793 5.7; 6373 2.5; 7010 0.2; 7711 -0.4; 8482 -2.0; 9330 -4.7; 10263 -3.9; 11289 -0.2; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 1.28 | -2.7 dB |
| Peaking | 169 Hz  | 0.48 | -6.6 dB |
| Peaking | 2705 Hz | 1.9  | -8.1 dB |
| Peaking | 5965 Hz | 8.23 | 7.6 dB  |
| Peaking | 9636 Hz | 4.68 | -5.4 dB |
| Peaking | 18 Hz   | 2.68 | 2.6 dB  |
| Peaking | 1326 Hz | 2.47 | 1.8 dB  |
| Peaking | 2155 Hz | 3.33 | -1.2 dB |
| Peaking | 4531 Hz | 1.94 | 2.7 dB  |
| Peaking | 4667 Hz | 5.23 | -6.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Pro/Monster%20Beats%20Pro.png)