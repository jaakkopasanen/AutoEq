# Etymotic hf5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.8; 106 4.9; 116 4.0; 128 3.1; 141 2.3; 155 1.6; 170 1.1; 187 0.6; 206 0.2; 227 -0.1; 249 -0.1; 274 -0.2; 302 -0.3; 332 -0.3; 365 -0.4; 402 -0.4; 442 -0.3; 486 -0.3; 535 -0.1; 588 0.1; 647 0.4; 712 0.7; 783 0.8; 861 0.7; 947 0.4; 1042 -0.3; 1146 -1.1; 1261 -1.9; 1387 -2.5; 1526 -2.9; 1678 -3.4; 1846 -3.8; 2031 -4.0; 2234 -3.4; 2457 -2.3; 2703 -1.7; 2973 -1.6; 3270 -1.7; 3597 -2.2; 3957 -2.9; 4353 -3.0; 4788 -2.1; 5267 -0.1; 5793 2.6; 6373 4.0; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.1; 15026 -2.4; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic hf5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.46 | 6.9 dB  |
| Peaking | 1873 Hz  | 1.71 | -4.0 dB |
| Peaking | 4301 Hz  | 2.45 | -3.2 dB |
| Peaking | 6302 Hz  | 3.92 | 5.1 dB  |
| Peaking | 14969 Hz | 6.19 | -2.6 dB |
| Peaking | 17 Hz    | 1.04 | 2.4 dB  |
| Peaking | 40 Hz    | 0.95 | -1.4 dB |
| Peaking | 95 Hz    | 1.55 | 2.6 dB  |
| Peaking | 196 Hz   | 0.48 | -1.4 dB |
| Peaking | 781 Hz   | 2.47 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Etymotic%20hf5/Etymotic%20hf5.png)