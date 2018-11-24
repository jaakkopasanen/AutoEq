# Sennheiser PXC 250 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.8; 45 5.1; 49 4.3; 54 3.4; 60 2.6; 66 1.9; 72 1.4; 79 0.9; 87 0.5; 96 0.2; 106 -0.2; 116 -0.3; 128 -0.4; 141 -0.4; 155 -0.4; 170 -0.3; 187 -0.3; 206 0.0; 227 0.3; 249 0.4; 274 0.5; 302 0.5; 332 0.6; 365 0.7; 402 0.9; 442 1.0; 486 1.2; 535 1.3; 588 1.5; 647 1.7; 712 1.7; 783 1.6; 861 1.3; 947 0.5; 1042 -0.5; 1146 -1.8; 1261 -3.4; 1387 -5.1; 1526 -6.3; 1678 -6.0; 1846 -7.0; 2031 -7.1; 2234 -6.1; 2457 -5.0; 2703 -4.0; 2973 -3.2; 3270 -2.3; 3597 0.2; 3957 3.6; 4353 5.9; 4788 5.2; 5267 4.9; 5793 5.3; 6373 2.0; 7010 -2.4; 7711 -3.7; 8482 -5.1; 9330 -7.9; 10263 -9.9; 11289 -7.0; 12418 -0.6; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 250 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 250 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.98 | 6.9 dB   |
| Peaking | 869 Hz   | 0.8  | 7.4 dB   |
| Peaking | 1724 Hz  | 0.55 | -10.5 dB |
| Peaking | 4692 Hz  | 1.54 | 10.4 dB  |
| Peaking | 9883 Hz  | 2.36 | -10.5 dB |
| Peaking | 49 Hz    | 2.88 | 1.0 dB   |
| Peaking | 122 Hz   | 1.49 | -1.1 dB  |
| Peaking | 6045 Hz  | 6.34 | 4.3 dB   |
| Peaking | 6775 Hz  | 2.74 | -2.8 dB  |
| Peaking | 13086 Hz | 4.29 | 2.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20PXC%20250%20II/Sennheiser%20PXC%20250%20II.png)