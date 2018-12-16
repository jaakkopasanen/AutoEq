# Sony XBA-H3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 0.0; 23 0.5; 25 0.3; 28 0.1; 31 -0.1; 34 -0.2; 37 -0.3; 41 -0.5; 45 -0.7; 49 -0.8; 54 -1.0; 60 -1.3; 66 -1.5; 72 -1.8; 79 -2.1; 87 -2.5; 96 -2.8; 106 -3.1; 116 -3.3; 128 -3.4; 141 -3.5; 155 -3.5; 170 -3.4; 187 -3.2; 206 -3.0; 227 -2.7; 249 -2.3; 274 -1.9; 302 -1.5; 332 -1.2; 365 -1.0; 402 -0.7; 442 -0.4; 486 -0.2; 535 0.0; 588 0.2; 647 0.4; 712 0.5; 783 0.6; 861 0.3; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -1.1; 1387 -1.3; 1526 -1.1; 1678 -0.7; 1846 0.0; 2031 1.3; 2234 3.2; 2457 5.0; 2703 5.6; 2973 3.5; 3270 0.9; 3597 -0.2; 3957 -0.1; 4353 -1.8; 4788 -4.0; 5267 -3.0; 5793 0.6; 6373 3.0; 7010 2.4; 7711 -0.0; 8482 -2.7; 9330 -5.2; 10263 -5.9; 11289 -4.1; 12418 -2.3; 13660 -1.4; 15026 -0.2; 16529 -1.6; 18182 -3.9; 20000 -0.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-H3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-H3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 142 Hz   | 0.75 | -3.7 dB |
| Peaking | 2612 Hz  | 3.88 | 6.3 dB  |
| Peaking | 4817 Hz  | 6.92 | -4.7 dB |
| Peaking | 10200 Hz | 3.35 | -6.6 dB |
| Peaking | 18362 Hz | 2.3  | -4.1 dB |
| Peaking | 19 Hz    | 1.46 | 0.8 dB  |
| Peaking | 723 Hz   | 1.68 | 0.9 dB  |
| Peaking | 1404 Hz  | 2.93 | -1.7 dB |
| Peaking | 6677 Hz  | 3.42 | 6.8 dB  |
| Peaking | 6731 Hz  | 1.3  | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20XBA-H3/Sony%20XBA-H3.png)