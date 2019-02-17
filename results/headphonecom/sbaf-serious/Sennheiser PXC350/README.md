# Sennheiser PXC350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.8; 25 -4.4; 28 -5.0; 31 -5.4; 34 -5.5; 37 -5.6; 41 -5.5; 45 -5.4; 49 -5.4; 54 -5.2; 60 -5.0; 66 -5.0; 72 -4.9; 79 -4.7; 87 -4.7; 96 -5.1; 106 -5.2; 116 -5.3; 128 -5.3; 141 -5.3; 155 -5.2; 170 -4.7; 187 -4.6; 206 -4.2; 227 -4.1; 249 -4.3; 274 -4.5; 302 -4.7; 332 -4.9; 365 -5.2; 402 -5.7; 442 -6.2; 486 -6.8; 535 -7.0; 588 -6.9; 647 -7.1; 712 -6.9; 783 -6.7; 861 -6.2; 947 -6.5; 1042 -6.3; 1146 -6.2; 1261 -6.3; 1387 -6.8; 1526 -7.7; 1678 -9.2; 1846 -10.6; 2031 -4.1; 2234 -0.5; 2457 -9.1; 2703 -11.1; 2973 -6.6; 3270 -3.7; 3597 -4.0; 3957 -2.2; 4353 -0.5; 4788 -3.3; 5267 -1.3; 5793 -3.0; 6373 -6.1; 7010 -7.1; 7711 -6.2; 8482 -7.0; 9330 -9.1; 10263 -9.0; 11289 -7.1; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.07 | 1.7 dB  |
| Peaking | 1875 Hz | 4.08 | -7.4 dB |
| Peaking | 2161 Hz | 5.05 | 10.6 dB |
| Peaking | 2585 Hz | 6.13 | -8.3 dB |
| Peaking | 4343 Hz | 2.22 | 5.8 dB  |
| Peaking | 255 Hz  | 2.02 | 1.2 dB  |
| Peaking | 568 Hz  | 2.23 | -1.3 dB |
| Peaking | 5546 Hz | 8.81 | 6.6 dB  |
| Peaking | 5628 Hz | 2.85 | -2.5 dB |
| Peaking | 9795 Hz | 4.12 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC350/Sennheiser%20PXC350.png)