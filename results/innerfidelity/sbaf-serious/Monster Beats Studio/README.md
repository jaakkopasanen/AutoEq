# Monster Beats Studio
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.9; 28 -3.7; 31 -6.7; 34 -8.3; 37 -8.7; 41 -8.6; 45 -8.3; 49 -8.0; 54 -7.8; 60 -7.6; 66 -7.4; 72 -7.2; 79 -7.5; 87 -8.2; 96 -8.8; 106 -9.1; 116 -9.2; 128 -9.4; 141 -9.6; 155 -9.5; 170 -9.5; 187 -9.6; 206 -9.6; 227 -9.4; 249 -9.3; 274 -9.0; 302 -8.9; 332 -8.9; 365 -8.2; 402 -8.4; 442 -8.1; 486 -7.7; 535 -7.2; 588 -6.0; 647 -4.1; 712 -2.8; 783 -1.5; 861 -0.9; 947 -1.3; 1042 -2.4; 1146 -3.7; 1261 -5.6; 1387 -7.3; 1526 -8.3; 1678 -9.2; 1846 -9.0; 2031 -8.2; 2234 -7.2; 2457 -5.5; 2703 -3.8; 2973 -1.8; 3270 -0.5; 3597 -1.8; 3957 -2.9; 4353 -5.6; 4788 -7.4; 5267 -2.7; 5793 -5.0; 6373 -3.3; 7010 -4.1; 7711 -7.4; 8482 -11.0; 9330 -10.8; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Studio GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Studio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 3.24 | 7.9 dB  |
| Peaking | 472 Hz  | 0.16 | -3.5 dB |
| Peaking | 841 Hz  | 1.63 | 9.4 dB  |
| Peaking | 3325 Hz | 2.28 | 7.5 dB  |
| Peaking | 8900 Hz | 6.49 | -5.8 dB |
| Peaking | 36 Hz   | 3.79 | -2.3 dB |
| Peaking | 1114 Hz | 5.43 | 1.7 dB  |
| Peaking | 1730 Hz | 2.99 | -2.3 dB |
| Peaking | 6622 Hz | 3.54 | 4.0 dB  |
| Peaking | 8069 Hz | 5.09 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Studio/Monster%20Beats%20Studio.png)