# Fischer Audio Coda
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.9; 25 -8.6; 28 -9.6; 31 -10.4; 34 -11.1; 37 -11.7; 41 -12.2; 45 -12.6; 49 -13.0; 54 -13.3; 60 -13.6; 66 -13.7; 72 -13.9; 79 -14.3; 87 -14.7; 96 -14.9; 106 -15.2; 116 -15.3; 128 -15.4; 141 -15.4; 155 -15.3; 170 -15.2; 187 -15.0; 206 -14.7; 227 -14.2; 249 -13.7; 274 -13.1; 302 -12.2; 332 -11.2; 365 -9.9; 402 -8.4; 442 -6.8; 486 -5.0; 535 -3.1; 588 -1.2; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.9; 1146 -2.8; 1261 -4.0; 1387 -4.9; 1526 -5.8; 1678 -6.4; 1846 -6.7; 2031 -6.8; 2234 -6.8; 2457 -6.7; 2703 -6.4; 2973 -5.9; 3270 -5.3; 3597 -5.2; 3957 -6.6; 4353 -8.2; 4788 -9.0; 5267 -9.1; 5793 -7.7; 6373 -4.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Coda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Coda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 66 Hz   | 0.5  | -5.2 dB |
| Peaking | 216 Hz  | 0.51 | -7.5 dB |
| Peaking | 700 Hz  | 1.06 | 9.4 dB  |
| Peaking | 5116 Hz | 3.44 | -3.4 dB |
| Peaking | 6671 Hz | 6.86 | 4.4 dB  |
| Peaking | 20 Hz   | 2.43 | 1.4 dB  |
| Peaking | 756 Hz  | 6.34 | -1.1 dB |
| Peaking | 1021 Hz | 3.74 | 2.0 dB  |
| Peaking | 1834 Hz | 1.44 | -1.4 dB |
| Peaking | 3406 Hz | 4.87 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB |
| Peaking | 125 Hz   | 1.41 | -7.2 dB |
| Peaking | 250 Hz   | 1.41 | -7.8 dB |
| Peaking | 500 Hz   | 1.41 | 3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20Coda/Fischer%20Audio%20Coda.png)