# Sennheiser PXC 250 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.2; 54 -2.0; 60 -2.8; 66 -3.5; 72 -4.1; 79 -4.5; 87 -4.9; 96 -5.3; 106 -5.6; 116 -5.8; 128 -5.9; 141 -5.9; 155 -5.8; 170 -5.8; 187 -5.7; 206 -5.4; 227 -5.1; 249 -5.0; 274 -5.0; 302 -4.9; 332 -4.8; 365 -4.7; 402 -4.6; 442 -4.5; 486 -4.3; 535 -4.1; 588 -3.9; 647 -3.8; 712 -3.7; 783 -3.8; 861 -4.2; 947 -4.9; 1042 -5.9; 1146 -7.3; 1261 -8.9; 1387 -10.5; 1526 -11.7; 1678 -11.4; 1846 -12.4; 2031 -12.6; 2234 -11.5; 2457 -10.5; 2703 -9.7; 2973 -9.1; 3270 -8.5; 3597 -6.3; 3957 -3.0; 4353 -0.5; 4788 -1.9; 5267 -3.1; 5793 -2.6; 6373 -4.7; 7010 -8.7; 7711 -10.5; 8482 -11.2; 9330 -12.0; 10263 -13.5; 11289 -13.3; 12418 -8.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 250 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 250 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.72 | 6.7 dB   |
| Peaking | 922 Hz   | 0.61 | 9.2 dB   |
| Peaking | 1638 Hz  | 0.57 | -11.7 dB |
| Peaking | 4609 Hz  | 1.62 | 9.2 dB   |
| Peaking | 9910 Hz  | 1.67 | -7.4 dB  |
| Peaking | 3368 Hz  | 5.7  | -1.8 dB  |
| Peaking | 5087 Hz  | 4.9  | -5.2 dB  |
| Peaking | 5571 Hz  | 1.7  | 4.4 dB   |
| Peaking | 7275 Hz  | 3.59 | -3.6 dB  |
| Peaking | 13514 Hz | 4.96 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20PXC%20250%20II/Sennheiser%20PXC%20250%20II.png)