# Fischer Audio TS-9002
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.9; 23 -18.9; 25 -18.9; 28 -18.8; 31 -18.7; 34 -18.6; 37 -18.6; 41 -18.5; 45 -18.5; 49 -18.3; 54 -18.2; 60 -18.0; 66 -17.9; 72 -17.7; 79 -17.5; 87 -17.2; 96 -17.0; 106 -16.7; 116 -16.4; 128 -16.1; 141 -15.7; 155 -15.3; 170 -14.9; 187 -14.4; 206 -13.9; 227 -13.3; 249 -12.6; 274 -12.0; 302 -11.5; 332 -10.8; 365 -10.0; 402 -9.0; 442 -8.0; 486 -6.8; 535 -5.7; 588 -4.7; 647 -4.0; 712 -3.5; 783 -3.3; 861 -3.3; 947 -3.3; 1042 -3.1; 1146 -2.7; 1261 -2.1; 1387 -1.5; 1526 -0.8; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -1.1; 2703 -2.3; 2973 -4.0; 3270 -5.6; 3597 -6.5; 3957 -7.0; 4353 -7.3; 4788 -7.7; 5267 -9.1; 5793 -10.5; 6373 -9.5; 7010 -5.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio TS-9002 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio TS-9002 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 84 Hz   |  0.21 | -9.6 dB |
| Peaking | 700 Hz  |  0.87 | 4.7 dB  |
| Peaking | 1924 Hz |  1.26 | 6.2 dB  |
| Peaking | 5531 Hz |  2.96 | -4.4 dB |
| Peaking | 19 Hz   |  0.79 | -6.4 dB |
| Peaking | 48 Hz   |  0.77 | -1.3 dB |
| Peaking | 2535 Hz |  5.58 | 1.2 dB  |
| Peaking | 3582 Hz |  3.58 | -1.4 dB |
| Peaking | 7156 Hz | 11.47 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.0 dB |
| Peaking | 62 Hz    | 1.41 | -8.1 dB  |
| Peaking | 125 Hz   | 1.41 | -7.5 dB  |
| Peaking | 250 Hz   | 1.41 | -5.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 4000 Hz  | 1.41 | -2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20TS-9002/Fischer%20Audio%20TS-9002.png)