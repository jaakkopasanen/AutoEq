# Sony IER-M7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.6; 60 4.9; 66 4.3; 72 3.6; 79 2.8; 87 2.1; 96 1.3; 106 0.6; 116 -0.2; 128 -0.8; 141 -1.4; 155 -2.0; 170 -2.4; 187 -2.8; 206 -3.1; 227 -3.3; 249 -3.3; 274 -3.1; 302 -2.8; 332 -2.5; 365 -2.1; 402 -1.9; 442 -1.7; 486 -1.3; 535 -1.0; 588 -0.7; 647 -0.4; 712 -0.1; 783 0.2; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.4; 1387 -0.2; 1526 0.2; 1678 0.7; 1846 1.2; 2031 1.9; 2234 2.7; 2457 3.6; 2703 4.8; 2973 5.5; 3270 4.7; 3597 3.9; 3957 5.1; 4353 5.1; 4788 4.5; 5267 5.6; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -2.3; 10263 -4.3; 11289 -6.0; 12418 -7.0; 13660 -9.0; 15026 -14.3; 16529 -19.4; 18182 -18.0; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.4  | 6.7 dB   |
| Peaking | 199 Hz   | 0.66 | -4.4 dB  |
| Peaking | 2902 Hz  | 1.91 | 4.4 dB   |
| Peaking | 5754 Hz  | 1.33 | 7.3 dB   |
| Peaking | 17143 Hz | 0.93 | -21.0 dB |
| Peaking | 852 Hz   | 1.88 | 1.4 dB   |
| Peaking | 1253 Hz  | 0.95 | -1.4 dB  |
| Peaking | 1875 Hz  | 1.36 | 0.7 dB   |
| Peaking | 18931 Hz | 3.94 | -2.0 dB  |
| Peaking | 20493 Hz | 2.07 | 2.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20IER-M7/Sony%20IER-M7.png)