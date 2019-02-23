# Torque t402v OverEar Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -3.2; 25 -3.8; 28 -4.7; 31 -5.5; 34 -6.1; 37 -6.7; 41 -7.3; 45 -7.9; 49 -8.3; 54 -8.8; 60 -9.3; 66 -9.6; 72 -9.8; 79 -10.0; 87 -10.6; 96 -11.4; 106 -12.1; 116 -12.5; 128 -13.0; 141 -13.1; 155 -13.5; 170 -13.1; 187 -13.8; 206 -14.2; 227 -14.4; 249 -14.7; 274 -14.6; 302 -13.9; 332 -12.8; 365 -11.1; 402 -9.0; 442 -6.4; 486 -4.6; 535 -2.6; 588 -0.6; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -1.8; 1042 -3.7; 1146 -2.9; 1261 -3.7; 1387 -5.4; 1526 -7.6; 1678 -9.5; 1846 -7.3; 2031 -5.3; 2234 -5.0; 2457 -4.8; 2703 -4.3; 2973 -3.8; 3270 -1.7; 3597 -0.6; 3957 -0.5; 4353 -0.6; 4788 -0.5; 5267 -1.0; 5793 -2.9; 6373 -7.2; 7010 -8.2; 7711 -7.9; 8482 -7.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OverEar Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OverEar Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.54 | 4.5 dB  |
| Peaking | 139 Hz  | 0.57 | -5.7 dB |
| Peaking | 290 Hz  | 1.29 | -6.3 dB |
| Peaking | 660 Hz  | 1.28 | 8.5 dB  |
| Peaking | 4154 Hz | 2    | 6.9 dB  |
| Peaking | 1207 Hz | 6.79 | 1.4 dB  |
| Peaking | 1665 Hz | 4.14 | -5.4 dB |
| Peaking | 1931 Hz | 0.85 | 1.2 dB  |
| Peaking | 5535 Hz | 4.01 | 5.3 dB  |
| Peaking | 6497 Hz | 1.85 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -9.8 dB |
| Peaking | 500 Hz   | 1.41 | 4.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OverEar%20Black/Torque%20t402v%20OverEar%20Black.png)