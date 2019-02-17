# JVC HA FR301
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -10.3; 25 -10.7; 28 -11.2; 31 -11.6; 34 -11.9; 37 -12.2; 41 -12.6; 45 -12.8; 49 -13.1; 54 -13.4; 60 -13.7; 66 -14.0; 72 -14.3; 79 -14.6; 87 -14.8; 96 -15.1; 106 -15.2; 116 -15.2; 128 -15.2; 141 -15.2; 155 -15.0; 170 -14.8; 187 -14.5; 206 -14.1; 227 -13.5; 249 -13.0; 274 -12.3; 302 -11.6; 332 -10.8; 365 -9.9; 402 -9.0; 442 -7.9; 486 -7.2; 535 -6.1; 588 -4.7; 647 -3.8; 712 -3.0; 783 -1.9; 861 -1.3; 947 -0.8; 1042 -0.6; 1146 -0.5; 1261 -0.7; 1387 -1.2; 1526 -2.0; 1678 -2.5; 1846 -2.9; 2031 -3.2; 2234 -3.7; 2457 -4.2; 2703 -5.5; 2973 -6.7; 3270 -7.4; 3597 -7.8; 3957 -8.7; 4353 -11.4; 4788 -13.1; 5267 -11.2; 5793 -7.6; 6373 -4.9; 7010 -4.0; 7711 -5.1; 8482 -7.3; 9330 -7.7; 10263 -4.4; 11289 -0.7; 12418 -0.7; 13660 -1.0; 15026 -6.0; 16529 -4.5; 18182 -0.8; 20000 -1.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA FR301 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA FR301 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 47 Hz    | 0.29 | -11.1 dB |
| Peaking | 160 Hz   | 0.7  | -7.6 dB  |
| Peaking | 335 Hz   | 1.28 | -4.6 dB  |
| Peaking | 4670 Hz  | 1.15 | -11.0 dB |
| Peaking | 15656 Hz | 2.88 | -5.7 dB  |
| Peaking | 1065 Hz  | 2.35 | 2.0 dB   |
| Peaking | 2829 Hz  | 3.91 | -0.9 dB  |
| Peaking | 6801 Hz  | 3.82 | 3.8 dB   |
| Peaking | 9332 Hz  | 2.35 | -6.8 dB  |
| Peaking | 10947 Hz | 2.08 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.1 dB |
| Peaking | 62 Hz    | 1.41 | -9.6 dB  |
| Peaking | 125 Hz   | 1.41 | -11.8 dB |
| Peaking | 250 Hz   | 1.41 | -10.2 dB |
| Peaking | 500 Hz   | 1.41 | -4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -9.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB  |
| Peaking | 16000 Hz | 1.41 | -3.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20HA%20FR301/JVC%20HA%20FR301.png)