# Skullcandy Push
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.2; 23 -15.1; 25 -15.0; 28 -14.9; 31 -14.8; 34 -14.6; 37 -14.5; 41 -14.3; 45 -14.2; 49 -14.1; 54 -14.0; 60 -14.0; 66 -14.0; 72 -14.1; 79 -14.2; 87 -14.2; 96 -14.2; 106 -14.0; 116 -13.6; 128 -13.2; 141 -12.8; 155 -12.2; 170 -11.6; 187 -10.8; 206 -10.1; 227 -9.3; 249 -8.6; 274 -7.9; 302 -7.2; 332 -6.6; 365 -5.9; 402 -5.3; 442 -4.6; 486 -4.0; 535 -3.2; 588 -2.5; 647 -1.8; 712 -1.2; 783 -0.8; 861 -0.5; 947 -0.7; 1042 -1.3; 1146 -2.2; 1261 -2.9; 1387 -3.2; 1526 -3.3; 1678 -3.5; 1846 -3.9; 2031 -4.3; 2234 -4.5; 2457 -4.0; 2703 -3.4; 2973 -2.7; 3270 -2.4; 3597 -2.7; 3957 -3.5; 4353 -4.7; 4788 -6.6; 5267 -8.1; 5793 -8.4; 6373 -7.0; 7010 -7.6; 7711 -9.8; 8482 -6.5; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Push GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Push ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.36 | -8.8 dB |
| Peaking | 114 Hz  | 0.59 | -6.4 dB |
| Peaking | 808 Hz  | 0.92 | 5.5 dB  |
| Peaking | 3552 Hz | 1.7  | 4.4 dB  |
| Peaking | 5663 Hz | 1.18 | -3.6 dB |
| Peaking | 6617 Hz | 8.05 | 2.3 dB  |
| Peaking | 7708 Hz | 4.37 | -4.0 dB |
| Peaking | 8847 Hz | 2.75 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.4 dB |
| Peaking | 62 Hz    | 1.41 | -6.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Push/Skullcandy%20Push.png)