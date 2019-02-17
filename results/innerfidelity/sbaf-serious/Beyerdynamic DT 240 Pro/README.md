# Beyerdynamic DT 240 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.9; 25 -8.3; 28 -8.9; 31 -9.3; 34 -9.6; 37 -9.9; 41 -10.1; 45 -10.4; 49 -10.5; 54 -10.7; 60 -10.8; 66 -10.8; 72 -10.9; 79 -10.4; 87 -9.6; 96 -10.8; 106 -12.0; 116 -12.1; 128 -11.3; 141 -11.2; 155 -11.6; 170 -11.2; 187 -11.4; 206 -11.1; 227 -10.2; 249 -9.6; 274 -8.8; 302 -7.8; 332 -6.9; 365 -6.5; 402 -7.2; 442 -7.2; 486 -7.4; 535 -7.1; 588 -6.6; 647 -6.7; 712 -7.0; 783 -6.9; 861 -7.0; 947 -6.8; 1042 -6.3; 1146 -6.5; 1261 -6.9; 1387 -7.6; 1526 -8.5; 1678 -9.2; 1846 -9.4; 2031 -9.3; 2234 -8.9; 2457 -7.5; 2703 -6.2; 2973 -4.7; 3270 -3.2; 3597 -0.9; 3957 -4.3; 4353 -4.6; 4788 -1.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 240 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 240 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.71 | -3.5 dB |
| Peaking | 152 Hz  | 0.91 | -4.6 dB |
| Peaking | 3545 Hz | 6.56 | 5.0 dB  |
| Peaking | 5597 Hz | 2.91 | 6.9 dB  |
| Peaking | 154 Hz  | 2.58 | 2.1 dB  |
| Peaking | 170 Hz  | 1.38 | -1.7 dB |
| Peaking | 346 Hz  | 4.57 | 1.6 dB  |
| Peaking | 1882 Hz | 2.67 | -3.5 dB |
| Peaking | 9140 Hz | 5.32 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20240%20Pro/Beyerdynamic%20DT%20240%20Pro.png)