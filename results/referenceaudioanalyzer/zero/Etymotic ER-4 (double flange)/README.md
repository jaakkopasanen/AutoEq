# Etymotic ER-4 (double flange)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.0; 25 -2.3; 28 -2.6; 31 -2.9; 34 -3.1; 37 -3.3; 41 -3.5; 45 -3.6; 49 -3.7; 54 -3.8; 60 -4.0; 66 -4.1; 72 -4.1; 79 -4.1; 87 -4.3; 96 -4.5; 106 -4.4; 116 -4.4; 128 -4.4; 141 -4.4; 155 -4.4; 170 -4.4; 187 -4.4; 206 -4.4; 227 -4.4; 249 -4.4; 274 -4.4; 302 -4.5; 332 -4.8; 365 -4.8; 402 -4.7; 442 -4.8; 486 -4.8; 535 -4.8; 588 -4.8; 647 -4.8; 712 -4.8; 783 -4.8; 861 -4.8; 947 -5.0; 1042 -5.1; 1146 -5.3; 1261 -5.6; 1387 -6.0; 1526 -6.5; 1678 -7.0; 1846 -7.7; 2031 -8.4; 2234 -9.0; 2457 -9.3; 2703 -8.9; 2973 -7.9; 3270 -6.3; 3597 -4.9; 3957 -5.0; 4353 -6.4; 4788 -7.1; 5267 -6.2; 5793 -3.8; 6373 -0.5; 7010 -2.0; 7711 -4.2; 8482 -4.5; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER-4 (double flange) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-4 (double flange) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.98 | 2.8 dB  |
| Peaking | 43 Hz   | 1.42 | 0.3 dB  |
| Peaking | 2308 Hz | 1.58 | -4.9 dB |
| Peaking | 4924 Hz | 5.29 | -2.6 dB |
| Peaking | 6535 Hz | 5.66 | 5.1 dB  |
| Peaking | 3509 Hz | 1.98 | -1.2 dB |
| Peaking | 3654 Hz | 4.58 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Etymotic%20ER-4%20(double%20flange)/Etymotic%20ER-4%20(double%20flange).png)