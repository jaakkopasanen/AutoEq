# RBH EP3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.6; 23 -17.6; 25 -17.5; 28 -17.3; 31 -17.1; 34 -17.0; 37 -16.8; 41 -16.6; 45 -16.3; 49 -16.1; 54 -15.9; 60 -15.7; 66 -15.6; 72 -15.4; 79 -15.3; 87 -15.1; 96 -15.0; 106 -14.7; 116 -14.3; 128 -14.0; 141 -13.6; 155 -13.3; 170 -12.8; 187 -12.2; 206 -11.7; 227 -11.0; 249 -10.5; 274 -9.7; 302 -9.1; 332 -8.5; 365 -7.7; 402 -7.1; 442 -6.2; 486 -5.7; 535 -5.0; 588 -4.1; 647 -3.6; 712 -3.2; 783 -2.6; 861 -2.6; 947 -2.6; 1042 -2.6; 1146 -2.6; 1261 -3.5; 1387 -5.0; 1526 -5.9; 1678 -6.5; 1846 -6.6; 2031 -6.7; 2234 -6.8; 2457 -6.1; 2703 -5.4; 2973 -3.5; 3270 -1.2; 3597 -0.5; 3957 -1.6; 4353 -5.0; 4788 -8.5; 5267 -12.2; 5793 -9.1; 6373 -3.2; 7010 -0.7; 7711 -2.4; 8482 -2.6; 9330 -2.7; 10263 -3.5; 11289 -2.7; 12418 -2.7; 13660 -2.7; 15026 -5.4; 16529 -3.9; 18182 -2.7; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RBH EP3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RBH EP3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.27 | -13.8 dB |
| Peaking | 149 Hz   | 0.35 | -8.2 dB  |
| Peaking | 1956 Hz  | 1.08 | -10.5 dB |
| Peaking | 2016 Hz  | 0.36 | 6.3 dB   |
| Peaking | 5265 Hz  | 4.23 | -12.6 dB |
| Peaking | 2719 Hz  | 5.74 | -1.7 dB  |
| Peaking | 3535 Hz  | 4.26 | 2.8 dB   |
| Peaking | 6776 Hz  | 1    | -1.6 dB  |
| Peaking | 6882 Hz  | 5.08 | 3.9 dB   |
| Peaking | 15550 Hz | 3.95 | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -15.6 dB |
| Peaking | 62 Hz    | 1.41 | -8.7 dB  |
| Peaking | 125 Hz   | 1.41 | -9.0 dB  |
| Peaking | 250 Hz   | 1.41 | -6.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -1.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RBH%20EP3/RBH%20EP3.png)