# NuForce HEM1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.3; 25 -5.6; 28 -5.9; 31 -6.2; 34 -6.4; 37 -6.5; 41 -6.7; 45 -6.9; 49 -7.1; 54 -7.3; 60 -7.5; 66 -7.7; 72 -8.0; 79 -8.2; 87 -8.5; 96 -8.8; 106 -9.2; 116 -9.4; 128 -9.6; 141 -9.7; 155 -9.8; 170 -9.8; 187 -9.9; 206 -9.9; 227 -9.8; 249 -9.7; 274 -9.6; 302 -9.4; 332 -9.2; 365 -9.0; 402 -8.8; 442 -8.7; 486 -8.4; 535 -8.2; 588 -7.8; 647 -7.3; 712 -6.8; 783 -6.3; 861 -5.8; 947 -5.5; 1042 -5.6; 1146 -6.2; 1261 -6.9; 1387 -7.1; 1526 -6.9; 1678 -6.4; 1846 -5.8; 2031 -5.6; 2234 -5.8; 2457 -6.6; 2703 -7.3; 2973 -7.0; 3270 -5.5; 3597 -3.7; 3957 -2.4; 4353 -1.9; 4788 -2.0; 5267 -1.8; 5793 -0.5; 6373 -0.9; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce HEM1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce HEM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.99 | 2.4 dB  |
| Peaking | 165 Hz  | 0.55 | -2.1 dB |
| Peaking | 364 Hz  | 0.24 | -1.7 dB |
| Peaking | 905 Hz  | 1.94 | 2.4 dB  |
| Peaking | 5277 Hz | 1.67 | 5.9 dB  |
| Peaking | 2049 Hz | 3.76 | 1.4 dB  |
| Peaking | 2854 Hz | 3.78 | -1.8 dB |
| Peaking | 3987 Hz | 2.6  | 3.2 dB  |
| Peaking | 5902 Hz | 1.12 | -3.9 dB |
| Peaking | 6238 Hz | 3.67 | 5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/NuForce%20HEM1/NuForce%20HEM1.png)