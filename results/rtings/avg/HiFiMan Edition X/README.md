# HiFiMan Edition X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.7; 28 5.2; 31 4.7; 34 4.3; 37 4.0; 41 3.6; 45 3.3; 49 3.1; 54 2.8; 60 2.6; 66 2.3; 72 2.1; 79 2.0; 87 1.8; 96 1.5; 106 1.2; 116 1.0; 128 0.6; 141 0.4; 155 0.1; 170 -0.1; 187 -0.3; 206 -0.3; 227 0.3; 249 0.1; 274 -0.0; 302 0.3; 332 0.5; 365 1.1; 402 0.4; 442 -0.3; 486 -0.5; 535 -0.5; 588 -0.7; 647 -1.1; 712 0.8; 783 2.6; 861 1.0; 947 0.6; 1042 1.0; 1146 4.7; 1261 2.4; 1387 2.5; 1526 3.9; 1678 2.0; 1846 1.6; 2031 0.5; 2234 0.9; 2457 0.3; 2703 0.4; 2973 -0.7; 3270 0.1; 3597 0.4; 3957 0.5; 4353 0.1; 4788 1.0; 5267 3.1; 5793 3.5; 6373 0.1; 7010 -0.3; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.0; 18182 -6.5; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Edition X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Edition X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.64 | 5.9 dB   |
| Peaking | 72 Hz    | 1.48 | 1.0 dB   |
| Peaking | 1138 Hz  | 7.96 | 4.1 dB   |
| Peaking | 1517 Hz  | 3.57 | 3.4 dB   |
| Peaking | 5522 Hz  | 6.43 | 4.3 dB   |
| Peaking | 185 Hz   | 4.29 | -0.7 dB  |
| Peaking | 366 Hz   | 6.62 | 1.2 dB   |
| Peaking | 698 Hz   | 2.59 | -2.8 dB  |
| Peaking | 756 Hz   | 5.87 | 5.1 dB   |
| Peaking | 19476 Hz | 1.92 | -10.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20Edition%20X/HiFiMan%20Edition%20X.png)