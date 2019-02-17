# Skullcandy Mix Master Mike MMM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.7; 25 -2.7; 28 -3.9; 31 -4.8; 34 -5.4; 37 -5.7; 41 -6.0; 45 -6.3; 49 -6.5; 54 -6.7; 60 -6.8; 66 -6.8; 72 -6.7; 79 -7.0; 87 -7.5; 96 -7.9; 106 -8.2; 116 -8.2; 128 -8.4; 141 -8.7; 155 -9.1; 170 -8.9; 187 -9.3; 206 -9.5; 227 -9.4; 249 -8.9; 274 -8.3; 302 -8.6; 332 -7.8; 365 -7.3; 402 -7.7; 442 -7.1; 486 -6.6; 535 -5.9; 588 -5.5; 647 -5.6; 712 -5.8; 783 -5.9; 861 -6.4; 947 -7.0; 1042 -6.7; 1146 -7.4; 1261 -8.0; 1387 -8.9; 1526 -9.7; 1678 -9.6; 1846 -8.6; 2031 -7.8; 2234 -6.6; 2457 -4.7; 2703 -2.8; 2973 -1.6; 3270 -1.5; 3597 -4.7; 3957 -7.9; 4353 -5.4; 4788 -3.2; 5267 -1.0; 5793 -0.8; 6373 -1.3; 7010 -4.2; 7711 -6.4; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Mix Master Mike MMM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Mix Master Mike MMM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.73 | 6.7 dB  |
| Peaking | 184 Hz  | 1.09 | -2.8 dB |
| Peaking | 1622 Hz | 2.89 | -3.6 dB |
| Peaking | 2975 Hz | 3.84 | 5.8 dB  |
| Peaking | 5778 Hz | 3.26 | 6.7 dB  |
| Peaking | 21 Hz   | 1.51 | 0.6 dB  |
| Peaking | 632 Hz  | 2.73 | 1.6 dB  |
| Peaking | 3891 Hz | 2.45 | 2.4 dB  |
| Peaking | 3928 Hz | 6.48 | -5.7 dB |
| Peaking | 8238 Hz | 4.29 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Mix%20Master%20Mike%20MMM/Skullcandy%20Mix%20Master%20Mike%20MMM.png)