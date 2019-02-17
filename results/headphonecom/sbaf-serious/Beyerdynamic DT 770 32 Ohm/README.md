# Beyerdynamic DT 770 32 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.4; 25 -9.8; 28 -10.2; 31 -10.6; 34 -10.9; 37 -11.1; 41 -11.4; 45 -11.5; 49 -11.6; 54 -11.6; 60 -11.2; 66 -10.2; 72 -7.9; 79 -4.3; 87 -7.5; 96 -12.1; 106 -13.2; 116 -13.0; 128 -12.4; 141 -11.0; 155 -8.9; 170 -7.5; 187 -6.4; 206 -4.8; 227 -4.4; 249 -4.7; 274 -5.4; 302 -5.8; 332 -6.1; 365 -6.2; 402 -6.2; 442 -6.3; 486 -6.1; 535 -6.0; 588 -5.7; 647 -5.3; 712 -5.4; 783 -5.6; 861 -6.2; 947 -6.6; 1042 -6.5; 1146 -6.0; 1261 -5.9; 1387 -6.0; 1526 -6.5; 1678 -6.9; 1846 -7.3; 2031 -7.8; 2234 -8.3; 2457 -8.1; 2703 -6.8; 2973 -4.8; 3270 -2.4; 3597 -0.5; 3957 -1.3; 4353 -6.4; 4788 -7.9; 5267 -6.5; 5793 -8.5; 6373 -12.5; 7010 -11.6; 7711 -11.8; 8482 -13.1; 9330 -13.0; 10263 -10.7; 11289 -10.1; 12418 -10.6; 13660 -8.3; 15026 -6.5; 16529 -9.5; 18182 -12.9; 20000 -11.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 32 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 32 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 1.26 | -5.5 dB |
| Peaking | 116 Hz   | 3.28 | -7.0 dB |
| Peaking | 3661 Hz  | 4.19 | 8.0 dB  |
| Peaking | 8348 Hz  | 1.1  | -6.5 dB |
| Peaking | 18874 Hz | 1.21 | -7.2 dB |
| Peaking | 79 Hz    | 5.75 | 8.9 dB  |
| Peaking | 81 Hz    | 1.6  | -3.7 dB |
| Peaking | 225 Hz   | 3.41 | 2.8 dB  |
| Peaking | 1190 Hz  | 0.29 | 0.7 dB  |
| Peaking | 2216 Hz  | 2.75 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | 3.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20770%2032%20Ohm/Beyerdynamic%20DT%20770%2032%20Ohm.png)