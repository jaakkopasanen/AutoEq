# Koss ESP950
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.0; 28 -1.3; 31 -1.5; 34 -1.6; 37 -1.7; 41 -1.8; 45 -1.8; 49 -1.9; 54 -2.1; 60 -2.1; 66 -2.3; 72 -2.3; 79 -2.4; 87 -3.2; 96 -4.2; 106 -5.1; 116 -5.7; 128 -5.7; 141 -5.8; 155 -5.8; 170 -6.1; 187 -6.2; 206 -6.3; 227 -6.3; 249 -6.4; 274 -6.3; 302 -6.3; 332 -6.4; 365 -6.4; 402 -6.5; 442 -6.5; 486 -6.7; 535 -6.9; 588 -6.9; 647 -7.1; 712 -7.3; 783 -7.4; 861 -7.9; 947 -8.2; 1042 -8.5; 1146 -8.9; 1261 -9.5; 1387 -10.0; 1526 -10.1; 1678 -9.4; 1846 -7.4; 2031 -5.4; 2234 -3.9; 2457 -3.4; 2703 -5.4; 2973 -6.4; 3270 -6.0; 3597 -4.2; 3957 -1.9; 4353 -1.4; 4788 -2.4; 5267 -2.6; 5793 -3.0; 6373 -4.1; 7010 -3.8; 7711 -5.9; 8482 -8.6; 9330 -9.8; 10263 -6.7; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss ESP950 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.68 | 5.3 dB  |
| Peaking | 69 Hz   | 1.88 | 2.8 dB  |
| Peaking | 1327 Hz | 1.61 | -4.3 dB |
| Peaking | 4832 Hz | 1    | 4.2 dB  |
| Peaking | 9016 Hz | 4.13 | -5.3 dB |
| Peaking | 46 Hz   | 2.84 | 0.9 dB  |
| Peaking | 311 Hz  | 0.41 | -0.3 dB |
| Peaking | 2382 Hz | 3.44 | 5.4 dB  |
| Peaking | 2898 Hz | 1.54 | -3.6 dB |
| Peaking | 4090 Hz | 4.78 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20ESP950/Koss%20ESP950.png)