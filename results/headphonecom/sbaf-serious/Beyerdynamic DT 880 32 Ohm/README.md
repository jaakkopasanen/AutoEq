# Beyerdynamic DT 880 32 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.1; 31 -2.5; 34 -2.9; 37 -3.1; 41 -3.4; 45 -3.9; 49 -4.3; 54 -4.7; 60 -5.1; 66 -5.0; 72 -4.7; 79 -5.8; 87 -6.7; 96 -7.1; 106 -7.4; 116 -7.7; 128 -8.2; 141 -8.4; 155 -8.6; 170 -8.8; 187 -9.0; 206 -9.0; 227 -8.8; 249 -8.8; 274 -8.7; 302 -8.6; 332 -8.4; 365 -8.0; 402 -7.6; 442 -7.4; 486 -7.5; 535 -7.3; 588 -6.8; 647 -6.4; 712 -6.2; 783 -6.0; 861 -5.9; 947 -5.7; 1042 -5.6; 1146 -5.3; 1261 -4.9; 1387 -5.0; 1526 -5.8; 1678 -6.3; 1846 -6.8; 2031 -7.2; 2234 -6.9; 2457 -6.0; 2703 -5.7; 2973 -6.0; 3270 -6.9; 3597 -7.4; 3957 -7.9; 4353 -8.1; 4788 -7.7; 5267 -9.0; 5793 -12.4; 6373 -12.5; 7010 -11.1; 7711 -12.8; 8482 -15.4; 9330 -14.9; 10263 -9.4; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -7.7; 20000 -8.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 32 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 32 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.32 | 6.2 dB  |
| Peaking | 198 Hz   | 0.62 | -3.5 dB |
| Peaking | 6147 Hz  | 2.24 | -5.8 dB |
| Peaking | 8835 Hz  | 3.69 | -9.7 dB |
| Peaking | 20643 Hz | 1.06 | -7.7 dB |
| Peaking | 1264 Hz  | 2.47 | 1.2 dB  |
| Peaking | 1959 Hz  | 4.42 | -1.3 dB |
| Peaking | 4681 Hz  | 2.14 | -1.6 dB |
| Peaking | 5008 Hz  | 6.43 | 3.0 dB  |
| Peaking | 11455 Hz | 4.44 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | -8.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20880%2032%20Ohm/Beyerdynamic%20DT%20880%2032%20Ohm.png)