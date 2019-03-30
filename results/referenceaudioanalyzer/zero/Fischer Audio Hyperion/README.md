# Fischer Audio Hyperion
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -1.2; 41 -2.5; 45 -3.6; 49 -4.6; 54 -5.5; 60 -6.2; 66 -6.8; 72 -7.4; 79 -7.9; 87 -8.4; 96 -8.8; 106 -8.8; 116 -8.8; 128 -8.8; 141 -8.8; 155 -8.8; 170 -8.6; 187 -8.4; 206 -8.0; 227 -7.7; 249 -7.5; 274 -7.4; 302 -7.1; 332 -6.8; 365 -6.6; 402 -6.5; 442 -6.3; 486 -6.1; 535 -5.8; 588 -5.3; 647 -4.6; 712 -4.7; 783 -5.9; 861 -7.5; 947 -9.1; 1042 -10.3; 1146 -11.0; 1261 -11.4; 1387 -11.7; 1526 -11.2; 1678 -9.8; 1846 -7.4; 2031 -4.8; 2234 -2.7; 2457 -1.5; 2703 -0.8; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.8; 5793 -5.0; 6373 -8.4; 7010 -10.8; 7711 -13.3; 8482 -13.6; 9330 -11.0; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Hyperion GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Hyperion ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.66 | 8.5 dB   |
| Peaking | 85 Hz    | 0.38 | -4.2 dB  |
| Peaking | 1402 Hz  | 0.99 | -16.1 dB |
| Peaking | 2549 Hz  | 0.27 | 12.2 dB  |
| Peaking | 7916 Hz  | 1.6  | -14.0 dB |
| Peaking | 699 Hz   | 5.39 | 1.7 dB   |
| Peaking | 986 Hz   | 5.11 | -1.7 dB  |
| Peaking | 5212 Hz  | 6.27 | 2.5 dB   |
| Peaking | 6183 Hz  | 6.07 | -1.8 dB  |
| Peaking | 15279 Hz | 1.81 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 9.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20Hyperion/Fischer%20Audio%20Hyperion.png)