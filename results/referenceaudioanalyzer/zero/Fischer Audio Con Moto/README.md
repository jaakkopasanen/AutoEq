# Fischer Audio Con Moto
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -10.9; 25 -11.1; 28 -11.4; 31 -11.6; 34 -11.7; 37 -11.8; 41 -11.8; 45 -11.9; 49 -11.8; 54 -11.8; 60 -11.8; 66 -11.8; 72 -11.8; 79 -11.8; 87 -11.8; 96 -11.9; 106 -12.1; 116 -12.4; 128 -12.5; 141 -12.5; 155 -11.6; 170 -9.6; 187 -6.3; 206 -2.8; 227 -1.3; 249 -1.1; 274 -1.2; 302 -1.5; 332 -1.9; 365 -2.1; 402 -2.5; 442 -3.2; 486 -3.9; 535 -4.5; 588 -5.1; 647 -5.8; 712 -6.4; 783 -7.0; 861 -7.6; 947 -8.1; 1042 -8.3; 1146 -8.2; 1261 -7.6; 1387 -6.5; 1526 -5.3; 1678 -4.0; 1846 -2.8; 2031 -1.7; 2234 -0.9; 2457 -0.5; 2703 -0.6; 2973 -1.5; 3270 -2.7; 3597 -3.5; 3957 -3.7; 4353 -4.1; 4788 -6.1; 5267 -8.9; 5793 -11.1; 6373 -12.4; 7010 -10.7; 7711 -5.9; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Con Moto GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Con Moto ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 144 Hz  | 1.14 | -9.9 dB |
| Peaking | 196 Hz  | 0.08 | -9.7 dB |
| Peaking | 246 Hz  | 0.51 | 17.9 dB |
| Peaking | 2437 Hz | 1.04 | 8.9 dB  |
| Peaking | 6230 Hz | 3.44 | -8.0 dB |
| Peaking | 309 Hz  | 3.34 | -1.5 dB |
| Peaking | 459 Hz  | 0.64 | 0.8 dB  |
| Peaking | 962 Hz  | 3.23 | -1.1 dB |
| Peaking | 1184 Hz | 4.72 | -1.0 dB |
| Peaking | 8236 Hz | 7.11 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -8.3 dB |
| Peaking | 250 Hz   | 1.41 | 6.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.9 dB |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20Con%20Moto/Fischer%20Audio%20Con%20Moto.png)