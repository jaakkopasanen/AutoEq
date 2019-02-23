# AKG K267 Tiesto Stage Setting
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.6; 25 -9.7; 28 -9.8; 31 -9.9; 34 -9.9; 37 -9.8; 41 -9.7; 45 -9.6; 49 -9.3; 54 -9.1; 60 -9.0; 66 -8.8; 72 -8.6; 79 -8.2; 87 -8.3; 96 -9.1; 106 -9.7; 116 -10.1; 128 -10.5; 141 -10.6; 155 -10.2; 170 -9.6; 187 -10.1; 206 -9.6; 227 -9.6; 249 -9.1; 274 -8.3; 302 -6.9; 332 -5.1; 365 -4.1; 402 -4.8; 442 -5.6; 486 -6.3; 535 -6.4; 588 -6.4; 647 -6.6; 712 -6.8; 783 -6.5; 861 -6.7; 947 -6.9; 1042 -7.2; 1146 -7.2; 1261 -8.1; 1387 -9.9; 1526 -11.0; 1678 -10.4; 1846 -9.2; 2031 -8.3; 2234 -7.4; 2457 -5.7; 2703 -5.6; 2973 -4.8; 3270 -4.5; 3597 -3.8; 3957 -1.8; 4353 -0.5; 4788 -0.5; 5267 -4.4; 5793 -1.3; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -8.3; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K267 Tiesto Stage Setting GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K267 Tiesto Stage Setting ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.63 | -3.4 dB |
| Peaking | 149 Hz  | 1.32 | -3.9 dB |
| Peaking | 1579 Hz | 2.96 | -4.9 dB |
| Peaking | 4325 Hz | 2.62 | 6.1 dB  |
| Peaking | 6236 Hz | 5.73 | 5.0 dB  |
| Peaking | 84 Hz   | 5.61 | 0.4 dB  |
| Peaking | 251 Hz  | 2.93 | -1.9 dB |
| Peaking | 365 Hz  | 3.03 | 3.3 dB  |
| Peaking | 2808 Hz | 4.97 | 0.7 dB  |
| Peaking | 9182 Hz | 5.75 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K267%20Tiesto%20Stage%20Setting/AKG%20K267%20Tiesto%20Stage%20Setting.png)