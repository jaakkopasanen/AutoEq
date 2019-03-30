# Philips SPH 6000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -2.2; 54 -3.7; 60 -5.0; 66 -5.9; 72 -6.5; 79 -6.6; 87 -6.5; 96 -6.4; 106 -6.2; 116 -6.2; 128 -5.9; 141 -5.6; 155 -5.5; 170 -5.2; 187 -5.2; 206 -4.9; 227 -5.0; 249 -5.4; 274 -6.0; 302 -6.4; 332 -6.3; 365 -6.4; 402 -6.8; 442 -7.4; 486 -7.8; 535 -7.8; 588 -7.6; 647 -7.4; 712 -7.9; 783 -8.4; 861 -8.4; 947 -7.5; 1042 -5.9; 1146 -4.9; 1261 -5.4; 1387 -7.5; 1526 -9.2; 1678 -9.4; 1846 -8.2; 2031 -6.1; 2234 -4.0; 2457 -2.6; 2703 -1.7; 2973 -1.9; 3270 -4.3; 3597 -7.3; 3957 -8.2; 4353 -6.7; 4788 -3.6; 5267 -2.8; 5793 -5.7; 6373 -8.2; 7010 -9.6; 7711 -10.9; 8482 -10.9; 9330 -9.2; 10263 -7.5; 11289 -7.5; 12418 -7.6; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SPH 6000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SPH 6000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 1.01 | 6.9 dB  |
| Peaking | 1654 Hz | 4.54 | -3.8 dB |
| Peaking | 2682 Hz | 3.42 | 5.7 dB  |
| Peaking | 5207 Hz | 6.02 | 5.3 dB  |
| Peaking | 7910 Hz | 1.85 | -4.7 dB |
| Peaking | 79 Hz   | 2.96 | -1.5 dB |
| Peaking | 207 Hz  | 1.93 | 1.6 dB  |
| Peaking | 660 Hz  | 1.2  | -2.2 dB |
| Peaking | 1357 Hz | 0.37 | 0.8 dB  |
| Peaking | 3867 Hz | 6.14 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20SPH%206000/Philips%20SPH%206000.png)