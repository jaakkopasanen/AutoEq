# Audiofly AF56
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.3; 23 -17.2; 25 -17.2; 28 -17.2; 31 -17.1; 34 -17.0; 37 -16.9; 41 -16.8; 45 -16.6; 49 -16.4; 54 -16.3; 60 -16.1; 66 -15.9; 72 -15.7; 79 -15.4; 87 -15.1; 96 -14.7; 106 -14.2; 116 -13.6; 128 -13.1; 141 -13.1; 155 -12.8; 170 -12.1; 187 -11.6; 206 -11.4; 227 -11.0; 249 -10.4; 274 -9.5; 302 -8.9; 332 -8.5; 365 -7.9; 402 -7.0; 442 -6.2; 486 -5.4; 535 -4.7; 588 -3.9; 647 -3.1; 712 -2.4; 783 -1.7; 861 -1.0; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -1.1; 2234 -2.5; 2457 -4.4; 2703 -6.6; 2973 -8.6; 3270 -9.4; 3597 -8.7; 3957 -7.8; 4353 -8.3; 4788 -9.2; 5267 -10.5; 5793 -13.3; 6373 -14.3; 7010 -11.2; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audiofly AF56 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audiofly AF56 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 81 Hz    | 0.16 | -6.6 dB  |
| Peaking | 1559 Hz  | 0.3  | 8.5 dB   |
| Peaking | 3221 Hz  | 1.54 | -8.7 dB  |
| Peaking | 6079 Hz  | 2.65 | -10.4 dB |
| Peaking | 17 Hz    | 0.72 | -5.1 dB  |
| Peaking | 42 Hz    | 0.63 | -2.5 dB  |
| Peaking | 79 Hz    | 1.65 | -0.8 dB  |
| Peaking | 225 Hz   | 1.35 | -0.2 dB  |
| Peaking | 12544 Hz | 2.61 | -0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.3 dB |
| Peaking | 62 Hz    | 1.41 | -7.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 16000 Hz | 1.41 | 0.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audiofly%20AF56/Audiofly%20AF56.png)