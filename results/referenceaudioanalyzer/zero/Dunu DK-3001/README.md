# Dunu DK-3001
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.6; 25 -5.6; 28 -5.7; 31 -5.8; 34 -5.8; 37 -5.9; 41 -5.8; 45 -5.8; 49 -5.9; 54 -5.8; 60 -5.7; 66 -5.5; 72 -5.5; 79 -5.5; 87 -5.5; 96 -5.5; 106 -5.3; 116 -5.2; 128 -5.2; 141 -4.9; 155 -4.9; 170 -4.9; 187 -4.9; 206 -4.6; 227 -4.5; 249 -4.3; 274 -4.1; 302 -3.9; 332 -3.6; 365 -3.3; 402 -3.0; 442 -2.7; 486 -2.4; 535 -2.2; 588 -1.9; 647 -1.6; 712 -1.4; 783 -1.3; 861 -1.1; 947 -1.0; 1042 -1.3; 1146 -1.6; 1261 -2.1; 1387 -2.8; 1526 -3.9; 1678 -5.5; 1846 -7.5; 2031 -9.7; 2234 -11.5; 2457 -11.9; 2703 -10.6; 2973 -8.3; 3270 -6.0; 3597 -3.7; 3957 -3.5; 4353 -6.5; 4788 -8.2; 5267 -7.1; 5793 -3.7; 6373 -0.5; 7010 -1.1; 7711 -3.3; 8482 -3.6; 9330 -3.6; 10263 -3.6; 11289 -3.6; 12418 -3.6; 13660 -3.6; 15026 -3.6; 16529 -3.6; 18182 -3.6; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DK-3001 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DK-3001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 0.09 | -2.1 dB  |
| Peaking | 1556 Hz | 0.33 | 4.5 dB   |
| Peaking | 2327 Hz | 1.62 | -12.8 dB |
| Peaking | 4938 Hz | 4.6  | -5.8 dB  |
| Peaking | 6575 Hz | 6.67 | 4.1 dB   |
| Peaking | 2826 Hz | 8.38 | -0.9 dB  |
| Peaking | 3736 Hz | 6.67 | 2.4 dB   |
| Peaking | 6381 Hz | 2.22 | 1.8 dB   |
| Peaking | 6423 Hz | 1.07 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.8 dB |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Dunu%20DK-3001/Dunu%20DK-3001.png)