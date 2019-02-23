# AKG Q701
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.9; 49 -1.2; 54 -1.5; 60 -1.8; 66 -2.2; 72 -2.5; 79 -2.9; 87 -3.4; 96 -3.9; 106 -4.3; 116 -4.8; 128 -5.2; 141 -5.6; 155 -5.9; 170 -6.0; 187 -6.1; 206 -6.1; 227 -6.1; 249 -6.1; 274 -6.2; 302 -6.2; 332 -6.2; 365 -6.2; 402 -6.2; 442 -6.1; 486 -5.7; 535 -5.2; 588 -4.6; 647 -4.6; 712 -4.3; 783 -3.9; 861 -3.8; 947 -4.0; 1042 -3.8; 1146 -3.9; 1261 -4.3; 1387 -4.7; 1526 -5.7; 1678 -7.2; 1846 -8.7; 2031 -9.8; 2234 -10.2; 2457 -9.2; 2703 -8.2; 2973 -7.0; 3270 -5.6; 3597 -6.1; 3957 -6.6; 4353 -6.9; 4788 -6.7; 5267 -7.2; 5793 -8.6; 6373 -11.6; 7010 -11.3; 7711 -10.8; 8482 -11.1; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.9; 18182 -11.5; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.51 | 6.4 dB  |
| Peaking | 1040 Hz  | 0.92 | 3.1 dB  |
| Peaking | 2108 Hz  | 2.75 | -4.9 dB |
| Peaking | 7181 Hz  | 2.46 | -5.5 dB |
| Peaking | 19030 Hz | 1.51 | -6.4 dB |
| Peaking | 221 Hz   | 1.15 | -0.4 dB |
| Peaking | 2635 Hz  | 4.5  | -1.0 dB |
| Peaking | 3285 Hz  | 4.01 | 1.5 dB  |
| Peaking | 8589 Hz  | 6.93 | -3.0 dB |
| Peaking | 10097 Hz | 1.37 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20Q701/AKG%20Q701.png)