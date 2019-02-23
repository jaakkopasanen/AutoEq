# Beyerdynamic DT 770 600 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.3; 45 -2.4; 49 -3.2; 54 -2.9; 60 -2.6; 66 -4.6; 72 -6.0; 79 -4.7; 87 -2.3; 96 -4.3; 106 -6.1; 116 -7.0; 128 -7.9; 141 -8.5; 155 -8.6; 170 -8.2; 187 -9.0; 206 -8.9; 227 -8.7; 249 -8.4; 274 -8.2; 302 -7.9; 332 -7.6; 365 -7.3; 402 -7.1; 442 -6.8; 486 -6.4; 535 -6.0; 588 -5.9; 647 -5.6; 712 -5.0; 783 -4.6; 861 -4.9; 947 -5.1; 1042 -4.6; 1146 -4.0; 1261 -4.2; 1387 -4.9; 1526 -5.3; 1678 -5.7; 1846 -5.8; 2031 -5.6; 2234 -5.9; 2457 -6.9; 2703 -6.0; 2973 -4.2; 3270 -2.1; 3597 -0.5; 3957 -0.5; 4353 -1.8; 4788 -0.5; 5267 -8.7; 5793 -11.6; 6373 -11.1; 7010 -7.6; 7711 -9.7; 8482 -13.9; 9330 -13.0; 10263 -6.9; 11289 -6.5; 12418 -7.1; 13660 -7.4; 15026 -6.5; 16529 -7.0; 18182 -10.9; 20000 -12.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 600 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 600 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 1.24 | 5.4 dB   |
| Peaking | 42 Hz   | 1.34 | 3.6 dB   |
| Peaking | 4666 Hz | 1.49 | 10.6 dB  |
| Peaking | 5693 Hz | 3.09 | -12.8 dB |
| Peaking | 8757 Hz | 4.19 | -9.1 dB  |
| Peaking | 88 Hz   | 5.57 | 4.3 dB   |
| Peaking | 195 Hz  | 0.78 | -2.7 dB  |
| Peaking | 1020 Hz | 0.82 | 2.2 dB   |
| Peaking | 2710 Hz | 1.53 | -2.6 dB  |
| Peaking | 3383 Hz | 4.36 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20770%20600%20Ohm/Beyerdynamic%20DT%20770%20600%20Ohm.png)