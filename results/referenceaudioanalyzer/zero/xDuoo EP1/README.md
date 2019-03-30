# xDuoo EP1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -13.9; 25 -13.9; 28 -13.9; 31 -13.9; 34 -13.9; 37 -13.9; 41 -13.9; 45 -13.9; 49 -13.9; 54 -13.9; 60 -13.9; 66 -13.7; 72 -13.6; 79 -13.5; 87 -13.6; 96 -13.5; 106 -13.3; 116 -13.2; 128 -13.2; 141 -12.9; 155 -12.9; 170 -12.9; 187 -12.8; 206 -12.6; 227 -12.6; 249 -12.3; 274 -12.0; 302 -11.7; 332 -11.4; 365 -11.0; 402 -10.5; 442 -10.0; 486 -9.4; 535 -8.6; 588 -7.7; 647 -6.6; 712 -5.2; 783 -3.7; 861 -2.1; 947 -0.8; 1042 -0.8; 1146 -1.8; 1261 -3.0; 1387 -3.9; 1526 -4.4; 1678 -4.5; 1846 -4.5; 2031 -4.4; 2234 -4.1; 2457 -3.9; 2703 -3.8; 2973 -3.8; 3270 -3.9; 3597 -4.2; 3957 -4.7; 4353 -5.9; 4788 -6.5; 5267 -5.4; 5793 -2.7; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`xDuoo EP1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `xDuoo EP1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 58 Hz    | 0.04 | -7.8 dB |
| Peaking | 947 Hz   | 1.89 | 6.3 dB  |
| Peaking | 1158 Hz  | 0.38 | 4.1 dB  |
| Peaking | 6353 Hz  | 6.56 | 5.5 dB  |
| Peaking | 22050 Hz | 1.06 | 0.2 dB  |
| Peaking | 142 Hz   | 3.33 | 0.3 dB  |
| Peaking | 3253 Hz  | 2.06 | 1.1 dB  |
| Peaking | 4830 Hz  | 3.38 | -2.2 dB |
| Peaking | 5765 Hz  | 4.62 | 1.3 dB  |
| Peaking | 8493 Hz  | 2.83 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -3.4 dB |
| Peaking | 1000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/xDuoo%20EP1/xDuoo%20EP1.png)