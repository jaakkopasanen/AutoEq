# MEE audio M6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 21 -10.5; 23 -10.4; 25 -10.2; 28 -9.9; 31 -9.6; 34 -9.4; 37 -9.1; 41 -8.8; 45 -8.5; 49 -8.2; 54 -8.0; 60 -8.0; 66 -8.0; 72 -8.0; 79 -8.0; 87 -8.1; 96 -8.2; 106 -8.4; 116 -8.6; 128 -8.8; 141 -8.9; 155 -8.8; 170 -8.6; 187 -8.4; 206 -8.0; 227 -7.6; 249 -6.9; 274 -6.3; 302 -5.7; 332 -5.1; 365 -4.4; 402 -3.6; 442 -2.7; 486 -1.8; 535 -0.8; 588 -0.2; 647 0.5; 712 0.9; 783 1.1; 861 0.8; 947 0.3; 1042 -0.1; 1146 -0.5; 1261 -0.6; 1387 -0.8; 1526 -1.0; 1678 -1.3; 1846 -1.9; 2031 -2.6; 2234 -3.1; 2457 -4.0; 2703 -6.0; 2973 -7.8; 3270 -8.2; 3597 -8.4; 3957 -10.3; 4353 -14.7; 4788 -12.0; 5267 -3.2; 5793 2.0; 6373 2.5; 7010 2.4; 7711 0.3; 8482 -0.1; 9330 -1.0; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-29**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 11 Hz   | 0.87 | -10.2 dB |
| Peaking | 40 Hz   | 0.27 | -7.2 dB  |
| Peaking | 189 Hz  | 0.88 | -5.8 dB  |
| Peaking | 4519 Hz | 1.74 | -21.2 dB |
| Peaking | 5848 Hz | 1.83 | 13.2 dB  |
| Peaking | 360 Hz  | 2.44 | -1.4 dB  |
| Peaking | 735 Hz  | 1.61 | 2.3 dB   |
| Peaking | 1615 Hz | 2.66 | 0.4 dB   |
| Peaking | 2991 Hz | 4.18 | -2.5 dB  |
| Peaking | 3838 Hz | 6.83 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/MEE%20audio%20M6/MEE%20audio%20M6.png)