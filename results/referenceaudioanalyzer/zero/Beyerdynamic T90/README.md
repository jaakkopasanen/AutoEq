# Beyerdynamic T90
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.7; 25 -2.2; 28 -2.8; 31 -3.3; 34 -3.6; 37 -3.9; 41 -4.1; 45 -4.3; 49 -4.5; 54 -4.8; 60 -5.1; 66 -5.4; 72 -5.5; 79 -5.6; 87 -5.8; 96 -5.9; 106 -5.9; 116 -6.1; 128 -6.2; 141 -6.3; 155 -6.5; 170 -6.3; 187 -6.4; 206 -6.2; 227 -6.2; 249 -6.2; 274 -6.0; 302 -5.8; 332 -5.5; 365 -5.2; 402 -4.8; 442 -4.3; 486 -3.8; 535 -3.6; 588 -3.4; 647 -3.2; 712 -2.7; 783 -2.0; 861 -1.5; 947 -1.2; 1042 -0.8; 1146 -0.5; 1261 -0.7; 1387 -1.0; 1526 -1.2; 1678 -1.5; 1846 -1.7; 2031 -2.0; 2234 -2.5; 2457 -2.9; 2703 -3.3; 2973 -3.8; 3270 -4.6; 3597 -5.8; 3957 -7.1; 4353 -7.8; 4788 -7.6; 5267 -7.5; 5793 -6.3; 6373 -5.9; 7010 -9.3; 7711 -12.2; 8482 -13.0; 9330 -12.5; 10263 -12.5; 11289 -12.8; 12418 -11.7; 13660 -9.3; 15026 -7.1; 16529 -5.3; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T90 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T90 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.97 | 4.8 dB  |
| Peaking | 173 Hz   | 0.55 | -1.7 dB |
| Peaking | 1212 Hz  | 0.75 | 4.7 dB  |
| Peaking | 8030 Hz  | 5.65 | -3.0 dB |
| Peaking | 10431 Hz | 0.94 | -7.9 dB |
| Peaking | 3169 Hz  | 1.49 | 2.1 dB  |
| Peaking | 4074 Hz  | 1.5  | -3.2 dB |
| Peaking | 6122 Hz  | 5.82 | 3.2 dB  |
| Peaking | 12749 Hz | 4.04 | -1.1 dB |
| Peaking | 16772 Hz | 1.03 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | -8.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20T90/Beyerdynamic%20T90.png)