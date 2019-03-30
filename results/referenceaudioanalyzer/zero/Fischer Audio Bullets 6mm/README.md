# Fischer Audio Bullets 6mm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.8; 23 -15.8; 25 -15.8; 28 -15.8; 31 -15.8; 34 -15.8; 37 -15.8; 41 -15.8; 45 -15.8; 49 -15.8; 54 -15.8; 60 -15.8; 66 -15.7; 72 -15.5; 79 -15.5; 87 -15.3; 96 -15.1; 106 -14.9; 116 -14.7; 128 -14.5; 141 -14.2; 155 -13.9; 170 -13.6; 187 -13.1; 206 -12.6; 227 -11.9; 249 -11.3; 274 -11.0; 302 -11.0; 332 -10.8; 365 -10.3; 402 -9.6; 442 -8.8; 486 -8.1; 535 -7.3; 588 -6.6; 647 -5.9; 712 -5.2; 783 -4.5; 861 -3.9; 947 -3.3; 1042 -2.7; 1146 -2.2; 1261 -1.7; 1387 -1.3; 1526 -0.7; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.7; 2457 -1.0; 2703 -1.6; 2973 -2.3; 3270 -3.0; 3597 -3.7; 3957 -4.1; 4353 -4.2; 4788 -4.5; 5267 -4.4; 5793 -5.6; 6373 -9.7; 7010 -11.7; 7711 -9.1; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Bullets 6mm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Bullets 6mm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 35 Hz   |  0.11 | -9.4 dB |
| Peaking | 1707 Hz |  0.58 | 6.4 dB  |
| Peaking | 5669 Hz |  2.55 | 1.7 dB  |
| Peaking | 6857 Hz |  3.89 | -7.4 dB |
| Peaking | 255 Hz  |  3.73 | 0.7 dB  |
| Peaking | 351 Hz  |  3.57 | -0.7 dB |
| Peaking | 3766 Hz |  6.09 | -0.5 dB |
| Peaking | 8352 Hz | 12.55 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20Bullets%206mm/Fischer%20Audio%20Bullets%206mm.png)