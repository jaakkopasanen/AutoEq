# California Headphone Silverado

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 21 -11.0; 23 -11.0; 25 -11.0; 28 -10.9; 31 -10.7; 34 -10.4; 37 -10.2; 41 -9.7; 45 -9.0; 49 -8.4; 54 -8.1; 60 -7.8; 66 -7.9; 72 -9.0; 79 -10.5; 87 -11.9; 96 -12.5; 106 -12.3; 116 -12.1; 128 -12.8; 141 -12.2; 155 -10.8; 170 -10.4; 187 -10.2; 206 -9.6; 227 -9.3; 249 -9.1; 274 -8.8; 302 -8.5; 332 -7.8; 365 -8.5; 402 -7.5; 442 -6.0; 486 -4.7; 535 -3.7; 588 -2.3; 647 -1.6; 712 -1.1; 783 -0.4; 861 -0.3; 947 -0.1; 1042 -0.1; 1146 -0.5; 1261 -2.1; 1387 -4.0; 1526 -4.9; 1678 -5.0; 1846 -4.0; 2031 -1.8; 2234 -2.4; 2457 0.2; 2703 1.8; 2973 2.9; 3270 3.2; 3597 4.0; 3957 3.7; 4353 2.9; 4788 2.7; 5267 2.1; 5793 -1.2; 6373 -2.5; 7010 -5.1; 7711 -7.0; 8482 -9.0; 9330 -6.6; 10263 -0.4; 11289 0.0; 12418 -1.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`California Headphone Silverado GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `California Headphone Silverado ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 1    | -9.4 dB  |
| Peaking | 136 Hz   | 0.42 | -11.8 dB |
| Peaking | 1688 Hz  | 2.92 | -5.6 dB  |
| Peaking | 3774 Hz  | 1.4  | 4.8 dB   |
| Peaking | 8191 Hz  | 2.65 | -9.8 dB  |
| Peaking | 93 Hz    | 5.71 | -1.4 dB  |
| Peaking | 171 Hz   | 4.16 | 1.4 dB   |
| Peaking | 381 Hz   | 3.11 | -2.7 dB  |
| Peaking | 796 Hz   | 1.89 | 2.2 dB   |
| Peaking | 10697 Hz | 7.87 | 2.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/California%20Headphone%20Silverado/California%20Headphone%20Silverado.png)