# AKG Y50BT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.5; 28 4.9; 31 4.2; 34 3.6; 37 3.2; 41 2.7; 45 2.3; 49 2.1; 54 1.9; 60 1.6; 66 1.4; 72 1.2; 79 1.1; 87 0.9; 96 0.7; 106 0.7; 116 0.9; 128 1.4; 141 2.4; 155 3.7; 170 5.3; 187 5.9; 206 4.9; 227 3.2; 249 2.0; 274 0.9; 302 -0.3; 332 -1.2; 365 -1.2; 402 -0.7; 442 -0.2; 486 0.0; 535 0.0; 588 -0.1; 647 -0.4; 712 -0.8; 783 -1.3; 861 -1.8; 947 -1.6; 1042 -0.4; 1146 -2.1; 1261 -3.0; 1387 -3.0; 1526 -2.8; 1678 -2.0; 1846 -0.6; 2031 0.6; 2234 2.0; 2457 4.0; 2703 5.2; 2973 3.6; 3270 -0.2; 3597 1.4; 3957 2.3; 4353 0.7; 4788 -0.7; 5267 -2.1; 5793 -2.4; 6373 -1.3; 7010 0.8; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.3; 13660 -3.2; 15026 -4.8; 16529 -5.2; 18182 -4.4; 20000 -3.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Y50BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Y50BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.74 | 6.0 dB  |
| Peaking | 185 Hz   | 2.81 | 6.2 dB  |
| Peaking | 1413 Hz  | 1.2  | -3.2 dB |
| Peaking | 2609 Hz  | 2.89 | 6.1 dB  |
| Peaking | 16974 Hz | 1.16 | -5.7 dB |
| Peaking | 318 Hz   | 1.41 | 1.7 dB  |
| Peaking | 337 Hz   | 2.66 | -3.4 dB |
| Peaking | 3926 Hz  | 9.63 | 2.4 dB  |
| Peaking | 5621 Hz  | 3.42 | -3.3 dB |
| Peaking | 7954 Hz  | 1.17 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20Y50BT/AKG%20Y50BT.png)