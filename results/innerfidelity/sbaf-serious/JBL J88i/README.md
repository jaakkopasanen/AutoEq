# JBL J88i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.3; 25 -7.6; 28 -8.0; 31 -8.3; 34 -8.6; 37 -8.8; 41 -9.1; 45 -9.3; 49 -9.5; 54 -9.7; 60 -10.0; 66 -10.2; 72 -10.5; 79 -10.9; 87 -11.3; 96 -11.7; 106 -11.9; 116 -12.2; 128 -12.7; 141 -13.1; 155 -13.5; 170 -13.1; 187 -13.4; 206 -13.6; 227 -13.8; 249 -13.8; 274 -13.6; 302 -13.1; 332 -12.0; 365 -10.7; 402 -8.5; 442 -5.4; 486 -4.5; 535 -3.3; 588 -3.8; 647 -5.3; 712 -7.9; 783 -8.9; 861 -9.7; 947 -10.1; 1042 -10.3; 1146 -10.5; 1261 -11.0; 1387 -11.3; 1526 -11.1; 1678 -9.6; 1846 -7.1; 2031 -4.6; 2234 -2.4; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.1; 4788 -3.3; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL J88i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL J88i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 116 Hz  | 0.69 | -5.8 dB |
| Peaking | 252 Hz  | 2.05 | -5.6 dB |
| Peaking | 1432 Hz | 1.58 | -7.9 dB |
| Peaking | 2781 Hz | 0.98 | 7.8 dB  |
| Peaking | 5945 Hz | 4.34 | 4.8 dB  |
| Peaking | 37 Hz   | 1.75 | -1.2 dB |
| Peaking | 350 Hz  | 2.95 | -3.4 dB |
| Peaking | 543 Hz  | 1.59 | 5.9 dB  |
| Peaking | 805 Hz  | 2.12 | -3.7 dB |
| Peaking | 8468 Hz | 3.38 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -8.5 dB |
| Peaking | 500 Hz   | 1.41 | 5.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20J88i/JBL%20J88i.png)