# Torque t402v OnEar Red
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.9; 25 -9.5; 28 -10.3; 31 -11.0; 34 -11.6; 37 -12.1; 41 -12.6; 45 -13.0; 49 -13.4; 54 -13.9; 60 -14.3; 66 -14.7; 72 -15.0; 79 -15.3; 87 -15.5; 96 -16.0; 106 -16.5; 116 -16.9; 128 -17.2; 141 -17.4; 155 -17.4; 170 -17.2; 187 -17.2; 206 -17.0; 227 -16.6; 249 -16.2; 274 -15.6; 302 -14.9; 332 -14.5; 365 -14.0; 402 -13.1; 442 -12.3; 486 -11.7; 535 -10.5; 588 -8.6; 647 -6.7; 712 -4.9; 783 -3.5; 861 -3.7; 947 -5.2; 1042 -7.4; 1146 -9.4; 1261 -10.8; 1387 -10.2; 1526 -11.4; 1678 -10.0; 1846 -8.7; 2031 -8.8; 2234 -9.7; 2457 -9.9; 2703 -9.7; 2973 -9.2; 3270 -8.0; 3597 -7.5; 3957 -7.5; 4353 -8.5; 4788 -7.5; 5267 -3.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OnEar Red GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OnEar Red ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 91 Hz   | 0.43 | -8.7 dB |
| Peaking | 244 Hz  | 0.94 | -6.0 dB |
| Peaking | 2293 Hz | 0.97 | -3.5 dB |
| Peaking | 6029 Hz | 3.81 | 7.4 dB  |
| Peaking | 8185 Hz | 2.83 | -0.5 dB |
| Peaking | 474 Hz  | 1.64 | -3.3 dB |
| Peaking | 811 Hz  | 2.15 | 5.2 dB  |
| Peaking | 989 Hz  | 0.43 | 1.8 dB  |
| Peaking | 1285 Hz | 1.97 | -5.0 dB |
| Peaking | 4514 Hz | 7.59 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.1 dB |
| Peaking | 125 Hz   | 1.41 | -8.7 dB |
| Peaking | 250 Hz   | 1.41 | -8.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OnEar%20Red/Torque%20t402v%20OnEar%20Red.png)