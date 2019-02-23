# T-Peos U200R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -10.7; 25 -10.7; 28 -10.7; 31 -10.7; 34 -10.7; 37 -10.6; 41 -10.6; 45 -10.6; 49 -10.7; 54 -10.8; 60 -10.9; 66 -10.9; 72 -11.1; 79 -11.3; 87 -11.4; 96 -11.7; 106 -11.7; 116 -11.7; 128 -11.8; 141 -11.8; 155 -11.7; 170 -11.6; 187 -11.4; 206 -11.2; 227 -10.9; 249 -10.6; 274 -10.1; 302 -9.7; 332 -9.2; 365 -8.7; 402 -8.3; 442 -7.6; 486 -7.2; 535 -6.7; 588 -5.9; 647 -5.5; 712 -5.2; 783 -4.8; 861 -4.9; 947 -5.1; 1042 -5.4; 1146 -5.7; 1261 -5.9; 1387 -6.7; 1526 -7.5; 1678 -8.0; 1846 -8.0; 2031 -7.5; 2234 -6.5; 2457 -4.2; 2703 -2.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -5.0; 4788 -10.1; 5267 -8.1; 5793 -2.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos U200R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos U200R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.26 | -4.1 dB |
| Peaking | 174 Hz  | 0.86 | -3.6 dB |
| Peaking | 3481 Hz | 2.18 | 7.3 dB  |
| Peaking | 4927 Hz | 5.25 | -7.5 dB |
| Peaking | 6144 Hz | 4.73 | 6.4 dB  |
| Peaking | 357 Hz  | 1.56 | -1.0 dB |
| Peaking | 830 Hz  | 0.98 | 2.3 dB  |
| Peaking | 1849 Hz | 1.7  | -3.0 dB |
| Peaking | 2722 Hz | 4.68 | 2.4 dB  |
| Peaking | 9212 Hz | 3.21 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20U200R/T-Peos%20U200R.png)