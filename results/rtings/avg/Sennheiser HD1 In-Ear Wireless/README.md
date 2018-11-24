# Sennheiser HD1 In-Ear Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 -2.5; 23 -2.6; 25 -2.6; 28 -2.7; 31 -2.8; 34 -2.9; 37 -2.9; 41 -3.1; 45 -3.2; 49 -3.2; 54 -3.5; 60 -4.0; 66 -4.4; 72 -4.8; 79 -5.2; 87 -5.7; 96 -6.3; 106 -6.9; 116 -7.5; 128 -8.0; 141 -8.5; 155 -8.7; 170 -8.8; 187 -8.7; 206 -8.6; 227 -8.3; 249 -8.1; 274 -7.7; 302 -7.2; 332 -6.6; 365 -5.9; 402 -5.3; 442 -4.5; 486 -3.7; 535 -2.7; 588 -1.7; 647 -0.7; 712 0.0; 783 0.5; 861 0.6; 947 0.3; 1042 -0.3; 1146 -0.7; 1261 -0.9; 1387 -1.1; 1526 -1.2; 1678 -1.1; 1846 -1.0; 2031 -0.6; 2234 0.6; 2457 1.9; 2703 2.9; 2973 3.1; 3270 2.7; 3597 2.0; 3957 1.3; 4353 0.5; 4788 0.3; 5267 -0.2; 5793 -2.5; 6373 -5.7; 7010 -6.9; 7711 -3.7; 8482 -2.3; 9330 -5.8; 10263 -10.3; 11289 -10.9; 12418 -9.8; 13660 -7.3; 15026 -1.0; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD1 In-Ear Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-33**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD1 In-Ear Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 57 Hz    | 0.23 | -2.5 dB  |
| Peaking | 196 Hz   | 0.64 | -7.5 dB  |
| Peaking | 3112 Hz  | 2.15 | 3.6 dB   |
| Peaking | 6716 Hz  | 5.5  | -6.3 dB  |
| Peaking | 11443 Hz | 1.94 | -12.0 dB |
| Peaking | 407 Hz   | 2.14 | -1.2 dB  |
| Peaking | 785 Hz   | 1.87 | 2.4 dB   |
| Peaking | 1669 Hz  | 1.38 | -1.5 dB  |
| Peaking | 2523 Hz  | 4.33 | 1.2 dB   |
| Peaking | 15899 Hz | 4.92 | 2.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD1%20In-Ear%20Wireless/Sennheiser%20HD1%20In-Ear%20Wireless.png)