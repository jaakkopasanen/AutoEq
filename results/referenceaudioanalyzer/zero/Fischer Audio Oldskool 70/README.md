# Fischer Audio Oldskool 70
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.2; 66 -2.4; 72 -3.5; 79 -4.4; 87 -5.3; 96 -5.9; 106 -6.2; 116 -6.4; 128 -6.4; 141 -6.4; 155 -6.4; 170 -6.4; 187 -6.2; 206 -6.1; 227 -5.9; 249 -5.8; 274 -5.6; 302 -5.4; 332 -5.2; 365 -5.1; 402 -4.9; 442 -4.8; 486 -4.8; 535 -4.8; 588 -4.8; 647 -4.7; 712 -4.5; 783 -4.5; 861 -4.5; 947 -4.5; 1042 -4.5; 1146 -4.5; 1261 -4.5; 1387 -4.4; 1526 -4.1; 1678 -3.9; 1846 -4.9; 2031 -7.8; 2234 -11.3; 2457 -14.1; 2703 -15.3; 2973 -14.2; 3270 -11.1; 3597 -7.2; 3957 -4.0; 4353 -1.9; 4788 -1.5; 5267 -7.4; 5793 -11.9; 6373 -12.1; 7010 -10.1; 7711 -8.5; 8482 -7.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Oldskool 70 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Oldskool 70 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 0.79 | 7.0 dB   |
| Peaking | 2116 Hz | 0.41 | 5.3 dB   |
| Peaking | 2717 Hz | 1.88 | -14.9 dB |
| Peaking | 4625 Hz | 2.66 | 9.4 dB   |
| Peaking | 5934 Hz | 2.23 | -10.0 dB |
| Peaking | 36 Hz   | 3.05 | -1.2 dB  |
| Peaking | 57 Hz   | 2.64 | 2.1 dB   |
| Peaking | 111 Hz  | 1.72 | -1.4 dB  |
| Peaking | 1707 Hz | 1.56 | -2.0 dB  |
| Peaking | 1746 Hz | 3.58 | 3.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20Oldskool%2070/Fischer%20Audio%20Oldskool%2070.png)