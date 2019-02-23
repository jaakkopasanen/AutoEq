# Torque t402v OnEar Blue
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -7.1; 25 -7.7; 28 -8.4; 31 -9.0; 34 -9.6; 37 -10.0; 41 -10.5; 45 -10.8; 49 -11.2; 54 -11.6; 60 -12.0; 66 -12.4; 72 -12.7; 79 -13.0; 87 -13.2; 96 -13.7; 106 -14.2; 116 -14.6; 128 -14.9; 141 -15.2; 155 -15.4; 170 -15.2; 187 -15.4; 206 -15.2; 227 -14.9; 249 -14.5; 274 -13.9; 302 -13.1; 332 -12.5; 365 -12.0; 402 -11.0; 442 -10.2; 486 -9.5; 535 -8.3; 588 -6.3; 647 -4.4; 712 -2.6; 783 -1.1; 861 -1.0; 947 -2.2; 1042 -4.5; 1146 -6.7; 1261 -8.5; 1387 -7.5; 1526 -8.1; 1678 -6.4; 1846 -5.2; 2031 -5.5; 2234 -6.6; 2457 -7.0; 2703 -7.0; 2973 -6.3; 3270 -5.2; 3597 -4.7; 3957 -4.7; 4353 -5.8; 4788 -4.8; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OnEar Blue GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OnEar Blue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 1.17 | -1.6 dB |
| Peaking | 172 Hz  | 0.41 | -8.9 dB |
| Peaking | 787 Hz  | 2.35 | 8.3 dB  |
| Peaking | 5948 Hz | 2.51 | 7.0 dB  |
| Peaking | 7843 Hz | 2.37 | -1.7 dB |
| Peaking | 986 Hz  | 4.71 | 2.1 dB  |
| Peaking | 1293 Hz | 2.49 | -2.5 dB |
| Peaking | 1893 Hz | 4.72 | 2.2 dB  |
| Peaking | 3186 Hz | 1.39 | -1.6 dB |
| Peaking | 3454 Hz | 3.64 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OnEar%20Blue/Torque%20t402v%20OnEar%20Blue.png)