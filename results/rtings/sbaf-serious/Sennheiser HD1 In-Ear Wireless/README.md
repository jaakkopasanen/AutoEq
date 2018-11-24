# Sennheiser HD1 In-Ear Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 -2.1; 23 -2.3; 25 -2.4; 28 -2.6; 31 -2.7; 34 -2.9; 37 -3.1; 41 -3.3; 45 -3.4; 49 -3.6; 54 -3.8; 60 -4.2; 66 -4.6; 72 -4.8; 79 -5.0; 87 -5.4; 96 -5.8; 106 -6.4; 116 -7.0; 128 -7.5; 141 -7.9; 155 -8.1; 170 -8.1; 187 -8.1; 206 -8.1; 227 -7.9; 249 -7.5; 274 -7.0; 302 -6.4; 332 -5.7; 365 -4.9; 402 -4.2; 442 -3.4; 486 -2.5; 535 -1.5; 588 -0.6; 647 0.3; 712 0.9; 783 1.0; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 -0.7; 1387 -1.1; 1526 -1.5; 1678 -1.4; 1846 -1.0; 2031 -0.2; 2234 1.1; 2457 2.4; 2703 3.7; 2973 4.6; 3270 5.2; 3597 5.2; 3957 3.7; 4353 1.8; 4788 1.9; 5267 2.8; 5793 1.4; 6373 -2.0; 7010 -3.7; 7711 -2.2; 8482 -2.8; 9330 -7.0; 10263 -9.1; 11289 -5.6; 12418 -2.0; 13660 -0.4; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD1 In-Ear Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD1 In-Ear Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 79 Hz    | 0.37 | -3.7 dB |
| Peaking | 207 Hz   | 0.81 | -6.3 dB |
| Peaking | 3407 Hz  | 1.91 | 5.7 dB  |
| Peaking | 6863 Hz  | 8.08 | -3.8 dB |
| Peaking | 10165 Hz | 3.2  | -9.9 dB |
| Peaking | 403 Hz   | 1.92 | -1.2 dB |
| Peaking | 755 Hz   | 1.33 | 2.8 dB  |
| Peaking | 2111 Hz  | 0.74 | -3.6 dB |
| Peaking | 2585 Hz  | 1.73 | 3.8 dB  |
| Peaking | 5374 Hz  | 5.98 | 2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20HD1%20In-Ear%20Wireless/Sennheiser%20HD1%20In-Ear%20Wireless.png)