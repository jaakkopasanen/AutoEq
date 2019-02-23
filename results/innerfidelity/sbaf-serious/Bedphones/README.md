# Bedphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -1.1; 116 -2.4; 128 -3.9; 141 -5.4; 155 -6.8; 170 -8.0; 187 -9.1; 206 -10.1; 227 -10.9; 249 -11.6; 274 -12.1; 302 -12.4; 332 -12.8; 365 -12.9; 402 -13.0; 442 -12.9; 486 -13.1; 535 -13.0; 588 -12.4; 647 -12.7; 712 -13.1; 783 -13.1; 861 -13.4; 947 -13.7; 1042 -13.8; 1146 -13.9; 1261 -14.1; 1387 -14.3; 1526 -14.3; 1678 -13.5; 1846 -11.7; 2031 -9.7; 2234 -7.5; 2457 -4.8; 2703 -2.7; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -4.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bedphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bedphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 82 Hz   | 0.28 | 9.1 dB   |
| Peaking | 265 Hz  | 0.54 | -10.3 dB |
| Peaking | 1575 Hz | 0.65 | -9.6 dB  |
| Peaking | 3071 Hz | 1.15 | 11.3 dB  |
| Peaking | 5902 Hz | 3.57 | 5.1 dB   |
| Peaking | 19 Hz   | 1.09 | 2.6 dB   |
| Peaking | 58 Hz   | 0.42 | -1.4 dB  |
| Peaking | 100 Hz  | 2.53 | 2.3 dB   |
| Peaking | 6878 Hz | 2.61 | 2.3 dB   |
| Peaking | 7605 Hz | 2.46 | -2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.7 dB  |
| Peaking | 125 Hz   | 1.41 | 3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -5.8 dB |
| Peaking | 500 Hz   | 1.41 | -4.5 dB |
| Peaking | 1000 Hz  | 1.41 | -7.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bedphones/Bedphones.png)