# Gerkules HDP DJ-PRO M1001
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.9; 54 -2.0; 60 -3.2; 66 -4.0; 72 -4.6; 79 -5.2; 87 -5.8; 96 -6.3; 106 -6.8; 116 -7.1; 128 -7.3; 141 -7.5; 155 -7.3; 170 -6.9; 187 -6.4; 206 -5.7; 227 -4.8; 249 -3.9; 274 -3.0; 302 -2.3; 332 -1.4; 365 -0.7; 402 -0.8; 442 -1.9; 486 -3.6; 535 -5.1; 588 -5.5; 647 -5.7; 712 -6.4; 783 -7.1; 861 -7.6; 947 -7.9; 1042 -8.1; 1146 -8.5; 1261 -9.0; 1387 -9.4; 1526 -9.5; 1678 -9.5; 1846 -9.2; 2031 -8.8; 2234 -8.4; 2457 -8.7; 2703 -9.5; 2973 -10.0; 3270 -9.9; 3597 -9.4; 3957 -8.5; 4353 -8.0; 4788 -8.4; 5267 -8.7; 5793 -8.6; 6373 -7.3; 7010 -4.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.0; 13660 -9.7; 15026 -7.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Gerkules HDP DJ-PRO M1001 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Gerkules HDP DJ-PRO M1001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.51 | 8.3 dB  |
| Peaking | 216 Hz   | 0.22 | -5.4 dB |
| Peaking | 363 Hz   | 0.92 | 10.5 dB |
| Peaking | 1496 Hz  | 2.05 | -1.8 dB |
| Peaking | 3316 Hz  | 1.3  | -2.8 dB |
| Peaking | 535 Hz   | 7.53 | -1.0 dB |
| Peaking | 2993 Hz  | 8.22 | -0.6 dB |
| Peaking | 5750 Hz  | 3.48 | -3.8 dB |
| Peaking | 6453 Hz  | 1.85 | 2.8 dB  |
| Peaking | 13872 Hz | 4.21 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | 3.1 dB  |
| Peaking | 500 Hz   | 1.41 | 3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Gerkules%20HDP%20DJ-PRO%20M1001/Gerkules%20HDP%20DJ-PRO%20M1001.png)