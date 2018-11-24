# Sennheiser HD1 In-Ear Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 21 -2.5; 23 -2.6; 25 -2.6; 28 -2.7; 31 -2.8; 34 -2.9; 37 -2.9; 41 -3.1; 45 -3.2; 49 -3.2; 54 -3.5; 60 -4.0; 66 -4.4; 72 -4.8; 79 -5.2; 87 -5.7; 96 -6.3; 106 -6.9; 116 -7.5; 128 -8.0; 141 -8.5; 155 -8.7; 170 -8.8; 187 -8.7; 206 -8.6; 227 -8.3; 249 -8.1; 274 -7.7; 302 -7.2; 332 -6.6; 365 -5.9; 402 -5.3; 442 -4.5; 486 -3.7; 535 -2.7; 588 -1.7; 647 -0.7; 712 0.0; 783 0.5; 861 0.6; 947 0.3; 1042 -0.3; 1146 -0.7; 1261 -0.9; 1387 -1.1; 1526 -1.2; 1678 -1.1; 1846 -1.0; 2031 -0.6; 2234 0.6; 2457 1.9; 2703 3.1; 2973 3.6; 3270 3.4; 3597 3.0; 3957 2.5; 4353 1.8; 4788 2.1; 5267 2.4; 5793 -0.0; 6373 -4.5; 7010 -6.3; 7711 -3.3; 8482 -3.2; 9330 -8.5; 10263 -12.5; 11289 -10.1; 12418 -6.5; 13660 -4.0; 15026 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD1 In-Ear Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD1 In-Ear Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 52 Hz    | 0.2  | -2.3 dB  |
| Peaking | 195 Hz   | 0.62 | -7.6 dB  |
| Peaking | 3882 Hz  | 1.08 | 3.8 dB   |
| Peaking | 6749 Hz  | 6.09 | -6.4 dB  |
| Peaking | 10559 Hz | 2.39 | -13.3 dB |
| Peaking | 803 Hz   | 2.61 | 2.4 dB   |
| Peaking | 1969 Hz  | 1.09 | -3.6 dB  |
| Peaking | 2768 Hz  | 1.08 | 3.7 dB   |
| Peaking | 3937 Hz  | 3.1  | -2.2 dB  |
| Peaking | 15504 Hz | 5.49 | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20HD1%20In-Ear%20Wireless/Sennheiser%20HD1%20In-Ear%20Wireless.png)