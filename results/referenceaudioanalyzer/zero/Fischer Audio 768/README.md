# Fischer Audio 768
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.9; 25 -12.3; 28 -12.9; 31 -13.3; 34 -13.6; 37 -13.8; 41 -14.0; 45 -14.2; 49 -14.3; 54 -14.4; 60 -14.3; 66 -14.4; 72 -14.3; 79 -14.1; 87 -14.0; 96 -13.8; 106 -13.6; 116 -13.3; 128 -13.1; 141 -12.7; 155 -12.4; 170 -12.0; 187 -11.5; 206 -11.1; 227 -10.5; 249 -9.9; 274 -9.3; 302 -8.7; 332 -8.1; 365 -7.3; 402 -6.5; 442 -5.6; 486 -4.9; 535 -4.5; 588 -3.9; 647 -3.1; 712 -2.1; 783 -1.1; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -2.5; 3270 -5.9; 3597 -9.9; 3957 -12.8; 4353 -13.5; 4788 -12.8; 5267 -13.5; 5793 -17.4; 6373 -18.7; 7010 -16.0; 7711 -10.4; 8482 -7.3; 9330 -8.1; 10263 -8.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio 768 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio 768 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 33 Hz   | 0.48 | -3.4 dB  |
| Peaking | 118 Hz  | 0.27 | -6.5 dB  |
| Peaking | 1709 Hz | 0.24 | 7.8 dB   |
| Peaking | 4063 Hz | 2.76 | -9.9 dB  |
| Peaking | 6253 Hz | 2.17 | -15.9 dB |
| Peaking | 849 Hz  | 3.61 | 1.1 dB   |
| Peaking | 1509 Hz | 2.26 | -0.4 dB  |
| Peaking | 2718 Hz | 4.57 | 2.1 dB   |
| Peaking | 4479 Hz | 0.17 | -0.4 dB  |
| Peaking | 8320 Hz | 8.02 | 2.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -6.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.1 dB |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | 1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20768/Fischer%20Audio%20768.png)