# Sennheiser PXC 450
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.7; 25 -7.7; 28 -7.2; 31 -6.5; 34 -6.0; 37 -5.7; 41 -5.4; 45 -5.3; 49 -5.2; 54 -5.2; 60 -5.1; 66 -5.2; 72 -5.4; 79 -5.7; 87 -6.0; 96 -6.3; 106 -6.8; 116 -7.1; 128 -7.4; 141 -7.6; 155 -7.6; 170 -7.4; 187 -6.9; 206 -6.3; 227 -6.4; 249 -6.7; 274 -7.2; 302 -7.7; 332 -8.0; 365 -8.4; 402 -8.9; 442 -9.3; 486 -9.6; 535 -9.9; 588 -10.0; 647 -9.9; 712 -9.5; 783 -8.8; 861 -7.8; 947 -6.9; 1042 -6.1; 1146 -5.2; 1261 -4.6; 1387 -4.0; 1526 -3.0; 1678 -1.7; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -4.5; 2703 -6.9; 2973 -1.0; 3270 -0.6; 3597 -3.2; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.2; 6373 -2.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -10.5; 13660 -10.1; 15026 -7.4; 16529 -9.6; 18182 -14.0; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 567 Hz   | 1.25 | -4.0 dB |
| Peaking | 1840 Hz  | 2.08 | 5.8 dB  |
| Peaking | 4681 Hz  | 1.2  | 6.3 dB  |
| Peaking | 15805 Hz | 2.49 | 5.2 dB  |
| Peaking | 18122 Hz | 0.49 | -8.1 dB |
| Peaking | 58 Hz    | 1.48 | 1.6 dB  |
| Peaking | 138 Hz   | 2.91 | -1.3 dB |
| Peaking | 2652 Hz  | 8    | -9.2 dB |
| Peaking | 2694 Hz  | 2.96 | 4.2 dB  |
| Peaking | 7841 Hz  | 8.78 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -4.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20PXC%20450/Sennheiser%20PXC%20450.png)