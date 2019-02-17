# Oppo PM3 sample C
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.0; 25 -4.1; 28 -4.2; 31 -4.3; 34 -4.3; 37 -4.4; 41 -4.4; 45 -4.4; 49 -4.4; 54 -4.4; 60 -4.7; 66 -4.7; 72 -4.8; 79 -4.9; 87 -4.9; 96 -5.3; 106 -6.3; 116 -6.8; 128 -7.4; 141 -7.7; 155 -7.5; 170 -6.7; 187 -7.4; 206 -7.0; 227 -6.2; 249 -5.6; 274 -4.7; 302 -3.8; 332 -3.2; 365 -2.9; 402 -3.1; 442 -3.5; 486 -4.4; 535 -5.3; 588 -5.4; 647 -6.0; 712 -6.4; 783 -6.4; 861 -6.4; 947 -6.4; 1042 -6.6; 1146 -7.0; 1261 -7.1; 1387 -7.6; 1526 -8.0; 1678 -8.1; 1846 -9.0; 2031 -9.0; 2234 -9.5; 2457 -8.3; 2703 -7.7; 2973 -7.2; 3270 -6.3; 3597 -6.6; 3957 -7.1; 4353 -6.4; 4788 -3.7; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.3; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM3 sample C GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 sample C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.02 | 2.5 dB  |
| Peaking | 61 Hz    | 2.03 | 1.6 dB  |
| Peaking | 378 Hz   | 2.19 | 4.0 dB  |
| Peaking | 2071 Hz  | 1.57 | -2.9 dB |
| Peaking | 5744 Hz  | 3.2  | 7.0 dB  |
| Peaking | 88 Hz    | 4.19 | 1.1 dB  |
| Peaking | 136 Hz   | 3.14 | -1.7 dB |
| Peaking | 195 Hz   | 6.23 | -1.1 dB |
| Peaking | 20870 Hz | 1.7  | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM3%20sample%20C/Oppo%20PM3%20sample%20C.png)