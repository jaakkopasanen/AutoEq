# Pioneer HDJ-1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.0; 60 -2.0; 66 -2.8; 72 -3.5; 79 -4.4; 87 -5.1; 96 -5.6; 106 -6.0; 116 -6.2; 128 -6.3; 141 -6.5; 155 -6.5; 170 -6.5; 187 -6.5; 206 -6.3; 227 -6.2; 249 -5.9; 274 -5.6; 302 -5.5; 332 -5.2; 365 -4.7; 402 -4.1; 442 -3.3; 486 -2.5; 535 -2.3; 588 -3.1; 647 -4.7; 712 -6.1; 783 -6.8; 861 -6.9; 947 -6.9; 1042 -7.6; 1146 -8.4; 1261 -9.0; 1387 -9.5; 1526 -9.4; 1678 -8.8; 1846 -7.9; 2031 -7.0; 2234 -6.4; 2457 -5.8; 2703 -4.9; 2973 -3.8; 3270 -1.9; 3597 -4.6; 3957 -11.8; 4353 -14.6; 4788 -13.7; 5267 -11.2; 5793 -11.7; 6373 -11.7; 7010 -8.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 33 Hz   | 0.77 | 6.9 dB   |
| Peaking | 505 Hz  | 2.24 | 4.6 dB   |
| Peaking | 1396 Hz | 1.79 | -3.2 dB  |
| Peaking | 3396 Hz | 2.29 | 12.1 dB  |
| Peaking | 4246 Hz | 1.79 | -13.4 dB |
| Peaking | 33 Hz   | 1.54 | -3.9 dB  |
| Peaking | 43 Hz   | 0.26 | 3.5 dB   |
| Peaking | 107 Hz  | 0.74 | -3.4 dB  |
| Peaking | 6415 Hz | 4.43 | -5.2 dB  |
| Peaking | 7162 Hz | 1.94 | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 4.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Pioneer%20HDJ-1000/Pioneer%20HDJ-1000.png)