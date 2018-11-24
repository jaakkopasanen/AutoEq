# RBH EP1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 21 -10.1; 23 -9.9; 25 -9.6; 28 -9.2; 31 -8.9; 34 -8.7; 37 -8.4; 41 -7.9; 45 -7.6; 49 -7.4; 54 -7.2; 60 -6.9; 66 -6.8; 72 -6.7; 79 -6.6; 87 -6.5; 96 -6.4; 106 -6.3; 116 -5.7; 128 -5.9; 141 -5.7; 155 -5.0; 170 -5.1; 187 -4.6; 206 -4.3; 227 -3.8; 249 -3.4; 274 -3.1; 302 -2.5; 332 -2.2; 365 -1.8; 402 -1.4; 442 -0.8; 486 -0.6; 535 -0.1; 588 0.3; 647 1.2; 712 1.0; 783 1.1; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.1; 1387 -2.0; 1526 -3.1; 1678 -4.0; 1846 -4.4; 2031 -4.4; 2234 -4.4; 2457 -3.6; 2703 -2.9; 2973 -1.0; 3270 0.5; 3597 0.9; 3957 -0.9; 4353 -4.8; 4788 -6.7; 5267 -3.7; 5793 0.0; 6373 3.3; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.1; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RBH EP1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RBH EP1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 13 Hz   | 0.18 | -10.0 dB |
| Peaking | 153 Hz  | 0.81 | -3.4 dB  |
| Peaking | 1979 Hz | 2.19 | -5.0 dB  |
| Peaking | 4802 Hz | 5.21 | -7.4 dB  |
| Peaking | 6549 Hz | 5.2  | 4.7 dB   |
| Peaking | 11 Hz   | 0.83 | -1.1 dB  |
| Peaking | 736 Hz  | 2.2  | 1.9 dB   |
| Peaking | 1510 Hz | 6.21 | -0.9 dB  |
| Peaking | 3399 Hz | 1.73 | -2.6 dB  |
| Peaking | 3465 Hz | 3.8  | 5.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RBH%20EP1/RBH%20EP1.png)