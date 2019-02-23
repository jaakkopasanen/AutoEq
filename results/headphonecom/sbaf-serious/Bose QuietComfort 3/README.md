# Bose QuietComfort 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -12.0; 25 -12.1; 28 -12.2; 31 -12.2; 34 -12.2; 37 -12.1; 41 -11.9; 45 -11.8; 49 -11.7; 54 -11.6; 60 -11.5; 66 -11.7; 72 -11.7; 79 -11.9; 87 -12.1; 96 -12.3; 106 -12.3; 116 -12.5; 128 -12.5; 141 -12.5; 155 -12.5; 170 -12.2; 187 -12.0; 206 -11.6; 227 -11.1; 249 -10.6; 274 -10.2; 302 -9.7; 332 -9.2; 365 -8.8; 402 -8.5; 442 -8.2; 486 -8.1; 535 -7.9; 588 -7.7; 647 -7.9; 712 -8.0; 783 -8.0; 861 -7.6; 947 -7.4; 1042 -7.7; 1146 -8.0; 1261 -8.2; 1387 -8.0; 1526 -6.6; 1678 -6.1; 1846 -4.3; 2031 -2.8; 2234 -1.6; 2457 -1.5; 2703 -1.2; 2973 -1.6; 3270 -2.0; 3597 -3.4; 3957 -5.0; 4353 -6.1; 4788 -3.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.49 | -5.1 dB |
| Peaking | 147 Hz  | 0.56 | -5.4 dB |
| Peaking | 1307 Hz | 1.4  | -2.4 dB |
| Peaking | 2492 Hz | 1.52 | 6.1 dB  |
| Peaking | 5787 Hz | 3.41 | 6.3 dB  |
| Peaking | 3328 Hz | 5.86 | 1.3 dB  |
| Peaking | 4313 Hz | 4.85 | -2.5 dB |
| Peaking | 5005 Hz | 9.1  | 2.5 dB  |
| Peaking | 8308 Hz | 4.38 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Bose%20QuietComfort%203/Bose%20QuietComfort%203.png)