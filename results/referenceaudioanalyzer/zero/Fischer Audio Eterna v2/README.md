# Fischer Audio Eterna v2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.5; 25 -12.8; 28 -13.2; 31 -13.5; 34 -13.6; 37 -13.8; 41 -13.9; 45 -14.0; 49 -14.0; 54 -14.0; 60 -14.0; 66 -13.9; 72 -13.9; 79 -13.7; 87 -13.5; 96 -13.6; 106 -13.4; 116 -13.2; 128 -13.2; 141 -12.9; 155 -12.9; 170 -12.6; 187 -12.5; 206 -12.3; 227 -12.1; 249 -11.9; 274 -11.8; 302 -11.6; 332 -11.5; 365 -11.3; 402 -11.1; 442 -10.9; 486 -10.7; 535 -10.6; 588 -10.4; 647 -10.3; 712 -10.1; 783 -10.0; 861 -9.9; 947 -9.7; 1042 -9.4; 1146 -9.1; 1261 -8.7; 1387 -8.2; 1526 -7.4; 1678 -6.5; 1846 -5.4; 2031 -4.4; 2234 -3.5; 2457 -2.7; 2703 -2.5; 2973 -2.5; 3270 -2.2; 3597 -1.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Eterna v2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Eterna v2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.26 | -3.6 dB |
| Peaking | 206 Hz  | 0.1  | -4.8 dB |
| Peaking | 4904 Hz | 0.52 | 8.6 dB  |
| Peaking | 8697 Hz | 1.05 | -5.3 dB |
| Peaking | 1315 Hz | 2.32 | -0.8 dB |
| Peaking | 2456 Hz | 1.85 | 1.9 dB  |
| Peaking | 3028 Hz | 1.99 | -1.6 dB |
| Peaking | 6359 Hz | 5.08 | 1.6 dB  |
| Peaking | 7411 Hz | 6.52 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20Eterna%20v2/Fischer%20Audio%20Eterna%20v2.png)