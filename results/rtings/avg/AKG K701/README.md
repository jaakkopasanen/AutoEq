# AKG K701

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.6; 31 5.2; 34 4.8; 37 4.5; 41 4.2; 45 3.9; 49 3.6; 54 3.3; 60 3.0; 66 2.6; 72 2.3; 79 1.9; 87 1.5; 96 1.1; 106 0.6; 116 0.2; 128 -0.2; 141 -0.6; 155 -0.8; 170 -1.0; 187 -1.1; 206 -1.1; 227 -1.1; 249 -1.0; 274 -1.2; 302 -1.2; 332 -1.2; 365 -1.2; 402 -1.3; 442 -1.3; 486 -1.1; 535 -0.4; 588 0.4; 647 0.4; 712 0.9; 783 0.9; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.6; 1261 -0.9; 1387 -1.4; 1526 -1.9; 1678 -3.2; 1846 -5.0; 2031 -6.0; 2234 -6.9; 2457 -6.3; 2703 -5.5; 2973 -4.5; 3270 -3.7; 3597 -2.9; 3957 -2.8; 4353 -2.7; 4788 -2.8; 5267 -3.7; 5793 -5.2; 6373 -7.3; 7010 -7.8; 7711 -7.8; 8482 -7.9; 9330 -5.0; 10263 -2.8; 11289 -5.3; 12418 -5.3; 13660 -0.8; 15026 -0.0; 16529 -3.6; 18182 -8.8; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.71 | 6.0 dB  |
| Peaking | 2278 Hz  | 1.89 | -6.7 dB |
| Peaking | 7607 Hz  | 1.27 | -8.0 dB |
| Peaking | 18009 Hz | 3.06 | -5.0 dB |
| Peaking | 19553 Hz | 1.93 | -7.8 dB |
| Peaking | 461 Hz   | 0.48 | -2.2 dB |
| Peaking | 737 Hz   | 1.18 | 3.0 dB  |
| Peaking | 11630 Hz | 6.83 | -4.3 dB |
| Peaking | 12629 Hz | 4.92 | -5.4 dB |
| Peaking | 12844 Hz | 1.8  | 4.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K701/AKG%20K701.png)