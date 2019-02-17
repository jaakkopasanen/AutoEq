# T-Peos Altone 200 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.2; 25 -4.7; 28 -5.3; 31 -5.8; 34 -6.2; 37 -6.5; 41 -6.9; 45 -7.2; 49 -7.5; 54 -7.8; 60 -8.1; 66 -8.4; 72 -8.6; 79 -9.0; 87 -9.2; 96 -9.5; 106 -9.5; 116 -9.5; 128 -9.5; 141 -9.4; 155 -9.2; 170 -9.0; 187 -8.6; 206 -8.2; 227 -7.7; 249 -7.2; 274 -6.7; 302 -6.1; 332 -5.4; 365 -4.8; 402 -4.2; 442 -3.4; 486 -3.0; 535 -2.4; 588 -1.6; 647 -1.1; 712 -1.0; 783 -0.5; 861 -0.6; 947 -0.9; 1042 -1.3; 1146 -1.7; 1261 -2.3; 1387 -3.3; 1526 -4.4; 1678 -5.5; 1846 -6.4; 2031 -7.1; 2234 -7.4; 2457 -6.2; 2703 -5.2; 2973 -4.0; 3270 -3.8; 3597 -3.7; 3957 -3.6; 4353 -2.8; 4788 -1.2; 5267 -0.7; 5793 -1.2; 6373 -3.0; 7010 -5.4; 7711 -5.5; 8482 -6.9; 9330 -9.6; 10263 -9.7; 11289 -5.7; 12418 -1.6; 13660 -1.2; 15026 -1.2; 16529 -1.2; 18182 -1.2; 20000 -1.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos Altone 200 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Altone 200 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 60 Hz    | 0.47 | -6.0 dB |
| Peaking | 143 Hz   | 0.93 | -4.7 dB |
| Peaking | 269 Hz   | 1.57 | -2.8 dB |
| Peaking | 2155 Hz  | 1.77 | -6.3 dB |
| Peaking | 9605 Hz  | 2.33 | -9.3 dB |
| Peaking | 819 Hz   | 2.51 | 1.7 dB  |
| Peaking | 4020 Hz  | 2.86 | -1.9 dB |
| Peaking | 5283 Hz  | 2.4  | 2.4 dB  |
| Peaking | 7006 Hz  | 5.21 | -2.6 dB |
| Peaking | 13099 Hz | 4.11 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Altone%20200%202014/T-Peos%20Altone%20200%202014.png)