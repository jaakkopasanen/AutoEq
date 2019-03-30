# Pioneer HDJ-2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.7; 34 -3.3; 37 -4.9; 41 -6.7; 45 -8.3; 49 -9.6; 54 -10.9; 60 -12.1; 66 -13.1; 72 -13.7; 79 -14.2; 87 -14.1; 96 -13.8; 106 -13.3; 116 -13.0; 128 -12.9; 141 -12.8; 155 -12.6; 170 -12.5; 187 -12.2; 206 -11.9; 227 -11.3; 249 -10.6; 274 -9.6; 302 -8.6; 332 -7.9; 365 -7.6; 402 -7.1; 442 -6.4; 486 -5.6; 535 -5.5; 588 -5.9; 647 -6.2; 712 -6.5; 783 -6.7; 861 -6.8; 947 -6.9; 1042 -7.2; 1146 -7.4; 1261 -7.4; 1387 -7.4; 1526 -7.3; 1678 -6.8; 1846 -6.1; 2031 -5.0; 2234 -3.6; 2457 -2.3; 2703 -1.1; 2973 -0.5; 3270 -0.7; 3597 -3.6; 3957 -6.4; 4353 -6.3; 4788 -3.4; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.6; 11289 -6.6; 12418 -6.8; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.04 | 8.2 dB  |
| Peaking | 77 Hz   | 0.75 | -8.4 dB |
| Peaking | 189 Hz  | 1.56 | -3.6 dB |
| Peaking | 2884 Hz | 2.96 | 6.5 dB  |
| Peaking | 5819 Hz | 3.51 | 6.6 dB  |
| Peaking | 517 Hz  | 3.14 | 1.8 dB  |
| Peaking | 1350 Hz | 1.96 | -1.4 dB |
| Peaking | 4127 Hz | 4.73 | -4.7 dB |
| Peaking | 4184 Hz | 1.37 | 2.2 dB  |
| Peaking | 8440 Hz | 1.99 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | -7.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Pioneer%20HDJ-2000/Pioneer%20HDJ-2000.png)