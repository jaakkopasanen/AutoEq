# Monster Turbine-Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -9.6; 23 -9.6; 25 -9.6; 28 -9.7; 31 -9.7; 34 -9.8; 37 -9.8; 41 -9.9; 45 -9.9; 49 -10.0; 54 -10.1; 60 -10.2; 66 -10.4; 72 -10.5; 79 -10.6; 87 -10.7; 96 -10.6; 106 -10.5; 116 -10.5; 128 -10.3; 141 -10.1; 155 -10.1; 170 -10.0; 187 -9.5; 206 -9.0; 227 -8.5; 249 -7.9; 274 -7.3; 302 -6.6; 332 -5.9; 365 -5.1; 402 -4.4; 442 -3.7; 486 -3.1; 535 -2.3; 588 -1.6; 647 -0.9; 712 -0.4; 783 -0.0; 861 0.1; 947 0.1; 1042 -0.2; 1146 -0.5; 1261 -0.9; 1387 -1.6; 1526 -2.5; 1678 -3.5; 1846 -4.2; 2031 -4.3; 2234 -3.8; 2457 -2.9; 2703 -1.5; 2973 0.2; 3270 1.7; 3597 2.1; 3957 0.9; 4353 -0.4; 4788 0.9; 5267 4.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine-Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.23 | -9.2 dB |
| Peaking | 133 Hz  | 0.67 | -5.4 dB |
| Peaking | 269 Hz  | 1.14 | -3.4 dB |
| Peaking | 1971 Hz | 2.63 | -4.8 dB |
| Peaking | 5881 Hz | 3.43 | 6.8 dB  |
| Peaking | 830 Hz  | 2.99 | 1.3 dB  |
| Peaking | 2588 Hz | 2.82 | -1.8 dB |
| Peaking | 3421 Hz | 2.15 | 2.9 dB  |
| Peaking | 4410 Hz | 5.65 | -2.7 dB |
| Peaking | 8145 Hz | 4.76 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Turbine-Pro/Monster%20Turbine-Pro.png)