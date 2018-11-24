# HiFiMAN HE-5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.3; 34 4.4; 37 3.7; 41 3.4; 45 3.0; 49 2.3; 54 1.7; 60 1.3; 66 1.2; 72 1.2; 79 1.1; 87 0.9; 96 0.7; 106 0.7; 116 0.4; 128 0.1; 141 -0.2; 155 -0.4; 170 -0.5; 187 -0.8; 206 -0.8; 227 -0.8; 249 -0.8; 274 -0.7; 302 -0.6; 332 -0.5; 365 -0.7; 402 -1.3; 442 -1.0; 486 -0.7; 535 -0.6; 588 -0.4; 647 -0.3; 712 0.2; 783 0.5; 861 0.1; 947 0.1; 1042 0.0; 1146 1.3; 1261 1.5; 1387 1.9; 1526 1.4; 1678 2.3; 1846 3.5; 2031 4.4; 2234 2.6; 2457 2.8; 2703 2.5; 2973 0.7; 3270 0.1; 3597 -0.1; 3957 -1.0; 4353 -3.4; 4788 -1.5; 5267 -0.0; 5793 -1.8; 6373 -3.8; 7010 -5.1; 7711 -5.6; 8482 -7.2; 9330 -8.9; 10263 -6.6; 11289 -2.6; 12418 -2.0; 13660 -1.8; 15026 -0.7; 16529 -3.0; 18182 -6.6; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.95 | 6.3 dB  |
| Peaking | 2043 Hz  | 1.74 | 4.0 dB  |
| Peaking | 4323 Hz  | 7.81 | -3.2 dB |
| Peaking | 8911 Hz  | 1.9  | -8.6 dB |
| Peaking | 18966 Hz | 1.7  | -7.6 dB |
| Peaking | 330 Hz   | 0.74 | -1.0 dB |
| Peaking | 1258 Hz  | 6.06 | 0.9 dB  |
| Peaking | 5230 Hz  | 8.78 | 1.6 dB  |
| Peaking | 6652 Hz  | 7.69 | -1.9 dB |
| Peaking | 14997 Hz | 5.22 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-5/HiFiMAN%20HE-5.png)