# Sennheiser PXC 550 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 0.0; 23 1.8; 25 1.1; 28 0.3; 31 -0.2; 34 -0.6; 37 -0.8; 41 -0.9; 45 -0.9; 49 -0.8; 54 -0.5; 60 -0.4; 66 -0.3; 72 -0.3; 79 -0.5; 87 -0.7; 96 -1.0; 106 -1.4; 116 -1.8; 128 -2.1; 141 -2.3; 155 -2.4; 170 -2.5; 187 -2.4; 206 -2.2; 227 -2.1; 249 -1.9; 274 -1.6; 302 -1.2; 332 -1.0; 365 -0.8; 402 -0.9; 442 -1.2; 486 -1.5; 535 -1.7; 588 -1.5; 647 -1.2; 712 -0.7; 783 -0.2; 861 0.2; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -0.4; 1387 -1.7; 1526 -3.5; 1678 -5.1; 1846 -5.5; 2031 -6.3; 2234 -5.5; 2457 -4.0; 2703 -3.3; 2973 -3.1; 3270 -2.6; 3597 -3.3; 3957 -0.7; 4353 5.3; 4788 -0.9; 5267 -5.4; 5793 -1.2; 6373 0.3; 7010 -1.2; 7711 -3.9; 8482 -7.2; 9330 -8.6; 10263 -6.2; 11289 -3.9; 12418 -6.2; 13660 -10.0; 15026 -7.9; 16529 -2.2; 18182 -1.5; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 550 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 2.88 | 2.2 dB  |
| Peaking | 1711 Hz  | 3.74 | -2.6 dB |
| Peaking | 2153 Hz  | 2.13 | -5.1 dB |
| Peaking | 12631 Hz | 0.81 | -7.8 dB |
| Peaking | 20024 Hz | 4.55 | -6.7 dB |
| Peaking | 180 Hz   | 0.72 | -2.4 dB |
| Peaking | 6646 Hz  | 3.64 | 4.6 dB  |
| Peaking | 11191 Hz | 1    | -7.3 dB |
| Peaking | 11399 Hz | 3.18 | 11.3 dB |
| Peaking | 17073 Hz | 3.3  | 4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20PXC%20550%20Wireless/Sennheiser%20PXC%20550%20Wireless.png)