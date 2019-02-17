# Sol Republic Master Tracks XC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.3; 25 -6.7; 28 -7.2; 31 -7.6; 34 -7.9; 37 -8.2; 41 -8.4; 45 -8.7; 49 -8.8; 54 -9.0; 60 -9.1; 66 -9.3; 72 -9.3; 79 -9.6; 87 -9.7; 96 -9.9; 106 -10.2; 116 -10.8; 128 -11.3; 141 -11.3; 155 -11.5; 170 -11.1; 187 -11.5; 206 -11.4; 227 -11.1; 249 -10.8; 274 -10.5; 302 -10.0; 332 -9.3; 365 -8.3; 402 -7.5; 442 -7.5; 486 -8.2; 535 -7.8; 588 -7.2; 647 -7.0; 712 -6.9; 783 -6.8; 861 -6.8; 947 -6.5; 1042 -6.4; 1146 -6.2; 1261 -5.5; 1387 -5.3; 1526 -4.9; 1678 -4.3; 1846 -3.2; 2031 -1.7; 2234 -0.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -3.7; 4788 -5.7; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sol Republic Master Tracks XC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sol Republic Master Tracks XC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 1.43 | -1.2 dB |
| Peaking | 181 Hz  | 0.52 | -5.0 dB |
| Peaking | 405 Hz  | 3.14 | 1.6 dB  |
| Peaking | 2794 Hz | 1.14 | 6.7 dB  |
| Peaking | 5947 Hz | 4.39 | 5.4 dB  |
| Peaking | 647 Hz  | 4.87 | 0.6 dB  |
| Peaking | 4241 Hz | 0.17 | -0.3 dB |
| Peaking | 4571 Hz | 2.22 | 3.5 dB  |
| Peaking | 4686 Hz | 6.61 | -6.1 dB |
| Peaking | 8135 Hz | 3.89 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sol%20Republic%20Master%20Tracks%20XC/Sol%20Republic%20Master%20Tracks%20XC.png)