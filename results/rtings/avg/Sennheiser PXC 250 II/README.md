# Sennheiser PXC 250 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.4; 49 -2.2; 54 -3.1; 60 -3.9; 66 -4.6; 72 -5.1; 79 -5.6; 87 -6.0; 96 -6.3; 106 -6.7; 116 -6.8; 128 -6.9; 141 -6.9; 155 -6.9; 170 -6.8; 187 -6.8; 206 -6.5; 227 -6.2; 249 -6.1; 274 -6.0; 302 -6.0; 332 -5.9; 365 -5.8; 402 -5.6; 442 -5.5; 486 -5.3; 535 -5.2; 588 -5.0; 647 -4.8; 712 -4.8; 783 -4.9; 861 -5.2; 947 -6.0; 1042 -7.0; 1146 -8.3; 1261 -9.9; 1387 -11.6; 1526 -12.8; 1678 -12.5; 1846 -13.5; 2031 -13.6; 2234 -12.5; 2457 -11.5; 2703 -10.8; 2973 -10.2; 3270 -9.6; 3597 -7.3; 3957 -4.1; 4353 -1.5; 4788 -3.0; 5267 -4.2; 5793 -3.7; 6373 -5.8; 7010 -9.7; 7711 -11.6; 8482 -12.3; 9330 -13.1; 10263 -14.6; 11289 -14.3; 12418 -9.6; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 250 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 250 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.97 | 6.9 dB   |
| Peaking | 869 Hz   | 0.82 | 7.3 dB   |
| Peaking | 1693 Hz  | 0.54 | -10.1 dB |
| Peaking | 4589 Hz  | 1.73 | 8.8 dB   |
| Peaking | 9925 Hz  | 1.63 | -8.4 dB  |
| Peaking | 125 Hz   | 1.9  | -1.1 dB  |
| Peaking | 2486 Hz  | 6.71 | 0.8 dB   |
| Peaking | 6149 Hz  | 5.62 | 4.7 dB   |
| Peaking | 6565 Hz  | 2.23 | -2.7 dB  |
| Peaking | 13718 Hz | 3.91 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20PXC%20250%20II/Sennheiser%20PXC%20250%20II.png)