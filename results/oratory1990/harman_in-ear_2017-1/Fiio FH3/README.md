# Fiio FH3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.7; 25 5.6; 28 5.6; 31 5.4; 34 5.1; 37 4.9; 41 4.5; 45 4.2; 49 3.7; 54 2.9; 60 2.1; 66 1.2; 72 0.7; 79 -0.3; 87 -0.8; 96 -1.2; 106 -2.1; 116 -2.4; 128 -3.3; 141 -3.5; 155 -3.9; 170 -4.3; 187 -4.7; 206 -4.9; 227 -4.9; 249 -4.8; 274 -4.5; 302 -4.0; 332 -3.4; 365 -2.9; 402 -2.5; 442 -2.1; 486 -1.6; 535 -1.2; 588 -0.8; 647 -0.5; 712 -0.2; 783 0.1; 861 0.3; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -1.1; 1387 -1.2; 1526 -0.9; 1678 -0.2; 1846 0.7; 2031 2.1; 2234 3.8; 2457 5.4; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.8; 5793 3.9; 6373 0.6; 7010 -0.8; 7711 -2.5; 8482 -3.1; 9330 -0.2; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -9.2; 15026 -18.0; 16529 -19.0; 18182 -17.2; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio FH3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio FH3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.42 | 6.2 dB   |
| Peaking | 187 Hz   | 0.48 | -5.4 dB  |
| Peaking | 7779 Hz  | 2.27 | -12.4 dB |
| Peaking | 8558 Hz  | 0.45 | 17.4 dB  |
| Peaking | 16444 Hz | 0.68 | -28.3 dB |
| Peaking | 1551 Hz  | 1.24 | -7.6 dB  |
| Peaking | 1993 Hz  | 0.54 | 5.4 dB   |
| Peaking | 12595 Hz | 5.89 | 5.7 dB   |
| Peaking | 15872 Hz | 0.11 | -1.6 dB  |
| Peaking | 19059 Hz | 5.14 | 0.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Fiio%20FH3/Fiio%20FH3.png)