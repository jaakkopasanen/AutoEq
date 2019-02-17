# Beyerdynamic DT 880 250 Ohm balanced
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.3; 49 -1.7; 54 -2.3; 60 -2.8; 66 -2.8; 72 -2.8; 79 -4.0; 87 -5.2; 96 -6.0; 106 -6.6; 116 -7.2; 128 -7.9; 141 -8.5; 155 -9.0; 170 -9.3; 187 -9.7; 206 -10.0; 227 -10.0; 249 -10.0; 274 -10.2; 302 -10.0; 332 -9.7; 365 -9.4; 402 -9.1; 442 -8.8; 486 -7.8; 535 -8.0; 588 -7.8; 647 -7.3; 712 -7.2; 783 -7.0; 861 -6.9; 947 -6.6; 1042 -6.3; 1146 -5.7; 1261 -5.2; 1387 -5.4; 1526 -6.0; 1678 -6.5; 1846 -6.9; 2031 -6.8; 2234 -6.6; 2457 -6.2; 2703 -6.7; 2973 -7.4; 3270 -7.6; 3597 -7.1; 3957 -6.3; 4353 -5.5; 4788 -6.0; 5267 -7.7; 5793 -10.1; 6373 -10.6; 7010 -9.2; 7711 -9.8; 8482 -11.5; 9330 -10.9; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 250 Ohm balanced GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 250 Ohm balanced ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.33 | 6.5 dB  |
| Peaking | 200 Hz   | 0.56 | -4.8 dB |
| Peaking | 1260 Hz  | 2.99 | 1.7 dB  |
| Peaking | 7918 Hz  | 1.72 | -4.5 dB |
| Peaking | 22050 Hz | 2.2  | -2.8 dB |
| Peaking | 3270 Hz  | 6.68 | -0.8 dB |
| Peaking | 4614 Hz  | 2.59 | 3.6 dB  |
| Peaking | 7209 Hz  | 1.22 | -6.3 dB |
| Peaking | 7377 Hz  | 3.52 | 7.2 dB  |
| Peaking | 10859 Hz | 2.1  | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20880%20250%20Ohm%20balanced/Beyerdynamic%20DT%20880%20250%20Ohm%20balanced.png)