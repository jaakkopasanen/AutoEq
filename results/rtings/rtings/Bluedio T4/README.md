# Bluedio T4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.3; 23 -3.7; 25 -3.0; 28 -2.1; 31 -1.1; 34 -0.2; 37 0.7; 41 1.6; 45 2.4; 49 3.1; 54 3.8; 60 4.5; 66 5.0; 72 5.5; 79 5.8; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 6.0; 588 6.0; 647 6.0; 712 5.9; 783 3.4; 861 1.7; 947 0.2; 1042 -0.5; 1146 -2.3; 1261 -2.0; 1387 -0.6; 1526 -0.5; 1678 -1.2; 1846 -2.2; 2031 -2.9; 2234 -3.3; 2457 -2.2; 2703 -0.6; 2973 0.4; 3270 1.3; 3597 2.4; 3957 2.1; 4353 -0.4; 4788 0.5; 5267 2.0; 5793 1.2; 6373 2.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.79 | -7.4 dB |
| Peaking | 128 Hz  | 0.18 | 6.7 dB  |
| Peaking | 624 Hz  | 1.33 | 5.2 dB  |
| Peaking | 1646 Hz | 0.37 | -5.4 dB |
| Peaking | 3985 Hz | 0.73 | 4.6 dB  |
| Peaking | 1202 Hz | 4.34 | -2.6 dB |
| Peaking | 1450 Hz | 1.96 | 3.7 dB  |
| Peaking | 3126 Hz | 0.69 | -4.1 dB |
| Peaking | 3366 Hz | 1.94 | 5.1 dB  |
| Peaking | 6556 Hz | 4.71 | 3.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Bluedio%20T4/Bluedio%20T4.png)