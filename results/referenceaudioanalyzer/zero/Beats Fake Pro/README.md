# Beats Fake Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -1.7; 87 -3.1; 96 -4.1; 106 -4.7; 116 -5.0; 128 -5.1; 141 -5.0; 155 -4.8; 170 -4.5; 187 -3.9; 206 -3.3; 227 -2.6; 249 -2.0; 274 -1.2; 302 -0.9; 332 -1.0; 365 -1.4; 402 -1.9; 442 -2.7; 486 -3.9; 535 -5.9; 588 -7.7; 647 -9.0; 712 -9.4; 783 -9.7; 861 -9.5; 947 -9.2; 1042 -9.2; 1146 -9.4; 1261 -9.6; 1387 -9.7; 1526 -10.0; 1678 -10.4; 1846 -10.7; 2031 -11.1; 2234 -11.5; 2457 -11.6; 2703 -11.1; 2973 -10.2; 3270 -8.8; 3597 -7.0; 3957 -7.1; 4353 -8.8; 4788 -8.9; 5267 -6.3; 5793 -3.2; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Fake Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Fake Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.57 | 6.8 dB  |
| Peaking | 345 Hz  | 1.17 | 6.4 dB  |
| Peaking | 722 Hz  | 1.44 | -4.0 dB |
| Peaking | 2177 Hz | 0.96 | -4.9 dB |
| Peaking | 6316 Hz | 4.73 | 6.0 dB  |
| Peaking | 38 Hz   | 2.99 | -1.1 dB |
| Peaking | 71 Hz   | 3.03 | 2.0 dB  |
| Peaking | 112 Hz  | 2.17 | -1.4 dB |
| Peaking | 3713 Hz | 7.12 | 2.2 dB  |
| Peaking | 4620 Hz | 7.21 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | 5.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beats%20Fake%20Pro/Beats%20Fake%20Pro.png)