# MEE audio M6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 21 -10.5; 23 -10.4; 25 -10.2; 28 -9.9; 31 -9.6; 34 -9.4; 37 -9.1; 41 -8.8; 45 -8.5; 49 -8.2; 54 -8.0; 60 -8.0; 66 -8.0; 72 -8.0; 79 -8.0; 87 -8.1; 96 -8.2; 106 -8.4; 116 -8.6; 128 -8.8; 141 -8.9; 155 -8.8; 170 -8.6; 187 -8.4; 206 -8.0; 227 -7.6; 249 -6.9; 274 -6.3; 302 -5.7; 332 -5.1; 365 -4.4; 402 -3.6; 442 -2.7; 486 -1.8; 535 -0.8; 588 -0.2; 647 0.5; 712 0.9; 783 1.1; 861 0.8; 947 0.3; 1042 -0.1; 1146 -0.5; 1261 -0.6; 1387 -0.8; 1526 -1.0; 1678 -1.3; 1846 -1.9; 2031 -2.6; 2234 -3.1; 2457 -4.1; 2703 -6.2; 2973 -8.3; 3270 -8.9; 3597 -9.4; 3957 -11.5; 4353 -16.0; 4788 -13.7; 5267 -5.8; 5793 -0.4; 6373 1.3; 7010 2.2; 7711 0.3; 8482 -0.5; 9330 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 11 Hz   | 0.9  | -10.2 dB |
| Peaking | 38 Hz   | 0.26 | -7.3 dB  |
| Peaking | 187 Hz  | 0.89 | -5.8 dB  |
| Peaking | 4481 Hz | 1.76 | -21.1 dB |
| Peaking | 6107 Hz | 1.69 | 10.5 dB  |
| Peaking | 357 Hz  | 2.36 | -1.4 dB  |
| Peaking | 734 Hz  | 1.64 | 2.3 dB   |
| Peaking | 1785 Hz | 1.42 | 0.5 dB   |
| Peaking | 2972 Hz | 4.21 | -2.6 dB  |
| Peaking | 3837 Hz | 6.99 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20M6/MEE%20audio%20M6.png)