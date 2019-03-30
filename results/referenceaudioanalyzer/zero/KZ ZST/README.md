# KZ ZST
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.7; 23 -15.6; 25 -15.6; 28 -15.5; 31 -15.4; 34 -15.3; 37 -15.2; 41 -15.0; 45 -14.7; 49 -14.5; 54 -14.2; 60 -13.9; 66 -13.6; 72 -13.2; 79 -12.9; 87 -12.5; 96 -12.0; 106 -11.6; 116 -11.1; 128 -10.6; 141 -10.0; 155 -9.5; 170 -9.1; 187 -8.6; 206 -8.2; 227 -7.7; 249 -7.2; 274 -6.7; 302 -6.2; 332 -5.8; 365 -5.3; 402 -4.9; 442 -4.6; 486 -4.3; 535 -4.0; 588 -3.7; 647 -3.6; 712 -3.5; 783 -3.5; 861 -3.6; 947 -3.7; 1042 -4.1; 1146 -4.6; 1261 -5.3; 1387 -6.4; 1526 -7.8; 1678 -9.8; 1846 -12.2; 2031 -14.0; 2234 -14.2; 2457 -12.7; 2703 -10.6; 2973 -9.4; 3270 -8.8; 3597 -7.1; 3957 -3.7; 4353 -2.3; 4788 -4.0; 5267 -3.8; 5793 -0.8; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -7.0; 11289 -7.8; 12418 -6.4; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZST GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZST ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.47 | -9.6 dB |
| Peaking | 94 Hz    | 1.01 | -3.3 dB |
| Peaking | 2212 Hz  | 2.58 | -9.2 dB |
| Peaking | 4271 Hz  | 6.7  | 4.4 dB  |
| Peaking | 6126 Hz  | 4.41 | 6.5 dB  |
| Peaking | 211 Hz   | 1.21 | -1.3 dB |
| Peaking | 852 Hz   | 0.44 | 3.0 dB  |
| Peaking | 1746 Hz  | 2.63 | -3.2 dB |
| Peaking | 3186 Hz  | 3.97 | -2.2 dB |
| Peaking | 11042 Hz | 4.06 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.2 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -9.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/KZ%20ZST/KZ%20ZST.png)