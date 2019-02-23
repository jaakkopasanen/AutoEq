# Skullcandy Mix Master
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -3.1; 25 -3.8; 28 -4.7; 31 -5.3; 34 -5.8; 37 -6.1; 41 -6.5; 45 -6.7; 49 -6.9; 54 -7.1; 60 -7.1; 66 -7.2; 72 -7.2; 79 -7.6; 87 -8.1; 96 -8.5; 106 -8.7; 116 -8.8; 128 -9.2; 141 -9.4; 155 -9.7; 170 -9.5; 187 -9.8; 206 -10.0; 227 -9.9; 249 -9.7; 274 -9.2; 302 -8.8; 332 -8.8; 365 -8.3; 402 -8.4; 442 -8.0; 486 -7.5; 535 -6.7; 588 -5.9; 647 -5.7; 712 -5.9; 783 -6.0; 861 -6.8; 947 -7.3; 1042 -7.4; 1146 -7.5; 1261 -8.3; 1387 -9.5; 1526 -10.2; 1678 -10.4; 1846 -9.4; 2031 -8.8; 2234 -7.4; 2457 -5.5; 2703 -3.8; 2973 -2.5; 3270 -1.9; 3597 -5.4; 3957 -8.8; 4353 -6.6; 4788 -4.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Mix Master GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Mix Master ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.82 | 4.3 dB  |
| Peaking | 182 Hz  | 0.76 | -3.5 dB |
| Peaking | 1642 Hz | 2.36 | -4.3 dB |
| Peaking | 3015 Hz | 4.6  | 5.0 dB  |
| Peaking | 5815 Hz | 3.57 | 7.0 dB  |
| Peaking | 609 Hz  | 0.91 | -2.3 dB |
| Peaking | 650 Hz  | 1.67 | 3.7 dB  |
| Peaking | 3843 Hz | 2.14 | 2.7 dB  |
| Peaking | 3951 Hz | 5.5  | -6.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Mix%20Master/Skullcandy%20Mix%20Master.png)