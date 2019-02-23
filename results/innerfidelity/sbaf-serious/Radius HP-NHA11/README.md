# Radius HP-NHA11
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.6; 23 -15.5; 25 -15.3; 28 -15.1; 31 -14.9; 34 -14.8; 37 -14.6; 41 -14.4; 45 -14.2; 49 -14.0; 54 -13.8; 60 -13.6; 66 -13.4; 72 -13.3; 79 -13.1; 87 -13.0; 96 -12.8; 106 -12.5; 116 -12.2; 128 -11.9; 141 -11.5; 155 -11.1; 170 -10.6; 187 -10.1; 206 -9.6; 227 -8.9; 249 -8.3; 274 -7.7; 302 -7.1; 332 -6.4; 365 -5.8; 402 -5.3; 442 -4.6; 486 -4.0; 535 -3.6; 588 -2.9; 647 -2.5; 712 -2.2; 783 -1.8; 861 -2.0; 947 -2.3; 1042 -2.7; 1146 -3.1; 1261 -3.7; 1387 -4.6; 1526 -5.7; 1678 -6.6; 1846 -7.1; 2031 -7.4; 2234 -7.5; 2457 -6.6; 2703 -6.1; 2973 -4.3; 3270 -2.8; 3597 -2.4; 3957 -4.2; 4353 -8.2; 4788 -11.2; 5267 -8.2; 5793 -3.2; 6373 -0.5; 7010 -3.2; 7711 -5.5; 8482 -5.7; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Radius HP-NHA11 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-NHA11 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.23 | -9.5 dB |
| Peaking | 131 Hz  | 0.68 | -3.5 dB |
| Peaking | 736 Hz  | 1.17 | 4.4 dB  |
| Peaking | 4863 Hz | 7.08 | -7.0 dB |
| Peaking | 6327 Hz | 4.89 | 5.9 dB  |
| Peaking | 1207 Hz | 2.05 | 1.7 dB  |
| Peaking | 2055 Hz | 1.15 | -2.9 dB |
| Peaking | 3498 Hz | 2.62 | 4.8 dB  |
| Peaking | 4427 Hz | 7.29 | -2.6 dB |
| Peaking | 8120 Hz | 3.52 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.9 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-NHA11/Radius%20HP-NHA11.png)