# Ocharaku Donguri Ti Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.2; 25 -5.7; 28 -6.2; 31 -6.6; 34 -6.8; 37 -7.0; 41 -7.2; 45 -7.5; 49 -7.6; 54 -7.8; 60 -8.0; 66 -8.2; 72 -8.5; 79 -8.9; 87 -9.3; 96 -9.6; 106 -9.8; 116 -9.9; 128 -10.0; 141 -10.1; 155 -10.1; 170 -10.0; 187 -9.8; 206 -9.5; 227 -9.2; 249 -8.8; 274 -8.4; 302 -8.0; 332 -7.6; 365 -7.2; 402 -6.8; 442 -6.4; 486 -6.0; 535 -5.6; 588 -5.2; 647 -4.8; 712 -4.4; 783 -4.1; 861 -3.9; 947 -4.1; 1042 -4.6; 1146 -5.7; 1261 -7.0; 1387 -8.4; 1526 -9.7; 1678 -9.0; 1846 -9.5; 2031 -10.6; 2234 -10.2; 2457 -11.6; 2703 -9.3; 2973 -7.0; 3270 -6.1; 3597 -6.1; 3957 -9.1; 4353 -12.1; 4788 -6.8; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.6; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Donguri Ti Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Donguri Ti Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 142 Hz  | 0.64 | -3.8 dB |
| Peaking | 829 Hz  | 1.22 | 3.5 dB  |
| Peaking | 1987 Hz | 1.33 | -4.8 dB |
| Peaking | 4384 Hz | 6.72 | -8.2 dB |
| Peaking | 5641 Hz | 2.6  | 7.6 dB  |
| Peaking | 18 Hz   | 2.22 | 2.0 dB  |
| Peaking | 2496 Hz | 7.4  | -2.9 dB |
| Peaking | 3424 Hz | 2.17 | 2.3 dB  |
| Peaking | 4055 Hz | 6.08 | -2.2 dB |
| Peaking | 8204 Hz | 3.71 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ocharaku%20Donguri%20Ti%20Plus/Ocharaku%20Donguri%20Ti%20Plus.png)