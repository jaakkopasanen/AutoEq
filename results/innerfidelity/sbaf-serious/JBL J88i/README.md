# JBL J88i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.6; 25 -3.9; 28 -4.3; 31 -4.6; 34 -4.9; 37 -5.1; 41 -5.3; 45 -5.5; 49 -5.7; 54 -5.9; 60 -6.2; 66 -6.5; 72 -6.8; 79 -7.1; 87 -7.5; 96 -8.0; 106 -8.2; 116 -8.5; 128 -9.0; 141 -9.4; 155 -9.7; 170 -9.3; 187 -9.7; 206 -9.9; 227 -10.0; 249 -10.1; 274 -9.8; 302 -9.3; 332 -8.3; 365 -7.0; 402 -4.7; 442 -1.6; 486 -0.9; 535 -0.5; 588 -0.5; 647 -1.6; 712 -4.1; 783 -5.2; 861 -6.0; 947 -6.3; 1042 -6.5; 1146 -6.7; 1261 -7.3; 1387 -7.6; 1526 -7.3; 1678 -5.9; 1846 -3.4; 2031 -0.9; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL J88i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL J88i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 405 Hz  | 0.39 | -7.6 dB |
| Peaking | 521 Hz  | 1.33 | 13.4 dB |
| Peaking | 1449 Hz | 2.65 | -4.0 dB |
| Peaking | 2951 Hz | 0.58 | 7.6 dB  |
| Peaking | 17 Hz   | 0.83 | 3.5 dB  |
| Peaking | 55 Hz   | 0.86 | 0.8 dB  |
| Peaking | 3251 Hz | 4.09 | -1.0 dB |
| Peaking | 6188 Hz | 2.03 | 5.4 dB  |
| Peaking | 7570 Hz | 1.44 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.5 dB |
| Peaking | 500 Hz   | 1.41 | 7.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20J88i/JBL%20J88i.png)