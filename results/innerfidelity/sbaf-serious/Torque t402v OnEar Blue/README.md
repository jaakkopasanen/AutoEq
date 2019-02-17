# Torque t402v OnEar Blue
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -10.0; 25 -10.6; 28 -11.4; 31 -12.0; 34 -12.5; 37 -13.0; 41 -13.4; 45 -13.8; 49 -14.1; 54 -14.5; 60 -15.0; 66 -15.3; 72 -15.6; 79 -15.9; 87 -16.2; 96 -16.6; 106 -17.2; 116 -17.6; 128 -17.9; 141 -18.1; 155 -18.3; 170 -18.2; 187 -18.3; 206 -18.2; 227 -17.9; 249 -17.5; 274 -16.8; 302 -16.1; 332 -15.5; 365 -15.0; 402 -14.0; 442 -13.2; 486 -12.5; 535 -11.2; 588 -9.3; 647 -7.4; 712 -5.6; 783 -4.0; 861 -3.9; 947 -5.2; 1042 -7.4; 1146 -9.7; 1261 -11.5; 1387 -10.5; 1526 -11.0; 1678 -9.4; 1846 -8.2; 2031 -8.5; 2234 -9.5; 2457 -10.0; 2703 -9.9; 2973 -9.2; 3270 -8.2; 3597 -7.7; 3957 -7.7; 4353 -8.8; 4788 -7.8; 5267 -3.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OnEar Blue GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OnEar Blue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 85 Hz   | 0.38 | -8.9 dB |
| Peaking | 242 Hz  | 0.88 | -7.0 dB |
| Peaking | 2508 Hz | 0.85 | -3.2 dB |
| Peaking | 6044 Hz | 3.74 | 7.6 dB  |
| Peaking | 8118 Hz | 2.89 | -0.5 dB |
| Peaking | 479 Hz  | 1.69 | -3.2 dB |
| Peaking | 827 Hz  | 1.89 | 5.5 dB  |
| Peaking | 1090 Hz | 0.31 | 1.0 dB  |
| Peaking | 1270 Hz | 2.35 | -5.4 dB |
| Peaking | 4524 Hz | 7.69 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -6.4 dB  |
| Peaking | 125 Hz   | 1.41 | -9.1 dB  |
| Peaking | 250 Hz   | 1.41 | -10.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OnEar%20Blue/Torque%20t402v%20OnEar%20Blue.png)