# Sony IER-M9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.8; 49 5.4; 54 4.8; 60 4.1; 66 3.5; 72 2.8; 79 2.0; 87 1.3; 96 0.6; 106 -0.1; 116 -0.9; 128 -1.5; 141 -2.0; 155 -2.5; 170 -3.0; 187 -3.3; 206 -3.6; 227 -3.6; 249 -3.6; 274 -3.4; 302 -3.0; 332 -2.7; 365 -2.4; 402 -2.1; 442 -1.8; 486 -1.5; 535 -1.1; 588 -0.8; 647 -0.5; 712 -0.2; 783 0.1; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.4; 1261 -0.4; 1387 -0.1; 1526 0.3; 1678 0.8; 1846 1.2; 2031 2.1; 2234 3.3; 2457 4.9; 2703 5.9; 2973 4.6; 3270 2.1; 3597 1.9; 3957 3.1; 4353 2.6; 4788 2.6; 5267 4.5; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -3.9; 10263 -7.5; 11289 -7.5; 12418 -6.4; 13660 -11.4; 15026 -21.7; 16529 -26.5; 18182 -20.8; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 1.07 | 7.2 dB   |
| Peaking | 2649 Hz  | 2.85 | 5.9 dB   |
| Peaking | 6006 Hz  | 2.05 | 7.6 dB   |
| Peaking | 16106 Hz | 1.38 | -22.6 dB |
| Peaking | 18027 Hz | 1.62 | -10.1 dB |
| Peaking | 31 Hz    | 0.44 | 4.6 dB   |
| Peaking | 32 Hz    | 1.57 | -5.8 dB  |
| Peaking | 206 Hz   | 0.71 | -4.3 dB  |
| Peaking | 10395 Hz | 6.17 | -3.4 dB  |
| Peaking | 12670 Hz | 5.88 | 3.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20IER-M9/Sony%20IER-M9.png)