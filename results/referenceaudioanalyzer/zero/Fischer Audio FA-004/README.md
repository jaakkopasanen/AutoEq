# Fischer Audio FA-004
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.6; 31 -2.7; 34 -3.7; 37 -4.5; 41 -5.4; 45 -6.1; 49 -6.6; 54 -7.0; 60 -7.1; 66 -7.1; 72 -7.0; 79 -7.2; 87 -7.4; 96 -7.8; 106 -7.8; 116 -7.8; 128 -7.8; 141 -7.7; 155 -7.7; 170 -7.4; 187 -7.2; 206 -6.9; 227 -6.3; 249 -5.7; 274 -5.2; 302 -4.8; 332 -4.6; 365 -4.5; 402 -4.7; 442 -5.2; 486 -5.5; 535 -6.0; 588 -6.7; 647 -7.4; 712 -7.8; 783 -7.7; 861 -7.3; 947 -6.3; 1042 -5.5; 1146 -5.8; 1261 -6.2; 1387 -6.1; 1526 -5.6; 1678 -4.8; 1846 -3.9; 2031 -3.1; 2234 -2.7; 2457 -2.6; 2703 -3.0; 2973 -3.3; 3270 -3.2; 3597 -2.5; 3957 -3.6; 4353 -8.0; 4788 -9.7; 5267 -9.6; 5793 -9.7; 6373 -10.1; 7010 -10.0; 7711 -10.9; 8482 -12.1; 9330 -12.5; 10263 -12.6; 11289 -12.9; 12418 -12.0; 13660 -8.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio FA-004 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio FA-004 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 2.21 | 6.7 dB  |
| Peaking | 2351 Hz  | 1.71 | 4.4 dB  |
| Peaking | 3766 Hz  | 2.85 | 7.3 dB  |
| Peaking | 4481 Hz  | 1.5  | -5.2 dB |
| Peaking | 10288 Hz | 1.21 | -6.6 dB |
| Peaking | 16 Hz    | 0.5  | 0.9 dB  |
| Peaking | 146 Hz   | 0.49 | -1.9 dB |
| Peaking | 333 Hz   | 1.07 | 3.1 dB  |
| Peaking | 713 Hz   | 2.96 | -2.0 dB |
| Peaking | 15214 Hz | 3.71 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20FA-004/Fischer%20Audio%20FA-004.png)