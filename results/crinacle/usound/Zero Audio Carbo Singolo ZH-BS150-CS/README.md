# Zero Audio Carbo Singolo ZH-BS150-CS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.7; 25 -3.9; 28 -4.1; 31 -4.2; 34 -4.4; 37 -4.5; 41 -4.7; 45 -4.9; 49 -5.1; 54 -5.3; 60 -5.6; 66 -5.9; 72 -6.3; 79 -6.7; 87 -7.1; 96 -7.6; 106 -8.0; 116 -8.4; 128 -8.7; 141 -9.0; 155 -9.3; 170 -9.5; 187 -9.6; 206 -9.6; 227 -9.6; 249 -9.6; 274 -9.5; 302 -9.3; 332 -9.0; 365 -8.9; 402 -9.1; 442 -8.7; 486 -8.3; 535 -7.8; 588 -7.4; 647 -6.8; 712 -6.1; 783 -5.4; 861 -4.8; 947 -4.5; 1042 -4.5; 1146 -5.0; 1261 -5.6; 1387 -5.9; 1526 -5.8; 1678 -5.7; 1846 -5.7; 2031 -6.5; 2234 -8.1; 2457 -9.8; 2703 -8.4; 2973 -4.7; 3270 -1.9; 3597 -0.6; 3957 -0.9; 4353 -3.6; 4788 -7.8; 5267 -5.5; 5793 -0.5; 6373 -0.6; 7010 -3.6; 7711 -6.9; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zero Audio Carbo Singolo ZH-BS150-CS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zero Audio Carbo Singolo ZH-BS150-CS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 190 Hz  | 1.02 | -3.8 dB |
| Peaking | 399 Hz  | 2.35 | -2.1 dB |
| Peaking | 3762 Hz | 2.95 | 11.7 dB |
| Peaking | 4412 Hz | 1.02 | -6.5 dB |
| Peaking | 6102 Hz | 3.54 | 9.5 dB  |
| Peaking | 25 Hz   | 0.93 | 2.5 dB  |
| Peaking | 975 Hz  | 2.9  | 2.2 dB  |
| Peaking | 1870 Hz | 2.56 | 1.5 dB  |
| Peaking | 2498 Hz | 3.6  | -4.0 dB |
| Peaking | 3117 Hz | 6.21 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Zero%20Audio%20Carbo%20Singolo%20ZH-BS150-CS/Zero%20Audio%20Carbo%20Singolo%20ZH-BS150-CS.png)