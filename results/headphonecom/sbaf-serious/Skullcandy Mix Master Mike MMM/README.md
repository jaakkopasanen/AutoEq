# Skullcandy Mix Master Mike MMM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -2.5; 25 -3.5; 28 -4.7; 31 -5.6; 34 -6.2; 37 -6.5; 41 -6.8; 45 -7.1; 49 -7.4; 54 -7.5; 60 -7.6; 66 -7.6; 72 -7.6; 79 -7.8; 87 -8.3; 96 -8.7; 106 -9.0; 116 -9.1; 128 -9.3; 141 -9.5; 155 -9.9; 170 -9.7; 187 -10.2; 206 -10.3; 227 -10.2; 249 -9.8; 274 -9.1; 302 -9.4; 332 -8.6; 365 -8.2; 402 -8.5; 442 -7.9; 486 -7.4; 535 -6.7; 588 -6.3; 647 -6.5; 712 -6.6; 783 -6.8; 861 -7.2; 947 -7.8; 1042 -7.6; 1146 -8.2; 1261 -8.9; 1387 -9.7; 1526 -10.5; 1678 -10.5; 1846 -9.4; 2031 -8.7; 2234 -7.4; 2457 -5.5; 2703 -3.6; 2973 -2.4; 3270 -2.3; 3597 -5.5; 3957 -8.7; 4353 -6.2; 4788 -4.0; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Mix Master Mike MMM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Mix Master Mike MMM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.42 | 5.4 dB  |
| Peaking | 178 Hz  | 0.68 | -3.7 dB |
| Peaking | 1614 Hz | 1.98 | -4.3 dB |
| Peaking | 2959 Hz | 4.36 | 5.1 dB  |
| Peaking | 5867 Hz | 3.66 | 6.9 dB  |
| Peaking | 611 Hz  | 3.79 | 1.1 dB  |
| Peaking | 3418 Hz | 7.28 | 3.1 dB  |
| Peaking | 3882 Hz | 4.87 | -4.2 dB |
| Peaking | 4981 Hz | 3.85 | 1.3 dB  |
| Peaking | 8232 Hz | 4.66 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Mix%20Master%20Mike%20MMM/Skullcandy%20Mix%20Master%20Mike%20MMM.png)