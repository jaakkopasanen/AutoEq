# Erzetich Phobos
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -1.2; 37 -2.3; 41 -3.9; 45 -5.3; 49 -6.9; 54 -8.5; 60 -9.7; 66 -10.3; 72 -10.5; 79 -10.4; 87 -10.0; 96 -9.3; 106 -8.8; 116 -8.5; 128 -8.2; 141 -8.0; 155 -7.8; 170 -7.6; 187 -7.5; 206 -7.5; 227 -7.5; 249 -7.5; 274 -7.5; 302 -7.5; 332 -7.2; 365 -7.2; 402 -7.2; 442 -6.8; 486 -6.4; 535 -5.9; 588 -6.1; 647 -6.8; 712 -7.4; 783 -7.8; 861 -8.1; 947 -8.1; 1042 -7.3; 1146 -6.3; 1261 -5.7; 1387 -5.6; 1526 -5.4; 1678 -6.0; 1846 -7.4; 2031 -8.7; 2234 -9.2; 2457 -8.9; 2703 -7.7; 2973 -6.2; 3270 -5.6; 3597 -5.6; 3957 -5.9; 4353 -6.2; 4788 -6.6; 5267 -6.7; 5793 -8.1; 6373 -8.3; 7010 -5.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Erzetich Phobos GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Erzetich Phobos ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.63 | 8.5 dB  |
| Peaking | 64 Hz   | 0.89 | -7.9 dB |
| Peaking | 272 Hz  | 1.21 | -0.7 dB |
| Peaking | 2259 Hz | 4.81 | -3.1 dB |
| Peaking | 558 Hz  | 2.27 | 1.9 dB  |
| Peaking | 1132 Hz | 0.81 | -3.9 dB |
| Peaking | 1341 Hz | 1.69 | 4.9 dB  |
| Peaking | 3476 Hz | 2.81 | 1.6 dB  |
| Peaking | 6046 Hz | 8.18 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Erzetich%20Phobos/Erzetich%20Phobos.png)