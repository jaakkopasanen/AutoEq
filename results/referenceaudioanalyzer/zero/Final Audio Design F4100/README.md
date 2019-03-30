# Final Audio Design F4100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.9; 25 -2.6; 28 -3.5; 31 -4.2; 34 -4.7; 37 -5.2; 41 -5.8; 45 -6.3; 49 -6.8; 54 -7.2; 60 -7.5; 66 -7.8; 72 -8.0; 79 -8.3; 87 -8.6; 96 -8.7; 106 -8.9; 116 -9.0; 128 -9.3; 141 -9.3; 155 -9.3; 170 -9.1; 187 -8.8; 206 -8.6; 227 -8.6; 249 -8.8; 274 -9.8; 302 -10.9; 332 -11.2; 365 -11.0; 402 -10.5; 442 -10.1; 486 -9.8; 535 -9.5; 588 -9.2; 647 -8.9; 712 -8.5; 783 -8.1; 861 -7.8; 947 -7.4; 1042 -7.0; 1146 -6.7; 1261 -6.3; 1387 -6.1; 1526 -5.8; 1678 -5.7; 1846 -5.8; 2031 -6.1; 2234 -6.7; 2457 -7.8; 2703 -9.9; 2973 -12.4; 3270 -13.0; 3597 -10.8; 3957 -6.6; 4353 -3.5; 4788 -1.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Design F4100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Design F4100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.12 | 5.8 dB  |
| Peaking | 106 Hz  | 0.76 | -2.4 dB |
| Peaking | 384 Hz  | 1.1  | -4.2 dB |
| Peaking | 3228 Hz | 3.49 | -8.5 dB |
| Peaking | 5358 Hz | 2.05 | 7.3 dB  |
| Peaking | 441 Hz  | 5.04 | 0.6 dB  |
| Peaking | 693 Hz  | 1.72 | -0.6 dB |
| Peaking | 1663 Hz | 2.15 | 1.4 dB  |
| Peaking | 6496 Hz | 5.34 | 3.1 dB  |
| Peaking | 7384 Hz | 1.82 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Final%20Audio%20Design%20F4100/Final%20Audio%20Design%20F4100.png)