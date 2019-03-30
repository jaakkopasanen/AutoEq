# Westone 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -11.0; 25 -11.4; 28 -11.8; 31 -12.2; 34 -12.5; 37 -12.7; 41 -12.9; 45 -13.1; 49 -13.2; 54 -13.3; 60 -13.4; 66 -13.5; 72 -13.6; 79 -13.7; 87 -13.7; 96 -13.7; 106 -13.7; 116 -13.7; 128 -13.5; 141 -13.3; 155 -13.3; 170 -13.3; 187 -13.1; 206 -13.0; 227 -12.7; 249 -12.4; 274 -12.0; 302 -11.6; 332 -11.2; 365 -10.8; 402 -10.3; 442 -9.6; 486 -9.0; 535 -8.3; 588 -7.6; 647 -6.8; 712 -6.1; 783 -5.4; 861 -4.8; 947 -4.4; 1042 -4.2; 1146 -4.2; 1261 -4.4; 1387 -4.9; 1526 -5.6; 1678 -6.2; 1846 -6.6; 2031 -6.6; 2234 -5.7; 2457 -3.3; 2703 -0.6; 2973 -0.5; 3270 -1.1; 3597 -2.8; 3957 -2.4; 4353 -0.5; 4788 -0.5; 5267 -0.6; 5793 -3.4; 6373 -4.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.46 | -4.5 dB |
| Peaking | 171 Hz  | 0.36 | -6.0 dB |
| Peaking | 926 Hz  | 1.37 | 3.6 dB  |
| Peaking | 2906 Hz | 3.74 | 5.7 dB  |
| Peaking | 4790 Hz | 2.17 | 6.1 dB  |
| Peaking | 1302 Hz | 4.23 | 0.9 dB  |
| Peaking | 2003 Hz | 2.84 | -1.5 dB |
| Peaking | 2588 Hz | 9.03 | 1.6 dB  |
| Peaking | 8640 Hz | 4.72 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Westone%203/Westone%203.png)