# Bose AE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.8; 25 -10.0; 28 -10.2; 31 -10.3; 34 -10.3; 37 -10.2; 41 -10.0; 45 -9.8; 49 -9.5; 54 -9.3; 60 -9.3; 66 -9.3; 72 -9.6; 79 -9.9; 87 -10.2; 96 -10.4; 106 -10.6; 116 -10.9; 128 -10.9; 141 -10.3; 155 -9.2; 170 -8.1; 187 -7.4; 206 -7.3; 227 -7.6; 249 -7.6; 274 -7.2; 302 -6.9; 332 -6.7; 365 -6.4; 402 -6.4; 442 -6.4; 486 -6.4; 535 -6.4; 588 -6.5; 647 -6.7; 712 -7.1; 783 -7.5; 861 -7.8; 947 -8.1; 1042 -8.2; 1146 -7.9; 1261 -6.8; 1387 -4.8; 1526 -2.1; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -2.1; 2973 -4.7; 3270 -6.9; 3597 -8.8; 3957 -9.9; 4353 -9.7; 4788 -8.5; 5267 -8.6; 5793 -9.3; 6373 -8.1; 7010 -6.8; 7711 -7.1; 8482 -7.5; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose AE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose AE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.52 | -3.6 dB |
| Peaking | 116 Hz  | 1.5  | -3.8 dB |
| Peaking | 2152 Hz | 1.82 | 7.5 dB  |
| Peaking | 3962 Hz | 2.7  | -4.6 dB |
| Peaking | 5807 Hz | 3.73 | -2.4 dB |
| Peaking | 1066 Hz | 2.02 | -2.8 dB |
| Peaking | 1605 Hz | 5.52 | 3.3 dB  |
| Peaking | 6050 Hz | 3.24 | -0.7 dB |
| Peaking | 7149 Hz | 1.61 | 1.2 dB  |
| Peaking | 8463 Hz | 3.27 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB |
| Peaking | 2000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.3 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Bose%20AE/Bose%20AE.png)