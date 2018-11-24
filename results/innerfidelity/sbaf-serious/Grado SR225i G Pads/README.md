# Grado SR225i G Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.6; 37 4.9; 41 3.8; 45 3.2; 49 2.7; 54 1.6; 60 0.2; 66 -0.8; 72 -1.4; 79 -2.0; 87 -2.5; 96 -3.0; 106 -3.3; 116 -3.3; 128 -3.3; 141 -3.3; 155 -3.2; 170 -2.9; 187 -2.6; 206 -2.4; 227 -2.0; 249 -1.7; 274 -1.3; 302 -1.2; 332 -0.9; 365 -0.7; 402 -0.8; 442 -0.4; 486 -0.4; 535 -0.4; 588 -0.2; 647 -0.0; 712 -0.1; 783 0.2; 861 -0.0; 947 -0.1; 1042 -0.1; 1146 -0.4; 1261 -0.9; 1387 -1.5; 1526 -1.6; 1678 -2.0; 1846 -1.6; 2031 -1.9; 2234 -1.4; 2457 -1.9; 2703 -2.2; 2973 -3.1; 3270 -2.8; 3597 -4.8; 3957 -4.4; 4353 -3.2; 4788 -4.6; 5267 -8.1; 5793 -9.4; 6373 -10.5; 7010 -8.7; 7711 -7.6; 8482 -9.0; 9330 -10.2; 10263 -6.5; 11289 -0.8; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i G Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i G Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.57 | 7.2 dB   |
| Peaking | 101 Hz   | 0.6  | -4.9 dB  |
| Peaking | 5940 Hz  | 3.9  | -1.8 dB  |
| Peaking | 6984 Hz  | 0.93 | -9.1 dB  |
| Peaking | 24000 Hz | 2.21 | -7.9 dB  |
| Peaking | 1626 Hz  | 3.63 | -1.3 dB  |
| Peaking | 4557 Hz  | 5.03 | 4.8 dB   |
| Peaking | 4602 Hz  | 1.41 | -3.4 dB  |
| Peaking | 9534 Hz  | 3.29 | -10.0 dB |
| Peaking | 9978 Hz  | 0.98 | 6.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20G%20Pads/Grado%20SR225i%20G%20Pads.png)