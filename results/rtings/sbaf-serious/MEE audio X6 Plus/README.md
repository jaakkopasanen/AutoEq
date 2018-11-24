# MEE audio X6 Plus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 -1.3; 23 -1.5; 25 -1.4; 28 -1.0; 31 -0.6; 34 -0.2; 37 -0.0; 41 0.1; 45 -0.0; 49 -0.3; 54 -0.7; 60 -1.1; 66 -1.0; 72 -0.6; 79 -0.2; 87 0.1; 96 0.2; 106 0.2; 116 -0.0; 128 -0.1; 141 -0.3; 155 -0.3; 170 -0.2; 187 -0.2; 206 -0.1; 227 0.1; 249 0.3; 274 0.8; 302 1.4; 332 1.9; 365 2.4; 402 2.9; 442 3.4; 486 3.5; 535 3.7; 588 3.8; 647 3.7; 712 3.3; 783 2.5; 861 1.5; 947 0.6; 1042 -0.2; 1146 -0.4; 1261 -0.6; 1387 -1.1; 1526 -2.1; 1678 -2.8; 1846 -3.1; 2031 -3.4; 2234 -3.9; 2457 -4.8; 2703 -6.0; 2973 -5.5; 3270 -3.3; 3597 -2.0; 3957 -3.2; 4353 -6.2; 4788 -9.3; 5267 -9.6; 5793 -2.5; 6373 1.6; 7010 2.4; 7711 0.3; 8482 -0.4; 9330 -0.5; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio X6 Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio X6 Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 49 Hz   | 0.02 | -0.5 dB  |
| Peaking | 542 Hz  | 1.05 | 4.8 dB   |
| Peaking | 2470 Hz | 1.34 | -4.7 dB  |
| Peaking | 5056 Hz | 3.83 | -10.8 dB |
| Peaking | 6528 Hz | 3.83 | 5.2 dB   |
| Peaking | 19 Hz   | 1.66 | -0.8 dB  |
| Peaking | 100 Hz  | 4.34 | 0.7 dB   |
| Peaking | 3399 Hz | 2.73 | -2.4 dB  |
| Peaking | 3408 Hz | 6.9  | 2.6 dB   |
| Peaking | 3716 Hz | 7.34 | 2.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/MEE%20audio%20X6%20Plus/MEE%20audio%20X6%20Plus.png)