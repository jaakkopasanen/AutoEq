# Brainwavz HM3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.9; 25 -8.6; 28 -9.6; 31 -10.4; 34 -11.1; 37 -11.7; 41 -12.4; 45 -12.8; 49 -13.2; 54 -13.5; 60 -13.9; 66 -14.1; 72 -14.2; 79 -14.1; 87 -13.9; 96 -13.6; 106 -13.3; 116 -12.9; 128 -12.3; 141 -11.6; 155 -11.2; 170 -11.0; 187 -10.8; 206 -10.5; 227 -9.8; 249 -9.1; 274 -8.4; 302 -7.6; 332 -6.4; 365 -4.8; 402 -3.5; 442 -2.6; 486 -1.8; 535 -1.4; 588 -1.8; 647 -2.4; 712 -2.8; 783 -2.8; 861 -2.5; 947 -2.1; 1042 -2.3; 1146 -2.7; 1261 -2.8; 1387 -2.3; 1526 -1.8; 1678 -1.2; 1846 -0.7; 2031 -0.5; 2234 -1.0; 2457 -2.1; 2703 -2.8; 2973 -2.6; 3270 -2.0; 3597 -1.4; 3957 -3.6; 4353 -8.4; 4788 -9.9; 5267 -9.8; 5793 -11.5; 6373 -14.2; 7010 -14.1; 7711 -10.6; 8482 -6.4; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Brainwavz HM3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz HM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 82 Hz   | 0.36 | -8.1 dB |
| Peaking | 526 Hz  | 1.14 | 5.4 dB  |
| Peaking | 1917 Hz | 1.03 | 5.1 dB  |
| Peaking | 3568 Hz | 6.02 | 4.2 dB  |
| Peaking | 6372 Hz | 2.22 | -9.2 dB |
| Peaking | 20 Hz   | 2.51 | 1.8 dB  |
| Peaking | 142 Hz  | 5.41 | 0.8 dB  |
| Peaking | 954 Hz  | 7.1  | 1.2 dB  |
| Peaking | 7321 Hz | 5.82 | -2.5 dB |
| Peaking | 8788 Hz | 2.68 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -7.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 4.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | -5.2 dB |
| Peaking | 16000 Hz | 1.41 | 1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Brainwavz%20HM3/Brainwavz%20HM3.png)