# Superlux HD 668B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 0.0; 23 4.2; 25 3.4; 28 2.4; 31 1.5; 34 0.6; 37 -0.1; 41 -0.9; 45 -1.6; 49 -2.0; 54 -2.5; 60 -3.0; 66 -3.5; 72 -3.9; 79 -4.3; 87 -4.7; 96 -4.9; 106 -5.0; 116 -5.0; 128 -4.8; 141 -4.4; 155 -3.9; 170 -3.2; 187 -2.6; 206 -2.3; 227 -2.2; 249 -2.2; 274 -2.2; 302 -2.3; 332 -2.3; 365 -1.9; 402 -1.9; 442 -2.0; 486 -1.8; 535 -0.9; 588 -1.1; 647 -1.1; 712 -0.9; 783 -0.7; 861 -0.3; 947 -0.2; 1042 0.1; 1146 0.2; 1261 0.0; 1387 -0.3; 1526 -1.1; 1678 -2.5; 1846 -4.3; 2031 -5.6; 2234 -5.2; 2457 -4.3; 2703 -3.1; 2973 -2.2; 3270 -1.9; 3597 -0.2; 3957 1.4; 4353 3.0; 4788 3.3; 5267 -4.1; 5793 -5.4; 6373 -3.8; 7010 -3.2; 7711 -4.4; 8482 -7.4; 9330 -10.3; 10263 -10.2; 11289 -7.1; 12418 -2.6; 13660 -2.0; 15026 -5.6; 16529 -4.7; 18182 -0.3; 20000 -1.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 668B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 668B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.5  | 7.4 dB   |
| Peaking | 85 Hz    | 0.4  | -5.4 dB  |
| Peaking | 2129 Hz  | 2.91 | -5.9 dB  |
| Peaking | 9701 Hz  | 1.81 | -10.6 dB |
| Peaking | 23522 Hz | 0.33 | -9.3 dB  |
| Peaking | 200 Hz   | 5.17 | 1.0 dB   |
| Peaking | 3133 Hz  | 2.5  | -2.1 dB  |
| Peaking | 4800 Hz  | 2.31 | 9.0 dB   |
| Peaking | 5512 Hz  | 4.41 | -11.0 dB |
| Peaking | 15711 Hz | 4.17 | -5.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Superlux%20HD%20668B/Superlux%20HD%20668B.png)