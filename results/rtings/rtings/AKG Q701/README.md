# AKG Q701

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.5; 28 4.9; 31 4.4; 34 4.0; 37 3.6; 41 3.3; 45 3.0; 49 2.7; 54 2.4; 60 2.1; 66 1.7; 72 1.4; 79 0.9; 87 0.4; 96 -0.0; 106 -0.5; 116 -0.9; 128 -1.4; 141 -1.7; 155 -2.0; 170 -2.1; 187 -2.3; 206 -2.3; 227 -2.2; 249 -2.3; 274 -2.3; 302 -2.3; 332 -2.3; 365 -2.4; 402 -2.4; 442 -2.3; 486 -1.9; 535 -1.3; 588 -0.7; 647 -0.8; 712 -0.5; 783 -0.1; 861 0.0; 947 -0.1; 1042 0.0; 1146 -0.1; 1261 -0.5; 1387 -0.9; 1526 -1.8; 1678 -3.3; 1846 -4.8; 2031 -5.9; 2234 -6.4; 2457 -5.3; 2703 -4.2; 2973 -2.6; 3270 -1.0; 3597 -1.2; 3957 -1.6; 4353 -1.8; 4788 -1.1; 5267 -0.7; 5793 -2.3; 6373 -6.6; 7010 -6.6; 7711 -5.6; 8482 -6.5; 9330 -5.1; 10263 -1.4; 11289 -0.6; 12418 -0.0; 13660 0.0; 15026 0.0; 16529 -0.1; 18182 -3.3; 20000 -0.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.28 | 6.6 dB  |
| Peaking | 223 Hz   | 0.62 | -2.8 dB |
| Peaking | 2180 Hz  | 2.42 | -6.6 dB |
| Peaking | 7597 Hz  | 1.94 | -7.0 dB |
| Peaking | 18684 Hz | 3.14 | -3.8 dB |
| Peaking | 990 Hz   | 1.54 | 1.3 dB  |
| Peaking | 5248 Hz  | 7.73 | 2.0 dB  |
| Peaking | 5870 Hz  | 0.07 | -0.4 dB |
| Peaking | 9128 Hz  | 8.03 | -2.7 dB |
| Peaking | 11899 Hz | 1.02 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/AKG%20Q701/AKG%20Q701.png)