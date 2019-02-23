# TDK BA200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -5.8; 25 -5.9; 28 -5.9; 31 -6.0; 34 -6.1; 37 -6.2; 41 -6.3; 45 -6.5; 49 -6.6; 54 -6.8; 60 -7.1; 66 -7.4; 72 -7.8; 79 -8.1; 87 -8.6; 96 -9.0; 106 -9.2; 116 -9.3; 128 -9.7; 141 -9.8; 155 -10.1; 170 -10.1; 187 -10.1; 206 -10.1; 227 -9.9; 249 -9.9; 274 -9.7; 302 -9.4; 332 -9.2; 365 -8.9; 402 -8.5; 442 -8.0; 486 -7.7; 535 -7.3; 588 -6.5; 647 -6.2; 712 -6.0; 783 -5.6; 861 -5.6; 947 -5.8; 1042 -6.0; 1146 -6.3; 1261 -6.7; 1387 -7.3; 1526 -8.0; 1678 -8.5; 1846 -8.7; 2031 -8.3; 2234 -7.6; 2457 -6.0; 2703 -4.4; 2973 -2.2; 3270 -0.6; 3597 -0.5; 3957 -0.6; 4353 -2.8; 4788 -2.3; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.4; 9330 -10.4; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TDK BA200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TDK BA200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 181 Hz  | 0.71 | -3.9 dB |
| Peaking | 1947 Hz | 2.45 | -3.3 dB |
| Peaking | 3445 Hz | 2.1  | 6.1 dB  |
| Peaking | 5858 Hz | 2.45 | 5.8 dB  |
| Peaking | 9107 Hz | 4.16 | -4.9 dB |
| Peaking | 42 Hz   | 0.09 | 0.8 dB  |
| Peaking | 91 Hz   | 1.24 | -1.2 dB |
| Peaking | 359 Hz  | 1.25 | -1.2 dB |
| Peaking | 797 Hz  | 1.49 | 1.4 dB  |
| Peaking | 1535 Hz | 4.46 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/TDK%20BA200/TDK%20BA200.png)