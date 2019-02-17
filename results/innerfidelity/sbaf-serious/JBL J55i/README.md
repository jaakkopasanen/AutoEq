# JBL J55i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.7; 25 -10.7; 28 -10.7; 31 -10.7; 34 -10.7; 37 -10.7; 41 -10.7; 45 -10.7; 49 -10.7; 54 -10.8; 60 -11.0; 66 -11.1; 72 -11.4; 79 -11.6; 87 -11.9; 96 -12.2; 106 -12.3; 116 -12.6; 128 -13.0; 141 -13.4; 155 -13.5; 170 -13.2; 187 -13.3; 206 -13.5; 227 -13.4; 249 -13.1; 274 -12.4; 302 -11.8; 332 -11.5; 365 -10.7; 402 -9.9; 442 -8.7; 486 -7.6; 535 -6.2; 588 -4.8; 647 -4.5; 712 -5.3; 783 -5.9; 861 -6.7; 947 -6.9; 1042 -6.1; 1146 -5.1; 1261 -4.6; 1387 -5.9; 1526 -8.2; 1678 -6.7; 1846 -0.7; 2031 -3.5; 2234 -6.0; 2457 -2.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL J55i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL J55i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.23 | -3.8 dB |
| Peaking | 196 Hz  | 0.48 | -6.8 dB |
| Peaking | 608 Hz  | 2.14 | 4.3 dB  |
| Peaking | 3324 Hz | 1.19 | 6.2 dB  |
| Peaking | 5645 Hz | 2.81 | 4.5 dB  |
| Peaking | 1263 Hz | 5.69 | 2.1 dB  |
| Peaking | 1618 Hz | 4.19 | -6.5 dB |
| Peaking | 1863 Hz | 3.58 | 7.9 dB  |
| Peaking | 2147 Hz | 6.74 | -5.9 dB |
| Peaking | 8342 Hz | 3.65 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -6.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20J55i/JBL%20J55i.png)