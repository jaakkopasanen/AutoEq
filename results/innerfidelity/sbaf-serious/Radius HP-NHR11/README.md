# Radius HP-NHR11
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -13.4; 25 -13.3; 28 -13.1; 31 -13.0; 34 -12.9; 37 -12.7; 41 -12.6; 45 -12.4; 49 -12.3; 54 -12.1; 60 -12.0; 66 -11.9; 72 -11.8; 79 -11.7; 87 -11.6; 96 -11.5; 106 -11.2; 116 -10.9; 128 -10.7; 141 -10.3; 155 -9.9; 170 -9.4; 187 -8.9; 206 -8.4; 227 -7.7; 249 -7.2; 274 -6.5; 302 -5.8; 332 -5.2; 365 -4.6; 402 -3.9; 442 -3.2; 486 -2.7; 535 -2.1; 588 -1.4; 647 -1.0; 712 -0.8; 783 -0.5; 861 -0.6; 947 -0.9; 1042 -1.3; 1146 -1.5; 1261 -2.1; 1387 -3.1; 1526 -4.1; 1678 -4.8; 1846 -5.2; 2031 -5.3; 2234 -5.3; 2457 -4.6; 2703 -4.0; 2973 -2.4; 3270 -0.9; 3597 -0.5; 3957 -1.9; 4353 -5.1; 4788 -7.9; 5267 -8.3; 5793 -4.5; 6373 -0.9; 7010 -1.7; 7711 -3.9; 8482 -4.2; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Radius HP-NHR11 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-NHR11 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.34 | -8.6 dB |
| Peaking | 122 Hz  | 0.57 | -4.8 dB |
| Peaking | 723 Hz  | 1.13 | 4.4 dB  |
| Peaking | 3536 Hz | 4.42 | 4.4 dB  |
| Peaking | 4936 Hz | 6.61 | -5.5 dB |
| Peaking | 723 Hz  | 2.67 | -1.2 dB |
| Peaking | 1574 Hz | 0.67 | 2.6 dB  |
| Peaking | 1882 Hz | 1.4  | -4.3 dB |
| Peaking | 5403 Hz | 9.67 | -2.4 dB |
| Peaking | 6542 Hz | 6.39 | 4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-NHR11/Radius%20HP-NHR11.png)