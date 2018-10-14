# Thinksoud RAIN

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 21 -10.1; 23 -10.2; 25 -10.3; 28 -10.5; 31 -10.6; 34 -10.7; 37 -10.7; 41 -10.8; 45 -11.0; 49 -11.1; 54 -11.3; 60 -11.4; 66 -11.7; 72 -11.8; 79 -12.0; 87 -12.1; 96 -12.2; 106 -12.2; 116 -12.2; 128 -12.2; 141 -12.1; 155 -11.9; 170 -11.7; 187 -11.4; 206 -11.0; 227 -10.5; 249 -10.0; 274 -9.4; 302 -8.8; 332 -8.1; 365 -7.2; 402 -6.5; 442 -5.8; 486 -5.1; 535 -4.3; 588 -3.6; 647 -2.8; 712 -2.1; 783 -1.4; 861 -1.0; 947 -0.3; 1042 0.2; 1146 0.4; 1261 0.4; 1387 0.4; 1526 0.3; 1678 0.4; 1846 0.7; 2031 1.1; 2234 1.2; 2457 0.5; 2703 -0.8; 2973 0.6; 3270 3.5; 3597 4.6; 3957 2.9; 4353 -0.6; 4788 -4.4; 5267 -7.6; 5793 -1.3; 6373 3.7; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.7dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksoud RAIN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.7dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 0.24 | -9.7 dB  |
| Peaking | 148 Hz  | 0.58 | -7.0 dB  |
| Peaking | 325 Hz  | 0.98 | -3.6 dB  |
| Peaking | 4782 Hz | 1.08 | 6.3 dB   |
| Peaking | 5101 Hz | 4.27 | -14.4 dB |
| Peaking | 1139 Hz | 2.34 | 1.1 dB   |
| Peaking | 2757 Hz | 7.11 | -2.8 dB  |
| Peaking | 3512 Hz | 5.35 | 2.9 dB   |
| Peaking | 6535 Hz | 5.22 | 5.8 dB   |
| Peaking | 6760 Hz | 1.2  | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Thinksoud%20RAIN/Thinksoud%20RAIN.png)