# KRK KNS 8400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 -7.6; 23 -7.5; 25 -7.3; 28 -7.0; 31 -6.7; 34 -6.3; 37 -5.8; 41 -5.0; 45 -4.3; 49 -3.4; 54 -2.3; 60 -1.2; 66 -1.0; 72 -2.0; 79 -4.1; 87 -6.5; 96 -8.4; 106 -10.4; 116 -11.1; 128 -9.3; 141 -9.9; 155 -9.5; 170 -9.4; 187 -9.4; 206 -7.8; 227 -6.2; 249 -4.5; 274 -3.1; 302 -1.9; 332 -0.4; 365 1.0; 402 2.3; 442 2.9; 486 2.7; 535 1.7; 588 0.4; 647 0.2; 712 0.5; 783 1.2; 861 -0.5; 947 -0.2; 1042 -0.2; 1146 -0.6; 1261 -1.0; 1387 -2.1; 1526 -2.9; 1678 -3.7; 1846 -4.6; 2031 -4.6; 2234 -5.3; 2457 -5.4; 2703 -5.3; 2973 -3.7; 3270 -3.8; 3597 -3.5; 3957 -4.3; 4353 -4.0; 4788 -1.4; 5267 -0.7; 5793 -1.3; 6373 -3.6; 7010 -1.6; 7711 -0.7; 8482 -5.0; 9330 -6.1; 10263 -0.2; 11289 0.0; 12418 0.0; 13660 -1.1; 15026 -1.6; 16529 -2.3; 18182 -5.5; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KRK KNS 8400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK KNS 8400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 1.13 | -7.8 dB  |
| Peaking | 112 Hz   | 2.15 | -9.7 dB  |
| Peaking | 183 Hz   | 2.33 | -8.1 dB  |
| Peaking | 2592 Hz  | 1.04 | -5.5 dB  |
| Peaking | 8927 Hz  | 6.02 | -6.9 dB  |
| Peaking | 64 Hz    | 3.8  | 2.9 dB   |
| Peaking | 101 Hz   | 0.24 | -0.7 dB  |
| Peaking | 450 Hz   | 2.25 | 4.2 dB   |
| Peaking | 3043 Hz  | 8.63 | 1.4 dB   |
| Peaking | 19941 Hz | 1.64 | -11.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/KRK%20KNS%208400/KRK%20KNS%208400.png)