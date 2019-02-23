# Sennheiser PX 360
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.3; 45 -1.9; 49 -2.4; 54 -2.9; 60 -3.6; 66 -4.2; 72 -4.7; 79 -5.4; 87 -6.1; 96 -6.6; 106 -6.8; 116 -7.1; 128 -6.9; 141 -6.0; 155 -5.4; 170 -5.6; 187 -4.1; 206 -5.5; 227 -6.4; 249 -7.0; 274 -7.2; 302 -7.0; 332 -7.6; 365 -7.2; 402 -6.5; 442 -5.9; 486 -6.1; 535 -5.9; 588 -5.5; 647 -5.8; 712 -6.0; 783 -6.1; 861 -6.5; 947 -7.0; 1042 -8.0; 1146 -9.2; 1261 -10.6; 1387 -12.3; 1526 -14.1; 1678 -15.5; 1846 -16.3; 2031 -15.4; 2234 -13.4; 2457 -10.4; 2703 -8.4; 2973 -6.6; 3270 -4.7; 3597 -2.6; 3957 -1.5; 4353 -3.9; 4788 -4.7; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.6; 10263 -10.0; 11289 -9.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 360 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.84 | 6.6 dB   |
| Peaking | 1834 Hz  | 1.89 | -10.7 dB |
| Peaking | 3723 Hz  | 3.11 | 5.5 dB   |
| Peaking | 5925 Hz  | 3.08 | 6.6 dB   |
| Peaking | 10269 Hz | 3.29 | -4.1 dB  |
| Peaking | 109 Hz   | 3.03 | -1.4 dB  |
| Peaking | 187 Hz   | 5.86 | 2.4 dB   |
| Peaking | 323 Hz   | 1.54 | -1.9 dB  |
| Peaking | 586 Hz   | 0.66 | 1.7 dB   |
| Peaking | 1335 Hz  | 2.94 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB   |
| Peaking | 62 Hz    | 1.41 | 1.1 dB   |
| Peaking | 125 Hz   | 1.41 | -0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20360/Sennheiser%20PX%20360.png)