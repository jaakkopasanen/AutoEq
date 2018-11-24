# HyperX Cloud II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.7; 23 -3.0; 25 -3.4; 28 -3.9; 31 -4.3; 34 -4.5; 37 -4.7; 41 -4.8; 45 -4.8; 49 -4.8; 54 -4.7; 60 -4.8; 66 -4.9; 72 -5.1; 79 -5.3; 87 -5.7; 96 -6.0; 106 -6.4; 116 -6.7; 128 -6.8; 141 -6.5; 155 -6.3; 170 -6.0; 187 -5.3; 206 -4.5; 227 -3.7; 249 -3.0; 274 -2.6; 302 -2.5; 332 -2.6; 365 -2.7; 402 -2.7; 442 -2.6; 486 -2.7; 535 -2.8; 588 -2.7; 647 -2.5; 712 -2.2; 783 -1.8; 861 -1.5; 947 -0.5; 1042 0.2; 1146 -0.2; 1261 -0.8; 1387 -1.4; 1526 -2.1; 1678 -3.2; 1846 -4.2; 2031 -5.4; 2234 -5.4; 2457 -4.1; 2703 -2.7; 2973 -1.7; 3270 -0.8; 3597 2.4; 3957 6.0; 4353 5.5; 4788 -1.7; 5267 -0.6; 5793 -0.5; 6373 -3.6; 7010 -4.8; 7711 -5.5; 8482 -9.0; 9330 -11.4; 10263 -7.1; 11289 -0.5; 12418 -0.1; 13660 -4.0; 15026 -6.1; 16529 -3.8; 18182 -2.8; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 95 Hz    | 0.3  | -6.0 dB  |
| Peaking | 2160 Hz  | 1.99 | -5.5 dB  |
| Peaking | 4010 Hz  | 5.43 | 8.4 dB   |
| Peaking | 8984 Hz  | 2.83 | -11.4 dB |
| Peaking | 15561 Hz | 2.29 | -5.7 dB  |
| Peaking | 152 Hz   | 1.08 | -4.4 dB  |
| Peaking | 213 Hz   | 0.49 | 4.3 dB   |
| Peaking | 542 Hz   | 0.66 | -2.8 dB  |
| Peaking | 1067 Hz  | 2.78 | 2.1 dB   |
| Peaking | 11812 Hz | 6.65 | 3.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/HyperX%20Cloud%20II/HyperX%20Cloud%20II.png)