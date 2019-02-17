# Beyerdynamic DT 880 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.4; 28 -1.9; 31 -2.3; 34 -2.6; 37 -2.9; 41 -3.2; 45 -3.2; 49 -3.1; 54 -3.4; 60 -3.7; 66 -4.4; 72 -4.6; 79 -4.7; 87 -5.4; 96 -6.0; 106 -6.2; 116 -6.4; 128 -6.9; 141 -7.1; 155 -7.3; 170 -7.6; 187 -7.7; 206 -7.7; 227 -7.7; 249 -7.7; 274 -7.6; 302 -7.5; 332 -7.3; 365 -7.1; 402 -7.0; 442 -6.8; 486 -6.3; 535 -6.4; 588 -6.2; 647 -6.2; 712 -6.1; 783 -6.1; 861 -6.2; 947 -6.0; 1042 -5.9; 1146 -5.4; 1261 -5.1; 1387 -5.3; 1526 -5.8; 1678 -6.1; 1846 -6.3; 2031 -6.0; 2234 -5.7; 2457 -5.4; 2703 -5.5; 2973 -6.0; 3270 -6.9; 3597 -7.4; 3957 -7.5; 4353 -6.0; 4788 -5.4; 5267 -8.4; 5793 -10.8; 6373 -10.4; 7010 -8.5; 7711 -10.4; 8482 -11.9; 9330 -11.2; 10263 -7.7; 11289 -6.0; 12418 -6.0; 13660 -6.4; 15026 -9.0; 16529 -9.5; 18182 -10.9; 20000 -15.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.73 | 5.7 dB  |
| Peaking | 55 Hz    | 1.34 | 1.7 dB  |
| Peaking | 208 Hz   | 0.85 | -1.9 dB |
| Peaking | 7892 Hz  | 1.58 | -5.0 dB |
| Peaking | 19762 Hz | 0.74 | -9.2 dB |
| Peaking | 1271 Hz  | 4.21 | 1.1 dB  |
| Peaking | 6018 Hz  | 4.63 | -5.8 dB |
| Peaking | 6815 Hz  | 1.63 | 4.0 dB  |
| Peaking | 8939 Hz  | 2.48 | -4.1 dB |
| Peaking | 11134 Hz | 2.33 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20880%20250%20Ohm/Beyerdynamic%20DT%20880%20250%20Ohm.png)