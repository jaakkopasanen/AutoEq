# Sennheiser Momentum In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 -1.5; 23 -1.6; 25 -1.8; 28 -2.0; 31 -2.2; 34 -2.4; 37 -2.5; 41 -2.7; 45 -2.9; 49 -3.1; 54 -3.4; 60 -3.8; 66 -4.2; 72 -4.4; 79 -4.6; 87 -5.0; 96 -5.5; 106 -6.1; 116 -6.6; 128 -7.1; 141 -7.5; 155 -7.6; 170 -7.6; 187 -7.6; 206 -7.5; 227 -7.4; 249 -7.1; 274 -6.6; 302 -5.9; 332 -5.2; 365 -4.5; 402 -3.9; 442 -3.1; 486 -2.2; 535 -1.3; 588 -0.5; 647 0.5; 712 1.2; 783 1.2; 861 1.0; 947 0.4; 1042 -0.2; 1146 -0.6; 1261 -0.6; 1387 -0.9; 1526 -1.2; 1678 -1.1; 1846 -0.6; 2031 0.1; 2234 1.3; 2457 2.9; 2703 4.2; 2973 5.1; 3270 5.7; 3597 5.6; 3957 4.1; 4353 2.2; 4788 2.3; 5267 3.1; 5793 2.5; 6373 -1.7; 7010 -3.9; 7711 -2.5; 8482 -3.6; 9330 -7.7; 10263 -7.8; 11289 -2.8; 12418 -0.4; 13660 -0.4; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 106 Hz  | 0.5  | -4.8 dB |
| Peaking | 227 Hz  | 1    | -5.0 dB |
| Peaking | 3300 Hz | 2.26 | 6.4 dB  |
| Peaking | 5398 Hz | 6.89 | 3.2 dB  |
| Peaking | 9663 Hz | 2.7  | -8.6 dB |
| Peaking | 776 Hz  | 1.43 | 4.2 dB  |
| Peaking | 1212 Hz | 0.42 | -2.6 dB |
| Peaking | 2532 Hz | 4.22 | 1.9 dB  |
| Peaking | 5913 Hz | 0.32 | 1.0 dB  |
| Peaking | 6815 Hz | 6.74 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)