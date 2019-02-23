# Fischer Audio SBA-03
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.7; 25 -1.8; 28 -2.0; 31 -2.2; 34 -2.4; 37 -2.7; 41 -3.0; 45 -3.2; 49 -3.4; 54 -3.7; 60 -4.1; 66 -4.4; 72 -4.8; 79 -5.2; 87 -5.7; 96 -6.2; 106 -6.5; 116 -6.7; 128 -7.1; 141 -7.4; 155 -7.6; 170 -7.7; 187 -7.9; 206 -8.0; 227 -8.0; 249 -8.1; 274 -7.9; 302 -7.9; 332 -7.7; 365 -7.5; 402 -7.3; 442 -7.0; 486 -6.9; 535 -6.5; 588 -6.0; 647 -5.9; 712 -5.9; 783 -5.6; 861 -5.7; 947 -5.9; 1042 -6.1; 1146 -6.4; 1261 -6.7; 1387 -7.3; 1526 -7.8; 1678 -8.3; 1846 -8.6; 2031 -8.9; 2234 -9.8; 2457 -10.4; 2703 -9.5; 2973 -5.3; 3270 -1.0; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -4.6; 5267 -8.2; 5793 -10.7; 6373 -5.0; 7010 -4.0; 7711 -6.2; 8482 -7.7; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio SBA-03 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio SBA-03 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 24 Hz   |  1.23 | 5.0 dB   |
| Peaking | 49 Hz   |  1.94 | 2.3 dB   |
| Peaking | 2595 Hz |  1.63 | -10.1 dB |
| Peaking | 3444 Hz |  1.44 | 11.6 dB  |
| Peaking | 5574 Hz |  6.92 | -7.5 dB  |
| Peaking | 242 Hz  |  0.92 | -1.8 dB  |
| Peaking | 790 Hz  |  1.42 | 1.2 dB   |
| Peaking | 1600 Hz |  4.17 | -0.8 dB  |
| Peaking | 6793 Hz | 10.39 | 3.2 dB   |
| Peaking | 8850 Hz |  5.37 | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20SBA-03/Fischer%20Audio%20SBA-03.png)