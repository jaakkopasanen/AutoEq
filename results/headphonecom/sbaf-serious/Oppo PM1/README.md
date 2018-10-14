# Oppo PM1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.9; 25 2.7; 28 2.4; 31 2.2; 34 2.0; 37 1.9; 41 2.1; 45 2.5; 49 3.1; 54 2.0; 60 0.2; 66 0.0; 72 -0.1; 79 -0.5; 87 -0.7; 96 -1.1; 106 -1.3; 116 -1.5; 128 -1.6; 141 -2.0; 155 -2.1; 170 -2.1; 187 -2.3; 206 -2.1; 227 -2.0; 249 -1.9; 274 -2.3; 302 -2.4; 332 -2.1; 365 -1.2; 402 -0.3; 442 -0.3; 486 -1.1; 535 -1.3; 588 -1.0; 647 -0.9; 712 -1.1; 783 -1.3; 861 -1.5; 947 -0.6; 1042 0.4; 1146 1.0; 1261 1.1; 1387 -0.1; 1526 0.0; 1678 0.1; 1846 0.7; 2031 1.2; 2234 1.7; 2457 2.6; 2703 2.9; 2973 3.0; 3270 3.1; 3597 3.1; 3957 3.1; 4353 3.3; 4788 4.4; 5267 5.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.0; 9330 -2.4; 10263 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.43 | 3.7 dB  |
| Peaking | 134 Hz  | 0.35 | -3.0 dB |
| Peaking | 2924 Hz | 1.6  | 2.6 dB  |
| Peaking | 5733 Hz | 1.99 | 6.2 dB  |
| Peaking | 8863 Hz | 3.3  | -3.5 dB |
| Peaking | 310 Hz  | 5.12 | -0.7 dB |
| Peaking | 412 Hz  | 5.94 | 1.5 dB  |
| Peaking | 875 Hz  | 2.37 | -1.9 dB |
| Peaking | 1152 Hz | 2    | 2.2 dB  |
| Peaking | 1460 Hz | 2.85 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Oppo%20PM1/Oppo%20PM1.png)