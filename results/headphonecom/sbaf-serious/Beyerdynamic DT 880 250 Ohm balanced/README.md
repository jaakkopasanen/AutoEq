# Beyerdynamic DT 880 250 Ohm balanced
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.8; 60 -1.3; 66 -1.3; 72 -1.4; 79 -2.5; 87 -3.8; 96 -4.5; 106 -5.2; 116 -5.7; 128 -6.4; 141 -7.0; 155 -7.6; 170 -7.9; 187 -8.3; 206 -8.5; 227 -8.5; 249 -8.6; 274 -8.7; 302 -8.6; 332 -8.2; 365 -8.0; 402 -7.6; 442 -7.4; 486 -6.4; 535 -6.6; 588 -6.3; 647 -5.9; 712 -5.7; 783 -5.5; 861 -5.4; 947 -5.1; 1042 -4.9; 1146 -4.2; 1261 -3.7; 1387 -3.9; 1526 -4.5; 1678 -5.0; 1846 -5.5; 2031 -5.3; 2234 -5.1; 2457 -4.7; 2703 -5.2; 2973 -5.9; 3270 -6.1; 3597 -5.6; 3957 -4.9; 4353 -4.0; 4788 -4.5; 5267 -6.2; 5793 -8.7; 6373 -9.1; 7010 -7.7; 7711 -8.4; 8482 -10.1; 9330 -9.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 250 Ohm balanced GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 250 Ohm balanced ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.78 | 7.1 dB  |
| Peaking | 1304 Hz | 1.81 | 2.7 dB  |
| Peaking | 4887 Hz | 1.66 | 3.4 dB  |
| Peaking | 5954 Hz | 3.1  | -4.7 dB |
| Peaking | 8720 Hz | 4.62 | -4.1 dB |
| Peaking | 37 Hz   | 3.5  | -1.4 dB |
| Peaking | 71 Hz   | 2.43 | 2.3 dB  |
| Peaking | 226 Hz  | 1.02 | -2.7 dB |
| Peaking | 2472 Hz | 4.48 | 1.2 dB  |
| Peaking | 3239 Hz | 5.29 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20880%20250%20Ohm%20balanced/Beyerdynamic%20DT%20880%20250%20Ohm%20balanced.png)