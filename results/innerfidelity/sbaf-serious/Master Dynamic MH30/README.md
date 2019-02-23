# Master Dynamic MH30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -11.8; 25 -11.9; 28 -11.9; 31 -12.0; 34 -12.0; 37 -11.9; 41 -11.9; 45 -11.8; 49 -11.9; 54 -11.9; 60 -12.0; 66 -12.0; 72 -12.0; 79 -12.0; 87 -12.1; 96 -12.1; 106 -12.2; 116 -12.3; 128 -12.4; 141 -12.3; 155 -12.4; 170 -11.9; 187 -12.0; 206 -11.6; 227 -11.0; 249 -10.3; 274 -9.5; 302 -9.2; 332 -9.1; 365 -9.3; 402 -9.4; 442 -9.5; 486 -9.8; 535 -9.8; 588 -9.5; 647 -9.5; 712 -9.5; 783 -9.0; 861 -8.7; 947 -8.0; 1042 -7.2; 1146 -6.3; 1261 -5.6; 1387 -5.2; 1526 -5.0; 1678 -4.9; 1846 -4.7; 2031 -4.6; 2234 -5.0; 2457 -5.0; 2703 -4.6; 2973 -4.4; 3270 -4.0; 3597 -2.4; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Master Dynamic MH30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Master Dynamic MH30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.23 | -5.3 dB |
| Peaking | 160 Hz  | 0.94 | -3.1 dB |
| Peaking | 687 Hz  | 0.86 | -3.3 dB |
| Peaking | 1450 Hz | 1.13 | 2.4 dB  |
| Peaking | 4822 Hz | 1.51 | 6.8 dB  |
| Peaking | 207 Hz  | 7.87 | -0.4 dB |
| Peaking | 3932 Hz | 5.83 | 2.1 dB  |
| Peaking | 4702 Hz | 1.91 | -1.4 dB |
| Peaking | 6414 Hz | 2.81 | 4.2 dB  |
| Peaking | 7354 Hz | 1.78 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Master%20Dynamic%20MH30/Master%20Dynamic%20MH30.png)