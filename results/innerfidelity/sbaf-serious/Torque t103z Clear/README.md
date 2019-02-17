# Torque t103z Clear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.6; 25 -10.0; 28 -10.7; 31 -11.2; 34 -11.7; 37 -12.0; 41 -12.4; 45 -12.8; 49 -13.2; 54 -13.5; 60 -13.9; 66 -14.3; 72 -14.7; 79 -15.0; 87 -15.4; 96 -15.7; 106 -15.8; 116 -15.9; 128 -16.0; 141 -16.0; 155 -15.9; 170 -15.7; 187 -15.4; 206 -15.1; 227 -14.6; 249 -14.3; 274 -13.7; 302 -13.1; 332 -12.4; 365 -11.8; 402 -11.1; 442 -10.2; 486 -9.7; 535 -9.0; 588 -8.0; 647 -7.6; 712 -6.0; 783 -5.9; 861 -5.8; 947 -5.8; 1042 -5.9; 1146 -5.9; 1261 -6.0; 1387 -6.3; 1526 -6.6; 1678 -6.7; 1846 -6.5; 2031 -6.1; 2234 -6.1; 2457 -6.0; 2703 -6.9; 2973 -6.6; 3270 -5.3; 3597 -4.8; 3957 -6.3; 4353 -10.1; 4788 -8.2; 5267 -8.5; 5793 -3.3; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t103z Clear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t103z Clear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 66 Hz   | 0.4  | -6.9 dB |
| Peaking | 162 Hz  | 0.79 | -5.4 dB |
| Peaking | 321 Hz  | 1.31 | -3.2 dB |
| Peaking | 4906 Hz | 3.39 | -4.6 dB |
| Peaking | 6250 Hz | 4.69 | 6.9 dB  |
| Peaking | 546 Hz  | 1.79 | -2.0 dB |
| Peaking | 701 Hz  | 1.14 | 2.0 dB  |
| Peaking | 1627 Hz | 3.93 | -0.8 dB |
| Peaking | 3565 Hz | 4.8  | 4.2 dB  |
| Peaking | 3729 Hz | 2.21 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -6.4 dB |
| Peaking | 125 Hz   | 1.41 | -8.5 dB |
| Peaking | 250 Hz   | 1.41 | -7.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t103z%20Clear/Torque%20t103z%20Clear.png)