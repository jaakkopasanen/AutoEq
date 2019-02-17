# Torque t402v OverEar Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.8; 25 -6.5; 28 -7.4; 31 -8.2; 34 -8.8; 37 -9.4; 41 -10.0; 45 -10.5; 49 -11.0; 54 -11.4; 60 -11.9; 66 -12.3; 72 -12.5; 79 -12.6; 87 -13.2; 96 -14.1; 106 -14.8; 116 -15.2; 128 -15.7; 141 -15.8; 155 -16.1; 170 -15.8; 187 -16.5; 206 -16.8; 227 -17.0; 249 -17.3; 274 -17.2; 302 -16.6; 332 -15.5; 365 -13.7; 402 -11.7; 442 -9.1; 486 -7.3; 535 -5.2; 588 -2.9; 647 -1.2; 712 -0.5; 783 -0.9; 861 -2.6; 947 -4.5; 1042 -6.4; 1146 -5.6; 1261 -6.4; 1387 -8.1; 1526 -10.3; 1678 -12.2; 1846 -10.0; 2031 -7.9; 2234 -7.7; 2457 -7.5; 2703 -7.0; 2973 -6.5; 3270 -4.3; 3597 -3.2; 3957 -3.1; 4353 -3.2; 4788 -2.9; 5267 -3.7; 5793 -5.6; 6373 -9.9; 7010 -10.9; 7711 -10.6; 8482 -10.5; 9330 -6.8; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -6.9; 15026 -5.8; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OverEar Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OverEar Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 125 Hz  | 0.42 | -8.4 dB |
| Peaking | 287 Hz  | 1.11 | -7.1 dB |
| Peaking | 675 Hz  | 1.68 | 8.3 dB  |
| Peaking | 1665 Hz | 3.26 | -6.7 dB |
| Peaking | 7590 Hz | 3.48 | -6.2 dB |
| Peaking | 18 Hz   | 2.77 | 2.5 dB  |
| Peaking | 2753 Hz | 2.53 | -1.9 dB |
| Peaking | 3585 Hz | 2.82 | 2.9 dB  |
| Peaking | 5035 Hz | 2.52 | 3.1 dB  |
| Peaking | 6504 Hz | 6.61 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -6.8 dB  |
| Peaking | 250 Hz   | 1.41 | -12.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.4 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OverEar%20Black/Torque%20t402v%20OverEar%20Black.png)