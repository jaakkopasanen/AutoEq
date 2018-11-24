# Beats Studio Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.2; 25 2.3; 28 1.1; 31 0.3; 34 -0.2; 37 -0.5; 41 -0.7; 45 -0.9; 49 -1.0; 54 -1.2; 60 -1.5; 66 -1.8; 72 -2.1; 79 -2.3; 87 -2.6; 96 -2.8; 106 -3.0; 116 -3.0; 128 -2.9; 141 -2.6; 155 -2.4; 170 -2.1; 187 -1.6; 206 -1.0; 227 -0.2; 249 0.5; 274 1.5; 302 2.7; 332 4.2; 365 5.9; 402 6.0; 442 6.0; 486 3.9; 535 1.2; 588 0.6; 647 0.4; 712 -0.2; 783 -0.7; 861 -0.6; 947 -0.1; 1042 -0.1; 1146 -0.7; 1261 -1.2; 1387 -1.0; 1526 -0.5; 1678 -0.5; 1846 -0.3; 2031 0.6; 2234 1.9; 2457 3.1; 2703 3.9; 2973 3.1; 3270 1.3; 3597 0.6; 3957 0.5; 4353 2.7; 4788 6.0; 5267 6.0; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.2; 9330 -3.8; 10263 -5.9; 11289 -4.7; 12418 -2.1; 13660 -0.1; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Studio Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 3.62 | 4.3 dB  |
| Peaking | 398 Hz   | 3.07 | 7.1 dB  |
| Peaking | 5618 Hz  | 1.31 | 4.5 dB  |
| Peaking | 5630 Hz  | 2.4  | 2.3 dB  |
| Peaking | 10300 Hz | 2.44 | -7.2 dB |
| Peaking | 108 Hz   | 1.02 | -3.3 dB |
| Peaking | 1324 Hz  | 1.5  | -1.4 dB |
| Peaking | 1916 Hz  | 3.02 | -1.3 dB |
| Peaking | 2671 Hz  | 1.71 | 3.9 dB  |
| Peaking | 3673 Hz  | 3.37 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Beats%20Studio%20Wireless/Beats%20Studio%20Wireless.png)