# qdc Anole VX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.8; 25 -6.1; 28 -6.4; 31 -6.6; 34 -6.8; 37 -6.9; 41 -7.1; 45 -7.3; 49 -7.4; 54 -7.6; 60 -7.8; 66 -7.9; 72 -8.1; 79 -8.3; 87 -8.5; 96 -8.7; 106 -8.8; 116 -9.0; 128 -9.0; 141 -8.9; 155 -8.8; 170 -8.7; 187 -8.5; 206 -8.3; 227 -8.0; 249 -7.7; 274 -7.4; 302 -7.1; 332 -6.9; 365 -6.6; 402 -6.4; 442 -6.3; 486 -6.3; 535 -6.3; 588 -6.4; 647 -6.5; 712 -6.7; 783 -6.8; 861 -7.1; 947 -7.4; 1042 -8.0; 1146 -8.6; 1261 -9.1; 1387 -9.1; 1526 -8.5; 1678 -7.7; 1846 -6.8; 2031 -6.2; 2234 -5.6; 2457 -4.8; 2703 -4.1; 2973 -3.8; 3270 -3.4; 3597 -3.7; 3957 -4.7; 4353 -5.7; 4788 -2.8; 5267 -0.5; 5793 -1.3; 6373 -7.3; 7010 -10.4; 7711 -9.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -7.8; 16529 -9.4; 18182 -9.9; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole VX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole VX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 1329 Hz  |  1.97 | -3.0 dB |
| Peaking | 3008 Hz  |  1.91 | 3.1 dB  |
| Peaking | 5447 Hz  |  4.1  | 7.1 dB  |
| Peaking | 7073 Hz  |  4.54 | -5.7 dB |
| Peaking | 17849 Hz |  1.3  | -3.9 dB |
| Peaking | 18 Hz    |  1.81 | 1.3 dB  |
| Peaking | 92 Hz    |  0.86 | -1.9 dB |
| Peaking | 166 Hz   |  1.49 | -1.5 dB |
| Peaking | 4313 Hz  | 12.93 | -1.5 dB |
| Peaking | 10943 Hz |  1.24 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Anole%20VX/qdc%20Anole%20VX.png)