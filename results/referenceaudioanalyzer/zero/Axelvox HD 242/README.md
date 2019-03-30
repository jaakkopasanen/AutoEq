# Axelvox HD 242
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.8; 60 -3.0; 66 -3.9; 72 -4.6; 79 -5.2; 87 -5.5; 96 -5.6; 106 -5.5; 116 -5.3; 128 -5.1; 141 -4.8; 155 -4.5; 170 -4.3; 187 -3.9; 206 -3.4; 227 -2.9; 249 -2.6; 274 -2.5; 302 -2.3; 332 -2.3; 365 -2.3; 402 -2.3; 442 -2.3; 486 -2.3; 535 -2.3; 588 -2.4; 647 -2.4; 712 -2.7; 783 -3.3; 861 -3.7; 947 -4.0; 1042 -4.4; 1146 -5.0; 1261 -5.6; 1387 -6.2; 1526 -6.8; 1678 -6.9; 1846 -7.2; 2031 -7.7; 2234 -8.3; 2457 -9.0; 2703 -9.4; 2973 -8.9; 3270 -8.2; 3597 -7.6; 3957 -6.7; 4353 -5.4; 4788 -6.4; 5267 -13.4; 5793 -16.7; 6373 -16.7; 7010 -15.4; 7711 -15.5; 8482 -16.3; 9330 -16.3; 10263 -14.8; 11289 -13.6; 12418 -13.5; 13660 -13.4; 15026 -13.3; 16529 -12.6; 18182 -8.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Axelvox HD 242 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Axelvox HD 242 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.83 | 6.8 dB  |
| Peaking | 414 Hz   | 0.64 | 4.7 dB  |
| Peaking | 6003 Hz  | 4.46 | -7.6 dB |
| Peaking | 8755 Hz  | 1.36 | -8.5 dB |
| Peaking | 14982 Hz | 0.96 | -6.2 dB |
| Peaking | 50 Hz    | 4.46 | 1.6 dB  |
| Peaking | 88 Hz    | 2.63 | -1.0 dB |
| Peaking | 938 Hz   | 1.4  | 1.2 dB  |
| Peaking | 2799 Hz  | 0.7  | -2.3 dB |
| Peaking | 4407 Hz  | 4.21 | 5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB   |
| Peaking | 62 Hz    | 1.41 | 1.6 dB   |
| Peaking | 125 Hz   | 1.41 | -0.2 dB  |
| Peaking | 250 Hz   | 1.41 | 3.4 dB   |
| Peaking | 500 Hz   | 1.41 | 3.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -12.3 dB |
| Peaking | 16000 Hz | 1.41 | -7.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Axelvox%20HD%20242/Axelvox%20HD%20242.png)