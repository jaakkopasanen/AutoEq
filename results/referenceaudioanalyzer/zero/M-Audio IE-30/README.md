# M-Audio IE-30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.3; 25 -10.4; 28 -10.6; 31 -10.8; 34 -10.8; 37 -10.9; 41 -10.9; 45 -10.9; 49 -10.9; 54 -10.9; 60 -10.9; 66 -10.9; 72 -10.9; 79 -10.9; 87 -10.8; 96 -10.6; 106 -10.5; 116 -10.5; 128 -10.3; 141 -10.2; 155 -10.2; 170 -10.0; 187 -9.9; 206 -9.9; 227 -9.8; 249 -9.6; 274 -9.3; 302 -9.1; 332 -8.8; 365 -8.5; 402 -8.3; 442 -8.3; 486 -8.3; 535 -8.0; 588 -7.7; 647 -7.3; 712 -7.1; 783 -6.8; 861 -6.5; 947 -6.3; 1042 -6.3; 1146 -6.2; 1261 -6.1; 1387 -6.1; 1526 -6.2; 1678 -6.2; 1846 -6.1; 2031 -6.0; 2234 -5.8; 2457 -5.4; 2703 -5.0; 2973 -4.7; 3270 -4.4; 3597 -4.3; 3957 -4.0; 4353 -3.3; 4788 -1.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`M-Audio IE-30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `M-Audio IE-30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.37 | -3.5 dB |
| Peaking | 174 Hz  | 0.34 | -3.0 dB |
| Peaking | 1600 Hz | 0.27 | 0.6 dB  |
| Peaking | 5894 Hz | 1.5  | 7.3 dB  |
| Peaking | 8025 Hz | 1.77 | -3.8 dB |
| Peaking | 544 Hz  | 2.68 | -0.5 dB |
| Peaking | 1064 Hz | 0.53 | 0.4 dB  |
| Peaking | 2011 Hz | 1.24 | -0.9 dB |
| Peaking | 2929 Hz | 1.4  | 0.7 dB  |
| Peaking | 4046 Hz | 5.06 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/M-Audio%20IE-30/M-Audio%20IE-30.png)