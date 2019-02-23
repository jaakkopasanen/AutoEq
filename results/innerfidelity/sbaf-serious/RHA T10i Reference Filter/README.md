# RHA T10i Reference Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -14.0; 25 -14.3; 28 -14.6; 31 -14.7; 34 -14.8; 37 -14.9; 41 -15.1; 45 -15.2; 49 -15.2; 54 -15.2; 60 -15.3; 66 -15.4; 72 -15.5; 79 -15.5; 87 -15.7; 96 -15.7; 106 -15.5; 116 -15.3; 128 -15.2; 141 -15.0; 155 -14.8; 170 -14.4; 187 -14.0; 206 -13.5; 227 -12.9; 249 -12.4; 274 -11.8; 302 -11.1; 332 -10.5; 365 -9.7; 402 -9.1; 442 -8.3; 486 -7.9; 535 -7.3; 588 -6.3; 647 -5.8; 712 -5.7; 783 -5.1; 861 -4.6; 947 -4.4; 1042 -4.8; 1146 -5.2; 1261 -5.6; 1387 -6.4; 1526 -7.3; 1678 -8.2; 1846 -8.8; 2031 -9.3; 2234 -9.4; 2457 -8.3; 2703 -6.5; 2973 -4.4; 3270 -3.5; 3597 -3.6; 3957 -2.2; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.4; 9330 -11.9; 10263 -14.3; 11289 -10.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T10i Reference Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T10i Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.24 | -7.3 dB  |
| Peaking | 183 Hz   | 0.42 | -5.4 dB  |
| Peaking | 2126 Hz  | 0.89 | -14.0 dB |
| Peaking | 3160 Hz  | 0.26 | 12.0 dB  |
| Peaking | 9888 Hz  | 1.75 | -13.5 dB |
| Peaking | 3706 Hz  | 7.81 | -1.5 dB  |
| Peaking | 6669 Hz  | 2    | 2.2 dB   |
| Peaking | 7321 Hz  | 4.04 | -2.8 dB  |
| Peaking | 12118 Hz | 6.47 | 2.5 dB   |
| Peaking | 14927 Hz | 0.5  | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T10i%20Reference%20Filter/RHA%20T10i%20Reference%20Filter.png)