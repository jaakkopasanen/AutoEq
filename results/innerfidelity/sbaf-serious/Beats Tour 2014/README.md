# Beats Tour 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.7; 25 -13.0; 28 -13.3; 31 -13.6; 34 -13.8; 37 -14.0; 41 -14.2; 45 -14.4; 49 -14.6; 54 -14.8; 60 -15.0; 66 -15.2; 72 -15.4; 79 -15.6; 87 -15.8; 96 -16.0; 106 -16.0; 116 -15.9; 128 -15.9; 141 -15.8; 155 -15.6; 170 -15.3; 187 -14.9; 206 -14.6; 227 -14.0; 249 -13.6; 274 -13.0; 302 -12.4; 332 -11.8; 365 -11.2; 402 -10.5; 442 -9.8; 486 -9.3; 535 -8.7; 588 -7.8; 647 -7.3; 712 -6.9; 783 -6.4; 861 -6.4; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -6.8; 1387 -7.2; 1526 -7.6; 1678 -7.7; 1846 -7.4; 2031 -6.8; 2234 -6.2; 2457 -4.9; 2703 -3.9; 2973 -2.2; 3270 -0.8; 3597 -0.5; 3957 -1.1; 4353 -3.6; 4788 -5.0; 5267 -4.8; 5793 -4.1; 6373 -2.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Tour 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Tour 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 67 Hz    | 0.39 | -7.2 dB |
| Peaking | 196 Hz   | 0.65 | -4.8 dB |
| Peaking | 3570 Hz  | 2.09 | 6.3 dB  |
| Peaking | 21573 Hz | 2.4  | 1.3 dB  |
| Peaking | 23 Hz    | 0.87 | -2.5 dB |
| Peaking | 804 Hz   | 2.55 | 1.3 dB  |
| Peaking | 1715 Hz  | 2.89 | -1.6 dB |
| Peaking | 6541 Hz  | 4.16 | 5.5 dB  |
| Peaking | 6602 Hz  | 1.54 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.6 dB |
| Peaking | 62 Hz    | 1.41 | -6.5 dB |
| Peaking | 125 Hz   | 1.41 | -7.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Tour%202014/Beats%20Tour%202014.png)