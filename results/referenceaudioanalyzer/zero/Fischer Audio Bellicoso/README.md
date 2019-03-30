# Fischer Audio Bellicoso
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.7; 23 -18.8; 25 -18.9; 28 -19.0; 31 -19.0; 34 -18.9; 37 -18.8; 41 -18.7; 45 -18.7; 49 -18.7; 54 -18.6; 60 -18.4; 66 -18.3; 72 -18.1; 79 -17.9; 87 -17.6; 96 -17.4; 106 -17.1; 116 -16.7; 128 -16.3; 141 -15.8; 155 -15.4; 170 -14.8; 187 -14.2; 206 -13.6; 227 -12.9; 249 -12.4; 274 -12.0; 302 -11.6; 332 -11.2; 365 -10.6; 402 -9.9; 442 -9.2; 486 -8.4; 535 -7.6; 588 -6.8; 647 -6.0; 712 -5.2; 783 -4.4; 861 -3.5; 947 -2.7; 1042 -2.0; 1146 -1.5; 1261 -1.0; 1387 -0.6; 1526 -0.5; 1678 -0.6; 1846 -1.9; 2031 -4.2; 2234 -5.6; 2457 -5.6; 2703 -4.5; 2973 -3.3; 3270 -2.2; 3597 -1.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.1; 6373 -6.9; 7010 -9.5; 7711 -7.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Bellicoso GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Bellicoso ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.11 | -12.4 dB |
| Peaking | 1653 Hz  | 0.64 | 7.9 dB   |
| Peaking | 2298 Hz  | 2.21 | -6.7 dB  |
| Peaking | 5085 Hz  | 1.33 | 6.2 dB   |
| Peaking | 6923 Hz  | 3.1  | -7.1 dB  |
| Peaking | 389 Hz   | 3.72 | -0.5 dB  |
| Peaking | 4693 Hz  | 4.83 | -1.9 dB  |
| Peaking | 4754 Hz  | 2.12 | 1.2 dB   |
| Peaking | 10994 Hz | 1.68 | -0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.0 dB |
| Peaking | 62 Hz    | 1.41 | -8.5 dB  |
| Peaking | 125 Hz   | 1.41 | -7.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20Bellicoso/Fischer%20Audio%20Bellicoso.png)