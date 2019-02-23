# Koss ESP950 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.4; 31 -1.6; 34 -1.7; 37 -1.8; 41 -1.9; 45 -1.9; 49 -2.1; 54 -2.4; 60 -2.4; 66 -2.5; 72 -2.5; 79 -2.7; 87 -3.9; 96 -5.1; 106 -5.8; 116 -6.3; 128 -6.3; 141 -6.3; 155 -6.3; 170 -6.6; 187 -6.7; 206 -6.8; 227 -6.7; 249 -6.8; 274 -6.7; 302 -6.9; 332 -6.8; 365 -6.8; 402 -6.8; 442 -6.8; 486 -7.0; 535 -7.1; 588 -7.2; 647 -7.4; 712 -7.6; 783 -7.7; 861 -8.2; 947 -8.6; 1042 -8.9; 1146 -9.2; 1261 -9.9; 1387 -10.3; 1526 -10.4; 1678 -9.9; 1846 -8.0; 2031 -5.9; 2234 -4.3; 2457 -3.5; 2703 -5.9; 2973 -7.3; 3270 -6.9; 3597 -5.0; 3957 -2.0; 4353 -1.2; 4788 -3.2; 5267 -3.4; 5793 -3.6; 6373 -4.8; 7010 -4.3; 7711 -6.3; 8482 -9.0; 9330 -9.2; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.6; 16529 -6.6; 18182 -6.6; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss ESP950 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.65 | 5.8 dB   |
| Peaking | 68 Hz   | 2.15 | 2.8 dB   |
| Peaking | 2352 Hz | 2.56 | 10.1 dB  |
| Peaking | 2924 Hz | 0.63 | -11.6 dB |
| Peaking | 4261 Hz | 1.24 | 13.1 dB  |
| Peaking | 118 Hz  | 4.13 | -0.8 dB  |
| Peaking | 4144 Hz | 6.77 | 2.4 dB   |
| Peaking | 4568 Hz | 2.7  | -2.7 dB  |
| Peaking | 7411 Hz | 1.07 | 2.4 dB   |
| Peaking | 8772 Hz | 3.94 | -5.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20ESP950%20sample%201/Koss%20ESP950%20sample%201.png)