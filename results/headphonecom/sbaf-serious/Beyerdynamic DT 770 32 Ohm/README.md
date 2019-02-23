# Beyerdynamic DT 770 32 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.7; 25 -9.1; 28 -9.6; 31 -9.9; 34 -10.2; 37 -10.4; 41 -10.7; 45 -10.9; 49 -11.0; 54 -10.9; 60 -10.5; 66 -9.5; 72 -7.2; 79 -3.6; 87 -6.8; 96 -11.5; 106 -12.5; 116 -12.3; 128 -11.7; 141 -10.3; 155 -8.2; 170 -6.8; 187 -5.7; 206 -4.1; 227 -3.7; 249 -4.0; 274 -4.7; 302 -5.2; 332 -5.4; 365 -5.6; 402 -5.5; 442 -5.6; 486 -5.5; 535 -5.3; 588 -5.1; 647 -4.6; 712 -4.7; 783 -4.9; 861 -5.5; 947 -5.9; 1042 -5.8; 1146 -5.3; 1261 -5.2; 1387 -5.3; 1526 -5.8; 1678 -6.2; 1846 -6.6; 2031 -7.1; 2234 -7.6; 2457 -7.4; 2703 -6.1; 2973 -4.2; 3270 -1.7; 3597 -0.5; 3957 -0.9; 4353 -5.7; 4788 -7.2; 5267 -5.8; 5793 -7.8; 6373 -11.8; 7010 -10.9; 7711 -11.1; 8482 -12.5; 9330 -12.3; 10263 -10.0; 11289 -9.4; 12418 -9.9; 13660 -7.6; 15026 -6.5; 16529 -8.8; 18182 -12.3; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 32 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 32 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 1.48 | -4.9 dB |
| Peaking | 115 Hz   | 3.7  | -6.5 dB |
| Peaking | 3642 Hz  | 3.5  | 7.6 dB  |
| Peaking | 8349 Hz  | 1.25 | -6.0 dB |
| Peaking | 18860 Hz | 1.27 | -6.5 dB |
| Peaking | 232 Hz   | 3.08 | 3.2 dB  |
| Peaking | 646 Hz   | 1.35 | 1.7 dB  |
| Peaking | 1320 Hz  | 3.78 | 1.1 dB  |
| Peaking | 2288 Hz  | 4.41 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | 3.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.3 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20770%2032%20Ohm/Beyerdynamic%20DT%20770%2032%20Ohm.png)