# Torque t402v OverEar Red
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.6; 34 -2.5; 37 -3.4; 41 -4.4; 45 -5.3; 49 -6.0; 54 -6.7; 60 -7.4; 66 -8.0; 72 -8.4; 79 -8.7; 87 -9.2; 96 -10.1; 106 -10.7; 116 -11.2; 128 -11.7; 141 -12.0; 155 -12.4; 170 -12.2; 187 -12.8; 206 -13.2; 227 -13.5; 249 -13.7; 274 -13.9; 302 -13.9; 332 -13.6; 365 -13.0; 402 -12.0; 442 -10.0; 486 -7.8; 535 -5.5; 588 -2.7; 647 -0.7; 712 -0.5; 783 -0.5; 861 -0.6; 947 -2.1; 1042 -4.3; 1146 -4.9; 1261 -5.9; 1387 -6.7; 1526 -8.0; 1678 -6.7; 1846 -4.1; 2031 -3.4; 2234 -4.7; 2457 -5.3; 2703 -5.6; 2973 -4.8; 3270 -2.4; 3597 -1.7; 3957 -1.4; 4353 -1.8; 4788 -1.5; 5267 -0.5; 5793 -0.5; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -8.0; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OverEar Red GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OverEar Red ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 1.12 | 6.9 dB   |
| Peaking | 345 Hz  | 0.39 | -10.4 dB |
| Peaking | 698 Hz  | 1.17 | 14.1 dB  |
| Peaking | 3850 Hz | 1.76 | 4.7 dB   |
| Peaking | 5755 Hz | 3.25 | 5.3 dB   |
| Peaking | 899 Hz  | 8.95 | 1.5 dB   |
| Peaking | 1600 Hz | 3.27 | -3.8 dB  |
| Peaking | 1890 Hz | 3.13 | 4.2 dB   |
| Peaking | 2750 Hz | 6.38 | -1.5 dB  |
| Peaking | 8504 Hz | 6.08 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -8.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OverEar%20Red/Torque%20t402v%20OverEar%20Red.png)