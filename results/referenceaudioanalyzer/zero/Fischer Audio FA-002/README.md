# Fischer Audio FA-002
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.9; 25 -5.3; 28 -5.8; 31 -6.2; 34 -6.5; 37 -6.7; 41 -6.9; 45 -7.0; 49 -7.2; 54 -7.3; 60 -7.3; 66 -7.5; 72 -7.9; 79 -8.5; 87 -9.0; 96 -9.4; 106 -9.6; 116 -9.6; 128 -9.6; 141 -9.6; 155 -9.6; 170 -9.6; 187 -9.5; 206 -9.3; 227 -9.3; 249 -9.3; 274 -9.2; 302 -9.0; 332 -8.9; 365 -8.6; 402 -8.5; 442 -8.3; 486 -8.0; 535 -7.8; 588 -7.4; 647 -6.9; 712 -6.3; 783 -5.5; 861 -4.6; 947 -3.6; 1042 -2.6; 1146 -1.3; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.8; 2031 -1.8; 2234 -2.1; 2457 -2.4; 2703 -3.9; 2973 -7.3; 3270 -10.8; 3597 -13.0; 3957 -13.5; 4353 -13.9; 4788 -15.2; 5267 -15.6; 5793 -13.5; 6373 -9.2; 7010 -5.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio FA-002 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio FA-002 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 1.23 | 3.0 dB   |
| Peaking | 134 Hz  | 0.66 | -2.9 dB  |
| Peaking | 649 Hz  | 0.52 | -4.7 dB  |
| Peaking | 1502 Hz | 0.53 | 9.7 dB   |
| Peaking | 4320 Hz | 1.44 | -12.3 dB |
| Peaking | 2613 Hz | 5.18 | 2.0 dB   |
| Peaking | 3410 Hz | 3.4  | -2.7 dB  |
| Peaking | 4320 Hz | 3.93 | 3.8 dB   |
| Peaking | 5579 Hz | 2.59 | -5.4 dB  |
| Peaking | 6930 Hz | 2.53 | 4.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB   |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 8.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -10.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20FA-002/Fischer%20Audio%20FA-002.png)