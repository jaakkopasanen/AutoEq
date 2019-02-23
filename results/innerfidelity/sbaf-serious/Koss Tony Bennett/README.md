# Koss Tony Bennett
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.7; 28 -2.5; 31 -3.2; 34 -3.9; 37 -4.4; 41 -5.0; 45 -5.5; 49 -6.0; 54 -6.4; 60 -7.0; 66 -7.4; 72 -7.7; 79 -6.9; 87 -5.8; 96 -7.0; 106 -9.0; 116 -9.8; 128 -10.3; 141 -11.1; 155 -11.6; 170 -11.1; 187 -11.9; 206 -12.2; 227 -11.9; 249 -11.7; 274 -11.1; 302 -10.5; 332 -9.8; 365 -9.4; 402 -9.8; 442 -10.6; 486 -11.4; 535 -11.3; 588 -10.7; 647 -10.0; 712 -9.6; 783 -8.4; 861 -7.3; 947 -6.6; 1042 -7.5; 1146 -6.5; 1261 -5.4; 1387 -5.1; 1526 -5.1; 1678 -5.2; 1846 -5.1; 2031 -4.9; 2234 -5.5; 2457 -5.4; 2703 -5.6; 2973 -5.7; 3270 -6.4; 3597 -3.5; 3957 -0.8; 4353 -0.7; 4788 -0.7; 5267 -0.7; 5793 -0.8; 6373 -1.3; 7010 -4.2; 7711 -6.4; 8482 -7.0; 9330 -9.5; 10263 -7.0; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Tony Bennett GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Tony Bennett ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.92 | 6.5 dB  |
| Peaking | 193 Hz  | 0.97 | -5.4 dB |
| Peaking | 549 Hz  | 1.78 | -3.9 dB |
| Peaking | 1545 Hz | 1.67 | 1.9 dB  |
| Peaking | 4946 Hz | 1.8  | 7.0 dB  |
| Peaking | 89 Hz   | 8.88 | 2.3 dB  |
| Peaking | 3908 Hz | 2.03 | -3.0 dB |
| Peaking | 3982 Hz | 4.96 | 5.0 dB  |
| Peaking | 6266 Hz | 6.21 | 2.8 dB  |
| Peaking | 9222 Hz | 4.51 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Tony%20Bennett/Koss%20Tony%20Bennett.png)