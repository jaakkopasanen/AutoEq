# Sony IER-M9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -2.2; 23 -2.3; 25 -2.4; 28 -2.6; 31 -2.7; 34 -2.8; 37 -2.9; 41 -3.0; 45 -3.1; 49 -3.2; 54 -3.3; 60 -3.5; 66 -3.6; 72 -3.8; 79 -4.0; 87 -4.2; 96 -4.3; 106 -4.5; 116 -4.6; 128 -4.6; 141 -4.6; 155 -4.6; 170 -4.5; 187 -4.3; 206 -4.1; 227 -3.9; 249 -3.6; 274 -3.4; 302 -3.0; 332 -2.7; 365 -2.4; 402 -2.1; 442 -1.8; 486 -1.5; 535 -1.1; 588 -0.8; 647 -0.5; 712 -0.2; 783 0.1; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.4; 1261 -0.4; 1387 -0.1; 1526 0.3; 1678 0.8; 1846 1.2; 2031 2.1; 2234 3.3; 2457 4.9; 2703 5.9; 2973 4.6; 3270 2.1; 3597 1.9; 3957 3.1; 4353 2.6; 4788 2.6; 5267 4.5; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -3.9; 10263 -7.5; 11289 -7.5; 12418 -6.4; 13660 -11.4; 15026 -21.7; 16529 -26.5; 18182 -20.8; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 111 Hz   | 0.33 | -4.6 dB  |
| Peaking | 2638 Hz  | 2.52 | 5.8 dB   |
| Peaking | 6018 Hz  | 2.06 | 7.6 dB   |
| Peaking | 16114 Hz | 1.39 | -22.8 dB |
| Peaking | 18037 Hz | 1.63 | -10.0 dB |
| Peaking | 25 Hz    | 1.75 | -1.1 dB  |
| Peaking | 776 Hz   | 3.2  | 0.9 dB   |
| Peaking | 8622 Hz  | 6.01 | 2.7 dB   |
| Peaking | 10277 Hz | 2.68 | -3.4 dB  |
| Peaking | 12576 Hz | 4.95 | 4.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20IER-M9/Sony%20IER-M9.png)