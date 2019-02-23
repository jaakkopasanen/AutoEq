# Master Dynamic MH40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.3; 25 -7.4; 28 -7.6; 31 -7.8; 34 -7.9; 37 -8.0; 41 -8.1; 45 -8.2; 49 -8.3; 54 -8.3; 60 -8.3; 66 -8.3; 72 -8.3; 79 -8.7; 87 -9.5; 96 -10.1; 106 -9.9; 116 -9.9; 128 -10.5; 141 -11.3; 155 -10.8; 170 -9.7; 187 -10.6; 206 -10.1; 227 -9.3; 249 -8.4; 274 -7.4; 302 -6.6; 332 -5.8; 365 -5.0; 402 -4.6; 442 -4.3; 486 -4.7; 535 -5.2; 588 -5.8; 647 -6.8; 712 -7.6; 783 -7.9; 861 -8.4; 947 -8.5; 1042 -8.5; 1146 -8.6; 1261 -8.7; 1387 -9.0; 1526 -9.3; 1678 -9.2; 1846 -8.9; 2031 -8.1; 2234 -6.0; 2457 -6.4; 2703 -8.9; 2973 -7.0; 3270 -4.6; 3597 -4.2; 3957 -3.0; 4353 -3.0; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.9; 9330 -9.6; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Master Dynamic MH40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Master Dynamic MH40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 65 Hz   | 0.68 | -1.8 dB |
| Peaking | 151 Hz  | 1.58 | -4.0 dB |
| Peaking | 1510 Hz | 1.29 | -3.1 dB |
| Peaking | 5450 Hz | 1.54 | 6.9 dB  |
| Peaking | 8992 Hz | 3.41 | -4.6 dB |
| Peaking | 219 Hz  | 3.51 | -1.7 dB |
| Peaking | 443 Hz  | 1.5  | 2.9 dB  |
| Peaking | 809 Hz  | 1.83 | -1.5 dB |
| Peaking | 2687 Hz | 2.44 | 2.5 dB  |
| Peaking | 2781 Hz | 6.5  | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Master%20Dynamic%20MH40/Master%20Dynamic%20MH40.png)