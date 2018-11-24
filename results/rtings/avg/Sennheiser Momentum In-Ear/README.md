# Sennheiser Momentum In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.8dB
GraphicEQ: 21 -1.9; 23 -1.9; 25 -2.0; 28 -2.1; 31 -2.2; 34 -2.3; 37 -2.4; 41 -2.5; 45 -2.7; 49 -2.8; 54 -3.0; 60 -3.5; 66 -4.0; 72 -4.4; 79 -4.8; 87 -5.4; 96 -5.9; 106 -6.5; 116 -7.1; 128 -7.6; 141 -8.0; 155 -8.2; 170 -8.3; 187 -8.2; 206 -8.0; 227 -7.9; 249 -7.7; 274 -7.3; 302 -6.8; 332 -6.2; 365 -5.5; 402 -4.9; 442 -4.2; 486 -3.4; 535 -2.5; 588 -1.6; 647 -0.6; 712 0.3; 783 0.7; 861 0.8; 947 0.4; 1042 -0.3; 1146 -0.8; 1261 -0.9; 1387 -0.9; 1526 -0.8; 1678 -0.8; 1846 -0.7; 2031 -0.4; 2234 0.8; 2457 2.5; 2703 3.4; 2973 3.5; 3270 3.1; 3597 2.4; 3957 1.7; 4353 0.8; 4788 0.6; 5267 0.1; 5793 -1.4; 6373 -5.5; 7010 -7.1; 7711 -4.1; 8482 -3.1; 9330 -6.5; 10263 -9.0; 11289 -8.1; 12418 -8.2; 13660 -7.4; 15026 -1.5; 16529 0.0; 18182 0.0; 20000 -1.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 138 Hz   | 0.57 | -7.1 dB |
| Peaking | 285 Hz   | 1.22 | -3.5 dB |
| Peaking | 3142 Hz  | 1.92 | 4.1 dB  |
| Peaking | 6790 Hz  | 6.07 | -6.3 dB |
| Peaking | 11384 Hz | 1.49 | -9.4 dB |
| Peaking | 24 Hz    | 1.4  | -1.4 dB |
| Peaking | 803 Hz   | 2.99 | 2.2 dB  |
| Peaking | 1730 Hz  | 1.24 | -1.3 dB |
| Peaking | 2553 Hz  | 4.63 | 1.5 dB  |
| Peaking | 16092 Hz | 4.8  | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)