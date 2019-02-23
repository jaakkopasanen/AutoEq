# Beyerdynamic DT 250-250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -1.9; 31 -2.4; 34 -2.8; 37 -3.1; 41 -3.5; 45 -3.8; 49 -4.1; 54 -4.3; 60 -4.6; 66 -4.7; 72 -4.8; 79 -4.0; 87 -3.5; 96 -4.1; 106 -4.2; 116 -4.7; 128 -6.0; 141 -6.6; 155 -6.6; 170 -6.1; 187 -7.0; 206 -7.1; 227 -7.0; 249 -6.9; 274 -6.9; 302 -7.0; 332 -7.0; 365 -6.7; 402 -6.8; 442 -6.8; 486 -7.0; 535 -7.2; 588 -7.1; 647 -7.3; 712 -7.8; 783 -7.8; 861 -8.3; 947 -8.7; 1042 -7.5; 1146 -7.9; 1261 -9.2; 1387 -10.2; 1526 -11.0; 1678 -11.3; 1846 -10.8; 2031 -9.7; 2234 -8.7; 2457 -7.5; 2703 -6.3; 2973 -4.4; 3270 -3.1; 3597 -4.0; 3957 -5.5; 4353 -6.5; 4788 -5.9; 5267 -3.4; 5793 -0.7; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -7.3; 9330 -9.8; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 250-250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 250-250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.65 | 5.9 dB  |
| Peaking | 91 Hz   | 2.79 | 2.4 dB  |
| Peaking | 1688 Hz | 1.16 | -4.6 dB |
| Peaking | 3204 Hz | 3.32 | 4.6 dB  |
| Peaking | 6041 Hz | 4.48 | 6.8 dB  |
| Peaking | 218 Hz  | 1.75 | -0.6 dB |
| Peaking | 1006 Hz | 1.83 | -1.4 dB |
| Peaking | 1110 Hz | 3.95 | 2.4 dB  |
| Peaking | 9087 Hz | 1.26 | 1.0 dB  |
| Peaking | 9368 Hz | 4.11 | -4.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20250-250/Beyerdynamic%20DT%20250-250.png)