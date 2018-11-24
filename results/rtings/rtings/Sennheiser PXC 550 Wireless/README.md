# Sennheiser PXC 550 Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 21 0.0; 23 1.8; 25 1.1; 28 0.3; 31 -0.2; 34 -0.6; 37 -0.8; 41 -0.9; 45 -0.9; 49 -0.8; 54 -0.5; 60 -0.4; 66 -0.3; 72 -0.3; 79 -0.5; 87 -0.7; 96 -1.0; 106 -1.4; 116 -1.8; 128 -2.1; 141 -2.3; 155 -2.4; 170 -2.5; 187 -2.4; 206 -2.2; 227 -2.1; 249 -1.9; 274 -1.6; 302 -1.2; 332 -1.0; 365 -0.8; 402 -0.9; 442 -1.2; 486 -1.5; 535 -1.7; 588 -1.5; 647 -1.2; 712 -0.7; 783 -0.2; 861 0.2; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -0.4; 1387 -1.7; 1526 -3.5; 1678 -5.1; 1846 -5.5; 2031 -6.3; 2234 -5.5; 2457 -4.0; 2703 -3.1; 2973 -2.7; 3270 -1.9; 3597 -2.3; 3957 0.5; 4353 6.0; 4788 0.8; 5267 -2.8; 5793 1.3; 6373 1.5; 7010 -0.4; 7711 -2.5; 8482 -6.6; 9330 -9.9; 10263 -7.9; 11289 -3.1; 12418 -2.9; 13660 -6.7; 15026 -5.2; 16529 -0.2; 18182 0.0; 20000 -2.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 550 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 2.83 | 2.3 dB   |
| Peaking | 2044 Hz  | 1.68 | -6.3 dB  |
| Peaking | 4368 Hz  | 9.4  | 7.9 dB   |
| Peaking | 9463 Hz  | 3.75 | -10.6 dB |
| Peaking | 14178 Hz | 3.59 | -7.2 dB  |
| Peaking | 20 Hz    | 2.62 | 1.4 dB   |
| Peaking | 169 Hz   | 0.94 | -2.5 dB  |
| Peaking | 529 Hz   | 4.14 | -1.3 dB  |
| Peaking | 5220 Hz  | 7.94 | -3.7 dB  |
| Peaking | 6098 Hz  | 4.69 | 3.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20PXC%20550%20Wireless/Sennheiser%20PXC%20550%20Wireless.png)