# Fischer Audio Titan
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.1; 34 -2.0; 37 -2.8; 41 -3.7; 45 -4.5; 49 -5.1; 54 -5.8; 60 -6.4; 66 -6.9; 72 -7.0; 79 -6.8; 87 -6.9; 96 -7.2; 106 -7.4; 116 -7.7; 128 -7.9; 141 -8.1; 155 -8.1; 170 -8.0; 187 -7.8; 206 -7.8; 227 -7.8; 249 -7.8; 274 -7.7; 302 -7.4; 332 -7.4; 365 -7.4; 402 -7.2; 442 -6.7; 486 -6.3; 535 -6.4; 588 -6.5; 647 -6.5; 712 -6.7; 783 -6.8; 861 -6.8; 947 -6.8; 1042 -7.0; 1146 -7.1; 1261 -7.1; 1387 -6.9; 1526 -6.3; 1678 -6.5; 1846 -7.4; 2031 -8.4; 2234 -8.9; 2457 -9.2; 2703 -9.2; 2973 -8.8; 3270 -7.2; 3597 -4.2; 3957 -1.1; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.9; 7010 -7.6; 7711 -12.3; 8482 -13.4; 9330 -11.1; 10263 -8.3; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Titan GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Titan ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 1.02 | 6.6 dB   |
| Peaking | 142 Hz  | 0.5  | -1.6 dB  |
| Peaking | 2745 Hz | 1.45 | -7.2 dB  |
| Peaking | 5301 Hz | 0.79 | 11.1 dB  |
| Peaking | 8158 Hz | 2.01 | -13.6 dB |
| Peaking | 508 Hz  | 5.23 | 0.7 dB   |
| Peaking | 1121 Hz | 4.22 | -0.7 dB  |
| Peaking | 4010 Hz | 9.85 | 1.5 dB   |
| Peaking | 4985 Hz | 8.09 | -1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20Titan/Fischer%20Audio%20Titan.png)