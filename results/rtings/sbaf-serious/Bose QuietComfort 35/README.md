# Bose QuietComfort 35

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 21 -5.6; 23 -5.1; 25 -4.9; 28 -4.8; 31 -4.9; 34 -5.1; 37 -5.2; 41 -5.4; 45 -5.6; 49 -5.6; 54 -5.6; 60 -5.4; 66 -5.3; 72 -5.1; 79 -4.8; 87 -4.6; 96 -4.5; 106 -4.4; 116 -4.4; 128 -4.3; 141 -4.2; 155 -4.0; 170 -3.8; 187 -3.7; 206 -3.6; 227 -3.4; 249 -3.1; 274 -2.9; 302 -2.5; 332 -2.3; 365 -2.0; 402 -1.8; 442 -1.7; 486 -1.5; 535 -1.3; 588 -1.0; 647 -0.7; 712 -0.5; 783 -0.4; 861 -0.3; 947 -0.1; 1042 0.2; 1146 0.4; 1261 -0.1; 1387 -1.9; 1526 -3.9; 1678 -6.0; 1846 -7.7; 2031 -7.6; 2234 -5.6; 2457 -4.5; 2703 -5.1; 2973 -4.3; 3270 -1.8; 3597 -1.5; 3957 -3.2; 4353 -3.2; 4788 -0.9; 5267 3.4; 5793 -0.7; 6373 -4.7; 7010 -0.2; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -0.6; 15026 -0.8; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.31 | -3.8 dB |
| Peaking | 86 Hz    | 0.29 | -4.3 dB |
| Peaking | 1880 Hz  | 3.42 | -6.9 dB |
| Peaking | 2734 Hz  | 1.67 | -3.7 dB |
| Peaking | 21661 Hz | 2.07 | -1.0 dB |
| Peaking | 1125 Hz  | 4.02 | 1.7 dB  |
| Peaking | 3424 Hz  | 7.65 | 2.7 dB  |
| Peaking | 4272 Hz  | 2.89 | -3.1 dB |
| Peaking | 5323 Hz  | 5.38 | 5.9 dB  |
| Peaking | 6229 Hz  | 7.81 | -5.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bose%20QuietComfort%2035/Bose%20QuietComfort%2035.png)