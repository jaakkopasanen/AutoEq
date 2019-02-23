# Nixon RPM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.5; 25 -2.4; 28 -3.7; 31 -4.8; 34 -5.8; 37 -6.6; 41 -7.6; 45 -8.3; 49 -9.0; 54 -9.4; 60 -9.7; 66 -10.2; 72 -10.8; 79 -11.1; 87 -11.5; 96 -11.7; 106 -11.5; 116 -11.6; 128 -11.8; 141 -11.9; 155 -11.9; 170 -11.6; 187 -11.7; 206 -11.6; 227 -11.4; 249 -11.3; 274 -11.1; 302 -11.0; 332 -12.1; 365 -11.5; 402 -11.0; 442 -10.6; 486 -10.1; 535 -9.3; 588 -8.8; 647 -8.7; 712 -9.1; 783 -9.2; 861 -9.7; 947 -9.7; 1042 -9.2; 1146 -8.8; 1261 -9.1; 1387 -8.6; 1526 -7.8; 1678 -6.9; 1846 -5.3; 2031 -3.7; 2234 -2.2; 2457 -0.7; 2703 -0.6; 2973 -0.6; 3270 -0.6; 3597 -0.6; 3957 -0.9; 4353 -2.4; 4788 -6.2; 5267 -0.8; 5793 -0.6; 6373 -1.1; 7010 -4.0; 7711 -6.3; 8482 -6.5; 9330 -6.6; 10263 -6.8; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.6; 16529 -6.6; 18182 -6.6; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nixon RPM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nixon RPM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.69 | 9.9 dB  |
| Peaking | 69 Hz   | 0.3  | -3.1 dB |
| Peaking | 664 Hz  | 0.08 | -3.5 dB |
| Peaking | 2952 Hz | 1.11 | 9.8 dB  |
| Peaking | 6006 Hz | 3.38 | 6.4 dB  |
| Peaking | 348 Hz  | 6.12 | -1.3 dB |
| Peaking | 612 Hz  | 3    | 1.6 dB  |
| Peaking | 2204 Hz | 2.14 | 3.5 dB  |
| Peaking | 2239 Hz | 0.84 | -2.6 dB |
| Peaking | 3873 Hz | 6.26 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -3.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nixon%20RPM/Nixon%20RPM.png)