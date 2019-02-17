# Polk Audio Hinge
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.6; 23 -12.9; 25 -13.1; 28 -13.2; 31 -13.3; 34 -13.4; 37 -13.5; 41 -13.5; 45 -13.6; 49 -13.6; 54 -13.7; 60 -13.9; 66 -13.9; 72 -13.9; 79 -14.0; 87 -14.0; 96 -14.6; 106 -14.8; 116 -15.4; 128 -15.6; 141 -16.0; 155 -15.6; 170 -15.0; 187 -14.6; 206 -13.5; 227 -12.0; 249 -10.6; 274 -8.9; 302 -8.8; 332 -8.8; 365 -8.5; 402 -8.7; 442 -9.1; 486 -9.1; 535 -8.7; 588 -7.7; 647 -6.7; 712 -5.9; 783 -4.4; 861 -2.9; 947 -1.3; 1042 -0.5; 1146 -2.3; 1261 -5.0; 1387 -6.6; 1526 -8.3; 1678 -7.9; 1846 -7.3; 2031 -8.8; 2234 -7.8; 2457 -6.0; 2703 -4.7; 2973 -4.0; 3270 -4.1; 3597 -2.5; 3957 -1.5; 4353 -4.4; 4788 -5.8; 5267 -2.6; 5793 -0.8; 6373 -2.0; 7010 -5.0; 7711 -4.3; 8482 -0.8; 9330 -0.6; 10263 -0.6; 11289 -0.6; 12418 -0.6; 13660 -0.6; 15026 -0.6; 16529 -0.6; 18182 -0.6; 20000 -0.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio Hinge GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio Hinge ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.28 | -11.4 dB |
| Peaking | 161 Hz   | 0.78 | -9.7 dB  |
| Peaking | 498 Hz   | 1.91 | -5.6 dB  |
| Peaking | 2006 Hz  | 1.15 | -7.5 dB  |
| Peaking | 18 Hz    | 1.11 | -2.1 dB  |
| Peaking | 1033 Hz  | 5.03 | 4.0 dB   |
| Peaking | 1471 Hz  | 5.28 | -2.3 dB  |
| Peaking | 7274 Hz  | 5.39 | -4.6 dB  |
| Peaking | 22050 Hz | 2.31 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.0 dB |
| Peaking | 62 Hz    | 1.41 | -8.2 dB  |
| Peaking | 125 Hz   | 1.41 | -13.5 dB |
| Peaking | 250 Hz   | 1.41 | -6.5 dB  |
| Peaking | 500 Hz   | 1.41 | -6.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -8.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 16000 Hz | 1.41 | 0.4 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20Hinge/Polk%20Audio%20Hinge.png)