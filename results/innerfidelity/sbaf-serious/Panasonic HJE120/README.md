# Panasonic HJE120
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -13.9; 25 -14.0; 28 -14.1; 31 -14.1; 34 -13.8; 37 -13.6; 41 -13.6; 45 -13.9; 49 -14.1; 54 -14.3; 60 -14.2; 66 -14.3; 72 -14.6; 79 -14.8; 87 -14.9; 96 -14.9; 106 -15.0; 116 -14.7; 128 -14.7; 141 -14.8; 155 -14.4; 170 -14.2; 187 -13.9; 206 -13.5; 227 -13.0; 249 -12.6; 274 -12.0; 302 -11.5; 332 -10.9; 365 -10.3; 402 -9.7; 442 -9.0; 486 -8.6; 535 -8.1; 588 -7.3; 647 -6.8; 712 -6.6; 783 -6.1; 861 -6.0; 947 -6.3; 1042 -6.7; 1146 -7.1; 1261 -7.7; 1387 -8.7; 1526 -10.2; 1678 -12.0; 1846 -13.8; 2031 -14.1; 2234 -12.0; 2457 -7.8; 2703 -5.2; 2973 -2.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.0; 4788 -4.5; 5267 -2.6; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic HJE120 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic HJE120 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.2  | -7.2 dB |
| Peaking | 175 Hz  | 0.68 | -4.4 dB |
| Peaking | 1985 Hz | 2.52 | -9.7 dB |
| Peaking | 3448 Hz | 1.75 | 7.5 dB  |
| Peaking | 6074 Hz | 4.64 | 5.4 dB  |
| Peaking | 41 Hz   | 3.22 | 0.5 dB  |
| Peaking | 352 Hz  | 2.15 | -0.7 dB |
| Peaking | 819 Hz  | 1.63 | 1.6 dB  |
| Peaking | 1561 Hz | 4.86 | -1.1 dB |
| Peaking | 8315 Hz | 4.06 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Panasonic%20HJE120/Panasonic%20HJE120.png)