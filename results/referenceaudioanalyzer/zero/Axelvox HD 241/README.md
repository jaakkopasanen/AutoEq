# Axelvox HD 241
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.4; 49 -2.1; 54 -2.7; 60 -3.0; 66 -3.2; 72 -3.3; 79 -3.5; 87 -3.6; 96 -3.8; 106 -3.6; 116 -3.5; 128 -3.5; 141 -3.5; 155 -3.5; 170 -3.5; 187 -3.4; 206 -3.1; 227 -2.8; 249 -2.5; 274 -2.6; 302 -2.6; 332 -2.5; 365 -2.5; 402 -2.6; 442 -2.5; 486 -2.6; 535 -2.8; 588 -3.1; 647 -3.0; 712 -3.1; 783 -3.6; 861 -4.3; 947 -4.6; 1042 -5.1; 1146 -5.5; 1261 -6.0; 1387 -6.6; 1526 -7.1; 1678 -7.1; 1846 -7.4; 2031 -8.1; 2234 -8.9; 2457 -9.3; 2703 -8.9; 2973 -7.7; 3270 -6.7; 3597 -6.0; 3957 -6.0; 4353 -10.4; 4788 -13.8; 5267 -14.4; 5793 -13.3; 6373 -13.3; 7010 -14.5; 7711 -15.8; 8482 -16.4; 9330 -16.3; 10263 -16.0; 11289 -15.3; 12418 -14.3; 13660 -14.2; 15026 -13.3; 16529 -8.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Axelvox HD 241 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Axelvox HD 241 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.47 | 6.1 dB  |
| Peaking | 298 Hz   | 0.61 | 3.6 dB  |
| Peaking | 672 Hz   | 1.56 | 2.0 dB  |
| Peaking | 8728 Hz  | 0.72 | -9.9 dB |
| Peaking | 14242 Hz | 2.24 | -4.1 dB |
| Peaking | 2388 Hz  | 2.44 | -2.3 dB |
| Peaking | 3828 Hz  | 2.52 | 6.4 dB  |
| Peaking | 4879 Hz  | 2.62 | -5.9 dB |
| Peaking | 6505 Hz  | 3.23 | 1.5 dB  |
| Peaking | 17505 Hz | 3.12 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB   |
| Peaking | 62 Hz    | 1.41 | 1.9 dB   |
| Peaking | 125 Hz   | 1.41 | 1.8 dB   |
| Peaking | 250 Hz   | 1.41 | 3.0 dB   |
| Peaking | 500 Hz   | 1.41 | 3.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -12.3 dB |
| Peaking | 16000 Hz | 1.41 | -5.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Axelvox%20HD%20241/Axelvox%20HD%20241.png)