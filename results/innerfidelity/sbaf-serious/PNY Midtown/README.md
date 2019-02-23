# PNY Midtown
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.0; 23 -14.0; 25 -14.0; 28 -14.0; 31 -13.9; 34 -13.9; 37 -13.9; 41 -13.8; 45 -13.8; 49 -13.8; 54 -13.8; 60 -13.8; 66 -13.8; 72 -13.8; 79 -13.9; 87 -13.9; 96 -14.0; 106 -13.8; 116 -13.6; 128 -13.5; 141 -13.2; 155 -13.0; 170 -12.6; 187 -12.1; 206 -11.7; 227 -11.1; 249 -10.7; 274 -10.1; 302 -9.5; 332 -8.8; 365 -8.2; 402 -7.5; 442 -6.8; 486 -6.2; 535 -5.8; 588 -4.8; 647 -4.5; 712 -4.0; 783 -3.4; 861 -3.4; 947 -3.8; 1042 -3.3; 1146 -3.2; 1261 -3.6; 1387 -4.3; 1526 -5.1; 1678 -6.1; 1846 -7.4; 2031 -8.1; 2234 -8.0; 2457 -7.2; 2703 -5.1; 2973 -1.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -1.9; 5267 -3.9; 5793 -8.3; 6373 -11.8; 7010 -6.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PNY Midtown GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PNY Midtown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 58 Hz   | 0.12 | -7.7 dB |
| Peaking | 836 Hz  | 0.44 | 5.3 dB  |
| Peaking | 2208 Hz | 1.52 | -7.4 dB |
| Peaking | 3572 Hz | 1.14 | 7.8 dB  |
| Peaking | 6220 Hz | 6.07 | -8.6 dB |
| Peaking | 41 Hz   | 0.43 | -0.9 dB |
| Peaking | 47 Hz   | 0.89 | 1.3 dB  |
| Peaking | 3767 Hz | 5.64 | -1.6 dB |
| Peaking | 3951 Hz | 2.07 | 0.9 dB  |
| Peaking | 9703 Hz | 2.01 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PNY%20Midtown/PNY%20Midtown.png)