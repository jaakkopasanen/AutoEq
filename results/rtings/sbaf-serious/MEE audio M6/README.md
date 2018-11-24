# MEE audio M6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 21 -10.1; 23 -10.0; 25 -9.9; 28 -9.8; 31 -9.6; 34 -9.4; 37 -9.2; 41 -9.0; 45 -8.7; 49 -8.5; 54 -8.3; 60 -8.3; 66 -8.2; 72 -8.0; 79 -7.8; 87 -7.7; 96 -7.8; 106 -7.9; 116 -8.1; 128 -8.3; 141 -8.3; 155 -8.2; 170 -8.0; 187 -7.8; 206 -7.5; 227 -7.1; 249 -6.4; 274 -5.6; 302 -4.9; 332 -4.2; 365 -3.4; 402 -2.5; 442 -1.6; 486 -0.6; 535 0.4; 588 0.9; 647 1.5; 712 1.8; 783 1.6; 861 1.0; 947 0.3; 1042 -0.1; 1146 -0.3; 1261 -0.4; 1387 -0.8; 1526 -1.3; 1678 -1.7; 1846 -1.8; 2031 -2.2; 2234 -2.6; 2457 -3.6; 2703 -5.4; 2973 -6.7; 3270 -6.3; 3597 -6.2; 3957 -9.1; 4353 -14.7; 4788 -12.1; 5267 -2.8; 5793 3.5; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 0.16 | -9.8 dB  |
| Peaking | 186 Hz  | 1.02 | -5.5 dB  |
| Peaking | 2893 Hz | 2.41 | -4.7 dB  |
| Peaking | 4497 Hz | 3.55 | -17.3 dB |
| Peaking | 6008 Hz | 3.13 | 9.2 dB   |
| Peaking | 122 Hz  | 2.96 | -0.6 dB  |
| Peaking | 181 Hz  | 3.09 | 0.9 dB   |
| Peaking | 322 Hz  | 1.48 | -1.3 dB  |
| Peaking | 667 Hz  | 1.6  | 2.8 dB   |
| Peaking | 1642 Hz | 2.76 | -0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/MEE%20audio%20M6/MEE%20audio%20M6.png)