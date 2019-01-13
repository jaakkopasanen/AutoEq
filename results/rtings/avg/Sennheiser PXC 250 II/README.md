# Sennheiser PXC 250 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.8; 45 5.1; 49 4.3; 54 3.4; 60 2.6; 66 1.9; 72 1.4; 79 0.9; 87 0.5; 96 0.2; 106 -0.2; 116 -0.3; 128 -0.4; 141 -0.4; 155 -0.4; 170 -0.3; 187 -0.3; 206 0.0; 227 0.3; 249 0.4; 274 0.5; 302 0.5; 332 0.6; 365 0.7; 402 0.9; 442 1.0; 486 1.2; 535 1.3; 588 1.5; 647 1.7; 712 1.7; 783 1.6; 861 1.3; 947 0.5; 1042 -0.5; 1146 -1.8; 1261 -3.4; 1387 -5.1; 1526 -6.3; 1678 -6.0; 1846 -7.0; 2031 -7.1; 2234 -6.0; 2457 -5.0; 2703 -4.3; 2973 -3.7; 3270 -3.1; 3597 -0.8; 3957 2.4; 4353 5.0; 4788 3.5; 5267 2.3; 5793 2.8; 6373 0.7; 7010 -3.2; 7711 -5.1; 8482 -5.8; 9330 -6.6; 10263 -8.1; 11289 -7.8; 12418 -3.1; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 250 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 250 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.96 | 6.9 dB   |
| Peaking | 875 Hz   | 0.82 | 7.3 dB   |
| Peaking | 1686 Hz  | 0.55 | -10.1 dB |
| Peaking | 4570 Hz  | 1.78 | 8.7 dB   |
| Peaking | 9900 Hz  | 1.76 | -8.4 dB  |
| Peaking | 126 Hz   | 1.92 | -1.1 dB  |
| Peaking | 3324 Hz  | 9.64 | -1.1 dB  |
| Peaking | 6057 Hz  | 8.79 | 2.8 dB   |
| Peaking | 7379 Hz  | 5.32 | -2.2 dB  |
| Peaking | 13789 Hz | 4.45 | 2.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20PXC%20250%20II/Sennheiser%20PXC%20250%20II.png)