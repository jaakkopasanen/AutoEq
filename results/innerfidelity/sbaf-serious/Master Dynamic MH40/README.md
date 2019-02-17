# Master Dynamic MH40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.2; 25 -5.4; 28 -5.5; 31 -5.7; 34 -5.8; 37 -6.0; 41 -6.1; 45 -6.1; 49 -6.2; 54 -6.2; 60 -6.2; 66 -6.2; 72 -6.2; 79 -6.7; 87 -7.4; 96 -8.1; 106 -7.8; 116 -7.8; 128 -8.4; 141 -9.2; 155 -8.8; 170 -7.7; 187 -8.6; 206 -8.0; 227 -7.2; 249 -6.3; 274 -5.3; 302 -4.5; 332 -3.8; 365 -2.9; 402 -2.5; 442 -2.2; 486 -2.6; 535 -3.1; 588 -3.7; 647 -4.7; 712 -5.5; 783 -5.8; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.6; 1387 -6.9; 1526 -7.2; 1678 -7.1; 1846 -6.8; 2031 -6.0; 2234 -3.9; 2457 -4.3; 2703 -6.8; 2973 -4.9; 3270 -2.6; 3597 -2.1; 3957 -1.0; 4353 -1.0; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Master Dynamic MH40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Master Dynamic MH40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 0.19 | 1.3 dB  |
| Peaking | 153 Hz  | 0.99 | -2.8 dB |
| Peaking | 418 Hz  | 1.48 | 4.9 dB  |
| Peaking | 4150 Hz | 2.06 | 5.4 dB  |
| Peaking | 5848 Hz | 3.37 | 5.0 dB  |
| Peaking | 928 Hz  | 4.1  | -0.4 dB |
| Peaking | 1847 Hz | 1.74 | -2.7 dB |
| Peaking | 2393 Hz | 1.99 | 4.1 dB  |
| Peaking | 2731 Hz | 6.89 | -4.3 dB |
| Peaking | 8965 Hz | 3.86 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 4.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Master%20Dynamic%20MH40/Master%20Dynamic%20MH40.png)