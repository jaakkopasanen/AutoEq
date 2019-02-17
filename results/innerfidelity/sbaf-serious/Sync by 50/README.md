# Sync by 50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.9; 25 -8.6; 28 -9.5; 31 -10.3; 34 -11.0; 37 -11.6; 41 -12.2; 45 -12.6; 49 -13.0; 54 -13.4; 60 -13.8; 66 -14.0; 72 -14.3; 79 -14.5; 87 -14.9; 96 -15.2; 106 -15.3; 116 -15.4; 128 -15.5; 141 -15.5; 155 -15.5; 170 -15.3; 187 -15.1; 206 -14.7; 227 -14.1; 249 -13.9; 274 -14.3; 302 -14.4; 332 -14.1; 365 -13.7; 402 -13.5; 442 -13.4; 486 -13.0; 535 -11.6; 588 -8.7; 647 -5.7; 712 -3.9; 783 -3.2; 861 -3.9; 947 -4.9; 1042 -5.8; 1146 -6.2; 1261 -5.8; 1387 -5.1; 1526 -6.3; 1678 -7.9; 1846 -8.5; 2031 -8.5; 2234 -7.7; 2457 -6.6; 2703 -5.1; 2973 -4.2; 3270 -3.9; 3597 -4.7; 3957 -5.8; 4353 -5.3; 4788 -2.4; 5267 -0.9; 5793 -2.8; 6373 -0.5; 7010 -6.3; 7711 -5.2; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sync by 50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sync by 50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 79 Hz   | 0.46 | -8.7 dB |
| Peaking | 217 Hz  | 0.97 | -5.2 dB |
| Peaking | 419 Hz  | 2.47 | -5.6 dB |
| Peaking | 1950 Hz | 4.22 | -3.6 dB |
| Peaking | 5544 Hz | 2.75 | 4.3 dB  |
| Peaking | 534 Hz  | 4.21 | -4.0 dB |
| Peaking | 791 Hz  | 1.15 | 5.9 dB  |
| Peaking | 1025 Hz | 2.99 | -2.5 dB |
| Peaking | 1089 Hz | 0.26 | -1.3 dB |
| Peaking | 3079 Hz | 4.54 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -6.9 dB |
| Peaking | 125 Hz   | 1.41 | -8.0 dB |
| Peaking | 250 Hz   | 1.41 | -7.5 dB |
| Peaking | 500 Hz   | 1.41 | -5.1 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sync%20by%2050/Sync%20by%2050.png)