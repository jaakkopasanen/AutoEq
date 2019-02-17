# Torque t402v OverEar Red
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.7; 25 -2.7; 28 -4.1; 31 -5.3; 34 -6.3; 37 -7.2; 41 -8.2; 45 -9.0; 49 -9.7; 54 -10.5; 60 -11.2; 66 -11.7; 72 -12.1; 79 -12.4; 87 -13.0; 96 -13.8; 106 -14.5; 116 -14.9; 128 -15.5; 141 -15.8; 155 -16.2; 170 -16.0; 187 -16.6; 206 -17.0; 227 -17.2; 249 -17.5; 274 -17.7; 302 -17.7; 332 -17.4; 365 -16.8; 402 -15.8; 442 -13.7; 486 -11.5; 535 -9.2; 588 -6.5; 647 -4.4; 712 -3.0; 783 -2.8; 861 -4.1; 947 -5.9; 1042 -8.0; 1146 -8.7; 1261 -9.6; 1387 -10.4; 1526 -11.7; 1678 -10.4; 1846 -7.8; 2031 -7.1; 2234 -8.5; 2457 -9.0; 2703 -9.4; 2973 -8.5; 3270 -6.1; 3597 -5.4; 3957 -5.2; 4353 -5.6; 4788 -5.2; 5267 -3.7; 5793 -3.5; 6373 -5.0; 7010 -5.8; 7711 -9.2; 8482 -11.8; 9330 -9.5; 10263 -7.1; 11289 -7.1; 12418 -7.1; 13660 -7.1; 15026 -7.1; 16529 -7.1; 18182 -7.1; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OverEar Red GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OverEar Red ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.24 | 7.8 dB  |
| Peaking | 135 Hz  | 0.43 | -6.8 dB |
| Peaking | 349 Hz  | 0.83 | -8.0 dB |
| Peaking | 706 Hz  | 1.54 | 9.0 dB  |
| Peaking | 1416 Hz | 2.23 | -4.6 dB |
| Peaking | 1977 Hz | 6.16 | 2.3 dB  |
| Peaking | 2847 Hz | 1.82 | -3.5 dB |
| Peaking | 3458 Hz | 3.15 | 3.6 dB  |
| Peaking | 5688 Hz | 1.88 | 4.0 dB  |
| Peaking | 8423 Hz | 4.41 | -6.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB   |
| Peaking | 62 Hz    | 1.41 | -4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -11.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OverEar%20Red/Torque%20t402v%20OverEar%20Red.png)