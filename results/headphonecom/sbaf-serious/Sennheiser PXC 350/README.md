# Sennheiser PXC 350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.9; 25 -5.4; 28 -6.0; 31 -6.4; 34 -6.6; 37 -6.6; 41 -6.6; 45 -6.5; 49 -6.4; 54 -6.3; 60 -6.1; 66 -6.0; 72 -6.0; 79 -5.8; 87 -5.8; 96 -6.2; 106 -6.3; 116 -6.3; 128 -6.3; 141 -6.3; 155 -6.2; 170 -5.7; 187 -5.7; 206 -5.2; 227 -5.1; 249 -5.3; 274 -5.6; 302 -5.8; 332 -5.9; 365 -6.3; 402 -6.7; 442 -7.2; 486 -7.8; 535 -8.1; 588 -8.0; 647 -8.1; 712 -8.0; 783 -7.8; 861 -7.3; 947 -7.6; 1042 -7.4; 1146 -7.3; 1261 -7.3; 1387 -7.8; 1526 -8.7; 1678 -10.3; 1846 -11.7; 2031 -5.0; 2234 -0.5; 2457 -10.2; 2703 -12.2; 2973 -7.7; 3270 -4.7; 3597 -5.1; 3957 -3.2; 4353 -0.5; 4788 -4.4; 5267 -1.9; 5793 -4.0; 6373 -7.2; 7010 -8.1; 7711 -7.0; 8482 -8.1; 9330 -10.1; 10263 -10.1; 11289 -8.1; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 1893 Hz |  2.69 | -9.4 dB |
| Peaking | 2172 Hz |  4.92 | 14.4 dB |
| Peaking | 2606 Hz |  5.74 | -8.8 dB |
| Peaking | 4354 Hz |  2.32 | 5.4 dB  |
| Peaking | 9675 Hz |  2.64 | -4.2 dB |
| Peaking | 78 Hz   |  2.97 | 0.7 dB  |
| Peaking | 243 Hz  |  1.53 | 1.5 dB  |
| Peaking | 588 Hz  |  1.69 | -1.8 dB |
| Peaking | 5493 Hz | 14.98 | 4.3 dB  |
| Peaking | 6647 Hz |  6.29 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC%20350/Sennheiser%20PXC%20350.png)