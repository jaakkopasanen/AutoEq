# Shure SE315

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.5; 106 4.7; 116 3.8; 128 3.0; 141 2.3; 155 1.7; 170 1.2; 187 0.9; 206 0.6; 227 0.4; 249 0.3; 274 0.0; 302 -0.1; 332 -0.0; 365 0.0; 402 0.2; 442 0.3; 486 0.5; 535 0.8; 588 1.0; 647 1.2; 712 1.4; 783 1.5; 861 1.4; 947 0.7; 1042 -0.6; 1146 -2.2; 1261 -3.3; 1387 -4.0; 1526 -4.1; 1678 -3.6; 1846 -2.3; 2031 -0.2; 2234 2.9; 2457 5.8; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 4.6; 4353 3.7; 4788 5.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE315 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 46 Hz    | 0.33 | 6.8 dB   |
| Peaking | 854 Hz   | 0.58 | 12.5 dB  |
| Peaking | 1541 Hz  | 0.4  | -23.5 dB |
| Peaking | 2711 Hz  | 0.68 | 19.6 dB  |
| Peaking | 5674 Hz  | 2.29 | 6.0 dB   |
| Peaking | 15 Hz    | 0.96 | 1.7 dB   |
| Peaking | 43 Hz    | 1.15 | -1.0 dB  |
| Peaking | 91 Hz    | 2.56 | 1.2 dB   |
| Peaking | 154 Hz   | 2.89 | -0.6 dB  |
| Peaking | 14076 Hz | 2.03 | 0.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SE315/Shure%20SE315.png)