# JBL J55i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.0; 23 -12.0; 25 -12.1; 28 -12.1; 31 -12.1; 34 -12.1; 37 -12.0; 41 -12.0; 45 -12.0; 49 -12.1; 54 -12.2; 60 -12.3; 66 -12.5; 72 -12.7; 79 -12.9; 87 -13.2; 96 -13.6; 106 -13.7; 116 -14.0; 128 -14.4; 141 -14.7; 155 -14.9; 170 -14.6; 187 -14.7; 206 -14.9; 227 -14.8; 249 -14.5; 274 -13.8; 302 -13.2; 332 -12.8; 365 -12.1; 402 -11.2; 442 -10.0; 486 -9.0; 535 -7.6; 588 -6.2; 647 -5.9; 712 -6.7; 783 -7.3; 861 -8.1; 947 -8.3; 1042 -7.5; 1146 -6.5; 1261 -6.0; 1387 -7.2; 1526 -9.6; 1678 -8.0; 1846 -1.0; 2031 -4.9; 2234 -7.3; 2457 -4.1; 2703 -1.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL J55i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL J55i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 40 Hz   |  0.2  | -5.5 dB |
| Peaking | 215 Hz  |  0.79 | -6.0 dB |
| Peaking | 1549 Hz |  9.21 | -4.4 dB |
| Peaking | 3483 Hz |  1.32 | 6.2 dB  |
| Peaking | 5702 Hz |  2.94 | 4.6 dB  |
| Peaking | 615 Hz  |  2.42 | 5.6 dB  |
| Peaking | 622 Hz  |  1.13 | -3.0 dB |
| Peaking | 1886 Hz | 10.17 | 6.0 dB  |
| Peaking | 2176 Hz |  8.5  | -4.3 dB |
| Peaking | 8299 Hz |  4.03 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -7.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20J55i/JBL%20J55i.png)