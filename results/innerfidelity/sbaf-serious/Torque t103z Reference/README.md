# Torque t103z Reference
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.1; 45 -1.8; 49 -2.5; 54 -3.2; 60 -4.0; 66 -4.8; 72 -5.5; 79 -6.4; 87 -7.2; 96 -8.1; 106 -8.8; 116 -9.5; 128 -10.3; 141 -11.1; 155 -11.9; 170 -12.6; 187 -13.3; 206 -14.0; 227 -14.5; 249 -15.0; 274 -15.3; 302 -15.4; 332 -15.2; 365 -14.8; 402 -14.1; 442 -13.1; 486 -12.3; 535 -11.3; 588 -10.2; 647 -9.6; 712 -8.0; 783 -7.7; 861 -7.6; 947 -7.7; 1042 -7.7; 1146 -7.9; 1261 -8.2; 1387 -8.8; 1526 -9.4; 1678 -10.0; 1846 -10.2; 2031 -10.1; 2234 -9.2; 2457 -6.8; 2703 -3.9; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t103z Reference GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t103z Reference ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.7  | 6.8 dB  |
| Peaking | 267 Hz  | 0.68 | -9.3 dB |
| Peaking | 2046 Hz | 1.81 | -6.4 dB |
| Peaking | 3271 Hz | 1.37 | 7.6 dB  |
| Peaking | 5621 Hz | 2.68 | 4.9 dB  |
| Peaking | 248 Hz  | 1.44 | 2.4 dB  |
| Peaking | 297 Hz  | 0.7  | -2.0 dB |
| Peaking | 774 Hz  | 2.03 | 1.8 dB  |
| Peaking | 1504 Hz | 5.8  | -0.8 dB |
| Peaking | 8325 Hz | 4    | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -8.7 dB |
| Peaking | 500 Hz   | 1.41 | -4.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t103z%20Reference/Torque%20t103z%20Reference.png)