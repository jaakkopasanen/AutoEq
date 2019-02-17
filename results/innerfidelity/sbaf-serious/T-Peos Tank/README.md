# T-Peos Tank
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.6; 23 -15.5; 25 -15.4; 28 -15.3; 31 -15.3; 34 -15.2; 37 -15.1; 41 -14.9; 45 -14.8; 49 -14.7; 54 -14.6; 60 -14.5; 66 -14.4; 72 -14.4; 79 -14.3; 87 -14.2; 96 -14.2; 106 -13.9; 116 -13.6; 128 -13.4; 141 -13.1; 155 -12.8; 170 -12.3; 187 -11.9; 206 -11.4; 227 -10.8; 249 -10.3; 274 -9.7; 302 -9.1; 332 -8.6; 365 -7.9; 402 -7.4; 442 -6.8; 486 -6.4; 535 -5.9; 588 -5.3; 647 -4.9; 712 -4.8; 783 -4.6; 861 -4.9; 947 -5.3; 1042 -5.9; 1146 -6.3; 1261 -7.1; 1387 -8.3; 1526 -9.8; 1678 -11.1; 1846 -11.7; 2031 -11.9; 2234 -11.4; 2457 -9.0; 2703 -6.3; 2973 -3.2; 3270 -1.1; 3597 -0.5; 3957 -2.2; 4353 -6.3; 4788 -10.7; 5267 -14.8; 5793 -10.1; 6373 -5.8; 7010 -5.0; 7711 -7.3; 8482 -10.4; 9330 -10.4; 10263 -7.4; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos Tank GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Tank ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.23 | -9.7 dB  |
| Peaking | 153 Hz  | 0.81 | -3.8 dB  |
| Peaking | 2005 Hz | 2.03 | -7.6 dB  |
| Peaking | 3495 Hz | 2.58 | 7.7 dB   |
| Peaking | 5196 Hz | 4.24 | -10.4 dB |
| Peaking | 297 Hz  | 1.82 | -0.9 dB  |
| Peaking | 743 Hz  | 1.37 | 1.9 dB   |
| Peaking | 1516 Hz | 4.94 | -1.5 dB  |
| Peaking | 6820 Hz | 4.6  | 3.0 dB   |
| Peaking | 8874 Hz | 3.68 | -5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.1 dB |
| Peaking | 62 Hz    | 1.41 | -6.3 dB  |
| Peaking | 125 Hz   | 1.41 | -6.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Tank/T-Peos%20Tank.png)