# Google Pixel Buds

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.5; 49 4.2; 54 2.5; 60 0.9; 66 -0.4; 72 -1.4; 79 -2.4; 87 -3.4; 96 -4.3; 106 -5.1; 116 -5.8; 128 -6.3; 141 -6.6; 155 -6.8; 170 -6.8; 187 -6.7; 206 -6.5; 227 -6.2; 249 -5.8; 274 -5.3; 302 -4.7; 332 -4.0; 365 -3.4; 402 -3.1; 442 -3.0; 486 -2.9; 535 -2.8; 588 -2.7; 647 -2.4; 712 -2.0; 783 -1.6; 861 -1.0; 947 -0.4; 1042 0.3; 1146 1.2; 1261 2.2; 1387 3.0; 1526 3.7; 1678 4.2; 1846 4.3; 2031 4.1; 2234 3.6; 2457 2.0; 2703 0.3; 2973 -1.4; 3270 -2.4; 3597 -2.6; 3957 -2.3; 4353 -2.0; 4788 -1.3; 5267 -0.8; 5793 -0.0; 6373 0.1; 7010 1.0; 7711 -0.2; 8482 -2.1; 9330 -1.8; 10263 -0.0; 11289 0.0; 12418 -0.6; 13660 -2.0; 15026 -2.5; 16529 -1.6; 18182 -0.1; 20000 -0.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Google Pixel Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Google Pixel Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.52 | 11.3 dB |
| Peaking | 114 Hz   | 0.35 | -9.8 dB |
| Peaking | 1866 Hz  | 1.34 | 5.6 dB  |
| Peaking | 3456 Hz  | 1.81 | -4.0 dB |
| Peaking | 14939 Hz | 2.01 | -2.6 dB |
| Peaking | 390 Hz   | 1.55 | 1.9 dB  |
| Peaking | 528 Hz   | 0.72 | -1.4 dB |
| Peaking | 1281 Hz  | 3.18 | 0.9 dB  |
| Peaking | 6910 Hz  | 4.84 | 1.5 dB  |
| Peaking | 8643 Hz  | 6.02 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Google%20Pixel%20Buds/Google%20Pixel%20Buds.png)