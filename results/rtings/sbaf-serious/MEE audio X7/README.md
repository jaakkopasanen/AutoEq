# MEE audio X7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.7; 28 5.1; 31 4.4; 34 3.9; 37 3.4; 41 2.9; 45 2.5; 49 2.1; 54 1.6; 60 1.0; 66 0.5; 72 0.1; 79 -0.2; 87 -0.6; 96 -1.1; 106 -1.8; 116 -2.4; 128 -2.9; 141 -3.3; 155 -3.5; 170 -3.6; 187 -3.7; 206 -3.8; 227 -3.7; 249 -3.3; 274 -2.8; 302 -2.2; 332 -1.6; 365 -0.9; 402 -0.3; 442 0.2; 486 0.8; 535 1.5; 588 1.6; 647 1.8; 712 2.0; 783 1.7; 861 1.0; 947 0.3; 1042 -0.1; 1146 -0.4; 1261 -0.8; 1387 -1.2; 1526 -1.8; 1678 -2.3; 1846 -2.5; 2031 -2.6; 2234 -2.7; 2457 -3.1; 2703 -4.6; 2973 -6.4; 3270 -7.2; 3597 -7.5; 3957 -9.4; 4353 -13.4; 4788 -13.8; 5267 -6.3; 5793 0.2; 6373 2.3; 7010 2.3; 7711 0.1; 8482 -2.4; 9330 -0.9; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio X7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio X7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 0.54 | 6.3 dB   |
| Peaking | 184 Hz  | 0.71 | -4.3 dB  |
| Peaking | 621 Hz  | 1.24 | 3.0 dB   |
| Peaking | 4723 Hz | 1.59 | -22.7 dB |
| Peaking | 5937 Hz | 1.66 | 14.5 dB  |
| Peaking | 1689 Hz | 2.95 | -0.9 dB  |
| Peaking | 2786 Hz | 1.74 | 1.3 dB   |
| Peaking | 2996 Hz | 5.33 | -2.3 dB  |
| Peaking | 8634 Hz | 5.79 | -3.4 dB  |
| Peaking | 9865 Hz | 1.24 | 1.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/MEE%20audio%20X7/MEE%20audio%20X7.png)