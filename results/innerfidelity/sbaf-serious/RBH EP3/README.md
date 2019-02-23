# RBH EP3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.6; 23 -17.6; 25 -17.5; 28 -17.3; 31 -17.1; 34 -17.0; 37 -16.8; 41 -16.6; 45 -16.3; 49 -16.1; 54 -15.9; 60 -15.7; 66 -15.6; 72 -15.4; 79 -15.3; 87 -15.1; 96 -15.0; 106 -14.7; 116 -14.3; 128 -14.0; 141 -13.6; 155 -13.3; 170 -12.8; 187 -12.2; 206 -11.7; 227 -11.0; 249 -10.4; 274 -9.7; 302 -9.1; 332 -8.5; 365 -7.7; 402 -7.1; 442 -6.2; 486 -5.7; 535 -5.0; 588 -4.1; 647 -3.6; 712 -3.2; 783 -2.6; 861 -2.6; 947 -2.6; 1042 -2.6; 1146 -2.6; 1261 -3.5; 1387 -5.0; 1526 -5.9; 1678 -6.5; 1846 -6.6; 2031 -6.7; 2234 -6.8; 2457 -6.1; 2703 -5.4; 2973 -3.5; 3270 -1.2; 3597 -0.5; 3957 -1.6; 4353 -5.0; 4788 -8.5; 5267 -12.2; 5793 -9.1; 6373 -3.2; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RBH EP3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RBH EP3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 0.34 | -10.5 dB |
| Peaking | 126 Hz  | 0.52 | -5.5 dB  |
| Peaking | 808 Hz  | 1.15 | 4.8 dB   |
| Peaking | 3592 Hz | 3.52 | 6.7 dB   |
| Peaking | 5261 Hz | 7.52 | -7.5 dB  |
| Peaking | 456 Hz  | 4.2  | 0.5 dB   |
| Peaking | 1176 Hz | 5.23 | 1.7 dB   |
| Peaking | 1858 Hz | 1.91 | -1.5 dB  |
| Peaking | 5673 Hz | 9.13 | -2.3 dB  |
| Peaking | 6559 Hz | 6.49 | 4.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RBH%20EP3/RBH%20EP3.png)